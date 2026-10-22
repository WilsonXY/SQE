# Assignment 1 Section 4: writing evidence and limits

Date: 22 October 2026. British English. Local work only; no commit, push or remote changes.

## Phase 1 delivery

Normal draft: `report/assignment-1/before/04-ivv.md`. Written without reading or applying Humanizer. The shared installation exists at `C:/Users/xingy/.codex/skills/humanizer/SKILL.md`; only its existence was checked. Phase 2 awaits the parent writer's announcement after every original section is complete.

**Selection reopened:** the parent writer reported that the author is reconsidering Kanban's quality trade-offs. This file and its draft remain a conditional Kanban working version. Do not treat the methodology or stage mapping as finally selected, and do not begin Humanizer while the author considers alternatives. The concepts, independence evidence and risk-based checking can inform a revised methodology integration.

Approximate word count: **1,364**, including headings, table captions and cells, excluding Markdown formatting, table separator rows and the source-tracking HTML comment. Table numbers 7 and 8 are provisional pending whole-report assembly. APA same-author year suffixes are intentionally left for whole-report normalisation.

## Corrections to the handoff

1. **Reporter independence:** [S63] directly credits iamsilk, Rex50527 and pyuysig with discovering the three vulnerabilities. It does not establish their organisational arrangements or funding. The original handoff's claim that all three independence dimensions are satisfied is unsupported. Table 7 records discovery attribution and leaves managerial/financial independence unverified. [S68] supplies the three-dimension definitions.
2. **Advisory dates:** live repository pages show 20 February, 23 April and 12 June 2026 for m2cq, prp4 and cq9c respectively. Earlier author screenshots were logged one day later; timezone rendering likely explains the difference, but the cause is not verified. Live dates are used in the reference metadata below.
3. **Preview limits:** [S66] says both preview and nightly web builds have no sync server. Server/authentication/synchronisation tests need a separate test instance. The proposal uses synthetic budgets rather than live personal finance data.
4. **Existing release order:** [S03] documents two other maintainer approvals, tag-triggered publication automation, smoke testing, then final announcement. The proposal adds candidate-build verification and required evidence as an exit gate; it does not claim that current smoke testing precedes every distribution action.
5. **IEEE tier limits:** [S67] official IEEE abstract was read and confirms integrity-level-dependent V&V requirements. Full standard unavailable; no prescribed level scheme, task table or compliance claim is used. High/standard/low are explicitly this report's proposal.
6. **Audit evidence:** no public evidence of an external audit was found in the earlier documented repo/docs/blog search [S01/S63 research snapshot]. The draft bounds the claim to public material reviewed; no claim that no audit ever occurred.
7. **Kanban explicit policies:** [S109], the official Kanban University guide, directly verifies movement criteria, joint agreement, WIP limits and feedback loops. It replaces the original draft's [S38] citation for this specific claim because the supplied S38 PDF is not available in this writing session. S38 remains a consulted planning source, not cited in this section.

## Claim-to-source map

| Draft location | Evidence / judgement | Sources |
|---|---|---|
| 4.1 paragraph 1 | Verification/validation scope; different integrity levels | [S67] official IEEE abstract only |
| 4.1 paragraph 2; 4.2 table; 4.6 paragraph 1 | Technical, managerial and financial independence; application to Actual is explicitly analytical | [S68] NASA primary account |
| 4.1 paragraph 3 | Agile IV&V remains relevant; security may be invisible in demos; assessment should match cadence | [S69] full abstract at authors' institution; full paper unread |
| 4.2 table | Existing maintainer review, release approvals, CI, previews | [S04], [S03], [S01 check.yml/codeql.yml], [S66] |
| 4.2 paragraphs 2–3; 4.5 paragraph 1 | Reporter credits; escaped vulnerabilities; missing authentication on six endpoints | [S63] three individual primary advisories |
| 4.2 paragraph 3 | Private reporting and coordinated disclosure | [S62] organisation security policy; [S70] accepted-manuscript abstract |
| 4.3 tier list; 4.4 table; 4.5 goals | Analyst recommendations, not existing policies or demonstrated outcomes | Inspired by [S67], implemented through [S109]; existing tools [S01/S03/S66] |
| 4.3 final paragraph | Optional funded external assessment; 24 audits and 231 findings in 2025 | [S72] OSTIF self-report, 30 January 2026 |
| 4.4 tools discussion | ASVS tests technical security controls; does not cover every quality attribute | [S58] official OWASP page, stable 5.0.0 confirmed |
| 4.6 paragraph 2 | Historical review bottleneck; superficial approval risk acknowledged by project | [S10], [S08] |
| 4.6 paragraph 3 | Documented monthly income and stipend allocation; implication for audit affordability | [S08]; no audit cost estimated |

## Exact reference metadata for the reference assembler

Only the sources below are cited in the Section 4 draft. Source IDs are planning metadata and should not appear in the report's references or prose. The parent writer must apply consistent same-author year suffixes across all report sections.

- **S01 (CI files within the repository):** Actual Budget. (2026). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual . The two checked files are at snapshot `27290a8`: https://raw.githubusercontent.com/actualbudget/actual/27290a8/.github/workflows/check.yml and https://raw.githubusercontent.com/actualbudget/actual/27290a8/.github/workflows/codeql.yml . This retains the existing report-wide S01 reference; the draft's collective documentation citation in 4.2 needs the repository's 2026 citation added during whole-report suffix normalisation.
- **S03:** Actual Budget. (n.d.). *How to cut a release*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/releasing/
- **S04:** Actual Budget. (n.d.). *New core contributors guide*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide/
- **S08:** Actual Budget. (n.d.). *Paying reviewers for administrative work*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors/
- **S10:** Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025/
- **S58:** OWASP Foundation. (2025). *OWASP application security verification standard* (Version 5.0.0). https://owasp.org/www-project-application-security-verification-standard/ . Official live identity page redirects to https://owasp.org/projects/asvs and confirms stable 5.0.0. Whole-report QA writer is checking the version's release date and specific requirements; Section 4 uses only the scope.
- **S62:** Actual Budget. (n.d.). *Security policy* [SECURITY.md]. GitHub. Retrieved October 22, 2026, from https://github.com/actualbudget/.github/blob/main/SECURITY.md
- **S63-m2cq:** Actual Budget. (2026, February 20). *Missing authentication for SimpleFIN and Pluggy AI bank sync endpoints* (GHSA-m2cq-xjgm-f668) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-m2cq-xjgm-f668
- **S63-prp4:** Actual Budget. (2026, April 23). *Privilege escalation via 'change-password' endpoint on OpenID-migrated servers* (GHSA-prp4-2f49-fcgp) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-prp4-2f49-fcgp
- **S63-cq9c:** Actual Budget. (2026, June 12). *Disabled OpenID users keep access through existing session tokens* (GHSA-cq9c-6w48-qmfg) [Security advisory]. GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-cq9c-6w48-qmfg
- **S66:** Actual Budget. (n.d.). *Preview builds*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/preview-builds/
- **S67:** Institute of Electrical and Electronics Engineers. (2025). *IEEE standard for system, software, and hardware verification and validation* (IEEE Std 1012-2024). https://standards.ieee.org/ieee/1800.2/7324/ . Official page explicitly has the correct standard despite the unusual URL path; active, published 22 August 2025; supersedes 1012-2016. Root/current source.
- **S68:** National Aeronautics and Space Administration. (n.d.). *IV&V overview*. Retrieved October 22, 2026, from https://www.nasa.gov/ivv-overview/
- **S69:** Smith, J., & Hayes, W. (2024). Independent verification & validation (IV&V) for agile developed projects. In *2024 IEEE Aerospace Conference* (pp. 1–10). IEEE. https://doi.org/10.1109/AERO58975.2024.10521415 . Full abstract read at https://www.sei.cmu.edu/library/independent-verification-validation-ivv-for-agile-developed-projects/ . Author institution lists Justin Smith and Will Hayes. No full-paper claims.
- **S70:** Liu, S., Zhou, J., Hu, X., Cogo, F. R., Xia, X., & Yang, X. (2025). An empirical study on vulnerability disclosure management of open source software systems. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3716822 . Crossref queried 22 October 2026: published 24 March 2025; no volume or issue fields; article-number `3716822`. Accepted manuscript https://xing-hu.github.io/assets/papers/tosem25shuhan.pdf has placeholder journal issue metadata. Do not invent a final volume/issue. `Cogo` without accent matches Crossref and manuscript; older source register has `Côgo`.
- **S72:** Open Source Technology Improvement Fund. (2026, January 30). *2025 annual report*. https://ostif.org/2025-annual-report/ . Primary organisational self-report, not independent evaluation of effectiveness.
- **S109:** Kanban University. (n.d.). *The official guide to the Kanban method*. Retrieved October 22, 2026, from https://kanban.university/kanban-guide/ . Official primary guide, explicit-policy and WIP sections read.

## Other consulted material

[S38] and [S47] planning records were read. S47's official publication page was checked for author and scope but is not needed in the report's final references. New source [S90] (Justin Smith's SEI blog, https://doi.org/10.58012/0X5F-EA19) was read and logged, including the Orion example; omitted from the draft to conserve words and avoid unnecessary aerospace detail. Search results, incidental rejected snippets and retrieval outcomes are recorded append-only in `planning/sources.md`.

## Integration decisions

The methodology writer confirmed the board **Backlog/triage → Ready/design → Build/PR → Verify → Release → Done**. Section 4's sixth lifecycle activity is maintenance, shown as **Done → Backlog** feedback, not a new maintenance column. Initial WIP limits should reflect available reviewers rather than an invented fixed number. The main table's gates are proposed policy; no software or workflow was changed in Actual Budget.
