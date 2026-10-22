# Section 2: Humanizer edit record

22 October 2026. The complete frozen original was read before editing. Humanizer 3.1.0 was then read in full and applied to the entire section. The pstack skills and their output were not read.

- Input: `../before/02-methodology.md`.
- Output: `../after/02-methodology.md`.
- Counted words: **1,373 before; 1,399 after**. This uses the manifest's convention: meaningful whitespace tokens, including headings, tables, captions and diagram text, with Markdown delimiters excluded.

## Mark, rewrite and self-audit

The first pass marked repeated contrast constructions (§1), unnecessary framing before the evidence (§4), uniform bold candidate labels (§19), and sentences describing the document where the subject could lead (§25). The historical-backlog caveat and the distinction between methodology support and product quality were substantive qualifications, so their meaning was retained. The three selected quality attributes were also retained as three distinct requirements (§6).

The whole section was rewritten in neutral, third-person British English. Subjects and actions were made clearer where useful (§11), and longer phrases were simplified (§18). Candidate descriptions retain the same evidence and limitations. The first rewrite counted 1,422 words; the self-audit shortened repetition and awkward phrases to reach 1,399 without adding facts.

The final pass checked contrast patterns, paragraph endings, repeated openings and decorative formatting. Technical uses of “QA gate” remain. Proposal wording, the limits of descriptive evidence and the uncertainty of numerical scores remain because they affect the argument. The section still needs some negative statements to explain the baseline restriction, assurance requirements and the scope of the recommendation.

## Representative paragraph

**Before**

> Review capacity remains the more relevant concern. Aboltins (2025) describes PRs waiting months during the early community transition. The current USD 2,000 monthly administrative stipend recognises review and triage work (Actual Budget, n.d.-f). This establishes a historical coordination risk, rather than proving a current backlog.

**After**

> Review capacity is the more relevant concern. Aboltins (2025) describes PRs that waited months during the early community transition. The current USD 2,000 monthly administrative stipend recognises review and triage work (Actual Budget, n.d.-f). The earlier delays establish a historical coordination risk; they provide no measure of the current backlog.

The final sentence now names the evidence and its limit directly (§1, §11). The dates, amount, citation and distinction between historical and current evidence are unchanged. The rewrite is a style change, not a stronger finding.

## Preservation checks

- The frozen input still has SHA-256 `24d13bf6a479bb2c04a78a41ba491cced769c4e7dc0c2e789ec7a9292df824c0`.
- Headings and table rows match the input exactly, including all scores, weights and totals.
- Both fenced diagrams match the input byte for byte.
- Parenthetical citations retain their exact text and order; narrative author/date citations remain with the same claims.
- The number-token multiset is unchanged. No source, factual name or additional claim was introduced.
- No em or en dashes occur outside the preserved diagrams.

Only the final prose appears in the rewritten section. No raw file, reference list or remote repository was changed.
