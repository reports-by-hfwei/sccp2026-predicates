# Comprehensive review: SCCP 2026 predicates presentation

## Scope and method

This is a read-only review of the current 25-page deck built from
[`sccp2026-predicates.tex`](../../sccp2026-predicates.tex).  The review used
both the source and the rendered
[`sccp2026-predicates.pdf`](../../sccp2026-predicates.pdf): all 25 pages were
rendered and visually inspected.  Findings below are organized as four
independent lenses:

1. Database-consistency researcher: correctness, scope, and research framing.
2. Conference-talk reviewer: story, audience load, and the contribution arc.
3. LaTeX/Beamer reviewer: typesetting, references, and maintainability.
4. Presentation-design reviewer: legibility, hierarchy, and projection value.

No manuscript or presentation source was changed by this review.

## Executive assessment

**Recommendation: major revision before presentation or distribution.**  The
deck has a strong visual system and a promising story: predicate operations
create a real gap between execution semantics and dependency-graph reasoning,
then the talk closes that gap with definitions, characterizations, and a
design space.  Slides 2, 10, 18, 19, and 24 make that arc easy to recover.

However, two publication-blocking issues are visible to the audience: the
design-space inclusion is reversed on the final takeaway, and two citation
keys render as raw identifiers.  These are followed by one notation mismatch
on the definition slide and several high-information slides whose source
screenshots are too small to carry their intended argument in a room.  Fixing
the P0 items and the first three P1 items below should substantially improve
both trust and comprehension without requiring a new talk structure.

## Priority-ordered findings

| Priority | Lens | Finding and evidence | Why it matters | Minimum remedy |
|---|---|---|---|---|
| **P0** | Database correctness | **The design-space interval is reversed on page 25.** Page 23 and [`sections/tech.tex`](../../sections/tech.tex#L93) state `PredRW+ \subseteq PredRW \subseteq PredRW-` and `PredRW+ \subseteq R \subseteq PredRW-`. The last takeaway instead states `PredRW- \subseteq R \subseteq PredRW+` in [`sections/takeaways.tex`](../../sections/takeaways.tex#L14). | This is the closing theorem statement.  It contradicts the earlier lower-frontier/upper-structural explanation and changes the set of admissible relations. | Use the same direction and colour/role convention everywhere: `\PredRWarXiv \subseteq \mathcal R \subseteq \PredRWCAV` (equivalently `PredRW+ \subseteq R \subseteq PredRW-`).  Recheck page 19, page 23, page 24, and page 25 together. |
| **P0** | Beamer/references | **Two citations are visibly unresolved.** Page 5 shows `Complexity:OOPSLA2019`; page 15 shows `Complexity:CAV2025`. Their call sites are [`sections/review-wo-predicates.tex`](../../sections/review-wo-predicates.tex#L47) and [`sections/review-predicates.tex`](../../sections/review-predicates.tex#L87), while no matching keys occur in `predicates.bib`. | Raw BibTeX keys immediately signal an unverified bibliography and weaken the scholarship claims on the two literature-review slides. | Correct the keys or add the intended bibliography entries; build with Biber; require no raw keys or undefined-citation warnings before release.  The CAV slide should use the existing `ComplexityMIL:CAV2025` key if that is the intended work. |
| **P1** | Database correctness | **Page 21 mixes the observed key.** The graph-witness relation is `T' \xrightarrow{PredWR(y)} T`, but the prose says that `T` externally observes `x`; see [`sections/tech.tex`](../../sections/tech.tex#L29-L31). | A first definition slide must give the audience one stable transaction/key trace.  Switching `y` to `x` makes it unclear whether this is a special case or a typo. | Make relation label, prose, and figure use the same key; keep the separate `y` used for the anti-dependency only if it is explicitly introduced as a second key. |
| **P1** | Database research | **The characterizations are crisp, but the page-23 graph condition is not.** The diagram says `G_H is acyclic in a certain way`, whereas SER requires acyclicity and SI permits cycles subject to the adjacent `RW/PredRW` condition. | “In a certain way” hides the technical distinction that makes the SI result valuable, and makes the proof triangle read as a slogan rather than a theorem bridge. | In the node or adjacent legend, state `SER: acyclic; SI: each cycle has adjacent RW/PredRW`.  Keep the full theorem statements on page 22, but make the miniature page-23 restatement self-contained. |
| **P1** | Research framing | **“No rigorous proof in the literature” on page 16 is too absolute for a research claim.** It is paired with a screenshot and a provenance graph in [`sections/review-predicates.tex`](../../sections/review-predicates.tex#L95-L100), but no scope qualifier is visible. | An audience member familiar with a proof outside the selected corpus can challenge the claim even if the intended, predicate-specific statement is correct. | State the precise gap: for example, “No published proof known to us for the predicate-aware characterization under these definitions.”  Add a small scope qualifier or explain it orally before displaying the claim. |
| **P1** | Visual design | **Pages 13, 16, 17, and the left half of page 20 rely on screenshots whose content is illegible at normal projection distance.** The right-side taxonomy on page 13 and the highlighted excerpts on pages 16--17 cannot be read without zooming. | These images occupy substantial visual area but do not supply readable evidence.  They add visual noise and encourage the speaker to narrate a document viewers cannot inspect. | Replace each screenshot with one cropped, enlarged excerpt containing only the claimed fact, plus a one-sentence interpretation.  For page 20, show a single simplified axiom fragment or use the existing predicate graph as the visual anchor. |
| **P1** | Conference narrative | **Page 22 is overloaded.** It contains two theorem cards, an “if” bridge, two challenge cards, two dense diagrams, and two conclusions. | The page is the intellectual peak of the talk; overload here prevents the audience from retaining either challenge or its proof consequence. | Use progressive disclosure, or split into “theorems + proof direction” and “two predicate-specific challenges.”  If one page is mandatory, remove repeated theorem prose and enlarge the two challenge diagrams. |
| **P1** | Beamer/layout | **Page 23 is visually balanced but vertically dense in its embedded form.** The proof triangle is legible as a standalone figure but becomes small after the two inclusion lines, theorem sentence, and proof-bound cards are placed around it.  The current layout is in [`sections/tech.tex`](../../sections/tech.tex#L90-L115). | This is the slide that must reconcile the design space with the two proof directions.  Small labels reduce the payoff from the newly added diagram. | Let the triangle be the central object: reduce the two top inclusions to one line, move the universal characterization sentence to the bottom, and use shorter proof-card clauses. |
| **P2** | Narrative | **The “without predicates” and “with predicates” review arcs repeat page 4/page 12 almost exactly.** The second instance supplies no visible predicate-specific contrast. | Repetition costs a full slide without advancing the gap argument, particularly in a 15-minute conference slot. | On page 12, retain the familiar SER/SI labels but add a red contrast such as “same headlines; predicate observations break the old bridge.”  Alternatively, compress the two review arcs by one slide. |
| **P2** | Presentation design | **Several slides use a full paper title page as a visual rather than a claim-bearing graphic.** This is most pronounced on pages 4--8, 13, 14--17. | It makes the literature tour feel archival instead of analytical and produces uneven visual density. | Adopt one consistent related-work pattern: author/year + one cropped result/definition + a one-line “what it provides / what it omits.”  Preserve full cover images only when provenance itself is the point. |
| **P2** | Writing/polish | **Visible typos undermine a carefully designed deck.** Page 19 says “Axomatic Specs” (also in [`tikz/contribution.tex`](../../tikz/contribution.tex#L15)); page 25 says “Downstrem Analysis Enabled” in [`sections/takeaways.tex`](../../sections/takeaways.tex#L3). | These are high-salience titles, including the contribution summary and final slide. | Correct to “Axiomatic” and “Downstream”; run a final title-only proofreading pass. |
| **P2** | Research framing | **The upper relation is labelled “CAV 2025 (inspired)” on page 15, but its status needs an explicit distinction from a definition introduced in this work.** | The audience may infer that the cited CAV paper literally defines the displayed relation. | Say “structural upper bound (this work; CAV-inspired)” and retain the citation.  This is consistent with the more careful wording already used on the design-space slide. |
| **P2** | Future work | **The interval notation on page 24 is hard to parse as a range.** The title `[`PredRW-`, `PredRW+`]` follows the textual order “upper, lower” in [`sections/future.tex`](../../sections/future.tex#L11). | It reinforces the risk of the page-25 direction error and makes the checker bounds harder to explain. | Name the two bounds explicitly (“lower-frontier / upper-structural guided checker”) or show the ordered inclusion rather than bracket notation. |

## Lens 1: database-consistency researcher

### What is working

- The central research question is well chosen.  Page 2 establishes why a
  predicate read returns a set rather than one version; pages 14--18 then make
  the resulting gap concrete rather than treating predicates as a cosmetic
  extension.
- The presentation distinguishes `PredWR` from `PredRW`, and page 15 makes the
  three `PredRW` choices visually comparable.  This is a better entry point
  for database audiences than leading with the complete formal definition.
- Page 22 presents the SER and SI outcomes side by side and correctly gives
  the audience a proof-level reason that SI is harder.
- The design-space framing is valuable: it prevents the talk from looking like
  it depends on one arbitrary predicate anti-dependency definition.

### Substantive risks to resolve

1. **Define the scope of every “exact characterization.”** A database audience
   will ask: fixed history or existential history-level statement; fixed base
   or execution-derived base; and which of SER/SI is currently under
   discussion.  Page 23 says “same existential SER/SI characterization,” which
   is good, but that qualifier should also be spoken when page 19 first claims
   the design space.
2. **Do not conflate a relation definition with an analysis policy.** Page 24
   moves from a mathematical interval to an accept/reject/refine checker.  Add
   one spoken or visual caveat that the bounds are a guidance strategy, not an
   already-complete decision procedure with the same complexity guarantee.
3. **Use one transaction/key convention per technical slide.** Page 14 and
   page 21 should make it obvious which transaction reads, which supplies the
   observed version, which later writer changes the result, and whether `x` or
   `y` is the predicate-sensitive key.
4. **Be careful with the literature gap.** The deck may be correct to identify
   a missing predicate-aware proof, but the presentation needs to delimit the
   result family rather than implying that all past SER/SI graph proofs are
   informal.

## Lens 2: conference-talk reviewer

### Story diagnosis

The story currently has four beats:

1. familiar item-operation consistency theory (pages 2--10);
2. what predicates change (pages 11--18);
3. four contributions (pages 19--23);
4. downstream agenda and takeaway (pages 24--25).

That macro-structure is sound.  Its main pacing problem is that the audience
spends 16 of 25 pages in the review before seeing the contribution map.  For a
15-minute research talk, target roughly five minutes for the review, eight for
the technical contribution, and two for consequence/close.  The deck can keep
its content but should make each review page answer a single question: *what
does the item-only result give us, and why does a predicate read invalidate or
leave open that bridge?*

### Recommended talk-level revisions

- Make page 10 end with an explicit premise: “For item operations, specs,
  depgraphs, and downstream analyses are connected.”  Make page 18 mirror it:
  “For predicates, all three links need repair.”  This produces an audible
  before/after transition.
- Page 19 should be introduced as the response to the three sticky notes on
  page 18, not merely as a numbered list of contributions.
- On page 22, say what the audience should remember before showing the two
  challenge figures: “Both theorems reduce to building an execution; predicates
  create a witness-alignment problem.”
- End page 25 with one decision-relevant sentence, e.g. the theory now makes
  predicate-aware checking/verification/robustness meaningful.  The present
  closing list is accurate but reads more like a paper abstract than a spoken
  final message.

## Lens 3: LaTeX/Beamer reviewer

### Strong points

- The SimplePlus theme is used consistently: typography, navy section titles,
  teal blocks, and the red emphasis colour form a coherent grammar.
- Frame titles are concise and section numbering is helpful in the technical
  sequence.
- Standalone TikZ diagrams keep repeated mathematical visuals reusable and
  sharp.

### Technical quality gates

1. Treat “no unresolved citations” as a release gate.  Raw citation keys on a
   projected slide are a P0 failure even if PDF generation exits successfully.
2. Add an automated spelling/title scan for visible prose.  It would catch
   `Axomatic` and `Downstrem` before a final build.
3. Keep definition text aligned with its mathematical label.  The `x`/`y`
   mismatch is exactly the class of slide-local inconsistency that a small
   source-level check cannot infer but a final notation pass can catch.
4. Avoid using paper covers or full-page screenshots below their readable
   resolution.  Beamer compiles them faithfully; the design problem is scale,
   not the renderer.
5. Preserve the current figure-source/PDF pairing.  It makes the diagrams
   maintainable, but regenerate only the figures whose sources changed to avoid
   unrelated binary diffs.

## Lens 4: presentation-design reviewer

### Visual strengths

- The deck is clean, sparse, and generally high contrast.  Pages 2, 10, 14,
  18, 19, 23, and 24 have a clear focal object.
- Colour carries stable meaning: navy for structure, teal/blue for positive
  links, and red for predicate-specific tension or restrictions.
- The sticky-note treatment on page 18 successfully distinguishes open gaps
  from the depgraph nodes rather than making them look like graph elements.

### Visual improvements

- **Projection test:** if a screenshot cannot be read from the back of a room,
  crop it or replace it.  Pages 13, 16, and 17 are the clearest cases.
- **One slide, one visual hierarchy:** page 22 has four competing focal areas;
  page 23 has three.  Choose the theorem or the proof bridge as the focal
  object, then make other material subordinate.
- **Use whitespace as grouping rather than blankness:** pages 6--8 have ample
  empty area but the paper covers and theorem card do not form a strong
  comparison.  A smaller source label and larger theorem/graph would improve
  balance.
- **Keep headings polished:** title spelling and formula direction have an
  outsize effect because readers use headings and coloured formula lines as
  navigation anchors.

## Suggested revision order

1. Correct the page-25 interval and make pages 19, 23, 24, and 25 use one
   lower-to-upper order.
2. Repair both citation keys and verify that the rendered PDF contains author
   names/years rather than key strings.
3. Resolve the page-21 key mismatch and make the page-23 depgraph condition
   precise.
4. Rephrase the page-16 literature claim with its predicate-aware scope.
5. Replace or crop unreadable screenshots; split or simplify page 22; then
   enlarge the page-23 proof triangle.
6. Make the page-12 repetition carry an explicit contrast, and proofread all
   titles and final-takeaway text.

## Final readiness check after revision

- [ ] The lower/upper design-space relation has the same direction on every
      page and in every figure.
- [ ] All citation labels are human-readable and every cited key resolves.
- [ ] Every technical diagram uses a single, consistent transaction/key
      convention.
- [ ] Page 22 and page 23 are readable at projected size, not only in the PDF
      viewer.
- [ ] Claims about the literature and checking consequences have visible scope
      qualifiers.
- [ ] Slide titles, contribution labels, and the final takeaway are
      spell-checked.
