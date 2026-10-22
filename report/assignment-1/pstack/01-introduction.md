# 1 Introduction

## 1.1 Background and purpose

Personal finance applications help people record income, track spending and plan how to use their money. Incorrect balances or lost records can affect everyday decisions. Exposed transactions can also reveal private information. Actual Budget's product statement identifies trust in the numbers and prompt completion of routine tasks as measures of success (Actual Budget, 2026a).

I chose Actual Budget while looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. After finding it, I wanted to examine the product more closely through this assignment.

This report evaluates a development methodology, proposes a quality assurance process and integrates independent verification and validation into the selected methodology. The recommendations draw on external analysis of public evidence. The analysis involved no contact with Actual's team.

## 1.2 What is Actual Budget?

Actual Budget is a free, open-source personal finance application distributed under the MIT licence. Its local-first design lets users work with data on their own devices and optionally synchronise through a server. The default envelope-budgeting approach assigns money already available to spending categories (Actual Budget, n.d.-k, 2026a).

James Long developed Actual as a commercial product. In early 2022, he closed the commercial service and made the software open source. A volunteer maintainer team then took responsibility for development (Aboltins, 2025).

## 1.3 Main features and operation

Actual provides budgets, account registers, transaction rules, scheduled transactions and reports (Actual Budget, n.d.-k). Desktop applications support local use. Server deployment options include Docker, PikaPods and Fly.io. The server supports synchronisation between devices and connections to bank-sync providers (Actual Budget, n.d.-d). Figure 1 shows how these optional connections relate to everyday local budgeting.

**Figure 1. Actual Budget's local-first operation**

```text
Device: local budget and application
                 ↕ optional synchronisation
User-selected server: self-hosted or hosted
                 ↕ optional bank synchronisation
Bank-sync provider
```

*Note.* Author's synthesis of Actual's installation and synchronisation documentation (Actual Budget, n.d.-d, n.d.-i). Local desktop budgeting needs no server. The connected features shown require one.

Optional end-to-end encryption protects synchronised budget data. Local device storage and bank-sync tokens held separately on the server remain outside that protection. Self-hosting gives users control over deployment, while responsibility for protecting devices and credentials remains with them (Actual Budget, n.d.-i).

## 1.4 Who is involved?

**Table 1. Stakeholders and quality expectations**

| Stakeholder | Main interest |
|---|---|
| Users and households | Correct figures, privacy and clear daily tasks |
| Self-hosters | Safe upgrades, recoverable data and manageable servers |
| Eight listed core maintainers | Review capacity and sustainable workloads |
| Contributors | Clear expectations and useful feedback |
| Donors and hosting partners | Continued maintenance and dependable operation |

*Note.* Based on Actual's product statement, contributor guide and funding discussion (Actual Budget, n.d.-a, 2026a; youngcw, 2025). The December 2025 roadmap reported over 8,000 PikaPods users. Their hosting fees partly supported the project. That user count is historical.

## 1.5 Main challenges

- Volunteer availability and community requests constrain review capacity. Section 2 examines the implications for development (Aboltins, 2025).
- Financial correctness, data protection and accessible interactions need explicit quality priorities. Section 3 sets out those priorities (Actual Budget, n.d.-i, 2026a).
- Encryption leaves some data outside its protection. Section 4 proposes independent checks of security and recovery behaviour within the development workflow (Actual Budget, n.d.-i).
