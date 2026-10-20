# Section 2 — Software Development Methodology (10 marks)

Status: **In discussion.** The flow is agreed. Candidates and criteria are next.

## Agreed

- Candidates are **not** limited to the common list. Less mainstream methodologies can be candidates too.
- Selection is based on **how effective the methodology would be for this project**, not on how popular it is.
- The section starts from **Actual's current (as-is) workflow**, then asks which methodology would suit Actual best if a proper one were adopted.
- Wording of the as-is finding: **"a defined workflow but no deliberate methodology"**.
- **Flow 2.1–2.6 as below**, provisionally. It may change slightly once writing starts.
- **Use a weighted decision matrix.** The full matrix goes in an appendix (appendices don't count towards the word limit; the lecturer confirmed this). A summary goes in the body.
- **No hybrid.** The selected methodology must be one that already exists and has been **proven in real-world use**, not something invented for this report.
- **DevOps is a candidate.** The author studied it as a methodology last semester.
- **Point of view: outside analysts recommending a methodology.** This is a university assignment only, and there is no contact with the Actual team. This also applies to Assignment 2.

## Flow

The logic runs: **what they do → what the project needs → what options exist → which fits best → how it would work → honest limits.**

| # | Subsection | Purpose | Main content |
|---|---|---|---|
| 2.1 | Current development process of Actual (as-is) | Ground the section in evidence | How work flows today: vote or issue → PR → CI → review → merge → monthly release. A workflow figure. Conclusion: a defined workflow but no deliberate methodology. |
| 2.2 | Project characteristics and selection criteria | Turn the brief's four lenses into criteria | Goals, constraints, risks and stakeholder expectations, plus the 8 selection factors from Lecture 2. These give weighted criteria (draft below). |
| 2.3 | Candidate methodologies | Show the options considered | Longlist → screening (one line each) → shortlist with a short description each. |
| 2.4 | Evaluation and selection | Make the choice traceable | Matrix summary (full version in an appendix), the selected methodology, and its justification against goals, constraints, risks and stakeholders. |
| 2.5 | Applying the methodology to Actual (to-be) | Show it is practical | Roles, cadence, artefacts and workflow under the chosen methodology. What changes compared with today. Section 4 (IV&V) builds on this. |
| 2.6 | Critical evaluation | Where most marks come from | Strengths, weaknesses, risks, mitigations, and the conditions under which this choice would stop being right. |

Approximate words: 2.1 ≈ 250 · 2.2 ≈ 250 · 2.3 ≈ 300 · 2.4 ≈ 300 · 2.5 ≈ 200 · 2.6 ≈ 250, about **1,500 in total**, plus the appendix matrix.

## Proposed (pending approval)

### A. Release Train: not a candidate

A **release train** means shipping on a fixed calendar, e.g. every month. Whatever is finished and tested by the cut-off date goes in, and anything unfinished waits for the next "train". Firefox (from 2011) and Chrome are well-known examples. The term "Agile Release Train" also comes from SAFe, where it means a team of agile teams.

It only covers **when to release**. It doesn't tell you how to gather requirements, plan, design, build or test, so it is a **release-management practice, not a development methodology**. Actual already does this (the automatic cut on the 25th of every month), so it belongs in **2.1 (as-is)** and possibly **2.5 (to-be)**, not in the candidate list.

### B. The current open-source ("Bazaar") model: a baseline only

It **does make sense** to include it purely for comparison. This is standard practice in decision analysis, sometimes called the "do-nothing" or "status quo" option:

- It is scored in the matrix with the same criteria, so readers can see whether each candidate actually **improves on today**.
- It is **not eligible to be selected**, because the brief asks for a proper methodology to be selected.
- Risk: the baseline might score close to the winner. That is still a valid finding. The criteria should fairly capture the as-is weaknesses already in the evidence: the PR review backlog that left PRs waiting for months in 2022, no explicit risk management, no assigned work.

### C. Updated longlist (with screening view)

| Family | Methodology | First view | Proposed status |
|---|---|---|---|
| Plan-driven | Waterfall | Requirements change constantly through votes, and releases are monthly. | Screen out |
| Plan-driven | V-Model | Too rigid as a whole methodology. Its V&V pairing is still useful in Section 4. | Screen out |
| Plan-driven | Incremental | Generic. Too broad to be distinct. | Screen out |
| Plan-driven / iterative | RUP | Heavy roles and artefacts for a volunteer team. | Screen out |
| Risk-driven | Spiral (Boehm) | Financial data integrity is high-risk, but heavy risk analysis each loop doesn't suit volunteers. | **Shortlist** |
| Agile | Scrum | Needs committed teams, a product owner and sprints. Evaluate on its merits. | **Shortlist** |
| Agile | Extreme Programming (XP) | Engineering practices fit well. Pair programming and an on-site customer don't. | **Shortlist** |
| Agile / Lean | Kanban | Continuous pull-based flow and WIP limits. "Start with what you do now." | **Shortlist** |
| Lean | Lean Software Development | Eliminate waste, build quality in, respect people. | **Shortlist** |
| Agile | Scrumban | Essentially a Scrum/Kanban hybrid. The "no hybrid" rule probably excludes it. | Screen out? |
| Agile | FDD | Class ownership and a chief-programmer role clash with open-source contribution. | Screen out |
| Agile | DSDM | Enterprise governance overhead. | Screen out |
| Agile | Crystal Clear | Assumes a small co-located team. | Screen out |
| Product-cycle | Shape Up (Basecamp) | Fixed time, variable scope, no backlog. Expects dedicated 6-week teams. | **Shortlist** |
| Ops-extended | DevOps | Strong automation and CI/CD culture, which Actual already partly has. Gives little guidance on requirements and prioritisation, which is good material for evaluation. | **Shortlist** |
| Scaled | SAFe / LeSS / Disciplined Agile | Built for large multi-team enterprises. | Screen out |
| Open-source | Bazaar / OSS model (Raymond, 1999; Mockus et al., 2002) | Describes today's process. | **Baseline only** |

Proposed shortlist: **Spiral, Scrum, XP, Kanban, Lean, Shape Up, DevOps** (7 candidates) plus the Bazaar baseline.

Current leaning (only a hypothesis): **Kanban**. Its principle "start with what you do now" fits a project that already has a working process. WIP limits and flow management directly target the review bottleneck. It has a documented track record. The strongest challengers are Lean and DevOps.

### D. Draft selection criteria for 2.2 (for the next discussion)

Scale: each methodology is scored **1–5** per criterion. Weight **1 = low, 2 = medium, 3 = high** importance to Actual.

| # | Criterion | Comes from (brief lens / Lecture 2 factor) | Draft weight |
|---|---|---|---|
| C1 | Copes with evolving, community-voted requirements | Goals, stakeholders / Project requirements, Flexibility | 3 |
| C2 | Works with volunteer, part-time, self-selected work (no fixed commitment) | Constraints / Team expertise, Time constraints | 3 |
| C3 | Supports distributed, asynchronous collaboration | Constraints / Team expertise | 2 |
| C4 | Builds quality in: defect prevention for financial correctness and data integrity | Goals ("users trust the numbers"), Risks | 3 |
| C5 | Explicit risk management (data loss, security, migrations) | Risks / Risk tolerance | 2 |
| C6 | Predictable, frequent delivery | Stakeholders / Time constraints | 2 |
| C7 | Low process overhead and ceremony (small core team, burnout risk) | Constraints, Risks / Project size & complexity | 3 |
| C8 | Manages flow and bottlenecks (e.g. the review backlog) | Risks, Constraints | 2 |
| C9 | Stakeholder and community involvement and feedback | Stakeholders / Customer involvement | 2 |
| C10 | Proven real-world use in comparable projects (open-source, distributed) | Your "proven to work" requirement | 2 |
| — | Regulatory compliance (Lecture 2 factor) | Low relevance: Actual is not a regulated bank and users self-host. Mentioned in the text, not scored. | — |

## Open questions

1. **Release Train:** agree it is a practice (covered in 2.1/2.5), not a candidate?
2. **Bazaar baseline:** agree it is scored for comparison but not selectable?
3. **Tailoring vs hybrid:** "no hybrid" means we pick one existing methodology. Is it OK for 2.5 to show that methodology **tailored** to Actual and keeping its existing good practices (e.g. CI and automated tests), as long as we don't claim a second methodology? Almost every methodology expects some tailoring. Kanban says so explicitly.
4. **Scrumban:** screen it out under the no-hybrid rule?
5. **Shortlist:** are the 7 candidates OK (Spiral, Scrum, XP, Kanban, Lean, Shape Up, DevOps)? Seven makes a big matrix, so it could be cut to about 5, but the matrix sits in an appendix.
6. **Criteria and weights (D):** add, remove or re-weight anything?
