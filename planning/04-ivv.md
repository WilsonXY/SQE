# Section 4 — Integrating IV&V with Kanban (10 marks)

Status: **Agreed** (2026-10-21). The flow may still be adjusted during writing.

## What the brief asks

> "To analyse and implement the integration of Independent Verification and Validation (IV&V) processes within the [Selected Methodology] framework to facilitate early defect detection, ensure requirements compliance, and improve overall software quality."

The marker will look for:
1. **Analyse**: what IV&V is, and what Actual has today.
2. **Implement**: a concrete integration *inside Kanban*, not a generic IV&V description.
3. The three goals, each shown explicitly: **early defect detection**, **requirements compliance**, **overall quality**.
4. Critical evaluation.

The selected methodology is **Kanban**, tailored (Section 2).

## Agreed (2026-10-21)

- **Flow 4.1–4.6** (provisional).
- **Phase mapping:** Lecture 6's six phases → six Kanban stages (requirements/triage, design, build/PR, verify, release train, operate/maintain).
- **External audit:** recommend an optional, periodic **funded external security audit** (OSTIF model [S72]). The report must also **briefly state the cost limitation**: Actual is a donation-funded OSS project (about USD 3,000–3,500/month in donations, USD 2,000/month already committed to maintainer stipends [S08]), so an audit depends on donor or third-party funding. The actual cost estimate belongs to Assignment 2.
- **No figure** for Section 4 by default. The author may add one during writing if it really earns its place.
- **No Assignment 1 conclusion** for now (optional; revisit during writing depending on the word count).
- **Independence model (Q2): agreed.** Internal reviews give **technical independence only**. Full independence (technical + managerial + financial) needs **outsiders** (vulnerability reporters, a funded audit). The report must **explain this situation honestly** (e.g. "a maintainer review is not full IV&V in the IEEE sense").
- **Risk tiers (Q3): own design.** The author tried the APU library (2026-10-21). IEEE Xplore returned **"Error 418"** (a block page), and APU's subscription lists **no IEEE Standards** [S74]. So, as agreed beforehand, we **use our own three tiers (high / standard / low), labelled "inspired by IEEE 1012's integrity-level concept"** [S67, abstract only]. We must not present the tiers as IEEE's scheme.
  - Optional later: if the author ever gets IEEE 1012-2024 (e.g. via a librarian), revisit.

## Relevant lecture guidance (not cited)

- **L6:** V vs V; verification activities (code review, unit and integration testing, static analysis, design verification); validation activities (functional testing, requirements validation, regulatory compliance validation, documentation validation).
- **L6 IV&V per phase:** requirements, design, implementation, testing, deployment, maintenance. Each phase has **activities, tools, roles, outcome**.
- **L6 benefits:** early detection, reliability, compliance, objective assessment.
- **L4:** IEEE 1012 / 1059 (now superseded by **IEEE 1012-2024** [S67]).

## Evidence (verified; see `research/` and `sources.md` → D3)

**IV&V concepts:**
- IEEE 1012-2024 is the current V&V standard [S67]. V&V checks conformance to requirements *and* intended use. V&V rigour depends on **integrity levels**.
- Independence has **three dimensions: technical, managerial and financial** [S68, NASA citing IEEE].
- **IV&V in agile:** agile "has in no way diminished the need for IV&V". Security is not easily demonstrable through user-visible behaviour, and IV&V should run "in phase with the development cadence" [S69].

**Kanban mechanism:** "make process policies explicit": **entry and exit criteria** for moving work between board columns [S38, p. 98]. This is where IV&V gates go.

**Independent checking Actual already has (as-is):**
- PR review by another maintainer [S04];
- the 2-maintainer release approval plus smoke test [S03];
- CI checks [S01];
- PR preview builds and nightly builds for community validation [S66];
- **external, non-core reporters who found 1 critical and 2 high vulnerabilities**, through private reporting and coordinated disclosure [S62, S63];
- Actual's coordinated-disclosure process matches what most practitioners recommend, which many OSS projects don't follow (only 55% of vulnerabilities do) [S70].

**Gaps:**
- independence is **ad hoc and mostly after release**: the critical and high flaws reached released versions;
- non-controversial PRs can be merged straight away by one maintainer [S04];
- no risk-based tiering of V&V effort;
- **no evidence of an external security audit** (docs/blog search).

**Real-world proof that IV&V options work:**
- NASA's IV&V Program [S68];
- OSTIF-funded OSS security audits: 24 audits in 2025, 231 findings, over 98% fixed [S72].

## Proposed flow (pending approval)

Same as-is → to-be logic as Sections 2 and 3.

| # | Subsection | Purpose | Main content | ~Words |
|---|---|---|---|---|
| 4.1 | V&V, IV&V and why Actual needs it | Concepts, briefly | V vs V [S67]; three kinds of independence [S68]; integrity levels [S67]; agile still needs IV&V, especially for security [S69]. Why for Actual: financial data, and real escaped vulnerabilities [S63]. | 180 |
| 4.2 | Current V&V in Actual and how independent it is (as-is) | The "analyse" part | Table: each existing V&V activity → who does it → technical / managerial / financial independence (yes / partial / no). Finding: real but ad hoc, and the strongest independence (external reporters) happens **after** release. | 230 |
| 4.3 | IV&V integration model for Kanban (to-be) | The "implement" part: design decisions | (a) **Independence level** Actual can realistically afford: an **internal independent reviewer role** plus **external augmentation** (the existing disclosure channel and an optional funded audit [S72]). (b) **Risk-tiering by integrity level** [S67]: e.g. *high* = authentication/authorization, sync, money calculations, migrations, bank sync; *standard* = UI and copy. (c) **Embedded as Kanban explicit policies** (entry and exit criteria per column) [S38], running in Kanban's cadence [S69]. | 230 |
| 4.4 | IV&V activities across the Kanban workflow | The core table (Lecture 6 format) | One table: Lecture 6's six phases mapped to Kanban stages (requirements/triage → design → build/PR → verify → release train → operate/maintain), with **IV&V activities, tools, independent role, exit criterion** for each. E.g. high-integrity items need an independent reviewer (not the author, not the area owner) using an OWASP ASVS checklist; authorization tests; a threat-model note in the ADR; validation on the preview build; an independent release smoke test; a regression test for every fixed advisory. | 400 (table words count) |
| 4.5 | How the integration achieves the three goals | Show the brief's goals explicitly | **Early defect detection:** e.g. GHSA-m2cq (missing auth middleware) would be caught at the design/PR gate by the ASVS authentication checklist and authorization tests. **Requirements compliance:** traceability chain feature request → acceptance criteria → PR "Fixes #" → tests → release note (Actual already has most links). **Overall quality:** fewer escaped defects; measured in Assignment 2. | 150 |
| 4.6 | Critical evaluation | Where most marks come from | Full IEEE independence (managerial, financial) is not achievable inside a volunteer project. Independence vs flow: extra gates risk recreating the 2022 review backlog [S10] and adding to maintainer burnout [S47], mitigated by tiering and WIP limits. Audit cost vs donations [S08]. Rubber-stamp risk. Tool false positives. | 210 |

Total about **1,400 words** (rebalanced 2026-10-21).

## Explanations for the two pending concept questions

### Q2: Independence model (where the question comes from)

IV&V means *independent* V&V. The standard definition (IEEE, as explained by NASA [S68]) says independence has **three dimensions**, and full IV&V needs all three:

| Dimension | Meaning (paraphrased from S68) | NASA example | What it protects against |
|---|---|---|---|
| **Technical** | The checker is not the developer and uses their own expertise (and ideally their own tools) to judge the work | IV&V analysts who didn't build the software | "Author blindness": people miss their own mistakes |
| **Managerial** | The checker belongs to a *separate organisation* from the developers, and decides what to check, how and when | The NASA IV&V Facility is separate from the project teams | Pressure from the dev team or its managers to skip or soften checks (e.g. to hit a release date) |
| **Financial** | The checker's budget is controlled by someone other than the developers | IV&V is funded separately from the project | Money pressure: "we pay you, so go easy on us" |

Applied to Actual, with evidence:
- **A maintainer reviewing another maintainer's PR:** technically independent (a different person). **Not** managerially independent: same 8-person core team, same leadership, same release goals [S02, S04]. **Not** financially independent: reviewers are paid from the same donation-funded stipend pool, and points are based on lines of code reviewed [S08].
- **Outside vulnerability reporters** (iamsilk, Rex50527, pyuysig [S63]): not part of the team, chose what to examine themselves, not paid by Actual. All three dimensions are satisfied.
- **A funded external audit** (OSTIF model [S72]): a separate organisation with its own audit process. Financial independence depends on who pays (better if a third-party funder pays rather than Actual).

**So the question was:** should the report state honestly that Actual can only achieve *technical* independence internally, and needs *outsiders* for full independence, with the to-be model combining (a) an internal independent-reviewer role, for technical independence, and (b) external parties, for full independence?

**Why this matters for marks:** the brief says "*Independent* Verification and Validation". A marker who knows the IEEE definition would mark down a report that calls a colleague's code review "IV&V" without qualification. Stating the limits is also good material for 4.6 (critical evaluation).

### Q3: Risk tiers / "integrity levels" (what they are)

**The idea:** not every part of a system deserves the same amount of checking. IEEE 1012-2024 handles this with **integrity levels** [S67]:
- each component gets a level based on **how bad it would be if it failed**;
- higher levels get **more and stricter** V&V tasks.

Everyday analogy: a hospital checks heart-surgery equipment far more strictly than the TV in the waiting room.

**For Actual, a possible tiering** (our own proposal, for discussion):

| Tier (proposed) | Example parts of Actual | Why | Extra IV&V (on top of normal review and CI) |
|---|---|---|---|
| **High** | Login, permissions and sessions (sync server); bank-sync endpoints; budget and balance calculations; database migrations; sync/CRDT; encryption | A failure means strangers read bank data (real case: GHSA-m2cq, critical [S63]), wrong money figures, or lost data | An independent reviewer who is not the author and not the area owner; an OWASP ASVS security checklist; authorization and regression tests; a short threat note in the ADR |
| **Standard** | Most features: reports, rules, UI components | A failure is annoying but recoverable | Normal review and CI, plus preview-build validation |
| **Low** | Themes, wording, docs | Cosmetic | Normal review only |

**Benefit:** scarce volunteer reviewing time goes where the risk is, instead of slowing *every* PR (which would recreate the 2022 review backlog [S10]).

**What "we can only cite its abstract" means:**
- The IEEE standard is behind a paywall. We have only read its official abstract, which confirms that V&V requirements are "specified for different integrity levels".
- We do **not** know IEEE's exact level scheme (e.g. how many levels it uses or how they're assigned).
- So the report would say: "inspired by IEEE 1012's integrity-level concept, this report proposes the following tiers for Actual". In other words, our own design, honestly labelled, not presented as IEEE's.
- Alternative: get the full IEEE 1012-2024 text (e.g. through the APU library's IEEE Xplore access, if available) and base the tiers on IEEE's actual scheme.

## How to check IEEE 1012-2024 (for the author)

APU's library announced that it replaced IEEE CSDL with **IEEE Xplore** from 1 January 2022, and IEEE Xplore covers "technical standards" [S73]. Not every IEEE Xplore subscription includes the **standards** collection, so this needs checking.

**Update (2026-10-21):** the library's *APU E-databases* page [S74] says APU's IEEE Xplore subscription includes **only**:
- **POP Online**: conference proceedings from 100 IEEE conference series, back to 2017;
- the **STEM25 Journals Collection**: 25 IEEE journals and magazines.

**It does not list IEEE Standards.** So IEEE 1012-2024 is **probably not accessible**, but a quick search will confirm it.

Steps:
1. Go to https://library.apiit.edu.my/apu-e-databases/ (E-Resources page → the **"APU E-databases"** box). Scroll down to **"IEEE Xplore®"** and click **"Access Here"**. This is the EZproxy link `https://login.ezproxy.apu.edu.my/login?url=https://ieeexplore.ieee.org/`. Log in with your APU account.
2. Open **IEEE Xplore** through the library link, so the university subscription is recognised. The top of the page should show "Access provided by: Asia Pacific University…" (or similar).
3. Search for **"IEEE 1012-2024"** or "IEEE Standard for System, Software, and Hardware Verification and Validation".
4. If the PDF opens (you have access):
   - send it the same way as the other PDFs (it won't be committed);
   - the useful parts are the **integrity level** section (how many levels, how they're assigned: consequence × likelihood?) and the table of **minimum V&V tasks per integrity level**;
   - if it also defines **independence** (technical/managerial/financial), we can cite IEEE directly instead of NASA's summary.
5. If you see "Purchase" or "Sign in to access" instead, the subscription doesn't include standards. Optionally ask the librarians; otherwise we use our own tiers.

## Open questions

None for planning.

## Side benefit of the library check

The same APU E-databases page lists EZproxy access to **ScienceDirect**, **SpringerLink**, **ACM Digital Library** and **IEEE Xplore conference proceedings (POP, from 2017)**. This may let the author:
- read the **full text of S69** (only if EZproxy works; the 2026-10-21 attempt hit IEEE "Error 418") (Smith & Hayes, 2024, IEEE Aerospace Conference), if that conference is in APU's POP package;
- get the **missing article numbers** for S41, S43 and S44 (SpringerLink).
