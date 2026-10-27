# Section 3 — Quality Assurance Process (10 marks)

Writing status, 22 October 2026: all three report versions are complete. The approved Kanban flow and mandatory QA requirements are integrated. Source checks corrected IEEE 730 to the published 2026 edition, verified all nine characteristic names and retained public-evidence limitations. See `research/qa-writing-evidence.md` and `../report/assignment-1/README.md`. The report remains a draft for author review.

Status: **Agreed** (re-agreed 2026-10-21 after the lecturer's 3-attribute feedback). The flow may still be adjusted during writing.

## What the brief asks

> "Critically select, evaluate, and apply quality assurance practices that address key software quality attributes, ensuring that the software product aligns with stakeholder requirements and industry standards."

Five things must be visible to the marker:
1. **Key quality attributes** (which ones, and why).
2. QA practices that are **selected**, **evaluated** and **applied** (not just listed).
3. Alignment with **stakeholder requirements**.
4. Alignment with **industry standards**.
5. **Critical** thinking throughout.

## Agreed

- **Flow 3.1–3.6** as below (as-is → gaps → to-be, mirroring Section 2). Provisional, like Section 2.
- **Quality model: ISO/IEC 25010:2023** (published 15 Nov 2023; replaces the 2011 edition taught in the lecture) [S53].
  - Correction to an assumption: 25010:2023 does **not** cover AI. AI system quality is a separate standard, **ISO/IEC 25059:2023** [S64].
  - Actual's *product* has no AI features (to confirm). AI shows up in Actual's *development process* (AI usage policy [S50], "AI slop" policy [S12]). That is a **process-quality** topic, which could be a nice point in 3.3 or 3.6, but it is not a 25010 attribute.
- ~~**Attributes:** rate all nine 25010:2023 characteristics briefly in one table, then go deep on the top 4–5.~~ **Superseded 2026-10-21:** the lecturer confirmed that **only 3 quality attributes** are needed. 
- **The 3 attributes (author's choice, 2026-10-21): Security, Reliability, Interaction capability** (ISO/IEC 25010:2023 names).
  - **Security:** advisories [S63], security policy [S62], CodeQL, E2EE [S51]. Standards: **OWASP ASVS** [S58], **OpenSSF** [S60].
  - **Reliability:** data integrity, sync, recovery. Evidence: migration and CRDT checks in CI [S01], backups, E2EE password-loss warning [S51]; **test coverage not measured** (coverage gap). 25010:2023 renamed the reliability subcharacteristic "maturity" to "faultlessness" (per S65, to verify).
  - **Interaction capability** (incl. accessibility/inclusivity): WCAG 2.1 AA target [S01] vs current **WCAG 2.2** [S59]; **no automated accessibility testing**. Standard: **WCAG 2.2**.
- ~~**Keep the short 9-row rating table** in 3.2~~ **Superseded 2026-10-27 (author):** 3.2 goes straight to the three attributes; no rating table. The other characteristics get no discussion, except one sentence on why functional suitability is left out.
- (Original note:) **Keep the short 9-row rating table** in 3.2 (~120 words: characteristic, one-line reason, High/Medium/Low) to show the 3 were chosen deliberately.
- **Knock-on effects (agreed):**
  - 3.3–3.5 focus only on the 3 chosen attributes;
  - **functional suitability** (calculation correctness) and **performance** (performance testing) drop to a brief mention: one row each in the rating table, plus at most a sentence;
  - the words saved go to critical evaluation (3.6).
- **Writing-thread caution:** "users trusting the numbers" [S01] makes functional suitability look important, so the rating table must give a **reasoned, evidence-based** line for why it isn't in the top 3. Possible reasoning (to verify before writing): existing unit and E2E tests already target calculations, and the published advisories concern security, not calculation errors. Don't claim "no calculation defects" without checking.
- **Boundaries:**
  - Section 3 = the QA *process* (attributes, practices, standards, quality gates, plan).
  - Section 4 = IV&V and detailed testing.
  - Assignment 2 = metric details. Section 3 names **at most one measure per attribute**.
- **No figures** for Section 3 for now. The author may reconsider later.
- **Appendix rule** (see `AGENTS.md`):
  - The appendix is only for supplementary "FYI" material. It is **not marked** and must not be used to dodge the word count.
  - Anything the argument depends on goes in the **body**.
  - So there is **no "full SQAP in the appendix"**. 3.5 carries the QA plan itself as a compact table in the body.
- **Words in tables count** towards the word limit (the author confirmed this), so tables must stay compact.
- **Standards scope: option B.** Evaluate the lecture standards (ISO/IEC 25010, IEEE 730, ISO 9001, ISO/IEC 27001, CMMI) **and** OSS-specific frameworks (OpenSSF Best Practices Badge and Scorecard, OWASP ASVS, WCAG). Adopt what fits; reject heavy certification standards or borrow their principles only, with reasons.
- **Security is a top-priority attribute.** Actual is a financial system holding sensitive data. The main gap is **proactive security verification before release**, not a missing policy.
- **Specific advisories may be cited** as evidence (e.g. GHSA-m2cq-xjgm-f668, critical, missing authentication on bank-sync endpoints).
- **Severity:** use the **maintainers' published rating** (and GitHub publish dates).
- **AI:** ISO/IEC 25059 (AI quality) is **out of scope**. AI only appears as a development-process topic.
- The advisory **reporters are outside the core team** (iamsilk, Rex50527, pyuysig; fixed by MatissJanis). **Carry this into Section 4** as evidence of independent verification.

## Agreed at review (27 October 2026)

The author asked for all ten Section 3 review findings to be applied (see `discussion-log.md`, 27 October 2026). Decisions that change the plan above:

- **QA defined** in a new Section 3 opening paragraph that also signposts 3.1–3.6 (mirrors Section 2's opening).
- **3.1 uses Garvin's (1984) five approaches** [S129] (Lecture 1's viewpoints). Transcendent is set aside; user, product, manufacturing (process) and value-based views are applied to Actual.
- **3.2 (superseded the same day; see the rating-table bullet above):** rating rule made explicit: two checkable questions, *harm* and *current checks*. Limited harm = Low; serious harm and already covered = Medium; serious harm with a gap = High. Ratings unchanged. "Release baseline" wording removed.
- **3.3:** the authorisation test matrix is defined and marked as this report's proposal ("could have caught"). The security policy's broken (404) link is **dropped** as low-value; the missing response time stays. Performance-testing sentence moved out of the QA-plan bullet.
- **3.4:** two selection tests (fit, cost) and the decision labels are defined before Table 3.2; text after the table no longer repeats it; edition trivia removed.
- **3.5:** "exit policy" used throughout (no "Definition of Done"; also in the executive summary). Risk tiers (Section 4.3) now decide which criteria apply. OpenSSF Scorecard placed in the Release train exit policy. Owners stated as existing roles. The "separate server with synthetic data" criterion left to Section 4, which gives its reason. New **Table 3.4** maps Lecture 3's SQAP sections to where the plan covers them; IEEE 730-2026 is cited only for its scope.
- **3.6:** automation paragraph names the checks it applies to; limits paragraph rewritten as three numbered limits; the "standards read only at scope level" sentence narrowed to IEEE 730-2026.

## Open questions (from the review, 27 October 2026)

- ~~The SQAP section list (Table 3.4)…~~ Resolved 27 October 2026: option 1 (the plan areas are the report's own design). Still open: the QA definition in the Section 3 opening is lecture content without a citation (S132).
- Section 3 grew from about 1,550 to about 2,570 words (tables included) because clarity came first. Trimming is for the author's word-count pass.

## Agreed: standards trimmed and plan areas reframed (27 October 2026)

- **Adopt four standards, one job each:** ISO/IEC 25010:2023 (frames the section), OWASP ASVS 5.0.0 (security gap), WCAG 2.2 AA (interaction-capability gap), IEEE 730-2026 (missing QA plan; applied in intent only, catalogue entry read). Table 3.1 now has the columns *Gap it closes* and *How it is used*.
- **Dropped:** the OpenSSF Badge and Scorecard (they overlap ASVS) and ISO/IEC/IEEE 29119-1 (Section 4 never used it). Their references were removed from the report. The 6-label decision vocabulary is gone.
- **ISO 9001, ISO/IEC 27001 and CMMI:** one paragraph, "considered and rejected on cost". Their ideas are tied to the user-based view (3.1) and the risk tiers (3.5).
- **Reliability:** one line saying no standard is needed, because its gap is a missing measure (the coverage report).
- **Option 1 for Table 3.3:** the plan's seven areas are presented as the report's own design ("Areas of Actual's QA plan"). The claim that an SQAP "is usually organised into standard sections" was removed, so no citation is needed. Background: Lecture 3's list is the IEEE 730-2002 outline, and no current readable source was found (S131, S133).
- This supersedes the earlier "Standards scope: option B" adopt/borrow/reject table and the "OpenSSF: Adopt" row above.

## Agreed: IEEE 730 rejected (27 October 2026)

- The author pointed out that IEEE 730 is behind a paywall. The cost test now adds: if contributors must follow a standard's requirements, its text must be free to read.
- **IEEE 730-2026 moved to the rejected paragraph.** It fits the missing-QA-plan gap, but it is available only by purchase or subscription (official catalogue rechecked 27 October 2026 [S82]). The plan in 3.5 is now stated as the report's own lightweight design. The "intent only" wording was removed from 3.4 and 3.6.
- Table 3.1 now has **three** adopted standards: ISO/IEC 25010:2023, OWASP ASVS 5.0.0 and WCAG 2.2. ISO/IEC 25010 is also sold; one sentence explains that it is used only to name the attributes, so contributors never need its text.
- The missing QA plan is closed by the plan itself; reliability is closed by the coverage measure.
- This supersedes "IEEE 730-2026 | Adapt" above.

## Relevant lecture guidance (not cited)

- L1: views of quality; functional, structural and process quality.
- L3: SQAP definition, 10 steps, SQAP sections.
- L4: ISO 9001, ISO/IEC 25010, 27001, 25022, CMMI, IEEE 1012/1059.
- L5: QA vs quality planning vs QC; process vs product quality.
- L6: configuration management; V&V.

## Evidence (verified; see `research/actual-development-process.md`)

**Actual already has strong automated QA:**
- typecheck, lint and format;
- Vitest unit tests, Playwright E2E and visual regression;
- CodeQL and dependency review;
- migration and CRDT checks;
- pre-commit hooks;
- review guidelines and an AI usage policy;
- 2-maintainer release approval plus a manual smoke test;
- optional E2E encryption.

**Security process (corrected 2026-10-20):**
- A **security policy exists** (org-level `SECURITY.md`, private vulnerability reporting, coordinated disclosure) [S62].
- **At least 10–14 published advisories** in the last year [S63]. The npm packages alone have 1 critical, 3 high and 6 moderate. **Mostly access-control flaws in the sync server**, many linked to the multi-user/OpenID feature added in 2025.
- Policy weaknesses: no response-time commitment, and a broken link (404).

**Apparent gaps (no evidence found in the repository, October 2026):**
- test coverage measurement (explicitly disabled in sync-server);
- automated accessibility testing (despite the WCAG 2.1 AA target);
- performance testing in CI;
- a written QA plan;
- **proactive** security verification (security is mostly handled reactively, after reports).

## Flow

| # | Subsection | Purpose | Main content | ~Words |
|---|---|---|---|---|
| 3.1 | What "quality" means for Actual | Define quality in context | Quality views (L1) applied to Actual; "users trusting the numbers" [S01 `PRODUCT.md`]; which stakeholder cares about which view. | 170 |
| 3.2 | Key quality attributes | Pick and prioritise | One table rating all **9** ISO/IEC 25010:2023 characteristics for Actual (why it matters, stakeholder, priority). Deep-dive the top 4–5, likely **functional suitability (calculation correctness)**, **reliability (data integrity, sync)**, **security** (now strongly evidenced by the advisories), **maintainability** (volunteer contributors), and **interaction capability** (incl. inclusivity, i.e. accessibility). | 270 |
| 3.3 | Current QA practices (as-is) and gaps | Evidence-based assessment | Coverage table: practice → attributes it protects. Gaps: coverage, accessibility automation, performance, no QA plan, reactive-only security. | 270 |
| 3.4 | Selecting QA practices and standards | The "critically select" part | For each gap or attribute: candidate practices and standards → adopt / adapt / reject, with reasons. (Scope of standards: pending, question 1.) | 270 |
| 3.5 | Applying the QA process within Kanban (to-be) | The "apply" part | A **compact QA plan in the body** (table), structured by L3's SQAP sections and built into the Kanban workflow from Section 2: explicit policies and a **Definition of Done** per board column, quality gates, roles, defect and vulnerability handling. | 250 |
| 3.6 | Critical evaluation | Where most marks come from | Strengths, cost and limits for volunteers; risks (automation overhead, e.g. bots and CI slowing PRs [S43]); what still isn't covered. | 170 |

Total about **1,400 words**, all in the body (rebalanced 2026-10-21 after the executive summary was confirmed to count). The 3.5 table counts towards this.

## Standards and frameworks: verified facts for 3.4 (see `sources.md` → D2)

| Standard / framework | Current edition (verified) | Planned judgement |
|---|---|---|
| ISO/IEC 25010 | **2023** (replaces 2011) [S53] | **Adopt** as the quality model |
| IEEE 730 | **2014** (active; a 2026 revision is in development) [S54] | **Adapt**: lightweight SQAP structure for 3.5 |
| ISO 9001 | **2026** (published 16 Sep 2026; the lecture's 2015 edition is superseded) [S55] | **Reject certification**; borrow principles |
| ISO/IEC 27001 | **2022** (+ Amd 1:2024) [S57] | **Reject certification**; borrow risk-based thinking |
| CMMI | **V3.0** (2023) [S56] | **Reject appraisal**; maybe describe maturity informally |
| OWASP ASVS | **5.0.0** [S58] | **Adopt** for sync-server access control, authentication and sessions (directly matches the advisories) |
| WCAG | **2.2** (W3C Rec, 12 Dec 2024 version) [S59]; Actual targets 2.1 AA | **Adopt** 2.2 AA plus automated checks |
| OpenSSF Best Practices Badge / Scorecard | Live programmes [S60]; **Actual has neither** (checked) | **Adopt**: free, OSS-specific, mostly automated |
| ISO/IEC/IEEE 29119 | **29119-1:2022** [S61] | Mostly Section 4; at most a mention here |

## Open questions

None for planning.
