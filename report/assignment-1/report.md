# Software Quality Engineering Evaluation of Actual Budget: Methodology, Quality Assurance and IV&V

*Working title; cover page, table of contents and lists are added at final assembly.*

# Executive Summary

This report evaluates Actual Budget, a free, open-source, local-first personal finance application run by a small volunteer team, whose users must be able to trust its numbers and the security of their data.

Actual has a defined workflow but no deliberate methodology. Its profile suits an agile approach, except that its few reviewers are overloaded and its defects can affect money and data. Of five candidates, Kanban fits best because it limits the review backlog; mandatory quality gates are added because Kanban prescribes no quality practices.

The QA process focuses on three ISO/IEC 25010:2023 characteristics: Security, Reliability and Interaction capability. Public evidence shows gaps in proactive security verification, coverage measurement and accessibility testing. The plan adopts OWASP ASVS 5.0.0 and WCAG 2.2 and writes risk-scaled checks into the exit policy of each Kanban stage.

IV&V adds risk-tiered independent review inside the team, plus external checks through coordinated disclosure and an optional funded audit. Internal review gives technical independence only, and volunteer time and donation funding remain the main limits.

# 1 Introduction

## 1.1 Background and Purpose

Personal finance applications help people record spending and plan a budget. Because they hold balances, transactions and sometimes bank connections, their quality matters: a wrong total can lead to a poor financial decision, and a security flaw can expose private data.

I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and keep track of my finances. This assignment gave me the opportunity to examine it in depth.

Written from the view of outside analysts, this report covers three topics. Section 2 selects a software development methodology for the project, Section 3 sets out a quality assurance (QA) process, and Section 4 integrates independent verification and validation (IV&V) into the selected methodology.

## 1.2 What Is Actual Budget

Actual Budget ("Actual") is a free, open-source personal finance application released under the MIT licence. It is local-first: the budget is kept on the user's own device, and syncing between devices is optional (Actual Budget, 2026a). It targets privacy-minded budgeters, self-hosters and families, and defines success as users trusting its numbers (Actual Budget, 2026a). By default, Actual uses envelope budgeting, in which people budget the money they already have rather than income they expect to receive (Actual Budget, n.d.-j).

Actual was created by James Long, who ran it as a paid product for over four years (Stacoviak & Santo, 2022). In early 2022 he closed the commercial product and released it as open source (Aboltins, 2025). It is now maintained by volunteers, led by a core team that formed after pull requests had waited months for review (Aboltins, 2025).

## 1.3 Main Features and How It Works

Actual covers budgeting, accounts and transactions, rules, scheduled transactions and reports (Actual Budget, n.d.-j). It runs as a desktop app, through Docker, or on paid hosting from PikaPods or Fly.io (Actual Budget, n.d.-c).

A server is not required for basic budgeting, but syncing between devices and bank synchronisation both need one (Actual Budget, n.d.-c). Users can optionally turn on end-to-end encryption for synced data, but data on the local device stays unencrypted and bank-sync tokens on the server are not covered (Actual Budget, n.d.-h). Figure 1 shows how the parts connect.

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

*Figure 1. How Actual Budget works (based on Actual Budget, n.d.-c).*

## 1.4 Who Is Involved

*Table 1.1. Main stakeholders of Actual Budget.*

| Stakeholder | Role and interest |
|---|---|
| Users | Need correct figures and private data |
| Self-hosters | Run their own server and need it secure |
| Core maintainers | Eight listed main contributors who review and release (Actual Budget, n.d.-a) |
| Contributors | Volunteers who choose their own work (Actual Budget, n.d.-a) |
| Donors and hosting partners | Fund the project through Open Collective (Actual Budget, n.d.-e); PikaPods reported over 8,000 users in December 2025 (youngcw, 2025) |

## 1.5 Main Challenges

- **Volunteer capacity and changing requirements.** Work depends on volunteers, and review has been a bottleneck before (Aboltins, 2025). Section 2 addresses how work is organised.
- **Trust in the numbers and data security.** Users rely on correct figures and protected data (Section 3).
- **Escaped defects and security flaws.** Problems found after release harm users (Section 4).

<!-- Cited: S01, S02, S08, S10, S11, S15, S51, S121, S122 -->

# 2 Software Development Methodology

Because a methodology can only be judged against the project it must serve, this section first describes how Actual works today. It then explains why Kanban, tailored with quality gates, fits Actual best, shows how it would work in practice and examines its weaknesses.

## 2.1 Current development process of Actual (as-is)

Actual's contributor documentation does not name any methodology (no evidence found, October 2026). It does, however, describe the same route for every change, shown in Figure 2.

Users' feature requests are ranked by votes, and nobody is assigned to them: contributors choose which to work on and submit a pull request (PR). Continuous integration (CI) and a core maintainer then check the PR, and a monthly release train ships whatever is ready (Actual Budget, 2026a, n.d.-a, n.d.-b, n.d.-d).

The step that has caused trouble is review. Only maintainers can approve a PR, and the project lists eight of them (Actual Budget, n.d.-a). After Actual became open source in 2022, PRs waited months because nobody was available to review them (Aboltins, 2025). The project now pays maintainers for review and triage from a USD 2,000 monthly pool funded by donations (Actual Budget, n.d.-e), which shows that review time is its scarcest resource.

Actual therefore has **a defined workflow but no deliberate methodology**. The steps are clear, but nothing manages how work moves through them, and nothing limits how many PRs can pile up waiting for the few people able to review them.

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

## 2.2 Why Kanban fits Actual

Actual's profile points mostly to an agile model. Its requirements change continuously as users vote, users shape the work directly, and each monthly release ships whatever is ready, all of which favour agile over linear models (GeeksforGeeks, 2025). Two factors pull the other way: the few experienced reviewers are volunteers whose time has already run out once (Aboltins, 2025), and risk tolerance is low, because defects can mislead money decisions and expose financial data (Actual Budget, 2026c). The methodology therefore has to handle changing priorities, work with self-chosen tasks, keep its rules written down, protect review time, and include quality and risk controls.

Kanban meets the first four. It limits work in progress (WIP), the number of items allowed in a stage at once (Kanban University, n.d.). This assignment proposes placing that limit on review: once it is reached, no new PRs enter review until waiting ones are cleared, which protects the maintainers' review time. Its rules for moving work between stages are written down, so they do not depend on who happens to be on the team, and contributors still pick tasks from the voted backlog whenever they have time, so nobody has to commit to a fixed amount of work. Kanban is also applied on top of an existing process rather than replacing it (Kanban University, n.d.), so Actual keeps the workflow that already suits its volunteers.

Kanban does not, however, say how quality should be checked, and this matters because Actual's risk tolerance is low. The report therefore adds **mandatory quality gates (QA gates)**: checks, defined in Section 3, that every change must pass before it moves to the next stage. **The selected methodology is Kanban, tailored with mandatory QA gates.**

Appendix A sets out how this choice was reached: Actual was profiled against eight standard selection factors, and Kanban was compared with Spiral, Scrum, Extreme Programming (XP) and DevOps. In brief, Scrum and XP require team members to commit their time together, which volunteers cannot do; Spiral would place expert risk analysis on the already overloaded reviewers; and DevOps mainly adds automated testing, which Actual's CI already provides.

## 2.3 Applying Kanban to Actual (to-be)

Figure 3 shows the proposed board. Each piece of work, such as a bug fix or a new feature, is a card that moves left to right through six columns, from triage to operation. Each column has an **exit policy**: a written condition that must be met before work can be pulled into the next column (Ahmad et al., 2018, p. 98).

The WIP limit proposed in Section 2.2 sits on the Verify column, where review happens. It should be set from the number of reviews the maintainers actually complete, so that new work stops entering once reviews start to pile up. Section 3 adds quality checks to the exit policies, and Section 4 adds independent checks. The monthly release stays as it is, and each release becomes the point at which the team checks whether the limits and policies need adjusting.

```
Rule: pull work only when the next column is under its WIP limit
+------------------------+------------------------------------------------+
| Column                 | Exit policy (pull criterion)                   |
+------------------------+------------------------------------------------+
| 1 Requirements/triage  | Problem, acceptance criteria and risk recorded |
| 2 Design               | Approach agreed; decision record if high-risk  |
| 3 Build/PR             | CI green; tests and release note included      |
| 4 Verify   [WIP limit] | Reviewer is not the implementer; QA gate passed|
|                        | (Security, Reliability, Interaction capability)|
| 5 Release train        | Monthly cut (25th); >=2 approvals; smoke test  |
| 6 Operate/maintain     | User reports and advisories triaged to col. 1  |
+------------------------+------------------------------------------------+
        ^                                                      |
        +------------------- feedback loop --------------------+
```

*Figure 3. Proposed (to-be) Kanban workflow for Actual with explicit exit policies.*

## 2.4 Critical evaluation

Kanban manages flow but does not improve quality by itself: it is "a relatively basic flow tool that needs to be supported by additional practices" (Ahmad et al., 2018, p. 110), which is why the QA gates are mandatory. Its WIP limit is also weaker in a volunteer project, because it cannot force anyone to review and blocked PRs may discourage newcomers (Salkever, 2023), so it should act as a signal rather than a hard block. The evidence has limits too. The selection factors come from a practitioner tutorial (GeeksforGeeks, 2025), the factor profile in Appendix A rests on qualitative judgement because Actual publishes no data to measure them, and no study shows Kanban improving a project like Actual, so its benefit is plausible but unproven. Tailoring it is still reasonable, since few projects follow any methodology in pure form (Kuhrmann et al., 2022). The choice should be revisited if Actual gains paid staff, which would make Scrum's commitments realistic, or runs its own hosted service, which would give DevOps operations to integrate.

<!-- Cited: S01, S02, S03, S04, S08, S10, S26, S34, S36, S38, S47, S105, S108, S109, S121, S123, S128, S63-m2cq -->

# 3 Quality Assurance Process

This section defines what quality means for Actual and which attributes matter most, finds the gaps in current practice, selects standards to close them, builds the resulting plan into the Kanban workflow and examines its weaknesses.

## 3.1 What Quality Means for Actual

Quality can be defined from several viewpoints. Garvin (1984) distinguishes five approaches: transcendent, product-based, user-based, manufacturing-based and value-based. The transcendent approach, quality as something recognised but hard to describe, gives a QA process nothing to check against. The other four each describe part of what quality means for Actual:

- **User-based.** Actual's product documentation defines success as "users trusting the numbers" (Actual Budget, 2026a, Product Purpose section). For users, quality means balances and envelope totals that are correct, private and easy to understand.
- **Product-based.** Quality lies in properties of the software itself, such as access control on the sync server and the integrity of budget data. Section 3.2 names these properties using ISO/IEC 25010.
- **Manufacturing-based.** In software, this is the process view: a workflow that follows its own standards and so produces those properties every time, not only when an experienced maintainer reviews the change.
- **Value-based.** Actual is free and funded by donations, so quality work must be affordable in volunteer time.

Users care most about the first view and volunteer maintainers about the last, so a QA process for Actual must protect financial data without stalling a volunteer workflow.

## 3.2 Key Quality Attributes

ISO/IEC 25010:2023 defines nine product quality characteristics (International Organization for Standardization & International Electrotechnical Commission, 2023). This report focuses on three of them: Security, Reliability and Interaction capability. Each meets two conditions: a failure would seriously harm users' money, data or access to the app, and public evidence shows that Actual's current checks leave a gap (Section 3.3).

- **Security** is the top priority. Actual stores budgets and, on the server, bank-sync tokens that sit outside end-to-end encryption (Actual Budget, n.d.-h). Access-control flaws in the sync server reached released versions in 2026 (Actual Budget, 2026b, 2026c, 2026d).
- **Reliability** covers data integrity across devices, database migrations and recovery. Losing both the encryption password and every local copy makes an encrypted budget unrecoverable (Actual Budget, n.d.-h).
- **Interaction capability** includes inclusivity and user assistance. Actual targets WCAG 2.1 AA (Actual Budget, 2026a), so accessibility is a stated requirement, not an extra.

## 3.3 Current QA Practices and Gaps

Actual already runs substantial automated QA. Every pull request triggers linting, type checking, Vitest unit tests and a database migration check, and Playwright end-to-end and visual regression tests run on pull requests and in the merge queue (Actual Budget, 2026a, n.d.-i). CodeQL scans run on pull requests, on pushes and weekly (Actual Budget, 2026a). Releases add two maintainer approvals and smoke tests (Actual Budget, n.d.-b). A security policy offers private vulnerability reporting and coordinated disclosure (Actual Budget, n.d.-g).

Comparing these practices with the three attributes shows four gaps. They rest on public evidence only: the repository, documentation and advisories were searched in October 2026, and any checks the team runs privately would not appear there.

- **Security: no proactive check of access control before release.** Three access-control flaws in the sync server, one critical and two high-severity, were published in 2026 (Actual Budget, 2026b, 2026c, 2026d). The critical one, GHSA-m2cq-xjgm-f668 (CVSS 9.2), was missing authentication on six SimpleFIN and Pluggy AI bank-sync endpoints, although the GoCardless endpoints had it (Actual Budget, 2026c). A check that existed for one provider was missing for two others, and the flaw was found only after release. This report proposes an **authorisation test matrix**: an automated test that lists every server endpoint and confirms that each one refuses requests without a valid login or the right permission. Such a test could have caught this inconsistency before release. The security policy also states no response time for reports (Actual Budget, n.d.-g).
- **Reliability: no coverage measurement.** Reliability defects still reach users. Until September 2026, a large sync could overflow an internal counter in some privacy-focused browsers, so that "the budget never opens"; the faulty code had been in released versions since at least 2023 (Brown, 2026). Yet the sync-server test configuration disables coverage (Actual Budget, 2026a), even though the testing checklist asks for "appropriate test coverage" (Actual Budget, n.d.-i, Testing Checklist section), so nobody can tell how much of the sync and migration code the tests exercise. Coverage shows only which code is untested, not whether tested code is correct, so it is a starting point rather than proof of reliability.
- **Interaction capability: no automated accessibility testing** was found, despite the WCAG target (Actual Budget, 2026a).
- **Process: no written QA plan.** Quality rules are spread across documentation, templates and CI files, so no single place states what must be checked before work moves on.

## 3.4 Selecting Standards and Practices

A standard is selected only if it passes two tests:

1. **Fit.** It closes one of the gaps in Section 3.3, or, for the quality model, frames the section.
2. **Cost.** A donation-funded volunteer team (Section 2.1) can apply it without certification or a paid appraisal. If contributors must follow its requirements, its text must also be free to read, so that every volunteer can consult it.

Three standards pass both tests (Table 3.1). ISO/IEC 25010 is sold, but it is used here only to name the three attributes, whose names are widely published; contributors never need to follow its text.

*Table 3.1. Standards adopted for Actual's QA process.*

| Standard | Gap it closes | How it is used |
|---|---|---|
| ISO/IEC 25010:2023 | Frames the section | Names and defines the three attributes (3.2) |
| OWASP ASVS 5.0.0 | Security | Its authentication, session and authorisation chapters cover the same kinds of flaw as the 2026 advisories (OWASP Foundation, 2025). Selected requirements from them, not a full verification level, become acceptance criteria for high-risk sync-server work |
| WCAG 2.2 | Interaction capability | Target moves from 2.1 AA to 2.2 AA, a modest step because 2.2 does not deprecate 2.1 (World Wide Web Consortium, 2024); automated checks at review |

The other two gaps need no standard: the reliability gap is closed by turning on a coverage report, and the missing QA plan by the plan in Section 3.5.

Other well-known standards fail the cost test. IEEE 730-2026, the standard for software QA processes, is available only by purchase or subscription (Institute of Electrical and Electronics Engineers [IEEE], 2026). ISO 9001:2026, ISO/IEC 27001:2022 and CMMI V3.0 assume a formal organisation and deliver their value through certification or an appraisal rating (International Organization for Standardization, 2026; International Organization for Standardization & International Electrotechnical Commission, 2022; Lear, 2023).

## 3.5 Applying the QA Process within Kanban

This section turns the gaps found in Section 3.3 into checks inside Actual's everyday workflow, by adding them to the exit policies of the Kanban board (Section 2.3). Quality is then checked as part of moving a card forward, not in a separate document that volunteers may never open.

Not every card needs every check: running security and data checks on a wording change would waste the review time that Section 2.1 found scarce. At triage, each card is therefore given a risk tier according to the worst plausible failure of the change, choosing the higher tier when unsure:

- *High*: a failure could expose financial data or credentials, give wrong money figures or lose budget data (authentication, authorisation and sessions; bank sync; budget and balance calculations; database migrations; sync and encryption).
- *Standard*: a failure would be visible but recoverable without data loss (most features, such as reports, rules and UI components).
- *Low*: a failure would be cosmetic (themes, wording and documentation).

The tiers are this report's own, borrowing only the idea in IEEE 1012-2024 that the verification a component needs depends on its integrity level (IEEE, 2025).

Table 3.2 is the resulting plan, and also the written QA plan that Section 3.3 found missing. Each row is a board column, showing the checks added to its exit policy (with the attribute each protects in brackets), which cards they apply to and who is responsible. Actual's existing checks stay in place, and the people responsible are existing maintainers and contributors, not new posts. Appendix B follows one card through the plan.

*Table 3.2. QA checks added to each Kanban column.*

| Kanban column | Checks added to the exit policy | Applies to | Who |
|---|---|---|---|
| Requirements/triage | Risk tier set; acceptance criteria written for security, data and accessibility (all three) | All cards | Triager |
| Design | Endpoints and permissions listed (security); migration and sync impact stated (reliability) | High tier | Implementer |
| Build/PR | Coverage report produced (reliability); new endpoints added to the authorisation test matrix (security) | All; matrix for High tier | Implementer |
| Verify | Automated WCAG 2.2 AA checks pass (interaction capability); selected ASVS requirements checked (security) | Cards that change the UI; ASVS for High tier | Reviewer |
| Release train | No open critical or high security finding (security) | Every release | Release maintainers |
| Operate/maintain | Security reports answered within a stated response time (security); each defect that reached users gets a regression test and a review of the check that missed it (all three) | Every report | Maintainers handling reports |

## 3.6 Critical Evaluation

The plan's main cost is volunteer time: every new exit criterion adds work for a small team whose review time is already scarce (Section 2.1). The risk tiers limit this cost, but a card placed in too low a tier at triage passes with fewer checks. The added automation is not free either. After adopting GitHub Actions, projects saw more rejected pull requests and longer acceptance times (Wessel et al., 2023), whereas code review bots were associated with more merged pull requests (Wessel et al., 2022). Because these studies cannot predict Actual's results, each new check should be monitored and removed if it slows review without finding defects. Finally, automated accessibility checks find rule violations but cannot judge whether an envelope-budgeting task is understandable, so manual review is still needed.

<!-- Cited: S01, S03, S08, S09, S10, S38, S43, S44, S47, S51, S53, S55, S57, S58, S59, S62, S63-m2cq, S63-prp4, S63-cq9c, S82, S85, S129, S137 -->

# 4 Integrating IV&V with Kanban

## 4.1 Current V&V in Actual and its independence (as-is)

IEEE 1012-2024 describes verification as checking whether the products of an activity conform to that activity's requirements, and validation as checking whether the product satisfies its intended use and user needs (IEEE, 2025). Independent V&V (IV&V) adds a condition on who does the checking. NASA, following IEEE, defines independence along three parameters (National Aeronautics and Space Administration, n.d.):

- **Technical:** the checker assesses the work independently of the developer.
- **Managerial:** responsibility for the checking sits in an organisation separate from the one building the software.
- **Financial:** the budget for the checking is controlled by an organisation independent of development.

Table 4.1 tests each of Actual's existing V&V activities against these three kinds of independence. *Partial* means the check is independent of the implementer but limited: automated tests check only what the team chose to test, and community testing of preview builds is informal. *Not established* means public evidence does not show either way.

*Table 4.1. Independence of Actual's existing V&V activities.*

| Activity | Performed by | Technical | Managerial | Financial |
|---|---|---|---|---|
| PR review | Another core maintainer (Actual Budget, n.d.-d) | Yes | No | No: reviewers share one stipend pool (Actual Budget, n.d.-e) |
| Release approval and smoke test | Two other maintainers approve; smoke tests follow (Actual Budget, n.d.-b) | Yes | No | No |
| CI tests and CodeQL scanning | Automated, configured by the team (Actual Budget, 2026a) | Partial | No | No |
| PR preview and nightly builds | Any community member, voluntarily (Actual Budget, n.d.-f) | Partial | Not established | Not established |
| Vulnerability reports | Reporters outside the core team (Actual Budget, 2026c) | Yes | Not established | Not established |
| External audit | No public evidence found in the documentation and blog (October 2026) | — | — | — |

Actual therefore has real independent checking, but it is ad hoc and mostly technical: how independently a change is checked depends on who happens to review or report it, not on how risky it is. The strongest independent findings came after release: the three 2026 advisories described in Section 3.3 credit reporters outside the core team with finding the flaws in released versions (Actual Budget, 2026b, 2026c, 2026d).

## 4.2 IV&V integration model for Kanban (to-be)

To make independent checking depend on risk rather than on who happens to review, the model makes three changes.

First, it uses the risk tiers set at triage (Section 3.5), so that only High-tier cards get extra independent checks. Independent review of every card would overload the few reviewers that Section 2 identified as the bottleneck.

Second, High-tier changes get an *independent reviewer*: a maintainer who neither wrote the change nor is listed for that area in Actual's CODEOWNERS file (Actual Budget, 2026a). For a new bank-sync endpoint, both the implementer and the sync server's listed owner are excluded, so someone else on the team must check it. The reviewer is still a colleague paid from the same stipend pool, so this gives technical independence only.

Third, the other two kinds of independence come from outside Actual's team and budget. One route already exists: outside reporters using private vulnerability reporting (Section 3.3), who found the three advisories examined in Section 4.1. The other is new: an occasional external security audit of the sync server, where those flaws were, paid for by a third party rather than from Actual's donations. The Open Source Technology Improvement Fund (OSTIF) arranges such audits for OSS projects with money from outside funding bodies, and reports that over 98% of the security-relevant findings from its 2025 audits were fixed (Open Source Technology Improvement Fund, 2026).

Each check is written into the exit policy of the board column where it happens, so a High-tier card cannot move on until its independent evidence is attached. This follows Smith and Hayes (2024, Abstract), who argue that agile "has in no way diminished the need for IV&V" and that IV&V should run in phase with the development cadence. High-tier reviews also count against the Verify column's WIP limit, so if they queue up, new work stops entering and the queue is visible on the board. Table 4.2 shows, for each column, who checks a High-tier card independently and what evidence they leave.

*Table 4.2. Independent checks at each board column.*

| Board column | Checks | Tools | Checker | Exit policy |
|---|---|---|---|---|
| Requirements/triage | *Validate* that acceptance criteria are testable and cover security and data needs; assign the risk tier (all cards) | Issue templates, triage labels | Triager other than the requester | Tier and testable criteria recorded |
| Design | *Verify* the design listed in Table 3.2 (endpoints, permissions, migration and sync impact) against ASVS and select the requirements that apply | Decision record, OWASP ASVS 5.0.0 | Independent reviewer | Design accepted; ASVS requirements selected |
| Build/PR | Automated checks from Table 3.2 run on every PR (all cards) | GitHub Actions, CodeQL, Vitest | None (automated) | CI green, including the authorisation test matrix |
| Verify | *Verify* the code against the selected ASVS requirements and that each acceptance criterion has a passing test; for migration, sync or calculation changes, *verify* that balances and envelope totals on a synthetic budget match before and after; *validate* behaviour on a preview build (Standard and High) | GitHub review, preview builds, Playwright, separate test server | Independent reviewer; validator other than the implementer | Approval names the ASVS requirements and tests checked; validation evidence attached; no open high findings |
| Release train | *Verify* that every High-tier card in the release met its Verify exit policy | Release checklist | One of the two approving maintainers | Evidence confirmed before approval and tagging |
| Operate/maintain | Triage external reports; for each fixed advisory, add a regression test and re-check the tier of the area involved | Private vulnerability reporting, advisories | External reporters; optional funded auditor; a reviewer other than the code owner for the tier re-check | Advisory published; regression test merged; tier rule corrected if the area was under-tiered |

Standard-tier cards skip the design review and need only preview-build validation; Low-tier cards follow normal review. Preview and nightly web builds have no sync server and are not meant for real budgets (Actual Budget, n.d.-f), hence the separate test server.

## 4.3 How the integration meets the three goals

The integration of IV&V is meant to achieve three goals: early defect detection, requirements compliance and better overall software quality. Each is tested below against Actual's own evidence.

For early defect detection, the model would have given the critical 2026 bank-sync flaw (Section 3.3) two independent chances to be caught before release; in practice it was found only afterwards. A card that adds bank-sync endpoints is High tier, so it meets the independent reviewer twice. The first time is at Design, before any code exists: the reviewer checks each planned endpoint against the ASVS authentication requirements, so an endpoint planned without a login check is flagged there. The second is at Verify, where the reviewer confirms that every endpoint is in the authorisation test matrix (Section 3.5). This second check matters because the matrix tests only the endpoints someone adds to it, and an implementer who forgot the login check could easily forget the test as well.

For requirements compliance, the model checks that what users asked for is what was built and tested. Actual already records most of the evidence: a feature request starts as an issue, the PR links back to that issue, and a release note describes the result (Actual Budget, 2026a). What it lacks is anyone checking that these pieces match, and the model adds that check at both ends of the board. At triage, someone other than the requester confirms that each acceptance criterion can actually be tested, so a vague criterion such as "the page should feel fast" is sent back to be made measurable. At Verify, the independent reviewer does not approve until every criterion has a passing test. A requirement therefore cannot reach a release without evidence that it was met.

The model improves overall quality by moving independent checking to the code where Actual's worst 2026 flaws were (Section 4.1), and to before release rather than after, while a theme or wording change still needs only one ordinary review. Defects that still escape are put to use: the Operate/maintain column turns each one into a regression test and asks whether its area was tiered too low, so the process checks for that kind of defect next time.

<!-- Cited: S01, S03, S04, S08, S62, S63-m2cq, S63-prp4, S63-cq9c, S66, S67, S68, S69, S72 -->

# References

Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025/

Actual Budget. (2026a). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual

Actual Budget. (2026b, June 12). *Disabled OpenID users keep access through existing session tokens* (GHSA-cq9c-6w48-qmfg) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-cq9c-6w48-qmfg

Actual Budget. (2026c, February 20). *Missing authentication for SimpleFIN and Pluggy AI bank sync endpoints* (GHSA-m2cq-xjgm-f668) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-m2cq-xjgm-f668

Actual Budget. (2026d, April 23). *Privilege escalation via 'change-password' endpoint on OpenID-migrated servers* (GHSA-prp4-2f49-fcgp) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-prp4-2f49-fcgp

Actual Budget. (n.d.-a). *Contributing to Actual Budget*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/

Actual Budget. (n.d.-b). *How to cut a release*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/releasing/

Actual Budget. (n.d.-c). *Installing Actual*. Retrieved October 22, 2026, from https://actualbudget.org/docs/install/

Actual Budget. (n.d.-d). *New core contributors guide*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide/

Actual Budget. (n.d.-e). *Paying reviewers for administrative work*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors/

Actual Budget. (n.d.-f). *Preview builds*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/preview-builds/

Actual Budget. (n.d.-g). *Security policy* [SECURITY.md]. GitHub. Retrieved October 22, 2026, from https://github.com/actualbudget/.github/blob/main/SECURITY.md

Actual Budget. (n.d.-h). *Syncing across devices*. Retrieved October 22, 2026, from https://actualbudget.org/docs/getting-started/sync/

Actual Budget. (n.d.-i). *Testing*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/testing/

Actual Budget. (n.d.-j). *A tour of Actual*. Retrieved October 22, 2026, from https://actualbudget.org/docs/tour/

Ahmad, M. O., Dennehy, D., Conboy, K., & Oivo, M. (2018). Kanban in software engineering: A systematic mapping study. *Journal of Systems and Software, 137*, 96–113. https://doi.org/10.1016/j.jss.2017.11.045

Beck, K., & Andres, C. (2005, June 10). *Getting started with eXtreme Programming: Toe dipping, racing dives, and cannonballs: Appendix: Primary practices*. InformIT. https://www.informit.com/articles/article.aspx?p=390816&seqNum=3

Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer, 21*(5), 61–72. https://doi.org/10.1109/2.59

Brown, S., II. (2026, September 15). *[AI] fix(sync): receive only the latest timestamp to stop counter overflow* (#8706) [Commit]. GitHub. https://github.com/actualbudget/actual/commit/5f60f2971ca0f4a84133ba43a047a9f7b029d409

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

National Aeronautics and Space Administration. (n.d.). *IV&V overview*. Retrieved October 22, 2026, from https://www.nasa.gov/ivv-overview/

Open Source Technology Improvement Fund. (2026, January 30). *2025 annual report*. https://ostif.org/2025-annual-report/

OWASP Foundation. (2025). *OWASP application security verification standard* (Version 5.0.0). https://owasp.org/www-project-application-security-verification-standard/

Salkever, A. (2023). *Open source maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects*. The Linux Foundation. https://doi.org/10.70828/lddj8886

Schwaber, K., & Sutherland, J. (2020). *The Scrum guide*. https://scrumguides.org/scrum-guide.html

Smith, J., & Hayes, W. (2024). Independent verification & validation (IV&V) for agile developed projects. In *2024 IEEE Aerospace Conference* (pp. 1–10). IEEE. https://doi.org/10.1109/AERO58975.2024.10521415

Stacoviak, A., & Santo, J. (Hosts). (2022, July 1). *Actual(ly) opening up with James Long* (No. 495) [Audio podcast episode]. In *The Changelog*. Changelog Media. https://changelog.com/podcast/495

Wessel, M., Serebrenik, A., Wiese, I., Steinmacher, I., & Gerosa, M. A. (2022). Quality gatekeepers: Investigating the effects of code review bots on pull request activities. *Empirical Software Engineering, 27*(5), Article 108. https://doi.org/10.1007/s10664-022-10130-9

Wessel, M., Vargovich, J., Gerosa, M. A., & Treude, C. (2023). GitHub Actions: The impact on the pull request process. *Empirical Software Engineering, 28*(6), Article 131. https://doi.org/10.1007/s10664-023-10369-w

World Wide Web Consortium. (2024, December 12). *Web content accessibility guidelines (WCAG) 2.2* (W3C Recommendation). https://www.w3.org/TR/WCAG22/

youngcw. (2025, December 20). *Roadmap for 2026*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2026/

# Appendix A: Methodology Selection

*Supporting detail for Section 2.2: how Kanban was selected.*

## A.1 Project characteristics and requirements

Actual's situation is first described against the eight factors commonly considered when selecting a software process model (GeeksforGeeks, 2025). Each factor points either to an iterative, agile model, suited to changing requirements and close customer involvement, or to a linear model such as Waterfall, suited to stable requirements, fixed deadlines and predictability. Table A.1 applies the factors to Actual; the last column shows which kind of model each points to.

*Table A.1. Actual against the selection factors.*

| Factor | Actual | Points to |
|---|---|---|
| Project requirements | Evolving: new requests arrive continuously and are re-ranked by users' votes (Actual Budget, 2026a) | Agile |
| Size and complexity | Small: eight core maintainers plus volunteers (Actual Budget, n.d.-a). Waterfall suits small projects only when requirements are straightforward, which Actual's are not | Agile |
| Flexibility and adaptability | Priorities shift with votes, and each monthly release ships whatever is ready (Actual Budget, n.d.-b) | Agile |
| Customer involvement | Users shape the work continuously through requests and votes (Actual Budget, 2026a) | Agile |
| Risk tolerance | Low: defects can mislead money decisions and expose financial data (Actual Budget, 2026c) | Linear |
| Time constraints | A fixed monthly release date, but no feature is promised for it (Actual Budget, n.d.-b) | Agile |
| Team expertise | Cross-functional volunteers who choose their own work (Actual Budget, n.d.-a, n.d.-d); the few experienced reviewers have been overloaded before (Aboltins, 2025) | Agile, but under strain |
| Regulatory compliance | No regulatory requirements found in Actual's documentation (October 2026) | No constraint |

Most factors point to an agile model, but two pull against it. Agile models need an experienced, self-disciplined team, and low risk tolerance favours linear models (GeeksforGeeks, 2025). Actual's experienced reviewers are few volunteers whose review time has already run out once, and a wrong balance can lead a household to a poor spending decision; in 2026 a critical security flaw let anyone read users' bank balances and transactions without logging in (Actual Budget, 2026c).

Actual therefore needs an agile model at its core, with written controls added where team expertise and risk tolerance leave it exposed, as the same guidance recommends combining approaches when a project's needs are mixed (GeeksforGeeks, 2025). Table A.2 turns this profile into five requirements, each with the reason Actual needs it and the part of the brief it answers. Section A.3 tests every candidate against them.

*Table A.2. Requirements for Actual's methodology.*

| Requirement | Why Actual needs it | Brief's lens |
|---|---|---|
| Handles changing priorities | Votes keep re-ranking the work (project requirements, flexibility) | Stakeholder expectations |
| Works with self-chosen tasks | Volunteers cannot be assigned work (team expertise) | Constraints |
| Keeps its rules written down | Actual's core team has changed over time (Aboltins, 2025), so practices held only in people's heads would be lost (team expertise) | Risks |
| Protects review time | Reviewers are the bottleneck, and maintainers link administrative overload to burnout (Salkever, 2023, pp. 26–27) (team expertise) | Constraints, risks |
| Includes quality and risk controls | Defects affect money and private data, so low risk tolerance calls for more structure (risk tolerance) | Goals, risks |

## A.2 Candidate methodologies

The comparison focuses on five established methodologies, each representing a different approach: Spiral, Scrum, Extreme Programming (XP), Kanban and DevOps. Waterfall and the V-Model were not shortlisted, because they suit stable requirements and leave little room for change (GeeksforGeeks, 2025), whereas Actual's requirements change with every vote. RAD and RUP were set aside because their planned phases and deliverables assume a team that can be scheduled, whereas Actual's volunteers choose their own work. Spiral is included although it is not agile, because risk tolerance is the one factor on which Actual leans away from agile methods.

Actual's current process is also kept in the comparison as a reference point. It is not a candidate, but any change must prove better than today.

## A.3 Evaluation and selection

Each candidate is compared with how Actual works, using the requirements in Table A.2. The comparison can produce two kinds of finding:

- a **clash**, where the methodology demands something Actual cannot provide. A clash rules the candidate out, because removing it would mean abandoning the methodology itself;
- a **gap**, where the methodology does not cover one of the requirements. A gap does not rule a candidate out, because a missing practice can be added.

Every candidate is assumed to keep Actual's existing CI, review and monthly release, so none is credited for what Actual already does. Table A.3 sets out what each candidate requires of a team and the resulting findings; the paragraphs that follow explain them.

*Table A.3. What each candidate requires, and its clashes and gaps.*

| Candidate | What it requires of the team | Clash with how Actual works | Requirement left uncovered (gap) |
|---|---|---|---|
| Spiral | Repeated cycles, each starting with expert analysis of the largest remaining risk | The analysis would fall on the overloaded reviewers | Handles changing priorities |
| Scrum | Sprints of up to one month, a Sprint Goal the team commits to, a single Product Owner who orders the work, a daily 15-minute meeting | Needs a committed Sprint Goal and a single Product Owner | Protects review time |
| XP | Weekly planning, test-first development, pair programming, a team that sits together | Needs developers working side by side at the same time | Includes quality and risk controls (security, accessibility) |
| **Kanban** | A visible board, work-in-progress (WIP) limits and written rules for moving work, applied on top of an existing process | None found | Includes quality and risk controls |
| DevOps | Shared responsibility and automation across building and running the software | None found | Protects review time |
| Current process (reference) | Already in place | None | Protects review time; includes quality and risk controls |

First, three candidates clash with how Actual works. Scrum and XP both assume team members who commit their time together. Scrum's Sprint Goal "is a commitment by the Developers" and its Product Owner "is one person, not a committee" (Schwaber & Sutherland, 2020), while XP's pair programming needs two developers available at once, even when pairs work remotely (Beck & Andres, 2005). Actual's volunteers choose their own work and cannot promise to be available together, and its priorities come from users' votes, so neither assumption holds.

Spiral fits Actual's low risk tolerance best, because every cycle starts with risk analysis. That analysis, however, needs expert judgement (Boehm, 1988), which is why Spiral is usually described as complex and expertise-dependent (GeeksforGeeks, 2025). In Actual the experts are the same few maintainers whose review time is already the bottleneck.

Next, Kanban and DevOps have no clash, so the question is which would add more to what Actual already does. DevOps mainly adds automated testing throughout delivery (DORA, n.d.), which Actual's CI already provides, and integration with operations, which has little to attach to because users run the server themselves or through a hosting provider (Actual Budget, n.d.-c). Neither addresses Actual's real bottleneck: human review.

Kanban, in contrast, targets the problem identified in Section 2.1: nothing limits how many PRs wait for review. It adds three things. First, it limits work in progress (WIP), the number of items allowed in a stage at once (Kanban University, n.d.). This assignment proposes placing that limit on review: once it is reached, no new PRs enter review until waiting ones are cleared, which protects the maintainers' review time. Second, the rules for moving work from one stage to the next are written down, so they do not depend on who happens to be on the team. Third, contributors still pick tasks from the voted backlog whenever they have time, so nobody has to commit to a fixed amount of work as Scrum would require.

Finally, Kanban has to be better than keeping today's process. The gain is modest but real: Actual's process already suits volunteers, and Kanban adds a review limit and written rules on top of it rather than replacing it. Kanban does not, however, say how quality should be checked, for example which tests a change must pass, and this matters because Actual's risk tolerance is low. The report therefore adds **mandatory quality gates (QA gates)**: checks, defined in Section 3, that every change must pass before it moves to the next stage. **The selected methodology is Kanban, tailored with mandatory QA gates.**

# Appendix B: Worked Example of the QA Plan

*Supplementary illustration of Table 3.2 (Section 3.5).*

Suppose a contributor adds a new bank-sync provider, the kind of change behind GHSA-m2cq-xjgm-f668 (Section 3.3). At triage, the card is marked High tier because it touches bank sync, and an acceptance criterion is written: every new endpoint must refuse requests without a valid login. At design, the implementer lists the new endpoints and who may call each one. At Build/PR, the endpoints are added to the authorisation test matrix. If the login check is missing, that test fails and the card cannot move to Verify, so a flaw like the 2026 one could be stopped before release. A typo fix in the documentation, by contrast, is Low tier and passes through the normal checks only.
