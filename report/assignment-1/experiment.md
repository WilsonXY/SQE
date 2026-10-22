# Writing comparison: method and controls

For the complete reusable procedure, agent prompts and guidance on repeating the experiment with another model, see [the standalone experiment protocol](../../WRITING-EXPERIMENT-PROTOCOL.md). This file remains the shorter record associated with the original document.

## Question

How does the same Assignment 1 report change when edited with Humanizer, compared with pstack's technical-writing and unslop skills?

This is a practical comparison of three text versions. It is not an experiment showing whether software detects AI writing or whether a marker will prefer one version.

## Three versions

1. **Raw:** the complete report written normally, without applying either writing-skill workflow. Section writers used the agreed handoff, verified sources and assignment constraints. The original was checked for factual accuracy, APA citations and consistency before it was frozen.
2. **Humanizer:** a complete prose rewrite of the frozen raw report using Humanizer 3.1.0. Original section writers edited their sections; the main writer edited the executive summary and introduction.
3. **Pstack:** another agent rewrites the same frozen raw report using technical-writing followed by unslop. This agent does not read Humanizer's instructions, output or edit notes.

The pstack version is derived directly from the raw report. It is not a further edit of the Humanizer version.

## What is held constant

- Assignment 1 scope, agreed structure, British English and the approximately 5,000-word constraint.
- Third person, with first person permitted only in the personal-reason paragraph in Section 1.1.
- The approved methodology scores, Kanban recommendation and essential QA requirements.
- Factual claims, dates, names, numerical information, source support and qualifications of the evidence.
- APA citations, the 43-entry reference list, numbered headings, table data and readable text diagrams.
- Local files only, with no commits, pushes or pull requests.

The full raw report was frozen before skill-based editing began. The pstack agent read its skill instructions during setup but did not read or influence the raw draft at that stage. The main and raw section writers did not read the full writing-skill instructions until normal drafting was complete. Skill names and discovery descriptions were visible in the tool catalogue and searches; the raw version is a normal instructed assignment draft, not an unprompted sample.

## Limits of the comparison

The agents inherited the same model, GPT-6.1-Sol, but had different working contexts. The Humanizer section writers already knew their material; pstack used a separate process with the frozen draft. There is one output per workflow. Differences cannot be attributed solely to skill instructions, and the comparison does not establish a general winner across models or subjects.

Academic requirements take precedence where generic editing advice conflicts with the task. APA parentheses and source limitations remain. The three specified quality attributes remain three real priorities; they are not deleted as a supposed rhetorical pattern. Technical terms, standard titles and established tool names are preserved. Tables and figures are held constant, so the comparison concerns surrounding report prose.

Both rewrites must retain the full argument and remain within the agreed 4,750–5,250-word range. This constrains how aggressively a skill can shorten the report. A lower word count would not by itself establish better writing.

## Provenance and review

- [Raw manifest](raw-manifest.md) records the frozen file hashes, approximate word counts and installed skill hashes.
- Humanizer source: https://github.com/blader/humanizer . Installed skill: `C:/Users/xingy/.codex/skills/humanizer/SKILL.md`.
- Pstack sources: https://github.com/cursor/plugins/tree/main/pstack/skills/technical-writing and https://github.com/cursor/plugins/tree/main/pstack/skills/unslop . Installed under `C:/Users/xingy/.codex/skills/`.
- [Process notes](process-notes/) record the actual editing work, required exceptions and representative changes.
- [Sources register](../../planning/sources.md) records the wider research and writing-tool discovery. Writing skills are not included as evidence in the report References.

The final checks compare headings, tables, diagrams, citation groups and numerical tokens, then review the prose for changed meanings. Mechanical matches alone cannot establish semantic accuracy. Any corrected drift is recorded in the process notes or validation record.
