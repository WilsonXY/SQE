# Section 4 — Integrating IV&V with Kanban (10 marks)

Status: **In discussion.** First proposal, 2026-10-21.

## What the brief asks

> "To analyse and implement the integration of Independent Verification and Validation (IV&V) processes within the [Selected Methodology] framework to facilitate early defect detection, ensure requirements compliance, and improve overall software quality."

The marker will look for:
1. **Analyse**: what IV&V is, and what Actual has today.
2. **Implement**: a concrete integration *inside Kanban*, not a generic IV&V description.
3. The three goals, each shown explicitly: **early defect detection**, **requirements compliance**, **overall quality**.
4. Critical evaluation.

The selected methodology is **Kanban**, tailored (Section 2).

## Relevant lecture guidance (not cited)

- **L6:** V vs V; verification activities (code review, unit and integration testing, static analysis, design verification); validation activities (functional testing, requirements validation, regulatory compliance validation, documentation validation).
- **L6 IV&V per phase:** requirements, design, implementation, testing, deployment, maintenance. Each phase has **activities, tools, roles, outcome**.
- **L6 benefits:** early detection, reliability, compliance, objective assessment.
- **L4:** IEEE 1012 / 1059 (now superseded by **IEEE 1012-2024** [S67]).

## Evidence (verified; see `research/` and `sources.md` → D3)

**IV&V concepts:**
- IEEE 1012-2024 is the current V&V standard [S67]. V&V checks conformance to requirements *and* intended use. V&V rigour depends on **integrity levels**.
- Independence has **three dimensions: technical, managerial and financial** [S68, NASA citing IEEE].
- **IV&V in agile:** agile "has in no way diminished the need for IV&V". Security is not easily demonstrable through user-visible behaviour, and IV&V should run "in phase with the development cadence" [S69].

**Kanban mechanism:** "make process policies explicit": **entry and exit criteria** for moving work between board columns [S38, p. 98]. This is where IV&V gates go.

**Independent checking Actual already has (as-is):**
- PR review by another maintainer [S04];
- the 2-maintainer release approval plus smoke test [S03];
- CI checks [S01];
- PR preview builds and nightly builds for community validation [S66];
- **external, non-core reporters who found 1 critical and 2 high vulnerabilities**, through private reporting and coordinated disclosure [S62, S63];
- Actual's coordinated-disclosure process matches what most practitioners recommend, which many OSS projects don't follow (only 55% of vulnerabilities do) [S70].

**Gaps:**
- independence is **ad hoc and mostly after release**: the critical and high flaws reached released versions;
- non-controversial PRs can be merged straight away by one maintainer [S04];
- no risk-based tiering of V&V effort;
- **no evidence of an external security audit** (docs/blog search).

**Real-world proof that IV&V options work:**
- NASA's IV&V Program [S68];
- OSTIF-funded OSS security audits: 24 audits in 2025, 231 findings, over 98% fixed [S72].

## Proposed flow (pending approval)

Same as-is → to-be logic as Sections 2 and 3.

| # | Subsection | Purpose | Main content | ~Words |
|---|---|---|---|---|
| 4.1 | V&V, IV&V and why Actual needs it | Concepts, briefly | V vs V [S67]; three kinds of independence [S68]; integrity levels [S67]; agile still needs IV&V, especially for security [S69]. Why for Actual: financial data, and real escaped vulnerabilities [S63]. | 200 |
| 4.2 | Current V&V in Actual and how independent it is (as-is) | The "analyse" part | Table: each existing V&V activity → who does it → technical / managerial / financial independence (yes / partial / no). Finding: real but ad hoc, and the strongest independence (external reporters) happens **after** release. | 250 |
| 4.3 | IV&V integration model for Kanban (to-be) | The "implement" part: design decisions | (a) **Independence level** Actual can realistically afford: an **internal independent reviewer role** plus **external augmentation** (the existing disclosure channel and an optional funded audit [S72]). (b) **Risk-tiering by integrity level** [S67]: e.g. *high* = authentication/authorization, sync, money calculations, migrations, bank sync; *standard* = UI and copy. (c) **Embedded as Kanban explicit policies** (entry and exit criteria per column) [S38], running in Kanban's cadence [S69]. | 250 |
| 4.4 | IV&V activities across the Kanban workflow | The core table (Lecture 6 format) | One table: Lecture 6's six phases mapped to Kanban stages (requirements/triage → design → build/PR → verify → release train → operate/maintain), with **IV&V activities, tools, independent role, exit criterion** for each. E.g. high-integrity items need an independent reviewer (not the author, not the area owner) using an OWASP ASVS checklist; authorization tests; a threat-model note in the ADR; validation on the preview build; an independent release smoke test; a regression test for every fixed advisory. | 400 (table words count) |
| 4.5 | How the integration achieves the three goals | Show the brief's goals explicitly | **Early defect detection:** e.g. GHSA-m2cq (missing auth middleware) would be caught at the design/PR gate by the ASVS authentication checklist and authorization tests. **Requirements compliance:** traceability chain feature request → acceptance criteria → PR "Fixes #" → tests → release note (Actual already has most links). **Overall quality:** fewer escaped defects; measured in Assignment 2. | 150 |
| 4.6 | Critical evaluation | Where most marks come from | Full IEEE independence (managerial, financial) is not achievable inside a volunteer project. Independence vs flow: extra gates risk recreating the 2022 review backlog [S10] and adding to maintainer burnout [S47], mitigated by tiering and WIP limits. Audit cost vs donations [S08]. Rubber-stamp risk. Tool false positives. | 200 |

Total about **1,450 words**.

## Open questions

1. **Flow 4.1–4.6:** OK?
2. **Independence model:** agree with the honest position that Actual can achieve **technical independence** internally, but full **managerial and financial** independence only through external parties (vulnerability reporters, a funded audit)? The design is "internal independent reviewer + external augmentation".
3. **Integrity-level tiering:** the concept comes from IEEE 1012-2024 (we can only cite its abstract, because the full text is paywalled). The actual tiers for Actual would be **our own design, clearly labelled as such**. OK?
4. **Phase mapping:** map Lecture 6's six phases onto **six Kanban stages** (requirements/triage, design, build/PR, verify, release train, operate/maintain)? This keeps the lecture's structure and stays inside Kanban.
5. **External audit recommendation:** include an optional, periodic **funded external security audit** (OSTIF model) paid from the donation surplus? It's strong real-world proof, but it adds a cost claim. The cost would only be estimated properly in Assignment 2 (Estimation).
6. **Figure:** Sections 1–2 plan 3 figures and Section 3 has none. Should Section 4 have **no new figure** (the 4.4 table carries it), or should the 2.5 to-be workflow figure show the IV&V gates so one figure serves both sections?
7. **Word budget for Assignment 1:** the current plan adds up to about **5,300 words**: Intro ~600 + Section 2 ~1,500 + Section 3 ~1,550 + Section 4 ~1,450 + optional conclusion ~200. Does the **executive summary** count towards the ~5,000? Is 5,300 acceptable as "approximately 5,000", or should we trim each section by about 5–10%?
8. **Conclusion (Section 5) in Assignment 1:** include a short one (~150–200 words) or not? The brief doesn't require it for Assignment 1, but it helps the report end cleanly.
