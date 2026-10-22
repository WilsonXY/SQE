# 1 Introduction

## 1.1 Background and Purpose

Personal finance applications help people record spending and plan a budget. Their quality matters because they hold balances, transactions and sometimes bank connections. A wrong total can lead to a poor financial decision, and a security flaw can expose private data.

I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. Once I had found Actual Budget and become interested in it, this assignment gave me the chance to examine it in depth.

The report takes the view of outside analysts and covers three topics. Section 2 selects a software development methodology for the project. Section 3 sets out a quality assurance (QA) process. Section 4 integrates independent verification and validation (IV&V) into the selected methodology.

## 1.2 What Is Actual Budget

Actual Budget ("Actual") is a free, open-source personal finance application released under the MIT licence. It is local-first. The budget stays on the user's own device, and syncing between devices is optional (Actual Budget, 2026a). It targets privacy-minded budgeters, self-hosters and families, and defines success as users trusting its numbers (Actual Budget, 2026a). By default, Actual uses envelope budgeting, where people budget the money they already have, not income they expect to receive (Actual Budget, n.d.-k).

James Long created Actual and ran it as a paid product for over four years (Stacoviak & Santo, 2022). In early 2022 he closed the commercial product and released it as open source (Aboltins, 2025). Volunteers now maintain it, led by a core team that formed after pull requests had waited months for review (Aboltins, 2025).

## 1.3 Main Features and How It Works

Actual covers budgeting, accounts and transactions, rules, scheduled transactions and reports (Actual Budget, n.d.-k). It runs as a desktop app, through Docker, or on paid hosting from PikaPods or Fly.io (Actual Budget, n.d.-d).

Basic budgeting needs no server, but syncing between devices and bank synchronisation both need one (Actual Budget, n.d.-d). Users can optionally turn on end-to-end encryption for synced data, but it leaves data on the local device unencrypted and does not cover bank-sync tokens on the server (Actual Budget, n.d.-i). Figure 1 shows how the parts connect.

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

- **Volunteer capacity and changing requirements.** Work depends on volunteers, and review has been a bottleneck before (Aboltins, 2025). Section 2 addresses how the project organises work.
- **Trust in the numbers and data security.** Users rely on correct figures and protected data (Section 3).
- **Escaped defects and security flaws.** Problems found after release harm users (Section 4).

<!-- Cited: S01, S02, S08, S10, S11, S15, S51, S121, S122 -->
