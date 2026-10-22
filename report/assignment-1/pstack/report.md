# Software Quality Engineering Evaluation of Actual Budget

Assignment 1

## Contents

- [Executive summary](#executive-summary)
- [1 Introduction](#1-introduction)
- [2 Software Development Methodology](#2-software-development-methodology)
- [3 Quality Assurance Process](#3-quality-assurance-process)
- [4 Integrating IV&V with Kanban](#4-integrating-ivv-with-kanban)
- [References](#references)

## List of figures

1. Actual Budget's local-first operation, Section 1.3.
2. Actual's current development workflow, Section 2.1.
3. Proposed Kanban workflow for Actual, Section 2.5.

## List of tables

1. Stakeholders and quality expectations, Section 1.4.
2. Methodology selection criteria and importance, Section 2.2.
3. Weighted methodology comparison, Section 2.4.
4. Priorities for additional quality assurance, Section 3.2.
5. Proposed QA plan and workflow gates, Section 3.5.
6. Current checking arrangements and evidential limits, Section 4.2.
7. Proposed V&V activities and movement conditions, Section 4.4.

---

# Executive summary

Actual Budget is a local-first personal finance application maintained by open-source contributors (Actual Budget, 2026a). This report assesses its development process and proposes quality assurance and independent verification and validation arrangements that account for volunteer participation.

The methodology comparison selects Kanban, which receives 102 of 120 weighted points, followed by DevOps with 94. The existing open-source workflow receives 95 as a non-selectable baseline. These scores express judgements about project fit. They do not measure software quality. Kanban can help manage review queues, accommodate voluntary work and establish explicit policies with little ceremony. It still needs engineering assurance practices.

Security, reliability and interaction capability are mandatory quality priorities in the proposal. Existing tests and CI remain, supported by targeted access-control verification, recovery evidence and accessibility checks. A compact QA plan assigns responsibilities and requires unresolved material failures to block progress. Standards guide these recommendations without establishing certification or formal conformity.

Independent assessment accompanies the workflow through non-author review, proportionate risk tiers and recorded acceptance evidence. Internal review offers limited independence, supplemented by external vulnerability reporting and optional funded audits. Adoption depends on gradual introduction, available reviewers and continuing evaluation. The report proposes these changes for assessment. It does not claim that Actual has implemented them or demonstrated a lower defect rate.

---

# 1 Introduction

## 1.1 Background and purpose

Personal finance applications help people record income, track spending and plan how to use their money. Incorrect balances or lost records can affect everyday decisions. Exposed transactions can also reveal private information. Actual Budget's product statement identifies trust in the numbers and prompt completion of routine tasks as measures of success (Actual Budget, 2026a).

I chose Actual Budget while looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. After finding it, I wanted to examine the product more closely through this assignment.

This report evaluates a development methodology, proposes a quality assurance process and integrates independent verification and validation into the selected methodology. The recommendations draw on external analysis of public evidence. The analysis involved no contact with Actual's team.

## 1.2 What is Actual Budget?

Actual Budget is a free, open-source personal finance application distributed under the MIT licence. Its local-first design lets users work with data on their own devices and optionally synchronise through a server. The default envelope-budgeting approach assigns money already available to spending categories (Actual Budget, n.d.-k, 2026a).

James Long developed Actual as a commercial product. In early 2022, he closed the commercial service and made the software open source. A volunteer maintainer team then took responsibility for development (Aboltins, 2025).

## 1.3 Main features and operation

Actual provides budgets, account registers, transaction rules, scheduled transactions and reports (Actual Budget, n.d.-k). Desktop applications support local use. Server deployment options include Docker, PikaPods and Fly.io. The server supports synchronisation between devices and connections to bank-sync providers (Actual Budget, n.d.-d). Figure 1 shows how these optional connections relate to everyday local budgeting.

**Figure 1. Actual Budget's local-first operation**

```text
Device: local budget and application
                 ↕ optional synchronisation
User-selected server: self-hosted or hosted
                 ↕ optional bank synchronisation
Bank-sync provider
```

*Note.* Author's synthesis of Actual's installation and synchronisation documentation (Actual Budget, n.d.-d, n.d.-i). Local desktop budgeting needs no server. The connected features shown require one.

Optional end-to-end encryption protects synchronised budget data. Local device storage and bank-sync tokens held separately on the server remain outside that protection. Self-hosting gives users control over deployment, while responsibility for protecting devices and credentials remains with them (Actual Budget, n.d.-i).

## 1.4 Who is involved?

**Table 1. Stakeholders and quality expectations**

| Stakeholder | Main interest |
|---|---|
| Users and households | Correct figures, privacy and clear daily tasks |
| Self-hosters | Safe upgrades, recoverable data and manageable servers |
| Eight listed core maintainers | Review capacity and sustainable workloads |
| Contributors | Clear expectations and useful feedback |
| Donors and hosting partners | Continued maintenance and dependable operation |

*Note.* Based on Actual's product statement, contributor guide and funding discussion (Actual Budget, n.d.-a, 2026a; youngcw, 2025). The December 2025 roadmap reported over 8,000 PikaPods users. Their hosting fees partly supported the project. That user count is historical.

## 1.5 Main challenges

- Volunteer availability and community requests constrain review capacity. Section 2 examines the implications for development (Aboltins, 2025).
- Financial correctness, data protection and accessible interactions need explicit quality priorities. Section 3 sets out those priorities (Actual Budget, n.d.-i, 2026a).
- Encryption leaves some data outside its protection. Section 4 proposes independent checks of security and recovery behaviour within the development workflow (Actual Budget, n.d.-i).

---

# 2 Software Development Methodology

## 2.1 Current development process

Actual has a defined workflow. The reviewed documentation does not identify a deliberate methodology. Contributors choose how to participate and review community contributions (Actual Budget, n.d.-e). Feature requests enter a voting-based backlog. Larger proposals should be discussed before implementation, while small changes can proceed directly to a pull request (PR) (Actual Budget, n.d.-a, 2026a).

Automated builds, checks and tests support PR review, as Figure 2 shows. Passing these checks alone cannot establish whether a change meets users' needs (Actual Budget, 2026a).

*Figure 2. Actual's current development workflow.*

```text
Community request/votes → Discussion → Contributor PR
                                          ↓
                                CI checks ↔ Review/rework
                                          ↓
                                        Merge
                                          ↓
                         Monthly cut: 25th, 17:00 UTC
                                          ↓
                      Release approval → Build/tag/publish
                                          ↓
                         Smoke tests → Final announcement
```

*Source: Adapted from Actual Budget (n.d.-c, 2026a). Small changes may bypass a separate discussion.*

Monthly releases require approval from at least two other maintainers and smoke tests of the server and desktop application (Actual Budget, n.d.-c). Feature flags allow incremental delivery and feedback before a feature becomes stable (Actual Budget, n.d.-b). The proposed process retains these engineering practices.

Review capacity warrants attention. Aboltins (2025) reports that PRs waited months during the early community transition. The current USD 2,000 monthly administrative stipend recognises review and triage work (Actual Budget, n.d.-f). The historical delays establish a coordination risk. They do not prove that a backlog persists today.

## 2.2 Project characteristics and selection criteria

Table 2 converts Actual's goals, constraints, risks and stakeholder expectations into ten selection criteria. Salkever's (2023) maintainer study supports attention to review demands and burnout. Methodology selection requires several criteria. This report uses a weighted sum, a simpler approach than Song et al.'s (2024) specialised model.

*Table 2. Methodology selection criteria and importance.*

| Criterion | Need | Weight |
|---|---|---:|
| C1 | Evolving, community-voted requirements | 3 |
| C2 | Voluntary, part-time participation | 3 |
| C3 | Distributed, asynchronous collaboration | 2 |
| C4 | Defect prevention and data integrity | 3 |
| C5 | Explicit risk management | 2 |
| C6 | Predictable, frequent delivery | 2 |
| C7 | Low overhead and ceremony | 3 |
| C8 | Flow and bottleneck management | 2 |
| C9 | Community involvement and feedback | 2 |
| C10 | Evidence transferable to comparable projects | 2 |

Weights range from 1 for low importance to 3 for high importance. Regulatory certification receives no separate score for this budgeting application, although security and privacy remain relevant. C2 assesses volunteer feasibility, C7 administration and C8 queues. These constraints partly overlap.

## 2.3 Candidate methodologies

Screening favoured established approaches with documented application evidence. Waterfall and the V-model offer limited flexibility as complete processes for community-led work. RUP and scaled frameworks require disproportionate coordination. Kanban represents Lean in the shortlist. Scrumban was omitted because its two parent approaches are already shortlisted. The planning search found insufficient independent research evidence for Shape Up, so it was excluded. This limitation concerns the search and does not establish that Shape Up fails.

- Spiral uses repeated, risk-driven evaluation. Boehm (1988) documents its use at TRW and its dependence on risk-assessment expertise.
- Scrum organises inspection and adaptation through Sprints, defined accountabilities and events. Shared planning and delivery depend on reliable capacity (Schwaber & Sutherland, 2020).
- Extreme Programming (XP) connects close collaboration with testing and frequent integration. Its creators allow adaptation and remote pairing. Coordinating intermittent contributors remains a concern (Beck & Andres, 2005).
- Kanban visualises work, controls work in progress (WIP) and manages flow. As a management method applied to an existing process, it would organise Actual's workflow and retain the engineering practices already used (Kanban University, n.d.).
- DevOps emphasises development and operational capabilities. Literature documents practice adoption alongside inconsistent definitions. Automation alone provides limited guidance for setting community priorities (Amaro et al., 2023).

The OSS/Bazaar model supplies a non-selectable baseline for distributed contribution and community feedback (Raymond, 2000). Actual's monthly release schedule remains a practice within the process. It is not a sixth candidate methodology.

## 2.4 Evaluation and selection

Table 3 scores each methodology's support for Actual's needs. The scores are analyst judgements and do not measure software quality. Each option retains existing CI and tests and must satisfy a mandatory QA gate. That gate requires relevant security, reliability and interaction checks, assigned responsibility and evidence that can block release, as Section 3 explains.

*Table 3. Weighted methodology comparison (1 = poor fit; 5 = strong fit).*

| Option | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Weight | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | /120 |
| Spiral | 4 | 2 | 3 | 4 | 5 | 3 | 2 | 2 | 3 | 2 | 72 |
| Scrum | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 81 |
| XP | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 82 |
| Kanban | 5 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 4 | 3 | 102 |
| DevOps | 4 | 4 | 5 | 4 | 3 | 5 | 4 | 3 | 3 | 4 | 94 |
| OSS baseline | 5 | 5 | 5 | 3 | 2 | 3 | 4 | 2 | 5 | 5 | 95 |

Total = sum(weight × score), with weights totalling 24. The baseline cannot be selected. Kanban leads because volunteer fit, low ceremony and queue management outweigh XP and DevOps' stronger engineering support. Kanban's C4=3 acknowledges that flow controls do not prescribe technical verification. DevOps' C7=4 recognises Actual's existing pipeline investment. The cost of Spiral's risk expertise reduces its fit for volunteers.

Equal weights still favour Kanban, with 42/50 compared with DevOps' 39. Giving quality the greatest weight could reverse the ranking. The recommendation therefore depends on the stated constraints and does not establish universal superiority.

Kanban's seven-point lead over the existing workflow is modest. A lower assessment of volunteer fit or adoption overhead could remove the advantage. Adoption needs to improve the baseline through visible review capacity, agreed movement conditions and acceptance evidence. Renaming the issue list would achieve little. XP and DevOps provide stronger engineering guidance, but both still need identified people to maintain checks and act on findings before release. The mandatory QA gate prevents high scores elsewhere from compensating for omitted essential assurance checks.

## 2.5 Applying Kanban to Actual

The proposed board in Figure 3 would show work and waiting. Kanban's explicit policies define the conditions for moving an item between stages. The method also supports WIP control and feedback (Kanban University, n.d.).

*Figure 3. Proposed Kanban workflow for Actual.*

```text
Backlog/triage → Ready/design → Build/PR → Verify → Release → Done
      ↑                            ↖ rework ↙                  │
      └──────── Operate/maintain: defects and feedback ────────┘

Pull work only when capacity and the preceding exit criteria permit.
Review/Verify WIP is constrained by available reviewer capacity.
```

Community input would remain part of requests. Maintainers would assess product fit and risk before work enters Ready. Each card would link the request, acceptance criteria, PR and test evidence. Contributors could choose work without Sprint commitments. Build/PR would retain existing CI and tests. Verify would require a reviewer and proportionate acceptance evidence. Section 4 develops the independent checks within this flow.

Maintainers would jointly set initial WIP limits according to review capacity, then revise the limits after observing queues. Blocked items would remain visible and count towards WIP. A weekly asynchronous review would examine ageing cards. A monthly flow review would accompany the existing release cycle. These proposed cadences provide feedback without mandatory daily meetings. Completed checks would determine release readiness. Urgent security fixes would receive expedited review while retaining all required checks.

## 2.6 Critical evaluation

Kanban addresses visibility and review queues, but a board cannot supply additional reviewers. When volunteers leave, lower WIP may reduce overload and throughput together. Limits need agreement and adjustment. Imposing limits without consultation could discourage occasional contributors. Ageing work warrants discussion, subdivision or withdrawal. It should not create pressure to approve unfinished work.

Ahmad et al. (2018) identify benefits alongside difficulties with implementation, training and supporting practices. Their mapping study also finds a largely descriptive evidence base, which limits causal claims about improvement. Adoption should therefore test observable queue behaviour. A reduction in defects cannot be promised. Kanban's flow controls need the security, reliability and accessibility practices developed in Section 3.

The matrix rewards related volunteer constraints through C2, C7 and C8. Their combined weight can favour Kanban more strongly than separate scores might suggest. The ranking supports a reasoned recommendation, but cannot predict the size of a quality improvement.

Kuhrmann et al. (2022) find that concrete practices matter more to agility than method labels. Retaining Actual's engineering controls is defensible tailoring. Those existing controls cannot be credited as new benefits of Kanban. Community votes also require product and risk judgement. Popular features should not automatically take priority over security maintenance.

A stable staffed team, binding delivery commitments or changed governance obligations would warrant reassessment. Stronger Sprint coordination or operational investment might then matter more than minimal ceremony. The present recommendation depends on the volunteer constraints used in this assessment.

---

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

---

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

---

# References

Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025/

Actual Budget. (n.d.-a). *Contributing to Actual Budget*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/

Actual Budget. (n.d.-b). *Feature flags (experimental features)*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/project-details/feature-flags/

Actual Budget. (n.d.-c). *How to cut a release*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/releasing/

Actual Budget. (n.d.-d). *Installing Actual*. Retrieved October 22, 2026, from https://actualbudget.org/docs/install/

Actual Budget. (n.d.-e). *New core contributors guide*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide/

Actual Budget. (n.d.-f). *Paying reviewers for administrative work*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors/

Actual Budget. (n.d.-g). *Preview builds*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/preview-builds/

Actual Budget. (n.d.-h). *Security policy* [SECURITY.md]. GitHub. Retrieved October 22, 2026, from https://github.com/actualbudget/.github/blob/main/SECURITY.md

Actual Budget. (n.d.-i). *Syncing across devices*. Retrieved October 22, 2026, from https://actualbudget.org/docs/getting-started/sync/

Actual Budget. (n.d.-j). *Testing*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/testing/

Actual Budget. (n.d.-k). *A tour of Actual*. Retrieved October 22, 2026, from https://actualbudget.org/docs/tour/

Actual Budget. (2026a). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual

Actual Budget. (2026b, June 12). *Disabled OpenID users keep access through existing session tokens* (GHSA-cq9c-6w48-qmfg) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-cq9c-6w48-qmfg

Actual Budget. (2026c, February 20). *Missing authentication for SimpleFIN and Pluggy AI bank sync endpoints* (GHSA-m2cq-xjgm-f668) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-m2cq-xjgm-f668

Actual Budget. (2026d, April 23). *Privilege escalation via 'change-password' endpoint on OpenID-migrated servers* (GHSA-prp4-2f49-fcgp) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-prp4-2f49-fcgp

Ahmad, M. O., Dennehy, D., Conboy, K., & Oivo, M. (2018). Kanban in software engineering: A systematic mapping study. *Journal of Systems and Software, 137*, 96–113. https://doi.org/10.1016/j.jss.2017.11.045

Amaro, R., Pereira, R., & da Silva, M. M. (2023). Capabilities and practices in DevOps: A multivocal literature review. *IEEE Transactions on Software Engineering, 49*(2), 883–901. https://doi.org/10.1109/TSE.2022.3166626

Beck, K., & Andres, C. (2005, June 10). *Getting started with eXtreme Programming: Toe dipping, racing dives, and cannonballs: Appendix: Primary practices*. InformIT. https://www.informit.com/articles/article.aspx?p=390816&seqNum=3

Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer, 21*(5), 61–72. https://doi.org/10.1109/2.59

Institute of Electrical and Electronics Engineers. (2025). *IEEE standard for system, software, and hardware verification and validation* (IEEE Std 1012-2024). https://standards.ieee.org/ieee/1800.2/7324/

Institute of Electrical and Electronics Engineers. (2026). *IEEE standard for software quality assurance processes* (IEEE Std 730-2026). https://standards.ieee.org/ieee/730/10854/

International Organization for Standardization. (2026). *Quality management systems — Requirements* (ISO Standard No. 9001:2026). https://www.evs.ee/en/iso-9001-2026

International Organization for Standardization & International Electrotechnical Commission. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC Standard No. 27001:2022). https://www.iso.org/standard/27001

International Organization for Standardization & International Electrotechnical Commission. (2023). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (ISO/IEC Standard No. 25010:2023). https://www.iso.org/standard/78176.html

Kanban University. (n.d.). *The official guide to the Kanban method*. Retrieved October 22, 2026, from https://kanban.university/kanban-guide/

Kuhrmann, M., Tell, P., Hebig, R., Klünder, J., Münch, J., Linssen, O., Pfahl, D., Felderer, M., Prause, C. R., MacDonell, S. G., Nakatumba-Nabende, J., Raffo, D., Beecham, S., Tüzün, E., López, G., Paez, N., Fontdevila, D., Licorish, S. A., Küpper, S., … Richardson, I. (2022). What makes agile software development agile? *IEEE Transactions on Software Engineering, 48*(9), 3523–3539. https://doi.org/10.1109/TSE.2021.3099532

Lear, R. (2023, April 10). *CMMI updates take performance improvements to the next level*. ISACA. https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2023/cmmi-updates-take-performance-improvements-to-the-next-level

Liu, S., Zhou, J., Hu, X., Cogo, F. R., Xia, X., & Yang, X. (2025). An empirical study on vulnerability disclosure management of open source software systems. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3716822

National Aeronautics and Space Administration. (n.d.). *IV&V overview*. Retrieved October 22, 2026, from https://www.nasa.gov/ivv-overview/

Open Source Security Foundation. (n.d.-a). *FLOSS best practices criteria (passing badge)*. Retrieved October 22, 2026, from https://www.bestpractices.dev/en/criteria/0

Open Source Security Foundation. (n.d.-b). *OpenSSF Scorecard*. Retrieved October 22, 2026, from https://scorecard.dev/

Open Source Technology Improvement Fund. (2026, January 30). *2025 annual report*. https://ostif.org/2025-annual-report/

OWASP Foundation. (2025). *OWASP application security verification standard* (Version 5.0.0). https://github.com/OWASP/ASVS/tree/v5.0.0

Raymond, E. S. (2000). *The cathedral and the bazaar* (Version 3.0). https://web.stanford.edu/class/me228/pdf/cathedral-bazaar.pdf

Salkever, A. (2023). *Open source maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects*. The Linux Foundation. https://doi.org/10.70828/lddj8886

Schwaber, K., & Sutherland, J. (2020). *The Scrum guide*. https://scrumguides.org/scrum-guide.html

Smith, J., & Hayes, W. (2024). Independent verification & validation (IV&V) for agile developed projects. In *2024 IEEE Aerospace Conference* (pp. 1–10). IEEE. https://doi.org/10.1109/AERO58975.2024.10521415

Song, Y., Mahmood, T., & Rehman, U. U. (2024). Selection of software development methodology by employing a multi-criteria decision-making approach based on logarithmic bipolar complex fuzzy aggregation operators. *IEEE Access, 12*, 38163–38179. https://doi.org/10.1109/ACCESS.2024.3373708

Wessel, M., Serebrenik, A., Wiese, I., Steinmacher, I., & Gerosa, M. A. (2022). Quality gatekeepers: Investigating the effects of code review bots on pull request activities. *Empirical Software Engineering, 27*, Article 108. https://doi.org/10.1007/s10664-022-10130-9

Wessel, M., Vargovich, J., Gerosa, M. A., & Treude, C. (2023). GitHub Actions: The impact on the pull request process. *Empirical Software Engineering, 28*, Article 131. https://doi.org/10.1007/s10664-023-10369-w

World Wide Web Consortium. (2024, December 12). *Web content accessibility guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/

youngcw. (2025, December 20). *Roadmap for 2026*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2026/
