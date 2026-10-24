# Humanizer process note: Section 2

- Input: frozen `RUN/raw/sections/02-methodology.md` (1,432 words, the coordinator-edited version).
- Skill: `C:/Users/xingy/.codex/skills/humanizer/SKILL.md` (v3.1.0), read in full and run in file mode. I did not read wilson-humanizer, technical-writing, unslop or anything under `RUN/pstack/`.
- Output: `RUN/humanizer/draft/02-methodology.md`.

## Patterns identified (strongest first)

| Pattern | Where in the frozen draft |
|---|---|
| §1 Not X but Y / X rather than Y | 2.5 "layered over ... rather than replacing it"; 2.3 "a scheduling practice, not a candidate"; 2.4 "analyst judgements, not measured outcomes"; 2.4 "methodology support, not Actual's software quality"; 2.3 Kanban "not a complete methodology" |
| §2 One-line closers / staged short sentences | 2.6 "Volunteering adds risk."; "The evidence is also thin."; "Open limitations remain (...)"; 2.4 bold closer "Kanban, tailored with mandatory QA gates, is selected." |
| §2/§3 "X matters" | 2.4 "The baseline's 95 matters, because ..." |
| §4 Staged run-up | 2.6 "Kanban's main weakness is the one the matrix exposes." placed before the actual point |
| §7 Repeated openings | 2.6 final paragraph: "would stop fitting if ... It would also stop fitting if ..." |
| §11 Passive with hidden actor (weak) | 2.3 "A longlist was screened first"; 2.2 "a weighted matrix is used" |
| §19 Bold as decoration | the four lenses in 2.2 (**goal**, **constraint**, **risks**, **Stakeholders**); **proof rule**, **mandatory QA gate**, **explicit policy**, **OSS ("Bazaar") model**, the bold finding in 2.1, the bold C4 caveat and the bold selection sentence; bold labels on the five candidate list items |
| §8 Dashes | Only en dashes in numeric ranges (1–5, 1–3, pp. 26–27); no em dashes |
| §25 Writing about the document | Figure 2 caption "compiled from the sources cited in 2.1" |

No chatbot residue, inflated significance, sales language, borrowed authority or stock AI vocabulary was found. The raw draft was already fairly plain.

## What changed

- Removed all bold from the prose and list labels. Bold remains only inside Table 2.2 (protected table content).
- Rewrote the five candidate bullets as plain sentences with the method as subject ("Spiral works in ...", "Scrum uses ..."). The list itself is kept because it is a genuine category list.
- 2.5 now opens "Kanban sits on top of Actual's existing GitHub workflow", replacing the "rather than replacing it" contrast. The closing summary of changes is now a plain comparison with today.
- 2.3: "not a candidate" became "was not scored". The proof rule is now stated as what it does ("required real-world evidence"), as defined in the agreed plan. No new fact was added.
- 2.4: the opener became "Kanban entered the matrix as a working hypothesis and was tested on its weak criteria too". The C4 sentence now gives the reason first, then the caveat. "The baseline's 95 matters" became "The baseline scores 95, so today's process already fits volunteers well". The selection is stated in plain prose ("This report therefore selects ...").
- 2.6: the staged opener was merged with the quotation it introduced, and the closing fragments were merged into longer sentences. The last paragraph now names its two cases instead of repeating "would stop fitting".
- 2.2: the four lenses are named in one sentence without bold. The matrix sentence names what is done ("the options are scored in a weighted matrix").

## Deliberate overrides of the skill (contract)

- **§1 contrasts kept** where the negative half carries a required evidence limit or corrects a likely misreading:
  - "analyst judgements, not measured outcomes" (evidence limitation);
  - "rates methodology support, not Actual's software quality" (a fixed contract decision);
  - Kanban "strictly ... not a complete methodology" (the source's own scope, required by the writing-session decisions).
- **§8 en dashes kept** in numeric ranges and the locator "pp. 26–27": numbers and locators are protected, and these are range marks, not connective dashes.
- **§25 caption kept** ("compiled from the sources cited in 2.1"): captions are protected.
- **§6 lists kept**: the four lenses, the three quality attributes and the five candidates are genuine categories.
- **§9 hedges kept**: "plausible but unproven", "no evidence found, October 2026", "can pass once those controls are embedded" and "only narrowly" are argued limitations.
- **"QA gate" kept** despite the §12 watch on figurative "gate": it is a technical term in the agreed plan and is used across Sections 3 and 4.
- Third person, British spelling ("visualises", "organisational", "decentralised", "favour") and every citation string are unchanged.

## Self-audit

- **Mechanical check against the frozen file:** citation strings (sorted), code blocks (both diagrams), table lines, captions, headings, quoted strings and the multiset of numbers in prose are all identical. The `<!-- Cited -->` comment is unchanged.
- **Fact check:** I re-read for added or dropped claims. Every supported claim is kept: the ranking, the margin breakdown, the equal-weight check and the conditions under which the choice would stop fitting.
  - "contributors choose their own work" and "so new work stops starting" have the same meaning as the raw draft.
  - The 2.3 phrase "required real-world evidence" restates the proof rule from the agreed plan; it adds no evidence claim.
- **Second pass for surviving tells** (§1, §2, §6, §8, §19): only the contract-protected cases listed above remain. There are no em dashes and no bold outside the table.
- **Residual:** 2.1 remains a sequence of short factual sentences, each with a citation. I kept this deliberately, because merging them would detach citations from their claims.

## Length

**1,482 words** (`count_words.py`), +50 (+3.5%) against the frozen 1,432, within ±5%. The first rewrite came to 1,522 (+6.3%). One trimming pass removed wordiness the rewrite had introduced, with no content removed. Token similarity to the frozen file is 0.890 (measured on the first rewrite).
