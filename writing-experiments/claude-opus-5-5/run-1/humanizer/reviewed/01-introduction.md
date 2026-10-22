# 1 Introduction

## 1.1 Background and Purpose

Personal finance applications help people record spending and plan a budget. They hold balances, transactions and sometimes bank connections, so a wrong total can lead to a poor financial decision and a security flaw can expose private data.

I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and keep track of my finances. I came across Actual Budget, became interested in it, and this assignment gave me the opportunity to examine it in depth.

The report takes the view of outside analysts. Section 2 selects a software development methodology for the project, Section 3 sets out a quality assurance (QA) process, and Section 4 integrates independent verification and validation (IV&V) into the selected methodology.

## 1.2 What Is Actual Budget

Actual Budget ("Actual") is a free, open-source personal finance application released under the MIT licence. It is local-first: the budget is kept on the user's own device, and syncing between devices is optional (Actual Budget, 2026a). It targets privacy-minded budgeters, self-hosters and families, and defines success as users trusting its numbers (Actual Budget, 2026a). By default, Actual uses envelope budgeting, in which people budget the money they already have rather than income they expect to receive (Actual Budget, n.d.-k).

Actual was created by James Long, who ran it as a paid product for over four years (Stacoviak & Santo, 2022). In early 2022 he closed the commercial product and released it as open source (Aboltins, 2025). Volunteers now maintain it. Their core team formed after pull requests had waited months for review (Aboltins, 2025).

## 1.3 Main Features and How It Works

Actual covers budgeting, accounts and transactions, rules, scheduled transactions and reports (Actual Budget, n.d.-k). It runs as a desktop app, through Docker, or on paid hosting from PikaPods or Fly.io (Actual Budget, n.d.-d).

A server is not required for basic budgeting, but syncing between devices and bank synchronisation both need one (Actual Budget, n.d.-d). Users can turn on end-to-end encryption for synced data. It does not cover data on the local device or bank-sync tokens on the server (Actual Budget, n.d.-i). Figure 1 shows how the parts connect.

```text
+----------------+   optional sync (E2EE optional)   +----------------+
|  User device   | <-------------------------------> |  Sync server   |
|  local budget  |                                   |  (self-hosted  |
|  works offline |                                   |   or hosted)   |
+----------------+                                   +----------------+
                                                             |
                                                             v
                                                     +----------------+
                                                     |  Bank-sync     |
                                                     |  provider      |
                                                     +----------------+
```

*Figure 1. How Actual Budget works (based on Actual Budget, n.d.-d).*

## 1.4 Who Is Involved

*Table 1.1. Main stakeholders of Actual Budget.*

| Stakeholder | Role and interest |
|---|---|
| Users | Need correct figures and private data |
| Self-hosters | Run their own server and need it secure |
| Core maintainers | Eight listed main contributors who review and release (Actual Budget, n.d.-a) |
| Contributors | Volunteers who choose their own work (Actual Budget, n.d.-a) |
| Donors and hosting partners | Fund the project through Open Collective (Actual Budget, n.d.-f); PikaPods reported over 8,000 users in December 2025 (youngcw, 2025) |

## 1.5 Main Challenges

- Work depends on volunteer capacity, requirements keep changing, and review has been a bottleneck before (Aboltins, 2025). Section 2 deals with how work is organised.
- Users rely on correct figures and on the security of their financial data (Section 3).
- Defects and security flaws that escape into a release harm users (Section 4).

<!-- Cited: S01, S02, S08, S10, S11, S15, S51, S121, S122 -->
