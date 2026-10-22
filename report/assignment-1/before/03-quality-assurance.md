# 3 Quality Assurance Process

## 3.1 What quality means for Actual

Actual's product guidance identifies privacy-minded household budgeters, self-hosters and families as users, and treats confidence in the figures as a measure of success (Actual Budget, 2026a). Quality therefore involves more than passing automated tests. Users need dependable records and understandable controls; self-hosters need clear security responsibilities; maintainers need changes they can review and support. A technically correct implementation can still fail these needs if an inaccessible interaction prevents someone from reconciling an account.

Quality assurance should establish how these expectations become requirements, review decisions and release evidence. Testing and inspection provide quality-control evidence within that process. A green pipeline alone cannot show whether the right requirements were selected. The proposed process therefore starts with stakeholder consequences and requires explicit acceptance criteria before implementation. The assessment uses the October 2026 repository review at commit `27290a8`, supplemented by the primary-source checks described below. Its recommendations concern observable project practices; they do not constitute an audit of maintainers' private activities.

## 3.2 Selecting the quality attributes

ISO/IEC 25010:2023 supplies a nine-characteristic product quality model (International Organization for Standardization [ISO] & International Electrotechnical Commission [IEC], 2023). Table 4 prioritises additional assurance effort for Actual; the ratings are the analyst's judgement, rather than ISO ratings or measured product scores.

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

Functional suitability remains a baseline release requirement. Its lower priority for *additional* effort reflects existing tests of budget recomputation and category totals, rather than an assumption that calculations are defect-free (Actual Budget, 2026a).

Security deserves the strongest attention: bank credentials and transaction histories require consistent access restrictions. Reliability concerns continued operation and recovery after interrupted synchronisation or migration. Interaction capability includes users completing tasks and avoiding consequential mistakes, with accessibility addressed through WCAG 2.2 (World Wide Web Consortium [W3C], 2024). These attributes interact. Actual's documentation warns that encrypted data cannot be recovered when both the local copy and encryption password are lost; a surviving local copy permits a key reset. It also states that end-to-end encryption excludes server-held bank-sync tokens and unencrypted local storage (Actual Budget, n.d.-i). Encryption therefore increases the need for clear recovery explanations and protection beyond encrypted budget files.

## 3.3 Existing practices and assurance gaps

Actual has a substantial technical foundation. Its testing guide describes Vitest, Playwright and visual regression testing. The reviewed workflows add type checking, linting, migration checks, CodeQL and dependency review; the release guide requires two other maintainers' approval and a manual smoke test (Actual Budget, n.d.-c, n.d.-j, 2026a). These practices offer complementary evidence, although visual similarity does not demonstrate accessible interaction, and static analysis cannot establish every business-specific permission rule.

A concrete security failure illustrates the limitation. GHSA-m2cq-xjgm-f668, published on 20 February 2026, carries the maintainers' critical rating of 9.2. Missing authentication allowed access to bank balances and transactions through SimpleFIN and Pluggy.ai endpoints; the advisory contrasts these with an integration that applied authentication middleware (Actual Budget, 2026c). This supports systematic cross-integration permission checks. It does not demonstrate that the patched release remains vulnerable.

The October repository review found no documented comprehensive pre-release security verification programme, automated accessibility checks, coverage reporting or consolidated QA plan. These are limits of public evidence, not proof that no such activity occurs. The sync-server configuration explicitly disables coverage; consequently, the testing checklist's requirement for appropriate coverage lacks a visible quantitative baseline (Actual Budget, n.d.-j, 2026a). A performance-testing gap was also recorded, outside the three selected priorities.

Actual does publish an organisation-wide security policy with private reporting and coordinated disclosure. Its stable-version link returned 404 when rechecked, and the policy states no response deadline (Actual Budget, n.d.-h). The recommendation is therefore to strengthen preventive verification and operational guidance, while retaining the existing disclosure channel.

## 3.4 Selecting standards and practices

The selection separates useful engineering guidance from organisational certification. ISO/IEC 25010:2023 is adopted to structure requirements. IEEE 730-2026 is adapted for planning, controlling and executing assurance; the publisher confirms that it supersedes the 2014 edition (Institute of Electrical and Electronics Engineers [IEEE], 2026). Only public scopes and previews were available for these standards, so this report proposes alignment rather than formal conformity.

ISO 9001:2026 addresses an organisation's quality management system, while ISO/IEC 27001:2022 addresses its information security management system (ISO, 2026; ISO & IEC, 2022). Certification is rejected for the present proposal: establishing and evidencing those organisational systems would divert volunteer capacity from the identified product gaps. Their customer-focus, improvement and risk-management principles remain useful. CMMI V3.0 appraisal is similarly rejected; its broad organisational improvement remit exceeds this targeted intervention (Lear, 2023).

OWASP ASVS 5.0.0 is adopted selectively. V6 Authentication, V7 Session Management and V8 Authorization provide relevant requirements, including documented permissions and server-enforced access restrictions (OWASP Foundation, 2025). These should inform an endpoint-and-role checklist, without claiming an ASVS verification level.

WCAG 2.2 AA is adopted as the proposed accessibility target. Actual specifies 2.1 AA; W3C recommends 2.2 for future applicability while retaining 2.1 as a Recommendation (Actual Budget, 2026a; W3C, 2024). Automated checks should accompany keyboard and assistive-technology review.

OpenSSF's Best Practices Badge criteria and Scorecard are adopted as supporting project checks: the former organises documented evidence; the latter automates checks for risky repository practices (Open Source Security Foundation, n.d.-a, n.d.-b). Neither establishes application security. The October public searches returned no badge entry or Scorecard result for Actual; this limited finding does not imply poor quality.

## 3.5 Applying a compact QA plan

Table 5 translates the assurance scope into responsibilities, records and exit policies for the Kanban flow selected in Section 2. These assurance obligations are requirements of the proposed process. This lightweight plan draws on IEEE's public scope without reproducing its prescribed contents (IEEE, 2026).

**Table 5. Proposed QA plan and workflow gates**

| Plan area and stage | Responsibility, required activity and exit evidence |
|---|---|
| Purpose and management: Backlog/triage | Maintainer identifies affected users, selected attributes and severity; names an available reviewer. |
| Requirements and documentation: Ready/design | Contributor records acceptance criteria, permission rules or recovery expectations and applicable ASVS/WCAG checks. |
| Methods and tools: Build/PR | Contributor retains existing CI, adds relevant regressions, and supplies synthetic data and reproducible checks. |
| Review and verification: Verify | Non-author reviewer confirms evidence. Security changes need denied-access checks; data changes need recovery checks; interface changes need automated and manual accessibility review. |
| Configuration and release: Release | Release lead retains approvals and smoke tests; records tested revision, upgrade guidance and unresolved findings. Release-blocking findings require correction. |
| Problem handling and records: Done/operate | Maintainer links ordinary defects to follow-up work; handles vulnerabilities privately, coordinates fixes and disclosure, and updates the policy's broken link. |

The proposed Definition of Done requires applicable checks to pass and evidence to be linked, with explicit reasons for exclusions. Initially, each attribute needs one measure: selected access-control cases passed, changed critical-code branch coverage, and selected WCAG criteria passed. No percentage target is justified before establishing a baseline. Failed recovery, unauthorised access or an inaccessible core task should block the affected change. Detailed test design and independent challenge belong in Section 4.

## 3.6 Critical evaluation

Implementation should begin with authentication changes, migration paths and core budgeting interactions. Extending every check to every contribution would consume scarce review time, and coverage can rise without testing useful outcomes. Reviewers must inspect what assertions demonstrate, particularly under interrupted or denied operations. Manual accessibility work also depends on skills that cannot be assumed to exist among available volunteers.

Evidence on automation is mixed. Wessel et al. (2023) associated GitHub Actions adoption with longer PR acceptance times, whereas Wessel et al. (2022) found increased monthly merged PRs after code-review bot adoption. These studies concern different interventions and do not predict Actual's results. They justify piloting checks and investigating noisy failures before expanding mandatory gates.

The plan can improve traceability and consistency, but cannot guarantee security or recoverability. Self-hosted configurations, external bank services and users' backup choices remain partly outside project control. A published checklist or badge may expose missing practices; neither replaces review of the deployed system or independent testing of high-impact changes.
