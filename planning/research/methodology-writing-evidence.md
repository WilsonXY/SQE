# Section 2 writing evidence and checks

Prepared 22 October 2026. Scope: Assignment 1 only, local Markdown work. No commit, push, PR or remote change. Humanizer skill installation exists at `C:/Users/xingy/.codex/skills/humanizer/SKILL.md`; its contents have deliberately not been read during original drafting.

## Draft status

- Original prose: `report/assignment-1/before/02-methodology.md`.
- Sections 2.1–2.3 and 2.5–2.6 drafted normally. **2.4 is deliberately absent until the author approves matrix scores.** The author has requested score revisions and is explaining them to the parent agent.
- Kanban is now the report recommendation under the approved volunteer-oriented criteria. This is a draft recommendation, not a claim of universal superiority or final author sign-off on the complete prose.
- Current whitespace count: 1,429 words including headings, tables and diagram text; 1,258 alphanumeric/hyphenated tokens. Table pipe characters account for much of the difference. The agreed target is approximately 1,400 words; exact counts depend on the final report tool.
- British English; third person; no citations to lecture slides. Markdown fenced diagrams remain readable in a plain-text reader.
- APA n.d. suffixes will be assigned centrally once the full report reference set is final. Unsuffixed placeholders currently distinguish sources only through this evidence map.

## Paragraph-to-source map

| Location / claim | S-ID | Source support and limits |
|---|---|---|
| 2.1 voluntary involvement/core review | S04 | Official live guide read this session. Does not name a formal methodology. The absence statement is limited to reviewed documentation. |
| 2.1 voting requests, CI checks | S01 | Official voting workflow re-read; other CI evidence retained from detailed planning inspection at commit 27290a8. A workflow does not prove check effectiveness. |
| 2.1 small versus large proposals | S02 | Contributor expectations re-read on official site. |
| Figure 2 monthly cut, release approval/build/smoke/announcement | S03 | Live release guide read: cut 25th, 17:00 UTC; approval from two other maintainers; tagging triggers builds/publishing, smoke follows before final announcement. Corrects oversimplified assumption that smoke precedes every publication step. |
| 2.1 incremental feature flags | S07 | Entire short page read; users can provide feedback on smaller deliverables. |
| 2.1 historic review queue | S10 | Official blog read; history after 2022 opening, not evidence of current queue size. |
| 2.1 administrative stipend | S08 | Live guide read: USD 2,000 monthly pool; do not imply fixed salary or guaranteed individual payment. |
| 2.2 volunteer/burnout criteria | S47 | Prior-session full-text read and page-specific planning record; this session relies on that provenance, not a newly accessed PDF. |
| 2.2 weighted comparison | S42 | Prior-session verified abstract. Supports multi-criteria choice generally, not this report's exact scores/weights or simple-sum method. |
| 2.3 Spiral | S26 | Original 1988 paper read via university mirror; initial web PDF opened; later downloaded to temporary directory outside repository for pp70–72. Risk-based iteration, TRW application and expertise dependence verified. Model is adaptable, not inherently document-heavy. |
| 2.3 Scrum | S34 | Current official 2020 guide read for accountabilities, Sprint events, forecast capacity, changing scope and Definition of Done. Distributed use is not prohibited. |
| 2.3 XP | S105 | **Creators' official-publisher practice appendix read in full.** Permits adapting practices and remote pairing, describes weekly planning/test-first/CI. This accessible source clears the specific practice-content gap without claiming full book chapter 7 access. |
| 2.3/2.5 Kanban | S109 | Official Kanban University guide read; method overlays an existing workflow, evolutionary improvement, self-organisation, explicit pull criteria and WIP controls. Cadence/board design and limits are this report's recommendations. |
| 2.3 DevOps | S39 | Prior-session verified abstract: 93 documents, 37 capabilities, inconsistent adoption and conceptual clarity. Claim that automation does not order Actual's community backlog is analyst evaluation. No dependence on unread Accelerate book S30. |
| 2.3 OSS baseline | S108 | Author's original essay, version 3.0, copyright 2000, read via Stanford mirror. Do not cite unread 1999 book edition S24. |
| 2.4 matrix / recommendation | Author-approved analysis; S26, S34, S105, S109, S39 plus Actual baseline sources | Weights remain [3,3,2,3,2,2,3,2,2,2]. Approved totals: Kanban 102; baseline 95 (non-selectable); DevOps 94; XP 82; Scrum 81; Spiral 72. All options retain the same CI/tests; C4 rates methodological support, not Actual product quality; QA gate mandatory. Scores remain analyst judgement, not empirical effect sizes. Equal-weight sums independently checked: Kanban 42, DevOps 39, baseline 39, XP/Scrum 34, Spiral 30. |
| 2.3 excluded candidates | Internal selection reasoning, S23 search record | Search-limited screening judgement, not empirical proof of inferiority. No Shape Up/Scrumban source is cited because no detailed empirical claim is used. |
| 2.6 Kanban evidence/limitations | S38 | Publisher abstract re-read this session; prior-session full-text notes identify training/implementation/support practices. Direct source manuscript retrieval 403; no claim of fresh p. 98/p. 106 reading. |
| 2.6 practice-level tailoring | S36 | Prior-session verified abstract and recorded survey results; do not imply that common hybrids require inventing a hybrid for Actual. |

## Exact references cited by current prose

The parent should insert only these cited works into the central References and resolve the Actual Budget n.d. suffixes alphabetically by title. S01–S10 below are separate citations despite repeated author/date placeholders.

- **S01:** Actual Budget. (2026). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual
- **S02:** Actual Budget. (n.d.). *Contributing to Actual Budget*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/
- **S03:** Actual Budget. (n.d.). *How to cut a release*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/releasing/
- **S04:** Actual Budget. (n.d.). *New core contributors guide*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide/
- **S07:** Actual Budget. (n.d.). *Feature flags (experimental features)*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/project-details/feature-flags/
- **S08:** Actual Budget. (n.d.). *Paying reviewers for administrative work*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors/
- **S10:** Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025/
- **S26:** Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer,21*(5),61–72. https://doi.org/10.1109/2.59
- **S34:** Schwaber, K., & Sutherland, J. (2020). *The Scrum guide*. https://scrumguides.org/scrum-guide.html
- **S36:** Kuhrmann, M., Tell, P., Hebig, R., Klünder, J., Münch, J., Linssen, O., Pfahl, D., Felderer, M., Prause, C. R., MacDonell, S. G., Nakatumba-Nabende, J., Raffo, D., Beecham, S., Tüzün, E., López, G., Paez, N., Fontdevila, D., Licorish, S. A., Küpper, S., … Richardson, I. (2022). What makes agile software development agile? *IEEE Transactions on Software Engineering,48*(9),3523–3539. https://doi.org/10.1109/TSE.2021.3099532
- **S38:** Ahmad, M. O., Dennehy, D., Conboy, K., & Oivo, M. (2018). Kanban in software engineering: A systematic mapping study. *Journal of Systems and Software,137*,96–113. https://doi.org/10.1016/j.jss.2017.11.045
- **S39:** Amaro, R., Pereira, R., & da Silva, M. M. (2023). Capabilities and practices in DevOps: A multivocal literature review. *IEEE Transactions on Software Engineering,49*(2),883–901. https://doi.org/10.1109/TSE.2022.3166626
- **S42:** Song, Y., Mahmood, T., & Rehman, U. U. (2024). Selection of software development methodology by employing a multi-criteria decision-making approach based on logarithmic bipolar complex fuzzy aggregation operators. *IEEE Access,12*,38163–38179. https://doi.org/10.1109/ACCESS.2024.3373708
- **S47:** Salkever, A. (2023). *Open source maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects*. The Linux Foundation. https://doi.org/10.70828/lddj8886
- **S105:** Beck, K., & Andres, C. (2005, June 10). *Getting started with eXtreme Programming: Toe dipping, racing dives, and cannonballs: Appendix: Primary practices*. InformIT. https://www.informit.com/articles/article.aspx?p=390816&seqNum=3
- **S108:** Raymond, E. S. (2000). *The cathedral and the bazaar* (Version 3.0). https://web.stanford.edu/class/me228/pdf/cathedral-bazaar.pdf
- **S109:** Kanban University. (n.d.). *The official guide to the Kanban method*. Retrieved October 22, 2026, from https://kanban.university/kanban-guide/

S105–S110 are registered immediately in `planning/sources.md`. S106 is access-limited and uncited; S107 is the search/failure log and uncited; S110 corroborates the official method but is uncited; S111 supports only the alternative-method reassessment, not the report. No supplied reference PDF was copied into the repository.
