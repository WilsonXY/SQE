# 4 Integrating IV&V with Kanban

## 4.1 Purpose and meaning

Verification checks whether development outputs meet specified requirements. Validation checks whether the product meets users' needs and intended use. IEEE 1012-2024 covers both and assigns different V&V requirements to different integrity levels (IEEE, 2025). For Actual Budget, a correctly implemented feature can still expose financial records or leave users misunderstanding balances.

Independence helps challenge assumptions that developers share. NASA distinguishes three dimensions. Technical independence allows assessors to exercise judgement separately from the developer. Managerial independence places assessment decisions under a separate organisation. Financial independence requires independent control of the assessment budget (National Aeronautics and Space Administration [NASA], n.d.). A colleague's review may provide technical separation while leaving the other dimensions unmet.

IV&V should accompany work throughout the proposed Kanban flow. Smith and Hayes (2024) explain that agile delivery still needs independent assessment, especially where demonstrations leave security weaknesses unseen. Their argument supports timely assurance. It does not establish a need for a separate audit of every Actual contribution.

## 4.2 Existing checks and their independence

Actual allows people other than a change's author to check the work. Table 6 assesses the independence of those arrangements. A second check does not automatically qualify as full IV&V.

**Table 6. Current checking arrangements and evidential limits**

| Arrangement | Technical independence | Managerial and financial independence |
|---|---|---|
| Another maintainer reviews a PR | Possible when the reviewer did not develop the change | Not established: shared project governance and stipend arrangements |
| Release receives two other maintainer approvals and smoke tests | Multiple perspectives; smoke-test executor need not be independent | No separate assessment organisation or budget documented |
| CI checks implementation | Repeatable checks; tests still reflect their authors' assumptions | Automation supplies neither dimension |
| Community uses preview/nightly builds | Possible independent validation; participation is voluntary | Participants' circumstances are unknown |
| Vulnerability reporters identify released flaws | Separately credited discovery | Organisational control and funding are unverified |

The documented review, release and preview processes provide these opportunities (Actual Budget, n.d.-c, n.d.-e, n.d.-g, 2026a). Advisories credit iamsilk, Rex50527 and pyuysig with reporting one critical and two high access-control vulnerabilities (Actual Budget, 2026b, 2026c, 2026d). The credits identify discoverers, but cannot establish full independence. These defects affected released versions, so independent feedback sometimes arrived after release and potential exposure. This does not establish observed compromise.

Actual's private reporting and coordinated disclosure policy is a strength (Actual Budget, n.d.-h). It accords with the practitioner preferences reported by Liu et al. (2025). The reviewed public material contains no evidence of a commissioned external security audit. This absence cannot establish that no audit occurred.

## 4.3 A proportionate independence model

The proposed model combines internal technical separation with external assessment when resources allow. Each substantive change needs an identified reviewer who did not author it. High-risk changes also need examination by someone outside the immediate implementation area where suitable expertise is available. If that separation is unavailable, the project should record the limitation and seek specialist help before advancing the change. Routine maintainer review provides limited independence.

The report proposes three risk tiers inspired by IEEE 1012's integrity-level concept. These categories belong to this proposal. They are not IEEE-prescribed levels.

- High risk covers authentication, authorisation, encryption, bank integrations, synchronisation, financial calculations and migrations. These changes require independent review, targeted failure tests and recorded residual risks.
- Standard risk covers ordinary functional changes with limited, recoverable impact. These changes require review, relevant CI checks and acceptance validation.
- Low risk covers isolated documentation or cosmetic changes. These changes require proportionate review and applicable checks. Effects on access, accessibility or financial meaning raise the tier.

Consequences determine risk. File type alone cannot establish it. A small wording change that misrepresents a balance cannot automatically qualify as low risk.

Assessment evidence becomes an explicit condition for moving cards between stages, consistent with Kanban's explicit-policy principle (Kanban University, n.d.). External assessment retains private reporting and adds an optional funded audit before major security-sensitive changes. OSTIF reports 24 published audits and 231 security findings in 2025 (Open Source Technology Improvement Fund, 2026). These figures illustrate an established funding model for open-source assessment. They do not predict comparable outcomes for Actual.

## 4.4 Activities within the workflow

Table 7 expresses the model as proposed working policies. The lifecycle activities map onto Section 2's board, with maintenance returning completed work to the backlog. Tools assist assessment. Named people remain responsible for decisions.

**Table 7. Proposed V&V activities and movement conditions**

| Lifecycle activity / board stage | Activity and evidence | Tools | Independent role | Exit condition |
|---|---|---|---|---|
| Requirements / Backlog–triage | Challenge intended behaviour, misuse cases and risk tier; define testable acceptance criteria | Issue template; risk label | Non-author reviewer; user representative where available | Criteria, tier and reviewer recorded |
| Design / Ready–design | Examine trust boundaries; check data integrity and recovery assumptions; record significant decisions | ADR; applicable ASVS checklist | Non-author reviewer; security specialist for high-risk access changes | Design concerns resolved; targeted tests agreed |
| Implementation / Build–PR | Trace requirements to changed code; inspect adverse paths; add regression tests | Linked PR; Vitest; CodeQL; dependency review | Non-author reviewer; additional domain reviewer where needed | Review complete; applicable checks pass; findings resolved |
| Testing / Verify | Independently reproduce acceptance cases; test denied access, restore/sync failures and keyboard interaction as relevant | Playwright; preview; isolated test server; synthetic budgets | Reviewer or community tester outside implementation | Acceptance evidence recorded; material failures corrected |
| Deployment / Release | Check accumulated evidence and unresolved risks; independently smoke-test candidate Docker and desktop builds | Release checklist; candidate builds | Two other maintainers; non-author smoke tester | Required approvals, smoke results and recovery instructions recorded |
| Maintenance / Done → Backlog | Triage incidents privately where necessary; verify fixes; add regression cases; coordinate disclosure | GitHub private reports; advisories; issue links | Non-author fix reviewer; reporter invited to retest | Fix verified and disclosed appropriately; follow-up risks enter backlog |

These gates extend existing tools and release approvals. The table does not claim that Actual already operates them. Preview and nightly web builds have no bundled sync server, so server checks need an isolated instance and synthetic data (Actual Budget, n.d.-g). ASVS supplies requirements for verifying application security controls (OWASP Foundation, 2025). Reliability checks need separate expected results because a passed security checklist cannot establish correct calculations or recovery.

Cards remain blocked while required findings are unresolved and continue to count towards the relevant WIP limit. A monthly release date cannot override a failed gate. An incomplete feature waits for a later release. An urgent security fix receives expedited assessment.

## 4.5 Contribution to the assignment's three goals

Design review and negative tests support early defect detection by checking mistakes before release. GHSA-m2cq describes six bank-sync endpoints without authentication middleware (Actual Budget, 2026c). Tests requiring each protected endpoint to reject an unauthenticated request could reveal that omission. Detection still depends on covering every relevant endpoint and setting correct test expectations.

Requirements compliance becomes inspectable when issue and acceptance criterion link to PR, test evidence and release note. Existing tests may pass while the agreed user need remains unmet. A reviewer can reject the implementation on that basis.

Overall quality improves only when assessment evidence affects release decisions and subsequent failures decline. Reviewing escaped defects and checking whether regression tests now cover their causes provides feedback for the backlog. These outcomes need later evaluation. This report does not demonstrate that they have occurred.

## 4.6 Constraints and trade-offs

Internal reviewers share Actual's governance, priorities and funding. The proposal therefore cannot promise full managerial or financial independence. An external auditor should control technical methods and report findings without developer veto. A third-party funder should protect the assessment budget. Being external does not establish those safeguards by itself.

Additional gates consume scarce reviewer time. After Actual became open source, PRs sometimes waited months for review (Aboltins, 2025). WIP limits based on capacity and differentiated risk tiers should allocate assessment effort proportionately. Review quality also requires attention. The payment guide acknowledges the possibility of superficial approvals (Actual Budget, n.d.-f). Recorded test claims and unresolved concerns provide more useful evidence than approval counts alone.

Funding constrains external assessment. The payment guide reports average monthly income of USD 3,000–3,500 and allocates USD 2,000 to reviewer stipends (Actual Budget, n.d.-f). A commissioned audit depends on available funds or sponsorship. These figures are not an audit budget. Scanner false positives and shortages of specialists can also delay work. Adoption should start with risk-based internal review, adding targeted external assessment when scope, funding and independence can be secured.
