# Planning — Assignment 1

| Stage | File | Status |
|---|---|---|
| Brief summary | `00-assignment-brief.md` | Done |
| 1. Introduction | `01-introduction.md` | **Agreed** |
| 2. Methodology | `02-methodology.md` | **Agreed** (shortlist: Spiral, Scrum, XP, Kanban, DevOps + OSS baseline) |
| 3. Quality Assurance Process | `03-quality-assurance.md` | **Re-opened**: only 3 quality attributes needed (lecturer); choosing which 3 |
| 4. IV&V with selected methodology | `04-ivv.md` | **Agreed** |
| 5. Conclusion (optional) | — | **Excluded for now** (revisit during writing, depending on the word count) |
| Front matter | `05-writing-handoff.md` §1 | Cover page: **the author handles it**. Executive summary: **required by the brief**, written last. TOC and lists: generated at assembly. |
| References (APA 7th) | — | Built at the end from cited sources only |
| **Writing handoff** | `05-writing-handoff.md` | **Ready.** Writing starts in a new thread. |

Supporting files:
- `research/actual-development-process.md`: verified facts about Actual's development process and product, with sources.
- `discussion-log.md`: dated record of each session.
- `sources.md`: register of **every** source consulted (APA 7), with IDs, status and where each is used. The report's References list is built only from the sources actually cited.

## Draft A1 table of contents (current)

- Title page · Executive summary · Table of contents · List of figures/tables · Abbreviations
- 1 Introduction: 1.1 Background and purpose · 1.2 What is Actual Budget · 1.3 Main features and how it works · 1.4 Who is involved · 1.5 Main challenges
- 2 Software Development Methodology: 2.1 As-is process · 2.2 Characteristics and criteria · 2.3 Candidates · 2.4 Evaluation and selection · 2.5 Applying it (to-be) · 2.6 Critical evaluation
- 3 Quality Assurance Process: *to be planned*
- 4 Integrating IV&V with [Selected Methodology]: *to be planned*
- 5 Conclusion: *optional, to be decided*
- References · Appendices

## Front matter notes

- The official cover page templates are `Assignment/Assignment_1_-Cover_-_2026.docx` and `Assignment_2_...`. They need a **title/topic**, hand-out date and hand-in date. Submission is through Moodle.
- Open question: the report title, e.g. "Software Quality Engineering Evaluation of Actual Budget: Methodology, Quality Assurance and IV&V". To be decided.

## Figure plan (agreed for now): keep figures few and useful

| Fig | Section | Shows | Why it earns its place |
|---|---|---|---|
| 1 | 1.3 | How Actual works: device ↔ optional self-hosted sync server ↔ bank-sync provider | Explains "local-first" plus optional sync faster than text |
| 2 | 2.1 | As-is workflow: vote/issue → PR → CI → review → merge → monthly release | The evidence base for the whole of Section 2 |
| 3 | 2.5 | To-be workflow under the selected methodology | Shows what changes; Section 4 builds on it |

Tables (criteria, the matrix summary, stakeholders) are not counted as figures. More figures for Sections 3 and 4 will be decided when those sections are planned.

## Global writing rules (agreed)

- Third person only. **Exception:** the personal-reason sentence in 1.1 uses "I".
- Methodologies (and later, any technique or practice we recommend) must be **existing and proven in real-world use**, with evidence we can cite.
- **Words in tables count** towards the word limit.
- Appendices don't count towards the ~5,000 words (the lecturer confirmed this), and **appendix content earns no marks**. Use appendices only for supplementary "FYI" material. Never move essential content there to save words.
- Point of view: outside analysts. No contact with the Actual team.

## Word budget for Assignment 1 (agreed 2026-10-21; updated after the executive summary decision)

- Target: **about 5,000 words ± 5%** (4,750–5,250). The author prefers **slightly under 5,000**.
- **The executive summary counts** towards the ~5,000 (author's decision, 2026-10-21).
- **Words in tables count.** Appendices don't count (and aren't marked).
- Budget, roughly proportional to marks (Intro 5; Sections 2–4 10 each):

| Part | Budget |
|---|---|
| Executive summary | ~200 |
| 1 Introduction | ~530 |
| 2 Methodology | ~1,400 |
| 3 Quality Assurance Process | ~1,400 |
| 4 IV&V with Kanban | ~1,370 |
| (5 Conclusion) | excluded for now |
| **Total** | **~4,900** |

- **Executive summary:** required by the brief ("a title page, an executive summary page, a table of contents and figures, the report itself, and appendices"). One page that summarises the whole report, including results, for a busy reader. **Written last.** Not a marked section, but its words count.

## Pending follow-ups (non-blocking)

| Item | Owner | Status | If resolved |
|---|---|---|---|
| IEEE 1012-2024 full text via APU IEEE Xplore | Author (contacting the APU library) | **Error 418** directly, via EZproxy, and in a clean Chrome (2026-10-21) → likely an IEEE/APU-side block; the subscription may not include Standards anyway | Revisit the Section 4 risk tiers (switch from our own tiers to IEEE's integrity-level scheme); cite IEEE directly for independence |
| ~~Does the executive summary count towards ~5,000 words?~~ | Author | **Resolved 2026-10-21: it counts.** Body trimmed to ~4,700 (+ ~200 summary = ~4,900). | — |
| Smith & Hayes (2024) full text (S69) | Author | Blocked by the same IEEE 418 | Cite beyond the abstract |
| Article numbers for S41, S43, S44 | Author / writing stage | Open | Complete the APA references |
