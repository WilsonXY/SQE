# Protocol for comparing three AI writing workflows

This document records how the writing experiment in this thread was conducted and provides a procedure for repeating it with another LLM. It covers preparation, agents, prompts, isolation and review. It excludes the assignment's subject matter, findings and writing results.

The original run used one model, GPT-6.1-Sol, through T3 Code's Codex harness. It compared three writing conditions within that model. No comparison between different models has been conducted here.

## 1. Define the three conditions

The raw condition is a complete document written normally from an agreed brief and verified evidence. The writer does not apply Humanizer, technical-writing or unslop. Normal research, planning, factual corrections, citation work and editorial instructions still apply. “Raw” therefore means the normal agent writing workflow before the experimental editing passes.

The Humanizer condition is a complete prose rewrite of that raw document using the Humanizer skill. The pstack condition is another rewrite of the same raw document, using technical-writing followed by unslop.

Both editing conditions receive the identical frozen input. Neither receives the other condition's rewrite. Each keeps its own output files. The experiment compares the whole Humanizer workflow with the combined pstack workflow; it cannot separate the individual effects of technical-writing and unslop.

Each condition produced one complete document version. The section writers were not independent repetitions of the experiment.

The original arrangement can be expressed as:

```text
Agreed brief + verified evidence + common writing constraints
                            |
                    Normal drafting
                            |
          Research corrections and document assembly
                            |
                    Freeze raw version
                      /             \
          Humanizer rewrite     technical-writing rewrite
                    |                     |
          Humanizer self-audit       unslop pass
                    |                     |
                 Review meaning and correct errors
                      \             /
                   Compare all three
```

The arrows describe information flow. The two editing processes may run concurrently once the raw input is frozen; their outputs must remain separate.

## 2. What happened in this thread

### Preparation and decisions

The coordinator read the existing handoff, document plans, source register and writing constraints. The user set the scope, required local Markdown files and authorised subagents. Questions affecting the content or writing convention were settled before the final raw draft was frozen.

The user challenged an important content decision while drafting was underway. The relevant subsection was held, alternatives were investigated, and independent work continued. After the user approved the revised decision, the affected prose was completed. This discussion belonged to document preparation. It was not a treatment applied to just one writing condition.

### Normal drafting

The coordinator divided the substantive sections between three writing agents and retained other sections, source coordination and assembly. Each writer received a section plan, relevant evidence and common constraints. Writers owned separate files to avoid concurrent edits to the same prose.

Writers checked evidence gaps and reported qualifications rather than guessing. They wrote their sections without applying the experimental writing skills. The coordinator assembled the document, resolved reference identities and citation suffixes, normalised numbering, checked the complete argument, and wrote the executive summary after the substantive sections were available.

The first version included these ordinary revisions. It was not the first text emitted by each agent.

### Skill installation and preparation

Humanizer was installed early in the thread. Its presence was checked, but its full instructions were not read by the normal writers until the complete raw document was frozen.

The user added the pstack condition after normal drafting had begun. A fresh agent read the two pstack skills during setup to check their dependencies. That agent did not read or influence the raw draft during setup. It returned to an idle state until the frozen input was available. Technical-writing required unslop; no additional dependency was needed for this task.

The agents shared a filesystem. Installing a skill once made the same instruction file available to all relevant agents. Each agent applying a skill read that file explicitly. Separate installations per writer were unnecessary in this environment.

Skill names, descriptions and discovery excerpts were visible in the environment. The raw condition was therefore protected by instructions against using the skills, rather than by complete absence of all information about them.

### Freeze and branching

The coordinator saved the complete raw sections, assembled document and reference list. A manifest recorded their SHA-256 hashes and the word-count method. From this point onward, editing agents were instructed to leave those files unchanged.

The original writers then read Humanizer and rewrote their respective sections. The coordinator applied Humanizer to the sections it had written. Each writer recorded the patterns identified, the rewrite and the self-audit.

The separate pstack agent received the complete frozen raw draft. It applied technical-writing, then unslop, to all sections. It did not read Humanizer's instructions, output or process notes. It copied the common reference list unchanged.

### Review and assembly

Each editing process checked its own work. The coordinator compared protected elements and reviewed the rewritten claims against the raw draft. A separate citation review covered the raw and Humanizer versions. The pstack citations were checked through matching and coordinator review.

Review found some wording that strengthened the evidence or altered a recommendation's force. Those passages were corrected within the affected rewrite. The final comparison therefore used reviewed versions. Intermediate rewrite drafts were not systematically preserved as separate experimental samples.

Review effort and the number of correction rounds were not fixed equally in advance.

The coordinator assembled each complete version using common front matter and references, selected corresponding excerpts, and documented the comparison. No blind reader study, formal preference scoring or AI-detector test was conducted.

## 3. Agent roles and information boundaries

The coordinator managed the brief, assignments, source consistency, raw freeze, final assembly and comparison. It also wrote and Humanizer-edited part of the document. The evaluator and writer roles were consequently not fully separate.

The raw writers received the agreed material and wrote normally. They could coordinate evidence and terminology but did not apply the experimental skills before the freeze.

The Humanizer editors were the original writers, so they retained their drafting and research context. They read the current frozen files before editing; relying on an earlier section draft could have missed the coordinator's final corrections.

The pstack editor was a fresh agent with its own context. It received the same frozen document and the necessary task constraints, without the Humanizer branch's material. One pstack editor handled the whole document, whereas several writers handled the Humanizer version.

All agents could technically access the shared workspace. Instructions and separate output folders provided the separation. There was no filesystem access control preventing an agent from opening another branch. A future run should record the same distinction between instructed separation and enforced isolation.

Because editor context and team allocation differed, the skill instructions were not the only possible cause of writing differences.

## 4. Inputs and constraints to hold constant

Prepare one input package before starting the editing conditions:

1. A brief stating the reader, purpose, scope and required structure.
2. A source pack containing the evidence the writers may use, with a claim-to-source map where needed.
3. A writing contract covering language, voice, terminology, citations, length and protected material.
4. The complete raw draft and common references.
5. A manifest identifying the input files, hashes, skill instructions and run settings.

In this thread, the fixed content included factual claims, names, dates, numerical information, source support, qualifications, headings, captions, tables, diagrams and inline code. The editing processes could restructure the surrounding prose while preserving those elements.

The user-required writing convention took precedence over generic skill advice. For example, academic citations kept their parentheses, and required third-person prose was not converted to the second-person style suggested by technical-writing. Genuine categories and evidence limitations were retained even when a skill warned against rhetorical triads or excessive hedging. Standard titles, proper names and technical notation also kept their required forms.

Record these exceptions in the shared contract before launching editors. Otherwise, one version may be rewarded for following a skill rule that another version correctly overrides.

The original run imposed an overall length range and gave writers additional section targets. The pstack editor also received a slightly narrower overall target. These were not perfectly matched editing budgets. For a future run, give both conditions the same length rules and state whether length is a hard validity requirement or an observation. Preserve the content instead of adding filler to reach a target.

## 5. Skill provenance and installation

The skills used in this thread came from these repositories:

- Humanizer: https://github.com/blader/humanizer
- Technical-writing: https://github.com/cursor/plugins/tree/main/pstack/skills/technical-writing
- Unslop: https://github.com/cursor/plugins/tree/main/pstack/skills/unslop

Humanizer's installed metadata identified version 3.1.0. The pstack repository head observed during installation was `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10`. Installation used the moving main branches; the original Humanizer repository commit was not recorded.

The hashes below identify the actual installed `SKILL.md` bytes used in the experiment:

```text
humanizer
0612f1dfb1672b0ea9b97e139bf1f06cabe98d8b27424fe8ff01e1fb4cc99cad

technical-writing
61fe9c424a798ebf36ad94941f87be049cb8827bdf86d21474a0dde37b513c43

unslop
ccab208e315ce05e2fab8eeee2f7879f1289b5c6844840b2d307adf31c79144f
```

A hash can reveal that an instruction file changed; it cannot reconstruct a missing file. Before a repeat run, preserve the actual skill instructions and their licence files, or pin retrievable repository commits and verify the installed hashes. Installing the latest versions would test a different set of instructions if they have changed.

The original environment used a skill-installer helper. Equivalent commands for a pinned repeat are:

```text
python <installer-script> --repo blader/humanizer --path . --name humanizer --ref <humanizer-commit>
python <installer-script> --repo cursor/plugins --path pstack/skills/technical-writing pstack/skills/unslop --ref <pstack-commit>
```

Replace the placeholders with actual paths and commits. Another agent harness can load the same instruction files directly. The treatment is the supplied skill text and its application, rather than the slash-command spelling.

## 6. Procedure for another model

### Choose what the repeat will measure

There are two useful extensions of the original design. Choose one before writing begins.

**Repeat the whole workflow with each model.** Each model writes its own normal draft from the same brief, evidence and constraints. Its two editing conditions start from its own frozen draft. This repeats the thread's procedure. Differences between models include both their initial writing and their editing; the editing inputs will differ.

**Compare editing on one common draft.** Every model receives the exact same frozen raw document. Each produces a Humanizer rewrite and a pstack rewrite. This holds the editing input constant, so it answers a narrower question about editing. It does not compare the models' independent first-draft writing. If there is only one shared raw document, do not describe it as a raw sample generated by every model.

Keep these designs separate in the records. A shared brief and a shared raw draft are different controls.

### Set up the run

Create a run ID for the model and repetition. Record the exact model identifier, provider, date, agent harness, visible reasoning settings, available tools and context strategy. Record temperature, seed, token limits and budgets if the environment exposes them. Mark unavailable settings as unknown; do not infer them from a friendly model label.

Record the available system, developer and repository instructions too. These can already prescribe a writing style before a named skill is applied. Keep them constant where possible, and mark hidden or unavailable instructions as unknown. Changing the model and the host together introduces another difference to account for.

The original parent ran at high reasoning effort, with native child agents inheriting the model and configuration. A complete per-agent record of sampling parameters, usage and elapsed time was not kept. This document does not fill in those missing settings.

Use new working contexts when moving to a different model. Decide whether the coordinator remains fixed or changes with the model. Record that choice, because a coordinator that writes, edits or reviews can affect the material being compared.

### Prepare and freeze the raw version

Give raw writers the common brief, source pack and contract. Do not supply the experimental skill bodies. Ask them to finish the complete document normally and report unresolved evidence gaps.

Resolve content decisions and factual errors before the freeze. Assemble the document, finish its references and apply the same normal quality checks to every raw run. Save this version and calculate its hashes. After the freeze, give both editing conditions that exact input.

If a substantive source error is discovered later, correct the shared baseline and restart both editing conditions from the newly identified baseline. Do not quietly improve just one condition's evidence and treat it as a style difference.

### Run the two editing conditions

For a close replication of this thread, let the original writers handle Humanizer and use one fresh agent for pstack. Keep the section ownership and coordinator role consistent when repeating this arrangement with another model.

For a more balanced editing comparison, use fresh editors for both conditions, with the same number of agents, the same section allocation, the same context pack and the same budgets. This removes some context differences, but it changes the original agent arrangement. Label it as a revised protocol.

Humanizer editors read the full skill, identify relevant patterns, rewrite the entire prose and self-audit meaning and remaining patterns. File outputs contain the final prose; process notes remain separate.

Pstack editors read both skills, apply technical-writing, then run unslop and self-audit. They work from the raw version throughout and do not consult Humanizer output. Keep the skill order fixed across runs.

### Review and preserve the evidence

Use the same review instructions and correction policy for both conditions. Preserve each editor's pre-review output as well as the reviewed version if review effort will be part of the comparison. Record what was changed and why.

Fix factual drift and violations of the shared contract. Avoid rewriting a condition simply to make it resemble the reviewer's preferred style. Record reviewer identity and context, and whether it saw the condition labels.

Keep every completed run. If a run is repeated after failure or an unsatisfactory result, record that event and its reason. Decide the number of repetitions before inspecting which workflow appears preferable.

## 7. Reusable prompts

These templates reconstruct the roles used here. They are reusable instructions, not a verbatim export of the original tool-call prompts. Replace every bracketed value before use. Keep a copy of the actual prompts sent during each new run.

### Shared contract

```text
Task: [purpose, reader and document type].
Scope: [included and excluded material].
Language and voice: [convention, person and authorised exceptions].
Required structure: [headings and section allocation].
Length rule: [range, what counts, whether it is mandatory].
Evidence: use only [source pack]; preserve source qualifications.
Protected material: [citations, references, values, names, tables,
figures, code, headings or other items that must remain fixed].
Work locally. Do not commit, push or publish.
Keep report prose and process notes in separate Markdown files.
```

### Normal writer

```text
Write [assigned scope] from the shared brief, source pack and contract.
Use your normal writing process. Do not read or apply Humanizer,
technical-writing or unslop instructions during this phase.
Verify material gaps and report unresolved decisions.
Save the complete normal draft to [raw output path].
Do not start an experimental rewrite. Return when normal writing
and its ordinary checks are complete.
```

### Humanizer editor

```text
The complete normal draft is frozen at [raw input path].
Read the current frozen files and the full Humanizer instructions
at [skill path]. Apply the skill's complete rewrite and self-audit
process to all assigned prose.
Follow the shared contract. Preserve supported claims and their
qualifications. Do not add research or facts.
Do not read the pstack skills, outputs or process notes.
Leave raw files unchanged. Write final prose to [Humanizer path].
Save a separate process note describing the pass and corrections.
```

### Pstack editor

```text
Work in a separate context from the Humanizer editor.
Read the frozen raw input at [raw input path] and the shared contract.
Read [technical-writing skill path] and [unslop skill path].
Rewrite all assigned prose with technical-writing, then apply unslop.
Preserve supported claims and their qualifications. Add no research.
Do not read Humanizer instructions, output or process notes.
Leave raw files unchanged. Save final prose to [pstack path].
Save a separate process note recording skill order, task-specific
exceptions, self-audit and corrections.
```

### Meaning and integrity reviewer

```text
Compare [condition output] with [frozen raw input] under the shared
contract. Check protected elements and review meaning paragraph by
paragraph, including uncertainty, causal force and recommendations.
Identify invented claims, missing caveats, changed source support,
and wording that turns a proposal into an observed result.
Separate required corrections from optional style preferences.
Report locations and reasons. Do not edit the frozen raw files.
Apply [the common review and correction policy].
```

## 8. Checks and comparison method

First check that the correct input was used and its hashes are unchanged. Compare the required headings, captions, tables, diagrams, inline code, references and citation groups. Check that numerical values and their associated claims remain correct. Exact text matches help detect changes to protected material, but they do not establish that surrounding meaning is preserved.

Review changes in evidential force manually. For example, “can improve” becoming “improves” introduces certainty; a vulnerability allowing access does not establish observed compromise; and a source recommending an action does not establish an existing mandatory rule. Check these distinctions in both editing conditions.

Use one counting method across all versions. In this run, counted words were whitespace tokens containing a letter or digit after removing Markdown-only delimiters, comments and link targets. Headings, captions, table cells and diagram text counted. Common front matter, references and process notes were excluded.

The original wording-similarity calculation used Python's `difflib.SequenceMatcher` with `autojunk=False` on lower-case word tokens. Tokens were extracted using:

```python
r"\w+(?:['\u2019-]\w+)*"
```

The calculation covered the section text, including the constant tables and diagrams, and excluded shared references and front matter. This provides a reproducible description of wording similarity. It does not measure writing quality. If a later run excludes protected blocks to focus on prose, label the metric differently and do not compare its percentages directly with this run's measure.

Select corresponding passages by section and position before choosing which wording seems preferable. Present the raw, Humanizer and pstack passage together. The thread used matching passages to examine sentence structure, paragraph flow and preservation of meaning. It did not assign formal quality scores.

For a later scored comparison, define the criteria before judging. Keep fidelity to meaning separate from preferences about clarity, rhythm, concision and voice. Where feasible, hide model and condition labels and vary presentation order. Record that as an additional evaluation stage rather than something already performed in this thread.

## 9. Run records and archive layout

One possible layout for each model and repetition is:

```text
writing-experiments/
  <model-id>/
    <run-id>/
      run-record.md
      input/
        brief.md
        source-pack.md
        contract.md
        skill-provenance.md
      raw/
        document.md
        references.md
        manifest.md
      humanizer/
        draft.md
        reviewed.md
        process.md
      pstack/
        draft.md
        reviewed.md
        process.md
      review/
        corrections.md
        checks.md
        comparison.md
```

The separate draft and reviewed files are an extension for future runs. The original thread retained frozen raw files and final rewrite files, plus process notes, rather than this complete layout.

Use the following record for every run:

```text
Run ID:
Date:
Design: own raw per model / shared raw across models
Model and provider:
Harness:
Available instruction stack and any unknown instructions:
Coordinator model and role:
Writer/editor allocation and context strategy:
Reasoning, sampling and token settings, or unknown:
Tool and research permissions:
Brief, source-pack and contract identities:
Raw file hashes:
Skill repositories, commits/versions and installed file hashes:
Actual prompts sent:
Length and resource limits:
Review policy, reviewer and review rounds:
Pre-review outputs retained: yes/no
Retries or deviations:
Counting and comparison methods:
Completion or failure status:
```

Changing the model, skill text, baseline, agent arrangement, source permissions or review policy changes the conditions of the comparison. Record the change so later readers can tell which procedure was repeated.

## Editing note

Technical-writing requests a proposed plain-language addition to unslop. This proposal belongs to this document's editing record only; no installed skill was changed.

```diff
--- unslop/SKILL.md
+++ unslop/SKILL.md (proposal only)
@@
-### Plain speech
+For "bake-off", use "comparison".
+
+### Plain speech
```
