# Voice Generation Prompt for `speech.md`

Generate a **single continuous English male-voice recording** of the academic talk in `speech.md`.

## 1. Overall Voice Profile

Use an **adult male voice** with a calm, confident, scholarly tone suitable for a short international database research conference presentation.

The voice should be:

- clear, professional, and natural;
- slightly warm, with a low-to-mid pitch;
- articulate but not overly formal;
- confident without sounding promotional;
- conversational enough to sound like a real researcher presenting his own work;
- neutral international / General American English in overall delivery;
- **not** theatrical, dramatic, “radio-announcer-like,” or artificially enthusiastic.

The intended audience consists of experts in database consistency, transactions, and concurrency control. Do not adopt a teaching-for-beginners tone.

## 2. Speaking Rate and Total Duration

Use a **medium-to-slightly-slow academic speaking rate**, targeting approximately **128–132 words per minute** on average.

The source script contains about 610 spoken words. The final recording should therefore aim for a total duration of approximately:

> **4 minutes 45 seconds to 5 minutes**

Do **not** exceed 5 minutes.

Do not achieve the timing target by rushing. Maintain clear articulation of technical terms. If timing needs adjustment, speak the easier review material slightly more briskly and reserve slightly more space for the contribution and characterization sections.

Recommended pacing pattern:

- opening and basic item-vs-predicate distinction: natural and welcoming;
- background/review slides: slightly brisker;
- transition to the predicate-specific gap: slightly slower and more deliberate;
- contributions and technical core: measured and precise;
- final takeaway: calm, concise, and conclusive.

## 3. Prosody and Academic Delivery

Use natural sentence-level intonation rather than reading every sentence with the same cadence.

Apply **subtle emphasis** to the main conceptual terms when they first become important, especially:

- predicate operations;
- omitted items / omission;
- dependency graphs;
- predicate anti-dependency;
- two-way correspondence;
- witness mismatch;
- observationally equivalent;
- exact graph recovery;
- lower bound and upper bound;
- correctness foundation.

Do not over-emphasize every technical term or acronym.

At contrastive structures such as:

- “without predicates” versus “with predicates”;
- “returned” versus “omitted”;
- “left” versus “right”;
- “lower bound” versus “upper bound”;
- “if” versus “only if”;

use a light contrastive stress so that the logical structure is audible.

When the script says things such as “Look at the employee table,” “Look at this example,” or “Look at the two cases,” sound as if briefly directing the audience’s attention to the current slide. Do not make these phrases theatrical.

## 4. Pauses

Treat `[PAUSE]` as an explicit meaningful pause of approximately **0.6–0.9 seconds**.

Also use natural micro-pauses:

- about 0.15–0.30 seconds at normal clause boundaries;
- about 0.3–0.5 seconds when moving to a new slide or major idea;
- slightly longer before the final takeaway.

Do not insert long pauses after every sentence. The presentation must remain continuous and fit within five minutes.

## 5. Slide and Markdown Handling

The Markdown headings in `speech(1).md` identify slides and are **not part of the spoken script**.

Therefore:

- do **not** read `# Speech`;
- do **not** read any `## ...` slide titles aloud;
- do **not** say “Slide one,” “next slide,” or similar stage directions unless those words explicitly occur in the spoken body;
- ignore Markdown formatting symbols such as `**`, `$`, backticks, quotation-mark markup, or other formatting artifacts;
- read only the prose paragraphs beneath the headings;
- preserve the order of all spoken paragraphs exactly.

Do not add, remove, paraphrase, summarize, or rewrite the content.

## 6. Technical Pronunciation

Pronounce technical notation consistently and distinctly.

Use the following spoken forms:

- `SER` → **“S-E-R”**
- `SI` → **“S-I”**
- `SQL` → **“S-Q-L”**
- `VIS/AR` → **“V-I-S slash A-R”**
- `PredRW` → **“Pred R-W”**
- `T-prime` → **“T prime”**
- standalone variables `T`, `S`, `X`, `Y`, `Z`, and `x` → pronounce as their English letter names
- `"if"` and `"only if"` → speak the words naturally; do not say “quote” or “quotation mark”
- `anti-dependency` → articulate clearly as **“anti-dependency”**
- `predicate-aware` → keep the compound smooth and natural
- `item-only` → keep the compound smooth and natural

For names such as **Hengfeng Wei, Si Liu, Yuxing Chen, Hunan University, and Adya**, pronounce them as personal or institutional names rather than spelling them letter by letter. Use a careful, respectful pronunciation and do not exaggerate the accent.

## 7. Handling Examples and Figures

When the script refers to an example shown on the slide, keep the explanation brief and visually anchored.

For example:

- when saying “Look at the employee table,” slightly stress **employee table**;
- when describing X, Y, and Z, keep the letters clearly separated;
- when describing salary 10 changing to salary 9, make the contrast audible but concise;
- when saying “Look at the two cases,” use a short pause before distinguishing **the left** from **the right**.

These are cues to help the audience follow the slide, not opportunities for additional explanation. Do not insert any commentary that is not in the script.

## 8. Delivery of the Core Contribution

The section beginning with:

> “We build that bridge...”

marks the transition from background to the authors’ contribution.

From this point onward, slightly increase vocal focus and confidence, but keep the delivery restrained and academic.

For the characterization section, make the logical contrast especially clear:

- a mismatch that changes the predicate outcome exposes a forbidden anti-dependency;
- observationally equivalent SI witnesses do not require exact graph recovery.

For the design-space section, make the relation between the two bounds easy to hear:

- **lower bound → “if” direction**
- **upper bound → “only if” direction**

Do not slow down excessively on these points; clarity should come from phrasing and stress rather than long pauses.

## 9. Ending

The final two sentences should sound like a concise research takeaway, not like a dramatic conclusion.

Slightly slow down on:

> “In summary, we build the bridge...”

Then honor the explicit `[PAUSE]` before:

> “This gives downstream analyses a correctness foundation.”

Deliver the last sentence firmly and calmly, with a falling final intonation. Do not append “thank you” or any other words unless they appear in the source script.

## 10. Quality Constraints

The final recording must satisfy all of the following:

1. One male English-speaking voice throughout.
2. Natural academic conference delivery.
3. Medium-to-slightly-slow pace, approximately 128–132 wpm.
4. Total duration approximately 4:45–5:00, never over 5:00.
5. Clear pronunciation of technical terminology and acronyms.
6. No spoken Markdown headings or formatting.
7. No added commentary, fillers, acknowledgments, or paraphrases.
8. No exaggerated emotion, sales tone, audiobook style, or synthetic “announcer” cadence.
9. Preserve the exact logical order and wording of the spoken prose in `speech(1).md`.
10. The result should sound like a well-rehearsed researcher delivering a precise five-minute conference talk.