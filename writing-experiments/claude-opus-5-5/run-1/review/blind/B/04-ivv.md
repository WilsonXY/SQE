# 4 Integrating IV&V with Kanban

## 4.1 V&V, IV&V and why Actual needs them

IEEE 1012-2024 describes verification as checking whether the products of an activity conform to that activity's requirements, and validation as checking whether the product satisfies its intended use and user needs (IEEE, 2025). It specifies V&V requirements for different integrity levels. Independent V&V (IV&V) adds a condition on who does the checking. NASA, following IEEE, defines independence along three parameters: technical (assessors judge the work independently of the developer), managerial (responsibility for IV&V sits in a separate organisation) and financial (the IV&V budget is controlled by an organisation independent of development) (National Aeronautics and Space Administration, n.d.).

Smith and Hayes (2024, Abstract) argue that the move to agile "has in no way diminished the need for IV&V". They note that security may not be readily demonstrable through user-visible behaviour, and recommend that IV&V runs in phase with the development cadence. Both points apply to Actual. It holds personal financial data, and its sync server has had critical and high-severity access-control flaws published as advisories in 2026 (Actual Budget, 2026c, 2026d).

## 4.2 Current V&V in Actual and its independence (as-is)

*Table 4.1. Independence of Actual's existing V&V activities.*

| Activity | Performed by | Technical | Managerial | Financial |
|---|---|---|---|---|
| PR review | Another core maintainer; non-controversial PRs may be merged straight away (Actual Budget, n.d.-e) | Yes | No | No: reviewers share one stipend pool (Actual Budget, n.d.-f) |
| Release approval and smoke test | At least two other maintainers (Actual Budget, n.d.-c) | Yes | No | No |
| CI tests and CodeQL scanning | Automated, configured by the team (Actual Budget, 2026a) | Partial | No | No |
| PR preview and nightly builds | Any community member, voluntarily (Actual Budget, n.d.-g) | Partial | Not established | Not established |
| Vulnerability reports | Reporters outside the core team (Actual Budget, 2026c) | Yes | Not established | Not established |
| External audit | No public evidence found (October 2026) | — | — | — |

Independent checking exists in Actual, but it is ad hoc and mostly technical. Internal reviewers share one small team, release goals and donation-funded pool, so they cannot provide managerial or financial independence. The strongest independent findings also came after release: the three advisories examined for this report credit iamsilk, Rex50527 and pyuysig, none of whom is a core maintainer, with discovering a critical and two high-severity flaws in released versions (Actual Budget, 2026b, 2026c, 2026d). These credits show who found the flaws. They say nothing about the reporters' organisations or funding, so the evidence supports technical independence only.

Actual asks for private reporting and coordinated disclosure (Actual Budget, n.d.-h), which most OSS practitioners support but only 55% of studied vulnerabilities actually followed (Liu et al., 2025). No public evidence of an external security audit was found in the documentation and blog reviewed (October 2026).

## 4.3 IV&V integration model for Kanban (to-be)

Inside the project, only technical independence is achievable, and a maintainer review is not full IV&V in the IEEE sense. The proposal therefore adds an *independent reviewer* role for high-risk work: a maintainer who is neither the author nor the code owner of the affected area. Managerial and financial independence must come from outside, through the existing coordinated-disclosure channel and an optional, periodic funded external security audit. The Open Source Technology Improvement Fund (OSTIF) shows that funded audits are workable for OSS: it self-reports 24 audits published in 2025, with 231 security-relevant findings and over 98% fixed (Open Source Technology Improvement Fund, 2026). Financial independence is stronger when a third party, not Actual, pays.

How much checking an item receives depends on its risk. Inspired by IEEE 1012's integrity-level concept (IEEE, 2025), this report proposes its own three tiers, which are not IEEE's scheme:

- *High*: authentication, authorisation and sessions; bank-sync endpoints; budget and balance calculations; database migrations; sync and encryption.
- *Standard*: most features, such as reports, rules and UI components.
- *Low*: themes, wording and documentation.

Kanban makes process policies explicit as entry and exit criteria that determine when an item may be pulled into the next state (Ahmad et al., 2018, p. 98), and the IV&V checks sit in those criteria. The tier label set at triage decides which criteria apply, and independent-reviewer capacity counts within the WIP limits that the Kanban Method uses to manage flow (Kanban University, n.d.). Each item is therefore checked as it moves, in phase with the flow (Smith & Hayes, 2024). Section 3 defines *what* each QA gate checks; Section 4 adds *who* verifies it and what independent evidence is required.

## 4.4 IV&V activities across the Kanban workflow

*Table 4.2. IV&V activities, tools, roles and exit criteria per Kanban stage (high-tier items unless stated).*

| Stage (lifecycle phase) | IV&V activities | Tools | Independent role | Exit criterion |
|---|---|---|---|---|
| Requirements/triage (requirements) | Assign risk tier; validate that acceptance criteria are testable and include security criteria | Issue templates, triage labels | Triager other than the requester | Tier and testable criteria recorded |
| Design (design) | Review design and a short threat note against access-control requirements | ADR, OWASP ASVS 5.0.0 | Independent reviewer | Threat note accepted; ASVS requirements selected |
| Build/PR (implementation) | Code review against selected ASVS requirements; check authorisation and regression tests exist | GitHub review, CodeQL, CI | Independent reviewer (not author, not code owner) | Approval citing ASVS IDs and tests; CI green |
| Verify (testing) | Validate behaviour on preview build; run server and security tests on a separate test server with synthetic budgets | Preview builds, Playwright, Vitest | Validator other than the author | Evidence attached; no open high findings |
| Release train (deployment) | Verify the release candidate and that every high-tier item met its exit criteria | Release checklist, Docker and desktop builds | At least two other maintainers; one checks tier evidence | Signed-off evidence before final release |
| Operate/maintain (maintenance) | Triage reports; add a regression test for each fixed advisory; feed findings back to triage | Private vulnerability reporting, advisories | External reporters; optional funded auditor | Advisory published; regression test merged |

Standard-tier items skip the design threat note and need only preview-build validation; low-tier items follow normal review. The ASVS suits the sync server's advisory history because it provides a basis for testing web application technical security controls (OWASP Foundation, 2025). Preview and nightly web builds include no sync server (Actual Budget, n.d.-g), so the Verify stage needs a separate controlled server. At the release train, the proposal asks for evidence before final approval; it does not assume that current smoke testing precedes every publication step (Actual Budget, n.d.-c).

## 4.5 How the integration meets the three goals

**Early defect detection.** GHSA-m2cq-xjgm-f668 arose because six SimpleFIN and Pluggy.ai endpoints lacked authentication middleware (Actual Budget, 2026c). Bank-sync work is high tier under the model, so an independent reviewer would apply ASVS authentication requirements, backed by authorisation tests, at the design or PR gate. That gives a defined point to detect the omission before release.

**Requirements compliance.** Each requirement is linked to its evidence: feature request, testable acceptance criteria, a PR referencing the issue, tests and the release note. Actual already has most of these links, and the independent reviewer checks that the chain is complete.

**Overall quality.** Tiering puts scarce review effort where failure costs most, with the aim of reducing escaped defects. Assignment 2 addresses how to measure this.

## 4.6 Critical evaluation

Even with the new role, the model cannot deliver full IEEE-style independence. The independent reviewer belongs to the same team and stipend pool, so managerial and financial independence still depend on outsiders, whose involvement is voluntary or funded.

Independence also competes with flow. After open-sourcing, PRs waited months for review (Aboltins, 2025), and growing demands on maintainers' time contribute to burnout in OSS projects (Salkever, 2023). A second, non-owner reviewer on every item would recreate that backlog. Tiering and WIP limits reduce this risk, but assigning a tier is a judgement and may understate risk.

Cost limits the external part of the model. Actual receives about USD 3,000–3,500 a month in donations, of which USD 2,000 is allocated to review stipends (Actual Budget, n.d.-f), so a funded audit depends on donors or a third-party funder. Its cost is estimated in Assignment 2.

Gates can also turn into box-ticking. Actual's own payment guide concedes that rubber-stamp reviews to earn points are theoretically possible (Actual Budget, n.d.-f). Requiring cited ASVS IDs and named tests makes approval harder to fake, though not impossible. ASVS also covers technical security controls only (OWASP Foundation, 2025), so reliability and interaction capability rely on Section 3's gates.

<!-- Cited: S01, S03, S04, S08, S10, S38, S47, S58, S62, S63-m2cq, S63-prp4, S63-cq9c, S66, S67, S68, S69, S70, S72, S109 -->
