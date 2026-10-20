# Discussion Log

## 2026-10-20 — Session 1

**Covered:** the assignment brief, the A1 table of contents, then Sections 1 and 2 in detail.

Decisions:
- Work section by section, slowly. Sections 1 and 2 first, then 3, 4 and 5.
- Don't assume; raise questions. Document every stage in `planning/`.
- Every change is pushed straight to `main` (see `AGENTS.md`).
- Introduction: fold "purpose and scope" (old 1.6) into 1.1. Keep it dead simple, with only brief signposting of later sections.
- Methodology: start from Actual's as-is workflow, then ask which methodology would suit best if a proper one were adopted. Candidates aren't limited to the common ones. Choose on effectiveness, not popularity.

Research done:
- Verified Actual's development process from its repo and docs. See `research/actual-development-process.md`. Result: no named methodology, but a documented, automated, volunteer-driven workflow with a monthly release train.

Open questions: see the *Open questions* lists in `01-introduction.md` and `02-methodology.md`.

## 2026-10-20 — Session 1 (continued): answers on Sections 1 and 2

Decisions:
- Third person only throughout.
- Introduction: include the personal reason (finding a self-hostable open-source finance app for an old home laptop) and a very brief history. Use diagrams only where they add value. Keep 1.4 and 1.5 separate. Signposting to later sections is nice to have.
- Methodology: weighted matrix with the full version in an appendix (appendices excluded from the word count; the lecturer confirmed this). Flow 2.1–2.6 accepted provisionally. **No hybrid**: one existing, proven methodology. DevOps is a candidate. Point of view: outside analysts (this also applies to Assignment 2).

Research done:
- Verified the history from Actual's blog (Roadmap for 2025, M. Janis): the commercial product closed and was open-sourced in early 2022, and PRs went unreviewed for months before the volunteer core team formed. The exact date of James Long's announcement is still *to verify*.

Proposed and waiting for the author:
- Release Train is a release practice, not a candidate.
- The Bazaar/OSS model is a baseline only.
- Tailoring vs hybrid.
- Scrumban screened out.
- Shortlist of 7.
- Draft criteria C1–C10 with weights.
- The intro's personal-reason wording and the figure plan.

Noted for Assignment 2: as outside analysts, we need to decide what exactly is estimated and risk-planned. To discuss when Assignment 2 planning starts.

## 2026-10-20 — Session 1 (continued): closing Section 1, narrowing Section 2

Decisions:
- **Section 1 is agreed.** The personal-reason sentence uses "I" (the only exception to third person). The figure plan (3 figures across Sections 1–2) is OK for now.
- The history uses "early 2022" from Actual's own blog. James Long's original post returns 404, the archive the author found (archive.jlongster.com) couldn't be reached from the research environment, and the exact date isn't needed.
- Section 2 agreed: the shortlist and the C1–C10 criteria and weights, Kanban as the working hypothesis, Release Train as a practice (not a candidate), the Bazaar model as a baseline only, and tailoring allowed.
- **Proof rule:** a candidate must have real-world evidence. An established named combination (e.g. Scrumban) counts if it is proven. Unproven or weird methods are dropped.
- **Shortlist: 5 candidates + 1 baseline.**

Research done:
- Scrumban: evidence found (Nikitina et al., ICSSP 2012 case study; studies of distributed teams), so it passes the proof rule.
- Shape Up: no peer-reviewed evidence, only practitioner blogs, so it is **dropped**.
- Seven methods pass the proof rule, so 2 must be cut. Proposed **Option A**: Spiral, Scrum, XP, Kanban, DevOps (+ baseline). Lean is folded into Kanban, and Scrumban is cut because its parents are already in.

Waiting for the author: the shortlist choice (Option A, B or C).

## 2026-10-20 — Session 1 (continued): Section 2 closed; citation rules

Decisions:
- **Shortlist: Option A**: Spiral, Scrum, XP, Kanban, DevOps, plus the open-source (Bazaar) baseline. **Section 2 is agreed.**
- **Citation rules** (added to `AGENTS.md`):
  - Every source from web search, fetched pages, the repo, papers or slides is logged in `planning/sources.md`, with an APA 7 reference, URL, access date, what was taken, where it is used, and its status.
  - The report's References list contains only the sources actually cited.
  - The university requires APA 7th edition.
  - AI-memory references are flagged *unverified* until checked.
- Created `planning/sources.md` and back-filled every source from this session (S01–S33, plus a search log).

Next: plan Section 3 (Quality Assurance Process).
