# Pstack rewrite process

22 October 2026.

## Input and isolation

The rewrite used the five frozen prose files under `report/assignment-1/before/` and the raw References file. The writing handoff and raw integrity manifest supplied scope and preservation requirements. No Humanizer instructions, Humanizer output or Humanizer process notes were read. The pstack text was not passed through Humanizer. No external research, facts or citations were added.

The five rewritten files are under `report/assignment-1/pstack/`, with their original filenames. References were copied byte-for-byte. The root writing process assembles the combined report and comparison. All work remained local, without commits, pushes, pull requests or publication.

## Skills and execution order

1. `C:/Users/xingy/.codex/skills/technical-writing/SKILL.md` guided the first prose pass. The pass clarified actors and conditions, split dense sentences, replaced abstract phrasing and retained the argument's qualifications.
2. `C:/Users/xingy/.codex/skills/unslop/SKILL.md` guided the subsequent review for inflated vocabulary, forced contrasts, redundant emphasis, synonym cycling and mannered or compressed prose. The final review also checked that clearer wording had not strengthened evidential claims.

Technical-writing explicitly requires unslop. Both were already installed, and neither required further dependencies. No installed skill was edited.

## Scope adaptations

The assignment is an analytical report. The skills' useful sentence rules were applied within that form. The agreed report structure took precedence over technical-writing's default of a single documentation mode. Its second-person default was replaced with the author's required third person. The personal-reason paragraph in Section 1.1 retained first person.

British English, existing technical names and standard editions were retained. Required APA citations retained their parentheses and exact citation text. Original headings and captions retained their numbering, wording and capitalisation. Tables, code-fence diagrams and inline code were protected from rewriting, including their existing punctuation, slashes, abbreviations and formatting. These assignment requirements took precedence over general skill rules about punctuation and sentence case.

The 20-word instruction and 25-word sentence guidance was treated as a clarity check, not an automatic limit. Citation groups and established names sometimes make a clear sentence longer. Necessary distinctions between proposals, documented practices, historical findings and limits of public evidence were preserved. No claim of certification, implementation or measured improvement was introduced.

## Main changes and examples

Long explanations were divided where the original sentence contained separate claims. Abstract descriptions were replaced with named checks or responsibilities where the raw draft already supplied them. Repeated terminology was retained instead of varying names for style. Qualifications received their own sentences where they governed the interpretation of evidence.

The examples below reproduce the local raw and rewritten text. They illustrate the editing method and are not additional report content.

### Executive summary

Before:

> These are judgements of project fit, rather than measured quality results.

After:

> These scores express judgements about project fit. They do not measure software quality.

### Section 1

Before:

> Their quality matters because incorrect balances or lost records can affect everyday decisions, while exposed transactions can reveal private information.

After:

> Incorrect balances or lost records can affect everyday decisions. Exposed transactions can also reveal private information.

### Section 2

Before:

> This establishes a historical coordination risk, rather than proving a current backlog.

After:

> The historical delays establish a coordination risk. They do not prove that a backlog persists today.

### Section 3

Before:

> These are limits of public evidence, not proof that no such activity occurs.

After:

> These findings describe the limits of public evidence. They cannot establish that the activities never occur.

### Section 4

Before:

> An external auditor should control technical methods and report findings without developer veto; a third-party funder should protect the assessment budget.

After:

> An external auditor should control technical methods and report findings without developer veto. A third-party funder should protect the assessment budget.

## Self-audit

Automated comparisons confirmed identical heading and caption sequences, all table rows, fenced diagrams, inline code and the multiset of parenthetical author-date citations for each file. Narrative citations retained their authors and dates. References have SHA-256 `84f039f53e9c2c7c8cb0a115ef143c6a425776f0859f383f4968425adb65458e`, matching the frozen raw copy. These checks establish preservation of the compared text, not independent verification of the underlying sources.

A prose scan found no second-person address or em dashes outside protected material. First person remains confined to the authorised paragraph in Section 1.1. Manual comparison checked that the selected attributes, methodology scores, standard editions, dates, figures, risk tiers and substantive limitations remained intact. A final evidential review retained advisory language for discussion of larger proposals, described missing authentication as allowing access, and kept improvement conditional. Feedback after release was qualified as potential exposure, without claiming observed compromise.

The count uses whitespace tokens containing a letter or digit after removing Markdown delimiters, link targets and comments. Fenced figure content counts; fence markers do not. Headings, captions, notes and table cells count. References and this process note do not. The same procedure reproduces all five counts in the frozen raw manifest.

| File | Raw | Pstack | Change |
|---|---:|---:|---:|
| 00-executive-summary.md | 208 | 212 | +4 |
| 01-introduction.md | 535 | 530 | -5 |
| 02-methodology.md | 1373 | 1411 | +38 |
| 03-quality-assurance.md | 1406 | 1380 | -26 |
| 04-ivv.md | 1351 | 1372 | +21 |
| Total | 4873 | 4905 | +32 |

The rewrite is within the requested 4,750–5,100 range. A submission application may count words differently. No separate factual audit was performed during this style-only branch, and no quality or readability improvement was experimentally measured.

## Optional skill-rule proposal

Technical-writing requests a proposed addition to unslop's abstract-metaphor rule. This optional proposal was not applied to the installed skill. It would make the replacement depend on the action intended, rather than substituting one vague term for another.

```diff
--- unslop/SKILL.md
+++ unslop/SKILL.md (proposal only)
@@
-### Plain speech
+For "touchpoint", name the review stage, interaction, or check.
+
+### Plain speech
```
