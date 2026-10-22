# pstack editing process: claude-opus-5-5/run-1

Editor: Claude Opus 5.5, in a context separate from the Humanizer editors. No Humanizer or wilson-humanizer instructions, `RUN/humanizer/**` or `report/assignment-1/**` were opened.

Input: frozen `RUN/raw/sections/*.md`. SHA-256 hashes were rechecked after editing and still match `raw/manifest.md`. Contract: `RUN/input/contract.md`.
Output: `RUN/pstack/draft/` (five section files plus `references.md`, which is a byte-identical copy of the raw file).

## Skill order

1. `technical-writing` (`C:/Users/xingy/.codex/skills/technical-writing/SKILL.md`) was read in full and applied to all five section files as pass 1.
2. `unslop` (`C:/Users/xingy/.codex/skills/unslop/SKILL.md`) was read in full and applied to the pass-1 output as pass 2.

Both passes edited prose only. Tables, diagrams, headings, captions and the `<!-- Cited -->` comments were left byte-for-byte as they were.

## Pass 1: technical-writing, main patterns flagged

- Mode: explanation (a report that weighs trade-offs). The report's view and evaluation were therefore kept.
- **Semicolons and colons used as sentence joiners** were replaced with full stops. Examples: 1.2 "local-first: the budget…", 2.1 "bottleneck before: after…", 3.1 the three-clause stakeholder sentence, 3.4 WCAG, and 4.2–4.6 (five instances).
- **Missing actors and passive voice** were rewritten to name the actor where it is known: "Issues and roles are not assigned" became "Nobody assigns issues or roles"; "release branch is cut automatically" became "Automation cuts the release branch"; "a weighted matrix is used" became "this report uses a weighted matrix"; "Only its scope was read" became "This report read only its scope"; "Its cost is estimated in Assignment 2" became "Assignment 2 estimates its cost". Similar edits were made elsewhere.
- **Ambiguous "it", "this" and "which"** were replaced with the noun. Examples: 2.4 "Its C4 score" became "Kanban's C4 score"; 2.6 "which would favour DevOps" became "Either change would favour DevOps"; 4.1 "This matters for Actual, which…" was split; 4.6 "reduce this risk" became "reduce the risk of a new backlog".
- **"Not" placed where it allows two readings.** 3.2 "Functional suitability is not ranked lower because correct numbers matter less" became "does not rank lower because … It ranks lower because …", which states the actual reason.
- **Dropped verbs.** 2.4 "and Spiral on expert risk analysis" became "Spiral loses on expert risk analysis". In 2.3, the candidate bullets that were verbless fragments became full sentences.
- **Long sentences with two thoughts** were split, as in 2.5 (Verify WIP limit), 3.6 (Wessel findings), 4.3 (independent reviewer role), 4.5 (early defect detection) and 4.6 (donations and audit cost).
- **Dangling modifier in 1.1.** "After discovering Actual Budget…, this assignment gave me…" became "Once I had found Actual Budget and become interested in it, this assignment gave me…". The first-person voice was kept as the contract requires.
- **Plain words.** Examples: "rather than replacing" became "and does not replace"; "consume" became "use up"; "is layered over" became "is applied to"; "effectively" became "in effect".

## Pass 2: unslop, main patterns flagged

- **Rule 15 (boldface overuse).** Bold was removed from in-sentence terms in 2.3–2.5 ("proof rule", "OSS (\"Bazaar\") model", "mandatory QA gate", "explicit policy") and from the three attribute names in the 3.2 prose, which already appear in Table 3.1. Bold was kept on the key conclusions and the section-label lead-ins.
- **Rules 14 and 16 (colon labels in lists).** The 2.3 candidate list used "**Spiral:** fragment". It now uses a bold lead-in ending in a full stop, followed by a sentence. In 3.3, the interaction-capability bullet had bold running into the sentence. It became a proper lead-in followed by "None was found despite the WCAG target".
- **Rule 32 (mannered prose).** "the QA plan lives on the board" became "is written into the board"; "a maturity appraisal would buy a rating" became "produce a rating"; "Automation helps but is not free" became "Automation helps, but it has costs"; "gates can become ritual" became "gates can become a formality".
- **Rule 27 (vague statement).** "Some limits remain" became "Four limits remain", matching the four limits that follow.
- **Global English carry-over (Latin phrase).** In 4.2, "ad hoc" became "unplanned".
- **Rule 13 (dashes).** Prose contains no em dashes. The en dashes left are numeric ranges inside protected numbers or citations (1–5, 1–3, USD 3,000–3,500, pp. 26–27).
- **Rule 7 (AI vocabulary), rule 3 (-ing phrases) and rule 23 (filler).** A scan found no AI-vocabulary hits. In 4.5, "aiming to reduce escaped defects" became "to reduce escaped defects".

## Task-specific exceptions (the contract overrode a skill)

- **Second person.** technical-writing prefers "you". The report stays in third person. "I" remains only in the personal-reason passage in 1.1.
- **Parentheses (unslop rule 13).** APA parenthetical citations and defined abbreviations such as "(PR)", "(WIP)" and "(OSTIF)" were kept. The NASA independence definitions in 4.1 keep their parenthetical glosses because they are paraphrased definitions attached to one citation.
- **Title-case headings (unslop rule 17 and technical-writing's "headings carry the point").** All headings were kept exactly, because headings and numbering are protected.
- **Rule of three (unslop rule 10).** These genuine categories were kept: the three independence parameters, the three quality views in 3.1, the three attributes, the three risk tiers, the three goals in 4.5, and the three challenges in 1.5.
- **Hedging (unslop rule 24).** Evidence limitations were kept verbatim: "no evidence found in the repository, October 2026", "Private practices may exist", "plausible but unproven", "may understate risk", "harder to fake, but not impossible", and "Only its scope was read" (now "This report read only its scope").
- **Sentence length (technical-writing, about 25 words).** Some long sentences were kept because one citation supports several clauses, and splitting them would detach a claim from its source. These are the 3.3 CI sentence (Actual Budget, 2026a, n.d.-j), the GHSA-m2cq-xjgm-f668 sentence (Actual Budget, 2026c), the OpenSSF sentence (Open Source Security Foundation, n.d.-a, n.d.-b), the advisory-credit sentence in 4.2 and the NASA definition sentence in 4.1.
- **Semicolons inside the High-tier list (4.3).** They were kept because they separate items that themselves contain commas. Commas alone would make the grouping ambiguous, and Global English favours clarity.
- **Passive kept where the actor is unknown or deliberately unstated.** "WCAG 2.2 is recommended for new work" was kept. Naming W3C as the recommender would add an unverified attribution. "no … evidence was found" was also kept because it is a protected evidence qualifier.
- **"Open limitations remain (Alaidaros et al., 2021)" (2.6).** This sentence is vague under unslop rule 27, but making it specific would add content not in the raw text. It was left as written.
- **Serial comma.** technical-writing asks for serial commas. The raw text's British style without them was kept for consistency, and no list became ambiguous.
- **Narrative and parenthetical citation forms.** Every citation keeps its original form. None was converted between narrative and parenthetical.

## Self-audit

A script (temporary, outside the repository) compared raw and draft for each file:

- Fenced diagrams, table rows, headings, captions and `<!-- Cited -->` comments are identical: **pass**.
- The multiset of citations (author, year, suffix and locator), direct quotations, and numbers, dates and identifiers is identical: **pass**. No citation was lost, duplicated or added.
- No second person in prose: **pass**.
- No em dashes in prose: **pass**. The only semicolons are inside citations and in the 4.3 High-tier list (a deliberate exception).
- US-spelling scan: the only hits are "Organization" in standards-body names inside citations, which are correct as proper names.
- `references.md` is byte-identical to raw: **pass**.
- `RUN/raw/**` hashes still match the manifest: **pass**.
- Manual read: no claim was strengthened. Qualifications ("would have a defined point … to detect", "cannot predict Actual's results", "self-reports") were kept, and no new facts or sources were added.

## Corrections made during the self-audit

- The 3.3 accessibility bullet left bold running into the sentence after pass 1. It was fixed in pass 2 (see the rule 16 entry above).
- The 2.3 list after pass 1 read "**Scrum:** Scrum uses…", which repeated the name. Pass 2 changed it to "**Scrum.** It uses…".
- The OpenSSF sentence in 3.4 still had a semicolon after pass 1. It was rejoined with commas so that the single citation still covers both clauses.

## Final word counts (`python writing-experiments/tools/count_words.py`)

| File | Raw | pstack | Change |
|---|---:|---:|---:|
| 00-executive-summary.md | 200 | 205 | +2.5% |
| 01-introduction.md | 548 | 539 | -1.6% |
| 02-methodology.md | 1,432 | 1,481 | +3.4% |
| 03-quality-assurance.md | 1,421 | 1,456 | +2.5% |
| 04-ivv.md | 1,360 | 1,379 | +1.4% |
| **Total** | **4,961** | **5,060** | +2.0% |

The total is within the 4,750–5,250 range, and every section is within ±5% of its frozen count. The small increases come from splitting sentences and restoring actors, articles and verbs. No filler was added.
