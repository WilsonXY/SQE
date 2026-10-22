# Shared writing contract — run claude-opus-5-5/run-1

Applies to every writer and editor in this run. Where a writing skill's generic advice conflicts with this contract, the contract wins. These exceptions are fixed before any editor starts, so neither editing condition is rewarded for following a skill rule that the other correctly overrides.

## Task

Write Assignment 1 of CT051-3-3 Software Quality Engineering (APU): a business report analysing **Actual Budget**, an open-source, local-first personal finance app. Reader: the module lecturer/marker. Purpose: select and critically evaluate a methodology, a QA process and an IV&V integration for Actual, from an outside analyst's point of view.

## Scope

Assignment 1 only: executive summary, Sections 1–4, References. No conclusion section, no cover page, no TOC, no PDF. Appendices are not used.

## Language and voice

- **British English** (e.g. *organisation, prioritise, behaviour, licence* (noun), *programme* except "computer program").
- **Third person throughout.** One exception: the personal-reason sentence(s) in 1.1 use "I".
- Introduction: dead simple and straightforward. Elsewhere: clear academic report prose with **critical evaluation**, not description alone.
- Point of view: outside analysts recommending; no contact with the Actual team. Never state that Actual has adopted a recommendation.

## Required structure

| File | Owner (raw) | Headings |
|---|---|---|
| `00-executive-summary.md` | Coordinator | Executive Summary (written last) |
| `01-introduction.md` | Coordinator | 1 Introduction: 1.1–1.5 per `planning/01-introduction.md` |
| `02-methodology.md` | Methodology writer | 2 Software Development Methodology: 2.1–2.6 |
| `03-quality-assurance.md` | QA writer | 3 Quality Assurance Process: 3.1–3.6 |
| `04-ivv.md` | IV&V writer | 4 Integrating IV&V with Kanban: 4.1–4.6 |
| `references.md` | Coordinator | References (APA 7, only works cited) |

Use Markdown headings `#` for section titles (`# 2 Software Development Methodology`) and `##` for subsections (`## 2.1 ...`). Figures are plain-text diagrams in fenced code blocks, readable without rendering, with a caption line `*Figure N. Title.*` beneath. Tables use Markdown tables with a caption line `*Table N. Title.*` above. Figure numbers: Fig 1 in 1.3, Fig 2 in 2.1, Fig 3 in 2.5. Tables: number within your own section as `Table 2.1`, `Table 2.2` … (section-prefixed numbering avoids cross-writer clashes).

## Length rule

Total (executive summary + Sections 1–4) must be **4,750–5,250 words**; the author prefers slightly under 5,000. Section targets: executive summary ~200, Section 1 ~530, Section 2 ~1,400, Section 3 ~1,400, Section 4 ~1,370 (subsection splits in `planning/05-writing-handoff.md` §2 are guidance). **Words in tables, captions, headings and diagrams count.** References and HTML comments do not count. Counting method: `python writing-experiments/tools/count_words.py <file>`.

For the **editing conditions** (Humanizer and pstack), the same rule applies identically: the whole rewritten document must stay within 4,750–5,250 words. Within that range length is an observation, not a target. Do not add filler to reach a number.

## Evidence

- Use only the source pack listed in `input/source-pack.md` (the registered, verified sources in `planning/sources.md` and the evidence files in `planning/research/`).
- You may re-open the URL of an already-registered source to check a detail. **Do not add new sources.** If a material gap appears, stop and report it to the coordinator instead of guessing.
- Do not cite sources marked *Do not cite*, *Old*, *Unreachable* or *Not used*. Cite "details verified only" sources only for what was actually verified.
- AI prior knowledge is not a source. Every factual claim about Actual is cited.
- Preserve source qualifications (e.g. "no evidence found in the repository (October 2026)", dated counts, "this report's own design").
- Lecture slides are never cited.

## Approved content decisions (fixed)

- Methodology: **Kanban, tailored, with mandatory QA gates**, selected by the approved matrix in `planning/research/methodology-quality-reassessment.md` ("Revised score proposal under the unchanged agreed weights"): Kanban 102, OSS/Bazaar baseline 95 (non-selectable), DevOps 94, XP 82, Scrum 81, Spiral 72, out of 120. The 3/5 quality score rates methodology support, not Actual's software quality. No invented hybrid.
- Quality attributes in depth: **Security, Reliability, Interaction capability** (ISO/IEC 25010:2023), with a short 9-row rating table.
- **IEEE 730-2026** supersedes IEEE 730-2014 (cite the 2026 edition at scope level).
- GHSA-m2cq-xjgm-f668 publication date: **20 February 2026** (live GitHub record).
- Risk tiers in Section 4 are this report's own design, "inspired by" IEEE 1012's integrity-level concept.
- Preview/nightly builds do not include a sync server.
- A credited external vulnerability reporter does not by itself establish managerial or financial independence beyond what public evidence shows. A disclosed vulnerability is not evidence of an observed compromise.
- Further corrections recorded in `planning/research/writing-session-decisions.md` → *Evidence corrections during writing* apply.

## Citations

APA 7 author–date in text: (Ahmad et al., 2018, p. 98), Aboltins (2025). Direct quotes in quotation marks with page or paragraph number; paraphrase by default.

**Disambiguation placeholder (raw writers only):** many sources share an author and year (e.g. `Actual Budget, n.d.`). Write the S-ID in braces right after the year: `(Actual Budget, n.d.{S03})`, `(Actual Budget, 2026{S01})`, `(International Organization for Standardization & International Electrotechnical Commission, 2023{S53})`. Apply braces to every citation, not only ambiguous ones. The coordinator converts them to final APA suffixes at assembly. End each raw section file with an HTML comment listing the S-IDs cited: `<!-- Cited: S01, S03, ... -->`.

## Protected material (editing conditions)

Editors must keep unchanged: every citation (author, year, suffix, page/para locator) and the claim each supports; headings and their numbering; table and figure captions; table contents, including scores, ratings and weights; diagram text; numbers, dates, names, identifiers (e.g. GHSA IDs, CVSS 9.2, USD amounts); direct quotations; the References list. Editors may restructure the surrounding prose freely within the contract.

Task-specific overrides of generic skill advice:
- Keep academic parenthetical citations (do not convert to links or footnotes).
- Keep third person; do not switch to second person ("you") even if a skill prefers it.
- Keep genuine lists of categories (e.g. three kinds of independence, three goals, three attributes) and genuine evidence limitations/hedges, even if a skill warns against triads or hedging.
- Keep standard titles, proper names, technical notation and required headings in their exact forms.
- Keep the critical-evaluation content; style editing must not delete an argued limitation.

## Working rules

Work locally. Do not commit, push or publish. Keep report prose and process notes in separate Markdown files. Do not edit files outside your assigned output paths.

**Do not open** anything under `report/assignment-1/` (another model's outputs for this experiment) or under other runs in `writing-experiments/`. Raw writers must not open or apply any writing skill (Humanizer, wilson-humanizer, technical-writing, unslop).
