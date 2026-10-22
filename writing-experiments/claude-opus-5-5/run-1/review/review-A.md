# Meaning and integrity review: blind version A

Reviewer scope: `review/blind/A/` (00–04) compared with `raw/sections/` (00–04) under `input/contract.md`. No other folders were opened.

## Summary

- REQUIRED corrections: 1 (low severity)
- OPTIONAL suggestions: 4
- Protected elements: spot-check passed (see below)
- Contract: no violations found. British English and third person are kept, with "I" only in 1.1. Total length is 5,060 words, inside 4,750–5,250.

Overall the edit is close to the raw text. Most changes split sentences, turn passive voice into active voice ("The report scored…", "This report read only its scope…") or make implicit links explicit. Caveats are intact: "no evidence found … October 2026", "private practices may exist", "analyst judgements, not measured outcomes", "plausible but unproven", "inspired by" IEEE 1012, "technical independence only", "self-reports", "cannot predict Actual's results" and "theoretically possible" all survive. Rankings, scores, the recommendation's strength and the critical-evaluation content are unchanged.

## Protected-element spot-check

- Citations: the parenthetical citation strings, author, year, suffix and locator, are identical in all five files (sorted diff, no differences). Narrative citations checked by eye: "Smith and Hayes (2024, Abstract)" is unchanged.
- Headings, table rows and table/figure captions: identical in all five files (line diff, no differences).
- Diagrams (Figures 1–3): unchanged.
- Numbers, identifiers and quotations checked by eye: 102/94/95/120, 42/50 and 39, 7-point margin, USD 2,000, USD 3,000–3,500, 17:00 UTC on the 25th, GHSA-m2cq-xjgm-f668, 20 February 2026, CVSS 9.2, 55%, 24 audits / 231 findings / 98%, 93 documents / 37 capabilities, 8,000 users, HTTP 404, and the quotations "users trusting the numbers", "may accelerate", "appropriate test coverage", "has in no way diminished the need for IV&V" and "a relatively basic flow tool…". All match.
- Claim–citation pairing: no citation has moved to a different claim. One sentence was rephrased ("Advisories published in 2026 describe critical and high-severity access-control flaws", in 3.3 and 4.1). It still sits next to the same citations and says the same thing.

## REQUIRED corrections

### R1. 02-methodology.md, 2.5: an intended effect of the WIP limit is stated as a certain outcome

- **Edited:** "The Verify column has a WIP limit, set from observed review throughput. When reviews pile up, the limit stops new work from starting."
- **Raw:** "Verify carries a WIP limit, set from observed review throughput, so that new work stops starting while reviews pile up."
- **Why it is drift:** The raw text gives the limit's *purpose* ("so that"). The edited text says the limit *does* stop new work, which presents an effect of a proposed design as certain. It also clashes with 2.6, which keeps the caveat that "A WIP limit cannot compel anyone to review" and says limits "should therefore act as signals". The raw sentence was consistent with that caveat. The edited one overstates what 2.6 then qualifies.
- **Minimal fix (keeps the edited two-sentence style):** "The Verify column has a WIP limit, set from observed review throughput. When reviews pile up, the limit is meant to stop new work from starting."

## OPTIONAL suggestions (not meaning drift)

1. **02-methodology.md, 2.5, opening sentence.** "Kanban is applied to Actual's existing GitHub workflow and does not replace it." Out of context, the present tense could read as an observed fact, and the contract says the report must never state that Actual has adopted a recommendation. The raw text ("Kanban is layered over…") has the same tense, and the heading marks the section as "(to-be)", so this is not drift. "Kanban would be applied to…" or "The proposal applies Kanban to…" would remove the ambiguity.
2. **04-ivv.md, 4.5 Overall quality.** "…where failure costs most, to reduce escaped defects." The raw "aiming to reduce" is slightly more tentative. "To reduce" still expresses purpose, not a result, so the meaning holds. Restoring "aiming to" would keep the original hedge exactly.
3. **01-introduction.md, 1.5.** "Section 2 addresses how the project organises work." The raw text reads "how work is organised". Section 2 both describes the current process and proposes a new one, so the edit is acceptable. "How work should be organised" would point more clearly to the recommendation.
4. **03-quality-assurance.md, 3.6.** "Four limits remain" replaces "Some limits remain". The count is correct (accessibility, badge, scope-level reading, public evidence), so the meaning is unchanged. It is noted only because it adds a number that the raw text did not state.

## Paragraph-level notes with no issue found

- 00: The workflow list moved into its own sentence. The recommendation and its weakness are unchanged. The final paragraph was split, but "technical independence only" and the resource limits are kept.
- 01: The personal-reason sentences stay in the first person, as the contract allows. The statement that E2EE leaves local data unencrypted and does not cover bank-sync tokens is unchanged.
- 02: Screening reasons, the proof rule, Scrumban's exclusion, the baseline being non-selectable, the C4 caveat, DevOps as the strongest alternative, the equal-weights check, the thin-evidence caveat and the conditions under which the choice would change are all intact.
- 03: The explanation of why Functional suitability is rated Medium is kept and made explicit without new claims. Gap findings keep their public-evidence qualification. The scope-only reading of IEEE 730 and the non-conformance claim are kept. The partial adoption of ASVS and the 2.2/2.1 nuance are kept. The Wessel et al. findings remain observational, with the caveat on predicting Actual's results.
- 04: The three independence parameters, the "technical independence only" conclusion from the reporter credits, the OSTIF self-report qualifier, tiers labelled as this report's own design "inspired by" IEEE 1012, preview builds having no sync server, the release-row disclaimer, the conditional wording "would … detect" in 4.5, and all of 4.6's limits are intact.
