# 1 Introduction

## 1.1 Background and purpose

Personal finance applications help people record income, track spending and plan how to use their money. Incorrect balances and lost records can affect everyday decisions. Exposed transaction histories can also reveal private information. Actual Budget's product statement measures success through users trusting the figures and completing routine tasks quickly (Actual Budget, 2026a).

I chose Actual Budget because I wanted an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. After finding it, this assignment gave me the opportunity to look at the product in more depth.

The report evaluates a development methodology and proposes a quality assurance process, then integrates independent verification and validation into that methodology. Its recommendations follow an external analysis of public evidence. The analysis involved no contact with Actual's team.

## 1.2 What is Actual Budget?

Actual Budget is a free, open-source personal finance application with an MIT licence. It stores working data on users' devices and supports optional server synchronisation. Its default envelope-budgeting approach allocates money already available to spending categories (Actual Budget, n.d.-k, 2026a).

James Long developed Actual as a commercial product. In early 2022, he closed the commercial service and released the software as open source. A volunteer maintainer team later took responsibility for development (Aboltins, 2025).

## 1.3 Main features and operation

Actual has budgets, account registers, transaction rules, scheduled transactions and reports (Actual Budget, n.d.-k). Its desktop applications support local use. Server options include Docker, PikaPods and Fly.io; a server enables synchronisation across devices and connections to bank-sync providers (Actual Budget, n.d.-d). Figure 1 shows how those optional connections support local budgeting.

**Figure 1. Actual Budget's local-first operation**

```text
Device: local budget and application
                 ↕ optional synchronisation
User-selected server: self-hosted or hosted
                 ↕ optional bank synchronisation
Bank-sync provider
```

*Note.* Author's synthesis of Actual's installation and synchronisation documentation (Actual Budget, n.d.-d, n.d.-i). Local desktop budgeting works without a server. The connected features shown require one.

Users can enable end-to-end encryption for synchronised budget data. The protection excludes local device storage and bank-sync tokens stored separately on the server. Users who self-host control the server but still need to protect their devices and credentials (Actual Budget, n.d.-i).

## 1.4 Who is involved?

**Table 1. Stakeholders and quality expectations**

| Stakeholder | Main interest |
|---|---|
| Users and households | Correct figures, privacy and clear daily tasks |
| Self-hosters | Safe upgrades, recoverable data and manageable servers |
| Eight listed core maintainers | Review capacity and sustainable workloads |
| Contributors | Clear expectations and useful feedback |
| Donors and hosting partners | Continued maintenance and dependable operation |

*Note.* Based on Actual's product statement, contributor guide and funding discussion (Actual Budget, n.d.-a, 2026a; youngcw, 2025). The December 2025 roadmap reported over 8,000 PikaPods users whose hosting fees partly supported the project. That figure describes the position at the time of publication.

## 1.5 Main challenges

- Volunteer availability and community requests constrain review capacity. Section 2 examines this development concern (Aboltins, 2025).
- Section 3 addresses financial correctness, data protection and accessible interactions through explicit quality priorities (Actual Budget, n.d.-i, 2026a).
- Encryption's limits leave security and recovery behaviour needing independent checks. Section 4 proposes how to include these checks in the development workflow (Actual Budget, n.d.-i).
