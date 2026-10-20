# Section 3 — Quality Assurance Process (10 marks)

Status: **In discussion.** First proposal, 2026-10-20.

## What the brief asks

> "Critically select, evaluate, and apply quality assurance practices that address key software quality attributes, ensuring that the software product aligns with stakeholder requirements and industry standards."

Five things must be visible to the marker:
1. **Key quality attributes** (which ones, and why).
2. QA practices that are **selected**, **evaluated** and **applied** (not just listed).
3. Alignment with **stakeholder requirements**.
4. Alignment with **industry standards**.
5. **Critical** thinking throughout.

## Relevant lecture guidance (not cited; see the AGENTS.md rule)

- L1: views of quality (transcendent, product, user, process, value); functional, structural and process quality.
- L3: SQAP definition, 10 preparation steps, SQAP sections (management, documentation, standards and conventions, reviews and audits, testing, problem reporting and corrective action, other: tools, CM, training, risk).
- L4: ISO 9001, ISO/IEC 25010, 27001, 25022, CMMI, IEEE 1012/1059.
- L5: QA vs quality planning vs quality control; process vs product quality.
- L6: configuration management; V&V.

## Evidence already gathered (verified, see `research/actual-development-process.md` → *QA practices as-is*)

**Actual already has a lot of automated QA:**
- type checking, lint and format;
- unit tests, E2E tests and visual regression;
- CodeQL security scanning and dependency review;
- migration and CRDT checks;
- pre-commit hooks;
- review guidelines;
- 2-maintainer release approval plus a manual smoke test;
- optional end-to-end encryption.

**Apparent gaps (no evidence found):**
- no test coverage measurement (coverage is explicitly disabled in sync-server);
- no automated accessibility testing despite the WCAG 2.1 AA target;
- no `SECURITY.md`;
- no performance testing in CI;
- no written QA plan.

## Proposed flow (pending approval)

Same pattern as Section 2: **as-is → gaps → to-be**, so the two sections read as one argument.

| # | Subsection | Purpose | Main content | ~Words |
|---|---|---|---|---|
| 3.1 | What "quality" means for Actual | Define quality in context | The quality views (L1) applied to Actual. Its own definition of success: "users trusting the numbers" (`PRODUCT.md`). Which stakeholder cares about which view. | 200 |
| 3.2 | Key quality attributes | Pick and prioritise attributes | ISO/IEC 25010 quality model. Rate every characteristic for Actual; deep-dive the top 4–5 (likely **functional suitability/correctness**, **reliability/data integrity**, **security/privacy**, **maintainability**, **interaction capability/usability and accessibility**). Table: attribute → why it matters for Actual → stakeholder → priority. | 300 |
| 3.3 | Current QA practices (as-is) and gaps | Evidence-based assessment | Map Actual's existing practices to each key attribute in a coverage table, so the gaps show up (coverage, accessibility, security policy, performance, no QA plan). | 300 |
| 3.4 | Selecting QA practices and standards | The "critically select" part | For each gap or attribute: candidate practices and standards, with keep, adopt or reject plus a reason. Includes judging which industry standards actually fit a volunteer OSS project (e.g. heavy certification standards vs lightweight OSS-specific frameworks). | 300 |
| 3.5 | Applying the QA process within Kanban (to-be) | The "apply" part | A lightweight SQAP for Actual following L3's SQAP sections, built into the Kanban workflow from Section 2: explicit policies and a **Definition of Done** per board column, quality gates, roles, defect handling. One table in the body, the full SQAP in an appendix. | 250 |
| 3.6 | Critical evaluation | Where most marks come from | Strengths, costs and limits for a volunteer team; risks (e.g. automation fatigue, bots slowing PRs [S43]); what still isn't covered. | 200 |

Total about **1,550 words**, plus an appendix (full SQAP table, full attribute rating).

## Proposed boundaries with other sections

- **Section 3 (QA)** = the overall quality *process*: attributes, practices, standards, quality gates, the plan. Testing appears as a QA/QC practice at a summary level.
- **Section 4 (IV&V)** = *independent* verification and validation activities per lifecycle phase (requirements, design, code, test, release, maintenance), with roles and independence. **Detailed testing activities go here, not in Section 3.**
- **Assignment 2 (Software Metrics)** = detailed metric definitions and calculations. **Section 3 names one measure per attribute at most** and leaves the details to Assignment 2.

## Candidate standards and frameworks to evaluate in 3.4

All from AI memory, **unverified**. To be checked and logged in `sources.md` before writing.

| Standard / framework | Likely judgement for Actual (to test) |
|---|---|
| ISO/IEC 25010 (quality model; the lecture cites the 2011 version, a **2023 revision** is believed to exist) | **Adopt** as the attribute model |
| IEEE 730 (SQA processes; the SQAP structure in L3 follows it) | **Adopt (lightweight)** as the plan structure |
| ISO 9001 (QMS certification) | Probably **reject**: a certification-oriented organisational QMS with no fit for a volunteer OSS project. Borrow its principles only. |
| CMMI (maturity appraisal) | Probably **reject** an appraisal; maybe use the maturity levels to describe where Actual sits |
| ISO/IEC 27001 (ISMS) | Probably **reject** certification; borrow risk-based security thinking |
| OWASP ASVS / OWASP Top 10 | Possibly **adopt** for the security requirements of the sync server |
| WCAG 2.1/2.2 | **Adopt**. Actual already targets 2.1 AA; the gap is automated checking |
| OpenSSF Best Practices Badge / OpenSSF Scorecard | Possibly **adopt**: OSS-specific, lightweight, industry-backed |
| ISO/IEC/IEEE 29119 (software testing) | Maybe reference for test documentation. Possibly too heavy. |

## Open questions

1. **Flow and framing:** OK with as-is → gaps → to-be (3.1–3.6), mirroring Section 2?
2. **Quality model:** use the **latest ISO/IEC 25010 (2023)**, mentioning that it updated the 2011 version taught in the lecture, or stick to 2011 to match the lecture? I'd recommend 2023 because of your recency rule, once verified.
3. **Attribute depth:** rate all characteristics briefly (table) and deep-dive the **top 4–5**? Or only discuss the top ones?
4. **Section 3 / 4 / Assignment 2 boundaries** (above): agree?
5. **Standards scope:** include OSS-specific industry frameworks (OpenSSF, OWASP, WCAG) alongside the lecture's ISO/CMMI standards, and openly **reject** heavy certification standards for a volunteer project, with reasons?
6. **SQAP in the appendix:** put the full lightweight SQAP table in an appendix, with a summary table in 3.5?
7. **Figures:** Sections 1–2 already have 3 figures. For Section 3, I suggest **no new figure**, only tables. Or one figure showing quality gates on the Kanban board? This could be merged with Figure 3 (2.5) so one picture serves both sections.
8. **Gap claims:** the gaps come from a file search of the repo. Are you comfortable stating them as "no evidence found in the repository (as of October 2026)"? Can you check one thing in a browser: does https://github.com/actualbudget/actual/security show a security policy?
