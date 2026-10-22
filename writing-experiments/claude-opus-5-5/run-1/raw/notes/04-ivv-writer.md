# Section 4 (IV&V) writer notes — run-1 raw

Output: `raw/sections/04-ivv.md`. Final word count: **1,398** (count_words.py; target ~1,370, +2%). No figure. Two tables: Table 4.1 (as-is independence), Table 4.2 (IV&V per Kanban stage). No Humanizer, wilson-humanizer, technical-writing or unslop instructions opened.

## Sources cited

S01, S03, S04, S08, S10, S38 (p. 98), S47, S58, S62, S63 (three advisories), S66, S67, S68, S69, S70, S72, S109.

- **S63 placeholders:** the three advisories are separate references, so the draft uses `{S63-m2cq}`, `{S63-prp4}`, `{S63-cq9c}`. Live GitHub dates per `ivv-writing-evidence.md`: m2cq 20 Feb 2026, prp4 23 Apr 2026, cq9c 12 Jun 2026. All three are "Actual Budget, 2026", together with S01 (also Actual Budget, 2026): the coordinator needs four 2026 suffixes (date-specific for the advisories).
- **S67:** IEEE 1012-2024, cited as 2025 (published 22 Aug 2025), abstract only. Only the V&V definition and "integrity levels" are used.
- **S70:** use "Cogo" (no accent, per Crossref), advance online publication with no volume or issue (see `ivv-writing-evidence.md`).
- **S72:** OSTIF figures are labelled as self-reported.
- **S38 p. 98** is used for entry and exit criteria, as the handoff planned. Its register entry is Verified (full text read 20 Oct). **S109** supports WIP limits. The earlier run replaced S38 with S109 because the PDF wasn't available. Both are in the source pack, so the coordinator may standardise on one.

## Live re-checks of registered sources (no new sources)

- S68 NASA page: verbatim definitions of technical, managerial and financial independence confirmed.
- S08 payment guide: USD 2,000/month stipend pool; USD 3,000–3,500 average monthly donations; LOC used as a proxy for review effort; the page itself asks "Could someone 'farm' points by doing rubber-stamp PRs?" and answers "Theoretically, yes." This supports the rubber-stamp point in 4.6 (paraphrased).

## Qualifications preserved

- Reporter credits show who discovered the flaws, not managerial or financial independence. Table 4.1 marks these as "Not established", following the contract over the original handoff's "all three".
- External audit: "No public evidence found (October 2026)", limited to the documentation and blog reviewed.
- Risk tiers are this report's own design, "inspired by" the IEEE 1012 integrity-level concept, and are not presented as IEEE's scheme.
- Preview and nightly builds have no sync server, so server and security tests use a separate controlled server with synthetic budgets.
- Release row: evidence is required before final approval. The draft does not claim that the current smoke test precedes publication (S03 ordering).
- The 4.5 GHSA-m2cq argument says the model gives a defined point at which the defect *could* be detected. It does not claim the defect would certainly have been caught. The draft does not say that any flaw was exploited.

## Decisions made within the plan

- The risk tiers are a bullet list in 4.3, not a table, to save words for the 4.4 table.
- The 4.4 table gives high-tier gates. One sentence after it scales them down for the standard and low tiers.
- Section 3 boundary: 4.3 says Section 3 defines *what* each gate checks and Section 4 adds *who* verifies it and what independent evidence is needed. This avoids repeating the QA plan.
- The internal independent reviewer is defined as "neither the author nor the code owner of the affected area" (CODEOWNERS exists per S01).
- The traceability chain in 4.5 says "a PR referencing the issue" and does not give the literal "Fixes #" syntax, which is not separately evidenced in the source pack.

## Evidence gaps / items for the coordinator

1. **Tool false positives (4.6):** "automated scanners may also raise findings that consume triage time" is analyst judgement with no citation. No registered source covers scanner false positives specifically. Keep it as judgement, cite S43/S44 if the QA writer's wording fits, or delete it.
2. **ASVS reference:** the draft cites S58 (OWASP project page). The QA writer's evidence uses S77 (the v5.0.0 GitHub tree) for the same work. The coordinator should merge these into one reference.
3. **"Within the documentation and blog reviewed"** relies on the October 2026 repo search recorded in `actual-development-process.md`. It was not re-run.
4. No unresolved content decisions.
