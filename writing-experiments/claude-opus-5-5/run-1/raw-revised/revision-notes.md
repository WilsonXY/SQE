# Revision notes: raw document, Section 2 (24 October 2026)

`document.md` here is the run-1 raw document with Section 2 rewritten after the author's feedback. The executive summary and references were updated to match. Sections 1, 3 and 4 are unchanged. The frozen original stays at `../raw/document.md` and still matches the hashes in `../raw/manifest.md`. The Humanizer and pstack conditions were not touched.

## Feedback addressed

| Feedback | Change |
|---|---|
| Sentences jump between points without building context; readers don't know where the section is going | Each subsection now opens by linking back to the step before it (as-is route → weak point → project profile → needs → screening → test → choice → application → limits). Points are chained with stated reasons ("because", "so", "which leaves"), and each list item is tied to the factor or evidence it comes from. |
| Self-made weights and scores feel weak | The weighted matrix (C1–C10, weights 1–3, scores 1–5, totals out of 120) has been removed. In its place: (1) Boehm and Turner's (2004) five home-ground factors profile Actual from cited evidence (Table 2.1); (2) the profile gives five needs, N1–N5; (3) each candidate's required elements, quoted or paraphrased from its defining source, are tested against the documented facts about Actual (Table 2.2). A contradiction rejects a candidate; an unmet need is a gap for tailoring. Neither table contains a number. |
| Writing needs to be grounded, with context behind each statement | The framework comes from a root source written by the creator of the Spiral model, and its Chapter 2 was read in full. Every rejection rests on a quoted or paraphrased requirement of that method (for example, the Scrum Guide's "commitment by the Developers" and "one person, not a committee"). The mandatory QA gates now follow from Boehm and Turner's rule that a mismatched factor is a "source of risk" needing disciplined practices. The previous draft only asserted them. |

## Argument in one line per subsection

- **2.1** Actual has a clear route but no methodology; review is the weak point, because only maintainers can do it.
- **2.2** Size, dynamism and culture are agile; personnel is agile but strained; criticality is mid-scale. That profile gives needs N1–N5.
- **2.3** Plan-driven and enterprise methods fail N1–N3. Five candidates are described by their required elements.
- **2.4** Scrum, XP and Spiral conflict with Actual. DevOps does not conflict but adds little (automation already exists; Actual runs no operations of its own). Kanban adds flow control on review, and QA gates cover its N5 gap.
- **2.5** The board is unchanged and now linked to N4 and N5.
- **2.6** Kanban's limits, the volunteer risk, the limits of the framework (2004; generic; qualitative positions), and the conditions that would reopen the choice.

## Evidence

- New: **S126** Boehm & Turner (2004), pp. 30, 31, 35, 39, 51, 54–57. Verified from the publisher's sample chapter; see `planning/sources.md`. The 2003 *Computer* article is closed access, so it was not read and is not cited (S127).
- Re-opened to confirm wording: S34 (Scrum Guide), S105 (XP primary practices), S109 (Kanban guide).
- No longer cited: S42 Song et al. (2024), which had supported the weighted matrix, and S37 Alaidaros et al. (2021), cut for length.
- Inferences labelled as analyst judgement in the text: Actual's position on each factor (2.6 says the positions are qualitative), and DevOps' operations side having "little to join" (from S10 plus S121).

## Counts (`writing-experiments/tools/count_words.py`)

| Part | Frozen raw | Revised |
|---|---:|---:|
| Executive summary | 200 | 169 |
| Section 2 | 1,432 | 1,748 |
| Sections total | 4,961 | 5,246 |

The total is inside the 4,750–5,250 range, but only just, and it is above the author's preferred "slightly under 5,000". The extra Section 2 words went into the linking sentences and the grounding; the shorter executive summary pays for part of it. Figure 2 was simplified slightly: the small-change/large-feature branch was removed because the prose no longer discusses it.

## Open questions for the author

1. Is Boehm and Turner's five-factor framework acceptable as the selection basis?
2. Should Sections 1, 3 or 4 be trimmed to bring the total under 5,000?
3. Should this approach also replace the weighted matrix in the planning files and the other experiment conditions?
