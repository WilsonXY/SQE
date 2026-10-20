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
- Verified the history from Actual's blog (Roadmap for 2025, M. J. Aboltins; first logged as "M. Janis", corrected later): the commercial product closed and was open-sourced in early 2022, and PRs went unreviewed for months before the volunteer core team formed. The exact date of James Long's announcement is still *to verify*.

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

## 2026-10-20 — Session 1 (continued): source verification for Section 2

Decisions:
- **Lecture slides are not cited** in the report (the author confirmed this). They are used as guidance only.
- **Recency rule:** prefer sources from the last 5 years (2021 or later). Older sources are allowed only if they are a **root** source (the original or defining source) or a **golden** source (seminal or highly cited). Added to `AGENTS.md`.
- **Verify sources first,** before planning Section 3.

Verification done:
- **Correction:** the author of the Actual blog posts S10 and S12 is **Matiss Janis Aboltins** (from the blog's `authors.yml`). APA: Aboltins, M. J. (2025). This replaces "Janis, M.".
- All Actual docs and blog URLs return 200 (S02–S12).
- The Changelog #495 is verified (S15). James Long's 2022 post is unreachable, and archive.jlongster.com only goes to 2020. History stays "early 2022" (S10).
- Root and golden sources verified for every shortlisted methodology: Spiral S26, Scrum S34, XP S35, Kanban S28, DevOps S30, OSS baseline S24 and S25.
- Recent sources found and abstracts read: S36 (Kuhrmann et al., 2022, IEEE TSE), S37 (Kanban review, 2021), S39 (DevOps review, 2023, IEEE TSE), S41 (CI review, 2022, EMSE), S42 (methodology selection by multi-criteria decision-making, 2024, IEEE Access), S43 and S44 (GitHub Actions and review bots, EMSE).
- Remaining items are listed in `sources.md` → section D. They mostly need the APU library: the S38 abstract, book subtitles, and Springer article numbers.

## 2026-10-20 — Session 1 (continued): section D items closed

The author supplied PDFs (XP book excerpt, DORA 2024 report pp. 1–49, LF Open Source Maintainers 2023, Ahmad et al. 2018 Kanban mapping study) and a Google Books link for Anderson's *Kanban*.

Results:
- **S35 XP:** the year is **2005** (copyright page), not 2004. 2nd ed., Beck with Andres, Addison-Wesley.
- **S28 Kanban:** full title, publisher (Blue Hole Press) and year (2010) confirmed.
- **S24 Raymond:** full title, O'Reilly, 1999 confirmed (via Google Books).
- **S38 Kanban mapping study:** read in full. Key point: Kanban "needs to be supported by additional practices", which supports tailoring.
- **S40 DORA 2024:** read pp. 1–49. Four keys and rework rate; unstable priorities raise burnout. Also useful for Assignment 2 (metrics).
- **S47 LF maintainers report:** read in full. 32 maintainer interviews; burnout and automation findings. It **replaces S45** (2020, old).
- **Correction:** "start with what you do now" (Kanban) came from AI memory and wasn't verified. It is replaced by Anderson's definition "an evolutionary change method" (2010, p. 6), as quoted in S38.
- New lead: S49 Harzl (2016), *Combining FOSS and Kanban* (old; use only if nothing recent is found).
- The PDFs are kept out of the repo for copyright reasons.

**No blockers remain for Section 2.** Next: plan Section 3 (Quality Assurance Process).

## 2026-10-20 — Session 1 (continued): Section 3 first proposal

Research done (Actual repo at `27290a8`, logged in `research/` → *QA practices as-is*):
- Mapped the CI workflows (check, build, E2E/VRT, CodeQL, dependency review, CRDT, size), pre-commit hooks, the testing guide, the AI usage policy, release QA, and E2E encryption.
- **Apparent gaps (no evidence found):** test coverage measurement (disabled in sync-server), automated accessibility testing, `SECURITY.md`, performance testing in CI, and a written QA plan.

Proposed for Section 3 (waiting for the author):
- Flow 3.1–3.6 (as-is → gaps → to-be, mirroring Section 2).
- ISO/IEC 25010 (2023, to verify) as the quality model.
- Boundaries: Section 3 = QA process; Section 4 = IV&V and detailed testing; Assignment 2 = metric details.
- Evaluate OSS-specific standards (OpenSSF, OWASP, WCAG) alongside ISO/CMMI, and reject heavy certification standards with reasons.
- Full SQAP in an appendix.
- Possibly no new figure.

The candidate standards (S53–S61) are **unverified** and must be checked before writing.
