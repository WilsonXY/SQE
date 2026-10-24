# Section 4 (IV&V): Humanizer process note

- Input: `raw/sections/04-ivv.md`, the frozen version with the coordinator's edits (1,360 words).
- Output: `humanizer/draft/04-ivv.md` (**1,372 words**, +0.9%).
- Skill: `C:/Users/xingy/.codex/skills/humanizer/SKILL.md` v3.1.0, read in full and used in file mode.
- Not opened: wilson-humanizer, technical-writing, unslop and `RUN/pstack/`.

## Patterns identified (strongest first)

| Pattern | Where | Action |
|---|---|---|
| §19 bold labels | 4.3 "**Achievable independence.**", "**Risk tiers.**", "**Explicit policies.**" | Removed. Each paragraph now opens with a topic sentence that makes the point. |
| §19 bold labels | 4.5 "**Early defect detection.**" etc. | **Kept** (see overrides). |
| §2 one-line closer / staged opener | 4.2 "The strongest independent findings came after release." stood as its own sentence before the evidence | Joined to the evidence with a colon. |
| §2 staged opener | 4.2 "The disclosure route itself is a strength." | Cut. The paragraph now starts with the fact. |
| §3 aphorism | 4.6 "gates can become ritual" | Changed to the plainer "Gates can also turn into box-ticking". |
| §2/§13 staged openers | 4.6 "Cost is a binding constraint." | Changed to a specific claim: "Cost limits the external part of the model." |
| §1 contrast, split form | 4.1 "Agile delivery does not remove the need for IV&V." followed by a quote that says the same thing | Cut the restatement and led with the cited argument. |
| §25 writing about the document | 4.3 "and the report does not present it as such" | Cut. The claim that a maintainer review is not full IV&V is kept. |
| §25 writing about the document | 4.4 "The release row adds evidence…; it does not claim…" | Rewritten about the release-train stage. The qualification about the current smoke-test order is **kept**. |
| §15 -ing rider | 4.5 "aiming to reduce escaped defects" | Changed to "with the aim of reducing escaped defects". |
| §7 repeated openings | 4.3 and 4.6 both began "Inside the project" after the first pass | 4.6 now opens "Even with the new role". |
| Long chained sentences (rhythm) | 4.1 Smith and Hayes sentence; 4.2 credits sentence; 4.6 rubber-stamp sentence | Split into shorter sentences to vary length. |

The skill's §6 forced-triad check was run. The triads are genuine categories, so they were kept: the three independence parameters, the three tiers, the three goals, and the team / release goals / pool sentence. §8 dashes: none were added. §12 vocabulary: "gate" is used in its technical QA sense, so it was kept.

## Deliberate overrides of the skill (contract)

1. **Bold goal labels in 4.5 kept.** The brief asks for each of the three goals to be shown explicitly. The labels name the brief's categories, so they carry information for the marker. Contract: "keep genuine lists of categories".
2. **"they are not IEEE's scheme" kept** (a §1/§25-style disclaimer). The contract requires the tiers to be labelled as this report's own design, inspired by IEEE 1012.
3. **Evidence qualifications kept** even where they read as scope hedges (§9/§23):
   - "Not established";
   - "No public evidence … (October 2026)" in the table and in the prose;
   - "self-reports";
   - "three advisories examined for this report";
   - "does not assume that current smoke testing precedes every publication step";
   - "may understate risk".
4. **Dashes in protected content kept:**
   - "USD 3,000–3,500" (protected number);
   - the "—" cells in Table 4.1 (protected table content).
5. **Third person and parenthetical APA citations kept.** The skill's §11 example uses "you"; the contract forbids second person.

## Self-audit result

I compared the raw and Humanizer files with a script, then re-read the output in full.

- Parenthetical and narrative citations are identical (29 out of 29, the same multiset).
- Headings, table captions, table rows, the tier list and the `Cited` comment are byte-identical.
- The direct quotation and every number are identical.
- No fact, name, date or source was added or removed. The 4.5 GHSA-m2cq claim keeps its hedge, "a defined point to detect", rather than a certain catch.
- Only the three intended bold labels remain.
- The only dash in the prose is the protected range.
- British spellings are unchanged.

Remaining mild patterns, judged acceptable:
- "Both points apply to Actual." is a short bridging sentence. It adds the application to Actual, so it is not a restatement.
- "Independence also competes with flow." is a topic sentence that the paragraph then supports.

Final word count: **1,372** (`count_words.py`), within ±5% of the 1,360 frozen count.
