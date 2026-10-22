# Assignment 1 writing-session decisions

## Final session status — 22 October 2026

The author approved the revised scores and Kanban with mandatory QA gates. The full raw report was completed, checked and frozen at 4,873 words. A Humanizer rewrite is complete at 4,934 words. At the author's additional request, another process used pstack technical-writing followed by unslop on the same raw input, producing a separate 4,905-word report without reading the Humanizer branch. All versions include 43 cited references. Complete files, the five-example comparison, provenance and validation are linked from `../../report/assignment-1/README.md`.

All work remained local, without commits, pushes, pull requests or PDF generation. Current decisions override the earlier pending-decision status notes below. No draft is represented as author-approved or lecturer-approved final work.

## Confirmed by the author

- 22 October 2026: local work only. No remote push or publication.
- Markdown is the reading deliverable. Figures may be handled separately if useful, but must remain intelligible from the Markdown report.
- Scope: Assignment 1 only.
- Delegated writers are authorised.
- Humanizer is installed once in the shared Codex skills directory for all writers. Each writer must complete the normal draft without reading or using it, then explicitly read and apply it in a second stage.
- Keep the full before and after versions for comparison.
- British English confirmed through the clarification response.
- The author selected 'Revise the scores — I’ll explain' in response to the initial Section 2 methodology matrix. This is not approval of the proposed scores.
- The author then questioned why Kanban scores only 3/5 for quality in a Software Quality Engineering assignment, and asked whether a method with stronger quality support could offer fewer trade-offs. Selection has been reopened. A quality-focused reassessment is being prepared; the initial scores remain unapproved.

## Working arrangements

- Root writer: introduction, source coordination, whole-report review, executive summary, references and assembly.
- Methodology writer: Section 2 and matrix proposal.
- QA writer: Section 3.
- IV&V writer: Section 4.
- Source IDs reserved to avoid clashes: QA S75–S89; IV&V S90–S104; methodology S105–S119; introduction and assembly S120 onwards.
- No writer edits another writer's section during drafting. Citation suffixes will be assigned centrally.
- Diagrams use original, readable text in the Markdown draft; no third-party screenshots or supplied reference PDFs are added.

## Evidence corrections during writing

- IEEE 730-2026 supersedes IEEE 730-2014. The QA writer verified the official IEEE catalogue; the report will use the published 2026 edition and describe its use at scope level unless full text is available.
- The live GitHub publication date of GHSA-m2cq-xjgm-f668 is 20 February 2026; the earlier screenshot's 21 February date may reflect a time-zone display. Use the live record consistently.
- A credited vulnerability reporter outside the core-maintainer list does not establish managerial or financial independence. The report will state the limits of public evidence.
- Preview/nightly web builds do not include a sync server. Proposed server-security tests must use a separate controlled server and synthetic data.
- XP's creator guidance allows adaptation and remote pairing. Any fit penalty must concern coordination cost in this volunteer setting, not an absolute prohibition on distributed work.
- Kanban's official guide describes a management method applied to an existing process. The assignment's methodology comparison must acknowledge this scope and explain why the selected flow-management approach still needs engineering and QA controls.

## Status of deliverables

Original drafting in progress. No section has been labelled author-approved or final. The Humanizer skill has not yet been read by the writers.

Introduction and conditional QA/IV&V normal drafts are available. Methodology subsections other than 2.4 are available as a conditional Kanban draft. These may need revision once the author settles the methodology. The executive summary, complete references, whole-report freeze and Humanizer stage await that decision.

The methodology reassessment is complete in `methodology-quality-reassessment.md`, with a shorter author-facing response at `../../report/assignment-1/methodology-decision.md`. The first matrix was revised for a common retained CI/test baseline and a consistent quality-support rubric. Revised totals under the original weights are Kanban 102, baseline 95 (non-selectable), DevOps 94, XP 82, Scrum 81 and Spiral 72, out of 120. These remain proposals, not an approved selection. Quality-first sensitivity scenarios are diagnostic only; weights must not be chosen merely to obtain a desired winner.
