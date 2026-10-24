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
