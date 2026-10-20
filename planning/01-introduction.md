# Section 1 — Introduction (5 marks)

Status: **Agreed.** Only the exact wording of the personal reason and the figure plan are still to confirm.

## Agreed

- 1.6 "Purpose and scope of this report" is **not** its own subsection. It is a short part of 1.1.
- Tone: **dead simple and straightforward.** No showing off. Clean and easy to read.
- Later sections are mentioned only briefly. No detail.
- **Third person only** throughout the report (no "I"/"we").
- **Include the personal reason for choosing Actual**, in third person. The author was looking for an open-source financial management app that could be self-hosted on an old laptop at home to manage and track personal finances. They found Actual Budget, became interested in it, and the assignment gave a chance to look at it in depth.
- **Include a short history:** very brief, two or three sentences at most.
- **Diagrams:** only where they really help the reader. Too many diagrams confuse. Balance matters (see the figure plan in `README.md`).
- 1.4 and 1.5 **stay as separate subsections**.
- Pointing 1.5's challenges to later sections is **nice to have**, not required. Do it lightly.

## Outline

| # | Subsection | What goes in it (plain words) |
|---|---|---|
| 1.1 | Background and purpose of this report | What a personal finance app is and why its quality matters (people's money and data). Why Actual was chosen (the personal reason). One short paragraph on what this report covers: methodology, QA process and IV&V. |
| 1.2 | What is Actual Budget | A free, open-source, local-first budgeting app built around envelope budgeting. A brief history: built as a paid product by James Long, closed and open-sourced in early 2022, now run by a volunteer core team. |
| 1.3 | Main features and how it works | Budgeting, accounts and transactions, rules, schedules, reports, bank sync, syncing across devices, ways to install it. **One simple figure** (proposed): device ↔ optional self-hosted sync server ↔ bank-sync provider. |
| 1.4 | Who is involved | Users, self-hosters, maintainers, contributors, donors/hosting partners. A small table. |
| 1.5 | Main challenges | 3–5 plain bullets. Where it's natural, each one points to the section that handles it (e.g. volunteers and changing requirements → Section 2; "users must trust the numbers" → Section 3; calculation or sync defects → Section 4). |

Word target: about **500–700 words**.

## Proposed wording for the personal reason (please confirm)

> Actual Budget was selected because the author was looking for an open-source personal finance application that could be self-hosted on an old home laptop to manage and track personal finances. Actual Budget met this need, and this assignment provided an opportunity to examine its development in depth.

## Open questions

1. Is the wording above OK? Is "the author" fine as the third-person reference?
2. Is one figure in 1.3 OK (see the figure plan in `README.md`)?

## Evidence

`research/actual-development-process.md`: *Product facts* and *History*.
