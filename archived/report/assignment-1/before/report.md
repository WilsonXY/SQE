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

Actual Budget is a local-first personal finance application maintained through open-source contributions (Actual Budget, 2026a). This report evaluates its development process and recommends quality assurance and independent verification and validation arrangements suited to volunteer participation.

The methodology comparison selects Kanban, with 102 of 120 weighted points, ahead of DevOps at 94. The existing open-source workflow scores 95 as a non-selectable baseline. These are judgements of project fit, rather than measured quality results. Kanban's strengths are managing review queues, accommodating voluntary work and introducing explicit policies with limited ceremony. It does not provide a complete engineering assurance method.

The proposal therefore makes security, reliability and interaction capability mandatory quality priorities. It retains existing tests and CI while adding targeted access-control verification, recovery evidence and accessibility checks. A compact QA plan assigns responsibility and makes unresolved material failures block progress. Relevant standards guide the proposal without implying certification or formal conformity.

Independent assessment is built into the same workflow through non-author review, proportionate risk tiers and recorded acceptance evidence. Internal review provides limited independence; external vulnerability reporting and optional funded audits supplement it. The recommendations require a gradual introduction, available reviewers and continuing evaluation. They are proposed changes, not implemented practices or demonstrated improvements in Actual's defect rate.

---

# 1 Introduction

## 1.1 Background and purpose

Personal finance applications help people record income, follow spending and plan how to use their money. Their quality matters because incorrect balances or lost records can affect everyday decisions, while exposed transactions can reveal private information. Actual Budget's product statement identifies trust in the numbers and quick completion of routine tasks as measures of success (Actual Budget, 2026a).

I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. Finding it gave me a reason to examine the product more closely through this assignment.

This report evaluates a development methodology, proposes a quality assurance process and integrates independent verification and validation into that methodology. It presents recommendations from an external analysis of public evidence, without contact with Actual's team.

## 1.2 What is Actual Budget?

Actual Budget is a free, open-source personal finance application distributed under the MIT licence. It is local-first: users can work with data on their own devices, with optional server synchronisation. Its default envelope-budgeting approach allocates money already available to spending categories (Actual Budget, n.d.-k, 2026a).

James Long originally developed Actual as a commercial product. In early 2022, he closed the commercial service and made the software open source; a volunteer maintainer team subsequently took responsibility for its development (Aboltins, 2025).

## 1.3 Main features and operation

Actual provides budgets, account registers, transaction rules, scheduled transactions and reports (Actual Budget, n.d.-k). Desktop applications support local use; Docker, PikaPods and Fly.io provide server deployment options. A server enables synchronisation between devices and connections to bank-sync providers (Actual Budget, n.d.-d). Figure 1 separates these optional connections from everyday local budgeting.

**Figure 1. Actual Budget's local-first operation**

```text
Device: local budget and application
                 ↕ optional synchronisation
User-selected server: self-hosted or hosted
                 ↕ optional bank synchronisation
Bank-sync provider
```

*Note.* Author's synthesis of Actual's installation and synchronisation documentation (Actual Budget, n.d.-d, n.d.-i). The server is optional for local desktop budgeting, but required for the connected features shown.

Optional end-to-end encryption protects synchronised budget data. It does not encrypt local device storage or the bank-sync tokens held separately on the server. Therefore, self-hosting gives users control but does not remove their responsibility for protecting devices and credentials (Actual Budget, n.d.-i).

## 1.4 Who is involved?

**Table 1. Stakeholders and quality expectations**

| Stakeholder | Main interest |
|---|---|
| Users and households | Correct figures, privacy and clear daily tasks |
| Self-hosters | Safe upgrades, recoverable data and manageable servers |
| Eight listed core maintainers | Review capacity and sustainable workloads |
| Contributors | Clear expectations and useful feedback |
| Donors and hosting partners | Continued maintenance and dependable operation |

*Note.* Based on Actual's product statement, contributor guide and funding discussion (Actual Budget, n.d.-a, 2026a; youngcw, 2025). The December 2025 roadmap reported over 8,000 PikaPods users whose hosting fees partly supported the project; this is a historical figure.

## 1.5 Main challenges

- Volunteer availability and community requests make review capacity a development constraint, examined in Section 2 (Aboltins, 2025).
- Financial correctness, data protection and accessible interactions require explicit quality priorities, addressed in Section 3 (Actual Budget, n.d.-i, 2026a).
- Encryption has limits; independently checking security and recovery behaviour remains necessary. Section 4 proposes how this checking can fit the development workflow (Actual Budget, n.d.-i).

---

# 2 Software Development Methodology

## 2.1 Current development process

Actual has a defined workflow but no deliberate methodology identified in the reviewed documentation. Contributors choose their involvement and review community contributions (Actual Budget, n.d.-e). Feature requests enter a voting-based backlog; larger proposals should be discussed before implementation, whereas small changes can proceed directly to a pull request (PR) (Actual Budget, n.d.-a, 2026a).

Automated builds, checks and tests support PR review (Figure 2); passing them does not establish that a change meets users' needs (Actual Budget, 2026a).

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

The monthly release requires at least two other maintainers' approval and smoke tests of the server and desktop application (Actual Budget, n.d.-c). Feature flags also enable incremental delivery and feedback before a feature becomes stable (Actual Budget, n.d.-b). These existing engineering practices should be retained.

Review capacity remains the more relevant concern. Aboltins (2025) describes PRs waiting months during the early community transition. The current USD 2,000 monthly administrative stipend recognises review and triage work (Actual Budget, n.d.-f). This establishes a historical coordination risk, rather than proving a current backlog.

## 2.2 Project characteristics and selection criteria

Table 2 translates Actual's goals, constraints, risks and stakeholder expectations into ten criteria. Salkever's (2023) maintainer study supports considering review demands and burnout. Methodology selection is a multi-criteria problem; this report uses a simpler weighted sum than Song et al.'s (2024) specialised model.

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

Weights range from 1 (low) to 3 (high). Regulatory certification is not separately scored for this budgeting application; security and privacy remain relevant. C2 concerns volunteer feasibility, C7 administration and C8 queues, although these constraints overlap.

## 2.3 Candidate methodologies

Screening favoured established approaches with documented application evidence. Waterfall and the V-model offer limited flexibility as whole-process choices for community-led work; RUP and scaled frameworks add disproportionate coordination structures. Lean was represented through Kanban; Scrumban was omitted to avoid duplicating its two shortlisted parents. Shape Up was excluded because the planning search did not establish sufficient independent research evidence. This search limitation does not establish that the approach fails.

- **Spiral** uses repeated, risk-driven evaluation. Boehm (1988) documents TRW use and dependence on risk-assessment expertise.
- **Scrum** organises inspection and adaptation through Sprints, defined accountabilities and events. Shared planning and delivery require dependable capacity (Schwaber & Sutherland, 2020).
- **Extreme Programming (XP)** connects close collaboration with testing and frequent integration. Its creators allow adaptation and remote pairing; synchronising intermittent contributors remains a concern (Beck & Andres, 2005).
- **Kanban** visualises work, controls work in progress (WIP) and manages flow. It is technically a management method applied to an existing process, so adoption would organise Actual's workflow while retaining its engineering practices (Kanban University, n.d.).
- **DevOps** emphasises development and operational capabilities. The literature provides evidence of practice adoption, but also inconsistent definitions; automation alone offers limited guidance for community prioritisation (Amaro et al., 2023).

The OSS/Bazaar model provides a non-selectable baseline, reflecting distributed contribution and community feedback (Raymond, 2000). Actual's monthly release schedule is a practice retained within the process, rather than a sixth candidate.

## 2.4 Evaluation and selection

Scores in Table 3 rate methodology support, not Actual's software quality. Every option retains existing CI/tests and must meet a mandatory QA gate: relevant security, reliability and interaction checks, assigned responsibility and evidence that can block release (Section 3). The scores are analyst judgements.

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

Total = sum(weight × score); weights sum to 24. The baseline is non-selectable. Kanban leads because volunteer fit, low ceremony and queue management outweigh stronger intrinsic engineering support in XP/DevOps. Its C4=3 acknowledges that flow controls do not prescribe technical verification. DevOps' C7=4 recognises Actual's existing pipeline investment; Spiral's risk expertise costs limit its volunteer fit.

Equal weights still favour Kanban (42/50 versus DevOps' 39). Quality-first priorities could reverse the result, so the recommendation depends on the stated constraints rather than universal superiority.

The seven-point margin over the existing workflow is also modest. A lower judgement of Kanban's volunteer fit or adoption overhead could remove that advantage. Its selection therefore requires a practical improvement over the baseline: visible review capacity, agreed movement conditions and evidence of acceptance. Renaming the existing issue list would not justify adoption. XP and DevOps offer stronger engineering guidance, but their application must still explain who maintains the checks and how findings affect release decisions. The mandatory QA gate prevents favourable scores elsewhere from compensating for an assurance plan that omits essential checks.

## 2.5 Applying Kanban to Actual

The proposed board would make existing work and waiting visible (Figure 3). Kanban's explicit policies define when an item may move between stages; the method also supports WIP control and feedback (Kanban University, n.d.).

*Figure 3. Proposed Kanban workflow for Actual.*

```text
Backlog/triage → Ready/design → Build/PR → Verify → Release → Done
      ↑                            ↖ rework ↙                  │
      └──────── Operate/maintain: defects and feedback ────────┘

Pull work only when capacity and the preceding exit criteria permit.
Review/Verify WIP is constrained by available reviewer capacity.
```

Requests would retain community input, with maintainers checking product fit and risk before work becomes Ready. Each card would link the request, acceptance criteria, PR and test evidence. Contributors could select work without Sprint commitments. Build/PR retains CI/tests; Verify requires a reviewer and proportionate acceptance evidence. Section 4 develops independent checks.

Maintainers would jointly set initial WIP limits from available review capacity and revise them after observing queues. Blocked items would remain visible and count towards WIP. A weekly asynchronous review of ageing cards, followed by a monthly flow review alongside the existing release cycle, would provide feedback without mandatory daily meetings. These are proposed cadences. Release readiness would depend on completed checks, with urgent security fixes receiving expedited review without waiving required checks.

## 2.6 Critical evaluation

Kanban directly addresses visibility and review queues, but a board cannot create reviewer capacity. When volunteers leave, lower WIP may prevent overload while reducing throughput. Limits therefore need agreement and adjustment; imposing them without consultation could discourage occasional contributors. Ageing work should prompt discussion, subdivision or withdrawal rather than pressure to approve it.

Research supports this caution. Ahmad et al. (2018) identify benefits alongside implementation, training and supporting-practice difficulties. Their mapping also reports a largely descriptive evidence base, limiting causal claims about improvement. Kanban should consequently be introduced as an experiment with observable queue behaviour, rather than a promised reduction in defects. Its flow controls need the security, reliability and accessibility practices developed in Section 3.

The matrix also rewards related volunteer constraints through C2, C7 and C8. Their combined influence can favour Kanban more strongly than treating each score as separate evidence would suggest. The ranking supports a reasoned recommendation; it cannot predict the size of any quality improvement.

Kuhrmann et al. (2022) find that concrete practices matter more to agility than method labels. Retaining Actual's existing engineering controls is therefore defensible tailoring, rather than a new Kanban benefit. Community votes also need product and risk judgement: popular features should not automatically displace security maintenance.

A stable staffed team, binding delivery commitments or different governance obligations would require reassessment. Stronger Sprint coordination or operational investment might then outweigh minimal ceremony. The recommendation depends on the volunteer constraints used here.

---

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

---

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
