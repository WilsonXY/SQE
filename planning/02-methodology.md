# Section 2 — Software Development Methodology (10 marks)

## Writing-thread decision — 22 October 2026

The author approved the revised scores and retained Kanban with mandatory QA gates after considering the quality-focused reassessment. Approved totals out of 120: Kanban 102, DevOps 94, XP 82, Scrum 81, Spiral 72; the existing OSS baseline scores 95 but is not selectable. Original agreed weights are retained. Security, reliability and interaction capability checks are essential requirements before preferences are scored. The 3/5 quality score rates methodology support, not Actual's software quality.

Section 2.4 has been drafted. The complete raw report is frozen under `report/assignment-1/before/`; Humanizer and pstack rewrites use that same input. This is a drafted recommendation, not a claim that Actual adopted it. The older discussion below records planning history; current approved scoring is in `research/methodology-quality-reassessment.md`.

## Author feedback on the Opus 5.5 run-1 raw draft — 24 October 2026

Scope: `writing-experiments/claude-opus-5-5/run-1/raw-revised/document.md` only. The frozen raw draft and the other runs are unchanged.

**Feedback (author):**
- Sentences jump from one point to the next without building context. Readers don't know where the section is going.
- The weighted matrix rests on self-made weights and scores, which feels weak. Drop the numeric weighting and show the selection as a reasoned flow.
- Writing must be grounded: every statement needs enough context and evidence behind it.

**Proposed (applied in the revised draft; author to confirm):**
- Replace C1–C10, the weights and the 1–5 scores with Boehm and Turner's (2004) five home-ground factors [S126]: size, criticality, dynamism, personnel, culture. Table 2.1 profiles Actual qualitatively from cited evidence. Size, dynamism and culture are agile; personnel is agile but strained (few expert reviewers); criticality is mid-scale (financial data, the 2026 advisories). Boehm and Turner's rule that mismatched factors are "sources of risk" needing some disciplined practice is what grounds the mandatory QA gates.
- Derive five needs (N1–N5) from the profile; these replace the criteria.
- Evaluation rule: each candidate's required elements, taken from its defining source, are set against the documented facts about Actual. A contradiction rejects the candidate; an unmet need is a gap for tailoring. Table 2.2 records the conflicts and gaps, with no numbers.
- The outcome is unchanged. Scrum (Sprint commitment and a single Product Owner), XP (sitting together and pairing) and Spiral (expert risk analysis loaded onto the review bottleneck) conflict with Actual. DevOps does not conflict but adds little, because Actual's automation already exists and it runs no operations of its own. Kanban is selected because it targets the review queue, with mandatory QA gates covering criticality.
- Each subsection now opens by linking back to the step before it.
- Song et al. (2024) [S42] and Alaidaros et al. (2021) [S37] are no longer cited.

**Agreed (author, 24 Oct 2026): 2.3 screening simplified.** The longlist paragraph (Waterfall, V-Model, RUP, FDD, Crystal Clear, DSDM, SAFe/LeSS, Shape Up, Lean, Scrumban, release train) read out of context, so it was removed. It is replaced by one sentence explaining that the five candidates each represent a different approach (risk-driven, agile framework, agile engineering, flow management, dev+ops), plus one grounded sentence on why plan-driven methods such as Waterfall were not shortlisted (stable requirements; Boehm & Turner, 2004, p. 31). Singer (2019) [S22] and Meireles et al. (2026) [S18] are no longer cited. The proof rule and the screening table above remain as planning history.

**Open questions:**
- Is the five-factor framework acceptable as the selection basis, or would the author prefer another established framework?
- The document sits at 5,246 of the 5,250 maximum, above the author's preferred "slightly under 5,000". Should other sections be trimmed?
- ~~Should this approach also be carried back into the other runs and the planning matrix files?~~ **Answered 24 Oct 2026:** no. The author is dropping the other versions and will continue from the revised raw document only.
- ~~Word count~~ **Deferred by the author (24 Oct 2026):** don't optimise for length for now; the author will handle it later.

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

Approximate words (rebalanced 2026-10-21 after the executive summary was confirmed to count): 2.1 ≈ 220 · 2.2 ≈ 220 · 2.3 ≈ 270 · 2.4 ≈ 290 (**including the matrix table**) · 2.5 ≈ 190 · 2.6 ≈ 210, about **1,400 in total**.

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
| Agile / Lean | Kanban | Proven. Continuous pull-based flow, WIP limits; "an evolutionary change method" (Anderson, 2010, p. 6, via S38). | Passes the proof rule |
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

None for planning.

## Matrix placement (agreed 2026-10-20, under the appendix rule)

- **The scored matrix itself goes in the body**: 6 options (5 candidates + baseline) × 10 criteria, with weights and totals, as one compact table.
- **The reasons for the decisive scores** go in the body text, e.g. C2 volunteers, C7 overhead, C8 flow.
- The appendix holds at most an optional **FYI** cell-by-cell note.
- **Words in tables count** towards the word limit, so the table stays compact: numbers plus short labels. The ~300-word budget for 2.4 must include it.

## Sources (verified 2026-10-20; full details in `sources.md`)

| Use | Sources |
|---|---|
| Actual as-is evidence (2.1) | S01–S12 (all live URLs checked). Optional: S15 for the history. |
| Root and golden source per candidate | Spiral S26 · Scrum S34 · XP S35 · Kanban S28 · DevOps S30 · OSS baseline S24, S25 · Lean (as Kanban's foundation) S29 |
| Recent evidence (2021+) | S36 Kuhrmann et al. 2022 (hybrids are common; practices matter more than methods → supports tailoring) · S37 Kanban review 2021 · S39 DevOps review 2023 · S41 CI review 2022 · S42 multi-criteria methodology selection 2024 (**supports the weighted matrix**) · S43 GitHub Actions 2023 · S47 LF maintainers report 2023 (volunteer constraints, burnout, automation) · S40 DORA 2024 (four keys; unstable priorities → burnout) |
| Golden evidence for Kanban | S38 Ahmad et al. 2018. Benefits and challenges tables. Conclusion: Kanban "is a relatively basic flow tool that needs to be supported by additional practices", which **directly justifies tailoring Kanban with Actual's CI and testing practices** in 2.5. |
| Screening only | Scrumban S18 (recent) · Shape Up S22, S23 |

Still to do before writing: see `sources.md` → section D.
