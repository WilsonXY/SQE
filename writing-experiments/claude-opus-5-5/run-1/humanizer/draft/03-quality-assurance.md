# 3 Quality Assurance Process

## 3.1 What Quality Means for Actual

Actual's product documentation defines success as "users trusting the numbers" (Actual Budget, 2026a, Product Purpose section). For a user, that means balances and envelope totals that are correct, private and easy to follow. Seen as a product, Actual earns that trust through properties such as access control on the sync server and the integrity of synchronised data. The process view asks whether the workflow produces those properties reliably.

Stakeholders weight these views differently. Users and families want correct, private budgets. Self-hosters carry extra risk because their server holds bank-sync credentials. Volunteer maintainers need checks that leave their scarce review time intact. A QA process for Actual therefore has to protect financial data without stalling a volunteer flow.

## 3.2 Key Quality Attributes

ISO/IEC 25010:2023 defines nine product quality characteristics (International Organization for Standardization & International Electrotechnical Commission, 2023). In Table 3.1, each is rated for the *additional* assurance effort it deserves in Actual.

*Table 3.1. ISO/IEC 25010:2023 characteristics rated for Actual.*

| Characteristic | Reason | Priority |
|---|---|---|
| Functional suitability | Correct totals are essential, but budget-calculation tests already exist | Medium |
| Performance efficiency | Personal-scale data volumes | Low |
| Compatibility | Web, desktop and server must sync | Medium |
| Interaction capability | WCAG target set but unchecked | **High** |
| Reliability | Sync, migrations and recovery protect data | **High** |
| Security | Sensitive financial data; repeated advisories | **High** |
| Maintainability | Volunteer contributors; strong static checks exist | Medium |
| Flexibility | Several install options already supported | Low |
| Safety | No physical harm in scope | Low |

Functional suitability's Medium rating needs explaining, because correct numbers are central to a budgeting app. The repository already tests budget recomputation, category totals and the exclusion of off-budget spending (Actual Budget, 2026a), and the published advisories concern security rather than calculation errors. Calculation correctness therefore stays in the release baseline, and new effort goes elsewhere.

Security comes first. Actual stores budgets and, on the server, bank-sync tokens that sit outside end-to-end encryption (Actual Budget, n.d.-i). Reliability covers data integrity across devices, database migrations and recovery; a user who loses both the encryption password and every local copy cannot recover an encrypted budget (Actual Budget, n.d.-i). Interaction capability includes inclusivity and user assistance. Because Actual targets WCAG 2.1 AA (Actual Budget, 2026a), accessibility is already one of its own requirements.

## 3.3 Current QA Practices and Gaps

Actual already runs a lot of automated QA. Every pull request triggers linting, type checking, Vitest unit tests and a database migration check, and Playwright end-to-end and visual regression tests run on pull requests and in the merge queue (Actual Budget, 2026a, n.d.-j). CodeQL scans run on pull requests, on pushes and weekly (Actual Budget, 2026a). A release needs approval from at least two other maintainers and smoke tests of the Docker server and desktop app (Actual Budget, n.d.-c). A security policy offers private vulnerability reporting and coordinated disclosure (Actual Budget, n.d.-h).

Set against the three attributes, these practices leave four gaps. Each is a public-evidence finding (no evidence found in the repository, October 2026), and private practices may exist.

Security lacks proactive verification before release. Critical and high-severity access-control flaws in the sync server were published in 2026 (Actual Budget, 2026b, 2026d). GHSA-m2cq-xjgm-f668, published on 20 February 2026 and rated critical (CVSS 9.2), reported missing authentication on SimpleFIN and Pluggy AI bank-sync endpoints, although the GoCardless integration had that protection (Actual Budget, 2026c). An inconsistency between two similar integrations reached a release, and an authorisation test matrix is the kind of check that would catch it. The security policy also gives no response time, and its link to the current stable release returned HTTP 404 when checked (Actual Budget, n.d.-h).

Reliability has no coverage measurement. The sync-server test configuration disables coverage (Actual Budget, 2026a), yet the testing checklist asks for "appropriate test coverage" (Actual Budget, n.d.-j, Testing Checklist section) with nothing to measure it against.

For interaction capability, no automated accessibility testing was found despite the WCAG target (Actual Budget, 2026a). Finally, the process has no written QA plan: quality rules are spread across documentation, templates and CI files. Performance testing is also absent from CI, but its low priority keeps it out of scope.

## 3.4 Selecting Standards and Practices

Each candidate standard or framework was judged against Actual's volunteer, donation-funded context.

*Table 3.2. Standards and frameworks selected for Actual's QA process.*

| Standard / framework | Decision | Reason |
|---|---|---|
| ISO/IEC 25010:2023 | Adopt | Current quality model; frames 3.2 |
| IEEE 730-2026 | Adapt | Planning and control structure for a light QA plan |
| ISO 9001:2026 | Borrow principles | Certification needs an organisational management system Actual lacks |
| ISO/IEC 27001:2022 | Borrow principles | Risk-based thinking useful; ISMS certification disproportionate |
| CMMI V3.0 | Reject appraisal | Appraisal cost outweighs value for volunteers |
| OWASP ASVS 5.0.0 | Adopt selectively | Authentication, session and authorisation chapters match the advisories |
| WCAG 2.2 | Adopt (AA) | Current W3C Recommendation |
| OpenSSF Badge and Scorecard | Adopt | Lightweight, open-source-specific, largely automated |
| ISO/IEC/IEEE 29119-1:2022 | Reference only | Testing concepts; detailed testing belongs in Section 4 |

IEEE 730-2026, published in August 2026, supersedes the 2014 edition (Institute of Electrical and Electronics Engineers [IEEE], 2026). Only its scope was read, so Section 3.5 adapts its planning-and-control idea without claiming conformance. ISO 9001:2026 sets requirements for an organisation to show it consistently meets customer requirements (International Organization for Standardization, 2026), and ISO/IEC 27001:2022 covers establishing and improving an information security management system (International Organization for Standardization & International Electrotechnical Commission, 2022). Both assume a formal organisation, so only their customer focus and risk-based thinking transfer to Actual. CMMI V3.0 is the current model (Lear, 2023). A maturity appraisal would give Actual a rating without removing any defects. ISO/IEC/IEEE 29119-1:2022 supplies general testing concepts (International Organization for Standardization et al., 2022), which Section 4 applies.

OWASP ASVS 5.0.0 provides a basis for testing technical security controls (OWASP Foundation, 2025). Its authentication, session management and authorisation chapters match the pattern of the advisories. Selected requirements from those chapters, rather than a full verification level, would become acceptance criteria for sync-server work. WCAG 2.2 is recommended for new work, although W3C states that it does not deprecate 2.1 (World Wide Web Consortium, 2024), so moving the target to 2.2 AA is a modest step. The OpenSSF Best Practices Badge is a criteria-based self-assessment, and Scorecard runs automated checks for risky practices. No public result for Actual was found on 22 October 2026 (Open Source Security Foundation, n.d.-a, n.d.-b).

## 3.5 Applying the QA Process within Kanban

Kanban moves work between stages through explicit policies, the "entry" and "exit" criteria that decide when an item may be pulled (Ahmad et al., 2018, p. 98). Table 3.3 puts the QA plan on the board as a Definition of Done for each stage, instead of in a separate document contributors may never open.

*Table 3.3. Compact QA plan embedded in the Kanban stages.*

| Kanban stage | Definition of Done (exit policy) | Owner |
|---|---|---|
| Requirements/triage | Risk noted; security, data and accessibility acceptance criteria written | Triager |
| Design | Server-side changes list endpoints and permissions; migration and sync impact stated | Author, area owner |
| Build/PR | Existing CI green; new endpoints added to the authorisation test matrix; coverage report produced | Author |
| Verify | Reviewer checks ASVS-derived criteria and automated WCAG 2.2 AA checks; server tests use a separate server with synthetic data | Reviewer |
| Release train | Two approvals; smoke tests; no open critical or high finding | Release maintainers |
| Operate/maintain | Reports handled privately; escaped defects add a regression test and a policy review | Security contact |

The rest of the plan follows IEEE 730's concern with planning and control (IEEE, 2026). Each attribute gets one measure, to be defined in Assignment 2: endpoints covered by the authorisation matrix for security, test coverage of the core and sync-server packages for reliability, and automated accessibility violations on key screens for interaction capability. The security policy should add a response-time target and fix its broken link. Section 4 specifies the independent verification roles.

## 3.6 Critical Evaluation

The plan's main cost is volunteer time. Actual's USD 2,000 monthly stipend pool pays for review and triage work (Actual Budget, n.d.-f), and pull requests in the project have already waited months for review (Aboltins, 2025). Every new exit criterion adds load, and maintainer interviews identify administrative overhead as a burnout risk (Salkever, 2023). The gates are therefore scaled by risk (Section 4 proposes tiers), so a documentation change does not wait for an authorisation matrix.

Automation has its own costs. After adopting GitHub Actions, projects saw more rejected pull requests and longer acceptance times (Wessel et al., 2023), whereas code review bots were associated with more merged pull requests and less discussion (Wessel et al., 2022). These observational findings cannot predict Actual's results, but they suggest monitoring each tool's effect.

Even with these controls, automated accessibility checks cannot judge whether an envelope-budgeting task is understandable, so manual review is still needed. An OpenSSF badge is a self-assessment and gives no audit assurance. The standards were read only at scope level, and the gaps rest on public evidence only.

<!-- Cited: S01, S03, S08, S09, S10, S38, S43, S44, S47, S51, S53, S55, S57, S58, S59, S60-badge, S60-scorecard, S61, S62, S63-m2cq, S63-prp4, S63-cq9c, S82, S85 -->
