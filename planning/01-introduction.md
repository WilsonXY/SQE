# Section 1 — Introduction (5 marks)

Status: **In discussion**

## Agreed

- 1.6 "Purpose and scope of this report" is **not** its own subsection. It is a short part of 1.1.
- Tone: **dead simple and straightforward.** No showing off. Clean and easy to read.
- It briefly says what later sections cover. No detail.

## Proposed outline (pending approval)

| # | Subsection | What goes in it (plain words) |
|---|---|---|
| 1.1 | Background and purpose of this report | What a personal finance app is and why its quality matters (it handles people's money and data). Then one short paragraph: this report looks at Actual Budget's development methodology, QA process and IV&V. |
| 1.2 | What is Actual Budget | A free, open-source, local-first budgeting app built around envelope budgeting. Who made it and who maintains it now (a community). |
| 1.3 | Main features and how it works | Budgeting, accounts and transactions, rules, schedules, reports, bank sync, syncing across devices, ways to install it. Possibly one very simple diagram (device ↔ optional sync server ↔ bank-sync provider). |
| 1.4 | Who is involved | Users, self-hosters, maintainers, contributors, donors/hosting partners: a small table or one paragraph. |
| 1.5 | Main challenges | 3–5 plain bullets. Each challenge points to the later section that deals with it, e.g. volunteers and changing requirements → Methodology; "users must trust the numbers" → QA; bugs in financial calculations or sync → IV&V. |

Word target: about **500–700 words**.

## Open questions

1. **Person and voice:** third person only ("This report…"), or is first person ("I chose…") acceptable to your lecturer?
2. **Why Actual was chosen:** the brief says to pick a product "based on interest, relevance". Include one or two lines on your personal reason?
3. **History:** include a short history (originally built by James Long, then open-sourced and community-run)? The date and commercial history still need verifying from an external source.
4. **Diagram in 1.3:** yes or no? It might go against "stupidly simple", but one picture can explain local-first and sync faster than text.
5. **1.4 and 1.5:** keep them as two subsections, or merge 1.3–1.5 so the intro has fewer headings?
6. **Signposting challenges to later sections (1.5):** happy with this idea?

## Evidence

See `research/actual-development-process.md` → *Product facts*.
