# QA writer notes — Section 3 (raw)

Output: `RUN/raw/sections/03-quality-assurance.md`. Final word count: **1,438** (`count_words.py`; target ~1,400, about 3% over).

No writing skill was opened or applied. No new sources were added. One registered source was re-opened: raw `PRODUCT.md` at `27290a8` and the live S09 testing guide, only to get section locators for the two direct quotes.

## Sources cited

S01, S03, S08, S09, S10, S38, S43, S44, S47, S51, S53, S55, S57, S58, S59, S60, S61, S62, S63, S82, S85.

Mapping notes for the coordinator:
- **S53** = ISO/IEC 25010:2023. The exact names of the nine characteristics were verified via S86/S81 (same work). "Inclusivity and user assistance" under interaction capability comes from the S81 foreword.
- **S55 / S57 / S58 / S59** are the original IDs. Their 22 Oct rechecks are S76 / S84 / S77 / S78; the content is the same. The ASVS chapter claim (authentication, session management, authorisation) rests on the S77 reading of V6/V7/V8. The claim that WCAG 2.2 "does not deprecate 2.1" rests on S78.
- **S60** covers two works: the badge criteria and Scorecard (rechecked as S83). The single citation `(Open Source Security Foundation, n.d.{S60})` supports both. The coordinator needs to split it into two n.d. references with suffixes.
- **S63**: two kinds of claim. (a) The aggregate "ten npm-package advisories, Oct 2025–Oct 2026: 1 critical, 3 high, 6 moderate, mostly sync-server access control" comes from the OSV query. (b) GHSA-m2cq-xjgm-f668 specifics come from the live advisory (20 Feb 2026, critical, CVSS 9.2, GoCardless had the middleware). The register suggests citing advisories individually. Claim (a) has no single APA work, so the coordinator must decide its reference form. One option is to cite only m2cq and soften (a) to "most published advisories".
- **S82** = IEEE 730-2026, cited at scope level only. First citation introduces the abbreviation "[IEEE]".
- **S85** = Lear (2023), replacing the S56 ISACA corporate form.
- **S61** = ISO/IEC/IEEE 29119-1:2022, written as "International Organization for Standardization et al., 2022". Confirm the APA form for three corporate authors.
- Direct quotes have section locators: S01 "Product Purpose section"; S09 "Testing Checklist section"; S38 p. 98.

## Evidence qualifications kept

- All gaps are stated as public-evidence findings: no evidence found in the repository (October 2026), and private practices may exist.
- Functional suitability gets Medium for *additional* effort, not lower importance. The reasoning uses existing calculation tests in `base.test.ts` and the fact that the advisories concern security. The draft does not claim there are no calculation defects.
- The encryption recovery warning is conditional (both the password and every local copy must be lost), per S51.
- The draft states that the GHSA-m2cq defect "reached a release". It does not say CodeQL failed: whether CodeQL was in place in Feb 2026 was not verified.
- The release guide is described without claiming that smoke tests come before publication.
- The S62 broken link is described as "returned HTTP 404 when checked" (checked 20 and 22 Oct).
- OpenSSF: "no public result found on 22 October 2026", not "never used".
- The Wessel studies are presented as observational and not predictive for Actual.
- IEEE 730 and the ISO standards: only scope was read, and the draft says so. No conformance claim is made.

## Decisions within the plan

- Quality views in 3.1 (user/product/process) are used as general lecture concepts and are **not attributed** to Garvin or any source, because no such source is registered. The coordinator may prefer to drop the "view" labels.
- The table 3.1 rating scale is defined as priority for *additional assurance effort*. That gives exactly three Highs: interaction capability, reliability and security. Compatibility and maintainability are Medium; performance, flexibility and safety are Low. These ratings are analyst judgements.
- 3.4 uses a 9-row decision table plus two prose paragraphs. 29119 is "reference only", deferred to Section 4.
- In 3.5 the QA plan is a 6-row Kanban-stage Definition of Done table: stage, exit policy, owner. The stage names match the Section 4 stages. The other IEEE 730-style plan elements (standards, measures, problem/vulnerability handling, roles) are covered in one paragraph. Independent roles are deferred to Section 4.
- One measure per attribute, named only: authorisation-matrix endpoint coverage, test coverage of core and sync-server packages, and automated accessibility violations. Definitions are left to Assignment 2.
- Server-side security tests use "a separate server with synthetic data", consistent with the contract point that preview/nightly builds have no sync server. This is stated as a recommendation, with no citation.
- 3.6 points to Section 4's risk tiers rather than defining them.
- No figure.

## Open points for the coordinator

1. Reference form for the S63 aggregate advisory count (see above).
2. Splitting S60 into two references.
3. The section is 38 words over target. It can be trimmed if the whole-report total runs high.
