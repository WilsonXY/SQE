# 4 Integrating IV&V with Kanban

## 4.1 Purpose and meaning

Verification checks whether outputs meet their specified requirements. Validation checks whether the product meets users' needs and intended use. IEEE 1012-2024 covers both activities, with different V&V requirements for different integrity levels (IEEE, 2025). An Actual Budget implementation can meet its specification yet expose financial records or leave users misunderstanding their balances.

Independent assessment helps reviewers question developers' shared assumptions. NASA identifies three dimensions: technical independence separates assessors' judgement from the developer's; managerial independence gives a separate organisation control over assessment decisions; financial independence places the assessment budget outside development's control (National Aeronautics and Space Administration [NASA], n.d.). A colleague's review can provide technical separation while sharing the same management and funding arrangements.

IV&V should run alongside work throughout the proposed Kanban flow. Smith and Hayes (2024) explain why agile delivery still needs independent assessment: security weaknesses, in particular, may be invisible in demonstrations. This supports assessment that keeps pace with development, although their argument does not establish a need for a separate audit of every Actual contribution.

## 4.2 Existing checks and their independence

People other than a change's author can check work in Actual. Table 6 records their independence; a second check alone cannot establish full IV&V.

**Table 6. Current checking arrangements and evidential limits**

| Arrangement | Technical independence | Managerial and financial independence |
|---|---|---|
| Another maintainer reviews a PR | Possible when the reviewer did not develop the change | Not established: shared project governance and stipend arrangements |
| Release receives two other maintainer approvals and smoke tests | Multiple perspectives; smoke-test executor need not be independent | No separate assessment organisation or budget documented |
| CI checks implementation | Repeatable checks; tests still reflect their authors' assumptions | Automation supplies neither dimension |
| Community uses preview/nightly builds | Possible independent validation; participation is voluntary | Participants' circumstances are unknown |
| Vulnerability reporters identify released flaws | Separately credited discovery | Organisational control and funding are unverified |

The documented review, release and preview processes provide these opportunities (Actual Budget, n.d.-c, n.d.-e, n.d.-g, 2026a). Advisories credit iamsilk, Rex50527 and pyuysig with reporting one critical and two high access-control vulnerabilities (Actual Budget, 2026b, 2026c, 2026d). The credits identify who discovered the flaws, but cannot establish full independence. All three affected released versions, so the independent feedback arrived after release and potential exposure.

Actual's policy provides for private reporting and coordinated disclosure (Actual Budget, n.d.-h), a strength consistent with the practitioner preferences reported by Liu et al. (2025). The public material reviewed contains no evidence of a commissioned external security audit. An audit may nevertheless have taken place without appearing in that material.

## 4.3 A proportionate independence model

Actual should combine internal technical separation with external assessment when resources permit. Each substantive change needs a named reviewer who did not author it. Someone outside the immediate implementation area should also examine high-risk changes where the necessary expertise is available. When that separation is unavailable, the project should record the limitation and seek specialist help before moving the change forward. These arrangements leave routine maintainer review with limited independence.

The following three risk tiers are this report's proposal, inspired by IEEE 1012's integrity-level concept. They are separate from IEEE's prescribed levels:

- High: authentication, authorisation, encryption, bank integrations, synchronisation, financial calculations and migrations. Require independent review, targeted failure tests and recorded residual risks.
- Standard: ordinary functional changes with limited, recoverable impact. Require review, relevant CI checks and acceptance validation.
- Low: isolated documentation or cosmetic changes. Require proportionate review and applicable checks. Any effect on access, accessibility or financial meaning raises the tier.

The consequences of a change determine its tier. Even a small wording change needs greater scrutiny if it misrepresents a balance; its file type cannot justify a low-risk classification.

Pulling a card into the next stage would require assessment evidence, following Kanban's explicit-policy principle (Kanban University, n.d.). External assessment would retain private reporting and add an optional funded audit before major security-sensitive changes. OSTIF reports 24 published audits and 231 security findings in 2025 (Open Source Technology Improvement Fund, 2026). This established funding model for open-source assessment cannot guarantee Actual the same outcomes.

## 4.4 Activities within the workflow

Table 7's proposed policies connect lifecycle activities to Section 2's board. Maintenance returns completed work to the backlog for further attention. Each activity has a responsible person whose assessment and decisions the tools support.

**Table 7. Proposed V&V activities and movement conditions**

| Lifecycle activity / board stage | Activity and evidence | Tools | Independent role | Exit condition |
|---|---|---|---|---|
| Requirements / Backlog–triage | Challenge intended behaviour, misuse cases and risk tier; define testable acceptance criteria | Issue template; risk label | Non-author reviewer; user representative where available | Criteria, tier and reviewer recorded |
| Design / Ready–design | Examine trust boundaries; check data integrity and recovery assumptions; record significant decisions | ADR; applicable ASVS checklist | Non-author reviewer; security specialist for high-risk access changes | Design concerns resolved; targeted tests agreed |
| Implementation / Build–PR | Trace requirements to changed code; inspect adverse paths; add regression tests | Linked PR; Vitest; CodeQL; dependency review | Non-author reviewer; additional domain reviewer where needed | Review complete; applicable checks pass; findings resolved |
| Testing / Verify | Independently reproduce acceptance cases; test denied access, restore/sync failures and keyboard interaction as relevant | Playwright; preview; isolated test server; synthetic budgets | Reviewer or community tester outside implementation | Acceptance evidence recorded; material failures corrected |
| Deployment / Release | Check accumulated evidence and unresolved risks; independently smoke-test candidate Docker and desktop builds | Release checklist; candidate builds | Two other maintainers; non-author smoke tester | Required approvals, smoke results and recovery instructions recorded |
| Maintenance / Done → Backlog | Triage incidents privately where necessary; verify fixes; add regression cases; coordinate disclosure | GitHub private reports; advisories; issue links | Non-author fix reviewer; reporter invited to retest | Fix verified and disclosed appropriately; follow-up risks enter backlog |

These proposed policies extend Actual's tooling and release approvals, without assuming that the gates already operate. Preview and nightly web builds lack a bundled sync server, so server checks need an isolated instance with synthetic data (Actual Budget, n.d.-g). ASVS supplies the basis for checklists that verify application security controls (OWASP Foundation, 2025). Reliability checks need their own expected results: passing a security checklist cannot establish correct calculations or recovery.

Unresolved required findings keep a card blocked within the relevant WIP limit. The monthly release date cannot override a failed gate. An incomplete feature waits for a later release; an urgent security fix receives expedited assessment.

## 4.5 Contribution to the assignment's three goals

Design review and negative tests support early defect detection before release. GHSA-m2cq describes six bank-sync endpoints that lacked authentication middleware (Actual Budget, 2026c). Tests requiring each protected endpoint to reject an unauthenticated request could reveal that omission. Their effectiveness depends on covering every endpoint and specifying the correct expected result.

For requirements compliance, the evidence chain runs from issue and acceptance criterion through PR and test evidence to release note. This lets a reviewer reject an implementation that passes existing tests yet fails the agreed user need.

Improving overall quality depends on whether the evidence affects release decisions and subsequent failures decline. Reviewing escaped defects, including whether regression tests now cover their causes, feeds further work into the backlog. These outcomes remain proposals for later evaluation; the report has not demonstrated them.

## 4.6 Constraints and trade-offs

Actual's internal reviewers share its governance, priorities and funding, preventing full managerial or financial independence. An external auditor should control technical methods and report findings without developer veto, with a third-party funder protecting the assessment budget. Those conditions require attention even when the assessor is external.

Every additional gate takes reviewer time. After Actual became open source, PRs waited months for review (Aboltins, 2025). WIP limits based on capacity and different assessment requirements for each risk tier should keep the burden proportionate. The payment guide also acknowledges the possibility of superficial approvals (Actual Budget, n.d.-f). Review records should state the claims tested and concerns unresolved, giving more useful evidence than a count of approval clicks.

The payment guide reports average monthly income of USD 3,000 to 3,500, with USD 2,000 allocated to reviewer stipends (Actual Budget, n.d.-f). These figures leave audit funding undetermined: a commissioned assessment would depend on available funds or sponsorship. Scanner false positives and shortages of specialists can delay work further. Actual should begin with internal review based on risk, adding targeted external assessment once its scope, funding and independence are secured.
