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
