# Section 2 — Software Development Methodology (10 marks)

Status: **In discussion**

## Agreed

- Candidates are **not** limited to the common list (Waterfall, V-Model, Spiral, RAD, RUP, Scrum, Kanban, XP). Less mainstream methodologies can be candidates too.
- Selection is based on **how effective the methodology would be for this project**, not on how popular or widely accepted it is.
- The section starts from **Actual's current (as-is) development workflow**, then asks: *if a proper methodology were adopted, which would suit Actual best, given its goals, constraints, risks and stakeholders?*

## Verified finding: the as-is state

Actual does **not** follow a named methodology. It **does** have a clear, documented, heavily automated workflow:

- **Prioritisation:** voting-based feature backlog.
- **Work allocation:** none. Volunteers choose their own work.
- **Delivery:** pull requests, CI, peer review and feature flags.
- **Release:** an automatic monthly release train, cut on the 25th, needing 2 maintainer approvals and a smoke test.
- **Funding:** a paid review stipend.

Full evidence and sources: `research/actual-development-process.md`.

So "no methodology" is true. "No process" would be **false**. The report should say: *there is an emergent process but no deliberate methodology*.

## Proposed flow (pending approval)

The logic runs: **what they do → what the project needs → what options exist → which fits best → how it would work → honest limits.**

| # | Subsection | Purpose | Main content |
|---|---|---|---|
| 2.1 | Current development process of Actual (as-is) | Ground the section in evidence | How work flows today: idea or vote → issue/PR → CI → review → merge → monthly release. A workflow figure. Conclusion: no deliberate methodology, an emergent OSS process. |
| 2.2 | Project characteristics and selection criteria | Turn the brief's four lenses into criteria | Goals, constraints, risks and stakeholder expectations (the brief's own words), plus the 8 selection factors from Lecture 2. These give a short list of criteria, with weights if we keep the matrix. |
| 2.3 | Candidate methodologies | Show the options considered | A longlist covering plan-driven, agile/lean and less-common methods. A quick screening removes the clearly unfit ones, with one line each on why. A shortlist of about 4–6 gets a short description each. |
| 2.4 | Evaluation and selection | Make the choice traceable | Compare the shortlist against the criteria (matrix or table), pick one, and justify it against goals, constraints, risks and stakeholders. |
| 2.5 | Applying the methodology to Actual (to-be) | Show it is practical, not just theory | Roles, cadence, artefacts and workflow under the chosen methodology. What changes compared with today. A figure. This is also what Section 4 (IV&V) builds on. |
| 2.6 | Critical evaluation | Where most marks come from | Strengths, weaknesses, risks, mitigations, and the conditions under which this choice would stop being right. |

Approximate words: 2.1 ≈ 250 · 2.2 ≈ 250 · 2.3 ≈ 300 · 2.4 ≈ 300 · 2.5 ≈ 200 · 2.6 ≈ 250, about **1,500 in total**.

## About the "scoring matrix"

A **weighted decision matrix**, also called multi-criteria decision analysis:

1. Take the criteria from 2.2, e.g. "copes with changing requirements" or "works with volunteers who can't commit time".
2. Give each criterion a weight for how important it is to Actual, e.g. 1–3.
3. Score each shortlisted methodology 1–5 on each criterion.
4. Multiply each score by its weight and add them up. The highest total is the most suitable.

**Why use it:** it makes the choice *traceable* (criteria → scores → decision) rather than "I like Kanban", which suits "select, justify, critically evaluate".
**Weakness:** the scores are subjective. Each important score needs a sentence of justification, or it looks made up. The full matrix could go in an appendix, with a summary in the body.
**Alternative:** a qualitative comparison table with good/partial/poor ratings and reasons. It is less numeric and easier to defend.

## Candidate longlist (draft, for discussion)

| Family | Methodology | First impression for Actual |
|---|---|---|
| Plan-driven | Waterfall | Likely screened out. Requirements change constantly through votes, and releases are monthly. |
| Plan-driven | V-Model | Likely screened out as a methodology because it is too rigid. Its V&V pairing is still useful for Section 4. |
| Plan-driven | Incremental | Generic. Partly matches feature flags. |
| Risk-driven | Spiral (Boehm) | Interesting because financial data integrity is high-risk. Heavy risk analysis each loop may not suit volunteers. |
| Plan-driven / iterative | RUP | Likely screened out: heavy roles and artefacts. |
| Agile | Scrum | Needs committed teams, a product owner and sprints. Volunteers can't commit. Should still be evaluated on its merits. |
| Agile | Extreme Programming (XP) | Engineering practices (CI, tests, small releases, collective ownership) already match well. Pair programming and an on-site customer don't. |
| Agile / Lean | Kanban | Continuous pull-based flow, no fixed roles or iterations. Close to how Actual already works. |
| Agile / Lean | Scrumban | A Scrum/Kanban hybrid. |
| Lean | Lean Software Development (Poppendieck) | Principles: eliminate waste, build quality in, deliver fast, decide late, respect people. A strong fit for a small, time-poor team. |
| Agile | Feature-Driven Development (FDD) | Probably screened out: class ownership and a chief-programmer role clash with open-source contribution. |
| Agile | DSDM | Probably screened out: enterprise governance overhead. Its MoSCoW prioritisation is useful. |
| Agile | Crystal Clear | Probably screened out: assumes a small co-located team. |
| Product-cycle | **Shape Up** (Basecamp, Singer 2019) | Interesting: fixed time, variable scope; "appetite"; a betting table instead of a backlog; cool-down periods. Its weakness is that it expects dedicated teams for 6-week cycles. |
| Open-source | **Open-source ("Bazaar") development model** (Raymond 1999; Mockus et al. 2002) | The "native" model: release early and often, peer review, self-selected work. Arguably what Actual already does. |
| Practice set | DevOps / Continuous Delivery | More a culture and practice set than an SDLC. Probably a complement, not a candidate. |
| Practice | Release Train (as used in Firefox/Chrome rapid release) | Actual's monthly cut already is one. Probably a component, not a candidate. |
| Scaled | SAFe / LeSS / Disciplined Agile | Screened out: built for large enterprises with many teams. |

**Current leaning (not decided, to be tested by 2.2–2.4):** a **hybrid**, probably Kanban/Lean flow plus XP engineering practices plus a monthly release train. Shape Up and the Bazaar model are the most interesting challengers.

## Open questions

1. **Flow 2.1–2.6:** happy with this order? Note that 2.6 is now a separate subsection, so Section 2 has six subsections instead of five.
2. **Framing:** the as-is finding is "a well-defined workflow but no deliberate methodology". Agree with this wording, rather than "no proper workflow"?
3. **Scoring matrix:** keep the weighted matrix (with justification and the full version in an appendix), or use a qualitative comparison table?
4. **Hybrid allowed?** The brief says "the most appropriate software development methodology" (singular). Is a hybrid acceptable to your lecturer, or must we name one base methodology (e.g. "Kanban, tailored with XP practices")?
5. **Longlist:** anything to add or remove? Should DevOps and Release Train count as candidates or as supporting practices?
6. **Shortlist size:** 4–6 shortlisted methods, with one-line screening for the rest. OK?
7. **Should "keep the current Bazaar model" be a candidate?** If it scores highest, the conclusion becomes "formalise what Actual already does". That is a valid but less exciting answer.
8. **Point of view:** is the report written as if *we* were Actual's maintainers adopting the methodology, or as an outside analyst recommending one? This also affects Assignment 2 (estimation and the risk plan).
