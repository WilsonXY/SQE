# 2 Software Development Methodology

## 2.1 Current development process of Actual (as-is)

Actual's contributing documentation names no methodology (no evidence found, October 2026). Issues and roles are not assigned, and contributors choose their own work (Actual Budget, n.d.-a, n.d.-e). Automation labels feature requests "needs votes", so the backlog is effectively requests ranked by community votes (Actual Budget, 2026a). Small changes go straight to a pull request (PR), and larger features are discussed in an issue first (Actual Budget, n.d.-a). Each PR runs continuous integration (CI) checks: linting, type-checking, unit, end-to-end and visual tests, and CodeQL (Actual Budget, 2026a). Core maintainers review it and may merge non-controversial changes straight away (Actual Budget, n.d.-e). Large features ship behind feature flags (Actual Budget, n.d.-b).

Releases follow a monthly train. The release branch is cut automatically at 17:00 UTC on the 25th. Two other maintainers must approve before tagging and publishing, and smoke tests precede the announcement (Actual Budget, n.d.-c). A USD 2,000 monthly pool pays maintainers for review and triage (Actual Budget, n.d.-f). Review capacity has been the bottleneck before: after the 2022 open-sourcing, PRs waited months for review (Aboltins, 2025). Actual therefore has **a defined workflow but no deliberate methodology** (Figure 2).

```
Feature request --> "needs votes" backlog (ranked by votes)
                           |
  small change             | larger feature: issue discussion first
        \                  v
         +--------> Pull request
                           |
                           v
          CI: lint, typecheck, unit, E2E, visual, CodeQL
                           |
                           v
          Maintainer review --> merge (feature flag if large)
                           |
                           v
          Monthly release cut (25th, 17:00 UTC)
                           |
                           v
          >=2 other maintainers approve --> tag and publish
          --> smoke test --> announce
```

*Figure 2. Actual's as-is development workflow (compiled from the sources cited in 2.1).*

## 2.2 Project characteristics and selection criteria

The criteria come from four lenses. The **goal** is users trusting the numbers (Actual Budget, 2026a). The main **constraint** is capacity: eight volunteer core maintainers, whose mental health the project puts first (Actual Budget, n.d.-a), funded by donations (Actual Budget, n.d.-f). The **risks** are slow review (Aboltins, 2025) and burnout, which consensus-heavy decision-making "may accelerate" (Salkever, 2023, pp. 26–27). **Stakeholders** set priorities through votes (Actual Budget, 2026a).

Methodology selection is a multi-criteria decision (Song et al., 2024), so a weighted matrix is used (Table 2.1).

*Table 2.1. Selection criteria and weights (1 = low, 3 = high).*

| # | Criterion | Weight |
|---|---|---:|
| C1 | Copes with evolving, community-voted requirements | 3 |
| C2 | Works with volunteer, self-selected work | 3 |
| C3 | Supports distributed, asynchronous collaboration | 2 |
| C4 | Builds quality in (financial correctness, data integrity) | 3 |
| C5 | Explicit risk management | 2 |
| C6 | Predictable, frequent delivery | 2 |
| C7 | Low process overhead | 3 |
| C8 | Manages flow and bottlenecks | 2 |
| C9 | Community involvement and feedback | 2 |
| C10 | Proven use in comparable projects | 2 |

## 2.3 Candidate methodologies

A longlist was screened first. Waterfall, the V-Model and RUP assume stable requirements; FDD, Crystal Clear, DSDM and SAFe/LeSS assume class ownership, co-location or enterprise governance. A **proof rule** then removed Shape Up (Singer, 2019), for which no peer-reviewed evaluation was found. Lean overlaps heavily with Kanban. Scrumban is used in practice (Meireles et al., 2026) but was cut because both of its parents are shortlisted. The release train is a scheduling practice, not a candidate.

Five candidates remain:

- **Spiral:** risk-driven cycles, each tackling the largest remaining risk. It depends on risk-assessment expertise (Boehm, 1988).
- **Scrum:** fixed-length Sprints, three accountabilities and a Definition of Done (Schwaber & Sutherland, 2020).
- **XP:** weekly cycles, test-first programming and CI. Its creators permit adaptation and remote pairing (Beck & Andres, 2005).
- **Kanban:** visualise work, limit work in progress (WIP), manage flow and make policies explicit. Its official guide presents it as a management method applied to an existing process, not a complete methodology (Kanban University, n.d.). It is compared here because flow is Actual's weakest point.
- **DevOps:** capabilities shared across development and operations. A review of 93 documents found 37 capabilities but inconsistent adoption and unclear concepts (Amaro et al., 2023).

The **OSS ("Bazaar") model** of decentralised volunteer development (Raymond, 2000; Mockus et al., 2002) describes Actual today. It is scored as a baseline but cannot be selected.

## 2.4 Evaluation and selection

Before scoring, each option had to pass a **mandatory QA gate**. It must state who checks Security, Reliability and Interaction capability (Section 3) and what blocks a release. All five candidates can pass once those controls are embedded. Every option keeps Actual's existing CI, tests, review and release train, so none earns credit for them. Scores (1–5) are analyst judgements, not measured outcomes.

*Table 2.2. Weighted decision matrix (score 1–5 × weight; maximum 120).*

| Option | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Weight | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 24 |
| Spiral | 4 | 2 | 3 | 4 | 5 | 3 | 2 | 2 | 3 | 2 | 72 |
| Scrum | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 3 | 81 |
| XP | 4 | 3 | 3 | 4 | 3 | 4 | 3 | 3 | 4 | 3 | 82 |
| **Kanban** | 5 | 5 | 5 | 3 | 3 | 4 | 5 | 5 | 4 | 3 | **102** |
| DevOps | 4 | 4 | 5 | 4 | 3 | 5 | 4 | 3 | 3 | 4 | 94 |
| OSS baseline | 5 | 5 | 5 | 3 | 2 | 3 | 4 | 2 | 5 | 5 | 95 |

Kanban entered as a working hypothesis, and the matrix tested it, including on its weak criteria. Its lead comes from C2, C7 and C8. Pull-based work needs no Sprint commitment from volunteers, and WIP limits target the review queue that has stalled Actual before. Its C4 score of 3 rates **methodology support, not Actual's software quality**, because managing flow prescribes no tests. XP (test-first) and DevOps (automated feedback) score 4, yet neither is a complete security or accessibility scheme. DevOps is the strongest alternative (94). Extending existing pipelines is cheap (C7 = 4), but automation does not allocate scarce human review (C8 = 3). Scrum and XP lose on coordination cost, and Spiral on expert risk analysis (C2, C7 = 2).

The baseline's 95 matters, because today's process already fits volunteers well. Kanban's 7-point margin rests mainly on flow control (C8) and lower overhead (C7), partly offset by weaker evidence (C10). With equal weights Kanban still ranks first (42/50, against 39 for DevOps and the baseline). **Kanban, tailored with mandatory QA gates, is selected.**

## 2.5 Applying Kanban to Actual (to-be)

Kanban is layered over Actual's existing GitHub workflow rather than replacing it (Kanban University, n.d.). The board has six columns, each with an **explicit policy**: an exit criterion that must hold before work is pulled onward (Ahmad et al., 2018, p. 98; Figure 3). Verify carries a WIP limit, set from observed review throughput, so that new work stops starting while reviews pile up. Section 3's QA gate is the Verify exit policy, and Section 4 attaches IV&V activities to each column. The monthly cut remains the delivery cadence, with a short flow review there to adjust limits and policies. The changes from today are a visible review queue, enforced limits and written, mandatory pull criteria.

```
Rule: pull work only when the next column is under its WIP limit
+------------------------+------------------------------------------------+
| Column                 | Exit policy (pull criterion)                   |
+------------------------+------------------------------------------------+
| 1 Requirements/triage  | Problem, acceptance criteria and risk recorded |
| 2 Design               | Approach agreed; decision record if high-risk  |
| 3 Build/PR             | CI green; tests and release note included      |
| 4 Verify   [WIP limit] | Reviewer is not the author; QA gate passed     |
|                        | (Security, Reliability, Interaction capability)|
| 5 Release train        | Monthly cut (25th); >=2 approvals; smoke test  |
| 6 Operate/maintain     | User reports and advisories triaged to col. 1  |
+------------------------+------------------------------------------------+
        ^                                                      |
        +------------------- feedback loop --------------------+
```

*Figure 3. Proposed (to-be) Kanban workflow for Actual with explicit exit policies.*

## 2.6 Critical evaluation

Kanban's main weakness is the one the matrix exposes. It is "a relatively basic flow tool that needs to be supported by additional practices" (Ahmad et al., 2018, p. 110). Without the QA gate and retained CI, the board would only display the existing queue. Reported challenges include setting up and maintaining the system, organisational culture, missing supporting practices and lack of training (Ahmad et al., 2018, p. 106). Open limitations remain (Alaidaros et al., 2021).

Volunteering adds risk. A WIP limit cannot compel anyone to review, and blocked PRs may discourage newcomers, as unanswered PRs do (Salkever, 2023). Limits should therefore act as signals, with the review stipend (Actual Budget, n.d.-f) directed at Verify. The evidence is also thin. C10 is only 3, and the small margin over the baseline makes the gain plausible but unproven. Tailoring one named method is defensible because processes commonly mutate into hybrids, and the practices chosen matter more than the label (Kuhrmann et al., 2022).

The choice would stop fitting if Actual gained paid staff or operated a hosted service, which would favour DevOps. It would also stop fitting if quality were weighted far above volunteer fit. DevOps overtakes Kanban only when the C4 weight is raised well beyond the agreed 1–3 scale, and then only narrowly.

<!-- Cited: S01, S02, S03, S04, S07, S08, S10, S18, S22, S25, S26, S34, S36, S37, S38, S39, S42, S47, S105, S108, S109 -->
