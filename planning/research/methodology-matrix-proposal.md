# Section 2 matrix proposal — author decision pending

Prepared 22 October 2026. This proposal preserves the ten criteria and weights already agreed in `planning/02-methodology.md`. Scores are analyst judgements about fit to Actual, not measured project outcomes. Section 2.4 must await the author's approval.

Scale: 1 = poor fit; 2 = limited fit; 3 = workable with material adaptation; 4 = good fit; 5 = strong fit. C10 assesses transferability of available evidence, rather than popularity. The OSS/Bazaar baseline is scored but cannot be selected under the agreed scope.

| Option | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Weighted total /120 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Weight | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 24 |
| Spiral | 4 | 2 | 3 | 4 | 5 | 3 | 1 | 2 | 3 | 2 | 69 |
| Scrum | 4 | 2 | 3 | 4 | 3 | 4 | 2 | 3 | 4 | 3 | 76 |
| XP | 4 | 2 | 2 | 5 | 3 | 4 | 2 | 3 | 4 | 3 | 77 |
| Kanban | 5 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 4 | 3 | 102 |
| DevOps | 4 | 4 | 5 | 5 | 3 | 5 | 2 | 3 | 3 | 4 | 91 |
| OSS/Bazaar baseline | 5 | 5 | 5 | 3 | 2 | 3 | 4 | 2 | 5 | 5 | 95 |

Formula: total = sum(weight × score), maximum 5 × 24 = 120. Normalised means: Spiral 2.88; Scrum 3.17; XP 3.21; Kanban 4.25; DevOps 3.79; baseline 3.96.

## Decisive rationales

- **Spiral:** C5=5 recognises explicit risk-driven iteration; C2=2 and C7=1 reflect the coordination and analysis demanded of a self-selecting volunteer group [S26, subject to content check].
- **Scrum:** C1=4 and C6=4 credit inspection and short delivery cycles; C2=2 and C7=2 reflect Sprint commitments, accountabilities and recurring events rather than any claim that distributed Scrum is impossible [S34].
- **XP:** C4=5 credits testing and integration emphasis; C2=2/C3=2 reflect synchronisation costs of intensive collaboration and short planning cycles. Verify specific practice claims before prose [S35].
- **Kanban:** C2=5/C7=5 reflect pull-based work without mandatory Sprint commitments; C8=5 directly addresses review queues. C4=3/C5=3 acknowledge that visualising flow supplies neither a complete testing strategy nor explicit risk analysis. C10=3 deliberately recognises limited directly comparable OSS evidence [S38].
- **DevOps:** C4=5/C6=5 credit automated verification and delivery capability; C7=2 reflects pipeline and operational investment, and C8=3 recognises that delivery automation alone does not allocate scarce human reviews. Actual's existing CI moderates, but does not eliminate, adoption effort [S39, S40].
- **OSS/Bazaar baseline:** C2=5/C3=5/C9=5 credit Actual's demonstrable volunteer and community fit. C5=2/C8=2 reflect absent explicit risk/flow controls, rather than an assertion that OSS cannot manage risk; C10=5 follows its direct applicability [S01–S10, S25].

## Sensitivity checks

- Equal criterion weights: Kanban 42/50, baseline 39, DevOps 38, XP/Scrum 32, Spiral 29. Kanban remains first.
- Changing any **one** agreed weight by one point within the 1–3 scale cannot reverse Kanban's 11-point lead over the next selectable option (DevOps); the greatest single-criterion difference is three points.
- More sceptical Kanban scoring: reduce C2 and C7 from 5 to 4, and C10 from 3 to 2. Kanban falls to 94, remaining above DevOps 91 but below the non-selectable baseline 95. Thus the practical improvement over today's process is less certain than the candidate ranking suggests.
- A counter-scenario should be retained in the report: a staffed operations team and overriding delivery/security needs could improve DevOps' C7 and risk fit sufficiently to change the selection. Scores must be revisited if those conditions change.

## Decision requested

Approve or amend these scores before drafting 2.4. The weighting is unchanged from the agreed plan. Source checks may require a particular score/rationale to be revised; any such change will be raised explicitly.
