# Assignment 1 validation record

22 October 2026. Scope: three Markdown versions of Assignment 1.

## Word counts

| Part | Raw | Humanizer | Pstack |
|---|---:|---:|---:|
| Executive summary | 208 | 219 | 212 |
| Introduction | 535 | 526 | 530 |
| Methodology | 1,373 | 1,399 | 1,411 |
| Quality Assurance Process | 1,406 | 1,424 | 1,380 |
| IV&V | 1,351 | 1,366 | 1,372 |
| **Total** | **4,873** | **4,934** | **4,905** |

All totals are within the agreed 4,750–5,250 range. The method counts whitespace tokens containing at least one letter or digit after removing Markdown-only delimiters, comments and link targets. It includes the executive summary, section headings, table cells, captions, notes and diagram text. Contents, figure/table lists and References are excluded. Counts in a submission application may differ slightly.

## Mechanical checks

Eighty-two integrity and consistency checks passed with no failures:

- Five section files in each version and all totals within range.
- Frozen raw section, assembled report and reference hashes still match the manifest.
- Reference files are byte-for-byte identical across the three versions.
- Headings, captions and table rows match the raw version.
- Diagram code blocks and inline code match the raw version.
- Parenthesised citation groups match in wording and occurrence.
- The set of numerical values is unchanged. Pstack repeats an existing edition year in explanatory prose; it adds no new numerical value.
- No unresolved Actual Budget author–date placeholders remain.

Matrix totals were also recomputed from the ten weights and scores: Spiral 72, Scrum 81, XP 82, Kanban 102, DevOps 94 and the non-selectable OSS baseline 95. The weights sum to 24 and the maximum is 120. Equal weights give Kanban 42/50 and DevOps 39/50.

Word-sequence similarity to the raw draft is 75.2% for Humanizer and 80.4% for pstack. This uses Python's `difflib.SequenceMatcher` with `autojunk=False` on lower-case word tokens in the five report sections, including constant table and diagram words. The calculation describes wording similarity, not quality, authorship or detectability.

## Citation and content review

The separate [citation review](process-notes/citation-review.md) confirmed all 43 reference entries are cited in the raw and Humanizer versions and that their citations resolve. Pstack retains the same citation groups and narrative source references; its reference list is unchanged. The main writer reviewed its citation-bearing paragraphs against the raw report.

Same-author suffixes distinguish Actual's software, individual advisories and documentation pages. The title *A tour of Actual* is sorted under T when assigning suffixes, so it is n.d.-k. Source dates and access limitations follow the writing evidence notes. Full standards were not available: the report uses public scopes and previews and makes no formal conformity claim.

Prose review specifically checked the limits of encryption, historical versus current figures, evidence of external-reporting independence, the proposed risk tiers, and the difference between existing practices and recommended gates. It corrected intermediate wording in both rewrite branches that could imply observed compromise or strengthen an evidence-limited statement. The original's narrower claims remain in the finished versions.

Exactly three quality characteristics receive High priority in the nine-row table: security, reliability and interaction capability. All three reports retain the required main-body decision matrix, compact QA plan and six-stage IV&V table. No essential argument was moved to an appendix.

## Files and scope

The deliverables are Markdown. No original briefs or lecture files were modified. No supplied reference PDFs were copied into the repository. Report recommendations were not implemented in the upstream software, and no software-test results, user interviews or contact with maintainers are claimed.

During the writing experiment, no commits, pushes, pull requests or PDF generation were performed. The author subsequently requested that the work be committed locally on `writing-experiment-6.1sol`. Nothing was pushed. The report versions are complete drafts for author review. This validation does not claim that a lecturer has approved them or that every factual statement has been independently audited beyond the recorded source checks.

Experiment artifact files are excluded from Git's line-ending conversion through `.gitattributes`, preserving their original bytes and recorded hashes when the branch is checked out elsewhere.

## Reproduce the section word counts

Run this Python snippet from the repository root. It counts the five section files, avoiding the duplicate text in each assembled report.

```python
from pathlib import Path
import re

def count_words(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    text = re.sub(r'^```.*$', '', text, flags=re.M)
    text = re.sub(
        r'^\s*\|?\s*[-:]+(?:\s*\|\s*[-:]+)+\s*\|?\s*$',
        '', text, flags=re.M,
    )
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    for marker in '|#*`':
        text = text.replace(marker, ' ')
    return sum(any(char.isalnum() for char in word)
               for word in text.split())

for version in ('before', 'after', 'pstack'):
    files = sorted(Path('report/assignment-1', version).glob('0*.md'))
    total = sum(count_words(file.read_text(encoding='utf-8')) for file in files)
    print(version, total)
```
