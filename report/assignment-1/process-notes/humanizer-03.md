# Humanizer pass: Section 3

## Scope and sequence

The complete original report was frozen before this pass. Section 3 was read from `before/03-quality-assurance.md`, including the main writer's final citation suffixes, Table 4/Table 5 numbering and confirmed Kanban selection. Humanizer version 3.1.0 at `C:/Users/xingy/.codex/skills/humanizer/SKILL.md` was then read in full and applied to the whole section. Only the resulting prose was written to `after/03-quality-assurance.md`.

The original section was not edited. Neither the later comparison branch nor its skills or output was consulted.

## Marked patterns

- Section 3.1: “Quality therefore involves more than passing automated tests” staged a contrast before the stakeholder requirements. Humanizer §1 recommends stating the supported point directly. The revision connects those requirements to the limits of automated testing.
- Section 3.2: “These attributes interact” announced a relationship that the encryption example could explain more directly (§2). The revision makes that relationship explicit in the sentence introducing the documentation.
- Section 3.3: “Actual has a substantial technical foundation” and “A concrete security failure illustrates the limitation” announced judgements before giving their evidence (§2, §13). The revision opens with the testing practices and the dated advisory.
- Section 3.4: “The selection separates useful engineering guidance from organisational certification” narrated the section's organisation (§25). The individual decisions and their reasons already make the distinction clear.
- Throughout: repeated passive adoption formulas and long semicolon constructions gave successive paragraphs the same rhythm (§7, §11). Sentence boundaries and subjects were varied without changing the decisions.

## Representative comparison

Before:

> A concrete security failure illustrates the limitation. GHSA-m2cq-xjgm-f668, published on 20 February 2026, carries the maintainers' critical rating of 9.2.

After:

> The maintainers published GHSA-m2cq-xjgm-f668 on 20 February 2026 with a critical rating of 9.2.

This removes the staged introduction (§2) and keeps the advisory identifier, date, attribution and rating. The rest of the paragraph retains the affected integrations, missing authentication, comparison integration, recommendation and patched-release caveat.

## Rewrite and self-audit

Every subsection was reviewed and its prose rewritten around the original claims. The final self-audit checked the strongest surviving patterns: unnecessary contrasts (§1), explanatory closers (§2), triads (§6), dashes (§8) and decorative bold (§19).

Some patterns were deliberately retained because they carry evidence or satisfy the assignment:

- The three user groups, three selected attributes and three measures are distinct items, not invented rhetorical triads (§6).
- The distinction between public evidence and unobserved private activities is necessary to avoid unsupported absence claims. The same applies to limited standard access, no formal conformity claim and the historical vulnerability caveat (§9, §23).
- The studies' different interventions and their inability to predict Actual's results remain explicit. “Associated” retains the original evidential strength rather than introducing causation (§14).
- Bold table captions identify numbered report tables. Table contents and headings were preserved exactly as instructed (§19, §20).
- No em dash or en dash remains. Inline code is unchanged (§8).

Local checks compared all parenthetical citation strings, headings and Markdown table rows between versions; no differences were found in those protected elements. The two Wessel narrative citations remain unchanged. All names, dates, standards, versions and numerical claims were reviewed against the original.

Word counts using whitespace tokens after stripping Markdown markers and table delimiter-only lines: original 1,408; revised 1,426. These counts include headings and table text. The main writer may report slightly different totals under the report-wide counting method.

No new external sources or factual claims were introduced. All work remained local, without a commit or push.
