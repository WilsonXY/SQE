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

Actual Budget is a local-first personal finance application maintained by open-source contributors (Actual Budget, 2026a). This report assesses its development process and proposes quality assurance and independent verification and validation arrangements that volunteers could sustain.

Kanban ranks first in the methodology comparison, scoring 102 of 120 weighted points against DevOps' 94. The existing open-source workflow scores 95 as a non-selectable baseline. These scores express judgements about project fit. They do not measure the quality of Actual's software. Kanban suits voluntary participation and helps manage review queues through explicit policies and limited ceremony. The method still needs engineering assurance practices.

The proposal makes security, reliability and interaction capability mandatory quality priorities. Existing tests and CI remain, supplemented by targeted access-control verification, recovery evidence and accessibility checks. The QA plan assigns responsibility for this work and blocks progress when material failures remain unresolved. Relevant standards inform the plan; certification and formal conformity are outside the proposal.

Non-author review and recorded acceptance evidence bring independent assessment into the workflow, with risk tiers determining the required effort. Internal review provides limited independence. External vulnerability reporting and optional funded audits supplement it. Introducing these arrangements gradually depends on reviewer availability and continuing evaluation. The report proposes changes and makes no claim that they have been implemented or have reduced Actual's defect rate.

---

# 1 Introduction

## 1.1 Background and purpose

Personal finance applications help people record income, track spending and plan how to use their money. Incorrect balances and lost records can affect everyday decisions. Exposed transaction histories can also reveal private information. Actual Budget's product statement measures success through users trusting the figures and completing routine tasks quickly (Actual Budget, 2026a).

I chose Actual Budget because I wanted an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. After finding it, this assignment gave me the opportunity to look at the product in more depth.

The report evaluates a development methodology and proposes a quality assurance process, then integrates independent verification and validation into that methodology. Its recommendations follow an external analysis of public evidence. The analysis involved no contact with Actual's team.

## 1.2 What is Actual Budget?

Actual Budget is a free, open-source personal finance application with an MIT licence. It stores working data on users' devices and supports optional server synchronisation. Its default envelope-budgeting approach allocates money already available to spending categories (Actual Budget, n.d.-k, 2026a).

James Long developed Actual as a commercial product. In early 2022, he closed the commercial service and released the software as open source. A volunteer maintainer team later took responsibility for development (Aboltins, 2025).

## 1.3 Main features and operation

Actual has budgets, account registers, transaction rules, scheduled transactions and reports (Actual Budget, n.d.-k). Its desktop applications support local use. Server options include Docker, PikaPods and Fly.io; a server enables synchronisation across devices and connections to bank-sync providers (Actual Budget, n.d.-d). Figure 1 shows how those optional connections support local budgeting.

**Figure 1. Actual Budget's local-first operation**

```text
Device: local budget and application
                 ↕ optional synchronisation
User-selected server: self-hosted or hosted
                 ↕ optional bank synchronisation
Bank-sync provider
```

*Note.* Author's synthesis of Actual's installation and synchronisation documentation (Actual Budget, n.d.-d, n.d.-i). Local desktop budgeting works without a server. The connected features shown require one.

Users can enable end-to-end encryption for synchronised budget data. The protection excludes local device storage and bank-sync tokens stored separately on the server. Users who self-host control the server but still need to protect their devices and credentials (Actual Budget, n.d.-i).

## 1.4 Who is involved?

**Table 1. Stakeholders and quality expectations**

| Stakeholder | Main interest |
|---|---|
| Users and households | Correct figures, privacy and clear daily tasks |
| Self-hosters | Safe upgrades, recoverable data and manageable servers |
| Eight listed core maintainers | Review capacity and sustainable workloads |
| Contributors | Clear expectations and useful feedback |
| Donors and hosting partners | Continued maintenance and dependable operation |

*Note.* Based on Actual's product statement, contributor guide and funding discussion (Actual Budget, n.d.-a, 2026a; youngcw, 2025). The December 2025 roadmap reported over 8,000 PikaPods users whose hosting fees partly supported the project. That figure describes the position at the time of publication.

## 1.5 Main challenges

- Volunteer availability and community requests constrain review capacity. Section 2 examines this development concern (Aboltins, 2025).
- Section 3 addresses financial correctness, data protection and accessible interactions through explicit quality priorities (Actual Budget, n.d.-i, 2026a).
- Encryption's limits leave security and recovery behaviour needing independent checks. Section 4 proposes how to include these checks in the development workflow (Actual Budget, n.d.-i).

---

# 2 Software Development Methodology

## 2.1 Current development process

Actual's documentation describes a defined workflow without identifying a deliberate methodology. Contributors choose how to participate and review community contributions (Actual Budget, n.d.-e). Feature requests enter a backlog ordered through voting. Larger proposals should be discussed before implementation; small changes can go directly to a pull request (PR) (Actual Budget, n.d.-a, 2026a).

PR review includes automated builds, checks and tests (Figure 2). A change can pass these checks without meeting users' needs (Actual Budget, 2026a).

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

At least two other maintainers must approve the monthly release, which also requires smoke tests of the server and desktop application (Actual Budget, n.d.-c). Feature flags allow incremental delivery and feedback before a feature becomes stable (Actual Budget, n.d.-b). The proposed process should keep these engineering practices.

Review capacity is the more relevant concern. Aboltins (2025) describes PRs that waited months during the early community transition. The current USD 2,000 monthly administrative stipend recognises review and triage work (Actual Budget, n.d.-f). The earlier delays establish a historical coordination risk; they provide no measure of the current backlog.

## 2.2 Project characteristics and selection criteria

Actual's goals, constraints, risks and stakeholder expectations inform the ten criteria in Table 2. Salkever's (2023) maintainer study supports considering review demands and burnout. Methodology selection involves several criteria. The weighted sum used here is simpler than Song et al.'s (2024) specialised model.

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

Weights run from 1 (low) to 3 (high). Security and privacy remain relevant even though regulatory certification has no separate score for this budgeting application. C2 assesses feasibility for volunteers; C7 covers administration, while C8 concerns queues. These constraints overlap.

## 2.3 Candidate methodologies

Screening favoured established approaches with documented applications. Waterfall and the V-model allow limited flexibility as whole-process choices for community-led work. RUP and scaled frameworks require disproportionate coordination structures. Kanban represents Lean in the shortlist. Including Scrumban would duplicate its two shortlisted parents. Shape Up was excluded because the planning search found insufficient independent research evidence; this is a limit of the search and does not demonstrate failure of the approach.

- Spiral uses repeated evaluation driven by risk. Boehm (1988) documents its use at TRW and its dependence on expertise in risk assessment.
- Scrum uses Sprints, defined accountabilities and events for inspection and adaptation. The team needs dependable capacity for shared planning and delivery (Schwaber & Sutherland, 2020).
- Extreme Programming (XP) combines close collaboration with testing and frequent integration. Its creators allow adaptation and remote pairing. Coordinating contributors with intermittent availability remains a concern (Beck & Andres, 2005).
- Kanban makes work visible and controls work in progress (WIP) to manage flow. It is a management method applied to an existing process. Actual could use it to organise the workflow and retain its engineering practices (Kanban University, n.d.).
- DevOps emphasises development and operational capabilities. Research documents adoption of its practices alongside inconsistent definitions. Automation alone gives limited guidance on community prioritisation (Amaro et al., 2023).

The OSS/Bazaar model is a non-selectable baseline for distributed contribution and community feedback (Raymond, 2000). Actual's monthly release schedule would remain a practice within the process; it is excluded as a sixth candidate.

## 2.4 Evaluation and selection

Table 3 scores the support each methodology provides. It does not rate Actual's software quality. All options retain existing CI/tests and must satisfy a mandatory QA gate: relevant security, reliability and interaction checks, assigned responsibility and evidence that can block release (Section 3). The scores express analyst judgement.

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

Total = sum(weight × score), with weights summing to 24. The baseline is non-selectable. Volunteer fit, low ceremony and queue management put Kanban ahead of the stronger intrinsic engineering support in XP/DevOps. C4=3 reflects Kanban's lack of prescribed technical verification. DevOps receives C7=4 because Actual has already invested in pipelines. The cost of Spiral's risk expertise limits its volunteer fit.

Kanban also leads with equal weights (42/50 versus DevOps' 39). Giving quality priority could reverse the ranking. The recommendation depends on the stated constraints; it establishes no universal superiority.

Kanban's seven-point lead over the existing workflow is modest. A lower score for volunteer fit or adoption overhead could remove it. Adoption needs a practical improvement: review capacity must be visible, with agreed conditions for moving work and evidence of acceptance. Merely renaming the issue list would achieve too little. XP and DevOps give stronger engineering guidance, but must still explain who maintains checks and how findings affect release decisions. The mandatory QA gate prevents favourable scores on other criteria from compensating for omitted essential checks.

## 2.5 Applying Kanban to Actual

The proposed board would show existing work and waiting (Figure 3). Kanban uses explicit policies to define when items may move between stages, together with WIP control and feedback (Kanban University, n.d.).

*Figure 3. Proposed Kanban workflow for Actual.*

```text
Backlog/triage → Ready/design → Build/PR → Verify → Release → Done
      ↑                            ↖ rework ↙                  │
      └──────── Operate/maintain: defects and feedback ────────┘

Pull work only when capacity and the preceding exit criteria permit.
Review/Verify WIP is constrained by available reviewer capacity.
```

Community input would remain part of requests. Maintainers would check product fit and risk before moving work to Ready. Cards would link requests to acceptance criteria, PRs and test evidence. Contributors could choose work without Sprint commitments. Build/PR keeps CI/tests, while Verify requires a reviewer and proportionate acceptance evidence. Section 4 develops the independent checks.

Maintainers would agree initial WIP limits based on available review capacity, then adjust them after observing queues. Blocked items would stay visible and count towards WIP. The proposed cadences are weekly asynchronous reviews of ageing cards and monthly flow reviews alongside the existing release cycle. These would provide feedback without mandatory daily meetings. Completed checks would determine release readiness. Urgent security fixes would receive expedited review, with required checks still applying.

## 2.6 Critical evaluation

Kanban addresses visibility and review queues without increasing reviewer capacity. If volunteers leave, reducing WIP may prevent overload and also reduce throughput. Maintainers need to agree and adjust limits; imposing them without consultation could discourage occasional contributors. Ageing work needs discussion, subdivision or withdrawal. It should not create pressure for approval.

Ahmad et al. (2018) report benefits as well as difficulties with implementation, training and supporting practices. Much of the evidence in their mapping is descriptive, which limits causal claims about improvement. Kanban should be introduced as an experiment that observes queue behaviour. A reduction in defects cannot be promised. Its flow controls need the security, reliability and accessibility practices developed in Section 3.

C2, C7 and C8 reward related volunteer constraints. Combining them can favour Kanban more strongly than the scores appear to warrant when treated as separate evidence. The ranking supports a reasoned recommendation but cannot predict how much quality would improve.

Kuhrmann et al. (2022) find that concrete practices matter more to agility than method labels. Keeping Actual's existing engineering controls is defensible tailoring. Their retention cannot count as a new Kanban benefit. Community votes need product and risk judgement too, so popular features should not automatically displace security maintenance.

A stable staffed team, binding delivery commitments or different governance obligations would require reassessment. Stronger Sprint coordination or operational investment might then be worth more than minimal ceremony. The present recommendation depends on its volunteer constraints.

---

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

---

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
