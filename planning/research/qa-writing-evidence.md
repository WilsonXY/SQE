# Assignment 1 Section 3: writing evidence

Date: 22 October 2026. British English confirmed by the author. Local files only; no commit, push, pull request or remote edit performed.

## Writing phase

Phase 1 original draft: `report/assignment-1/before/03-quality-assurance.md`.

The shared Humanizer installation exists at `C:/Users/xingy/.codex/skills/humanizer/SKILL.md`. Its instructions have **not** been read or used in Phase 1. The full original draft was written normally. Awaiting parent instruction before reading the skill and beginning a separate whole-section rewrite.

The methodology selection has been reopened by the author. Section 3.5 currently uses the proposed Kanban columns conditionally; QA requirements can transfer to a different selected method. No claim of a final methodology agreement is intended.

## Corrections to the planning handoff

- [S79, S82] **IEEE 730-2026 is published and active**, not under development: official publisher date 21 August 2026. IEEE 730-2014 is inactive-reserved, superseded. Draft adapts scope-level assurance planning/control concepts from 2026 and does not claim access to full clauses or conformity.
- [S75, S81, S86] Exact ISO/IEC 25010:2023 characteristic names checked against primary standard text in the GSO adoption preview: functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety. **The iTeh preview does not list all nine in its TOC**; an earlier append-only register note claiming that is explicitly corrected later in the register. GSO's primary adoption preview supplies all nine definitions; original ISO edition remains 2023, not 2025.
- [S76] ISO 9001:2026 validity from 16 September 2026 is confirmed by EVS, the Estonian standards body. Full standard not read.
- [S63, S80] GHSA-m2cq-xjgm-f668 repo publication **20 February 2026**, replacing the planning screenshot's 21 February date. Maintainer severity critical, CVSS4 score9.2. Patched version26.2.1; historical defect evidence is not a claim of present vulnerability. Root and IVV writer informed.
- [S51] Correct guide title: *Syncing Across Devices*. Encryption recovery warning is conditional: loss of both encryption password and local copy prevents recovery. A surviving local copy supports resetting the key. End-to-end encryption excludes bank-sync credentials and local storage. Do not repeat an unconditional lost-password assertion.
- [S59, S78] W3C recommends2.2 for future applicability but explicitly says2.2 does **not** deprecate or supersede2.1. Actual's target2.1 AA is a target, not an established conformance finding.
- [S85] CMMI article author is **Ron Lear**, dated10 April2023, rather than corporate-author ISACA. The model version V3.0 was confirmed; no formal maturity appraisal is proposed.
- [S43, S44, S87] Verified article numbers: Wessel et al.2023=131; Wessel et al.2022=108. Do not infer that Actions and code-review bots have identical effects or that observational findings predict Actual's results.

## Evidence-to-citation mapping

The main writer owns final APA suffix assignment and consolidated References. The following titles identify otherwise ambiguous Actual Budget corporate-author citations.

| Draft location / claim | Source IDs and source actually read | Citation/ref mapping |
|---|---|---|
|3.1 users and confidence;3.2 target, tests;3.3 workflows and coverage|S01/S80 fixed repo snapshot27290a8; live PRODUCT.md; `packages/loot-core/src/server/budget/base.test.ts`, `.github/workflows/check.yml`, `packages/sync-server/vitest.config.ts`; prior repository review in `actual-development-process.md`|Actual Budget(2026), *Actual* [Computer software]. Distinguish from advisory with2026 suffix.|
|3.2 ISO model and nine headings|S75 original ISO scope; S81 limited original preview; S86 original text in regional adoption preview|ISO & IEC(2023), ISO/IEC25010:2023; a single original-standard reference is sufficient, with accessed previews recorded here.|
|3.2 encryption/recovery|S51, live official sync guide read in full|Actual Budget(n.d.), *Syncing Across Devices*.|
|3.3 Vitest, Playwright, VRT and checklist|S09, live official testing guide read in full|Actual Budget(n.d.), *Testing*.|
|3.3 release approvals/smoke|S03, live release guide read|Actual Budget(n.d.), *How to Cut a Release*.|
|3.3 critical missing authentication|S63/S80 live repo advisory read incl summary/details/date/severity|Actual Budget(2026, February20), *Missing authentication for SimpleFIN and Pluggy AI bank sync endpoints*.|
|3.3 private reporting, policy broken link|S62 organisation SECURITY.md read; linked release-notes URL rechecked404|Actual Budget(n.d.), *Security policy*.|
|3.4–3.5 IEEE scope|S82 official IEEE catalogue read|IEEE(2026), IEEE730-2026.|
|3.4 QMS and ISMS|S76 EVS catalogue; S84 ISO scope page|ISO(2026), ISO9001:2026; ISO & IEC(2022), ISO/IEC27001:2022.|
|3.4 CMMI model|S85 full official bylined article read|Lear(2023).|
|3.4 ASVS technical chapters|S77 OWASP official project page and v5.0.0 V6/V7/V8 raw files read|OWASP Foundation(2025), ASVS5.0.0.|
|3.2,3.4–3.6 accessibility target and limits|S78 W3C2.2 official Recommendation read|W3C(2024).|
|3.4,3.6 badge and Scorecard|S83 official passing criteria and Scorecard page; terminal public project lookups on22 October: badge200 `[]`, Scorecard404|Open Source Security Foundation(n.d.), separate *FLOSS best practices criteria (passing badge)* and *OpenSSF Scorecard* references; assign n.d. suffixes.|
|3.6 automation tradeoffs|S87 primary publisher abstracts/introduction; matches S43/S44|Wessel et al.(2023), Article131; Wessel et al.(2022), Article108.|

## Exact reference candidates (only retain cited works)

- Actual Budget. (2026). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual
- Actual Budget. (2026, February 20). *Missing authentication for SimpleFIN and Pluggy AI bank sync endpoints* (GHSA-m2cq-xjgm-f668). GitHub. https://github.com/actualbudget/actual/security/advisories/GHSA-m2cq-xjgm-f668
- Actual Budget. (n.d.). *How to cut a release*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/releasing/
- Actual Budget. (n.d.). *Security policy* [SECURITY.md]. GitHub. Retrieved October 22, 2026, from https://github.com/actualbudget/.github/blob/main/SECURITY.md
- Actual Budget. (n.d.). *Syncing across devices*. Retrieved October 22, 2026, from https://actualbudget.org/docs/getting-started/sync/
- Actual Budget. (n.d.). *Testing*. Retrieved October 22, 2026, from https://actualbudget.org/docs/contributing/testing/
- Institute of Electrical and Electronics Engineers. (2026). *IEEE standard for software quality assurance processes* (IEEE Std 730-2026). https://standards.ieee.org/ieee/730/10854/
- International Organization for Standardization. (2026). *Quality management systems — Requirements* (ISO Standard No. 9001:2026). https://www.evs.ee/en/iso-9001-2026
- International Organization for Standardization, & International Electrotechnical Commission. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC Standard No. 27001:2022). https://www.iso.org/standard/27001
- International Organization for Standardization, & International Electrotechnical Commission. (2023). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (ISO/IEC Standard No. 25010:2023). https://www.iso.org/standard/78176.html
- Lear, R. (2023, April 10). *CMMI updates take performance improvements to the next level*. ISACA. https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2023/cmmi-updates-take-performance-improvements-to-the-next-level
- Open Source Security Foundation. (n.d.). *FLOSS best practices criteria (passing badge)*. Retrieved October 22, 2026, from https://www.bestpractices.dev/en/criteria/0
- Open Source Security Foundation. (n.d.). *OpenSSF Scorecard*. Retrieved October 22, 2026, from https://scorecard.dev/
- OWASP Foundation. (2025). *OWASP application security verification standard* (Version 5.0.0). https://github.com/OWASP/ASVS/tree/v5.0.0
- Wessel, M., Serebrenik, A., Wiese, I., Steinmacher, I., & Gerosa, M. A. (2022). Quality gatekeepers: Investigating the effects of code review bots on pull request activities. *Empirical Software Engineering, 27*, Article 108. https://doi.org/10.1007/s10664-022-10130-9
- Wessel, M., Vargovich, J., Gerosa, M. A., & Treude, C. (2023). GitHub Actions: The impact on the pull request process. *Empirical Software Engineering, 28*, Article 131. https://doi.org/10.1007/s10664-023-10369-w
- World Wide Web Consortium. (2024, December 12). *Web content accessibility guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/

GSO adoption preview supports access to original standard terminology; no independent GSO requirement is applied. If directly citing that accessed edition instead, use: GCC Standardization Organization. (2025). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model* (GSO ISO/IEC25010:2025, adopting ISO/IEC25010:2023). [Public preview URL in S86].

## Limits and report judgement

Only public scopes/previews were read for ISO/IEEE material; no clause-by-clause compliance, certification or prescribed full SQAP template is asserted. The table is the analyst's compact applied plan. Existing calculation tests justify a lower priority for *additional assurance effort*, not lower stakeholder importance of correct calculations. Functional suitability remains a release baseline.

The snapshot's absence claims are explicitly October2026 public-evidence findings. Live checks verify individual pages/metadata and do not establish a complete fresh audit of the upstream repository. Private security assurance may exist. The critical advisory shows a historical escaped defect and cross-integration inconsistency, not current vulnerability. The OpenSSF public lookups do not prove the tools were never run.

No test execution, software testing outcome, user interview or contact with Actual maintainers is claimed. Proposed quality gates, named measures and blocker examples are recommendations. Assignment2 metric definitions are excluded. Section4 owns detailed independent verification and validation design.

## Checks

- Nine ISO characteristic rows and exactly three High priorities retained.
- Standards selection addresses all handoff candidates; certification/appraisal rejection is reasoned; ASVS and WCAG adopted selectively.
- QA plan is in the body; no essential argument moved into appendices; no figure added.
- Third person and British English used.
- At most one proposed measure per selected attribute; no unsupported numeric threshold introduced.
- Original word count approximately1,430 including headings/table text, excluding Markdown delimiter-only lines; final count should be rerun after bibliography suffix alignment.
