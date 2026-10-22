# Mechanical checks — claude-opus-5-5/run-1

Tools: `writing-experiments/tools/count_words.py` (counting and similarity, as in protocol §8) and `writing-experiments/tools/check_protected.py` (protected-element multiset comparison against frozen raw).

## Input integrity

- The raw files were checked against `raw/manifest.md` after both editing conditions finished: all six `sections/*.md` hashes are OK.
- The installed skill files match the protocol §5 hashes (`input/skill-provenance.md`).
- `references.md` is byte-identical in raw, `humanizer/reviewed` and `pstack/reviewed`.

## Protected elements (headings, table rows, captions, code blocks, parenthetical and narrative citations, quotations, numbers/identifiers, added prose dashes)

| Version | Groups with differences | Detail |
|---|---:|---|
| humanizer/draft | 1 | 03: the in-text reference to "Table 3.2" was removed. The table and caption are unchanged. |
| humanizer/reviewed | 1 | Same as the draft |
| pstack/draft | 0 | — |
| pstack/reviewed | 0 | — |

The missing table reference was not treated as a required correction, because the raw draft already leaves Tables 1.1, 2.2, 4.1 and 4.2 unreferenced in the prose. It is an observation for the author, and it applies to the raw draft too.

## Word counts (sections only; references and front matter excluded)

| Section | Raw | Humanizer draft | Humanizer reviewed | pstack draft | pstack reviewed |
|---|---:|---:|---:|---:|---:|
| Executive summary | 200 | 202 | 205 | 205 | 205 |
| 1 Introduction | 548 | 531 | 532 | 539 | 539 |
| 2 Methodology | 1,432 | 1,482 | 1,482 | 1,481 | 1,484 |
| 3 QA | 1,421 | 1,472 | 1,471 | 1,456 | 1,456 |
| 4 IV&V | 1,360 | 1,372 | 1,379 | 1,379 | 1,379 |
| **Total** | **4,961** | **5,059** | **5,069** | **5,060** | **5,063** |

All versions are within 4,750–5,250. The raw version is the only one under 5,000, which the author prefers.

## Wording similarity (difflib on lower-case word tokens, section text including tables and diagrams)

| Pair | Ratio |
|---|---:|
| raw vs Humanizer (reviewed) | 0.911 |
| raw vs pstack (reviewed) | 0.937 |
| Humanizer vs pstack (reviewed) | 0.887 |
| Humanizer draft vs reviewed | 0.995 |
| pstack draft vs reviewed | 1.000 |

For reference, the same script on the GPT-6.1-Sol run's files gives raw vs Humanizer 0.752, raw vs pstack 0.804, and Humanizer vs pstack 0.767.

## Descriptive style counts (prose only: tables, headings, captions and diagrams excluded)

| Version | Bold spans | Sentences | Mean words/sentence | SD | Semicolons | Colons | "not … but" / ", not" contrasts |
|---|---:|---:|---:|---:|---:|---:|---:|
| Raw | 32 | 194 | 19.5 | 12.3 | 21 | 23 | 12 |
| Humanizer | 3 | 211 | 18.4 | 9.9 | 12 | 21 | 4 |
| pstack | 25 | 242 | 16.0 | 10.7 | 6 | 14 | 13 |

These are crude regex counts. They describe surface changes and say nothing about quality.
