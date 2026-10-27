# Software Quality Engineering Evaluation of Actual Budget: Methodology, Quality Assurance and IV&V

*Working title; cover page, table of contents and lists are added at final assembly.*

# Executive Summary

This report evaluates Actual Budget, a free, open-source, local-first personal finance application run by a small volunteer team. Its users need to trust the numbers it shows and the security of their financial data.

Actual has a defined workflow but no deliberate methodology. Judged against standard methodology selection factors, Actual suits an agile approach, except that its few reviewers are overloaded and its defects can affect users' money and data. Of five candidates, Kanban fits best because it directly limits the review backlog. Mandatory quality gates are added because Kanban itself prescribes no quality practices.

The QA process focuses on three ISO/IEC 25010:2023 characteristics: Security, Reliability and Interaction capability. Public evidence shows gaps in proactive security verification, coverage measurement and accessibility testing. The proposed QA plan adopts OWASP ASVS 5.0.0 and WCAG 2.2 and writes its quality checks into the exit policy of each Kanban stage, scaled by risk.

IV&V adds risk-tiered independent review inside the team and external checks through coordinated disclosure and an optional funded audit. Internal review gives technical independence only, and volunteer time and donation funding remain the main limits.

# 1 Introduction

## 1.1 Background and Purpose

Personal finance applications help people record spending and plan a budget. Because they hold balances, transactions and sometimes bank connections, their quality matters: a wrong total can lead to a poor financial decision, and a security flaw can expose private data.

I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and keep track of my finances. After discovering Actual Budget and becoming interested in it, this assignment gave me the opportunity to examine it in depth.

Written from the view of outside analysts, this report covers three topics. Section 2 selects a software development methodology for the project, Section 3 sets out a quality assurance (QA) process, and Section 4 integrates independent verification and validation (IV&V) into the selected methodology.

## 1.2 What Is Actual Budget

Actual Budget ("Actual") is a free, open-source personal finance application released under the MIT licence. It is local-first: the budget is kept on the user's own device, and syncing between devices is optional (Actual Budget, 2026a). It targets privacy-minded budgeters, self-hosters and families, and defines success as users trusting its numbers (Actual Budget, 2026a). By default, Actual uses envelope budgeting, in which people budget the money they already have rather than income they expect to receive (Actual Budget, n.d.-k).

Actual was created by James Long, who ran it as a paid product for over four years (Stacoviak & Santo, 2022). In early 2022 he closed the commercial product and released it as open source (Aboltins, 2025). It is now maintained by volunteers, led by a core team that formed after pull requests had waited months for review (Aboltins, 2025).

## 1.3 Main Features and How It Works

Actual covers budgeting, accounts and transactions, rules, scheduled transactions and reports (Actual Budget, n.d.-k). It runs as a desktop app, through Docker, or on paid hosting from PikaPods or Fly.io (Actual Budget, n.d.-d).

A server is not required for basic budgeting, but syncing between devices and bank synchronisation both need one (Actual Budget, n.d.-d). Users can optionally turn on end-to-end encryption for synced data, but data on the local device stays unencrypted and bank-sync tokens on the server are not covered (Actual Budget, n.d.-i). Figure 1 shows how the parts connect.

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

- **Volunteer capacity and changing requirements.** Work depends on volunteers, and review has been a bottleneck before (Aboltins, 2025). Section 2 addresses how work is organised.
- **Trust in the numbers and data security.** Users rely on correct figures and protected data (Section 3).
- **Escaped defects and security flaws.** Problems found after release harm users (Section 4).

<!-- Cited: S01, S02, S08, S10, S11, S15, S51, S121, S122 -->

# 2 Software Development Methodology

A software development methodology, also called a software process model, is a framework describing the activities performed at each stage of a software development project. This section recommends one for Actual. Because a methodology can only be judged against the project it must serve, the section first describes how Actual works today (2.1) and what kind of project it is (2.2). It then introduces five candidate methodologies (2.3), tests them against Actual's needs and selects one (2.4), shows how the choice would work in practice (2.5) and examines its weaknesses (2.6).

## 2.1 Current development process of Actual (as-is)

Actual's contributor documentation does not name any methodology (no evidence found, October 2026). It does, however, describe the same route for every change, shown in Figure 2.

Work starts from users' requests. Feature requests are automatically labelled "needs votes", so the list of planned work is in effect ranked by the number of votes each request receives (Actual Budget, 2026a). Nobody is assigned to a request; contributors choose what they want to work on (Actual Budget, n.d.-a, n.d.-e). A contributor submits a change as a pull request (PR), which asks for the change to be merged into the project's main code on GitHub. Small changes go straight to a PR, while larger features are discussed in an issue first (Actual Budget, n.d.-a).

Every PR then passes two checks. First, continuous integration (CI) automatically builds the code and runs linting, type-checking, unit, end-to-end and visual tests, together with CodeQL security scanning (Actual Budget, 2026a). Second, a core maintainer reviews the change and may merge it straight away if it is uncontroversial (Actual Budget, n.d.-e). Large features are merged behind feature flags, so that they can ship in small parts as experimental features that users choose to switch on (Actual Budget, n.d.-b). Finally, merged work reaches users through a monthly release train. On the 25th of each month a release branch is cut automatically from whatever is ready, two other maintainers approve it, and smoke tests run before the release is announced (Actual Budget, n.d.-c).

The step that has caused trouble is review. Only maintainers can approve a PR, and the project lists eight of them (Actual Budget, n.d.-a). After Actual became open source in 2022, PRs waited months because nobody was available to review them (Aboltins, 2025). The project now pays maintainers for review and triage from a USD 2,000 monthly pool funded by donations (Actual Budget, n.d.-f), which shows that review time is its scarcest resource.

Actual therefore has **a defined workflow but no deliberate methodology**. The steps are clear, but nothing manages how work moves through them. In particular, nothing limits how many PRs can pile up waiting for the few people able to review them.

```
Feature request --> "needs votes" backlog (ranked by votes)
                           |
  small change             | larger feature: issue discussion first
        \                  v
         +--------> Pull request
                           |
                           v
          CI: lint, typecheck, unit, E2E, visual, CodeQL
                           |
                           v
          Maintainer review --> merge (feature flag if large)
                           |
                           v
          Monthly release cut (25th, 17:00 UTC)
                           |
                           v
          >=2 other maintainers approve --> tag and publish
          --> smoke test --> announce
```

*Figure 2. Actual's as-is development workflow (compiled from the sources cited in 2.1).*

## 2.2 Project characteristics and selection criteria

To choose fairly between methodologies, Actual's situation must first be described against established selection factors rather than the report's own scoring. This report uses the eight factors commonly considered when selecting a software process model: project requirements, size and complexity, flexibility and adaptability, customer involvement, risk tolerance, time constraints, team expertise and regulatory compliance (GeeksforGeeks, 2025). Each factor points either to an iterative, agile model, suited to changing requirements and close customer involvement, or to a linear model such as Waterfall, suited to stable requirements, fixed deadlines and predictability. Table 2.1 applies the factors to Actual; the last column shows which kind of model each factor points to.

*Table 2.1. Actual against the selection factors.*

| Factor | Actual | Points to |
|---|---|---|
| Project requirements | Evolving: new requests arrive continuously and are re-ranked by users' votes (Actual Budget, 2026a) | Agile |
| Size and complexity | A small team of eight core maintainers plus volunteers (Actual Budget, n.d.-a). The common rule favours Waterfall for small projects only when requirements are straightforward, which Actual's are not | Agile |
| Flexibility and adaptability | Priorities shift with votes, and each monthly release ships whatever is ready (Actual Budget, n.d.-c) | Agile |
| Customer involvement | Users shape the work continuously through requests and votes (Actual Budget, 2026a) | Agile |
| Risk tolerance | Low: defects can mislead money decisions and expose financial data (Actual Budget, 2026c) | Linear |
| Time constraints | A fixed monthly release date, but no feature is promised for it (Actual Budget, n.d.-c) | Agile |
| Team expertise | Cross-functional: any contributor may work on any issue, and volunteers choose their own work rather than being assigned roles (Actual Budget, n.d.-a, n.d.-e). The few experienced reviewers are already overloaded (Aboltins, 2025) | Agile, but under strain |
| Regulatory compliance | No regulatory requirements found in Actual's documentation (October 2026) | No constraint |

Most factors point clearly to an agile model, but two need explanation. On team expertise, agile models need an experienced, self-disciplined team (GeeksforGeeks, 2025). Actual has such people, but they are few, they are volunteers, and their review time has already run out once. On risk tolerance, low tolerance and a need for predictability favour linear models (GeeksforGeeks, 2025). Actual's defects cannot endanger anyone's safety, but a wrong balance can lead a household to a poor spending decision, and in 2026 a critical security flaw allowed anyone to read users' bank balances and transactions without logging in (Actual Budget, 2026c). Actual therefore cannot accept much risk.

Because the factors do not all point the same way, no single model fits Actual unchanged. The same guidance recommends considering models that combine elements of different approaches to meet a project's specific needs (GeeksforGeeks, 2025). For Actual, this means an agile model at its core, with stricter, written controls added where team expertise and risk tolerance leave it exposed.

Five requirements follow from this profile. Table 2.2 lists them, with the reason Actual needs each one and the part of the brief it answers: Actual's goals, constraints, risks or stakeholder expectations. Section 2.4 tests every candidate against these requirements.

*Table 2.2. Requirements for Actual's methodology.*

| Requirement | Why Actual needs it | Brief's lens |
|---|---|---|
| Handles changing priorities | Users' votes re-rank the work continuously (project requirements, flexibility) | Stakeholder expectations |
| Works with self-chosen tasks | Volunteers choose their own work and cannot be assigned it (team expertise) | Constraints |
| Keeps its rules written down | Actual's core team has changed over time (Aboltins, 2025), so practices held only in people's heads would be lost (team expertise) | Risks |
| Protects review time | Reviewers are the bottleneck, and maintainers link administrative overload to burnout (Salkever, 2023, pp. 26–27) (team expertise) | Constraints, risks |
| Includes quality and risk controls | Defects affect money and private data (Actual Budget, 2026c), and low risk tolerance calls for the predictability of a more structured process (risk tolerance) | Goals, risks |

## 2.3 Candidate methodologies

Many methodologies exist, so the comparison focuses on five established ones, each representing a different approach. Linear models such as Waterfall and the V-Model were not shortlisted, because they suit well-defined, stable requirements and leave little room for change (GeeksforGeeks, 2025), whereas Actual's requirements change with every vote. RAD and RUP were also set aside, because both are organised around planned phases and deliverables that assume a team that can be scheduled, whereas Actual's volunteers choose their own work. Spiral is included although it is not agile, because risk tolerance is the one factor on which Actual leans away from agile methods.

Table 2.3 summarises what each candidate requires of a team, because Section 2.4 compares those demands with how Actual works. It also gives the situations each is commonly suited to and its main drawback (GeeksforGeeks, 2025).

*Table 2.3. Candidate methodologies.*

| Candidate | Approach | What it requires of the team | Commonly suited to | Main drawback |
|---|---|---|---|---|
| Spiral | Risk-driven | Repeated cycles, each starting with expert analysis of the largest remaining risk | High-risk projects | Complex; may require expertise |
| Scrum | Agile framework | Sprints of up to one month, a Sprint goal the team commits to, a single Product Owner who orders the work, a daily 15-minute meeting | Projects with a clear product backlog | Challenging for large teams |
| XP | Agile engineering | Weekly planning, test-first development, pair programming, a team that sits together | Rapidly changing requirements (as an agile method) | Needs an experienced, self-disciplined team |
| Kanban | Flow management | A visible board, work-in-progress (WIP) limits and written rules for moving work, applied on top of an existing process | Continuous delivery; efficient workflow management | Limited for large, complex projects |
| DevOps | Development and operations | Shared responsibility and automation across building and running the software | Not covered in the common comparison | — |

Actual's current way of working is also kept in the comparison as a reference point. It follows the open-source "bazaar" model, in which many volunteers contribute openly with little central planning (Raymond, 2000; Mockus et al., 2002). It is not a candidate, because the aim is to improve on it, but comparing against it shows whether a change would actually be better than today.

## 2.4 Evaluation and selection

Each candidate is now compared with how Actual works, using the requirements in Table 2.2. The comparison can produce two kinds of finding:

- a **clash**, where the methodology demands something Actual cannot provide. A clash rules the candidate out, because removing it would mean abandoning the methodology itself;
- a **gap**, where the methodology does not cover one of the requirements. A gap does not rule a candidate out, because a missing practice can be added.

Every candidate is assumed to keep Actual's existing automated checks, review and monthly release, so none is credited for what Actual already does. Table 2.4 summarises the findings, and the paragraphs that follow explain them.

*Table 2.4. Clashes and gaps for each candidate.*

| Candidate | Clash with how Actual works | Requirement left uncovered (gap) |
|---|---|---|
| Spiral | Needs expert risk analysis every cycle from the overloaded reviewers | Handles changing priorities |
| Scrum | Needs a committed Sprint goal and a single Product Owner | Protects review time |
| XP | Needs developers working side by side at the same time | Includes quality and risk controls (security, accessibility) |
| **Kanban** | None found | Includes quality and risk controls |
| DevOps | None found | Protects review time |
| Current process (reference) | None | Protects review time; includes quality and risk controls |

First, three candidates clash with how Actual works. Scrum and XP both assume team members who commit their time together. Scrum's Sprint Goal "is a commitment by the Developers" and its Product Owner "is one person, not a committee" (Schwaber & Sutherland, 2020), while XP's pair programming needs two developers available at once, even when pairs work remotely (Beck & Andres, 2005). Actual's volunteers choose their own work and cannot promise to be available together, and its priorities come from users' votes, so neither assumption holds.

Spiral fits Actual's low risk tolerance best, because every cycle starts with risk analysis. That analysis, however, needs expert judgement (Boehm, 1988), which is why Spiral is usually described as complex and expertise-dependent (GeeksforGeeks, 2025). In Actual the experts are the same few maintainers whose review time is already the bottleneck.

Next, Kanban and DevOps have no clash, so the question becomes which would add more to what Actual already does. DevOps mainly adds automated testing throughout delivery (DORA, n.d.), which Actual's CI already provides, and integration with operations, which has little to attach to because users run the server themselves or through a hosting provider (Actual Budget, n.d.-d). Neither of these addresses Actual's real bottleneck: human review.

Kanban, in contrast, fixes the problem identified in Section 2.1: nothing currently limits how many PRs wait for review. It adds three things. First, Kanban limits work in progress (WIP), the number of items allowed in a stage at once (Kanban University, n.d.). This report proposes placing that limit on the review stage, where Actual's bottleneck lies: once the limit is reached, no new PRs enter review until waiting ones are cleared, which protects the maintainers' review time. Second, the rules for moving work from one stage to the next are written down, so they do not depend on who happens to be on the team. Third, contributors still pick tasks from the voted backlog whenever they have time, so nobody has to commit to a fixed amount of work as Scrum would require.

Finally, Kanban has to be better than simply keeping today's process. The gain is modest but real: Actual's process already suits volunteers, and Kanban adds a review limit and written rules on top of it rather than replacing it. Kanban does, however, leave one requirement unmet. It does not say how quality should be checked, for example which tests a change must pass, and this matters because Actual's risk tolerance is low (Table 2.1). The report therefore adds **mandatory quality gates (QA gates)**: checks, defined in Section 3, that every change must pass before it moves to the next stage. **The selected methodology is Kanban, tailored with mandatory QA gates.**

## 2.5 Applying Kanban to Actual (to-be)

In practice, Kanban would be added on top of Actual's existing route rather than replacing it (Kanban University, n.d.). Figure 3 shows the proposed board. Each column is a stage that work passes through, and each has an **exit policy**: a written condition that must be met before work can be pulled into the next column (Ahmad et al., 2018, p. 98).

Each piece of work, such as a bug fix or a new feature, is a card that moves left to right through six columns:

- **Requirements/triage:** the request is recorded and its risk is assessed.
- **Design:** the author decides how to build it.
- **Build/PR:** the author writes the code and opens a pull request, and the automated tests (CI) run.
- **Verify:** another maintainer reviews the pull request.
- **Release train:** approved work goes out in the monthly release.
- **Operate/maintain:** users run the release, and their bug and security reports feed back into triage.

The Verify column, where review happens, carries the WIP limit. The limit should be set from the number of reviews the maintainers actually complete, tracked through process metrics such as lead time (from request to delivery) and cycle time (from commit to release), so that new work stops entering once reviews start to pile up. Section 3 adds quality checks for security, reliability and interaction capability to the exit policies, and Section 4 adds independent checks to each column. The monthly release stays as it is, and each release becomes the point at which the team checks whether the limits and policies need adjusting.

Compared with today, three things change: the review queue becomes visible on the board, the number of PRs waiting for review is limited, and the conditions for moving work forward are written down and mandatory.

```
Rule: pull work only when the next column is under its WIP limit
+------------------------+------------------------------------------------+
| Column                 | Exit policy (pull criterion)                   |
+------------------------+------------------------------------------------+
| 1 Requirements/triage  | Problem, acceptance criteria and risk recorded |
| 2 Design               | Approach agreed; decision record if high-risk  |
| 3 Build/PR             | CI green; tests and release note included      |
| 4 Verify   [WIP limit] | Reviewer is not the author; QA gate passed     |
|                        | (Security, Reliability, Interaction capability)|
| 5 Release train        | Monthly cut (25th); >=2 approvals; smoke test  |
| 6 Operate/maintain     | User reports and advisories triaged to col. 1  |
+------------------------+------------------------------------------------+
        ^                                                      |
        +------------------- feedback loop --------------------+
```

*Figure 3. Proposed (to-be) Kanban workflow for Actual with explicit exit policies.*

## 2.6 Critical evaluation

Kanban's main weakness is that it manages flow but does not improve quality by itself. It is "a relatively basic flow tool that needs to be supported by additional practices" (Ahmad et al., 2018, p. 110), which is why the QA gates are mandatory. Teams also report difficulty setting it up, adapting their culture and training people (Ahmad et al., 2018, p. 106).

The WIP limit is also weaker in a volunteer project. It cannot force anyone to review, and blocked PRs may discourage newcomers (Salkever, 2023). It should therefore act as a signal rather than a hard block, with the paid review pool (Actual Budget, n.d.-f) directed at review.

The evidence has limits too. The selection factors come from a practitioner tutorial (GeeksforGeeks, 2025), and Table 2.1 relies on qualitative judgement because Actual publishes no data to measure them. No study shows Kanban improving a project like Actual, so its benefit is plausible but unproven. Tailoring it is still reasonable, since few projects follow any methodology in pure form (Kuhrmann et al., 2022).

Finally, the choice should be revisited if Actual gains paid staff, which would make Scrum's commitments realistic, or runs its own hosted service, which would give DevOps operations to integrate.

<!-- Cited: S01, S02, S03, S04, S07, S08, S10, S25, S26, S34, S36, S38, S47, S105, S108, S109, S121, S123, S128, S63-m2cq -->

# 3 Quality Assurance Process

Quality assurance (QA) is the planned set of activities that gives confidence that software meets its requirements, by putting suitable processes, procedures and standards in place and making sure they are followed. This section designs a QA process for Actual. It first sets out what quality means for Actual (3.1) and which quality attributes matter most (3.2). It then compares current practice with those attributes to find the gaps (3.3), selects standards and practices to close them (3.4), builds the resulting plan into the Kanban workflow from Section 2 (3.5) and examines the plan's weaknesses (3.6).

## 3.1 What Quality Means for Actual

Quality can be defined from several viewpoints. Garvin (1984) distinguishes five approaches: transcendent, product-based, user-based, manufacturing-based and value-based. The transcendent approach treats quality as something recognised but hard to describe, so it gives a QA process nothing to check against. The other four each describe part of what quality means for Actual:

- **User-based.** Actual's product documentation defines success as "users trusting the numbers" (Actual Budget, 2026a, Product Purpose section). For users, quality means balances and envelope totals that are correct, private and easy to understand.
- **Product-based.** Quality lies in properties of the software itself, such as access control on the sync server and the integrity of budget data. Section 3.2 names these properties using ISO/IEC 25010.
- **Manufacturing-based.** In software, this is the process view: a workflow that follows its own standards and so produces those properties every time, not just when an experienced maintainer happens to review the change.
- **Value-based.** Actual is free and funded by donations, so quality work must be affordable in volunteer time.

Stakeholders weight these views differently. Users and families want correct, private budgets. Self-hosters also run a server that holds bank-sync credentials. Volunteer maintainers need checks that do not use up scarce review time. A QA process for Actual must therefore protect financial data without stalling a volunteer workflow.

## 3.2 Key Quality Attributes

ISO/IEC 25010:2023 defines nine product quality characteristics (International Organization for Standardization & International Electrotechnical Commission, 2023). This report focuses on three of them: Security, Reliability and Interaction capability. Each meets two conditions: a failure would seriously harm users' money, data or access to the app, and public evidence shows that Actual's current checks leave a gap (Section 3.3).

- **Security** is the top priority. Actual stores budgets and, on the server, bank-sync tokens that sit outside end-to-end encryption (Actual Budget, n.d.-i). Access-control flaws in the sync server reached released versions in 2026 (Actual Budget, 2026b, 2026c, 2026d).
- **Reliability** covers data integrity across devices, database migrations and recovery. Losing both the encryption password and every local copy makes an encrypted budget unrecoverable (Actual Budget, n.d.-i), yet test coverage of this code is not measured.
- **Interaction capability** includes inclusivity and user assistance. Actual targets WCAG 2.1 AA (Actual Budget, 2026a), so accessibility is a stated requirement, not an extra, yet no automated accessibility testing was found.

Functional suitability might look like a fourth candidate, since correct totals are central to users' trust. It is left out because it is already checked: the repository tests budget recomputation, category totals and the exclusion of off-budget spending (Actual Budget, 2026a), and the 2026 advisories concern security, not calculation errors.

## 3.3 Current QA Practices and Gaps

Actual already runs substantial automated QA. Every pull request triggers linting, type checking, Vitest unit tests and a database migration check, and Playwright end-to-end and visual regression tests run on pull requests and in the merge queue (Actual Budget, 2026a, n.d.-j). CodeQL scans run on pull requests, on pushes and weekly (Actual Budget, 2026a). A release needs approval from at least two other maintainers and smoke tests of the Docker server and desktop app (Actual Budget, n.d.-c). A security policy offers private vulnerability reporting and coordinated disclosure (Actual Budget, n.d.-h).

Comparing these practices with the three attributes shows four gaps. They rest on public evidence only: the repository, documentation and advisories were searched in October 2026, and any checks the team runs privately would not appear there.

- **Security: no proactive check of access control before release.** Critical and high-severity access-control flaws in the sync server were published in 2026 (Actual Budget, 2026b, 2026d). GHSA-m2cq-xjgm-f668, published on 20 February 2026 and rated critical (CVSS 9.2), reported missing authentication on the SimpleFIN and Pluggy AI bank-sync endpoints, although the GoCardless integration had that protection (Actual Budget, 2026c). A check that existed for one bank-sync provider was therefore missing for two others, and the flaw was found only after release. This report proposes an **authorisation test matrix**: an automated test that lists every server endpoint and confirms that each one refuses requests without a valid login or the right permission. Such a test could have caught this inconsistency before release. The security policy also states no response time for reports (Actual Budget, n.d.-h).
- **Reliability: no coverage measurement.** The sync-server test configuration disables coverage (Actual Budget, 2026a), yet the testing checklist asks for "appropriate test coverage" (Actual Budget, n.d.-j, Testing Checklist section). Without a measure, nobody can tell how much of the sync and migration code the tests actually exercise.
- **Interaction capability: no automated accessibility testing** was found, despite the WCAG target (Actual Budget, 2026a).
- **Process: no written QA plan.** Quality rules are spread across documentation, templates and CI files, so no single place states what must be checked before work moves on.

Performance tests are also absent from CI, but performance efficiency is outside the three attributes, so that gap is left out of scope.

## 3.4 Selecting Standards and Practices

A standard is selected only if it passes two tests:

1. **Fit.** It closes one of the gaps in Section 3.3, or, for the quality model, frames the section.
2. **Cost.** A volunteer team, funded by donations and a USD 2,000 monthly stipend pool for review and administration (Actual Budget, n.d.-f), can apply it without certification or a paid appraisal. If contributors must follow its requirements, its text must also be free to read, so that every volunteer can consult it.

Three standards pass both tests (Table 3.1). ISO/IEC 25010 is sold, but it is used here only to name the three attributes, whose names are widely published; contributors never need to follow its text.

*Table 3.1. Standards adopted for Actual's QA process.*

| Standard | Gap it closes | How it is used |
|---|---|---|
| ISO/IEC 25010:2023 | Frames the section | Names and defines the three attributes (3.2) |
| OWASP ASVS 5.0.0 | Security | Selected requirements become acceptance criteria for High-tier work |
| WCAG 2.2 | Interaction capability | Target moves from 2.1 AA to 2.2 AA; automated checks at review |

- **OWASP ASVS 5.0.0** provides a basis for testing technical security controls (OWASP Foundation, 2025). Its authentication, session management and authorisation chapters cover the same kinds of flaw as the 2026 advisories. This report therefore proposes using selected requirements from those chapters, not a full ASVS verification level, as acceptance criteria for sync-server work.
- **WCAG 2.2** is recommended for new work, although W3C states that it does not deprecate 2.1 (World Wide Web Consortium, 2024). Moving Actual's target from 2.1 AA to 2.2 AA is therefore a modest step, and automated checks against it close the accessibility gap.

Section 3.3 found four gaps, but only the security and accessibility gaps need a standard. The reliability gap is that test coverage is not measured; the fix is to turn on a coverage report (Section 3.5), not to adopt a standard. The remaining gap, the lack of a written QA plan, is filled by the plan this report sets out in Section 3.5.

Other well-known standards fail the cost test. IEEE 730-2026, the standard for software QA processes, is available only by purchase or subscription (IEEE, 2026). ISO 9001:2026, ISO/IEC 27001:2022 and CMMI V3.0 assume a formal organisation and deliver their value through certification or an appraisal rating (International Organization for Standardization, 2026; International Organization for Standardization & International Electrotechnical Commission, 2022; Lear, 2023).

## 3.5 Applying the QA Process within Kanban

This section turns the gaps found in Section 3.3 into checks that run inside Actual's everyday workflow. Section 2.5 placed all work on a Kanban board: each bug fix or feature is a card that moves from triage through design, build, review and release to operation, and each column has an exit policy that must be met before the card moves on (Ahmad et al., 2018, p. 98). The QA plan adds its checks to these exit policies. Quality is then checked as part of moving work forward, not in a separate document that volunteers may never open.

Not every change needs every check. At triage, each card is given a risk tier, defined in Section 4.3: *High* for work on authentication, bank sync, calculations, database migrations, sync and encryption; *Low* for themes, wording and documentation; and *Standard* for everything else. The heavier security and data checks apply only to High-tier cards, so volunteers' time goes where failure costs most.

Table 3.2 is the resulting plan. Each row is a column of the board. It shows the checks added to that column's exit policy, with the attribute each check protects in brackets, which cards the checks apply to and who is responsible. Actual's existing checks (CI, maintainer review, two release approvals and smoke tests) stay in place and are not repeated.

*Table 3.2. QA checks added to each Kanban column.*

| Kanban column | Checks added to the exit policy | Applies to | Who |
|---|---|---|---|
| Requirements/triage | Risk tier set; acceptance criteria written for security, data and accessibility (all three) | All cards | Triager |
| Design | Endpoints and permissions listed (security); migration and sync impact stated (reliability) | High tier | Implementer |
| Build/PR | Coverage report produced (reliability); new endpoints added to the authorisation test matrix (security) | All; matrix for High tier | Implementer |
| Verify | Automated WCAG 2.2 AA checks pass (interaction capability); selected ASVS requirements checked (security) | Cards that change the UI; ASVS for High tier | Reviewer |
| Release train | No open critical or high security finding (security) | Every release | Release maintainers |
| Operate/maintain | Security reports answered within a stated response time (security); each defect that reached users gets a regression test and a review of the check that missed it (all three) | Every report | Maintainers handling security reports |

The people in the Who column are existing maintainers and contributors; the plan assigns duties, not new posts, and triage and review are already paid from the stipend pool (Actual Budget, n.d.-f). Written into the contributing guide as well as onto the board, Table 3.2 is also the written QA plan that Section 3.3 found missing.

**Worked example.** Suppose a contributor adds a new bank-sync provider, the kind of change behind GHSA-m2cq-xjgm-f668 (Section 3.3). At triage, the card is marked High tier because it touches bank sync, and an acceptance criterion is written: every new endpoint must refuse requests without a valid login. At design, the implementer lists the new endpoints and who may call each one. At Build/PR, the endpoints are added to the authorisation test matrix. If the login check is missing, that test fails and the card cannot move to Verify, so a flaw like the 2026 one could be stopped before release. A typo fix in the documentation, by contrast, is Low tier and passes through the normal checks only.

Each attribute has one measure, defined in Assignment 2: the share of server endpoints covered by the authorisation test matrix (security), test coverage of the core and sync-server packages (reliability), and the number of automated accessibility violations on key screens (interaction capability).

## 3.6 Critical Evaluation

The plan's main cost is volunteer time. Every new exit criterion adds work for a small team. Reviewers are paid from a USD 2,000 monthly stipend pool (Actual Budget, n.d.-f), the project has already had pull requests waiting months for review (Aboltins, 2025), and maintainers identify administrative overhead as a burnout risk (Salkever, 2023). The risk tiers in Section 3.5 limit this cost, because documentation and styling changes skip the security and data criteria. The tier, however, is a judgement made at triage: a change placed in too low a tier passes with fewer checks.

The plan also adds automation: a coverage report, accessibility checks and the authorisation test matrix. Automation is not free. After adopting GitHub Actions, projects saw more rejected pull requests and longer acceptance times (Wessel et al., 2023), whereas code review bots were associated with more merged pull requests and less discussion (Wessel et al., 2022). These observational studies cannot predict Actual's results, so each new check should be monitored for its effect on review time and tuned or removed if it slows the flow without finding defects.

Two limits remain. First, automated accessibility checks find rule violations but cannot judge whether an envelope-budgeting task is understandable, so manual review is still needed. Second, the evidence is public only: the gaps in Section 3.3 may be partly covered by private practices.

<!-- Cited: S01, S03, S08, S09, S10, S38, S43, S44, S47, S51, S53, S55, S57, S58, S59, S62, S63-m2cq, S63-prp4, S63-cq9c, S82, S85, S129 -->

# 4 Integrating IV&V with Kanban

## 4.1 V&V, IV&V and why Actual needs them

IEEE 1012-2024 describes verification as checking whether the products of an activity conform to that activity's requirements, and validation as checking whether the product satisfies its intended use and user needs (IEEE, 2025). It specifies V&V requirements for different integrity levels. Independent V&V (IV&V) adds a condition on who does the checking. NASA, following IEEE, defines independence along three parameters: technical (assessors judge the work independently of the developer), managerial (responsibility for IV&V sits in a separate organisation) and financial (the IV&V budget is controlled by an organisation independent of development) (National Aeronautics and Space Administration, n.d.).

Agile delivery does not remove the need for IV&V. Smith and Hayes (2024, Abstract) argue that the move to agile "has in no way diminished the need for IV&V", note that security may not be readily demonstrable through user-visible behaviour, and recommend that IV&V runs in phase with the development cadence. This matters for Actual, which holds personal financial data and whose sync server has had critical and high-severity access-control flaws published as advisories in 2026 (Actual Budget, 2026c, 2026d).

## 4.2 Current V&V in Actual and its independence (as-is)

*Table 4.1. Independence of Actual's existing V&V activities.*

| Activity | Performed by | Technical | Managerial | Financial |
|---|---|---|---|---|
| PR review | Another core maintainer; non-controversial PRs may be merged straight away (Actual Budget, n.d.-e) | Yes | No | No: reviewers share one stipend pool (Actual Budget, n.d.-f) |
| Release approval and smoke test | At least two other maintainers (Actual Budget, n.d.-c) | Yes | No | No |
| CI tests and CodeQL scanning | Automated, configured by the team (Actual Budget, 2026a) | Partial | No | No |
| PR preview and nightly builds | Any community member, voluntarily (Actual Budget, n.d.-g) | Partial | Not established | Not established |
| Vulnerability reports | Reporters outside the core team (Actual Budget, 2026c) | Yes | Not established | Not established |
| External audit | No public evidence found (October 2026) | — | — | — |

Actual therefore has real independent checking, but it is ad hoc and mostly technical. Internal reviewers share one small team, release goals and donation-funded pool, so they cannot provide managerial or financial independence. The strongest independent findings came after release. The three advisories checked for this report credit iamsilk, Rex50527 and pyuysig, none of whom is a core maintainer, with discovering a critical and two high-severity flaws in released versions (Actual Budget, 2026b, 2026c, 2026d). The credits establish who found the flaws; they do not show the reporters' organisational or funding arrangements, so only technical independence is evidenced.

The disclosure route itself is a strength. Actual asks for private reporting and coordinated disclosure (Actual Budget, n.d.-h), a practice most OSS practitioners support but which only 55% of studied vulnerabilities actually followed (Liu et al., 2025). No public evidence of an external security audit was found in the documentation and blog reviewed (October 2026).

## 4.3 IV&V integration model for Kanban (to-be)

**Achievable independence.** A maintainer review is not full IV&V in the IEEE sense, and the report does not present it as such. Internally, the proposal adds an *independent reviewer* role for high-risk work: a maintainer who is neither the author nor the code owner of the affected area. This gives technical independence only. Managerial and financial independence must come from outside: the existing coordinated-disclosure channel and an optional, periodic funded external security audit. The Open Source Technology Improvement Fund (OSTIF) shows this is workable for OSS: it self-reports 24 audits published in 2025, with 231 security-relevant findings and over 98% fixed (Open Source Technology Improvement Fund, 2026). Financial independence is stronger when a third party, not Actual, pays.

**Risk tiers.** Inspired by IEEE 1012's integrity-level concept (IEEE, 2025), this report proposes its own three tiers; they are not IEEE's scheme:

- *High*: authentication, authorisation and sessions; bank-sync endpoints; budget and balance calculations; database migrations; sync and encryption.
- *Standard*: most features, such as reports, rules and UI components.
- *Low*: themes, wording and documentation.

**Explicit policies.** Kanban makes process policies explicit as entry and exit criteria that determine when an item may be pulled into the next state (Ahmad et al., 2018, p. 98). The tier label set at triage decides which IV&V criteria apply, and independent-reviewer capacity is counted within the WIP limits that the Kanban Method uses to manage flow (Kanban University, n.d.). Checks therefore run per item, in phase with the flow (Smith & Hayes, 2024). Section 3 defines *what* each QA gate checks; Section 4 adds *who* verifies it and what independent evidence is required.

## 4.4 IV&V activities across the Kanban workflow

*Table 4.2. IV&V activities, tools, roles and exit criteria per Kanban stage (high-tier items unless stated).*

| Stage (lifecycle phase) | IV&V activities | Tools | Independent role | Exit criterion |
|---|---|---|---|---|
| Requirements/triage (requirements) | Assign risk tier; validate that acceptance criteria are testable and include security criteria | Issue templates, triage labels | Triager other than the requester | Tier and testable criteria recorded |
| Design (design) | Review design and a short threat note against access-control requirements | ADR, OWASP ASVS 5.0.0 | Independent reviewer | Threat note accepted; ASVS requirements selected |
| Build/PR (implementation) | Code review against selected ASVS requirements; check authorisation and regression tests exist | GitHub review, CodeQL, CI | Independent reviewer (not author, not code owner) | Approval citing ASVS IDs and tests; CI green |
| Verify (testing) | Validate behaviour on preview build; run server and security tests on a separate test server with synthetic budgets | Preview builds, Playwright, Vitest | Validator other than the author | Evidence attached; no open high findings |
| Release train (deployment) | Verify the release candidate and that every high-tier item met its exit criteria | Release checklist, Docker and desktop builds | At least two other maintainers; one checks tier evidence | Signed-off evidence before final release |
| Operate/maintain (maintenance) | Triage reports; add a regression test for each fixed advisory; feed findings back to triage | Private vulnerability reporting, advisories | External reporters; optional funded auditor | Advisory published; regression test merged |

Standard-tier items skip the design threat note and need only preview-build validation; low-tier items follow normal review. The ASVS suits the sync server's advisory history because it provides a basis for testing web application technical security controls (OWASP Foundation, 2025). Preview and nightly web builds include no sync server (Actual Budget, n.d.-g), so the Verify stage needs a separate controlled server. The release row adds evidence before final approval; it does not claim that current smoke testing precedes every publication step (Actual Budget, n.d.-c).

## 4.5 How the integration meets the three goals

**Early defect detection.** GHSA-m2cq-xjgm-f668 arose because six SimpleFIN and Pluggy.ai endpoints lacked authentication middleware (Actual Budget, 2026c). Under the model, bank-sync work is high tier, so an independent reviewer applying ASVS authentication requirements, backed by authorisation tests, would have a defined point at the design or PR gate to detect the omission before release.

**Requirements compliance.** The model links each requirement to its evidence: feature request, testable acceptance criteria, a PR referencing the issue, tests and the release note. Actual already has most of these links; the independent reviewer checks that the chain is complete.

**Overall quality.** Tiering concentrates scarce review effort where failure is costliest, aiming to reduce escaped defects. Assignment 2 addresses how to measure this.

## 4.6 Critical evaluation

The model cannot deliver full IEEE-style independence internally. The independent reviewer belongs to the same team and stipend pool, so managerial and financial independence still depend on outsiders, whose involvement is voluntary or funded.

Independence also competes with flow. After open-sourcing, PRs waited months for review (Aboltins, 2025), and growing demands on maintainers' time contribute to burnout in OSS projects (Salkever, 2023). Requiring a second, non-owner reviewer for every item would recreate that backlog. Tiering and WIP limits reduce this risk, but tier assignment is a judgement that may understate risk.

Cost is a binding constraint. Actual receives about USD 3,000–3,500 a month in donations, of which USD 2,000 is allocated to review stipends (Actual Budget, n.d.-f), so a funded audit depends on donors or a third-party funder. Its cost is estimated in Assignment 2.

Finally, gates can become ritual. Actual's own payment guide concedes that rubber-stamp reviews to earn points are theoretically possible (Actual Budget, n.d.-f); requiring cited ASVS IDs and named tests makes approval harder to fake but not impossible. ASVS covers technical security controls only (OWASP Foundation, 2025), leaving reliability and interaction capability to Section 3's gates.

<!-- Cited: S01, S03, S04, S08, S10, S38, S47, S58, S62, S63-m2cq, S63-prp4, S63-cq9c, S66, S67, S68, S69, S70, S72, S109 -->

# References

Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025/

Actual Budget. (2026a). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual

Actual Budget. (2026b, June 12). *Disabled OpenID users keep access through existing session tokens* (GHSA-cq9c-6w48-qmfg) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-cq9c-6w48-qmfg

Actual Budget. (2026c, February 20). *Missing authentication for SimpleFIN and Pluggy AI bank sync endpoints* (GHSA-m2cq-xjgm-f668) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-m2cq-xjgm-f668

Actual Budget. (2026d, April 23). *Privilege escalation via 'change-password' endpoint on OpenID-migrated servers* (GHSA-prp4-2f49-fcgp) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-prp4-2f49-fcgp

Actual Budget. (n.d.-a). *Contributing to Actual Budget*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/

Actual Budget. (n.d.-b). *Feature flags (experimental features)*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/project-details/feature-flags/

Actual Budget. (n.d.-c). *How to cut a release*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/releasing/

Actual Budget. (n.d.-d). *Installing Actual*. Retrieved October 22, 2026, from https://actualbudget.org/docs/install/

Actual Budget. (n.d.-e). *New core contributors guide*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide/

Actual Budget. (n.d.-f). *Paying reviewers for administrative work*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors/

Actual Budget. (n.d.-g). *Preview builds*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/preview-builds/

Actual Budget. (n.d.-h). *Security policy* [SECURITY.md]. GitHub. Retrieved October 22, 2026, from https://github.com/actualbudget/.github/blob/main/SECURITY.md

Actual Budget. (n.d.-i). *Syncing across devices*. Retrieved October 22, 2026, from https://actualbudget.org/docs/getting-started/sync/

Actual Budget. (n.d.-j). *Testing*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/testing/

Actual Budget. (n.d.-k). *A tour of Actual*. Retrieved October 22, 2026, from https://actualbudget.org/docs/tour/

Ahmad, M. O., Dennehy, D., Conboy, K., & Oivo, M. (2018). Kanban in software engineering: A systematic mapping study. *Journal of Systems and Software, 137*, 96–113. https://doi.org/10.1016/j.jss.2017.11.045

Beck, K., & Andres, C. (2005, June 10). *Getting started with eXtreme Programming: Toe dipping, racing dives, and cannonballs: Appendix: Primary practices*. InformIT. https://www.informit.com/articles/article.aspx?p=390816&seqNum=3

Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer, 21*(5), 61–72. https://doi.org/10.1109/2.59

DORA. (n.d.). *Test automation*. Retrieved October 26, 2026, from https://dora.dev/capabilities/test-automation/

Garvin, D. A. (1984). What does "product quality" really mean? *Sloan Management Review, 26*(1), 25–43. https://sloanreview.mit.edu/article/what-does-product-quality-really-mean/

GeeksforGeeks. (2025, July 23). *How to choose the best SDLC model for your project*. https://www.geeksforgeeks.org/software-engineering/how-to-choose-the-best-sdlc-model-for-your-project/

Institute of Electrical and Electronics Engineers. (2025). *IEEE standard for system, software, and hardware verification and validation* (IEEE Std 1012-2024). https://standards.ieee.org/ieee/1800.2/7324/

Institute of Electrical and Electronics Engineers. (2026). *IEEE standard for software quality assurance processes* (IEEE Std 730-2026). https://standards.ieee.org/ieee/730/10854/

International Organization for Standardization. (2026). *Quality management systems — Requirements* (ISO Standard No. 9001:2026). https://www.evs.ee/en/iso-9001-2026

International Organization for Standardization & International Electrotechnical Commission. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC Standard No. 27001:2022). https://www.iso.org/standard/27001

International Organization for Standardization & International Electrotechnical Commission. (2023). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (ISO/IEC Standard No. 25010:2023). https://www.iso.org/standard/78176.html

Kanban University. (n.d.). *The official guide to the Kanban method*. Retrieved October 22, 2026, from https://kanban.university/kanban-guide/

Kuhrmann, M., Tell, P., Hebig, R., Klünder, J., Münch, J., Linssen, O., Pfahl, D., Felderer, M., Prause, C. R., MacDonell, S. G., Nakatumba-Nabende, J., Raffo, D., Beecham, S., Tüzün, E., López, G., Paez, N., Fontdevila, D., Licorish, S. A., Küpper, S., … Richardson, I. (2022). What makes agile software development agile? *IEEE Transactions on Software Engineering, 48*(9), 3523–3539. https://doi.org/10.1109/TSE.2021.3099532

Lear, R. (2023, April 10). *CMMI updates take performance improvements to the next level*. ISACA. https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2023/cmmi-updates-take-performance-improvements-to-the-next-level

Liu, S., Zhou, J., Hu, X., Côgo, F. R., Xia, X., & Yang, X. (2025). An empirical study on vulnerability disclosure management of open source software systems. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3716822

Mockus, A., Fielding, R. T., & Herbsleb, J. D. (2002). Two case studies of open source software development: Apache and Mozilla. *ACM Transactions on Software Engineering and Methodology, 11*(3), 309–346. https://doi.org/10.1145/567793.567795

National Aeronautics and Space Administration. (n.d.). *IV&V overview*. Retrieved October 22, 2026, from https://www.nasa.gov/ivv-overview/

Open Source Technology Improvement Fund. (2026, January 30). *2025 annual report*. https://ostif.org/2025-annual-report/

OWASP Foundation. (2025). *OWASP application security verification standard* (Version 5.0.0). https://owasp.org/www-project-application-security-verification-standard/

Raymond, E. S. (2000). *The cathedral and the bazaar* (Version 3.0). https://web.stanford.edu/class/me228/pdf/cathedral-bazaar.pdf

Salkever, A. (2023). *Open source maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects*. The Linux Foundation. https://doi.org/10.70828/lddj8886

Schwaber, K., & Sutherland, J. (2020). *The Scrum guide*. https://scrumguides.org/scrum-guide.html

Smith, J., & Hayes, W. (2024). Independent verification & validation (IV&V) for agile developed projects. In *2024 IEEE Aerospace Conference* (pp. 1–10). IEEE. https://doi.org/10.1109/AERO58975.2024.10521415

Stacoviak, A., & Santo, J. (Hosts). (2022, July 1). *Actual(ly) opening up with James Long* (No. 495) [Audio podcast episode]. In *The Changelog*. Changelog Media. https://changelog.com/podcast/495

Wessel, M., Serebrenik, A., Wiese, I., Steinmacher, I., & Gerosa, M. A. (2022). Quality gatekeepers: Investigating the effects of code review bots on pull request activities. *Empirical Software Engineering, 27*(5), Article 108. https://doi.org/10.1007/s10664-022-10130-9

Wessel, M., Vargovich, J., Gerosa, M. A., & Treude, C. (2023). GitHub Actions: The impact on the pull request process. *Empirical Software Engineering, 28*(6), Article 131. https://doi.org/10.1007/s10664-023-10369-w

World Wide Web Consortium. (2024, December 12). *Web content accessibility guidelines (WCAG) 2.2* (W3C Recommendation). https://www.w3.org/TR/WCAG22/

youngcw. (2025, December 20). *Roadmap for 2026*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2026/

