# AGENTS.md

Every change, edit or piece of documentation is pushed straight to `main`. This repo is entirely for my individual assignment, and no coding is involved.

## What this repo is

- Module: CT051-3-3 Software Quality Engineering (APU), individual assignment.
- Chosen software product: **Actual Budget** (https://github.com/actualbudget/actual), an open-source, local-first personal finance (envelope budgeting) app.
- Assignment 1 (40%, Week 7): Introduction, Methodology, Quality Assurance Process, IV&V integrated with the selected methodology, References (APA 7th).
- Assignment 2 (60%, Week 14): Estimation, Risk Management Plan, Software Metrics, Requirement Analysis, Conclusion & Recommendation, References.
- The full brief is in `Assignment/`. A summary is in `planning/00-assignment-brief.md`.

## Layout

| Path | Purpose |
|---|---|
| `Assignment/` | Original assignment brief (.doc) |
| `Lecture Slides/` | Module lecture slides (L1–L12) |
| `planning/` | Planning and alignment notes, one file per report section |
| `planning/research/` | Verified facts about Actual Budget, with sources |
| `planning/sources.md` | Register of **every** source consulted (APA 7), with status and where it's used |
| `planning/discussion-log.md` | Dated log of what was discussed and decided in each session |

## How to work in this repo

1. **Plan before writing.** Every section is discussed and agreed with the author first. Report prose is written only after a section's plan is marked *Agreed* in its `planning/` file.
2. **Don't assume. Ask.** If anything is unclear (scope, framing, a fact about Actual), raise it as an open question. Don't guess.
3. **Document every stage.** After each discussion, update:
   - the section's `planning/NN-*.md` file, under its *Agreed*, *Proposed* and *Open questions* headings;
   - `planning/discussion-log.md`, with a dated entry.
4. **Verify facts about Actual Budget** against primary sources (its repo, docs and blog) and record each one in `planning/research/` with its source. Mark anything unverified as *to verify*.
5. **Commit and push straight to `main`** after every change, with a clear commit message.

## Citations and sources (plagiarism protection)

The university requires **APA 7th edition** referencing. Plagiarism risk is taken very seriously.

1. **Log every source, every time.** Anything gathered from outside goes into `planning/sources.md` **immediately**, with an ID (S01, S02…). This covers web searches, fetched pages, repository files, papers, standards, lecture slides and podcasts.
   - Include sources that were only skimmed, unreachable or rejected, and mark their status.
   - Each entry records:
     - the full APA 7 reference;
     - the URL and access date;
     - how it was found;
     - what was taken from it;
     - where it is used;
     - its verification status.
2. **Reference by ID in planning notes,** e.g. `[S05]`, so every fact can be traced back to its source.
3. **AI prior knowledge is not a source.** Anything the assistant states from memory, such as a paper, an author, a date or a statistic, is marked *unverified* in `sources.md`. It must be checked against the actual source before it is used in the report.
4. **Search snippets and summaries are not enough.** Read the actual source (or at least its abstract or official page) before citing it in the report.
5. **Report References list = only what is cited.** The References section of each submitted report lists only the works actually cited in that report's text. Each in-text citation uses APA 7 author–date format, e.g. (Janis, 2025) or Janis (2025). `sources.md` is the wider research log, not the reference list.
6. **Paraphrase properly and quote sparingly.** Direct quotes go in quotation marks with a page or paragraph number, e.g. (Janis, 2025, para. 3).
