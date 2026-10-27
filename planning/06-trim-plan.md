# Assignment 1 — Trim Plan (word-count review)

Prepared 2026-10-27. **Status: Proposed. Nothing has been applied yet.** The author decides item by item.

## 1. The problem in numbers

Counted on `report/assignment-1/report.md` as it stood at commit `a2e48a9`. The count includes headings, captions, tables and in-text citations. It excludes the References list, the HTML source comments and the three ASCII figures (about 220 words).

| Part | Now | Target | Cut needed |
|---|---|---|---|
| Executive summary | 189 | ~180 | ~10 |
| 1 Introduction | 549 | ~520 | ~30 |
| 2 Methodology | 2,759 | ~1,650 | **~1,100** |
| 3 QA Process | 2,072 | ~1,450 | **~620** |
| 4 IV&V | 1,700 | ~1,330 | **~370** |
| **Total** | **~7,270** | **~5,000** (4,750–5,250; author prefers slightly under 5,000) | **~2,250** |

Section 2 holds 38% of the words but earns the same 10 marks as Sections 3 and 4.

**About the figures.** Figure 3 is really a table drawn as a figure (column | exit policy). Figures are not counted above. If the final PDF shows Figure 3 as a real table, count its ~95 words. Moving text into figures to save words is not part of this plan.

## 2. Rules for this trim

- Cut what the reader doesn't need: repetition, recaps of earlier sections, tutorial background, definitions of basic terms, and detail the argument never uses.
- Don't compress sentences into shorthand. Every sentence that stays must still make sense to a fresh, technical reader.
- Keep the evidence behind every claim that stays.
- Keep everything the brief marks: Section 2's selection and critical evaluation, Section 3's meaning of quality and critical evaluation, and Section 4's three goals.

## 3. Biggest source of waste: the same thing said in several places

| Repeated content | Where it appears now | Proposal: keep it in | Elsewhere |
|---|---|---|---|
| CI checks list (lint, type-check, unit, E2E, visual, CodeQL) | 2.1, Figure 2, 3.3, Table 4.1 | **3.3** (the QA as-is) and Figure 2 | 2.1 just says "automated checks (CI)" |
| Release train detail (25th, two approvals, smoke test) | 2.1, Figure 2, Table 2.1, 3.3, Figure 3, Table 4.1 | **Figure 2** and Table 4.1 | 2.1 keeps one clause; 3.3 drops it |
| GHSA-m2cq story (SimpleFIN/Pluggy missing auth, GoCardless had it) | 2.2, 3.2, **3.3**, 3.5 example, 4.1, **4.3** | **3.3** (full); 3.5 example (applies the plan) | 4.3 refers back and covers only what the independent review adds |
| Kanban board explained column by column | 2.5 bullets, Figure 3, 3.5 opening paragraph, Table 4.2 | **Figure 3** | 2.5 bullets and the 3.5 recap go |
| "What Kanban changes" (visible queue, WIP limit, written rules) | 2.4 Kanban paragraph, 2.5 "Compared with today" | **2.4** | 2.5 paragraph goes |
| Volunteer capacity (stipend pool, months-long review backlog, burnout) | 1.2, 1.5, 2.1, Table 2.1, Table 2.2, 2.6, 3.4, 3.6, Table 4.1, 4.2 | **2.1** (stated once with evidence) | Later sections say "review time is scarce (Section 2.1)" instead of citing all three again |
| "Evidence is public only; private checks may exist" | 3.3, 3.6 | **3.3** | 3.6 sentence goes |
| "How independently a change is checked depends on who reviews it" | end of 4.1, start of 4.2, 4.3 overall-quality paragraph | **4.1** | 4.2 and 4.3 just point back |

## 4. Itemised proposals

**A** = safe: removes repetition, recaps, roadmap lists or generic background. The reader loses nothing.
**B** = judgement: removes content that has some value. The author decides.

### Executive summary and Section 1 (~40 words)

| # | Where | Proposal | Type | Saves |
|---|---|---|---|---|
| 1-1 | 1.1, "After discovering Actual Budget and becoming interested in it, this assignment gave me…" | Shorten to "This assignment gave me the opportunity to examine it in depth." This also fixes a dangling modifier: the assignment didn't discover Actual. | A | ~10 |
| 1-2 | 1.2–1.5 | Leave as they are. They are within budget and introduce the facts later sections rely on. | — | 0 |
| ES-1 | Executive summary | Revisit last, after the body is settled. Each sentence should match a finding that survives the trim. | A | ~10–25 |

### Section 2 (~1,100 words)

| # | Where | Proposal | Why | Type | Saves |
|---|---|---|---|---|---|
| 2-1 | Section intro | Keep the one-line definition of methodology. Replace the six-part roadmap "(2.1)…(2.6)" with one sentence: as-is, then needs, then candidates and selection, then the to-be and its limits. | Roadmap duplicates the headings | A | ~45 |
| 2-2 | 2.1 paragraphs 2–3 | Remove the definition of a pull request (basic term). Remove the feature-flags sentence (never used again). Replace the CI test list with "automated checks (CI), including tests and CodeQL security scanning"; the full list is in 3.3. Cut the release-train detail to one clause; Figure 2 shows the steps. | Repetition; basic term; unused detail | A | ~110 |
| 2-3 | 2.2 lead-in | Remove "rather than the report's own scoring" (left over from the old scoring matrix). Remove the inline list of the eight factors; Table 2.1's first column lists them. Keep the agile/linear explanation the last column needs. | Leftover; repetition | A | ~50 |
| 2-4 | Table 2.1 | Shorten the Size and Team expertise cells to the fact and its source. Keep every row and the "Points to" column. | Verbose cells | A | ~40 |
| 2-5 | Paragraph after Table 2.1 | Keep the two exceptions (expertise and risk) with their evidence, but don't restate what the table rows already say. | Repeats table | A | ~45 |
| 2-6 | "Because the factors do not all point the same way…" paragraph | Fold into one sentence leading to Table 2.2: agile at the core, with written controls where expertise and risk leave it exposed. | Says one point in three sentences | A | ~40 |
| 2-7 | Table 2.2 and lead-in | Shorten the "Why Actual needs it" cells where Table 2.1 already gave the reason (rows 1–2). Keep the new reasons in rows 3–5 (team change, burnout, risk). Keep the "Brief's lens" column: it shows the marker the brief's four lenses. | Repeats Table 2.1 | A | ~50 |
| 2-8 | Table 2.3 | Drop the "Commonly suited to" and "Main drawback" columns. They are generic tutorial content; the argument uses only Spiral's drawback, which 2.4 cites directly. This also removes the empty DevOps row ("Not covered… / —"). | Tutorial content (problem area 3) | A | ~60 |
| 2-9 | 2.3 screening paragraph and Table 2.3 lead-in | Tighten. Keep why Waterfall/V-Model and RAD/RUP were left out, and why Spiral was kept. | Wordy | A | ~45 |
| 2-10 | 2.3 bazaar paragraph | Replace with one sentence: today's process stays in Table 2.4 as a reference point, so that a change must beat the status quo. Drop the "bazaar" label and its two citations. **Raymond (2000) and Mockus et al. (2002) would leave the References**; neither is cited anywhere else. | The label is never used again | B | ~40 |
| 2-11 | 2.4 clash/gap definitions | Tighten. Keep both definitions and the fairness rule ("none is credited for what Actual already does"). | Wordy | A | ~35 |
| 2-12 | 2.4 Kanban paragraph | Keep why Kanban wins: it is the only candidate that targets the review bottleneck. Shorten the "three things" list, then delete 2.5's "Compared with today, three things change" paragraph, which repeats it. | Repetition | A | ~90 |
| 2-13 | 2.4 DevOps and "Finally" paragraphs | Tighten. Keep the status-quo comparison and the reason for mandatory QA gates. | Wordy | A | ~45 |
| 2-14 | 2.5 six-column bullet list | Delete. Figure 3 shows the same six columns with their exit policies, and the column names explain themselves. Keep the paragraph defining exit policy. | Repeats Figure 3 | A | ~90 |
| 2-15 | 2.5 WIP paragraph | Remove the lead-time and cycle-time definitions; metrics belong to Assignment 2. Keep "set the limit from the reviews maintainers actually complete" and the monthly review point. | Out of focus | A | ~30 |
| 2-16 | 2.6 | Light tightening only. This is the marked critical evaluation. | — | A | ~20 |
| 2-17 | Tables 2.3 + 2.4 | **Merge into one table**: Candidate · What it requires of the team · Clash with Actual · Requirement left uncovered. Table 2.4's clash column already restates Table 2.3's "requires" column. 2.3 keeps only its screening prose. | Two tables doing one job | B | ~60 |
| 2-18 | Tables 2.1 + 2.2 | **Optional, bigger:** add a last column "So the methodology must…" to Table 2.1 and drop Table 2.2. The **cost** is losing the Brief's lens column and the burnout and team-change reasons, which have no row in Table 2.1. Recommended only if the total is still over after everything else. | Two tables doing one job | B | ~110 |

Items 2-1 to 2-17 save about 1,000. Add 2-18 to reach about 1,100.

### Section 3 (~620 words)

| # | Where | Proposal | Why | Type | Saves |
|---|---|---|---|---|---|
| 3-1 | Section intro | Keep the QA definition. Cut the roadmap as in 2-1. | Duplicates headings | A | ~50 |
| 3-2 | 3.1 | Keep all of Garvin, because the brief marks "the meaning of quality when applied to software". Shorten the transcendent sentence and the manufacturing bullet. Cut the stakeholder paragraph to its last sentence ("protect financial data without stalling a volunteer workflow"); Table 1.1 already gives each stakeholder's interest. | Repeats Table 1.1 | A | ~65 |
| 3-3 | 3.2 bullets | Remove the "…yet no X was found" endings; 3.3 states the gaps. In the Reliability bullet, "yet test coverage of this code is not measured" doesn't follow from the password-loss sentence before it, so it is a logic slip as well as a repeat. | Repetition; non sequitur | A | ~30 |
| 3-4 | 3.3 opening paragraph | Keep as the one place that lists the CI checks (see Section 3). Drop the release-approval sentence; it is in 2.1 and Table 4.1. | Repetition | A | ~20 |
| 3-5 | 3.3 security and reliability bullets | Tighten. Keep GHSA-m2cq in full here (this becomes its one full telling), the authorisation test matrix definition, the counter-overflow example and the coverage caveat. | Wordy | A | ~35 |
| 3-6 | "Performance tests are also absent from CI…" | Delete. The section has already said it covers three attributes only. | Out of focus | A | ~25 |
| 3-7 | 3.4 Table 3.1 and the two bullets after it | Keep one or the other, not both. **Decided 2026-10-27: keep Table 3.1 and drop the bullets.** The two reasons the bullets carry (ASVS's authentication, session and authorisation chapters match the 2026 flaws; W3C says 2.2 does not deprecate 2.1) move into the table's cells in short form, so the evidence stays. | The bullets repeat the table | B | ~40 |
| 3-8 | 3.4 "Section 3.3 found four gaps…" paragraph and the two-tests lead-in | Tighten. Keep: reliability needs a setting, not a standard; the QA plan gap is filled by 3.5. | Wordy | A | ~50 |
| 3-9 | 3.5 opening paragraph | Remove the recap of the board (columns, cards, exit policies), which 2.5 and Figure 3 already give. Keep "the QA plan adds its checks to the exit policies, so quality is checked as work moves". | Recap | A | ~65 |
| 3-10 | 3.5 second paragraph and Table 3.2 | Tighten the reading guide and the longer cells (Operate/maintain row). Keep all rows and columns. | Wordy | A | ~45 |
| 3-11 | 3.5 worked example | Keep (the author asked for it). Light trim only. | — | A | ~20 |
| 3-12 | 3.6 | Point back to 2.1 for the stipend pool, backlog and burnout instead of citing all three again. Delete the "evidence is public only" sentence, which repeats 3.3. **The author said they would simplify 3.6 themselves**, so this is only a suggestion. | Repetition | A | ~65 |
| 3-13 | Risk tiers used before they are defined | "High-tier" first appears in Table 3.1 (3.4) and Table 3.2 (3.5), but the tiers are defined in 4.2. A fresh reader meets the term two sections early. Options: (a) define the three tiers in 3.5, where the QA plan first relies on them, and have 4.2 refer back; or (b) define them briefly in 2.5 at triage. Either way the words move rather than grow. | Reader flow, not word count | — | 0 |

Items 3-1 to 3-12 save about 620.

### Section 4 (~370 words)

| # | Where | Proposal | Why | Type | Saves |
|---|---|---|---|---|---|
| 4-1 | Table 4.1 "Performed by" cells | Shorten, e.g. the PR review cell to "Another core maintainer (cite)". | Wordy | A | ~15 |
| 4-2 | Paragraph after Table 4.1 | Remove the sentence restating the table (no managerial or financial independence). Keep "ad hoc and mostly technical" and "the strongest findings came after release, from outsiders". The reporters' GitHub handles could become "three reporters outside the core team". | Repeats table | A/B | ~35 |
| 4-3 | 4.2 opening | Replace the restatement of 4.1 with a short link ("To make independence depend on risk, not chance, the model makes three changes."). | Repetition | A | ~20 |
| 4-4 | 4.2 outside-checks paragraph | Keep OSTIF and one figure that shows it works (over 98% of findings fixed). Drop the 24-audits and 10-funders figures. | Detail the argument doesn't use | B | ~20 |
| 4-5 | 4.2 exit-policy paragraph and Table 4.2 | Tighten. The "threat note" is a new concept used in one cell; fold it into the design note from Table 3.2 and drop its definition. Shorten the Verify row (the longest cell in the report) and the Build/PR row, which repeats Table 3.2. | One-use concept; repetition | B | ~80 |
| 4-6 | 4.3 lead-in | Cut to one sentence naming the three goals. Remove the preview of which evidence each paragraph uses. | Meta | A | ~40 |
| 4-7 | 4.3 early detection | Don't retell the flaw; it is in 3.3. Don't re-walk the columns; that is the 3.5 worked example. Keep only what IV&V adds: two independent checks (Design and Verify) and why the second matters (an implementer who forgets the login check may forget the test too). | Repeats 3.3 and 3.5 | A | ~65 |
| 4-8 | 4.3 requirements compliance | Light trim. Keep the "feel fast" example. | — | A | ~20 |
| 4-9 | 4.3 overall quality | Don't restate the 4.1 finding and the tiers; point back. Keep the regression-test feedback loop. | Repetition | A | ~35 |
| 4-10 | Section 4 has no introduction | Sections 2 and 3 open with a short introduction; Section 4 starts straight at 4.1. Consider a one- or two-sentence opener (~30 words) for consistency. | Consistency | — | +30 |

Items 4-1 to 4-9 save about 330, or about 300 if 4-10 is added.

## 5. Where this lands

| | Words |
|---|---|
| Now | ~7,270 |
| After all **A** items | ~5,450 |
| After **A** + 2-10, 2-17, 3-7, 4-4, 4-5 (**B**) | ~5,200 |
| After also 2-18 and final line-level tightening while applying | **~4,950–5,050** |

The estimates are rough (±10% per item). The real number is measured after each section is applied.

## 6. Small accuracy slips found during this read (not word-count items)

- 3.3 says "Pluggy AI", while 4.3 says "Pluggy.ai". Use the advisory's spelling, "Pluggy AI", in both (4.3 may lose the name anyway under 4-7).
- 4.3's "six endpoints" is backed by the research notes (`research/actual-development-process.md`, m2cq entry). No change needed. If 4-7 keeps a count, 3.3 is where it belongs.

## 7. Suggested order of work

1. Author agrees or rejects each item (A items can be approved as a block).
2. Apply Section 2 first (largest cut), measure, report.
3. Then Section 3, then Section 4, then 1.1 and the executive summary.
4. After each section: log in `discussion-log.md`, update `sources.md` if a citation leaves the References, commit and push.
