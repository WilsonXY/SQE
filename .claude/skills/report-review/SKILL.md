---
name: report-review
description: Review checklist for the SQE assignment report. Use ONLY when the author says they are reviewing the work or report (e.g. "I'm reviewing section 3", "review time", "doing review on the report"), or asks for feedback on already-written report prose. Do NOT use while drafting or writing new prose, during planning, or for research; this skill is for the review stage only.
---

# Report review

The author is reviewing report prose that has already been written. Use this checklist to find problems and to fix the ones the author points out. It records what went wrong in Section 2 of Assignment 1 (October 2026), so the same problems can be caught in other sections.

**Scope:** review stage only. Do not apply it while drafting; writing follows `planning/05-writing-handoff.md` and `AGENTS.md`.

**Working report:** `report/assignment-1/report.md` (see `AGENTS.md`).

## How to run a review

1. Read the whole section the author names, as a reader new to the report would, before judging any single sentence.
2. Check it against the six problem areas below.
3. Report each finding with:
   - its location (subsection and the sentence quoted);
   - which problem area it falls under;
   - why it is a problem for the reader;
   - a suggested fix in plain words.
   
   Most serious first. Don't rewrite before the author agrees, unless they ask for a direct fix.
4. When the author doesn't understand a passage, explain it in plain words first. Their confusion is itself a finding: the passage needs rewriting.
5. After each agreed change, log it in `planning/discussion-log.md` (and the section's `planning/NN-*.md` file if a decision changed). Then commit and push, following `AGENTS.md`.

## The six problem areas

### 1. Weak grounding
- Choices rest on the writer's own numbers, weights or scores with no stated basis. Prefer an established framework, or a test that can be checked (for example, comparing what a method requires with documented facts).
- A claim is asserted, not argued. For every sentence ask: "Why is this written this way?" and "Is there enough context and evidence behind it?"
- A recommendation (for example, mandatory QA gates) has no stated reason linking it to the evidence.

### 2. Written for the writer, not the reader
- **No flow.** A sentence jumps to a new point without building context; paragraphs switch topics without signposting ("first", "next", "finally").
- **Insider shorthand.** Codes and labels the reader was never given (for example N1–N5), or compressed phrases such as "required elements", "earns credit", "documented fact", "keeps knowledge in conversation", "proof rule" or "class ownership".
- **Tables appear before they're explained.** Say what the columns mean before the table, and define terms such as "clash" and "gap" before using them.
- **Content without context.** For example, a list of ten methods each dismissed in half a sentence.
- **Context in the wrong places.** Context is missing where it's needed while other points are over-explained, which breaks focus.
- Test: could a reader who has read only the earlier sections follow this paragraph without asking the author?

### 3. Wrong focus or wrong reader level
- The report is about **software quality engineering for Actual Budget**, not a tutorial on methodologies, standards or tools. Cut background that explains a method itself (history, research programmes, long feature lists) unless it bears on Actual's quality. Put summaries in short tables; they don't need a citation per cell when the claim is cited elsewhere.
- The reader is **new to the report but technical**. Don't define basic software terms (pull request, pair programming). Do explain the report's own reasoning, labels and proposals.

### 4. Unfamiliar theory instead of lecture material
- If the lecture slides (`Lecture Slides/`) already cover the topic (framework, factors, model, definition, terminology, metric), the report should use or tailor that material. Flag outside theories the lecturer won't recognise.
- Slides are not cited: cite the slide's original source after checking it (`AGENTS.md`, *Citations* rule 8). For example, Lecture 2's selection factors are cited as GeeksforGeeks (2025).
- To check what the slides cover, convert them to text, for example: `soffice --headless --convert-to pdf`, then `pdftotext`. Work in the scratchpad, not the repo.

### 5. Citation and accuracy slips
- The page or paragraph locator doesn't cover every claim in the sentence.
- A factual claim has no citation.
- The report's own proposal reads as if it came from the source. Say "this report proposes…" where it does (for example, putting the WIP limit on review).
- A quote no longer fits the case after editing (for example, a qualifier was trimmed away so the quote now overstates the fit).
- When a citation is removed, check whether the reference is still cited elsewhere; if not, remove it from the References list and update `planning/sources.md`.

### 6. Compression, verbosity and repetition
- **Over-compression.** Shorthand and missing context often came from squeezing text to fit the word limit. Clarity comes first; the author handles word count separately.
- **Verbosity.** Wordy paragraphs that take several sentences to make one point. Simplify.
- **Repetition.** Two paragraphs making the same argument (for example, Scrum and XP clashing for the same reason) should be merged.
- **Structural slips.** For example, "Second," with no "First", or table numbers and cross-references left stale after an edit.
