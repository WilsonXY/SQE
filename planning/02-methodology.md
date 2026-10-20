# Section 2 — Software Development Methodology (10 marks)

Status: **Agreed** (2026-10-20). The flow may still be adjusted slightly during writing.

## Agreed

- Candidates are **not** limited to the common list. Less mainstream methodologies can be candidates too.
- Selection is based on **how effective the methodology would be for this project**, not on how popular it is.
- The section starts from **Actual's current (as-is) workflow**, then asks which methodology would suit Actual best if a proper one were adopted.
- Wording of the as-is finding: **"a defined workflow but no deliberate methodology"**.
- **Flow 2.1–2.6 as below**, provisionally. It may change slightly once writing starts.
- **Use a weighted decision matrix.** The full matrix goes in an appendix (appendices don't count towards the word limit; the lecturer confirmed this). A summary goes in the body.
- **No hybrid we invent ourselves.** The selected methodology must already exist and be **proven in real-world use**.
- **Proof rule for candidates:** a methodology is a candidate only if there is real-world evidence it works (for example peer-reviewed case studies or a documented track record). Methodologies with weak evidence that would be hard to explain and defend are dropped. An established named methodology that combines others (e.g. Scrumban) is acceptable **if** it passes this rule.
- **Tailoring is allowed.** 2.5 can show the one chosen methodology adapted to Actual and keeping its existing good practices (CI, automated tests), without claiming a second methodology.
- **DevOps is a candidate.** The author studied it as a methodology last semester.
- **Release Train is not a candidate.** It is a release-scheduling practice (fixed-calendar releases; whatever is ready ships). It is covered in 2.1 (as-is: the monthly cut on the 25th) and possibly 2.5.
- **The open-source ("Bazaar") model is a baseline only.** It is scored with the same criteria for comparison ("status quo" option) but **cannot be selected**.
- **Shortlist size: 5 candidates + 1 baseline.**
- **Criteria C1–C10 and weights** as below.
- **Point of view: outside analysts recommending a methodology.** This is a university assignment only, with no contact with the Actual team. This also applies to Assignment 2.
- Current leaning, accepted as a working hypothesis to be tested by the matrix: **Kanban**.

## Flow

The logic runs: **what they do → what the project needs → what options exist → which fits best → how it would work → honest limits.**

| # | Subsection | Purpose | Main content |
|---|---|---|---|
| 2.1 | Current development process of Actual (as-is) | Ground the section in evidence | How work flows today: vote or issue → PR → CI → review → merge → monthly release train. A workflow figure. Conclusion: a defined workflow but no deliberate methodology. |
| 2.2 | Project characteristics and selection criteria | Turn the brief's four lenses into criteria | Goals, constraints, risks and stakeholder expectations, plus the 8 selection factors from Lecture 2. These give criteria C1–C10. |
| 2.3 | Candidate methodologies | Show the options considered | Longlist → screening (one line each, including the proof rule) → shortlist of 5 with a short description each, plus the baseline. |
| 2.4 | Evaluation and selection | Make the choice traceable | Matrix summary (full version in an appendix), the selected methodology, and its justification against goals, constraints, risks and stakeholders. |
| 2.5 | Applying the methodology to Actual (to-be) | Show it is practical | The chosen methodology tailored to Actual: roles, cadence, artefacts and workflow. What changes compared with today. Section 4 (IV&V) builds on this. |
| 2.6 | Critical evaluation | Where most marks come from | Strengths, weaknesses, risks, mitigations, and the conditions under which this choice would stop being right. |

Approximate words: 2.1 ≈ 250 · 2.2 ≈ 250 · 2.3 ≈ 300 · 2.4 ≈ 300 · 2.5 ≈ 200 · 2.6 ≈ 250, about **1,500 in total**, plus the appendix matrix.

## Selection criteria (agreed)

Scale: each methodology is scored **1–5** per criterion. Weight **1 = low, 2 = medium, 3 = high** importance to Actual.

| # | Criterion | Comes from (brief lens / Lecture 2 factor) | Weight |
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
| C10 | Proven real-world use in comparable projects (open-source, distributed) | Author's "proven to work" requirement | 2 |
| — | Regulatory compliance (Lecture 2 factor) | Low relevance: Actual is not a regulated bank and users self-host. Mentioned in the text, not scored. | — |

## Longlist and screening

| Family | Methodology | Screening reason | Status |
|---|---|---|---|
| Plan-driven | Waterfall | Requirements change constantly through votes, and releases are monthly. | Screened out |
| Plan-driven | V-Model | Too rigid as a whole methodology. Its V&V pairing is still useful in Section 4. | Screened out |
| Plan-driven | Incremental | Generic. Too broad to be distinct. | Screened out |
| Plan-driven / iterative | RUP | Heavy roles and artefacts for a volunteer team. | Screened out |
| Risk-driven | Spiral (Boehm, 1988) | Proven, especially in large and high-risk projects. Its risk focus matches financial data integrity, but its heavy risk analysis is a poor fit for volunteers. | Passes the proof rule |
| Agile | Scrum | Proven and widely studied. Needs committed teams, a product owner and sprints. | Passes the proof rule |
| Agile | Extreme Programming (XP) | Proven. Engineering practices fit well. Pair programming and an on-site customer don't. | Passes the proof rule |
| Agile / Lean | Kanban | Proven. Continuous pull-based flow, WIP limits, "start with what you do now". | Passes the proof rule |
| Lean | Lean Software Development | Proven principles, but it is more a set of principles than a concrete process. Kanban is its most common concrete implementation. | Passes the proof rule |
| Ops-extended | DevOps | Proven (e.g. DORA / *Accelerate* research). Strong on automation and CI/CD. Gives little guidance on requirements and prioritisation. | Passes the proof rule |
| Agile hybrid (established) | Scrumban (Ladas, 2009) | **Evidence exists:** a peer-reviewed case study of a Scrum-to-Scrumban transition (Nikitina, Kajko-Mattsson & Strale, ICSSP 2012) and studies in distributed teams. The evidence base is smaller than for Scrum or Kanban. | Passes the proof rule (moderate evidence) |
| Product-cycle | Shape Up (Singer, 2019) | **No peer-reviewed evidence found.** Only Basecamp's own book and practitioner blogs and trial reports. Hard to defend academically. | **Dropped (fails the proof rule)** |
| Agile | FDD | Class ownership and a chief-programmer role clash with open-source contribution. | Screened out |
| Agile | DSDM | Enterprise governance overhead. | Screened out |
| Agile | Crystal Clear | Assumes a small co-located team. | Screened out |
| Scaled | SAFe / LeSS / Disciplined Agile | Built for large multi-team enterprises. | Screened out |
| Practice | Release Train | A release-scheduling practice, not a methodology. Covered in 2.1/2.5. | Not a candidate |
| Open-source | Bazaar / OSS model (Raymond, 1999; Mockus et al., 2002) | Describes today's process. | **Baseline only** |

Seven methodologies pass the proof rule (Spiral, Scrum, XP, Kanban, Lean, DevOps, Scrumban), so **2 must be cut** to reach 5.

## Shortlist (agreed: Option A)

**Final shortlist: Spiral, Scrum, XP, Kanban, DevOps, plus the open-source (Bazaar) model as the baseline.**

Options considered:

**Option A (chosen): Spiral, Scrum, XP, Kanban, DevOps, plus the Bazaar baseline**
- **Lean is cut** because it overlaps heavily with Kanban. Kanban is the concrete method built on Lean principles, so Lean is covered as Kanban's foundation (one sentence in 2.3).
- **Scrumban is cut** because both of its parents (Scrum and Kanban) are already shortlisted, and its evidence base is the thinnest of the seven.
- **Spiral is kept** so that the matrix includes one non-agile, risk-driven option. A comparison of agile methods only would look one-sided, and Spiral's risk focus is directly relevant to a finance app.

Option B: Scrum, XP, Kanban, Lean, DevOps. Agile/Lean only, with no plan-driven contrast.

Option C: Spiral, Scrum, Kanban, Scrumban, DevOps. This drops XP, even though XP's engineering practices are the closest match to Actual's current CI and testing culture.

## Open questions

None for planning. Before writing, the authoritative sources for each shortlisted methodology must be found and verified: see `sources.md` section D (S24–S32 are still unverified, and Scrum, XP and DevOps sources are still needed).

## Sources

All sources for this section are logged in `sources.md`: Actual's evidence S01–S12, Scrumban screening S17–S21, Shape Up screening S22–S23, and methodology literature S24–S32 (unverified).
