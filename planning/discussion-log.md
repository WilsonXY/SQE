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

## 2026-10-20 — Session 1 (continued): Section 3 decisions; security correction

Decisions:
- **Never commit the PDFs the author supplies** (rule added to `AGENTS.md`).
- Section 3:
  - flow 3.1–3.6 OK (provisional);
  - **ISO/IEC 25010:2023**;
  - rate all 9 characteristics and go deep on the top 4–5;
  - boundaries agreed (3 = QA process, 4 = IV&V and detailed testing, Assignment 2 = metric details);
  - **no figures** for now.
- **Appendix rule:** appendices are unmarked "FYI" only; never move essential content there to save words (added to `AGENTS.md` and `README.md`). Consequences:
  - no full SQAP in the appendix (the compact QA plan goes in the 3.5 body);
  - the Section 2 matrix placement needs revisiting (question added to `02-methodology.md`).

Corrections and verification:
- **Correction:** "no SECURITY.md" was **wrong**. The author's screenshot showed a security policy and published advisories. The policy is an **org-level** file (`actualbudget/.github/SECURITY.md`), which the repo-only search missed. Verified (raw file fetched). Its release-notes link is broken (404).
- Advisories verified via the OSV.dev API: 10 for the npm packages (Oct 2025–Oct 2026), 1 critical, 3 high and 6 moderate, mostly sync-server access-control flaws. The screenshot shows a few more.
- ISO/IEC 25010:2023 verified (evs.ee: 9 characteristics, published 15.11.2023, replaces 2011). The changes come from the arc42 secondary source. **The author assumed 25010:2023 covers AI; it doesn't.** AI quality is ISO/IEC 25059:2023.

Waiting for the author:
- standards scope (A / B / C, with context given);
- the security framing (proactive vs reactive);
- using the advisories as evidence;
- advisory credits (who reported them);
- the severity-mismatch handling;
- whether the product has any AI features;
- the Section 2 matrix placement.

## 2026-10-20 — Session 1 (continued): Section 3 closed

Decisions:
- Section 3 **agreed**. Standards scope is **option B**.
- **Security is a top-priority attribute**; the gap is proactive pre-release security verification.
- Advisories may be cited.
- Use maintainer severity ratings and GitHub publish dates.
- ISO/IEC 25059 (AI) is out of scope.
- Section 2 matrix: the scored table goes in the body, with an optional FYI appendix.
- **Words in tables count** towards the word limit.

Evidence:
- The advisory credits (author's screenshots) show that the reporters of GHSA-m2cq (critical), GHSA-prp4 (high) and GHSA-cq9c (high) are **not core maintainers** (iamsilk, Rex50527, pyuysig). All were fixed by MatissJanis. This counts as independent verification, for Section 4.
- Standards verified (official scope/edition pages): ISO/IEC 25010:2023; IEEE 730-2014 (active; 2026 revision in development); **ISO 9001:2026** (published 16 Sep 2026, superseding the lecture's 2015 edition); ISO/IEC 27001:2022; CMMI V3.0 (2023); OWASP ASVS 5.0.0; **WCAG 2.2** (Actual still targets 2.1); ISO/IEC/IEEE 29119-1:2022.
- **Actual has no OpenSSF Best Practices badge and no public Scorecard result.**

Next: plan Section 4 (IV&V integrated with Kanban).

## 2026-10-21 — Section 4 first proposal

Research done:
- IEEE 1012-2024 is the current V&V standard (published 22 Aug 2025; replaces 1012-2016; abstract mentions integrity levels) [S67].
- NASA IV&V overview: technical, managerial and financial independence [S68].
- Smith & Hayes (2024), IV&V for agile projects [S69].
- Liu et al. (2025) on OSS vulnerability disclosure [S70].
- OSTIF 2025 report on funded OSS audits [S72].
- The Kanban "explicit policies" (entry/exit criteria) mechanism, from Ahmad et al. (2018) [S38].
- Actual: PR preview and nightly builds [S66]; **no evidence of an external security audit**.

Proposed (waiting for the author), see `04-ivv.md`:
- flow 4.1–4.6;
- the independence model (internal independent reviewer + external augmentation);
- integrity-level tiering;
- mapping Lecture 6's six phases onto six Kanban stages;
- an optional funded external audit;
- figure choice;
- the A1 word budget (~5,300 planned) and whether to include an A1 conclusion.

## 2026-10-21 — Section 4 answers; word budget

Decisions:
- Section 4 flow 4.1–4.6 OK.
- Phase mapping (Lecture 6's six phases → six Kanban stages) OK.
- Recommend an optional funded external audit, **and briefly state the cost limitation** of a donation-funded OSS project.
- **No figure** for Section 4 by default.
- **No Assignment 1 conclusion** for now.
- **Word count:** about 5,000 ± 5%, preferably slightly under. Budgets rebalanced: Intro 550, S2 1,450, S3 1,450, S4 1,400 = **~4,850**.

The author asked for more context on Q2 (independence model) and Q3 (risk tiers / integrity levels). Plain-language explanations with Actual examples were added to `04-ivv.md`.

Still open: Q2, Q3, and whether the executive summary counts towards the word limit.

## 2026-10-21 — Section 4: independence agreed; IEEE 1012 check; executive summary

Decisions:
- **Independence model agreed:** internal reviews give technical independence only, and full independence needs outsiders. This must be explained honestly in the report.
- **Risk tiers:** the author will check the APU library (IEEE Xplore) for IEEE 1012-2024 first. If it's not obtainable, we use our own three tiers, labelled "inspired by IEEE 1012". The steps are in `04-ivv.md`.
- The author asked what the "executive summary" is. It is required by the brief's deliverables (a one-page summary of the whole report). It was added to `README.md`, with the word-count implication. Still open: whether it counts towards the ~5,000.

Research done:
- The APU Library switched to IEEE Xplore on 1 Jan 2022 [S73]. Standards access is not yet confirmed.

## 2026-10-21 — Locating IEEE Xplore at APU

- The author couldn't find IEEE Xplore on the E-Resources page. It sits under the **"APU E-databases"** box (https://library.apiit.edu.my/apu-e-databases/) → "IEEE Xplore®" → "Access Here" (EZproxy).
- The library page lists APU's IEEE subscription as **POP conference proceedings (2017+) and STEM25 journals only, with no Standards**. IEEE 1012-2024 is probably not accessible, so the likely outcome is our own three tiers. The author will confirm with a quick search.
- Side benefit: through EZproxy the author can probably read S69 in full and fill in the S41/S43/S44 article numbers (SpringerLink).

## 2026-10-21 — IEEE 1012 check result; Section 4 agreed

- The author's IEEE Xplore attempt gave **"Error 418"**, and the APU subscription lists no Standards anyway. As agreed beforehand, we **use our own three risk tiers**, labelled "inspired by IEEE 1012".
- **Section 4 is agreed.** All four Assignment 1 sections are now planned and agreed.
- Still open (not blocking planning): whether the **executive summary** counts towards the ~5,000 words.

## 2026-10-21 — IEEE Xplore retry

- The author retried in a private window. The APU login worked (the URL became `ieeexplore-ieee-org.ezproxy.apu.edu.my`), but IEEE Xplore still returned **Error 418**. Since 418 appears both directly and via EZproxy, the cause is likely browser-level bot protection.
- Suggested next steps: a clean browser with no extensions (Chrome/Edge); "Institutional Sign In" on IEEE Xplore (not ieee.org); otherwise the library's Get Help.
- Fallback unchanged: our own three risk tiers ("inspired by IEEE 1012").

## 2026-10-21 — IEEE access: final attempt for now

- The author tried a brand-new Chrome browser, and Xplore via EZproxy (`ieeexplore-ieee-org.ezproxy.apu.edu.my`) still returned **Error 418**. So the problem is on IEEE's or APU's side, not the browser.
- **Decision:** go with **our own risk tiers** for now. The author will keep trying and will contact the APU library. Revisit if access works (tracked in `README.md` → *Pending follow-ups*).
