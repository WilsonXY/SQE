# Run record — claude-opus-5-5/run-1

Template from `WRITING-EXPERIMENT-PROTOCOL.md` §9. Fields are updated as the run progresses.

```text
Run ID: claude-opus-5-5/run-1
Date: 22 October 2026
Design: own raw per model (repeat of the whole workflow)
Model and provider: claude-opus-5-5 (Claude Opus 5.5), Anthropic
Harness: Claude Code (Claude Agent SDK) inside T3 Code, Windows 11
Available instruction stack and any unknown instructions:
  - Claude Code system prompt (not reproduced; partly unknown)
  - Repository CLAUDE.md -> AGENTS.md (author's writing-thread instructions)
  - Subagents: Claude Code general-purpose agent system prompt (unknown content) + the prompts in input/prompts.md
Coordinator model and role: claude-opus-5-5. Writes Section 1, executive summary,
  references and assembly; applies Humanizer to Section 1 and the executive summary;
  runs the reviews and the comparison. Writer, editor and evaluator roles are
  therefore not fully separate (same as the original run).
Writer/editor allocation and context strategy (close replication of the original):
  - 3 fresh general-purpose subagents (Opus 5.5, inherited) write Sections 2, 3, 4.
  - The same 3 agents, resumed with their drafting context, apply Humanizer to their own sections.
  - 1 fresh general-purpose subagent applies technical-writing then unslop to the whole frozen raw draft.
Reasoning, sampling and token settings, or unknown: reasoning effort set by the harness
  (not user-visible per agent); temperature, seed and token limits unknown.
Tool and research permissions: file read/write, shell, WebFetch. Writers may re-open
  registered source URLs; no new sources. Coordinator re-opened S120, S121, S122, S51
  (22 Oct 2026) to verify Section 1 details.
Brief, source-pack and contract identities: input/contract.md, input/source-pack.md
  (planning files at commit dab5f8a).
Raw file hashes: see raw/manifest.md
Skill repositories, commits/versions and installed file hashes: input/skill-provenance.md
Actual prompts sent: input/prompts.md
Length and resource limits: 4,750-5,250 words for raw and both editing conditions,
  same rule for both. No token or time budgets set.
Review policy, reviewer and review rounds: one fresh Opus 5.5 reviewer per condition,
  identical prompt, blind labels (A = pstack, B = Humanizer; key in blind-key.md);
  one round; coordinator applied all REQUIRED fixes, no OPTIONAL ones. See review/corrections.md.
Pre-review outputs retained: yes (humanizer/draft, pstack/draft)
Retries or deviations: reviewer B hit an API rate limit and was resumed with a
  continue-only message. No run was repeated or discarded. Other deviations below.
Counting and comparison methods: writing-experiments/tools/count_words.py
  (reproduces the original run's raw total of 4,873 exactly on its files).
Completion or failure status: complete (22 October 2026). Raw 4,961; Humanizer 5,069;
  pstack 5,063 counted words. All within 4,750-5,250.
```

## Deviations from the original run

- Inputs: the original writers produced the evidence files and the approved matrix during drafting. Here they exist before drafting, and writers may not add sources.
- Length rule: both editing conditions get the same range (the original gave pstack a narrower target).
- Pre-review drafts are preserved separately from reviewed versions (an extension the protocol recommends).
- The raw draft did not go through a mid-drafting content dispute (the methodology re-scoring happened in the original run and is an input here).
- Citations use an `{S-ID}` placeholder during drafting, resolved at assembly.
- Reviewers: the original run used coordinator review plus a citation review. This run used two blind fresh reviewers with a shared written policy, which is an extension the protocol recommends.
- Editing length: every editor got a per-section ±5% band around the frozen counts. This probably encouraged lighter edits than the original.
- Raw heading case is inconsistent (Sections 1 and 3 title case, Sections 2 and 4 sentence case). Headings were protected, so all three conditions inherit this.

## Outputs

| Path | Content |
|---|---|
| `raw/document.md`, `raw/sections/`, `raw/manifest.md` | Frozen raw version and hashes |
| `raw/notes/` | Writer notes and coordinator assembly notes |
| `humanizer/draft/`, `humanizer/reviewed/`, `humanizer/document.md` | Humanizer pre-review, reviewed and assembled versions |
| `humanizer/process/` | Per-editor Humanizer process notes |
| `pstack/draft/`, `pstack/reviewed/`, `pstack/document.md`, `pstack/process.md` | pstack versions and process note |
| `review/review-A.md`, `review/review-B.md` | Blind reviews |
| `review/corrections.md`, `review/checks.md`, `review/comparison.md` | Corrections applied, mechanical checks, three-way comparison |
