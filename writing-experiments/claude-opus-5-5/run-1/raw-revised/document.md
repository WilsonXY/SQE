# Software Quality Engineering Evaluation of Actual Budget: Methodology, Quality Assurance and IV&V

*Assignment 1 — raw condition (run claude-opus-5-5/run-1), revised 24–26 October 2026 after author feedback on Section 2. The frozen original is `archived/writing-experiments/claude-opus-5-5/run-1/raw/document.md`. Working title; cover page, table of contents and lists are added at final assembly.*

# Executive Summary

This report evaluates Actual Budget, a free, open-source, local-first personal finance application run by a small volunteer team. Its users need to trust the numbers it shows and the security of their financial data.

Actual has a defined workflow but no deliberate methodology. Judged with Boehm and Turner's framework for comparing agile and plan-driven methods, Actual suits an agile approach, except that its few reviewers are overloaded and its defects can affect users' money and data. Of five candidates, Kanban fits best because it directly limits the review backlog. Mandatory quality gates are added because Kanban itself prescribes no quality practices.

The QA process focuses on three ISO/IEC 25010:2023 characteristics: Security, Reliability and Interaction capability. Public evidence shows gaps in proactive security verification, coverage measurement and accessibility testing. The proposed QA plan adopts OWASP ASVS 5.0.0, WCAG 2.2 and OpenSSF tools and embeds a Definition of Done in each Kanban stage.

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

A software development methodology is the agreed way a team organises its work, from deciding what to build to releasing it. This section recommends one for Actual. Because a methodology can only be judged against the project it must serve, the section first describes how Actual works today (2.1) and what kind of project it is (2.2). It then introduces five candidate methodologies (2.3), tests them against Actual's needs and selects one (2.4), shows how the choice would work in practice (2.5) and examines its weaknesses (2.6).

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

To choose fairly between methodologies, Actual's situation must first be described in a form that methodologies can be compared against. Using an established framework for this, rather than the report's own scoring, makes the comparison easier to check.

Methodologies broadly fall into two families. Agile methodologies aim for rapid value and quick responses to change, working in short cycles and relying on people sharing knowledge directly. Plan-driven methodologies aim for predictability, stability and high assurance, relying on detailed plans and documents agreed in advance (Boehm & Turner, 2004, pp. 26–27, 35). Boehm and Turner (2004) compared the two families and found that each succeeds best under particular conditions, which they call its "home ground" (p. 51). They reduced these conditions to five factors that can be checked for any project (pp. 54–56):

- **size:** how many people work on the project;
- **criticality:** how much harm a defect can cause;
- **dynamism:** how fast the requirements change;
- **personnel:** how many experienced people are available;
- **culture:** whether people work best with freedom or with clear rules.

Table 2.1 applies the five factors to Actual. The second column states the conditions in which agile methods do best; the third gives the evidence for Actual; the last shows where Actual sits as a result.

*Table 2.1. Actual against Boehm and Turner's five factors.*

| Factor | Agile methods suit (Boehm & Turner, 2004, pp. 55–56) | Actual | Result |
|---|---|---|---|
| Size | Small teams | Eight core maintainers plus volunteers (Actual Budget, n.d.-a) | Agile |
| Dynamism | Frequently changing requirements | Priorities change with every vote (Actual Budget, 2026a) | Agile |
| Culture | People who prefer freedom | No assigned roles or tasks (Actual Budget, n.d.-e) | Agile |
| Personnel | Experienced people available at all times | A few experienced volunteers, already overloaded by review (Aboltins, 2025) | Agile, but under strain |
| Criticality | Defects that cause little harm | Defects can mislead money decisions and expose financial data (Actual Budget, 2026c) | Between the two |

Three factors point clearly to an agile methodology, but the other two need explanation. On personnel, agile methods depend on experienced people being continuously available (Boehm & Turner, 2004, p. 55). Actual has such people, but they are few, they are volunteers, and their review time has already run out once. On criticality, Boehm and Turner rank the harm a defect can cause on a scale running from loss of comfort, through loss of money, to loss of life (p. 56). Actual's defects cannot cost lives. However, a wrong balance can lead a household to a poor spending decision, and in 2026 a critical security flaw allowed anyone to read users' bank balances and transactions without logging in (Actual Budget, 2026c). This places Actual in the middle of the scale, away from the low-harm end where agile methods are most at home.

Boehm and Turner advise that each factor that does not fit should be treated as a risk to be managed (p. 57). A project that matches one family on most factors but not all is likely to need "some mix of agile and plan-driven methods" (p. 54). For Actual, this means an agile methodology at its core, with stricter, written controls added where personnel and criticality leave it exposed.

Five requirements follow from this profile. Table 2.2 lists them, with the reason Actual needs each one and the part of the brief it answers: Actual's goals, constraints, risks or stakeholder expectations. Section 2.4 tests every candidate against these requirements.

*Table 2.2. Requirements for Actual's methodology.*

| Requirement | Why Actual needs it | Brief's lens |
|---|---|---|
| Handles changing priorities | Users' votes re-rank the work continuously (dynamism) | Stakeholder expectations |
| Works with self-chosen tasks | Volunteers choose their own work and cannot be assigned it (culture, size) | Constraints |
| Keeps its rules written down | Knowledge held only in people's heads is lost as they leave (Boehm & Turner, 2004, p. 35), and Actual's core team has changed over time (Aboltins, 2025) | Risks |
| Protects review time | Reviewers are the bottleneck, and maintainers link administrative overload to burnout (Salkever, 2023, pp. 26–27) | Constraints, risks |
| Includes quality and risk controls | Defects affect money and private data, and plan-driven methods handle quality requirements such as reliability better (Boehm & Turner, 2004, p. 39) | Goals, risks |

## 2.3 Candidate methodologies

Many methodologies exist, so the comparison focuses on five established ones, each representing a different approach. Plan-driven methods such as Waterfall were not shortlisted, because they expect requirements to stay largely stable (Boehm & Turner, 2004, p. 31), whereas Actual's change with every vote. Spiral is included although it is not agile, because criticality is the one factor on which Actual leans away from agile methods.

Table 2.3 summarises what each candidate requires of a team, because Section 2.4 compares those demands with how Actual works.

*Table 2.3. Candidate methodologies.*

| Candidate | Approach | What it requires of the team |
|---|---|---|
| Spiral | Risk-driven | Repeated cycles, each starting with expert analysis of the largest remaining risk |
| Scrum | Agile framework | Sprints of up to one month, a Sprint goal the team commits to, a single Product Owner who orders the work, a daily 15-minute meeting |
| XP | Agile engineering | Weekly planning, test-first development, pair programming, a team that sits together |
| Kanban | Flow management | A visible board, work-in-progress (WIP) limits and written rules for moving work, applied on top of an existing process |
| DevOps | Development and operations | Shared responsibility and automation across building and running the software |

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

Spiral fits Actual's criticality best, because every cycle starts with risk analysis. That analysis, however, needs expert judgement (Boehm, 1988), and in Actual the experts are the same few maintainers whose review time is already the bottleneck.

Next, Kanban and DevOps have no clash, so the question becomes which would add more to what Actual already does. DevOps mainly adds automated testing throughout delivery (DORA, n.d.), which Actual's CI already provides, and integration with operations, which has little to attach to because users run the server themselves or through a hosting provider (Actual Budget, n.d.-d). Neither of these addresses Actual's real bottleneck: human review.

Kanban, by contrast, adds what Section 2.1 found missing. A WIP limit on review stops new work from starting while PRs are piling up, which protects review time. Written rules for moving work between stages keep knowledge out of individual heads. And because volunteers pull work from the voted list whenever they are free, nobody has to commit to a Sprint.

Finally, Kanban is compared with Actual's current process. The improvement is real but modest: today's process already suits volunteers, and Kanban adds control over the review queue and written rules rather than a new way of working. Kanban also leaves one gap, because it does not prescribe quality practices such as testing. That gap corresponds to the criticality factor in Table 2.1, the factor for which Boehm and Turner advise adding stricter controls. It is therefore filled with **mandatory quality gates (QA gates)**: checkpoints, defined in Section 3, that every change must pass before it moves on. **Kanban, tailored with mandatory QA gates, is selected.**

## 2.5 Applying Kanban to Actual (to-be)

In practice, Kanban would be added on top of Actual's existing route rather than replacing it (Kanban University, n.d.). Figure 3 shows the proposed board. Each column is a stage that work passes through, and each has an **exit policy**: a written condition that must be met before work can be pulled into the next column (Ahmad et al., 2018, p. 98).

The Verify column, where review happens, carries the WIP limit. The limit should be set from the number of reviews the maintainers actually complete, so that new work stops entering once reviews start to pile up. Verify's exit policy is the QA gate from Section 3, which covers security, reliability and interaction capability, and Section 4 adds independent checks to each column. The monthly release stays as it is, and each release becomes the point at which the team checks whether the limits and policies need adjusting.

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

Kanban's main weakness is the gap identified in Section 2.4. A mapping study of Kanban in software engineering concludes that it is "a relatively basic flow tool that needs to be supported by additional practices" (Ahmad et al., 2018, p. 110). Without the QA gates and Actual's existing automated tests, the board would only display the queue rather than improve the work passing through it. The same study also reports difficulties with setting up and maintaining Kanban, organisational culture, missing supporting practices and training (Ahmad et al., 2018, p. 106).

Second, volunteering limits what a WIP limit can achieve. A limit cannot force anyone to review, and holding back new PRs may discourage newcomers, just as unanswered PRs do (Salkever, 2023). The limit should therefore act as a signal to the team rather than a hard block, and the paid review pool (Actual Budget, n.d.-f) should be directed at the Verify column.

Third, the evidence behind the choice has limits. Boehm and Turner's framework was written in 2004 to compare agile and plan-driven methods in general, not for volunteer open-source projects. Some of its scales are numerical, such as the share of requirements that change each month, but Actual publishes no such figures, so Table 2.1 rests on qualitative judgement from the cited evidence. No study was found showing Kanban improving a project like Actual, so its benefit over today's process is plausible but unproven. Adapting one named methodology, rather than following it exactly, is still reasonable: a large international survey found that few projects follow a single approach in pure form, and that the practices a team uses shape how agile it is more than the methodology's name does (Kuhrmann et al., 2022).

Finally, the recommendation depends on Actual's present situation. If Actual gained paid staff, the strain on personnel would ease and Scrum's commitments could become realistic. If it began running its own hosted service, DevOps would have operations to integrate. Either change would mean repeating the comparison.

<!-- Cited: S01, S02, S03, S04, S07, S08, S10, S25, S26, S34, S36, S38, S47, S105, S108, S109, S121, S123, S126, S63-m2cq -->

# 3 Quality Assurance Process

## 3.1 What Quality Means for Actual

Actual's product documentation defines success as "users trusting the numbers" (Actual Budget, 2026a, Product Purpose section). From the user's view, quality means balances and envelope totals that are correct, private and understandable. From the product view, it means properties such as sync-server access control and data integrity. From the process view, it means a workflow that produces those properties repeatedly.

Stakeholders weight these views differently. Users and families want correct, private budgets; self-hosters also run a server holding bank-sync credentials; volunteer maintainers need checks that do not consume scarce review time. A QA process for Actual must therefore protect financial data without stalling a volunteer flow.

## 3.2 Key Quality Attributes

ISO/IEC 25010:2023 defines nine product quality characteristics (International Organization for Standardization & International Electrotechnical Commission, 2023). Table 3.1 rates each for the *additional* assurance effort it deserves in Actual.

*Table 3.1. ISO/IEC 25010:2023 characteristics rated for Actual.*

| Characteristic | Reason | Priority |
|---|---|---|
| Functional suitability | Correct totals are essential, but budget-calculation tests already exist | Medium |
| Performance efficiency | Personal-scale data volumes | Low |
| Compatibility | Web, desktop and server must sync | Medium |
| Interaction capability | WCAG target set but unchecked | **High** |
| Reliability | Sync, migrations and recovery protect data | **High** |
| Security | Sensitive financial data; repeated advisories | **High** |
| Maintainability | Volunteer contributors; strong static checks exist | Medium |
| Flexibility | Several install options already supported | Low |
| Safety | No physical harm in scope | Low |

Functional suitability is not ranked lower because correct numbers matter less. The repository already tests budget recomputation, category totals and the exclusion of off-budget spending (Actual Budget, 2026a), while the published advisories concern security rather than calculation errors. It stays a release baseline, not an area for new effort.

**Security** is the top priority. Actual stores budgets and, on the server, bank-sync tokens that sit outside end-to-end encryption (Actual Budget, n.d.-i). **Reliability** covers data integrity across devices, database migrations and recovery; losing both the encryption password and every local copy makes an encrypted budget unrecoverable (Actual Budget, n.d.-i). **Interaction capability** includes inclusivity and user assistance. Actual targets WCAG 2.1 AA (Actual Budget, 2026a), so accessibility is a stated requirement, not an extra.

## 3.3 Current QA Practices and Gaps

Actual already runs substantial automated QA. Every pull request triggers linting, type checking, Vitest unit tests and a database migration check, and Playwright end-to-end and visual regression tests run on pull requests and in the merge queue (Actual Budget, 2026a, n.d.-j). CodeQL scans run on pull requests, on pushes and weekly (Actual Budget, 2026a). A release needs approval from at least two other maintainers and smoke tests of the Docker server and desktop app (Actual Budget, n.d.-c). A security policy offers private vulnerability reporting and coordinated disclosure (Actual Budget, n.d.-h).

Mapping these practices to the three attributes reveals gaps. Each is a public-evidence finding (no evidence found in the repository, October 2026); private practices may exist.

- **Security: proactive pre-release verification.** Critical and high-severity access-control flaws in the sync server were published in 2026 (Actual Budget, 2026b, 2026d). GHSA-m2cq-xjgm-f668, published on 20 February 2026 and rated critical (CVSS 9.2), reported missing authentication on SimpleFIN and Pluggy AI bank-sync endpoints, although the GoCardless integration had that protection (Actual Budget, 2026c). This inconsistency between similar integrations reached a release; an authorisation test matrix is the kind of check that would catch it. The security policy also states no response time, and its link to the current stable release returned HTTP 404 when checked (Actual Budget, n.d.-h).
- **Reliability: no coverage measurement.** The sync-server test configuration disables coverage (Actual Budget, 2026a), yet the testing checklist asks for "appropriate test coverage" (Actual Budget, n.d.-j, Testing Checklist section) with no measure behind it.
- **Interaction capability: no automated accessibility testing** was found despite the WCAG target (Actual Budget, 2026a).
- **Process: no written QA plan.** Quality rules are spread across documentation, templates and CI files. Performance testing is also absent from CI, but its low priority keeps it out of scope.

## 3.4 Selecting Standards and Practices

Table 3.2 evaluates general quality standards and open-source frameworks against Actual's volunteer, donation-funded context.

*Table 3.2. Standards and frameworks selected for Actual's QA process.*

| Standard / framework | Decision | Reason |
|---|---|---|
| ISO/IEC 25010:2023 | Adopt | Current quality model; frames 3.2 |
| IEEE 730-2026 | Adapt | Planning and control structure for a light QA plan |
| ISO 9001:2026 | Borrow principles | Certification needs an organisational management system Actual lacks |
| ISO/IEC 27001:2022 | Borrow principles | Risk-based thinking useful; ISMS certification disproportionate |
| CMMI V3.0 | Reject appraisal | Appraisal cost outweighs value for volunteers |
| OWASP ASVS 5.0.0 | Adopt selectively | Authentication, session and authorisation chapters match the advisories |
| WCAG 2.2 | Adopt (AA) | Current W3C Recommendation |
| OpenSSF Badge and Scorecard | Adopt | Lightweight, open-source-specific, largely automated |
| ISO/IEC/IEEE 29119-1:2022 | Reference only | Testing concepts; detailed testing belongs in Section 4 |

IEEE 730-2026, published in August 2026, supersedes the 2014 edition (Institute of Electrical and Electronics Engineers [IEEE], 2026). Only its scope was read, so Section 3.5 adapts its planning-and-control idea without claiming conformance. ISO 9001:2026 sets requirements for an organisation to show it consistently meets customer requirements (International Organization for Standardization, 2026), and ISO/IEC 27001:2022 covers establishing and improving an information security management system (International Organization for Standardization & International Electrotechnical Commission, 2022). Both assume a formal organisation, so only their customer focus and risk-based thinking transfer. CMMI V3.0 is the current model (Lear, 2023), but a maturity appraisal would buy a rating, not fewer defects. ISO/IEC/IEEE 29119-1:2022 supplies general testing concepts (International Organization for Standardization et al., 2022), applied in Section 4.

OWASP ASVS 5.0.0 provides a basis for testing technical security controls (OWASP Foundation, 2025). Its authentication, session management and authorisation chapters match the advisory pattern, so selected requirements, not a full verification level, become acceptance criteria for sync-server work. WCAG 2.2 is recommended for new work, although W3C states that it does not deprecate 2.1 (World Wide Web Consortium, 2024); moving the target to 2.2 AA is therefore a modest step. The OpenSSF Best Practices Badge is a criteria-based self-assessment and Scorecard runs automated checks for risky practices; no public result for Actual was found on 22 October 2026 (Open Source Security Foundation, n.d.-a, n.d.-b).

## 3.5 Applying the QA Process within Kanban

Kanban moves work between stages through explicit policies, the "entry" and "exit" criteria that decide when an item may be pulled (Ahmad et al., 2018, p. 98). The QA plan therefore lives on the board as a Definition of Done for each stage (Table 3.3), not in a separate document that volunteers may never open.

*Table 3.3. Compact QA plan embedded in the Kanban stages.*

| Kanban stage | Definition of Done (exit policy) | Owner |
|---|---|---|
| Requirements/triage | Risk noted; security, data and accessibility acceptance criteria written | Triager |
| Design | Server-side changes list endpoints and permissions; migration and sync impact stated | Author, area owner |
| Build/PR | Existing CI green; new endpoints added to the authorisation test matrix; coverage report produced | Author |
| Verify | Reviewer checks ASVS-derived criteria and automated WCAG 2.2 AA checks; server tests use a separate server with synthetic data | Reviewer |
| Release train | Two approvals; smoke tests; no open critical or high finding | Release maintainers |
| Operate/maintain | Reports handled privately; escaped defects add a regression test and a policy review | Security contact |

The other plan elements follow IEEE 730's planning-and-control concern (IEEE, 2026). Each attribute has one measure, defined in Assignment 2: endpoints covered by the authorisation matrix (security), test coverage of the core and sync-server packages (reliability) and automated accessibility violations on key screens (interaction capability). The security policy should add a response-time target and fix its broken link. Independent verification roles are specified in Section 4.

## 3.6 Critical Evaluation

The plan's main cost is volunteer time. Actual's USD 2,000 monthly stipend pool pays for review and triage work (Actual Budget, n.d.-f), and the project has already experienced pull requests waiting months for review (Aboltins, 2025). Every new exit criterion adds load, and maintainer interviews identify administrative overhead as a burnout risk (Salkever, 2023). The gates are therefore scaled by risk (Section 4 proposes tiers): a documentation change should not wait for an authorisation matrix.

Automation helps but is not free. After adopting GitHub Actions, projects saw more rejected pull requests and longer acceptance times (Wessel et al., 2023), whereas code review bots were associated with more merged pull requests and less discussion (Wessel et al., 2022). These observational findings cannot predict Actual's results, but show that each tool's effect needs monitoring.

Some limits remain. Automated accessibility checks cannot judge whether an envelope-budgeting task is understandable, so manual review is still needed. An OpenSSF badge is a self-assessment, not an audit. The standards were read only at scope level. The gaps rest on public evidence only.

<!-- Cited: S01, S03, S08, S09, S10, S38, S43, S44, S47, S51, S53, S55, S57, S58, S59, S60-badge, S60-scorecard, S61, S62, S63-m2cq, S63-prp4, S63-cq9c, S82, S85 -->

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

Boehm, B., & Turner, R. (2004). *Balancing agility and discipline: A guide for the perplexed*. Addison-Wesley.

DORA. (n.d.). *Test automation*. Retrieved October 26, 2026, from https://dora.dev/capabilities/test-automation/

Institute of Electrical and Electronics Engineers. (2025). *IEEE standard for system, software, and hardware verification and validation* (IEEE Std 1012-2024). https://standards.ieee.org/ieee/1800.2/7324/

Institute of Electrical and Electronics Engineers. (2026). *IEEE standard for software quality assurance processes* (IEEE Std 730-2026). https://standards.ieee.org/ieee/730/10854/

International Organization for Standardization. (2026). *Quality management systems — Requirements* (ISO Standard No. 9001:2026). https://www.evs.ee/en/iso-9001-2026

International Organization for Standardization & International Electrotechnical Commission. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC Standard No. 27001:2022). https://www.iso.org/standard/27001

International Organization for Standardization & International Electrotechnical Commission. (2023). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (ISO/IEC Standard No. 25010:2023). https://www.iso.org/standard/78176.html

International Organization for Standardization, International Electrotechnical Commission, & Institute of Electrical and Electronics Engineers. (2022). *Software and systems engineering — Software testing — Part 1: General concepts* (ISO/IEC/IEEE Standard No. 29119-1:2022).

Kanban University. (n.d.). *The official guide to the Kanban method*. Retrieved October 22, 2026, from https://kanban.university/kanban-guide/

Kuhrmann, M., Tell, P., Hebig, R., Klünder, J., Münch, J., Linssen, O., Pfahl, D., Felderer, M., Prause, C. R., MacDonell, S. G., Nakatumba-Nabende, J., Raffo, D., Beecham, S., Tüzün, E., López, G., Paez, N., Fontdevila, D., Licorish, S. A., Küpper, S., … Richardson, I. (2022). What makes agile software development agile? *IEEE Transactions on Software Engineering, 48*(9), 3523–3539. https://doi.org/10.1109/TSE.2021.3099532

Lear, R. (2023, April 10). *CMMI updates take performance improvements to the next level*. ISACA. https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2023/cmmi-updates-take-performance-improvements-to-the-next-level

Liu, S., Zhou, J., Hu, X., Côgo, F. R., Xia, X., & Yang, X. (2025). An empirical study on vulnerability disclosure management of open source software systems. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3716822

Mockus, A., Fielding, R. T., & Herbsleb, J. D. (2002). Two case studies of open source software development: Apache and Mozilla. *ACM Transactions on Software Engineering and Methodology, 11*(3), 309–346. https://doi.org/10.1145/567793.567795

National Aeronautics and Space Administration. (n.d.). *IV&V overview*. Retrieved October 22, 2026, from https://www.nasa.gov/ivv-overview/

Open Source Security Foundation. (n.d.-a). *FLOSS best practices criteria (passing badge)*. Retrieved October 22, 2026, from https://www.bestpractices.dev/en/criteria/0

Open Source Security Foundation. (n.d.-b). *OpenSSF Scorecard*. Retrieved October 22, 2026, from https://scorecard.dev/

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

