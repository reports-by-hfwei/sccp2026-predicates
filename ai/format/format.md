# SCCP2026 Beamer formatting conventions

## Slide design

- Use the current SimplePlus Beamer theme and preserve the root document's
  packages, notation macros, bibliography configuration, and title metadata.
- Keep each frame focused on one claim.  Prefer figures, small TikZ diagrams,
  formulas, keywords, and short phrases over prose paragraphs.
- Use the corresponding heading in `draft/draft.md` verbatim as the frame title.
- Make the narrative cumulative: each slide should answer or motivate the next.
- Use examples when they make an abstract predicate or dependency concept easier
  to understand.  Avoid implementation-level detail in this short-talk deck.

## Source structure

- Keep content frames in `sections/*.tex`; include them from
  `sccp2026-predicates.tex` in presentation order.
- Indent nested environments by two spaces and place long options, node styles,
  formulas, and table rows on separate logical lines.
- Use `\column{0.45\textwidth}` inside a `columns` environment.  Do not use
  `\begin{column}{...}` / `\end{column}` pairs.
- Prefer explicit `\begin{center}` / `\end{center}` blocks over a bare
  `\centering`.  A `table` or `figure` environment may use `\centering`.
- Use `\begin{tabular}` with `booktabs` rules for tables; do not use vertical
  rules or excessive cell decoration.

## Reusable commands and visuals

- Define reusable commands in `newcommands.tex`; do not duplicate them in
  individual section files.
- Include a figure as `\fig{<width factor>}{<path>}`.  The width factor is the
  numeric multiplier of the local `\linewidth`, e.g.,
  `\fig{.70}{figs/example.png}`.
- Use semantic color helpers from `newcommands.tex`: `\blue{...}` for primary
  concepts, `\red{...}` for contrasts or open questions, `\green{...}` for
  positive highlights, and `\gray{...}` for secondary text.
- Place citations with `\ncite{...}` at the lower right of a frame.  Preserve
  existing bibliography keys and never invent a citation.
- Prefer supplied figures.  If a new diagram is necessary, use TikZ source in
  `tikz/`, compile it to PDF, copy the PDF to `figs/`, and include it with
  `\fig`.

## Validation and delivery

- Compile `sccp2026-predicates.tex` after every `.tex` update and commit the
  generated PDF with the source changes.
- Check the log for errors, undefined citations, undefined references, and
  overfull boxes.  Render and inspect changed slides when layout is affected.
- Preserve user changes and unrelated untracked files.  Push the completed
  change set after verification.
