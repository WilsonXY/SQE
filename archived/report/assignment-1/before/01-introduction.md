# 1 Introduction

## 1.1 Background and purpose

Personal finance applications help people record income, follow spending and plan how to use their money. Their quality matters because incorrect balances or lost records can affect everyday decisions, while exposed transactions can reveal private information. Actual Budget's product statement identifies trust in the numbers and quick completion of routine tasks as measures of success (Actual Budget, 2026a).

I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. Finding it gave me a reason to examine the product more closely through this assignment.

This report evaluates a development methodology, proposes a quality assurance process and integrates independent verification and validation into that methodology. It presents recommendations from an external analysis of public evidence, without contact with Actual's team.

## 1.2 What is Actual Budget?

Actual Budget is a free, open-source personal finance application distributed under the MIT licence. It is local-first: users can work with data on their own devices, with optional server synchronisation. Its default envelope-budgeting approach allocates money already available to spending categories (Actual Budget, n.d.-k, 2026a).

James Long originally developed Actual as a commercial product. In early 2022, he closed the commercial service and made the software open source; a volunteer maintainer team subsequently took responsibility for its development (Aboltins, 2025).

## 1.3 Main features and operation

Actual provides budgets, account registers, transaction rules, scheduled transactions and reports (Actual Budget, n.d.-k). Desktop applications support local use; Docker, PikaPods and Fly.io provide server deployment options. A server enables synchronisation between devices and connections to bank-sync providers (Actual Budget, n.d.-d). Figure 1 separates these optional connections from everyday local budgeting.

**Figure 1. Actual Budget's local-first operation**

```text
Device: local budget and application
                 ↕ optional synchronisation
User-selected server: self-hosted or hosted
                 ↕ optional bank synchronisation
Bank-sync provider
```

*Note.* Author's synthesis of Actual's installation and synchronisation documentation (Actual Budget, n.d.-d, n.d.-i). The server is optional for local desktop budgeting, but required for the connected features shown.

Optional end-to-end encryption protects synchronised budget data. It does not encrypt local device storage or the bank-sync tokens held separately on the server. Therefore, self-hosting gives users control but does not remove their responsibility for protecting devices and credentials (Actual Budget, n.d.-i).

## 1.4 Who is involved?

**Table 1. Stakeholders and quality expectations**

| Stakeholder | Main interest |
|---|---|
| Users and households | Correct figures, privacy and clear daily tasks |
| Self-hosters | Safe upgrades, recoverable data and manageable servers |
| Eight listed core maintainers | Review capacity and sustainable workloads |
| Contributors | Clear expectations and useful feedback |
| Donors and hosting partners | Continued maintenance and dependable operation |

*Note.* Based on Actual's product statement, contributor guide and funding discussion (Actual Budget, n.d.-a, 2026a; youngcw, 2025). The December 2025 roadmap reported over 8,000 PikaPods users whose hosting fees partly supported the project; this is a historical figure.

## 1.5 Main challenges

- Volunteer availability and community requests make review capacity a development constraint, examined in Section 2 (Aboltins, 2025).
- Financial correctness, data protection and accessible interactions require explicit quality priorities, addressed in Section 3 (Actual Budget, n.d.-i, 2026a).
- Encryption has limits; independently checking security and recovery behaviour remains necessary. Section 4 proposes how this checking can fit the development workflow (Actual Budget, n.d.-i).
