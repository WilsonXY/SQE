# 4 Integrating IV&V with Kanban

## 4.1 Purpose and meaning

Verification examines whether development outputs meet their specified requirements. Validation examines whether the resulting product meets users' needs and intended use. IEEE 1012-2024 covers both activities and specifies different V&V requirements for different integrity levels (IEEE, 2025). For Actual Budget, correct implementation is insufficient if a feature exposes financial records or allows users to misunderstand their balances.

Independence adds protection against assumptions shared by developers. NASA distinguishes technical independence, where assessors exercise judgement separately from the developer; managerial independence, where a separate organisation controls assessment decisions; and financial independence, where the assessment budget is controlled independently of development (National Aeronautics and Space Administration [NASA], n.d.). A colleague's review can provide technical separation without satisfying all three dimensions.

IV&V should therefore accompany work throughout the proposed Kanban flow. Smith and Hayes (2024) explain that agile delivery still needs independent assessment, particularly because security weaknesses may remain invisible in demonstrations. Their argument supports timely assurance; it does not establish that every Actual contribution needs a separate audit.

## 4.2 Existing checks and their independence

Actual already provides opportunities for checking by people other than a change's author. Table 6 evaluates their independence rather than treating every second check as full IV&V.

**Table 6. Current checking arrangements and evidential limits**

| Arrangement | Technical independence | Managerial and financial independence |
|---|---|---|
| Another maintainer reviews a PR | Possible when the reviewer did not develop the change | Not established: shared project governance and stipend arrangements |
| Release receives two other maintainer approvals and smoke tests | Multiple perspectives; smoke-test executor need not be independent | No separate assessment organisation or budget documented |
| CI checks implementation | Repeatable checks; tests still reflect their authors' assumptions | Automation supplies neither dimension |
| Community uses preview/nightly builds | Possible independent validation; participation is voluntary | Participants' circumstances are unknown |
| Vulnerability reporters identify released flaws | Separately credited discovery | Organisational control and funding are unverified |

The documented review, release and preview processes support these opportunities (Actual Budget, n.d.-c, n.d.-e, n.d.-g, 2026a). Advisories credit iamsilk, Rex50527 and pyuysig with reporting one critical and two high access-control vulnerabilities (Actual Budget, 2026b, 2026c, 2026d). Credits establish discovery attribution, not full independence. These defects affected released versions, demonstrating that independent feedback sometimes arrives after exposure.

Actual's private reporting and coordinated disclosure policy is a strength (Actual Budget, n.d.-h). This accords with practitioner preferences reported by Liu et al. (2025). However, the public material reviewed provides no evidence of a commissioned external security audit; absence of public evidence does not prove that none occurred.

## 4.3 A proportionate independence model

The proposed model combines internal technical separation with external assessment where resources permit. Each substantive change should have an identified reviewer who did not author it. High-risk changes should additionally be examined by someone outside the immediate implementation area where expertise allows. If that separation is unavailable, the limitation should be recorded and specialist help sought before the change advances. Routine maintainer review remains a limited form of independence.

Inspired by IEEE 1012's integrity-level concept, this report proposes three risk tiers. These are the report's own categories, rather than IEEE-prescribed levels:

- **High:** authentication, authorisation, encryption, bank integrations, synchronisation, financial calculations and migrations. Require independent review, targeted failure tests and recorded residual risks.
- **Standard:** ordinary functional changes with limited, recoverable impact. Require review, relevant CI checks and acceptance validation.
- **Low:** isolated documentation or cosmetic changes. Require proportionate review and applicable checks. Any effect on access, accessibility or financial meaning raises the tier.

Risk follows consequences rather than file type. A small wording change that misrepresents a balance cannot automatically qualify as low risk.

Assessment evidence becomes an explicit condition for pulling cards between stages, consistent with Kanban's explicit-policy principle (Kanban University, n.d.). External augmentation retains private reporting and adds an optional funded audit before major security-sensitive changes. OSTIF reports 24 published audits and 231 security findings in 2025, illustrating an established funding model for open-source assessment rather than guaranteeing Actual similar outcomes (Open Source Technology Improvement Fund, 2026).

## 4.4 Activities within the workflow

Table 7 turns the model into proposed working policies. The lifecycle activities map onto Section 2's board; maintenance feeds completed work back into the backlog. Tools support assessment, while named people remain responsible for decisions.

**Table 7. Proposed V&V activities and movement conditions**

| Lifecycle activity / board stage | Activity and evidence | Tools | Independent role | Exit condition |
|---|---|---|---|---|
| Requirements / Backlog–triage | Challenge intended behaviour, misuse cases and risk tier; define testable acceptance criteria | Issue template; risk label | Non-author reviewer; user representative where available | Criteria, tier and reviewer recorded |
| Design / Ready–design | Examine trust boundaries; check data integrity and recovery assumptions; record significant decisions | ADR; applicable ASVS checklist | Non-author reviewer; security specialist for high-risk access changes | Design concerns resolved; targeted tests agreed |
| Implementation / Build–PR | Trace requirements to changed code; inspect adverse paths; add regression tests | Linked PR; Vitest; CodeQL; dependency review | Non-author reviewer; additional domain reviewer where needed | Review complete; applicable checks pass; findings resolved |
| Testing / Verify | Independently reproduce acceptance cases; test denied access, restore/sync failures and keyboard interaction as relevant | Playwright; preview; isolated test server; synthetic budgets | Reviewer or community tester outside implementation | Acceptance evidence recorded; material failures corrected |
| Deployment / Release | Check accumulated evidence and unresolved risks; independently smoke-test candidate Docker and desktop builds | Release checklist; candidate builds | Two other maintainers; non-author smoke tester | Required approvals, smoke results and recovery instructions recorded |
| Maintenance / Done → Backlog | Triage incidents privately where necessary; verify fixes; add regression cases; coordinate disclosure | GitHub private reports; advisories; issue links | Non-author fix reviewer; reporter invited to retest | Fix verified and disclosed appropriately; follow-up risks enter backlog |

The table extends existing tooling and release approvals rather than assuming that these gates already operate. Actual's preview and nightly web builds have no bundled sync server; server checks therefore need an isolated instance and synthetic data (Actual Budget, n.d.-g). Security checklists draw on ASVS, which provides a basis for verifying application security controls (OWASP Foundation, 2025). Reliability checks need their own expected results; passing a security checklist cannot establish correct calculations or recovery.

Cards with unresolved required findings remain blocked and count towards the relevant WIP limit. A monthly release date does not override a failed gate: an incomplete feature waits for a later release, while an urgent security fix receives expedited assessment.

## 4.5 Contribution to the assignment's three goals

For early defect detection, design review and negative tests target mistakes before release. GHSA-m2cq describes six bank-sync endpoints missing authentication middleware (Actual Budget, 2026c). Requiring an unauthenticated request to be rejected at each protected endpoint could expose that omission. Detection remains conditional on complete endpoint coverage and correct test expectations.

Requirements compliance becomes inspectable through a chain from issue and acceptance criterion to PR, test evidence and release note. A reviewer can reject an implementation that passes existing tests but fails the agreed user need.

Overall quality improves only if this evidence changes release decisions and subsequent failures decline. Reviewing escaped defects and whether their causes now have regression coverage provides feedback to the backlog. These are proposed outcomes to evaluate later, not results demonstrated by this report.

## 4.6 Constraints and trade-offs

Internal reviewers share Actual's governance, priorities and funding, so the proposal cannot promise full managerial or financial independence. An external auditor should control technical methods and report findings without developer veto; a third-party funder should protect the assessment budget. External status alone is insufficient.

Additional gates also consume scarce reviewer time. Actual's post-open-source backlog left PRs waiting months for review (Aboltins, 2025). Capacity-aware WIP limits and differentiated risk tiers should prevent all changes receiving the same assessment burden. Review quality also matters: the payment guide acknowledges the possibility of superficial approvals (Actual Budget, n.d.-f). Recording tested claims and unresolved concerns is more useful than counting approval clicks.

Funding remains a constraint. The published payment guide reports average monthly income of USD 3,000–3,500, with USD 2,000 allocated to reviewer stipends (Actual Budget, n.d.-f). A commissioned audit consequently depends on available funds or sponsorship; these figures do not constitute an audit budget. Scanner false positives and specialist shortages can further delay work. The recommended starting point is risk-based internal review, with targeted external assessment added when its scope, funding and independence can be secured.
