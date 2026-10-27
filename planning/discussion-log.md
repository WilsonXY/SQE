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
