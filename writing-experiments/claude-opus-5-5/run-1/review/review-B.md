# Meaning and integrity review: blind version B

Compared: `review/blind/B/*.md` (edited) against `raw/sections/*.md` (frozen raw), under `input/contract.md`. Source checks used only `planning/research/*.md` and `planning/*.md`.

## Protected elements (spot-check)

I spot-checked every heading, Tables 1.1, 2.1, 2.2, 3.1, 3.2, 3.3, 4.1 and 4.2 (cell contents, scores, totals, weights), Figures 1–3 (diagram text and captions), all in-text citations and locators (for example Ahmad et al., 2018, p. 98/p. 106/p. 110; Salkever, 2023, pp. 26–27; Actual Budget, 2026a, Product Purpose section; n.d.-j, Testing Checklist section), numbers and identifiers (102/95/94/82/81/72, 42/50, 39, USD 2,000, USD 3,000–3,500, CVSS 9.2, GHSA-m2cq-xjgm-f668, 20 February 2026, 17:00 UTC on the 25th, 93/37, 24/231/98%, 55%, 8,000) and direct quotations. All of these match the raw. The HTML `Cited:` comments also match. This agrees with the earlier mechanical check.

The only change to protected material is that the raw's bold labels have been removed. These were run-in labels in the 1.5 bullets, the 3.3 gap bullets and the 4.3 paragraph labels, plus bold emphasis in 2.1, 2.3, 2.4 and 3.2. None of them is a heading or caption. The 4.5 bold labels are kept. The loss of the 1.5 labels causes one meaning change, listed as R3.

Contract checks: I found no American spellings ("Organization/Standardization" appear only in proper names) and no second person. "I" appears only in 1.1. I found no padding.

## REQUIRED corrections (8)

### R1. Executive summary: Kanban's weakness is no longer called a weakness
- **Edited:** "Kanban itself prescribes no technical quality practices, so those gates carry the quality work."
- **Raw:** "Its weakness is that it prescribes no technical quality practices."
- **Why it is drift:** The raw evaluates this as a weakness, and that critical judgement is repeated in 2.6 ("Kanban's main weakness"). The edit turns it into a design rationale with a new causal claim ("so those gates carry the quality work"). As a result, the summary no longer states the method's main limitation. The contract says an argued limitation must not be removed.
- **Minimal fix:** "Its weakness is that Kanban itself prescribes no technical quality practices, so those gates must carry the quality work."

### R2. Executive summary: the scope and ranking of the IV&V limits have changed
- **Edited:** "Volunteer time and donation funding limit how far independence can go."
- **Raw:** "…volunteer time and donation funding remain the main limits."
- **Why it is drift:** The raw names these two factors as the *main* limits on the IV&V proposal as a whole. In 4.6 these limits cover flow and backlog as well as cost. The edit drops "main" and narrows the limits to independence only.
- **Minimal fix:** "Volunteer time and donation funding remain the main limits."

### R3. 1.5: "changing requirements" has become "volunteers' changing priorities"
- **Edited:** "Work depends on volunteers, whose priorities change, and review has been a bottleneck before (Aboltins, 2025)."
- **Raw:** "**Volunteer capacity and changing requirements.** Work depends on volunteers, and review has been a bottleneck before (Aboltins, 2025)."
- **Why it is drift:** The raw challenge covers two things: volunteer capacity and changing (community-voted) *requirements*. Changing requirements is the challenge the agreed plan maps to Section 2 (`planning/01-introduction.md`, `planning/05-writing-handoff.md`), and it is criterion C1. The edit drops changing requirements and adds a new claim that volunteers' priorities change. Nothing in the raw or the sources states that claim. Volunteer *capacity* also disappears as a named challenge.
- **Minimal fix:** "Work depends on volunteer capacity, requirements keep changing, and review has been a bottleneck before (Aboltins, 2025)."

### R4. 2.3: the proof rule is misdefined
- **Edited:** "A proof rule then required real-world evidence, and Shape Up (Singer, 2019) failed it because no peer-reviewed evaluation was found."
- **Raw:** "A **proof rule** then removed Shape Up (Singer, 2019), for which no peer-reviewed evaluation was found."
- **Why it is drift:** The edit adds a definition, "real-world evidence", that the raw does not give. It is also inconsistent with the planning record. Shape Up has practitioner use and trial reports (`planning/02-methodology.md`), which counts as real-world evidence. It failed because it had no *peer-reviewed* evidence. The sentence therefore now contradicts itself.
- **Minimal fix:** "A proof rule then required peer-reviewed evidence, and Shape Up (Singer, 2019) failed it because no peer-reviewed evaluation was found."

### R5. 3.3: an incorrect number has been added ("two similar integrations")
- **Edited:** "An inconsistency between two similar integrations reached a release, and an authorisation test matrix is the kind of check that would catch it."
- **Raw:** "This inconsistency between similar integrations reached a release; an authorisation test matrix is the kind of check that would catch it."
- **Why it is drift:** The previous sentence names three integrations: SimpleFIN and Pluggy AI lacked authentication, while GoCardless had it (S63-m2cq). "Two" is a new count that the source does not support. Changing "This" to "An" also loosens the link to the advisory just described.
- **Minimal fix:** "This inconsistency between similar integrations reached a release, and an authorisation test matrix is the kind of check that would catch it."

### R6. 4.2: a critical-evaluation judgement has been lost
- **Edited:** "Actual asks for private reporting and coordinated disclosure (Actual Budget, n.d.-h), which most OSS practitioners support but only 55% of studied vulnerabilities actually followed (Liu et al., 2025)."
- **Raw:** "The disclosure route itself is a strength. Actual asks for private reporting and coordinated disclosure (Actual Budget, n.d.-h), a practice most OSS practitioners support but which only 55% … (Liu et al., 2025)."
- **Why it is drift:** The raw makes an explicit evaluation: Actual's disclosure route is a strength, and the Liu et al. figure supports that by contrast. Without the evaluation, the paragraph is description only, and the 55% figure no longer has a stated purpose. This removes evaluative content.
- **Minimal fix:** Restore the lead sentence: "The disclosure route itself is a strength."

### R7. 4.5: a proposal now reads as Actual's current state
- **Edited:** "Each requirement is linked to its evidence: feature request, testable acceptance criteria, a PR referencing the issue, tests and the release note. Actual already has most of these links, and the independent reviewer checks that the chain is complete."
- **Raw:** "The model links each requirement to its evidence: … Actual already has most of these links; the independent reviewer checks that the chain is complete."
- **Why it is drift:** The raw attributes the complete chain to the proposed model. The edit drops "The model", so the first sentence reads as a statement of fact about Actual. It then conflicts with "Actual already has most of these links". The contract requires that the report never presents a recommendation as already adopted.
- **Minimal fix:** "Under the model, each requirement is linked to its evidence: …"

### R8. 4.6: the cost constraint is weaker and narrower
- **Edited:** "Cost limits the external part of the model."
- **Raw:** "Cost is a binding constraint."
- **Why it is drift:** The raw calls cost a *binding* constraint, without qualification. The edit softens "binding" to "limits" and restricts it to the external part. This weakens the critical evaluation, and the same drift appears in the executive summary (R2).
- **Minimal fix:** "Cost is a binding constraint, above all on the external part of the model." Or simply: "Cost is a binding constraint."

## OPTIONAL items (14)

These are minor nuance shifts. None of them goes beyond what the raw text and its sources support.

1. **Executive summary:** "The report recommends Kanban with explicit exit policies…" drops "tailored" from the approved wording ("Kanban, tailored, with mandatory QA gates"). The tailoring is implied by the listed additions, but "tailored Kanban" could be restored.
2. **Executive summary:** "Its users need correct figures and secure financial data" replaces "need to trust the numbers it shows and the security of their financial data". This loses the "trust" framing used in 1.2 and 3.1.
3. **1.1:** The raw's evaluative clause "their quality matters" was dropped. The causal sentence still makes the point.
4. **1.3:** "It does not cover data on the local device" is less explicit than the raw's "data on the local device stays unencrypted".
5. **2.5:** "Compared with today, the review queue is visible, limits are enforced and pull criteria are written and mandatory." Out of context, the present tense could be read as an observed state. "would be visible… would be enforced…" would remove that reading. The raw also used present tense ("The changes from today are…").
6. **2.5:** "Kanban sits on top of Actual's existing GitHub workflow" drops the raw's explicit "rather than replacing it". The meaning is mostly kept.
7. **3.1:** "the integrity of synchronised data" narrows the raw's general "data integrity". Migrations and local data fall under the raw scope too.
8. **3.1:** "produces those properties reliably" replaces "repeatedly". This is a small shift that overlaps with the Reliability characteristic.
9. **3.1:** "Self-hosters carry extra risk because their server holds bank-sync credentials" adds a risk judgement to the raw's description, which was only that they "also run a server holding bank-sync credentials". This is reasonable, but it is an inference.
10. **3.3:** "Set against the three attributes, these practices leave four gaps." The fourth gap (no written QA plan) is a process gap, not an attribute gap. Consider "these practices leave gaps in the three attributes and in the process".
11. **3.4:** The prose no longer refers to Table 3.2 before the table. Consider "Table 3.2 judges each candidate…".
12. **3.4:** "would give Actual a rating without removing any defects" is slightly more absolute than the raw's "a rating, not fewer defects".
13. **3.6:** "so a documentation change does not wait for an authorisation matrix" turns the raw's normative "should not wait" into a descriptive statement. It sits within the proposal, so the risk is low.
14. **4.1:** "Both points apply to Actual" refers to two points, but the supporting sentence (financial data, advisories) supports only the security-demonstrability point, not the in-phase cadence point. The raw's "This matters for Actual" was looser. In 4.3, the raw's "and the report does not present it as such" was also dropped. The meaning survives through "is not full IV&V in the IEEE sense".

## Summary

- REQUIRED: 8. These are R1 to R8: lost weakness framing, IV&V limits narrowed, changing requirements lost, proof rule misdefined, invented "two integrations", lost "disclosure route is a strength", proposal read as current state, and the cost constraint weakened.
- OPTIONAL: 14.
- Protected elements: intact apart from bold run-in labels, which are not protected.
- Contract: British English, third person and no padding are all observed.
