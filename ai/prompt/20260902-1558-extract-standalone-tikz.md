# Prompt: Extract standalone TikZ figures

Refactor every TikZ diagram embedded in `sections/*.tex` into its own
independently compilable source under `tikz/`.  Use the `standalone` document
class, preserve the diagram's content and visual semantics, compile each source
to a PDF, copy the PDF to `figs/`, and replace the original in-frame TikZ code
with the reusable `\fig{<width>}{figs/<name>.pdf}` command.  Keep slide titles
and non-figure content unchanged.  Apply the Beamer conventions in
`ai/format/format.md`, including readable TikZ option lists such as
`align = center` and `-Latex, very thick`.  Update the formatting guide with
the standalone-TikZ workflow, compile the main deck, inspect diagnostics and
changed slide layout, then commit and push only task-related files while
preserving unrelated working-tree changes.
