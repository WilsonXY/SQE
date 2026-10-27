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

## 2026-10-21 — End of the planning thread; writing handoff

Decisions:
- **Cover page:** the author will handle it.
- **Executive summary:** the author asked whether the introduction can replace it. **No.** The brief lists "an executive summary page" as a required deliverable, and the two do different jobs (the executive summary summarises the whole report *including results* and is written last; the introduction sets up the topic, with no results). Still open: whether it counts towards ~5,000 words (the author will ask the lecturer).
- **Writing will start in a new thread.** Created `planning/05-writing-handoff.md`, covering:
  - the final structure;
  - the word budget;
  - all writing rules;
  - a brief per section with its sources;
  - the pre-writing source checks;
  - source readiness;
  - the per-section workflow;
  - a suggested opening message.
- `AGENTS.md` now points to the handoff ("Start here"), and the draft location is `report/assignment-1/`.

Flagged for the writing thread:
- Section 2 **matrix scores are not yet agreed** (propose and get approval before drafting 2.4).
- The **spelling convention** (British vs American) is to be decided with the author.
- The final assembly format/tool is to be decided with the author.

## 2026-10-21 — Executive summary counts towards the word limit

- **Decision (author):** the executive summary **counts** towards the ~5,000 words.
- Budget rebalanced to stay slightly under 5,000: executive summary ~200, Intro ~530, S2 ~1,400, S3 ~1,400, S4 ~1,370 = **~4,900**. The sub-budgets were updated in every planning file, `README.md` and `05-writing-handoff.md`.

## 2026-10-21 — Lecturer feedback: only 3 quality attributes

- The author confirmed with the lecturer that Section 3 needs **only 3 quality attributes** (examples given: security, performance).
- The author asked what "rating in a table" meant. Shown: a 9-row ISO/IEC 25010:2023 table (characteristic, one-line reason for Actual, High/Medium/Low priority) whose purpose is to show deliberate selection.
- Proposed: **Security, Reliability, Functional suitability**. Performance is not recommended (low risk, little evidence). Alternatives: Interaction capability, Maintainability.
- Pending: the author's choice of the 3, whether to keep the short rating table, and confirmation of the knock-on effects on 3.3–3.5.

## 2026-10-21 — Section 3 re-agreed with 3 attributes

- **Attributes:** Security, Reliability, **Interaction capability** (the author swapped functional suitability for interaction capability).
- Keep the short 9-row ISO/IEC 25010:2023 rating table (~120 words).
- Knock-on effects agreed: 3.3–3.5 focus on the 3, and freed words go to 3.6. Because interaction capability was chosen, **accessibility/WCAG 2.2 stays in full**; **functional suitability and performance** drop to brief mentions.
- Writing-thread caution recorded: the reason for leaving out functional suitability must be evidence-based.
- Section 3 is **Agreed** again. The handoff has been updated.

## 2026-10-22 — Local Assignment 1 writing thread

- Author overrides the repository push rule: all changes remain local; no push or publication.
- Deliver writing as Markdown, with complete before-and-after versions. Assignment 1 only.
- Author authorised delegated writers and requested installation of https://github.com/blader/humanizer . Installed using the skill-installer helper into the shared skills directory for all writers.
- Strict order: first complete normal writing without Humanizer; then read/apply the skill to rewrite the whole report.
- British English confirmed.
- Three section writers started (methodology, QA, IV&V); root handles introduction, assembly and references. Detailed decisions and evidence corrections: `research/writing-session-decisions.md`.
- Initial matrix proposed and saved to `research/methodology-matrix-proposal.md`. Author requested revisions and will explain. No approval recorded; Section 2.4 held while independent source checks and writing continue.

## 2026-10-22 — Methodology quality concern and revised proposal

- Author questioned Kanban's 3/5 quality-support score in an SQE assignment and asked whether a stronger-quality method could have fewer trade-offs.
- Reopened selection. Prepared `research/methodology-quality-reassessment.md` with fairer scores, a common retained technical baseline, mandatory proposed QA coverage and sensitivity checks. Reader-facing response: `../report/assignment-1/methodology-decision.md`.
- Corrected initial over-penalties for DevOps pipeline adoption and XP remote collaboration. Consistently distinguished explicit quality policies from prescribed engineering checks; neither Scrum nor Kanban automatically verifies all selected attributes.
- Revised unapproved totals /120: Kanban 102, baseline 95 (non-selectable), DevOps 94, XP 82, Scrum 81, Spiral 72. A quality-heavy scenario can favour DevOps by one point; that fragile difference is not evidence for a switch by itself.
- Normal drafts saved for Sections 1, 3 and 4 and for Section 2 except 2.4. Method-specific prose remains provisional. No executive summary or complete report has been frozen. Humanizer remains unread and unused until normal writing is complete.
- Await author's direction on methodology and revised scoring before dependent writing continues. No commits, pushes or publication of repository changes.

## 2026-10-22 — Completed Assignment 1 and three-version writing experiment

- Author approved the recommended revised matrix, retained Kanban and made QA checks mandatory. Section 2.4 completed under the original agreed weights.
- Author added a third, separate writing process using pstack technical-writing and unslop. Installed both from the official cursor/plugins pstack paths. Their shared instructions are available to the dedicated agent; no extra dependency was required.
- Completed and froze the normal report before applying writing skills to prose. Raw body plus executive summary: 4,873 approximate words. Raw hashes recorded in `../report/assignment-1/raw-manifest.md`.
- Original section writers read and used Humanizer 3.1.0 for complete prose rewrites, with final draft/rewrite/self-audit records. Humanizer total: 4,934.
- A separate agent used technical-writing then unslop on the same frozen raw draft, without reading Humanizer instructions, output or notes. Pstack total: 4,905. Academic third person, required APA citations and the agreed report structure override generic skill defaults.
- All versions preserve the 43 cited references, headings, captions, tables and text diagrams. Citation review passed; 82 mechanical checks had no failures. Semantic review corrected intermediate wording that overstated evidential certainty. No new facts or research were introduced by the style passes.
- Final reader files: `../report/assignment-1/before/report.md`, `after/report.md`, `pstack/report.md`; comparison and validation are linked from the reading guide.
- Author review is outstanding. The delivered Markdown is complete; no PDF or cover page was assembled. No commits, pushes, pull requests or upstream software changes were made.

Writing-tool source note: all three original section writers and the root writer read the installed Humanizer skill only after the full raw report was frozen. The dedicated pstack writer read the two installed pstack skills, applying them in that branch only. The root writer read pstack's instructions for comparative review only after the Humanizer prose was complete. Tooling sources remain outside report References; source register entries S124/S125 and installation hashes document provenance.

## 2026-10-22 — Standalone methodology for repeating the writing experiment

- Author requested one document about the experiment procedure, independent of assignment subject matter and output results, for reuse with another LLM.
- Created `../WRITING-EXPERIMENT-PROTOCOL.md` and linked it from the root README and existing experiment note.
- Recorded actual preparation, normal drafting, skill installation, frozen baseline, branch isolation, Humanizer and pstack application order, review/correction process and historical limitations.
- Included reusable prompts, input/agent controls, skill provenance, a run-record template and two distinct cross-model designs: each model's own raw draft or one shared editing baseline. Future refinements are explicitly distinguished from what occurred in this thread.
- Used the already-read technical-writing and unslop skills for the methodology document. No experimental report was restyled or modified. Frozen raw hashes were rechecked and match.
- All work remains local; no new model experiment, commit, push or publication was performed.

## 2026-10-22 — Local branch commit authorised

- Author requested moving the experiment work off main, then explicitly requested a commit on `writing-experiment-6.1sol`.
- Created that local branch from the existing checkout and preserved all tracked and untracked experiment files. The main branch pointer is to remain unchanged.
- Added a Git attribute to preserve experiment artifact bytes, because core.autocrlf is enabled and the frozen input contains mixed original line endings. This keeps recorded hashes valid in future checkouts.
- The local commit includes report variants, research records, the reusable protocol and planning updates. Remote push remains prohibited.

## 2026-10-22 — Writing experiment repeated with Claude Opus 5.5 (branch `writing-experiment-opus5.5`)

- The author asked for the same writing experiment to be repeated with Claude Opus 5.5, following `WRITING-EXPERIMENT-PROTOCOL.md`. The branch was created from `writing-experiment-6.1sol` at `dab5f8a`, so the planning inputs are identical.
- Design: own raw draft per model, with a close replication of the agent arrangement. The coordinator wrote Section 1, the executive summary and the references; three fresh writers wrote Sections 2–4; the same writers then applied Humanizer; one fresh agent applied technical-writing then unslop. The installed skill hashes match the original run.
- The agents were told not to open `report/assignment-1/**`, and no new sources were allowed. The raw draft was frozen at 4,961 words; the reviewed Humanizer version is 5,069 words and the reviewed pstack version 5,063.
- An extension to the original procedure: two blind reviewers, one per condition, with a shared correction policy. They found 8 required corrections in Humanizer and 1 in pstack, all applied, with pre-review drafts kept.
- All outputs, records and the comparison are in `writing-experiments/claude-opus-5-5/run-1/`. Everything stays local: no commit or push has been made in this session yet.

## 2026-10-24 — Section 2 rewritten after author feedback (Opus 5.5 run-1 raw only)

- The author reviewed `writing-experiments/claude-opus-5-5/run-1/raw/document.md` and asked for changes to Section 2 only: better flow between sentences for a reader new to the report; no self-made numeric weights; grounded statements throughout.
- The frozen raw file was kept byte-identical because the experiment hashes depend on it. The revision lives in `writing-experiments/claude-opus-5-5/run-1/raw-revised/document.md`, with notes in `raw-revised/revision-notes.md`.
- The weighted matrix was replaced with Boehm and Turner's (2004) five home-ground factors (new source S126, Chapter 2 read in full from the publisher's sample chapter), five derived needs (N1–N5) and a conflict/gap test against each method's defining source. Kanban with mandatory QA gates is still the outcome. The executive summary was updated to match, and the references were updated: Boehm & Turner (2004) added, Song et al. (2024) and Alaidaros et al. (2021) removed.
- S34, S105 and S109 were re-opened to confirm quoted wording. The new section totals 1,748 words and the document 5,246 (limit 5,250).
- The approach is recorded as *Proposed* in `02-methodology.md`, pending author confirmation. The changes were committed and pushed to `writing-experiment-opus5.5`, as authorised for this branch.

## 2026-10-24 — Direction after reviewing the Section 2 revision

- The author is dropping the other versions (the Humanizer and pstack conditions, and the planning matrix files). Further modifications continue from the revised raw document only: `writing-experiments/claude-opus-5-5/run-1/raw-revised/document.md`. No files were deleted.
- Word count is deferred: don't constrain edits by length for now; the author will deal with it later.
- `.obsidian/` was added to `.gitignore`. The change was pushed to `writing-experiment-opus5.5` for review.

## 2026-10-24 — Other versions archived

- The author asked to keep only the version in focus and move everything else into a new `archived/` folder.
- Kept in place: `writing-experiments/claude-opus-5-5/run-1/raw-revised/` (`document.md` and `revision-notes.md`).
- Moved with `git mv`, keeping relative paths: `report/` → `archived/report/`; `WRITING-EXPERIMENT-PROTOCOL.md` → `archived/`; `writing-experiments/README.md` and `tools/` → `archived/writing-experiments/`; the run-1 `raw/`, `humanizer/`, `pstack/`, `review/`, `input/`, `run-record.md` and `blind-key.md` → `archived/writing-experiments/claude-opus-5-5/run-1/`. Nothing was deleted.
- Updated pointers in `README.md`, `planning/README.md`, the `AGENTS.md` layout table, `.gitattributes` and the revision files. Older dated log entries keep their original paths as history. `planning/` and the source register stay where they are.

## 2026-10-24 — Section 2.3 screening paragraph replaced

- The author found the 2.3 longlist paragraph out of context. They agreed to replace it with one sentence giving the reason for the five candidates (each represents a different approach) and one plain sentence on why plan-driven methods such as Waterfall were not shortlisted, citing Boehm & Turner (2004, p. 31).
- "kept because" in the Spiral bullet became "included because", since the screening step is no longer shown.
- Shape Up (Singer, 2019) and Scrumban (Meireles et al., 2026) are no longer cited and were removed from the References. Both stay in `sources.md` (S22, S18).
- Word count was not considered, per the author's earlier instruction.

## 2026-10-26 — Section 2 rewritten for a fresh reader

- Author feedback: Section 2 read as if written for the writer, not a new reader. Needed context was missing, some points were over-explained, and insider terms went unexplained. The author confirmed the diagnosis: shorthand phrases, table headings not explained, and no signposting between methods.
- Rewrote all of Section 2 in `raw-revised/document.md`:
  - added an introduction;
  - defined terms at first use;
  - turned the requirements into named rows of a table, with the brief's lens column;
  - defined clash and gap before the evaluation table;
  - signposted 2.4 with first, next and finally;
  - added plain-language explanations of 2.5 and 2.6.
- The executive summary's methodology paragraph was rewritten in plain terms. DORA (n.d.) and DORA (2024) were added to the References (existing sources S123 and S40). Word count was not constrained, per the author.

## 2026-10-26 — Section 2.3 candidates turned into a table

- Author feedback: the candidate descriptions should be a simple table without citations. The report's focus is SQE, not teaching methodologies, and the reader is new to the report but technical.
- The five bullet descriptions were replaced with Table 2.3 (candidate, approach, what it requires of the team). The evaluation table was renumbered to Table 2.4.
- Amaro et al. (2023) [S39] is no longer cited and was removed from the References. Boehm (1988), Schwaber & Sutherland (2020), Beck & Andres (2005) and Kanban University (n.d.) are still cited in 2.4 and 2.5.
- Guidance noted for later edits: write for a technical reader who is new to the report. Don't define basic software terms.

## 2026-10-26 — Section 2.4 tightened

- Merged the Scrum and XP clash paragraphs into one summary: both assume team members who commit their time together, which Actual's self-selecting volunteers and vote-driven priorities cannot provide. The Boehm & Turner p. 35 point was dropped from this paragraph; it is still cited in Table 2.2.
- Simplified the DevOps paragraph to its SQE point. DevOps adds automated testing, which Actual's CI already provides, and operations integration, which has little to attach to. Neither of these addresses human review. DORA (2024) [S40] is no longer cited and was removed from the References; DORA (n.d.) [S123] is still cited.

## 2026-10-27 — Lecture selection factors checked

- The author asked whether the lecture slides cover how to choose a methodology, preferring material the lecturer is familiar with over a less familiar theory.
- Lecture 2 has "how to choose" slides with eight factor pairs: requirements clarity; size and complexity; flexibility; customer involvement; risk tolerance; time constraints; team expertise; regulatory compliance. Their text matches GeeksforGeeks (2025), *How to choose the best SDLC model for your project*, logged as S128 (low credibility; not yet cited).
- Options presented to the author. Decision pending.

## 2026-10-27 — Lecture-first rule added; Section 2 retailored

- The author chose option 1: Lecture 2's eight selection factors as the framework (cited to GeeksforGeeks, 2025), backed by Boehm & Turner (2004).
- The author added a rule, now item 5 under "How to work in this repo" in AGENTS.md: when the lecture slides cover something, use or tailor it rather than introducing an unfamiliar outside theory.
- All twelve lecture decks were converted to text to rescan Section 2. Changes:
  - lecture definition of a process model in the section opening;
  - "linear" versus "iterative/agile" vocabulary;
  - Table 2.1 rebuilt on the eight factors plus culture;
  - 2.3 screens Waterfall, V-Model, RAD and RUP;
  - Table 2.3 takes the lecture comparison table's suitability and drawback columns;
  - 2.4 cites the Spiral and Kanban entries from that table;
  - 2.5 uses Lecture 7's lead time and cycle time.
- Flagged to the author:
  - DevOps is not in the lecture comparison.
  - The RAD and RUP screening sentence draws on lecture content and has no citation.

## 2026-10-27 — Boehm & Turner removed

- The author asked to remove Boehm & Turner (2004) as backing entirely, because Section 2 is now tailored to the lecture material.
- Removed every citation and dependency:
  - the exec summary clause;
  - the 2.2 framework sentence and the culture factor (its volunteer-choice point moved into the team expertise row);
  - the team-expertise and risk-tolerance explanations, now grounded in the lecture's own rules (GeeksforGeeks, 2025);
  - the "mix of methods" paragraph, now resting on GeeksforGeeks's advice to consider hybrid models;
  - the requirement rationales;
  - the Waterfall/V-Model screening;
  - the 2.4 verdict wording;
  - the 2.6 evidence-limits sentence.
- Removed the reference. Boehm (1988), the Spiral paper, stays cited.

## 2026-10-27 — 2.4 Kanban and verdict paragraphs rewritten

- The author found the last two paragraphs of 2.4 unclear ("talking to yourself").
- They were rewritten as plain statements. The Kanban paragraph now names the problem it fixes, then lists its three additions (review WIP limit, written stage rules, self-chosen tasks) with "first, second, third". The verdict paragraph now separates three things: the comparison with today's process, the one unmet requirement (no quality checks) and why it matters (low risk tolerance), and the QA gates that fill it.

## 2026-10-27 — WIP-limit sentence in 2.4 clarified

- The author asked where the WIP-limit sentence comes from. The answer: limiting WIP is a core Kanban practice (Kanban University, n.d. [S109]; Ahmad et al., 2018, pp. 97–98 [S38]). Placing the limit on review is this report's proposal, based on Actual's review bottleneck (S02, S08, S10).
- The sentence now defines WIP, cites the Kanban guide and states that placing the limit on review is the report's proposal.

## 2026-10-27 — 2.6 simplified

- The author found 2.6 verbose. It was cut to four short paragraphs with the same points and citations: Kanban's weakness and why the QA gates are mandatory; the WIP limit in a volunteer project; the limits of the evidence; when to revisit the choice. The stray "Second, …" opener without a "First" was fixed.

## 2026-10-27 — Review-stage skill created

- The author finished reviewing Section 2 and asked for the recurring problems to be summarised. Six areas: weak grounding; writing for the writer, not the reader; wrong focus or reader level; unfamiliar theory instead of lecture material; citation and accuracy slips; compression, verbosity and repetition.
- Created the repo skill `.claude/skills/report-review/SKILL.md`. It triggers only when the author says they are reviewing the work or report, never during writing. It holds the six areas as a checklist, with examples from Section 2 and a short review procedure. Pointers added to the `AGENTS.md` layout table and to "How to work in this repo" (item 6).

## 2026-10-27 — Branch merged to main

- The author asked to merge `writing-experiment-opus5.5` into `main` before starting the Section 3 review in a new session. `main` was an ancestor of the branch, so it was fast-forwarded and pushed.

## 2026-10-27 — AGENTS.md cleaned up for single-version work

- The author asked to remove the "Current writing-thread instructions (22 October 2026)" block. Those rules applied only to the multi-model writing experiment (raw/Humanizer/pstack versions, the 6.1sol and Opus 5.5 branches and their push restrictions). From now on the author works on one version only.
- The block was removed. "Use British English", a standing author decision, moved to "Report writing rules". "Commit and push straight to `main`" became "Commit and push straight to the remote", both in the intro sentence and in rule 7.

## 2026-10-27 — Working report moved to a neutral path

- At the author's request, the single working report moved from `writing-experiments/claude-opus-5-5/run-1/raw-revised/document.md` to `report/assignment-1/report.md`. Its experiment header line ("raw condition (run claude-opus-5-5/run-1) …") was replaced with the plain working-title note.
- The Section 2 revision notes were moved to `archived/writing-experiments/claude-opus-5-5/run-1/raw-revised/revision-notes.md`. The empty `writing-experiments/` folder is gone, and its `.gitattributes` rule was removed.
- Pointers updated in `AGENTS.md`, `README.md`, `planning/README.md` and the report-review skill. Older log entries keep their original paths as history.

## 2026-10-27 — Section 3 review: all ten findings applied

- New session on `claude/great-shannon-hm15ak` (level with `main`). The author moved from the Section 2 review to Section 3. Section 3 was checked against the `report-review` skill and lecture decks L1, L3, L4 and L5 (converted to text in the scratchpad).
- Ten findings were reported; the author asked for all of them to be applied and pushed for their review:
  1. 3.5 now uses Lecture 3's SQAP sections (new Table 3.4) instead of an undefined "IEEE 730 planning-and-control concern".
  2. 3.2 states the rating rule (harm and current checks) before Table 3.1, which now has *Harm* and *Current checks* columns. Ratings unchanged.
  3. 3.4 states the fit and cost tests and defines the decision labels before Table 3.2. The text after it no longer repeats the table.
  4. OpenSSF Scorecard and the badge are tied to the security gap and placed in the plan (Release train).
  5. Risk tiers moved into 3.5 (from 3.6), with a new *Applies to* column in Table 3.3.
  6. A Section 3 opening defines QA and signposts the section. 3.1 uses Garvin's (1984) five approaches (S129).
  7. "Exit policy" is used throughout (3.5 and the executive summary), replacing "Definition of Done".
  8. The authorisation test matrix is defined and marked as this report's proposal. The 3.2 advisory claim is cited. Owners are stated as existing roles. The synthetic-data criterion is left to Section 4.
  9. Shorthand removed ("release baseline", "advisory pattern", "planning-and-control idea"). The performance sentence moved out of the QA-plan bullet. The 404 link detail dropped.
  10. 3.6 links the automation evidence to the proposed checks and gives three numbered limits.
- Sources: S129 Garvin (partially verified, official page) is added to References. S130 (Sommerville), S131 (origin of the SQAP sections) and S132 (IEEE QA definition) could not be reached and are logged as unverified. The SQAP section list and the QA definition are used **without a citation** and flagged to the author.
- Section 3 grew from about 1,550 to about 2,570 words. Clarity came first; the author handles word count.
- Out of scope, noted for the Section 4 review: the IEEE 1012 reference URL points to `standards.ieee.org/ieee/1800.2/7324/`, a different standard.

## 2026-10-27 — 3.2 cut to the three attributes

- On review, the author asked for 3.2 to focus straight on the three attributes and not write much about the other characteristics.
- The nine-row rating table (Table 3.1) and the High/Medium/Low rating rule were removed. 3.2 now:
  - names the three attributes and the two conditions each meets (serious harm, and a public-evidence gap);
  - gives one bullet each for Security, Reliability and Interaction capability, with harm and gap;
  - keeps one sentence on why functional suitability is left out, since 3.1's "users trusting the numbers" makes it look like a candidate.
- Knock-on edits: 3.3 no longer refers to "High" attributes or to Table 3.1; the performance sentence now says it is outside the three attributes. Tables were renumbered: standards = 3.1, QA plan = 3.2, SQAP sections = 3.3.
- `planning/03-quality-assurance.md`: the "keep the 9-row rating table" decision is marked superseded.

## 2026-10-27 — Standards scope discussed; option 2 search for the SQAP source

- The author asked whether adopting so many standards makes sense. Recommendation: keep four, each with one job.
  - ISO/IEC 25010:2023 frames the section.
  - OWASP ASVS 5.0.0 closes the security gap.
  - WCAG 2.2 AA closes the interaction-capability gap.
  - IEEE 730, adapted, closes the missing-QA-plan gap.
  - Drop OpenSSF (it overlaps ASVS) and ISO/IEC/IEEE 29119-1 (Section 4 never uses it).
  - Shrink ISO 9001, ISO/IEC 27001 and CMMI to a short "considered, rejected" sentence, since Lecture 4 teaches them.
  - Reliability needs no standard; its gap is closed by the coverage measure.
  - **Not yet applied.**
- The author asked what dropping IEEE 730 would cost. Answer:
  - the SQAP section list in Table 3.3 would be an uncited factual claim;
  - presenting someone else's structure without attribution is a plagiarism risk;
  - the plan would lose its only process standard.
- The author chose option 2: find and verify the original source of Lecture 3's SQAP sections. Result (S133, sources.md):
  - The list matches the **IEEE 730-2002 and earlier** plan outline.
  - IEEE 730-2014 replaced that outline. It is "more like a whole new standard", organised into process implementation, product assurance and process assurance, with 16 tasks.
  - 730-2026 now supersedes 2014.
  - Pressman's text and the 2002 standard could not be read.
  - No current, readable source for Lecture 3's list exists, so option 2 cannot give Table 3.3 a proper citation. Options were put back to the author.

## 2026-10-27 — Standards trimmed; option 1 for the plan areas

- The author approved the standards trim and chose option 1.
- 3.4:
  - The two tests are now inclusion rules.
  - Table 3.1 lists four adopted standards with the gap each closes and how it is used.
  - Separate bullets cover ASVS, WCAG 2.2 and IEEE 730-2026; the IEEE 730 bullet says it is applied in intent only.
  - One line says reliability needs no standard.
  - One paragraph rejects ISO 9001, ISO/IEC 27001 and CMMI on cost, while linking their ideas to 3.1 and 3.5.
  - OpenSSF and 29119-1 were removed, along with their three references.
- 3.5: Scorecard was removed from the Release train exit policy. The "SQAP is usually organised into standard sections" claim was replaced: Table 3.3 now presents the plan's seven areas as the report's own design.
- 3.6: Scorecard was removed from the automation list. The limits are now two (the OpenSSF self-assessment limit was dropped), and the IEEE 730 caveat now points to 3.4.
- Executive summary: "and OpenSSF tools" removed.
- Section 3 is now about 2,160 words (it was about 2,570 after the first review pass).

## 2026-10-27 — IEEE 730 rejected because its text is paywalled

- The author asked whether IEEE 730 being paywalled is a problem. Answer: yes, by the report's own cost test. Volunteers cannot consult a standard they are meant to follow, and the report could only claim "intent only". ASVS and WCAG are free; ISO/IEC 25010 is paid but is used only for attribute names.
- Applied: the cost test now requires standards that contributors must follow to be free to read. IEEE 730-2026 moved to the rejected paragraph, citing the official catalogue for its scope and its purchase/subscription-only access (rechecked today). Table 3.1 now has three standards. The missing QA plan is closed by the report's own plan in 3.5. "Intent only" was removed from 3.4 and 3.6.

## 2026-10-27 — Rejected-standards paragraph trimmed

- The author asked to trim the rejected-standards paragraph in 3.4, since those standards are not used, and offered to remove them entirely.
- Recommendation: keep them, but cut them to two sentences. Lecture 4 teaches ISO 9001, ISO/IEC 27001 and CMMI, so naming them and the reason for rejecting each shows they were considered.
- Applied: the "no standard for the other two gaps" paragraph and the rejected-standards paragraph went from about 210 to about 100 words. The per-standard descriptions and the "ideas still reflected" sentence were removed. One sentence now covers IEEE 730 (paid access), and one covers ISO 9001, ISO/IEC 27001 and CMMI together (formal organisation; certification or appraisal). All four references stay cited.

## 2026-10-27 — 3.4 "other two gaps" sentence rewritten; coverage gap explained

- The author did not follow "No standard is adopted for the other two gaps…". It made the reader count the four gaps from 3.3, and "needs a measure" and "closed by the plan itself" were shorthand. It was rewritten to name the four gaps, say that only security and accessibility need a standard, say that reliability's fix is turning on a coverage report, and say that the missing QA plan is filled by the plan in 3.5.
- The author asked what the reliability gap is. Explained:
  - `packages/sync-server/vitest.config.ts` sets `coverage: { enabled: false }`, the root config has no coverage setting, and no coverage tooling was found, yet the PR checklist asks for "appropriate test coverage".
  - It is filed under Reliability because sync, migration and recovery code protects data integrity.
  - Weaknesses flagged: it rests on one config file and missing tooling, it is a missing measure rather than a shown failure, and coverage does not prove correctness.
  - Offered: search Actual's issues and advisories for sync or migration defects that reached users, or state in 3.3 that coverage is an indirect measure. Awaiting the author's decision.

## 2026-10-27 — 3.5 rebuilt; board columns explained in 2.5

- The author could not understand 3.5 or its two tables. Its purpose, the board model and how to read the table were explained in plain words, with a worked example (a new bank-sync provider versus a typo fix).
- The author found that Section 2 does not explain the board's mental model well, and asked for the 3.5 table to be ordered by Kanban column rather than by attribute.
- Applied:
  - 2.5 now has a six-item list of what happens in each column, and its sentence on the Verify QA gate was updated.
  - 3.5 was rewritten:
    - a purpose opening with a recap of the board;
    - the risk tiers;
    - a how-to-read sentence;
    - Table 3.2 by column, listing only added checks, each tagged with the attribute it protects;
    - owners, and Table 3.2 named as the written QA plan;
    - a worked example ending with where a flaw like GHSA-m2cq could be stopped ("could", in line with 3.3);
    - the measures.
  - Table 3.3 was removed.
- Section 3 is now about 2,210 words.

## 2026-10-27 — "Author" renamed "Implementer" in Table 3.2

- At the author's request, the Who column of Table 3.2 (Design and Build/PR rows) now says "Implementer" instead of "Author". The worked example in 3.5 was changed to match ("the implementer lists the new endpoints").
- Not changed (flagged to the author): Section 2.5's column list ("the author decides…", "the author writes the code…"), Figure 3 ("Reviewer is not the author") and Section 4 ("not author, not code owner"; "Validator other than the author").

## 2026-10-27 — 3.5 paragraphs merged

- The author asked whether the risk-tier paragraph was needed, and whether the table-intro and owners paragraphs could be merged.
- Answer: the tiers are needed, because Table 3.2's "Applies to" column and the worked example use "High tier". The full definition is not needed, because Section 4.3 already gives it.
- Applied: three paragraphs (risk tiers, how to read the table, owners) became one paragraph before Table 3.2, of about 100 words instead of about 190. It names Table 3.2 as the written QA plan, says how to read it, says the heavier checks apply only to High-tier cards (defined in 4.3), and says existing checks and people stay. The stipend citation in 3.5 was dropped; Actual Budget (n.d.-f) is still cited in 3.4 and 3.6.

## 2026-10-27 — "Implementer" used throughout

- At the author's request, the remaining uses of "author" for the person who builds a change were changed to "implementer": the 2.5 column list (Design, Build/PR), Figure 3 (Verify row; the ASCII alignment was kept), 4.3 (independent reviewer definition) and Table 4.2 (Build/PR and Verify roles). No body uses of "author" in that sense remain.

## 2026-10-27 — Reliability gap strengthened with release-note evidence

- The author approved option 1 (look for real reliability defects), with option 2 (admit the limit) as the fallback.
- Findings (S134–S136): the official 2026 release notes list sync and bank-sync data fixes:
  - a timestamp overflow when downloading a large sync, and the CLI failing to push changes to E2EE budgets (26.10.0);
  - Pluggy bank sync repeatedly rewriting transactions (26.8.0).
- None was reported as user data loss, and the notes do not say whether each bug reached an earlier release.
- Applied to the 3.3 reliability bullet: these fixes are cited as evidence that defects in this area are still being found, followed by the coverage gap. **Option 2's sentence was also added** (coverage shows only untested code, not correctness).
- Two references added: Fiddaman (2026) and Aboltins (2026).
- Flagged to the author, not changed:
  - 26.7.0 and 26.8.0 also fixed Balance Forecast double-counting and running-balance refresh bugs. This weakens 3.2's claim that functional suitability is "already checked".
  - 26.8.0 added a CI check that protects shipped migration files. This is an existing reliability practice that 3.3 could mention.

## 2026-10-27 — Commit-history search for reliability evidence

- The author asked how to give the session access to Actual's GitHub issues. Answer: issues need the Claude GitHub App installed on actualbudget/actual, which only that organisation's owners can do. The public code and commit history can be read without it. The author chose the commit-history search.
- The author also asked what the two flagged points were and how big their impact is. Answer:
  - (1) The calculation fixes undercut the 3.2 phrase "already checked". The impact is moderate for credibility, and the fix is one sentence.
  - (2) The 26.8.0 migration-protection CI check is missing from 3.3. The impact is low; it is a fairness point.
- Findings (S137–S139): the strongest reliability example is #8706 (26.10.0). A large sync could overflow a timestamp counter in privacy-focused browsers, so "the budget never opens", and the faulty loop had been in released code since at least April 2023. A core budget calculation bug (#7272, covering overspending from leftover balances, v26.4.0) was fixed with regression tests. The data and calculation fixes all added regression tests.
- Wording for 3.2 and 3.3 was proposed to the author; not yet applied.

## 2026-10-27 — Reliability example applied; functional suitability removed

- The author approved edit (A) and declined (B). They asked for every mention of functional suitability to be removed, since the section focuses on three attributes only.
- Applied:
  - the 3.3 reliability bullet now cites #8706 (Brown, 2026) instead of the release-note examples;
  - the functional suitability paragraph in 3.2 was deleted, and there are no other mentions;
  - References: Brown (2026) added; Fiddaman (2026) and Aboltins (2026) removed.

## 2026-10-27 — Measures paragraph removed from 3.5

- The author asked what the closing 3.5 paragraph was. It named one measure per attribute for Assignment 2: endpoint coverage of the authorisation matrix, test coverage, and accessibility violations. The author asked for it to be removed because it belongs to Assignment 2. Removed.

## 2026-10-27 — 3.6 simplification reverted

- At the author's request, the 3.6 simplification (commit 0c51861) was reverted with `git revert`. The author will simplify 3.6 themselves later. 3.6 is back to its previous three-paragraph version (about 230 words).

## 2026-10-27 — Section 3 review branch merged to main

- At the author's request, `claude/great-shannon-hm15ak` was fast-forwarded into `main` and pushed. It carries all of this session's Section 3 review changes.

## 2026-10-27 — Section 4 review started

- New branch `claude/section-4-review-tf1qs8` created from the latest `main` (which includes the merged Section 2 and 3 reviews).
- Section 4 (about 1,480 words) was read in full against the six problem areas in `.claude/skills/report-review/SKILL.md`, Sections 2.5 and 3.5, and Lecture 6's IV&V slides (phases with activities, tools, roles and outcome).
- Findings presented to the author, most serious first; nothing changed in the report yet:
  1. Tables 3.2 and 4.2 overlap and disagree on the same columns (where ASVS review happens; what Verify means; Section 2.5 says Verify is the PR review).
  2. The IV&V model is almost all security, although High tier also covers calculations, migrations and sync.
  3. Risk tiers are listed with no rule for assigning them.
  4. 4.5 repeats the 3.5 worked example and does not say what the independent check adds.
  5. Release-row disclaimer sentence in 4.4 is written for the writer.
  6. Tables 4.1 and 4.2 have no lead-in; "Partial" and "Not established" are not defined; insider terms (ADR, threat note, ASVS IDs, points, "independent-reviewer capacity counted within the WIP limits").
  7. Terminology drift: exit policy / entry and exit criteria / exit criterion / QA gate.
  8. Report proposals that read as if sourced (WIP-limit capacity sentence).
  9. "Section 3 defines what; Section 4 adds who" is not what the tables do.
  10. 4.6 repeats 3.6 (backlog, burnout, tier judgement, stipend).
  11. Two Assignment 2 mentions, while the author removed a similar one from 3.5.
  12. Smaller accuracy checks: NASA's financial-independence wording is not recorded in S68's notes; stipend described differently in 3.4 and 4.6; "merged straight away" wording in Table 4.1.

## 2026-10-27 — Section 4 review findings applied

- The author asked for all twelve findings to be applied, split if needed; they will review the result afterwards.
- Facts rechecked first (logged in `sources.md`, "Section 4 review: source rechecks"): NASA financial independence [S68], stipend scope, points and the rubber-stamp FAQ [S08], "approve and merge straight away" [S04], release-step order [S03], CODEOWNERS and the issue/PR templates [S01].
- Applied, by finding:
  1. Table 4.2 now matches 2.5 and 3.5: review and ASVS at Verify; Build/PR is automated only. A lead-in says how Table 4.2 builds on Table 3.2.
  2. Reliability check added to the Verify row (synthetic-budget totals before and after migration, sync or calculation changes); 4.6's ASVS sentence now states the limit of that check.
  3. Tier rule added in 4.3 (worst plausible failure; higher tier when in doubt).
  4. 4.5 early detection says what the independent reviewer adds beyond the test matrix (the GoCardless/SimpleFIN/Pluggy.ai inconsistency, checked at Design and Verify).
  5. Release-row disclaimer replaced with a plain statement of the smoke-test order.
  6. Lead-ins added for Tables 4.1 and 4.2; "Partial" and "Not established" defined; threat note, ASVS requirement numbers, decision record (replacing "ADR"), code owner and points explained; the WIP-limit sentence rewritten.
  7. "Exit policy" used throughout Section 4.
  8. The "Section 3 defines what, Section 4 adds who" sentence was removed; the 4.4 lead-in states the actual split.
  9. The WIP-limit idea is now marked "this report also proposes".
  10. Stipend described as "review and administrative work"; Table 4.1 says "approve and merge"; the external-audit sentence was merged into the table row.
  11. 4.6 rewritten to avoid repeating 3.6: independence versus expertise and flow (CODEOWNERS), with Salkever (2023) no longer cited in Section 4 (still cited in 2.6 and 3.6). Kanban University (n.d.) is no longer cited in Section 4 (still cited in 2.5). Both stay in References.
  12. Assignment 2 mention removed from 4.5; kept in 4.6.
- Word count: Section 4 went from about 1,480 to about 1,960 words.

## 2026-10-27 — Section 4.1 merged into the as-is subsection

- The author felt 4.1 (V&V, IV&V and why Actual needs them) was unnecessary. Answer: the independence definitions are needed (they are Table 4.1's columns), and so is verification versus validation (Table 4.2 marks activities that way). The rest was background in the wrong place or a repeat of 3.2 and 3.3. Recommended merging the definitions into the as-is subsection; the author approved.
- Applied:
  - 4.1 as a separate subsection was removed. Its two definition sentences now open the as-is subsection, followed by the Table 4.1 lead-in.
  - The integrity-level sentence moved to the risk-tier paragraph (now 4.2).
  - The Smith and Hayes (2024) argument (agile still needs IV&V; run it in phase with the cadence) moved to the explicit-policies paragraph (now 4.2). Its security point was dropped.
  - "This matters for Actual…" deleted (repeats 3.2/3.3; the advisories are still cited in 4.1).
  - Subsections renumbered 4.1–4.5. Cross-references updated: 3.5 now says the tiers are defined in Section 4.2, and the overall-quality paragraph now refers to Section 4.1. Table 4.2's "(Section 4.1)" still points to the definitions.
- No reference lost its last citation. Section 4 is now about 1,910 words (was about 1,960).

## 2026-10-27 — Independence definitions made visible in 4.1

- The author asked what Table 4.1's Technical, Managerial and Financial columns were for, then asked for the definitions not to be hidden in the first paragraph.
- Applied: the three NASA/IEEE independence parameters are now a three-item bulleted list, set apart from the V&V definitions. The Table 4.1 lead-in says the table tests each activity against them, one column each. The column headings now carry a short gloss: "Technical (not the developer)", "Managerial (separate organisation)" and "Financial (separate budget)". The wording still paraphrases S68, and the citation is unchanged.

## 2026-10-27 — Disclosure-route paragraph removed from 4.1

- The author asked whether the paragraph "The disclosure route itself is a strength…" was needed. Answer: no. Section 3.3 already says Actual offers private reporting and coordinated disclosure (same citation), and Table 4.1 shows the route. The 55% comparison was not built on anywhere.
- Removed at the author's request. Liu et al. (2025) had no other citation, so it was removed from References (S70 marked no longer cited in `sources.md`). Section 4 is about 45 words shorter.

## 2026-10-27 — 4.2 rewritten in concrete terms; Table 4.1 headings plain again

- The author said 4.2 read as abstract filler ("reading air"). Diagnosis given: abstract labels instead of actions, no link back to 4.1's finding, filler sentences restating each other, a vague audit, and a final paragraph that mostly repeated 2.5. A draft was shown; the author approved it.
- Applied: 4.2 now opens with 4.1's finding and makes three numbered changes ("First / Second / Third"):
  - an independent reviewer, with a bank-sync example of who is excluded;
  - outside checks, namely existing private reporting plus a third-party-funded audit scoped to the sync server, using OSTIF's 2025 figures including its 10 funding bodies [S72];
  - risk tiers, linked to Section 2's reviewer bottleneck.
- The IEEE integrity-level disclaimer is now stated once. A closing paragraph places the checks in exit policies, cites Smith and Hayes (2024), and states the WIP-limit rule. The Ahmad et al. (2018) citation was dropped from 4.2; it is still cited in 2.5 and 3.5. 4.2 is about 480 words (was about 405).
- At the author's request, the bracketed glosses were removed from Table 4.1's headings, which are back to Technical / Managerial / Financial. The bulleted definitions above the table stay.

## 2026-10-27 — 4.4 and 4.5 rewritten in concrete terms

- The author said 4.4 and 4.5 had the same problem as the old 4.2. Diagnosis: slogan topic sentences ("Cost is a binding constraint", "exit policies can become ritual", "gains an independent assessment"), no concrete scene, and 4.5 opening with a repeat of 4.2. Applied directly; the author's stated workflow is to review afterwards.
- 4.4:
  - A one-line intro names the three goals.
  - Early detection replays GHSA-m2cq through the board (Design, then Verify).
  - Requirements compliance names the trail the templates already record, the gap (nobody checks that it holds together) and the two added checks, with an untestable-criterion example. "Fixes #" was not quoted in the report.
  - Overall quality states the before/after concretely.
  - The bold goal labels were kept so the marker can find each goal.
- 4.5:
  - Each paragraph now opens with a concrete claim.
  - The independence limit is shown as release pressure on the same team.
  - Expertise, audit money, rubber stamps, then the ASVS blind spot (now its own paragraph).
  - No citation added or removed.
- Word count: 4.4 is about 350 (was about 225) and 4.5 about 340 (was about 265). Section 4 is now about 2,150 words.

## 2026-10-27 — 4.2 order: tiers first

- The author asked to swap the first and third changes in 4.2, and why the independent reviewer said "(defined below)". Answer: it pointed forward to the tiers, which came last. Putting the tiers first removes the need for it.
- Applied: the order is now (1) risk tiers, with the bullets and the IEEE disclaimer; (2) the independent reviewer for High-tier changes, with "(defined below)" removed; (3) outside checks. "the extra checks" became "extra checks", since nothing has been introduced yet. No wording changed otherwise.

## 2026-10-27 — 4.3 lead-in shortened

- The author found the 4.3 lead-in wordy. It went from about 95 words to about 50 and now:
  - maps the phases to the columns;
  - says Table 4.2 shows who independent performs or confirms Table 3.2's checks, and what evidence they leave;
  - defines the threat note.
- Removed:
  - the verify/validate sentence (the terms are defined in 4.1, and the table still marks activities);
  - the "ASVS requirement numbers" definition. The Verify exit policy now reads "Approval names the ASVS requirements and tests checked", which needs no definition and matches 4.5's wording.

## 2026-10-27 — 4.3 lead-in reduced to what the table shows

- The author asked why the lead-in focused on mapping phases and on not repeating Table 3.2. Answer: those sentences were defensive. They answered the earlier overlap finding for the writer's benefit, and the table's first column already shows the phase mapping. The reader only needs to know what the table shows.
- Applied: the lead-in now says "Table 4.2 shows, for each Kanban column, who checks the work independently and what evidence they leave", followed by the threat-note definition (about 30 words).

## 2026-10-27 — Section 4 rescanned for defensive and meta text

- The author asked for the whole of Section 4 to be rescanned for the same issue as the 4.3 lead-in: text that answers an objection the reader never raised, or describes the report instead of Actual.
- Removed or simplified:
  - 4.1: "one column each" (obvious from the table).
  - 4.1: the sentence saying reporter credits do not show organisational or funding arrangements. The table's "Not established" and its definition already say this.
  - 4.1: "The three advisories checked for this report" became "The critical and two high-severity advisories cited in Section 3.2".
  - 4.2: the two-sentence IEEE disclaimer became one: "The tiers are this report's own, borrowing only the idea in IEEE 1012-2024 that…". The agreed honesty about not using IEEE's scheme is kept.
  - 4.2: "and is not full IV&V in the IEEE sense" was cut. "Technical independence only" and 4.5 already make the point.
  - Table 4.2, Build/PR role: "None: automated checks configured by the team (partial, Table 4.1)" became "None (automated)".
  - 4.3: the smoke-test placement sentence (a leftover of the earlier disclaimer). Table 4.1 already notes that smoke tests run after publication, and the release row says "before approval and tagging".
  - 4.4: the intro sentence restating the heading.
- Kept on purpose:
  - the 4.2 opening recap of 4.1 (it links the model to the problem);
  - the Smith and Hayes support;
  - the preview-build reason for the separate test server.
- Flagged, not changed: 4.5's "its cost is estimated in Assignment 2" (agreed 2026-10-21, but similar to the 3.5 Assignment 2 mention the author removed).
- Section 4 is about 1,980 words (was about 2,150).

## 2026-10-27 — 4.3 merged into 4.2

- The author asked what 4.3 was for, given 4.2. Answer: 4.3 held Table 4.2, the column-by-column version of the model in Lecture 6's per-phase format. The table is needed (it covers the brief's "implement", and the next subsection relies on it), but after the cuts its own text was four sentences, and 4.2 already pointed to it. Recommended merging; the author approved.
- Applied:
  - the 4.3 heading was removed;
  - Table 4.2 and its notes now close 4.2;
  - the table introduction and the threat-note definition were moved to the end of 4.2's exit-policy paragraph, after the WIP-limit sentence, so that "This follows Smith and Hayes" still refers to the exit policies.
- 4.4 and 4.5 were renumbered 4.3 and 4.4. No cross-reference pointed to them; 3.5's "defined in Section 4.2" is still correct.

## 2026-10-27 — Table 4.2 headings renamed

- The author found Table 4.2's headings badly named. They now use plain words for Lecture 6's activities / tools / roles / outcome: "Board column | What is checked | Tools | Who checks | Card moves on when" (was "Column (lifecycle phase) | IV&V activities | Tools | Independent role | Exit policy added").
- The redundant phase labels "(requirements)" and "(design)" were dropped from the first column. The others stay, because they name a different phase: Build/PR (implementation), Verify (testing), Release train (deployment) and Operate/maintain (maintenance).
- Caption: "Independent checks at each board column (High-tier cards unless stated)."

## 2026-10-27 — Phase labels removed from Table 4.2

- The author asked why the first column named each stage twice (the column name plus a bracketed lifecycle phase). Answer: the brackets mapped the columns to Lecture 6's six phases, but each column name already says the same thing. The author's screenshot predated the previous push, which had already removed "(requirements)" and "(design)".
- Applied: the remaining four labels were removed, so the column holds plain board-column names only.

## 2026-10-27 — Table 4.2 Verify tools trimmed

- At the author's request, "with synthetic budgets" was removed from the Verify row's Tools cell, which now reads "separate test server". The synthetic budget is already named in the same row's "What is checked" cell.

## 2026-10-27 — 4.3 rewritten to guide the reader

- The author said 4.3 read like notes rather than guiding the reader. Diagnosis: no intro saying how the goals would be judged; paragraphs opened with evidence rather than the claim; facts were stacked without connectives.
- Applied:
  - A short intro names the three goals and the evidence used for each (the critical advisory, the templates, the escaped flaws from 4.1).
  - Each goal paragraph now opens with its claim ("two chances to be caught before release"; "checks that what users asked for is what was built and tested"; "moves independent checking … to before release"), walks through the steps with signposts ("The first time… The second…"; "at both ends of the board"), and closes by tying back to the goal.
  - No facts or citations changed.
- 4.3 is about 490 words (was about 330). Section 4 is about 2,110 words.

## 2026-10-27 — Table 4.2 caption shortened

- At the author's request, "(High-tier cards unless stated)" was removed from the Table 4.2 caption. To keep the meaning, the lead-in sentence now says the table shows "who checks a High-tier card independently". Rows that apply more widely are still marked "(all cards)" or "(Standard and High)", and the note after the table covers Standard and Low tiers.

## 2026-10-27 — 4.4 rewritten to guide the reader

- The author said 4.4 had the same note-taking problem as 4.3. Applied the same treatment:
  - An intro names the five weaknesses, grouped by cause (team, budget, the checks themselves), and says each will be given as what goes wrong, how far the model limits it, and what is left.
  - Each paragraph has a bold claim label, explains the mechanism (e.g. release pressure on the same team; CODEOWNERS areas being High-tier), states the mitigation and the residue.
  - A closing sentence ties the limits together.
- No facts or citations changed; "its cost is estimated in Assignment 2" is kept.
- 4.4 is about 570 words (was about 340). Section 4 is about 2,340 words.

## 2026-10-27 — 4.4 rewritten again: no bold labels, shorter

- The author rejected the previous 4.4: bold claim labels made it worse, and it had become far too long.
- Applied: plain paragraphs, each opening with its point as a normal sentence, and linked by transitions ("also", "Money limits…", "The checks themselves have two weaknesses. First… Second…").
  - The intro and closing summary were removed.
  - The rubber-stamp and ASVS blind-spot points were merged into one paragraph.
  - No facts or citations changed.
- 4.4 is about 300 words (was about 570 in the rejected version, and about 340 before that). Section 4 is about 2,070 words.
- Lesson for later sections: guide the reader with topic sentences and transitions, not bold run-in labels, and don't let guidance add length.

## 2026-10-27 — 4.4 Critical evaluation deleted

- The author asked whether 4.4 had any point. Answer: the brief's IV&V task is "analyse and implement the integration … to facilitate early defect detection, ensure requirements compliance, and improve overall software quality". Unlike the methodology and QA tasks, it does not say "critically evaluate". 4.4 came from a planning assumption, not the brief. Its points repeated 4.2 and 3.6, or are risks that belong to Assignment 2.
- Deleted at the author's request, including its "cost is estimated in Assignment 2" pointer. No reference lost its last citation (Aboltins, 2025, OWASP Foundation, 2025 and Actual Budget, n.d.-f are all still cited elsewhere).
- Its points were saved in `04-ivv.md` under "Carried forward to Assignment 2", as candidate risks for the Risk Management Plan and the audit cost for Estimation.
- Section 4 now has three subsections and is about 1,790 words (was about 2,080).
- Not changed: the executive summary's IV&V sentence ("Internal review gives technical independence only, and volunteer time and donation funding remain the main limits"). 4.2 still supports it, but the author may want to recheck it now that there is no evaluation subsection.

## 2026-10-27 — Bold labels removed from 4.3

- At the author's request, the bold run-in labels in 4.3 were removed. The goals are now named in each paragraph's opening sentence ("For early defect detection, …"; "For requirements compliance, …"; "The model improves overall quality …"), in the same order as the intro lists them. No other wording changed.

## 2026-10-27 — Table 4.2 last heading made a noun

- At the author's request, Table 4.2's last heading changed from "Card moves on when" to "Exit policy". This is the term Section 2.5 defines and Sections 3 and 4 use throughout.

## 2026-10-27 — Table 4.2 headings all nouns

- At the author's request, "What is checked" became "Checks" and "Who checks" became "Checker". Table 4.2's headings are now: Board column | Checks | Tools | Checker | Exit policy.

## 2026-10-27 — Whole-report trim review (word count)

- The author has finished the clarity reviews of Sections 1–4, written without a word limit, and asked for a critical read of the whole report to find what can be cut to meet the word limit. The cuts must be honest: remove what the reader doesn't need, and never compress sentences into shorthand.
- Measured: about 7,270 words (headings, captions, tables and citations counted; References, source comments and the three ASCII figures excluded). Target is about 5,000. Section 2 is 2,759 words, 38% of the total, for the same 10 marks as Sections 3 and 4.
- Main finding: most of the excess is the same content told in several places. Examples: the CI checks list (4 places), the release-train detail (6), the GHSA-m2cq story (6), the board column by column (4), and the volunteer-capacity evidence (10).
- Proposed in `planning/06-trim-plan.md`: about 45 itemised cuts, marked A (safe: repetition, recaps, roadmaps, generic background) or B (judgement: removes some content, e.g. the bazaar baseline label with Raymond and Mockus, merging Tables 2.3 and 2.4, and the threat note). Estimate: A items reach about 5,450 words; adding the B items reaches about 4,950–5,050.
- Also flagged: "High-tier" is used in 3.4 and 3.5 but defined only in 4.2; 3.2's Reliability bullet has a non sequitur; 1.1 has a dangling modifier; "Pluggy AI" and "Pluggy.ai" are spelled differently; Section 4 has no introduction.
- Nothing applied yet; awaiting the author's decisions.

## 2026-10-27 — Trim plan: first decisions

- 3-7 decided: keep Table 3.1 and drop the bullets after it. The bullets' two reasons (ASVS chapters match the 2026 flaws; W3C does not deprecate WCAG 2.1) move into the table in short form.
- The author asked whether the non-word-count problems should wait until after trimming. Answer: most are fixed by trim items or depend on the final count. The one to settle first is where the risk tiers are defined, because the 3.5 and 4.2 trims rewrite that text.

## 2026-10-27 — Trim applied: Section 2

- The author approved all A and B items and asked for the risk-tier definition to move to 3.5.
- Applied in Section 2: 2-1 to 2-17. The roadmap was cut. In 2.1, the PR definition, the feature-flags sentence, the CI test list and the release detail were removed (Figure 2 keeps the steps). 2.2's lead-in and table cells were tightened. The two-exceptions and "combine" paragraphs were shortened. Table 2.3 (candidates) and Table 2.4 (clashes and gaps) were merged into one Table 2.3, and the "suited to" and "drawback" columns were dropped. The bazaar paragraph became one sentence. The 2.5 column bullets and the "Compared with today" paragraph were removed, along with the lead/cycle-time definitions.
- References: Feature flags (n.d.-b), Raymond (2000) and Mockus et al. (2002) were removed. The remaining n.d. letters were shifted down by one. `sources.md` was updated.
- 2-18 (folding Table 2.2 into Table 2.1) is held until Sections 3 and 4 are trimmed and the total is measured.
- Section 2 went from 2,621 to 2,084 words (a consistent count: headings, captions, tables and citations; no figures or References). This is a smaller cut than the plan estimated.

## 2026-10-27 — Trim applied: Sections 3, 4 and 1.1

- Section 3: 3-1 to 3-12 applied.
  - The roadmap was cut.
  - 3.1's stakeholder paragraph was reduced to its conclusion.
  - The "yet…" endings were removed from 3.2, which also fixes the Reliability non-sequitur.
  - The release sentence and the performance sentence were removed from 3.3. The GHSA-m2cq account is now the single full one, including "six endpoints".
  - In 3.4, Table 3.1 is kept, the bullets are folded into it, and "High-tier work" became "high-risk sync-server work".
  - The board recap was removed from 3.5.
  - 3.6 now points back to 2.1, and its "public evidence" duplicate was removed.
- **The risk-tier definition (High/Standard/Low, with the IEEE 1012 integrity-level note) moved from 4.2 to 3.5**, where Table 3.2 first relies on it. 4.2 now refers back to it. To be checked by the author.
- Section 4: 4-1 to 4-9 applied.
  - Table 4.1 cells were shortened, and the 4.1 conclusion no longer restates the table or names the reporters.
  - The 4.2 lead-in was cut, and the OSTIF figures were reduced to the 98% fixed rate.
  - The threat note was removed, and the Design row now verifies the Table 3.2 design list against ASVS.
  - In 4.3, the lead-in is one sentence, the flaw is no longer retold (3.3 has it, which also resolves the Pluggy spelling), and the overall-quality paragraph points back to 4.1.
- 1-1 applied (the dangling modifier in 1.1 is fixed).
- Measured total: 5,990 words, from 7,037 on the same count. The plan's estimate of about 5,000 was too optimistic by about 1,000 words, because most of the safe cuts saved less than estimated. A second round needs content decisions from the author. See the round-2 list in `06-trim-plan.md`.

## 2026-10-27 — Round 2: C1, C4, C5 applied; selection-to-appendix declined

- C1: the methodology and QA definitions that opened Sections 2 and 3 were removed. QA is still defined as an abbreviation in 1.1.
- C4: the 3.5 worked example moved to a new **Appendix A** (FYI only). 3.5 points to it in one sentence. 4.3 still walks through the same bank-sync case in the body.
- C5: the executive summary was shortened (186 to 171).
- The author asked to move the Kanban selection process to an appendix and go straight to Kanban. **Not applied.** The brief marks "select, justify, and critically evaluate… based on goals, constraints, risks, and stakeholder expectations", so the selection is the justification. Appendices are not marked. AGENTS.md forbids moving content the argument depends on into an appendix to save words.
- The author asked whether 2.6 and 3.6 are needed. Answer: yes. The brief asks for critical evaluation in both the methodology and QA tasks, unlike the IV&V task (which is why 4.4 was deleted).
- Total now 5,799. R1–R8 re-evaluated with context for the author; not yet applied.

## 2026-10-27 — 2.6 and 3.6 each made one paragraph; citation check

- At the author's request, 2.6 and 3.6 are each one paragraph.
  - **2.6 keeps:** Kanban needs added practices (Ahmad et al., 2018, p. 110); the WIP limit as a signal (Salkever, 2023); the evidence limits (GeeksforGeeks, qualitative judgement, no Kanban study); tailoring (Kuhrmann et al., 2022); the revisit triggers. **Dropped:** the set-up and culture difficulty (Ahmad p. 106) and the line about directing the paid review pool.
  - **3.6 keeps:** the volunteer-time cost and the tier misjudgement risk; automation effects (both Wessel studies), with the monitor-and-remove rule; the accessibility-checks limit. **Dropped:** the burnout citation (Salkever is still cited in 2.2 and 2.6) and the "less discussion" detail.
  - No reference lost its last citation.
- APA fix: the first IEEE citation (3.4) now reads "(Institute of Electrical and Electronics Engineers [IEEE], 2026)".
- Citation check: about 85 parenthetical citations, about 290 words (about 5% of the body). Each one backs a stated fact. Repeated citations (e.g. Aboltins, 2025 six times) come from repeated facts, not over-citing.
- R7 explained to the author: it is the last paragraph of 3.4, which names the standards that fail the cost test.
- Total now 5,712.
