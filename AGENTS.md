# AGENTS.md

## Current writing-thread instructions (22 October 2026)

The author's instructions for this thread override the remote-publishing rules below:

- Work locally only. Do not push, open a pull request, or publish repository changes.
- Scope is Assignment 1. Deliver writing as Markdown; no PDF assembly is requested.
- Use British English, confirmed by the author.
- Preserve a complete normal draft under `report/assignment-1/before/` before reading or applying Humanizer. Then use the installed Humanizer skill to rewrite the whole report under `report/assignment-1/after/`.
- Preserve three versions and provide a Markdown comparison: raw, Humanizer, and a separate pstack `technical-writing` plus `unslop` rewrite from the same raw input. Keep the pstack output under `report/assignment-1/pstack/`; do not pass it through Humanizer. Humanizer is installed at `C:/Users/xingy/.codex/skills/humanizer/SKILL.md`, shared by the writing agents. The two pstack skills are installed alongside it.
- Delegated writing is authorised. The author approved the revised scores and retained Kanban with mandatory QA gates on 22 October 2026; Section 2.4 may be completed without further approval.
- The author subsequently requested a local commit of this work on `writing-experiment-6.1sol`. This commit is authorised; do not push or change `main`.
- On 23 October 2026 the author asked for the Opus 5.5 replication on `writing-experiment-opus5.5` to be committed and pushed to the matching remote branch. That push is authorised; `main` stays unchanged.
- On 27 October 2026 the author asked for `writing-experiment-opus5.5` to be merged into `main`. It was fast-forwarded and pushed. Work continues from `main`.

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
| `planning/05-writing-handoff.md` | **Start here for writing:** structure, word budget, rules, section briefs, workflow |
| `writing-experiments/claude-opus-5-5/run-1/raw-revised/document.md` | **Current working report** (Assignment 1). All further edits go here |
| `.claude/skills/report-review/SKILL.md` | Review-stage checklist (six problem areas found in Section 2). Use **only** when the author says they are reviewing the report, never while writing |
| `archived/` | Superseded versions and experiment records (former `report/`, the other `writing-experiments/` material, `WRITING-EXPERIMENT-PROTOCOL.md`). Reference only |

## Start here

- **Writing Assignment 1:** read `planning/05-writing-handoff.md` first.
- **Planning status and pending follow-ups:** `planning/README.md`.

## How to work in this repo

1. **Plan before writing.** Every section is discussed and agreed with the author first. Report prose is written only after a section's plan is marked *Agreed* in its `planning/` file.
2. **Don't assume. Ask.** If anything is unclear (scope, framing, a fact about Actual), raise it as an open question. Don't guess.
3. **Document every stage.** After each discussion, update:
   - the section's `planning/NN-*.md` file, under its *Agreed*, *Proposed* and *Open questions* headings;
   - `planning/discussion-log.md`, with a dated entry.
4. **Verify facts about Actual Budget** against primary sources (its repo, docs and blog) and record each one in `planning/research/` with its source. Mark anything unverified as *to verify*.
5. **Use the lecture material first.** When the lecture slides already cover something (a framework, selection factors, a model, a definition, terminology or a metric), use it or tailor it. Don't bring in an unfamiliar theory from outside that the lecturer and readers won't recognise. Outside sources may back up, strengthen or extend the lecture content, but they should not replace it. Slides are still not cited (see *Citations* rule 8): cite the original source the slide draws on, after checking it.
6. **Review stage.** When the author says they are reviewing the work or report, follow `.claude/skills/report-review/SKILL.md`. Don't apply it while drafting.
7. **Commit and push straight to `main`** after every change, with a clear commit message.

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
5. **Report References list = only what is cited.** The References section of each submitted report lists only the works actually cited in that report's text. Each in-text citation uses APA 7 author–date format, e.g. (Aboltins, 2025) or Aboltins (2025). `sources.md` is the wider research log, not the reference list.
6. **Paraphrase properly and quote sparingly.** Direct quotes go in quotation marks with a page or paragraph number, e.g. (Aboltins, 2025, para. 3).
7. **Recency: prefer sources from the last 5 years** (university preference). An older source is acceptable **only** if it is:
   - a **root** source (the original or defining source of the concept, e.g. the creator's own paper, book or guide); or
   - a **golden** source (seminal or highly cited in the field).
   
   Tag every entry in `sources.md` as *Recent*, *Root*, *Golden* or *Old*, and avoid citing *Old*.
8. **Lecture slides are not cited** in the report. They are used only as guidance. If a slide reproduces content from another source (e.g. a website), cite that original source directly after checking it.
9. **Never commit reference files the author supplies** (PDFs of books, papers, reports, etc.). They are shared for reading only, because of copyright and licensing. Log them in `sources.md` instead.

## Report writing rules

- **Appendices are not marked and don't count towards the word limit.** Use them **only** for supplementary "FYI" material.
  - Never move content the argument depends on into an appendix to save words.
  - Everything needed to understand and justify a section goes in the body.
- Third person throughout. The only exception is the personal-reason sentence in 1.1, which uses "I".
