# Prompts sent in run claude-opus-5-5/run-1

Verbatim prompts as sent, in order. `{...}` marks the per-writer values filled in from the table.

## 1. Normal writers (sent 22 October 2026)

| Writer | Section | Output | Notes file |
|---|---|---|---|
| methodology | 2 | `raw/sections/02-methodology.md` | `raw/notes/02-methodology-writer.md` |
| qa | 3 | `raw/sections/03-quality-assurance.md` | `raw/notes/03-qa-writer.md` |
| ivv | 4 | `raw/sections/04-ivv.md` | `raw/notes/04-ivv-writer.md` |

```text
You are the {writer} writer in a writing experiment. Repository root:
C:\Users\xingy\Desktop\Degree L3 Sem1\SQE\SQE Assignment (branch writing-experiment-opus5.5).
Run folder: writing-experiments/claude-opus-5-5/run-1 (call it RUN).

Task: write Section {N} of Assignment 1 ({title}) from the shared brief,
source pack and contract. Use your normal writing process.

Read first, in this order:
1. RUN/input/contract.md  (binding; overrides anything else)
2. RUN/input/source-pack.md
3. planning/05-writing-handoff.md (§2 budget, §3 rules, §4 your section brief, §5 source readiness)
4. {plan file} and the evidence files for your section: {evidence files}
5. planning/research/writing-session-decisions.md
6. planning/research/actual-development-process.md and the planning/sources.md entries you cite
{section-specific notes}

Rules:
- Do NOT read or apply Humanizer, wilson-humanizer, technical-writing or unslop
  instructions during this phase. Do not open report/assignment-1/** (another
  model's outputs) or anything else under writing-experiments/ except RUN/input
  and your own output files.
- No new sources. You may re-open the URL of an already-registered source to
  check a detail. If a material evidence gap or an unresolved content decision
  appears, do not guess: record it in your notes file and tell me in your final
  message.
- Other sections are written by other writers in parallel. The coordinator
  writes Section 1. Refer to other sections by number only; do not write them.
- Use the {S-ID} citation placeholder convention from the contract and end the
  file with <!-- Cited: ... -->.
- Check your length with: python writing-experiments/tools/count_words.py <file>
  (target ~{target} words including tables, captions and diagrams).
- Work locally. Do not commit or push. Do not edit any file except your two outputs.

Save the complete normal draft to {output}. Save a short notes file to {notes}
recording: sources cited, any evidence gaps or qualifications, decisions you
made within the plan, and the final word count.

Do not start any experimental rewrite. Return when normal writing and its
ordinary checks are complete, with a short summary (word count, gaps, any
questions for the coordinator).
```

Section-specific notes:

- **methodology:** "Use the approved matrix in planning/research/methodology-quality-reassessment.md (section 'Revised score proposal under the unchanged agreed weights') exactly; the criteria C1–C10 and weights are in planning/02-methodology.md. Section 2.4 is approved and may be written. Figures: Fig 2 (as-is workflow) in 2.1, Fig 3 (to-be Kanban workflow) in 2.5. The full matrix goes in the body (contract: no appendices). Section 4 will build on the Kanban stages and explicit policies you define in 2.5, so name the board columns clearly: the IV&V writer has been told the stages are requirements/triage, design, build/PR, verify, release train, operate/maintain."
- **qa:** "Section 3 hangs the QA plan on the Kanban workflow chosen in Section 2 (stages: requirements/triage, design, build/PR, verify, release train, operate/maintain; explicit policies and Definition of Done). Use IEEE 730-2026, not 2014. No figures in Section 3 by default."
- **ivv:** "The selected methodology is Kanban with mandatory QA gates (Section 2). Use the six Kanban stages requirements/triage, design, build/PR, verify, release train, operate/maintain for the 4.4 table. Section 3 defines the QA gates; Section 4 adds independence on top, so do not duplicate the QA plan. No figures in Section 4 by default."

## 2. Humanizer editors (sent after the raw freeze, 22 October 2026)

Sent with SendMessage to the same three writer agents, resuming their drafting context. Per-writer values: section number, file name, frozen word count (1,432 / 1,421 / 1,360) and the list of coordinator pre-freeze edits to that file. Template:

```text
Phase 2 (Humanizer editing condition) for Section {N}. The complete normal draft is now frozen.

The complete normal draft is frozen at RUN/raw/sections/{file} (RUN = writing-experiments/claude-opus-5-5/run-1). The coordinator edited your file before the freeze: {edits}. See RUN/raw/notes/coordinator-assembly.md. Read the CURRENT frozen file, not your memory of your draft.

Read the full Humanizer instructions at C:/Users/xingy/.codex/skills/humanizer/SKILL.md (not the different "wilson-humanizer" skill). Apply the skill's complete rewrite and self-audit process to all prose in your section.

Follow the shared contract (RUN/input/contract.md), especially "Protected material" and its task-specific overrides: keep every citation exactly (author, year, suffix, locator) attached to the claim it supports; keep headings, captions, table contents, {the diagram text,} numbers, names and direct quotations unchanged; keep third person and British English; keep genuine categories and evidence limitations. Preserve supported claims and their qualifications. Do not add research or facts.
Length: keep your section within about ±5% of its frozen count ({count} words; check with python writing-experiments/tools/count_words.py) so the whole document stays within 4,750–5,250. Length is an observation, not a target; never pad.

Do not read the technical-writing or unslop skills, or anything under RUN/pstack/. Do not open report/assignment-1/**. Leave RUN/raw/** unchanged.
Write the final prose to RUN/humanizer/draft/{file}. Save a separate process note at RUN/humanizer/process/{file} describing: the patterns you identified, what you changed, where you deliberately overrode the skill because of the contract, the self-audit result, and the final word count. Do not commit. Reply with a short summary when done.
```

The coordinator applies the same Humanizer process to `00-executive-summary.md` and `01-introduction.md`, and reads no pstack material until its Humanizer work is finished.

## 3. Pstack editor (fresh agent, sent at the same time as section 2)

```text
You are the pstack editor in a writing experiment. Work in a separate context from the Humanizer editors.
Repository root: C:\Users\xingy\Desktop\Degree L3 Sem1\SQE\SQE Assignment (branch writing-experiment-opus5.5). RUN = writing-experiments/claude-opus-5-5/run-1.

Read the frozen raw input at RUN/raw/sections/ (00-executive-summary.md, 01-introduction.md, 02-methodology.md, 03-quality-assurance.md, 04-ivv.md, references.md; hashes in RUN/raw/manifest.md) and the shared contract at RUN/input/contract.md.
Read C:/Users/xingy/.codex/skills/technical-writing/SKILL.md and C:/Users/xingy/.codex/skills/unslop/SKILL.md in full.
Rewrite all assigned prose (all five section files) with technical-writing, then apply unslop. Keep this order.

Follow the contract, especially "Protected material" and its task-specific overrides, which take precedence over generic skill advice: keep every citation exactly (author, year, suffix, locator) attached to the claim it supports; keep headings, captions, table contents, diagram text, numbers, names and direct quotations unchanged; keep third person (no "you") and British English; keep academic parenthetical citations; keep genuine categories and evidence limitations even if a skill warns against triads or hedging. The one first-person exception is the personal-reason passage in 1.1. Preserve supported claims and their qualifications. Add no research or facts.
Length: keep each section within about ±5% of its frozen count (200, 548, 1,432, 1,421, 1,360; check with python writing-experiments/tools/count_words.py <file>) so the whole document stays within 4,750–5,250. Length is an observation, not a target; never pad.

Do not read Humanizer (C:/Users/xingy/.codex/skills/humanizer) or wilson-humanizer instructions, anything under RUN/humanizer/, the raw writers' notes are fine to read only if needed for context. Do not open report/assignment-1/** (another model's outputs). Leave RUN/raw/** unchanged.
Save final prose to RUN/pstack/draft/ using the same five file names, and copy references.md unchanged into RUN/pstack/draft/references.md.
Save a separate process note at RUN/pstack/process.md recording: skill order, the main patterns each skill flagged, task-specific exceptions where the contract overrode a skill, the self-audit result, corrections, and final word counts per section. Do not commit or push. Reply with a short summary when done.
```

## 4. Meaning and integrity reviewers (two fresh agents, blind labels, sent together)

The drafts were copied to `review/blind/A` (pstack) and `review/blind/B` (Humanizer); the key is in `blind-key.md`, outside the review folder. Both reviewers received this prompt, with only the label changed:

```text
You are a meaning and integrity reviewer in a writing experiment. Repository root: C:\Users\xingy\Desktop\Degree L3 Sem1\SQE\SQE Assignment. RUN = writing-experiments/claude-opus-5-5/run-1.

Compare the edited document in RUN/review/blind/{L}/ (files 00-executive-summary.md, 01-introduction.md, 02-methodology.md, 03-quality-assurance.md, 04-ivv.md) with the frozen raw input in RUN/raw/sections/ (same file names), under the shared contract RUN/input/contract.md.

Only open those files and the contract (you may consult planning/sources.md or planning/research/*.md if you need to check whether a claim is supported by the source pack). Do NOT open RUN/humanizer, RUN/pstack, RUN/blind-key.md, any process notes, any writing-skill files, other blind folders, or report/assignment-1/**. Do not edit any file except your report.

Check protected elements (a mechanical check already found citations, tables, captions, headings, diagrams, quotations and numbers unchanged; spot-check rather than redo it). Then review meaning paragraph by paragraph, including uncertainty, causal force and recommendations. Identify: invented claims; missing caveats or evidence limitations; changed source support (a claim moved away from the citation that supports it, or a citation now attached to a claim it does not support); wording that turns a proposal into an observed result or a possibility into a certainty; changed rankings, scope or recommendation strength; lost critical-evaluation content; contract violations (third person except 1.1, British English, no padding).

Separate REQUIRED corrections (meaning drift or contract violations) from OPTIONAL style preferences. Do not recommend changes merely to make the text resemble your preferred style, and do not judge which version reads better.

Correction policy: a correction is REQUIRED only if the edited text says something the raw text and its sources do not support, drops a qualification or claim that the raw text made, or violates the contract. For each REQUIRED item give: file, the exact edited sentence, the raw counterpart, why it is drift, and a minimal fix that restores the raw meaning while keeping the edited style.

Write your report to RUN/review/review-{L}.md and reply with a short summary (counts of required and optional items).
```

The coordinator applies the REQUIRED fixes identically to both conditions, in `humanizer/reviewed/` and `pstack/reviewed/`. Optional items are not applied.
