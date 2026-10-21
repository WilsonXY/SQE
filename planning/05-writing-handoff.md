# Assignment 1 — Writing Handoff

Prepared 2026-10-21, at the end of the planning thread. **A new writing thread starts here.**

Planning for Assignment 1 is complete: Sections 1–4 are all **Agreed**. This file collects everything needed to write the report. It summarises; the detailed decisions live in the per-section planning files.

## 0. Start-of-thread checklist (for the writing assistant)

1. Read `AGENTS.md` (rules: push to `main`, don't assume, citations, recency, appendices).
2. Read this file in full.
3. Before writing a section, read:
   - its planning file (`01-introduction.md`, `02-methodology.md`, `03-quality-assurance.md`, `04-ivv.md`);
   - the matching parts of `research/actual-development-process.md`;
   - the `sources.md` entries it uses.
4. Check `README.md` → *Pending follow-ups* for anything that changed (e.g. IEEE 1012 access).
5. Follow the per-section workflow in §6.

## 1. Report structure (Assignment 1)

Delivered as a **PDF**, formatted as a business report (brief → Deliverables).

| Part | Status / owner | Notes |
|---|---|---|
| Cover / title page | **Author handles it** (APU template `Assignment/Assignment_1_-Cover_-_2026.docx`) | Not part of the writing work |
| Executive summary | **Required by the brief.** Write it **last**. **Counts towards the word limit.** | ~200 words, one page. See §1.1 |
| Table of contents; list of figures; list of tables | Generated at final assembly | — |
| List of abbreviations | Optional | Useful: SQA, IV&V, V&V, CI, PR, WIP, CVD, E2EE, OSS, ASVS, WCAG, CRDT |
| 1 Introduction | Agreed | `01-introduction.md` |
| 2 Software Development Methodology | Agreed | `02-methodology.md` |
| 3 Quality Assurance Process | Agreed | `03-quality-assurance.md` |
| 4 Integrating IV&V with Kanban | Agreed | `04-ivv.md` |
| (5 Conclusion) | **Excluded for now** | Revisit only if the word count allows |
| References | Built at the end | APA 7; **only works cited in the text** |
| Appendices | Only if needed | **FYI only: not marked, not counted.** At most an optional per-score note for the Section 2 matrix |

### 1.1 Executive summary vs introduction

The two are **not interchangeable**:
- the brief lists "an executive summary page" separately from the report body;
- they do different jobs.

| | Executive summary | Introduction |
|---|---|---|
| Purpose | The **whole report in brief**, *including results*: chosen methodology and why, key QA findings and recommendations, the IV&V approach | **Sets up** the topic: what Actual is, why it matters, what the report will cover. **No results.** |
| Reader | A busy reader who reads only this page | Every reader, before the body |
| When to write | **Last** | First |
| Marked? | Not a marked criterion, but required by the brief | Yes (5 marks) |

**It counts towards the ~5,000 words** (author's decision, 2026-10-21). Budget: about **200 words**.

## 2. Word budget (agreed)

- Target: **~5,000 ± 5% (4,750–5,250)**. The author **prefers slightly under 5,000**.
- **Words in tables count.** Appendices don't count.

| Part | Budget | Sub-budgets |
|---|---|---|
| Executive summary | ~200 | Counts towards the limit; written last |
| 1 Introduction | ~530 | 1.1–1.5 (no fixed split) |
| 2 Methodology | ~1,400 | 2.1 220 · 2.2 220 · 2.3 270 · 2.4 290 (incl. matrix) · 2.5 190 · 2.6 210 |
| 3 QA Process | ~1,400 | 3.1 170 · 3.2 270 · 3.3 270 · 3.4 270 · 3.5 250 (incl. QA plan table) · 3.6 170 |
| 4 IV&V | ~1,370 | 4.1 170 · 4.2 220 · 4.3 220 · 4.4 400 (incl. table) · 4.5 150 · 4.6 210 |
| **Total** | **~4,900** | Within 4,750–5,250, slightly under 5,000 as preferred |

## 3. Writing rules (all agreed)

**Voice and tone:**
- **Third person** throughout.
  - **Only exception:** the personal-reason sentence(s) in 1.1 use **"I"**.
- The Introduction must be **dead simple and straightforward**: no showing off, and only a brief mention of what later sections cover.

**Argument:**
- Every section needs **critical evaluation**, not just description (brief: "critically evaluate").
- **Point of view: outside analysts** recommending; no contact with the Actual team.
- Methodology and practices recommended must be **existing and proven in real-world use**, with citable evidence.
- **No hybrid methodology.** Kanban is selected and **tailored** (keeps Actual's CI and testing practices), justified by S38 and S36.

**Structure and length:**
- **Tables:** compact (words count).
- **Figures** (planned; few and useful):
  - Fig 1 in 1.3: how Actual works (device ↔ optional self-hosted sync server ↔ bank-sync provider);
  - Fig 2 in 2.1: as-is workflow;
  - Fig 3 in 2.5: to-be Kanban workflow.
  - **No figures in Sections 3 and 4** by default; the author may add one if it really earns its place.
- **Appendices:** FYI only. Never move essential content there.

**Citations** (`AGENTS.md` → *Citations and sources*):
- **APA 7th**, author–date in text, e.g. (Aboltins, 2025), Aboltins (2025), (Ahmad et al., 2018, p. 105).
- Direct quotes go in quotation marks with a page or paragraph number. Paraphrase by default.
- **Every factual claim about Actual** is cited to its source (S-ID → APA reference).
- **Recency:** prefer 2021+. Older sources are allowed only if they are a **root** or **golden** source. Never cite *Old*-tagged sources.
- **Only cite what has actually been read** (at least the abstract or official page). Several items are only "details verified" (see §5).
- **Lecture slides are not cited.**
- Never commit the PDFs the author supplies.

**Open for the writing thread to settle with the author:**
- **Spelling convention:** British or American English? Pick one and keep it consistent. *Suggestion:* British English, which is common at Malaysian universities, but **ask the author**.

## 4. Section briefs

### Section 1 — Introduction (~530 words) · `01-introduction.md`

- **1.1 Background and purpose:**
  - what personal finance apps are and why their quality matters (money and data);
  - the **personal reason, in "I"**. Agreed direction: *"I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and keep track of my finances. After discovering Actual Budget and becoming interested in it, this assignment gave me the opportunity to examine it in depth."* Final wording is decided at writing time;
  - one short scope paragraph (methodology, QA, IV&V).
- **1.2 What is Actual Budget:**
  - free, open-source (MIT), local-first, envelope budgeting [S01];
  - users and "users trusting the numbers" [S01 `PRODUCT.md`];
  - **history in 2–3 sentences**: built by James Long as a paid product; "early 2022" closed and open-sourced; now a volunteer core team [S10]. Optional support: [S15].
- **1.3 Features and how it works:**
  - budgeting, accounts and transactions, rules, schedules, reports, bank sync, multi-device sync;
  - **optional end-to-end encryption** [S51];
  - install options: PikaPods, Fly.io, Docker, desktop apps [S01];
  - **Figure 1.**
- **1.4 Who is involved** (small table): users, self-hosters, 8 core maintainers [S02], contributors, donors/hosting partners (Open Collective [S08], PikaPods with over 8,000 users [S11]).
- **1.5 Main challenges** (3–5 plain bullets). Lightly point each to the section that handles it:
  - volunteers and changing requirements → S2;
  - "trust the numbers" and data security → S3;
  - escaped defects and security flaws → S4.
- **Pre-writing checks:** none blocking. Optionally re-check the install options and feature list against the current docs.

### Section 2 — Methodology (~1,400 words) · `02-methodology.md`

- **2.1 As-is:**
  - "a **defined workflow but no deliberate methodology**";
  - voting backlog → PR → CI → review → merge → **monthly release train** (cut on the 25th, ≥2 approvals, smoke test);
  - feature flags; paid review stipends;
  - the 2022 review backlog [S10];
  - evidence: [S01–S08, S10, S11].
  - **Figure 2.**
- **2.2 Criteria:**
  - C1–C10 with weights (table in `02-methodology.md`), drawn from goals, constraints, risks and stakeholders plus Lecture 2's factors;
  - supports: [S42] (multi-criteria decision-making for methodology selection), [S47] (volunteer maintainer constraints and burnout).
- **2.3 Candidates:**
  - a short longlist screening, including the **proof rule** (Shape Up dropped, no peer-reviewed evidence [S22, S23]; Scrumban cut [S18]);
  - the **shortlist: Spiral [S26], Scrum [S34], XP [S35], Kanban [S28, S38, S37], DevOps [S30, S39, S40]**;
  - **baseline: OSS/Bazaar model [S24, S25]** (scored, not selectable);
  - Release Train = a practice, not a candidate [S32].
- **2.4 Evaluation and selection:**
  - the **scored matrix in the body** (6 × 10, weights, totals);
  - reasons for the decisive scores;
  - Kanban is the **working hypothesis, which the scoring must actually test**.
- **2.5 To-be:** Kanban tailored to Actual (explicit policies [S38], WIP limits, flow, keeping CI and tests). **Figure 3.** Section 4 builds on this.
- **2.6 Critical evaluation:** Kanban's challenges [S38 Table 14, S37]; "relatively basic flow tool" [S38]; hybrid reality [S36]; when the choice would stop fitting.
- **⚠ Not yet agreed: the actual matrix scores (1–5).** The writing thread must **propose the scores with one-line justifications and get the author's approval before drafting 2.4.**
- **Pre-writing checks (sources):**
  - **S35 XP:** read Ch. 7 *Primary Practices* before citing practice details (only the TOC and Ch. 1 have been read). The author may need to supply that chapter.
  - **S24 Raymond:** content not read. Read the relevant part before citing any claim (e.g. "release early, release often"). The essay is online at catb.org, which wasn't reachable from the research environment.
  - **S26 Boehm, S30 *Accelerate*, S34 Scrum Guide:** check at least the sections used. S34 was partly read.
  - **S28 Anderson:** cite via S38 ("as cited in"), or the author checks p. 6 directly.
  - Article numbers for **S41, S43, S44** (SpringerLink).

### Section 3 — QA Process (~1,400 words) · `03-quality-assurance.md`

- **3.1 Quality for Actual:** views of quality applied (L1 guidance, not cited); "users trusting the numbers" [S01].
- **3.2 Attributes:**
  - rate all **9 ISO/IEC 25010:2023** characteristics [S53] in one compact table;
  - deep-dive the top 4–5: functional suitability (calculation correctness), reliability (data integrity, sync), **security (top priority** [S63]**)**, maintainability, interaction capability (incl. inclusivity/accessibility);
  - ISO/IEC 25059 (AI) is out of scope.
- **3.3 As-is QA and gaps:**
  - existing practices [S01, S03, S09, S50, S51, S62];
  - gaps, stated as "**no evidence found in the repository (October 2026)**": coverage measurement (disabled in sync-server), automated accessibility testing, performance testing in CI, a written QA plan, **proactive pre-release security verification**;
  - advisories as evidence: e.g. **GHSA-m2cq-xjgm-f668 (critical, CVSS 9.2, missing authentication on bank-sync endpoints)** [S63]. Use maintainer severities and GitHub publish dates;
  - the security policy's broken link (404) [S62].
- **3.4 Selection (option B):**

  | Standard / framework | Decision |
  |---|---|
  | ISO/IEC 25010:2023 [S53] | Adopt |
  | IEEE 730-2014 [S54] | Adapt (SQAP structure) |
  | **ISO 9001:2026** [S55] (not the lecture's 2015 edition) | Reject certification; borrow principles |
  | ISO/IEC 27001:2022 [S57] | Reject certification; borrow principles |
  | CMMI V3.0 [S56] | Reject appraisal |
  | OWASP ASVS 5.0.0 [S58] | Adopt |
  | **WCAG 2.2** [S59] (Actual targets 2.1) | Adopt |
  | OpenSSF Best Practices Badge + Scorecard [S60] (Actual has neither) | Adopt |
  | ISO/IEC/IEEE 29119 [S61] | Mainly for Section 4 |

- **3.5 Apply:** a **compact QA plan table in the body**, structured by the L3/IEEE 730 SQAP sections and built into the Kanban columns (**Definition of Done**, quality gates, roles, defect and vulnerability handling).
- **3.6 Critical evaluation:** volunteer cost and limits; automation overhead (CI and bots can slow PRs [S43]; bots also help [S44]); remaining gaps.
- **Pre-writing checks:**
  - **verify the exact names of the 9 ISO/IEC 25010:2023 characteristics** from an authoritative source (currently derived from the official scope [S53] plus a secondary summary [S65]);
  - read the OpenSSF badge criteria page [S60] and the ASVS chapter names [S58] before referring to specific requirements;
  - optionally run Lenarduzzi et al. (2021) and Hendrick & Ramaswami (2023) through the verify and log process if they're useful (they're in the search log, not yet evaluated).

### Section 4 — IV&V with Kanban (~1,370 words) · `04-ivv.md`

- **4.1 Concepts:**
  - V&V definition [S67, IEEE 1012-2024 abstract; 2016 superseded];
  - **three kinds of independence** (technical, managerial, financial) [S68];
  - integrity levels [S67];
  - agile still needs IV&V, especially for security [S69].
- **4.2 As-is independence table:** maintainer review (technical only); 2-maintainer release approval [S03]; CI; preview and nightly builds [S66]; **external reporters iamsilk, Rex50527, pyuysig (all three kinds of independence)** [S63]; CVD good practice [S70, S62]; **no evidence of an external audit**.
- **4.3 Model:**
  - an internal independent-reviewer role (technical independence) **plus** external augmentation (CVD channel, an optional funded audit [S72]);
  - **explain honestly** that a maintainer review is not full IV&V;
  - **risk tiers high / standard / low** = **our own design**, labelled "inspired by IEEE 1012's integrity-level concept" [S67];
  - embedded as **Kanban explicit policies (entry/exit criteria)** [S38, p. 98], in Kanban's cadence [S69].
- **4.4 Main table (Lecture 6 format):** six phases → six Kanban stages (requirements/triage, design, build/PR, verify, release train, operate/maintain), each with **activities, tools, independent role, exit criterion**.
- **4.5 Three goals:**
  - early defect detection (e.g. GHSA-m2cq would be caught at the design/PR gate);
  - requirements compliance (traceability: request → acceptance criteria → PR "Fixes #" → tests → release note);
  - overall quality (fewer escaped defects; measured in Assignment 2).
- **4.6 Critical evaluation:**
  - full managerial and financial independence is impossible internally;
  - independence vs flow (the 2022 backlog [S10], burnout [S47]);
  - **audit cost limitation for a donation-funded OSS project** (about USD 3,000–3,500/month in donations, USD 2,000 committed to stipends [S08]). The cost is estimated properly in Assignment 2;
  - rubber-stamp risk; tool false positives.
- **Pre-writing checks:**
  - S69 full text (blocked by IEEE Error 418);
  - S70 volume/issue/article number;
  - if IEEE 1012-2024 becomes available, revisit the tiers.

## 5. Source readiness summary (see `sources.md` for details)

| Ready to cite (read/verified) | Details verified only: read before citing specifics | Do not cite |
|---|---|---|
| S01–S12, S15, S25, S34 (partly), S36–S44, S47, S50–S52, S55, S57–S63, S65 (secondary), S66–S70, S72 | S24, S26, S28 (use via S38), S30, S35 (beyond Ch. 1), S53 (characteristic names), S54, S56, S61, S73/S74 (internal only) | S13, S14, S16, S19–S21, S23, S45, S46, S48, S71 (unless read), all *Old* entries |

## 6. Per-section workflow in the writing thread

1. **Source check:** clear that section's pre-writing checks (§4). Log every new source in `sources.md` immediately.
2. **Settle remaining detail decisions with the author before drafting.** For example: Section 2 matrix scores, the spelling convention, final table layouts.
3. **Draft** into `report/assignment-1/NN-section-name.md` (one Markdown file per section, e.g. `01-introduction.md`). Use in-text APA citations, and keep a list of the S-IDs actually cited at the bottom of each draft file, to build the References later.
4. **Word count** (including tables) against §2. Report it to the author.
5. **Author review → revise.**
6. **Update status** in the section's planning file and `README.md` ("Drafted" → "Final"), add a `discussion-log.md` entry, and **push to `main`**.
7. When all sections are final:
   - write the **executive summary**;
   - build **References** (`report/assignment-1/references.md`) from the cited S-IDs only, in APA 7 order;
   - final assembly into the author's chosen format, then **PDF**. **Format/tool to be decided with the author** (e.g. Word with the APU cover, or Markdown → PDF).

**Suggested order:** Section 1 (sets the style) → 2 → 3 → 4 → executive summary → references.

## 7. Suggested opening message for the writing thread

> Read `AGENTS.md` and `planning/05-writing-handoff.md`, then let's start writing Assignment 1 Section 1 (Introduction). Follow the per-section workflow in the handoff.
