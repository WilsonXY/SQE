# Review corrections — claude-opus-5-5/run-1

## Review policy

- Two fresh reviewer agents (Opus 5.5), one per condition. Both got the identical prompt (`input/prompts.md` §4) and saw only blind labels: A = pstack, B = Humanizer. The key was in `blind-key.md`, outside the review folder.
- A correction is REQUIRED only if the edited text says something the raw text and its sources don't support, drops a claim or qualification the raw text made, or breaks the contract. The coordinator applied every REQUIRED fix as proposed, in `<condition>/reviewed/`. No OPTIONAL item was applied to either condition.
- One review round per condition. Pre-review outputs are kept unchanged in `<condition>/draft/`.
- Reviewer B's run was cut off by an API rate limit, then resumed with a one-line "continue" message and no new instructions. Reviewer A ran without interruption.

## Results

| | pstack (A) | Humanizer (B) |
|---|---:|---:|
| Required corrections | 1 | 8 |
| Optional items | 4 | 14 |
| Required corrections in coordinator-edited text (exec summary, Section 1) | 0 | 3 |
| Words changed by corrections (similarity draft → reviewed) | 1.000 | 0.995 |

### pstack, applied

| ID | File | Drift | Fix |
|---|---|---|---|
| A-R1 | 02 §2.5 | "the limit stops new work from starting": stated a WIP limit's intended effect as fact, contradicting 2.6's point that a limit cannot compel review | "the limit is meant to stop new work from starting" |

### Humanizer, applied

| ID | File | Drift | Fix |
|---|---|---|---|
| B-R1 | 00 | Kanban's weakness reframed as design rationale | "Its weakness is that Kanban itself prescribes… so those gates must carry the quality work" |
| B-R2 | 00 | "remain the main limits" narrowed to "limit how far independence can go" | Raw wording restored |
| B-R3 | 01 §1.5 | "changing requirements" became an unsupported "volunteers, whose priorities change" | "Work depends on volunteer capacity, requirements keep changing…" |
| B-R4 | 02 §2.3 | Proof rule restated as "real-world evidence"; Shape Up has practitioner evidence, so the sentence contradicted itself | "required peer-reviewed evidence" |
| B-R5 | 03 §3.3 | Invented count "two similar integrations" (the advisory involves three) | "This inconsistency between similar integrations" |
| B-R6 | 04 §4.2 | Evaluative sentence "The disclosure route itself is a strength." deleted | Restored |
| B-R7 | 04 §4.5 | "Each requirement is linked…" reads as Actual's current state | "Under the model, each requirement is linked…" |
| B-R8 | 04 §4.6 | "Cost is a binding constraint" weakened to "Cost limits the external part" | Raw wording restored |

## How to read the asymmetry

The 1 : 8 split is consistent with the similarity data: Humanizer moved further from raw (0.911) than pstack did (0.937), so there was more text that could drift. Both conditions dropped or reframed evaluative "staging" sentences, and the Humanizer skill targets exactly those (§2 closers, §4 openers). Four of the eight (B-R1, B-R2, B-R6, B-R8) are evaluative judgements that Humanizer read as staging.

Three cautions apply:

1. The two reviewers are different agent instances, so their thresholds may differ. A single reviewer seeing both conditions in random order would control for this. That was not done.
2. Reviewer B was interrupted and resumed. Reviewer A was not.
3. Three of the eight Humanizer corrections fall in text the coordinator edited. The coordinator also wrote the review policy and applied the fixes. The writer, editor and evaluator roles are not fully separate (the same limitation as the original run).
