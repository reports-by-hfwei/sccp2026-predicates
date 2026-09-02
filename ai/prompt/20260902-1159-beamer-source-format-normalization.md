# Beamer source format normalization

Normalize the TeX files under `sections/` for the SCCP2026 Beamer report.  Use
the concise Beamer column command, for example `\column{0.45\textwidth}`, in
place of `column` environments.  Prefer explicit `center` environments to bare
`\centering`, except in conventional `table` or `figure` contexts.  Preserve
the slide content, macros, citations, and visual layout; update the project
format guide with the current enduring conventions, compile the root document,
check for diagnostics, and commit the source and PDF.
