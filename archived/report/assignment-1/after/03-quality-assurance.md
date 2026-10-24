# 3 Quality Assurance Process

## 3.1 What quality means for Actual

Actual's product guidance identifies privacy-minded household budgeters, self-hosters and families as users, and regards confidence in the figures as a measure of success (Actual Budget, 2026a). Each group has requirements that automated tests alone cannot settle. Budgeters need dependable records and understandable controls. Self-hosters need clear security responsibilities, while maintainers need changes they can review and support. Even a technically correct implementation fails a user's needs when an inaccessible interaction prevents that person from reconciling an account.

Quality assurance should turn these expectations into requirements and establish how reviewers assess changes and support release decisions. Testing and inspection supply quality-control evidence, but a green pipeline cannot establish whether the project selected the right requirements. The proposed process starts by considering the consequences for stakeholders, then requires explicit acceptance criteria before implementation begins. This assessment draws on the October 2026 repository review at commit `27290a8` and the primary-source checks below. Its recommendations cover observable project practices. Maintainers' private activities have not been audited.

## 3.2 Selecting the quality attributes

ISO/IEC 25010:2023 defines a product quality model with nine characteristics (International Organization for Standardization [ISO] & International Electrotechnical Commission [IEC], 2023). The priorities in Table 4 indicate where Actual needs additional assurance effort. They are the analyst's judgements, not ratings supplied by ISO or measured scores of the product.

**Table 4. Priorities for additional quality assurance**

| Characteristic | Priority | Reason in Actual's context |
|---|---|---|
| Functional suitability | Medium | Calculations remain essential; budgeting tests already provide direct checks. |
| Performance efficiency | Medium | Slow imports could disrupt household budgeting. |
| Compatibility | Medium | Imports and bank integrations cross system boundaries. |
| Interaction capability | High | Users need accessible, understandable financial controls. |
| Reliability | High | Interrupted synchronisation and recovery can threaten retained records. |
| Security | High | Exposed financial data has demonstrated access-control risks. |
| Maintainability | Medium | Volunteers need changes that remain reviewable. |
| Flexibility | Medium | Deployment and device requirements vary. |
| Safety | Low | Direct physical hazards appear limited in household budgeting. |

Functional suitability remains a baseline requirement for release. Existing tests check budget recomputation and category totals, which justifies a lower priority for *additional* effort; these checks do not establish that calculations are defect-free (Actual Budget, 2026a).

Security needs the most attention because bank credentials and transaction histories require consistent access restrictions. Reliability covers continued operation and recovery after synchronisation or migration is interrupted. Interaction capability concerns users completing tasks without consequential mistakes; WCAG 2.2 addresses accessibility within this area (World Wide Web Consortium [W3C], 2024). Actual's encryption documentation shows how these concerns overlap. Encrypted data is unrecoverable if both the local copy and encryption password are lost, although a surviving local copy permits a key reset. End-to-end encryption also excludes bank-sync tokens held on the server and unencrypted local storage (Actual Budget, n.d.-i). Clear recovery explanations and protection beyond encrypted budget files are therefore necessary alongside encryption.

## 3.3 Existing practices and assurance gaps

Actual's testing guide describes Vitest, Playwright and visual regression testing. The reviewed workflows include type checking, linting, migration checks, CodeQL and dependency review. Release guidance also requires approval from two other maintainers and a manual smoke test (Actual Budget, n.d.-c, n.d.-j, 2026a). These checks provide different forms of evidence. Visual similarity, however, cannot demonstrate accessible interaction, and static analysis cannot establish every permission rule specific to the application.

The maintainers published GHSA-m2cq-xjgm-f668 on 20 February 2026 with a critical rating of 9.2. Missing authentication allowed access to bank balances and transactions through SimpleFIN and Pluggy.ai endpoints. The advisory identifies another integration that applied authentication middleware (Actual Budget, 2026c). The inconsistency supports checking permissions systematically across integrations. This historical failure does not establish that the patched release remains vulnerable.

In the October repository review, no comprehensive pre-release security verification programme, automated accessibility checks, coverage reporting or consolidated QA plan was documented. Those findings describe the available public evidence; activities may occur without being publicly documented. The sync-server configuration explicitly disables coverage, leaving no visible quantitative baseline behind the testing checklist's requirement for appropriate coverage (Actual Budget, n.d.-j, 2026a). The review also recorded a performance-testing gap outside the three selected priorities.

Actual's organisation-wide security policy provides private reporting and coordinated disclosure. Its stable-version link returned 404 when rechecked, and it gives no response deadline (Actual Budget, n.d.-h). The existing disclosure channel should remain, with stronger preventive verification and clearer operational guidance.

## 3.4 Selecting standards and practices

ISO/IEC 25010:2023 is adopted to structure requirements. IEEE 730-2026 is adapted to plan, control and execute assurance; its publisher confirms that it supersedes the 2014 edition (Institute of Electrical and Electronics Engineers [IEEE], 2026). Public scopes and previews were the only material available for these standards. The proposed process therefore supports alignment, without establishing formal conformity.

ISO 9001:2026 covers an organisation's quality management system, and ISO/IEC 27001:2022 covers its information security management system (ISO, 2026; ISO & IEC, 2022). Certification is rejected for this proposal because establishing those organisational systems and producing the evidence would divert volunteer capacity from the identified product gaps. Their principles of customer focus, improvement and risk management remain useful. CMMI V3.0 appraisal is also rejected: its broad remit for organisational improvement exceeds the needs of this targeted intervention (Lear, 2023).

Selected requirements from OWASP ASVS 5.0.0 are adopted. V6 Authentication, V7 Session Management and V8 Authorization cover relevant controls, including documented permissions and access restrictions enforced by the server (OWASP Foundation, 2025). An endpoint-and-role checklist should use these requirements. Adopting selected controls does not establish an ASVS verification level.

The proposed accessibility target is WCAG 2.2 AA. Actual specifies 2.1 AA; W3C recommends 2.2 for future applicability and retains 2.1 as a Recommendation (Actual Budget, 2026a; W3C, 2024). Keyboard and assistive-technology review should accompany automated checks.

OpenSSF's Best Practices Badge criteria are adopted to organise documented project evidence. Scorecard adds automated checks for risky repository practices (Open Source Security Foundation, n.d.-a, n.d.-b). Neither establishes application security. Public searches in October returned no badge entry or Scorecard result for Actual. That finding alone gives no basis for judging the product poor quality.

## 3.5 Applying a compact QA plan

For the Kanban flow selected in Section 2, Table 5 assigns assurance responsibilities and specifies the records and exit policies. These obligations are requirements of the proposed process. The plan uses IEEE's public scope as guidance; it does not reproduce the standard's prescribed contents (IEEE, 2026).

**Table 5. Proposed QA plan and workflow gates**

| Plan area and stage | Responsibility, required activity and exit evidence |
|---|---|
| Purpose and management: Backlog/triage | Maintainer identifies affected users, selected attributes and severity; names an available reviewer. |
| Requirements and documentation: Ready/design | Contributor records acceptance criteria, permission rules or recovery expectations and applicable ASVS/WCAG checks. |
| Methods and tools: Build/PR | Contributor retains existing CI, adds relevant regressions, and supplies synthetic data and reproducible checks. |
| Review and verification: Verify | Non-author reviewer confirms evidence. Security changes need denied-access checks; data changes need recovery checks; interface changes need automated and manual accessibility review. |
| Configuration and release: Release | Release lead retains approvals and smoke tests; records tested revision, upgrade guidance and unresolved findings. Release-blocking findings require correction. |
| Problem handling and records: Done/operate | Maintainer links ordinary defects to follow-up work; handles vulnerabilities privately, coordinates fixes and disclosure, and updates the policy's broken link. |

Under the proposed Definition of Done, applicable checks must pass and their evidence must be linked; exclusions need explicit reasons. Each attribute initially has one measure: selected access-control cases passed, changed critical-code branch coverage, and selected WCAG criteria passed. A baseline must precede any justified percentage target. Failed recovery, unauthorised access or an inaccessible core task should block the affected change. Section 4 develops the test design and independent challenge.

## 3.6 Critical evaluation

Authentication changes, migration paths and core budgeting interactions should receive attention first. Applying every check to every contribution would consume scarce review time. Coverage can also increase without demonstrating useful outcomes, so reviewers must examine the assertions, especially for interrupted or denied operations. Manual accessibility review requires skills that available volunteers cannot be assumed to possess.

Automation studies give different results. Wessel et al. (2023) associated GitHub Actions adoption with longer PR acceptance times. Wessel et al. (2022) found more monthly merged PRs after code-review bot adoption. The interventions differ, and neither study predicts Actual's results. These findings support piloting checks and investigating noisy failures before extending mandatory gates.

The plan can improve traceability and consistency without guaranteeing security or recoverability. Project controls cover only part of the risk from self-hosted configurations, external bank services and users' backup choices. A published checklist or badge can reveal missing practices, but review of the deployed system and independent testing of high-impact changes are still needed.
