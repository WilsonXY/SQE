# Three-version comparison — claude-opus-5-5/run-1

Complete documents:

- Raw: `../raw/document.md`
- Humanizer: `../humanizer/document.md`
- pstack (technical-writing then unslop): `../pstack/document.md`

All three come from the same frozen raw input and share the same 49-entry reference list. Numbers are in `checks.md` and review outcomes are in `corrections.md`.

## How the passages were chosen

Five passages were fixed by file, subsection and paragraph position before any of them was read: executive summary paragraph 2; 2.4 paragraph 2; 3.6 paragraph 1; 4.3 paragraph 1; 4.6 paragraph 4. All are reviewed versions. Nothing was scored. The notes describe differences and do not rank the versions.

## 1. Executive summary, paragraph 2

**Raw**
> Actual has a defined workflow, with community-voted requests, pull requests, continuous integration, maintainer review and a monthly release train, but no deliberate methodology. Five candidates were scored against ten weighted criteria. Kanban scored highest (102 out of 120), ahead of DevOps (94) and Actual's current open-source model (95, used as a baseline). Kanban is therefore recommended, tailored with explicit exit policies, work-in-progress limits on review and mandatory quality gates. Its weakness is that it prescribes no technical quality practices.

**Humanizer**
> Actual has a defined workflow, with community-voted requests, pull requests, continuous integration, maintainer review and a monthly release train, but no deliberate methodology. Scored against ten weighted criteria, Kanban came first among five candidates with 102 out of 120. DevOps scored 94, and Actual's current open-source model, used as a non-selectable baseline, scored 95. The report recommends Kanban with explicit exit policies, work-in-progress limits on review and mandatory quality gates. Its weakness is that Kanban itself prescribes no technical quality practices, so those gates must carry the quality work.

**pstack**
> Actual has a defined workflow but no deliberate methodology. The workflow combines community-voted requests, pull requests, continuous integration, maintainer review and a monthly release train. The report scored five candidate methodologies against ten weighted criteria. Kanban scored highest (102 out of 120), ahead of DevOps (94) and Actual's current open-source model (95, used as a baseline). The report therefore recommends Kanban, tailored with explicit exit policies, work-in-progress limits on review and mandatory quality gates. Kanban's weakness is that it prescribes no technical quality practices.

**Notes**
- pstack moves the finding to the front and the list after it. It also names "the report" as the actor twice.
- Humanizer reorders the scores into separate sentences and adds "non-selectable".
- Humanizer's first draft dropped "weakness". Review B-R1 restored it, and the restored clause is the coordinator's own Humanizer wording.

## 2. Section 2.4, paragraph 2 (reasons for the scores)

**Raw**
> Kanban entered as a working hypothesis, and the matrix tested it, including on its weak criteria. Its lead comes from C2, C7 and C8. Pull-based work needs no Sprint commitment from volunteers, and WIP limits target the review queue that has stalled Actual before. Its C4 score of 3 rates **methodology support, not Actual's software quality**, because managing flow prescribes no tests. XP (test-first) and DevOps (automated feedback) score 4, yet neither is a complete security or accessibility scheme. DevOps is the strongest alternative (94). Extending existing pipelines is cheap (C7 = 4), but automation does not allocate scarce human review (C8 = 3). Scrum and XP lose on coordination cost, and Spiral on expert risk analysis (C2, C7 = 2).

**Humanizer**
> Kanban entered the matrix as a working hypothesis and was tested on its weak criteria too. Its lead comes from C2, C7 and C8. Under pull-based work, volunteers make no Sprint commitment, and WIP limits act on the review queue that has stalled Actual before. Kanban scores 3 on C4 because managing flow prescribes no tests; that score rates methodology support, not Actual's software quality. XP (test-first) and DevOps (automated feedback) score 4, although neither is a complete security or accessibility scheme. DevOps is the strongest alternative at 94. Extending Actual's existing pipelines would be cheap (C7 = 4), but automation does not allocate scarce human review (C8 = 3). Scrum and XP lose on coordination cost, Spiral on expert risk analysis (C2, C7 = 2).

**pstack**
> Kanban entered as a working hypothesis, and the matrix tested it, including on its weak criteria. Its lead comes from C2, C7 and C8. Pull-based work needs no Sprint commitment from volunteers, and WIP limits target the review queue that has stalled Actual before. Kanban's C4 score of 3 rates **methodology support, not Actual's software quality**, because a flow method prescribes no tests. XP (test-first) and DevOps (automated feedback) score 4, yet neither is a complete security or accessibility scheme. DevOps is the strongest alternative (94). Extending existing pipelines is cheap (C7 = 4), but automation does not allocate scarce human review (C8 = 3). Scrum and XP lose on coordination cost. Spiral loses on expert risk analysis (C2, C7 = 2).

**Notes**
- pstack is almost identical to raw. It resolves one pronoun ("Kanban's"), restores a verb ("Spiral loses"), and keeps the bold phrase.
- Humanizer removes the bold and puts the reason before the caveat. It also changes "is cheap" to "would be cheap", which is slightly more conditional.
- Reviewer B listed that change as optional, and it was not applied.

## 3. Section 3.6, paragraph 1 (cost of the QA plan)

**Raw**
> The plan's main cost is volunteer time. Actual's USD 2,000 monthly stipend pool pays for review and triage work (Actual Budget, n.d.-f), and the project has already experienced pull requests waiting months for review (Aboltins, 2025). Every new exit criterion adds load, and maintainer interviews identify administrative overhead as a burnout risk (Salkever, 2023). The gates are therefore scaled by risk (Section 4 proposes tiers): a documentation change should not wait for an authorisation matrix.

**Humanizer**
> The plan's main cost is volunteer time. Actual's USD 2,000 monthly stipend pool pays for review and triage work (Actual Budget, n.d.-f), and pull requests in the project have already waited months for review (Aboltins, 2025). Every new exit criterion adds load, and maintainer interviews identify administrative overhead as a burnout risk (Salkever, 2023). The gates are therefore scaled by risk (Section 4 proposes tiers), so a documentation change does not wait for an authorisation matrix.

**pstack**
> The plan's main cost is volunteer time. Actual's USD 2,000 monthly stipend pool pays for review and triage work (Actual Budget, n.d.-f), and pull requests in the project have already waited months for review (Aboltins, 2025). Every new exit criterion adds load, and maintainer interviews identify administrative overhead as a burnout risk (Salkever, 2023). The plan therefore scales the gates by risk, using the tiers proposed in Section 4. A documentation change should not wait for an authorisation matrix.

**Notes**
- Both editors made the same edit to the second sentence independently.
- Humanizer turns the colon into a result clause ("does not wait"), which states as fact what raw gave as a norm ("should not"). Neither reviewer marked this as required.
- pstack names the actor ("The plan") and splits the sentence.

## 4. Section 4.3, paragraph 1 (achievable independence)

**Raw**
> **Achievable independence.** A maintainer review is not full IV&V in the IEEE sense, and the report does not present it as such. Internally, the proposal adds an *independent reviewer* role for high-risk work: a maintainer who is neither the author nor the code owner of the affected area. This gives technical independence only. Managerial and financial independence must come from outside: the existing coordinated-disclosure channel and an optional, periodic funded external security audit. The Open Source Technology Improvement Fund (OSTIF) shows this is workable for OSS: it self-reports 24 audits published in 2025, with 231 security-relevant findings and over 98% fixed (Open Source Technology Improvement Fund, 2026). Financial independence is stronger when a third party, not Actual, pays.

**Humanizer**
> Inside the project, only technical independence is achievable, and a maintainer review is not full IV&V in the IEEE sense. The proposal therefore adds an *independent reviewer* role for high-risk work: a maintainer who is neither the author nor the code owner of the affected area. Managerial and financial independence must come from outside, through the existing coordinated-disclosure channel and an optional, periodic funded external security audit. The Open Source Technology Improvement Fund (OSTIF) shows that funded audits are workable for OSS: it self-reports 24 audits published in 2025, with 231 security-relevant findings and over 98% fixed (Open Source Technology Improvement Fund, 2026). Financial independence is stronger when a third party, not Actual, pays.

**pstack**
> **Achievable independence.** A maintainer review is not full IV&V in the IEEE sense, and the report does not present it as such. Inside the team, the proposal adds an *independent reviewer* role for high-risk work. The independent reviewer is a maintainer who is neither the author nor the code owner of the affected area. The role gives technical independence only. Managerial and financial independence must come from outside, through the existing coordinated-disclosure channel and an optional, periodic funded external security audit. The Open Source Technology Improvement Fund (OSTIF) shows that such audits are workable for OSS. It self-reports 24 audits published in 2025, with 231 security-relevant findings and over 98% fixed (Open Source Technology Improvement Fund, 2026). Financial independence is stronger when a third party, not Actual, pays.

**Notes**
- Humanizer removes the bold label and the sentence about the report itself (§25). It turns the paragraph's conclusion into its opening sentence and joins the role to the limitation with "therefore".
- pstack keeps the label and the self-reference. It replaces "This" with "The role" and splits the colon list into separate sentences.
- Both editors replaced the vague "this is workable" with a named referent.

## 5. Section 4.6, paragraph 4 (gates becoming ritual)

**Raw**
> Finally, gates can become ritual. Actual's own payment guide concedes that rubber-stamp reviews to earn points are theoretically possible (Actual Budget, n.d.-f); requiring cited ASVS IDs and named tests makes approval harder to fake but not impossible. ASVS covers technical security controls only (OWASP Foundation, 2025), leaving reliability and interaction capability to Section 3's gates.

**Humanizer**
> Gates can also turn into box-ticking. Actual's own payment guide concedes that rubber-stamp reviews to earn points are theoretically possible (Actual Budget, n.d.-f). Requiring cited ASVS IDs and named tests makes approval harder to fake, though not impossible. ASVS also covers technical security controls only (OWASP Foundation, 2025), so reliability and interaction capability rely on Section 3's gates.

**pstack**
> Finally, gates can become a formality. Actual's own payment guide concedes that rubber-stamp reviews to earn points are theoretically possible (Actual Budget, n.d.-f). Requiring cited ASVS IDs and named tests makes approval harder to fake, but not impossible. ASVS covers technical security controls only (OWASP Foundation, 2025), so reliability and interaction capability depend on Section 3's gates.

**Notes**
- The two editors converged almost word for word: same semicolon split, same "so … Section 3's gates" ending, and the figurative "ritual" replaced in both.
- They differ only in the replacement word ("box-ticking" vs "a formality") and in Humanizer's two uses of "also".

## Overall observations

- **Size of edit.** Both editors made light edits in this run (similarity to raw is 0.911 for Humanizer and 0.937 for pstack). Humanizer changed more, mostly by reordering sentences and merging or splitting them. pstack mostly split sentences, named actors and resolved pronouns.
- **Surface markers.** Humanizer removed almost all prose bold (32 → 3) and two-thirds of the "not X but Y" contrasts (12 → 4). pstack kept most bold (25) and every contrast (13), but cut semicolons from 21 to 6 and wrote the shortest sentences (mean 16.0 words).
- **Meaning risk.** Humanizer's pattern rules (staging, closers and openers) took out several evaluative sentences that carried the critical-evaluation argument: "Its weakness…", "The disclosure route itself is a strength." and "Cost is a binding constraint." The blind review restored them. pstack's single required correction was about certainty, not lost evaluation.
- **Contract overrides.** Headings, citations, tables and diagrams survived intact in both conditions. The pstack editor applied the per-section ±5% length rule and kept third person without being reminded.

## Limits of this comparison

- There is one run per condition, with one reviewer per condition. No blind reader study, preference scoring or AI-detector test was done.
- The editors' context and allocation differed, as in the original run. The three Humanizer section editors had their own drafting context, and the coordinator edited part of the Humanizer text. The pstack editor was a single fresh agent.
- The cross-model similarity gap (Opus 0.91/0.94 against GPT-6.1-Sol 0.75/0.80) cannot be attributed to the model alone. Both runs protected the same kinds of element, but this run told every editor to stay within ±5% of each section's frozen count. That pushes towards lighter edits. The prompts were also rebuilt from the protocol templates, not copied from the original run.
