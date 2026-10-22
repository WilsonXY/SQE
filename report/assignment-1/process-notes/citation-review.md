# Citation review: raw and Humanizer reports

Reviewed 22 October 2026. Scope: `before/report.md`, `after/report.md`, shared `references.md` and the existing section evidence maps. No report files were changed. The pstack branch and its skills were not read.

## Result

No high-, medium- or low-severity citation findings within the requested scope. All 43 reference entries are cited in each report, and all identified in-text author–date citations resolve to the shared bibliography. No orphan reference or unresolved citation was found.

## Passed checks

| Check | Evidence and locations |
|---|---|
| Complete, identical bibliography | `references.md` contains 43 entries. The reference blocks beginning at line 376 of both assembled reports match that file exactly, excluding the heading and surrounding whitespace. |
| Actual Budget undated suffixes | All 11 entries, `n.d.-a` through `n.d.-k`, appear in both report bodies and resolve to the appropriate guide. *A tour of Actual* correctly sorts under “tour” after *Testing*, giving `n.d.-k`: `references.md:25`; both reports, lines 56 and 62. |
| Actual Budget dated suffixes | `2026a` identifies the software; `2026b` the disabled-user session advisory; `2026c` the missing-authentication advisory; `2026d` the password-change privilege-escalation advisory. Titles and suffixes agree with alphabetical ordering: `references.md:27–33`; both reports, lines 252 and 321. Dates agree with the IV&V evidence map: 12 June, 20 February and 23 April 2026 respectively. |
| Narrative citations | Checked possessive forms for Salkever and Song at line 132; Boehm in Section 2.3; Ahmad and Kuhrmann in Section 2.6; both Wessel studies at line 291; Smith and Hayes at line 305; Liu at line 323. Each resolves to the correct author group and year. These locations apply to both versions. |
| Corporate abbreviations | ISO/IEC are introduced in the full-author citation at line 228; W3C at line 246; IEEE at line 260; NASA at line 303. Subsequent abbreviated citations resolve consistently. IEEE (2025) correctly cites the standard numbered 1012-2024, whose publication year is 2025. |
| Same citation coverage after rewriting | Normalised parenthetical author–year occurrence counts agree across raw and Humanizer; narrative and figure-source citations were also inspected. The figure citation `Actual Budget (n.d.-c, 2026a)` was checked manually because its author sits outside parentheses. |
| Standard-access limits | Both reports, line 260, explicitly limit access to public scopes/previews and avoid a formal-conformity claim. At Section 4.3, the proposed risk tiers are explicitly separate from IEEE's prescribed levels. The standard-related claims remain at the scope/preview level supported by the evidence maps. |
| Evidence limits retained | Both versions preserve the public-evidence limitation for apparent QA gaps, the historical nature of the patched vulnerability, unverified reporter independence and the absence-of-public-audit-evidence qualification. The evidence maps document these distinctions. |

## Review boundary

This was a completeness and consistency check against the recorded primary-source work. It did not re-open broad research, inspect paywalled standards or claim independent verification of every source's full contents. The wider source register properly includes consulted but uncited material; those research-log entries are not orphan report references.
