#!/usr/bin/env python3
"""Incrementally build the SCCP 2026 predicates presentation.

The script intentionally uses only Python's standard library.  It first
rebuilds changed standalone TikZ figures, then rebuilds the presentation.
Git supplies the change set so generated PDFs and auxiliary files do not
trigger needless figure builds.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MAIN_TEX = ROOT / "sccp2026-predicates.tex"
TIKZ_DIR = ROOT / "tikz"
BIB_FILE = ROOT / "predicates.bib"

# Keep the .bbl file: biblatex reads it on later incremental builds when the
# bibliography itself has not changed.  The remaining files are diagnostics or
# bookkeeping that pdflatex/biber can regenerate.
AUXILIARY_SUFFIXES = (
    ".aux",
    ".bcf",
    ".blg",
    ".fdb_latexmk",
    ".fls",
    ".log",
    ".nav",
    ".out",
    ".run.xml",
    ".snm",
    ".synctex.gz",
    ".toc",
)


def run(command: list[str], *, cwd: Path = ROOT) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def git_output(*arguments: str) -> set[Path]:
    """Return repository-relative paths printed by a Git command."""
    completed = subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {Path(line) for line in completed.stdout.splitlines() if line}


def changed_paths(directory: str) -> set[Path]:
    """Find tracked modifications and untracked files below *directory*."""
    changed = git_output("diff", "--name-only", "HEAD", "--", directory)
    untracked = git_output(
        "ls-files", "--others", "--exclude-standard", "--", directory
    )
    return changed | untracked


def remove_auxiliaries(tex_file: Path) -> None:
    """Remove temporary products for one TeX source, preserving its PDF/.bbl."""
    stem = tex_file.with_suffix("")
    for suffix in AUXILIARY_SUFFIXES:
        (stem.with_suffix(suffix)).unlink(missing_ok=True)
    # Biber may leave these after an interrupted update on Windows.
    for suffix in (".bbl-SAVE-ERROR", ".bcf-SAVE-ERROR"):
        (stem.with_suffix(suffix)).unlink(missing_ok=True)


def build_tikz_figures() -> None:
    figures = sorted(
        path
        for path in changed_paths("tikz")
        if path.suffix == ".tex" and (ROOT / path).is_file()
    )
    if not figures:
        print("No changed TikZ sources.")
        return

    for relative_path in figures:
        tex_file = ROOT / relative_path
        try:
            run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    tex_file.name,
                ],
                cwd=tex_file.parent,
            )
        finally:
            remove_auxiliaries(tex_file)


def bibliography_tool() -> str:
    """Use the bibliography backend declared by the presentation source."""
    source = MAIN_TEX.read_text(encoding="utf-8")
    backend = re.search(r"backend\s*=\s*([^,\]]+)", source)
    return "biber" if backend and backend.group(1).strip() == "biber" else "bibtex"


def bibliography_changed() -> bool:
    return Path("predicates.bib") in changed_paths("predicates.bib")


def build_presentation() -> None:
    job_name = MAIN_TEX.stem
    pdf_latex = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        MAIN_TEX.name,
    ]
    must_refresh_bibliography = bibliography_changed() or not (
        ROOT / f"{job_name}.bbl"
    ).exists()

    try:
        run(pdf_latex)
        if must_refresh_bibliography:
            tool = bibliography_tool()
            print(f"Refreshing bibliography with {tool}.")
            run([tool, job_name])
        else:
            print("Bibliography unchanged; using the existing .bbl file.")
        run(pdf_latex)
        if must_refresh_bibliography:
            run(pdf_latex)
    finally:
        remove_auxiliaries(MAIN_TEX)


def main() -> int:
    for executable in ("git", "pdflatex"):
        if shutil.which(executable) is None:
            print(f"Required executable not found: {executable}", file=sys.stderr)
            return 1

    if not MAIN_TEX.is_file() or not BIB_FILE.is_file() or not TIKZ_DIR.is_dir():
        print("Expected project files are missing.", file=sys.stderr)
        return 1

    try:
        build_tikz_figures()
        if bibliography_changed() or not (ROOT / f"{MAIN_TEX.stem}.bbl").exists():
            tool = bibliography_tool()
            if shutil.which(tool) is None:
                print(f"Required bibliography executable not found: {tool}", file=sys.stderr)
                return 1
        build_presentation()
    except subprocess.CalledProcessError as error:
        print(f"Build failed with exit code {error.returncode}.", file=sys.stderr)
        return error.returncode or 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
