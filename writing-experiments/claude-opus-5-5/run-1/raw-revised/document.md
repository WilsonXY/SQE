# Software Quality Engineering Evaluation of Actual Budget: Methodology, Quality Assurance and IV&V

*Assignment 1 — raw condition (run claude-opus-5-5/run-1), revised 24 October 2026 after author feedback on Section 2. The frozen original is `../raw/document.md`. Working title; cover page, table of contents and lists are added at final assembly.*

# Executive Summary

This report evaluates Actual Budget, a free, open-source, local-first personal finance application run by a small volunteer team. Its users need to trust the numbers it shows and the security of their financial data.

Actual has a defined workflow but no deliberate methodology. Boehm and Turner's five factors place it on agile ground, except for scarce reviewers and financial criticality. Kanban fits these conditions best because it targets the review bottleneck, and mandatory quality gates cover its lack of technical quality practices.

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

## 2.1 Current development process of Actual (as-is)

A methodology can only be judged against the project it must serve, and Actual already has an established process that any methodology would change rather than replace. Its contributing documentation names no methodology (no evidence found, October 2026), but it describes a consistent route for every change.

Figure 2 traces that route. Feature requests are labelled "needs votes", so the backlog is effectively ranked by community votes (Actual Budget, 2026a), and contributors choose their own work rather than being assigned it (Actual Budget, n.d.-a, n.d.-e). Each pull request (PR) passes continuous integration (CI) checks and then maintainer review (Actual Budget, 2026a, n.d.-e), with large features merged behind feature flags (Actual Budget, n.d.-b). Merged work leaves on a monthly release train that needs two further approvals and smoke tests (Actual Budget, n.d.-c).

Review is the weak point, because only maintainers can do it. After the 2022 open-sourcing, PRs waited months for a reviewer (Aboltins, 2025), and the project now pays for review and triage from a USD 2,000 monthly pool (Actual Budget, n.d.-f). Actual therefore has **a defined workflow but no deliberate methodology** (Figure 2): the steps are clear, but nothing limits how much work waits for the few people who can approve it.

```
Feature request --> "needs votes" backlog (ranked by votes)
                           |
                           v
                     Pull request
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

Choosing a method requires describing Actual's conditions in terms that methods can be tested against; Boehm and Turner (2004) supply them. They identified the "home ground" of agile and of plan-driven methods, the conditions in which each is most likely to succeed (p. 51), and condensed these into five factors (pp. 54–55). They also cover the brief's lenses: criticality reflects goals and risks, size and personnel the constraints, and dynamism and culture stakeholder expectations.

*Table 2.1. Actual against Boehm and Turner's five factors.*

| Factor | Agile home ground (Boehm & Turner, 2004, pp. 55–56) | Evidence for Actual | Position |
|---|---|---|---|
| Size | Small teams | Eight core maintainers plus volunteers (Actual Budget, n.d.-a) | Agile |
| Dynamism | Frequent requirement change | Backlog re-ranked by votes; monthly releases | Agile |
| Culture | Many degrees of freedom | No assigned roles (Actual Budget, n.d.-e) | Agile |
| Personnel | Scarce experts continuously present | Few expert volunteers, already the review bottleneck | Agile, strained |
| Criticality | Low loss from defects (scale centre) | Defects affect money decisions and private data | Middle |

Size, dynamism and culture put Actual on agile ground; the last two rows show where agile methods are exposed. Agile methods need continuously available experts (Boehm & Turner, 2004, p. 55), yet Actual's experts are the small group whose review time has already run out once. Criticality is the loss that defects can cause, on a scale from comfort through funds to lives (p. 56). Actual's defects cannot cost lives, but a wrong balance can mislead a household, and a critical 2026 advisory exposed bank balances and transactions without authentication (Actual Budget, 2026c). Actual therefore sits mid-scale.

Boehm and Turner treat such mismatches "as sources of risk" (p. 57), noting that a project fitting four factors but not the fifth needs "risk assessment and likely some mix of agile and plan-driven methods" (p. 54). Actual's methodology should therefore be agile in shape, with explicit discipline where personnel and criticality are exposed. Five needs follow and serve as the selection criteria:

- **N1.** Absorb vote-driven changes in priority without a fixed plan (dynamism).
- **N2.** Work with self-selected contributors who are not assigned roles or tasks (culture, size).
- **N3.** Keep coordination written: unwritten knowledge grows riskier as people rotate (Boehm & Turner, 2004, p. 35), and Actual's core team has changed over time (Aboltins, 2025).
- **N4.** Protect maintainers' review time; maintainer interviews link administrative overhead and consensus-heavy decision-making to burnout (Salkever, 2023, pp. 26–27).
- **N5.** Provide explicit quality and risk controls, where Boehm and Turner judge plan-driven methods well ahead (2004, p. 39).

## 2.3 Candidate methodologies

These needs narrow the field. Waterfall, the V-Model and RUP expect stable requirements, with change of about 1% a month (Boehm & Turner, 2004, p. 31), which a continuously re-ranked backlog is unlikely to respect (N1). FDD, Crystal Clear, DSDM and SAFe/LeSS assume class ownership, co-location or enterprise governance (N2, N3). A proof rule removed Shape Up (Singer, 2019), for which no peer-reviewed evaluation was found. Lean overlaps with Kanban, Scrumban (Meireles et al., 2026) combines two shortlisted methods, and the release train is a scheduling practice rather than a methodology.

Five candidates remain, each described by what its defining source requires, which 2.4 then tests:

- **Spiral:** risk-driven cycles relying on risk-assessment expertise (Boehm, 1988), kept because criticality is Actual's main non-agile factor.
- **Scrum:** Sprints of one month or less, a Sprint Goal the Developers commit to, one Product Owner who orders the backlog, and a Daily Scrum (Schwaber & Sutherland, 2020).
- **XP:** weekly planning, test-first programming, pair programming and a team that sits together, presented as practices to adapt rather than rules (Beck & Andres, 2005).
- **Kanban:** visualise work, limit work in progress (WIP), manage flow and make policies explicit; a management method applied to an existing way of working, not a complete methodology (Kanban University, n.d.).
- **DevOps:** capabilities shared across development and operations; a review of 93 documents found 37 capabilities but inconsistent adoption (Amaro et al., 2023).

The **OSS ("Bazaar") model** (Raymond, 2000; Mockus et al., 2002) describes Actual today, so it is a baseline that cannot be selected: the question is what a deliberate methodology would add.

## 2.4 Evaluation and selection

Each candidate's required elements are set against Actual's evidence. A candidate is rejected only where a required element contradicts a documented fact; an unmet need is a gap for tailoring to fill. Every option keeps Actual's CI, tests, review and release train, so none earns credit for them, and each must pass a **mandatory QA gate** stating who checks Security, Reliability and Interaction capability (Section 3) and what blocks a release.

*Table 2.2. Candidates tested against Actual's needs.*

| Option | Conflict with Actual | Gap left open |
|---|---|---|
| Spiral | Expert risk analysis each cycle (N4) | Voted priorities (N1) |
| Scrum | Sprint commitment; one Product Owner (N2) | Review queue (N4) |
| XP | Sitting together; pairing (N2, N3) | Security, accessibility (N5) |
| **Kanban** | None found | Quality practices (N5) |
| DevOps | None found | Review queue (N4) |
| OSS baseline | None (today's process) | Flow control (N4) |

Three candidates conflict with Actual in ways that tailoring could not remove. Scrum's Sprint Goal "is a commitment by the Developers", and its Product Owner "is one person, not a committee" (Schwaber & Sutherland, 2020), whereas Actual's contributors choose their own work and votes set priorities. XP permits remote pairing (Beck & Andres, 2005), but pairing still needs two people working at once, which self-selected volunteers cannot guarantee, and it keeps knowledge in conversation, which Boehm and Turner (2004) call fragile when people rotate (p. 35). Spiral suits criticality best, but it adds expert risk analysis to every cycle (Boehm, 1988) for the maintainers who already limit review.

Kanban and DevOps raise no conflict, so the question is what each would add. DevOps' automated feedback largely exists, because every PR runs CI, and its operations side has little to join: after the commercial product closed (Aboltins, 2025), users have run the server themselves or on third-party hosting (Actual Budget, n.d.-d). Neither addresses the review queue. Kanban supplies what 2.1 found missing: a WIP limit stops new work starting while reviews pile up (N4), written pull criteria replace knowledge held only by maintainers (N3), and pulling from a voted backlog needs no Sprint commitment (N1, N2).

Compared with the baseline, this gain is narrow: flow control and explicit policies, not a new way of working. Kanban also prescribes no tests, which leaves N5 open. That gap is the criticality mismatch that Boehm and Turner say needs disciplined practices, so mandatory QA gates close it. **Kanban, tailored with mandatory QA gates, is selected.**

## 2.5 Applying Kanban to Actual (to-be)

Kanban is layered over the route in Figure 2 rather than replacing it (Kanban University, n.d.). Each of six columns has an **explicit policy**, an exit criterion that must hold before work is pulled onward (Ahmad et al., 2018, p. 98; Figure 3). Verify carries a WIP limit set from observed review throughput (N4), and its exit policy is Section 3's QA gate (N5); Section 4 attaches IV&V activities to each column. The monthly cut remains the cadence and hosts a short flow review of limits and policies. What changes is a visible review queue, enforced limits and written, mandatory pull criteria.

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

Kanban's main weakness is the N5 gap. It is "a relatively basic flow tool that needs to be supported by additional practices" (Ahmad et al., 2018, p. 110), so without the QA gate and retained CI the board would only display the existing queue. Reported challenges include set-up, organisational culture, supporting practices and training (Ahmad et al., 2018, p. 106).

Volunteering adds risk, because a WIP limit cannot compel anyone to review, and blocked PRs may discourage newcomers as unanswered PRs do (Salkever, 2023). Limits should therefore act as signals, with the review stipend (Actual Budget, n.d.-f) directed at Verify.

The evidence is limited too. Boehm and Turner's framework addresses agile and plan-driven methods generally, not volunteer open source, and Actual publishes no change-rate figures for its partly numerical scales, so Table 2.1 is qualitative. No study found shows Kanban improving a project like Actual, so the gain is plausible but unproven. Tailoring one named method is still defensible, because processes commonly mutate into hybrids and practices matter more than labels (Kuhrmann et al., 2022). The choice should be revisited if Actual gained paid staff or its own hosted service, either of which would change the conditions it rests on.

<!-- Cited: S01, S02, S03, S04, S07, S08, S10, S18, S22, S25, S26, S34, S36, S38, S39, S47, S105, S108, S109, S121, S126, S63-m2cq -->

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

Amaro, R., Pereira, R., & da Silva, M. M. (2023). Capabilities and practices in DevOps: A multivocal literature review. *IEEE Transactions on Software Engineering, 49*(2), 883–901. https://doi.org/10.1109/TSE.2022.3166626

Beck, K., & Andres, C. (2005, June 10). *Getting started with eXtreme Programming: Toe dipping, racing dives, and cannonballs: Appendix: Primary practices*. InformIT. https://www.informit.com/articles/article.aspx?p=390816&seqNum=3

Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer, 21*(5), 61–72. https://doi.org/10.1109/2.59

Boehm, B., & Turner, R. (2004). *Balancing agility and discipline: A guide for the perplexed*. Addison-Wesley.

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

Meireles, M. A. C., Soares, K., Afonso, Á., Lobão de Araújo, L., Lobão, L., & Pinheiro, G. (2026). Scrumban in hybrid environments: An empirical investigation of organizational use and impact in development teams. *Journal of Software Engineering Research and Development, 14*(1), 498–516. https://doi.org/10.5753/jserd.2026.7887

Mockus, A., Fielding, R. T., & Herbsleb, J. D. (2002). Two case studies of open source software development: Apache and Mozilla. *ACM Transactions on Software Engineering and Methodology, 11*(3), 309–346. https://doi.org/10.1145/567793.567795

National Aeronautics and Space Administration. (n.d.). *IV&V overview*. Retrieved October 22, 2026, from https://www.nasa.gov/ivv-overview/

Open Source Security Foundation. (n.d.-a). *FLOSS best practices criteria (passing badge)*. Retrieved October 22, 2026, from https://www.bestpractices.dev/en/criteria/0

Open Source Security Foundation. (n.d.-b). *OpenSSF Scorecard*. Retrieved October 22, 2026, from https://scorecard.dev/

Open Source Technology Improvement Fund. (2026, January 30). *2025 annual report*. https://ostif.org/2025-annual-report/

OWASP Foundation. (2025). *OWASP application security verification standard* (Version 5.0.0). https://owasp.org/www-project-application-security-verification-standard/

Raymond, E. S. (2000). *The cathedral and the bazaar* (Version 3.0). https://web.stanford.edu/class/me228/pdf/cathedral-bazaar.pdf

Salkever, A. (2023). *Open source maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects*. The Linux Foundation. https://doi.org/10.70828/lddj8886

Schwaber, K., & Sutherland, J. (2020). *The Scrum guide*. https://scrumguides.org/scrum-guide.html

Singer, R. (2019). *Shape Up: Stop running in circles and ship work that matters*. Basecamp. https://basecamp.com/shapeup

Smith, J., & Hayes, W. (2024). Independent verification & validation (IV&V) for agile developed projects. In *2024 IEEE Aerospace Conference* (pp. 1–10). IEEE. https://doi.org/10.1109/AERO58975.2024.10521415

Stacoviak, A., & Santo, J. (Hosts). (2022, July 1). *Actual(ly) opening up with James Long* (No. 495) [Audio podcast episode]. In *The Changelog*. Changelog Media. https://changelog.com/podcast/495

Wessel, M., Serebrenik, A., Wiese, I., Steinmacher, I., & Gerosa, M. A. (2022). Quality gatekeepers: Investigating the effects of code review bots on pull request activities. *Empirical Software Engineering, 27*(5), Article 108. https://doi.org/10.1007/s10664-022-10130-9

Wessel, M., Vargovich, J., Gerosa, M. A., & Treude, C. (2023). GitHub Actions: The impact on the pull request process. *Empirical Software Engineering, 28*(6), Article 131. https://doi.org/10.1007/s10664-023-10369-w

World Wide Web Consortium. (2024, December 12). *Web content accessibility guidelines (WCAG) 2.2* (W3C Recommendation). https://www.w3.org/TR/WCAG22/

youngcw. (2025, December 20). *Roadmap for 2026*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2026/

