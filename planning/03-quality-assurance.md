# Section 3 — Quality Assurance Process (10 marks)

Status: **In discussion.** Flow and most decisions agreed (2026-10-20). Standards scope and security framing are pending.

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
- **Attributes:** rate **all nine** 25010:2023 characteristics briefly in one table, then go deep on the **top 4–5**.
- **Boundaries:**
  - Section 3 = the QA *process* (attributes, practices, standards, quality gates, plan).
  - Section 4 = IV&V and detailed testing.
  - Assignment 2 = metric details. Section 3 names **at most one measure per attribute**.
- **No figures** for Section 3 for now. The author may reconsider later.
- **Appendix rule** (see `AGENTS.md`):
  - The appendix is only for supplementary "FYI" material. It is **not marked** and must not be used to dodge the word count.
  - Anything the argument depends on goes in the **body**.
  - So there is **no "full SQAP in the appendix"**. 3.5 carries the QA plan itself as a compact table in the body.

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
| 3.1 | What "quality" means for Actual | Define quality in context | Quality views (L1) applied to Actual; "users trusting the numbers" [S01 `PRODUCT.md`]; which stakeholder cares about which view. | 200 |
| 3.2 | Key quality attributes | Pick and prioritise | One table rating all **9** ISO/IEC 25010:2023 characteristics for Actual (why it matters, stakeholder, priority). Deep-dive the top 4–5, likely **functional suitability (calculation correctness)**, **reliability (data integrity, sync)**, **security** (now strongly evidenced by the advisories), **maintainability** (volunteer contributors), and **interaction capability** (incl. inclusivity, i.e. accessibility). | 300 |
| 3.3 | Current QA practices (as-is) and gaps | Evidence-based assessment | Coverage table: practice → attributes it protects. Gaps: coverage, accessibility automation, performance, no QA plan, reactive-only security. | 300 |
| 3.4 | Selecting QA practices and standards | The "critically select" part | For each gap or attribute: candidate practices and standards → adopt / adapt / reject, with reasons. (Scope of standards: pending, question 1.) | 300 |
| 3.5 | Applying the QA process within Kanban (to-be) | The "apply" part | A **compact QA plan in the body** (table), structured by L3's SQAP sections and built into the Kanban workflow from Section 2: explicit policies and a **Definition of Done** per board column, quality gates, roles, defect and vulnerability handling. | 250 |
| 3.6 | Critical evaluation | Where most marks come from | Strengths, cost and limits for volunteers; risks (automation overhead, e.g. bots and CI slowing PRs [S43]); what still isn't covered. | 200 |

Total about **1,550 words**, all in the body.

## Context for the pending standards question

**Why the question matters.** The brief says QA must align with "**industry standards**", and 3.4 says "**critically select**". So the marker expects:
- a discussion of standards, beyond what Actual already does; and
- *reasoned choices*: why a standard fits or doesn't.

**The difficulty.** Lecture 4's standards (ISO 9001, ISO/IEC 27001, CMMI) are mostly **organisation-level management systems or maturity appraisals**. They assume a company that pays for audits and certification. Actual has no company behind it: just 8 core volunteers, about USD 3,000–3,500 a month in donations [S08], and stipends for review work.

**Options:**
- **(A) Lecture standards only.** Discuss ISO 9001, 27001, CMMI and 25010. Risk: the honest conclusion is that most don't fit a volunteer project, which leaves little to *apply*.
- **(B) Lecture standards + OSS-specific frameworks (my recommendation).** Also evaluate lightweight, free, open-source-specific industry frameworks, e.g.:
  - **OpenSSF Best Practices Badge / Scorecard**: built specifically for OSS projects;
  - **OWASP ASVS**: security requirements for the sync server's access-control flaws;
  - **WCAG**: Actual already claims 2.1 AA.
  
  Then **openly adopt the frameworks that fit and reject or "borrow principles only" from the heavy ones**, with reasons. This *is* the critical selection the brief asks for, and it produces concrete standards to apply in 3.5.
- **(C) OSS frameworks only.** Not recommended. It ignores the lecture standards the marker will look for.

All the standards and frameworks above are still **unverified** [S54–S61]. They will be checked before writing.

## Open questions

1. **Standards scope:** A, **B (recommended)** or C, now that the context is above?
2. **Security framing:** the advisories make security clearly a **top-priority attribute** and show the main gap is **proactive** security assurance (e.g. authorization tests, threat modelling or security review for new multi-user features), not the lack of a policy. Agree with this framing?
3. **Using the advisories as evidence:** OK to cite specific advisories (e.g. the critical "missing authentication for bank-sync endpoints")? It's strong, concrete evidence. Each would be cited as a GitHub advisory, and the severities taken as published by Actual's maintainers.
4. **Who reported the vulnerabilities?** This matters for Section 4: external researchers finding flaws = de facto *independent* verification. Could you open 2–3 advisories in your browser (e.g. GHSA-m2cq-xjgm-f668, GHSA-cq9c-6w48-qmfg, GHSA-prp4-2f49-fcgp) and tell me what the **"Credits"** section says?
5. **Severity mismatch:** GHSA-m62c-5q34-f3cf shows **Low** on Actual's page but **High** in the global database (OSV). I'd use the **maintainers' rating** and mention the difference only if relevant. OK?
6. **Does Actual's product have any AI features?** I'm not aware of any; please say if you know of one. If not, ISO/IEC 25059 (AI quality) is out of scope, and AI comes up only as a development-process topic.
