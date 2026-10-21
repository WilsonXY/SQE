# Section 3 — Quality Assurance Process (10 marks)

Status: **Re-opened** (2026-10-21): the lecturer confirmed only **3 quality attributes** are needed. Which 3 is pending; the rest of the plan stands.

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
- ~~**Attributes:** rate all nine 25010:2023 characteristics briefly in one table, then go deep on the top 4–5.~~ **Superseded 2026-10-21:** the lecturer confirmed that **only 3 quality attributes** are needed. See *Open questions* for which 3, and whether to keep a short selection table.
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

1. **Which 3 attributes?** (Lecturer: "only needs 3", e.g. security, performance.)
   - **Recommended: Security, Reliability (data integrity, sync, recovery), Functional suitability (calculation correctness).** These have the strongest evidence and are what users care about most ("users trusting the numbers").
   - **Performance efficiency is not recommended:** low risk (small personal datasets, runs locally) and almost no evidence.
   - Alternatives: **Interaction capability** (accessibility: WCAG 2.1 target vs current 2.2; no automated accessibility tests) or **Maintainability** (volunteer contributors).
2. **Keep the short 9-row "rating" table** (one line and High/Medium/Low per characteristic, about 120 words) to show the 3 were selected deliberately from ISO/IEC 25010:2023? Or drop it and justify the choice in two or three sentences?
3. **Knock-on effects (to confirm):**
   - 3.3–3.5 focus on the chosen 3 (e.g. Security → OWASP ASVS, OpenSSF; Reliability → recovery and migration checks; Functional suitability → test coverage);
   - WCAG/accessibility and performance testing shrink to a brief mention (or drop) unless their attribute is chosen;
   - the freed words (~100–150) go to critical evaluation.
