# LaTeX figure and color macro cleanup

For the SCCP2026 Beamer source, define a two-argument `\fig` macro in
`newcommands.tex`: the first argument is the numeric factor before
`\linewidth`, and the second is the figure path.  Replace direct
`\includegraphics` calls in `sections/` with this macro, preserving each
existing figure and displayed width.  Then add concise color macros such as
`\blue{text}` and `\red{text}` to `newcommands.tex` and use them in suitable
slide content.  Compile the root deck after each change set and push each
change set separately.
