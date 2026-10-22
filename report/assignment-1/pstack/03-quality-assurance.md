# 3 Quality Assurance Process

## 3.1 What quality means for Actual

Actual's product guidance identifies privacy-minded household budgeters, self-hosters and families as users. Confidence in the figures is a measure of success (Actual Budget, 2026a). Quality requires dependable records and understandable controls for users, clear security responsibilities for self-hosters, and reviewable, supportable changes for maintainers. Automated tests cannot establish all these qualities. An implementation can be technically correct yet prevent someone from reconciling an account because the interaction is inaccessible.

Quality assurance should connect these expectations to requirements, review decisions and release evidence. Testing and inspection supply quality-control evidence within that process. A passing pipeline cannot establish whether the project selected the right requirements. The proposed process begins with stakeholder consequences and requires explicit acceptance criteria before implementation. The assessment draws on the October 2026 repository review at commit `27290a8` and the primary-source checks described below. It assesses observable project practices. It does not audit maintainers' private activities.

## 3.2 Selecting the quality attributes

ISO/IEC 25010:2023 defines nine product quality characteristics (International Organization for Standardization [ISO] & International Electrotechnical Commission [IEC], 2023). Table 4 assigns priorities for additional assurance effort. The ratings express the analyst's judgement. They are neither ISO ratings nor measured scores for Actual.

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

Functional suitability remains a baseline release requirement. Existing tests cover budget recomputation and category totals, supporting a lower priority for *additional* effort. That judgement does not assume defect-free calculations (Actual Budget, 2026a).

Security needs the strongest attention because bank credentials and transaction histories require consistent access restrictions. Reliability concerns continued operation and recovery after interrupted synchronisation or migration. Interaction capability covers task completion and avoidance of consequential mistakes. WCAG 2.2 addresses accessibility within that priority (World Wide Web Consortium [W3C], 2024).

The attributes affect one another. Actual warns that encrypted data cannot be recovered if both the local copy and encryption password are lost. A surviving local copy allows a key reset. End-to-end encryption also excludes server-held bank-sync tokens and unencrypted local storage (Actual Budget, n.d.-i). Users therefore need clear recovery explanations and protection for data outside encrypted budget files.

## 3.3 Existing practices and assurance gaps

Actual already has substantial technical checks. Its testing guide describes Vitest, Playwright and visual regression testing. Reviewed workflows include type checking, linting, migration checks, CodeQL and dependency review. The release guide requires approval from two other maintainers and a manual smoke test (Actual Budget, n.d.-c, n.d.-j, 2026a). Each check provides different evidence. Visual similarity does not establish accessible interaction, while static analysis cannot verify every business-specific permission rule.

GHSA-m2cq-xjgm-f668 illustrates the security limitation. Published on 20 February 2026, it carries the maintainers' critical rating of 9.2. Missing authentication allowed access to bank balances and transactions through SimpleFIN and Pluggy.ai endpoints. The advisory contrasts those endpoints with an integration that used authentication middleware (Actual Budget, 2026c). This failure supports systematic permission checks across integrations. It does not establish that the patched release remains vulnerable.

The October repository review found no documented comprehensive pre-release security verification programme, automated accessibility checks, coverage reporting or consolidated QA plan. These findings describe the limits of public evidence. They cannot establish that the activities never occur. The sync-server configuration explicitly disables coverage. The testing checklist requires appropriate coverage, but no quantitative baseline was visible (Actual Budget, n.d.-j, 2026a). The review also recorded a performance-testing gap outside the three selected priorities.

Actual publishes an organisation-wide security policy for private reporting and coordinated disclosure. On rechecking, its stable-version link returned 404. The policy also gives no response deadline (Actual Budget, n.d.-h). The proposal retains this disclosure channel and strengthens preventive verification and operational guidance.

## 3.4 Selecting standards and practices

The proposal selects engineering guidance separately from organisational certification. ISO/IEC 25010:2023 structures requirements. IEEE 730-2026 guides planning, control and execution of assurance. Its publisher confirms that the 2026 edition supersedes the 2014 edition (Institute of Electrical and Electronics Engineers [IEEE], 2026). Access was limited to public scopes and previews, so the proposal seeks alignment and cannot claim formal conformity.

ISO 9001:2026 addresses organisational quality management systems. ISO/IEC 27001:2022 addresses information security management systems (ISO, 2026; ISO & IEC, 2022). Certification is rejected for this proposal because establishing and evidencing those systems would divert volunteer capacity from the identified product gaps. Their principles of customer focus, improvement and risk management remain useful. CMMI V3.0 appraisal is also rejected. Its broad organisational improvement remit exceeds this targeted intervention (Lear, 2023).

The proposal adopts selected OWASP ASVS 5.0.0 requirements. V6 Authentication, V7 Session Management and V8 Authorization cover relevant controls, including documented permissions and server-enforced access restrictions (OWASP Foundation, 2025). An endpoint-and-role checklist should use these requirements. The proposal claims no ASVS verification level.

WCAG 2.2 AA is the proposed accessibility target. Actual specifies 2.1 AA. W3C recommends 2.2 for future applicability and retains 2.1 as a Recommendation (Actual Budget, 2026a; W3C, 2024). Automated checks need support from keyboard and assistive-technology review.

OpenSSF's Best Practices Badge criteria and Scorecard provide supporting project checks. The badge criteria organise documented evidence. Scorecard automates checks for risky repository practices (Open Source Security Foundation, n.d.-a, n.d.-b). Neither establishes application security. October public searches found no badge entry or Scorecard result for Actual. That limited finding does not establish poor quality.

## 3.5 Applying a compact QA plan

Table 5 assigns responsibilities, records and exit policies to the Kanban flow selected in Section 2. The assurance obligations are required by the proposed process. This lightweight plan uses IEEE's public scope as guidance without reproducing its prescribed contents (IEEE, 2026).

**Table 5. Proposed QA plan and workflow gates**

| Plan area and stage | Responsibility, required activity and exit evidence |
|---|---|
| Purpose and management: Backlog/triage | Maintainer identifies affected users, selected attributes and severity; names an available reviewer. |
| Requirements and documentation: Ready/design | Contributor records acceptance criteria, permission rules or recovery expectations and applicable ASVS/WCAG checks. |
| Methods and tools: Build/PR | Contributor retains existing CI, adds relevant regressions, and supplies synthetic data and reproducible checks. |
| Review and verification: Verify | Non-author reviewer confirms evidence. Security changes need denied-access checks; data changes need recovery checks; interface changes need automated and manual accessibility review. |
| Configuration and release: Release | Release lead retains approvals and smoke tests; records tested revision, upgrade guidance and unresolved findings. Release-blocking findings require correction. |
| Problem handling and records: Done/operate | Maintainer links ordinary defects to follow-up work; handles vulnerabilities privately, coordinates fixes and disclosure, and updates the policy's broken link. |

The proposed Definition of Done requires applicable checks to pass, linked evidence and explicit reasons for exclusions. Each attribute initially needs one measure. These are selected access-control cases passed, changed critical-code branch coverage and selected WCAG criteria passed. A percentage target would be unjustified without a baseline. Failed recovery, unauthorised access or an inaccessible core task should block the affected change. Section 4 develops detailed test design and independent challenge.

## 3.6 Critical evaluation

Implementation should begin with authentication changes, migration paths and core budgeting interactions. Applying every check to every contribution would consume scarce review time. Coverage can also rise without useful outcome checks. Reviewers need to examine what assertions demonstrate, especially when operations are interrupted or denied. Manual accessibility review requires skills that available volunteers may lack.

Research gives mixed evidence about automation. Wessel et al. (2023) associate GitHub Actions adoption with longer PR acceptance times. Wessel et al. (2022) find increased monthly merged PRs after adoption of code-review bots. The studies examine different interventions and cannot predict Actual's results. They support piloting checks and investigating noisy failures before expanding mandatory gates.

The plan can improve traceability and consistency. It cannot guarantee security or recoverability. Project controls cannot fully govern self-hosted configurations, external bank services or users' backup choices. A published checklist or badge can reveal missing practices. Review of the deployed system and independent tests of high-impact changes remain necessary.
