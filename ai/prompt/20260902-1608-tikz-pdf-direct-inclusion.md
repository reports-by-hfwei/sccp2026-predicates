# Prompt: Include TikZ PDFs directly

Revise the SCCP2026 Beamer repository so a standalone TikZ figure's generated
PDF remains beside its source in `tikz/`.  Update every affected `\fig` call to
reference `tikz/<name>.pdf` directly, compile the standalone sources into that
directory, and remove duplicate generated PDFs from `figs/`.  Update
`ai/format/format.md` to make direct inclusion the required workflow.  Preserve
unrelated user changes, compile and verify the main deck, commit the source and
generated TikZ PDFs, then push the focused change set.
