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
