# Methodology reassessment: quality before selection

**Decision update, 22 October 2026:** The author approved the recommended option: the revised score table under the unchanged agreed weights, Kanban, and mandatory QA gates. The quality-first sensitivity scenarios remain diagnostic alternatives, not adopted weights. Section 2.4 has now been drafted. The proposal wording below preserves the reasoning presented before approval.

22 October 2026. Requested after the author challenged Kanban's quality score. This document is a proposal, **not approval of new scores or weights**. Section 2.4 remains unwritten. It supersedes the initial proposal for discussion, without silently changing the agreed methodology plan.

## Direct answer

The author's concern is justified. Kanban scored 3 because its defining contribution is managing work and queues; it does not itself prescribe test-first development, an access-control test suite or accessibility verification. Its score should not be raised merely because the module is Software Quality Engineering. The assignment's quality focus instead requires a stronger explanation of how a selected process prevents defects and whether the evaluation gives that need enough importance.

XP offers more direct engineering practices, particularly test-first work, frequent integration and technical collaboration [S105]. DevOps strengthens verification and delivery/operations feedback, but its name does not establish that security, financial integrity and accessibility are covered [S39,S40]. Existing Actual CI already coexists with escaped access-control flaws [S63, other section's fresh checks]. Consequently neither method deserves an automatic5 for comprehensive product quality. No verified source demonstrates that a switch would give Actual better quality with fewer costs in every relevant dimension.

The fair question is which **incremental changes** are most useful once every option retains Actual's current CI, tests and release checks. Kanban's proposed value is making review capacity and quality gates enforceable in the flow; that is a plausible intervention, not evidence that it adds technical defect-prevention practices on its own.

## A like-for-like baseline and quality gate

For every candidate, assume the same retained starting point: PR review, existing CI/tests, feature flags and the monthly release arrangement. These must not be counted as a new benefit of Kanban, XP or DevOps. Compare changes in their use, coverage, feedback and ownership, not whether they exist.

Before scoring preferences, require a minimum proposed QA arrangement covering:

1. **Security:** explicit security acceptance criteria, access-control verification where relevant and controlled vulnerability handling.
2. **Reliability:** evidence for financial calculations, sync integrity, migrations and recovery when affected.
3. **Interaction capability:** relevant accessibility and user-task acceptance checks.

An option whose application cannot state who performs these checks and what blocks release fails the gate, regardless of its numerical score. This is a recommended analytical safeguard, not a claim that an external standard specifies this exact three-part gate. All five candidates **could** pass when the Section 3 controls are explicitly embedded; their generic labels alone establish none of these outcomes.

The scoring then asks how much the method itself helps organise and sustain those controls. C4 should mean **support for preventing product defects across the chosen qualities**, rather than simply presence of automation. Scores are contextual analyst judgements, not experimental effect sizes.

## Revised score proposal under the unchanged agreed weights

| Option | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Total/120 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Weight | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 24 |
| Spiral | 4 | 2 | 3 | 4 | 5 | 3 | 2 | 2 | 3 | 2 | 72 |
| Scrum | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 81 |
| XP | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 82 |
| Kanban | 5 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 4 | 3 | 102 |
| DevOps | 4 | 4 | 5 | 4 | 3 | 5 | 4 | 3 | 3 | 4 | 94 |
| OSS/Bazaar baseline | 5 | 5 | 5 | 3 | 2 | 3 | 4 | 2 | 5 | 5 | 95 |

Weighted total = sum(weight×score); weights sum 24; maximum 120. Baseline is still non-selectable. Equal-weight check: Kanban 42/50, DevOps 39, baseline 39, Scrum 34, XP 34, Spiral 30.

Changes from the first proposal:

- **Spiral C7:1→2.** Boehm's original describes adaptable risk-driven effort, not obligatory heavy documentation. The cost concern is expert risk assessment and repeated decision work [S26].
- **Scrum C2:2→3; C3:3→4; C7:2→3.** A distributed team can run Scrum; variable availability complicates Sprint goals but is not prohibition. Defined events have overhead, yet also replace ad hoc coordination [S34].
- **XP C2:2→3; C3:2→3; C7:2→3.** The creators explicitly allow adapting practices and remote pairing [S105]. Score coordination demands once in each distinct dimension: irregular availability(C2), time-zone synchronisation(C3), recurring planning/practice maintenance(C7). These remain correlated, so total penalties require caution.
- **XP C4:5→4.** Strong engineering practices address defect prevention and reliability, but do not constitute a complete security/accessibility assurance scheme [S105].
- **DevOps C4:5→4.** Automated tests and operational feedback are valuable but not evidence of the selected attributes being fully verified [S39,S40].
- **DevOps C7:2→4.** Actual already operates pipelines. Charging it for building CI from nothing was unfair. This revision assumes incremental extension; a proposal requiring a new platform or staffed operations function would need lower overhead fit.
- **Kanban remains C4=3.** Existing CI/tests are common baseline, not grounds to award its flow method stronger intrinsic quality coverage. Its favourable flow/volunteer scores remain hypotheses about fit, not measured outcomes.

The remaining C4 scores are defensible only as relative support, not a claim that XP and DevOps deliver equal measured quality. **A score of 3/5 rates methodology support; it is not a rating of Actual software quality.** Scrum is also C4=3: its Definition of Done and inspection do not prescribe technical checks for the three selected qualities, and explicit quality policies are available under Kanban too. Spiral retains C4=4 because risk analysis explicitly selects mitigation and verification effort; XP adds test-first engineering; DevOps adds shared development/operational responsibility and feedback. Each still needs the QA gate. A1–5 scale is coarse and should not imply more precision than the evidence permits.

## Quality-first sensitivity with an actual change of winner

The agreed weight scale stops at3 and C4 is already3. Increasing it beyond3 creates a **new, unapproved weighting model**. This must be discussed openly rather than presented as the agreed matrix. These scenarios test sensitivity; weights must never be selected merely to make a preferred candidate win. Author priorities should determine weights before using the resulting ranking.

Keep revised scores above and compare these transparent scenarios:

| Scenario | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Kanban | DevOps | Winner among selectable options |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Agreed weights | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 102 | 94 | Kanban |
| More quality/risk emphasis | 2 | 2 | 2 | 5 | 5 | 2 | 2 | 2 | 2 | 2 | 102 | 99 | Kanban |
| Threshold | 2 | 2 | 2 | 8 | 5 | 2 | 2 | 2 | 2 | 2 | 111 | 111 | Tie |
| Quality-first alternative | 2 | 2 | 2 | 9 | 5 | 2 | 2 | 2 | 2 | 2 | 114 | 115 | DevOps |

In the last scenario weights sum 30: quality receives 30%, explicit risk 16.7%, together 46.7%. All totals /150 are DevOps 115, Kanban 114, XP 105, baseline 105, Spiral 103 and Scrum 98. It changes the winner, but a one-point difference is too fragile to claim a decisive result. A one-level judgement change on a material criterion can reverse it.

Reproduction for the middle family: let C4=q, C5=5 and every other weight=2. Kanban=87+3q; DevOps=79+4q. They tie at q=8 and DevOps leads for q>8. Raising **only** C4 in the original agreed weights produces a tie at C4=11 and a DevOps lead at 12. Neither threshold is an empirical law; both depend on the proposed scores.

## Would DevSecOps deserve another candidate slot?

Potentially, especially because security is a selected priority. NIST's 2024 guidance recognises DevSecOps and documents integration of software-supply-chain security into CI/CD [S111]. It therefore has a substantially stronger documentary basis than an improvised method name.

However, that publication's scope is supply-chain security for cloud-native pipelines. It is not evidence that Actual's application-level authorisation, financial consistency or accessibility would become adequate merely by adopting the label. Comparable volunteer-project evidence, incremental responsibilities and assurance coverage would need investigation before scoring it. It must not silently replace DevOps or expand the agreed five-candidate shortlist. A defensible alternative is discussing it as an established security-oriented extension when designing QA under a DevOps selection, with the exact selection and no-hybrid requirement settled explicitly with the author.

## Recommendation for the author

**Keep Kanban as the provisional preference if the decision remains about improving Actual's existing workflow under the agreed volunteer constraints, but make QA coverage a mandatory gate and use the revised fairer comparison.** This recommends a limited flow intervention supported by explicit engineering and assurance controls. It does not claim Kanban inherently produces the best product quality.

**Choose DevOps provisionally if the author wants quality and operational feedback to dominate the selection**, subject to spelling out what would change beyond Actual's present pipelines. The quality-first matrix shows this is possible without manipulating Kanban's score. Its one-point numerical lead does not justify switching by itself. A switch needs a separately justified priority decision and a credible incremental implementation, rather than treating the sensitivity result as evidence that DevOps is empirically superior.

XP deserves credit for explicit engineering discipline and could be sensible if the main intervention were test-first development supported by sustained collaboration. The current evidence does not establish that its additional coordination is a better incremental fit for Actual than improving the existing verification pipeline and review flow. This remains an inference, not a proven rejection.

The decision is therefore about **what the methodology must contribute**: managing scarce review capacity, or making engineering/operational assurance the central organising approach. The next author decision should approve a revised score rubric and either retain the agreed weights or explicitly adopt a quality-first alternative. Section 2.4 and downstream method-specific headings remain pending that decision.

## Source status

S26,S34,S105,S109 were directly read in this session. S38 publisher abstract was re-read; detailed paper notes were verified in the prior session. S39,S40,S47 rely on recorded prior readings, supplemented by the live DORA official overview. S63 live advisory checks are owned by the QA/IV&V agents. S111 metadata/abstract were read and logged immediately in `planning/sources.md`; it is not currently a report citation. No Humanizer skill has been read or applied.
