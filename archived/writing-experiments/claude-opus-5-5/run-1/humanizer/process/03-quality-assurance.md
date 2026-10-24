# Humanizer process note — Section 3

- **Input:** the frozen `RUN/raw/sections/03-quality-assurance.md` (1,421 words).
- **Output:** `RUN/humanizer/draft/03-quality-assurance.md` (**1,472 words**, +3.6%).
- **Skill:** `C:/Users/xingy/.codex/skills/humanizer/SKILL.md` v3.1.0, read in full and applied in file mode (mark tells → draft → check → final).
- **Not read:** technical-writing, unslop or `RUN/pstack/`.
- **Not edited:** `RUN/raw/**`.

## Patterns identified in the frozen draft

| § | Pattern | Where |
|---|---|---|
| 1 | Not X but Y / clipped contrast tail | "Functional suitability is not ranked lower because correct numbers matter less"; "a release baseline, not an area for new effort"; "a stated requirement, not an extra"; "would buy a rating, not fewer defects"; "Automation helps but is not free"; "a self-assessment, not an audit" |
| 2 | One-line closer / short summary sentence | "The gaps rest on public evidence only." as a standalone final sentence |
| 4 | Staged run-up | "Some limits remain."; "Mapping these practices to the three attributes reveals gaps." |
| 7 | Repeated sentence openings | "From the user's view … From the product view … From the process view" (3.1) |
| 19 | Bold as decoration / bold-labelled list | bold attribute names in the 3.2 prose paragraph; the four bold-labelled gap bullets in 3.3 |
| 25 | Writing about the document | "Table 3.2 evaluates …"; "Table 3.1 rates each …" |
| 6 | Triads (checked, mostly genuine) | the three quality views, three stakeholder groups and three attributes are real categories. "correct, private and understandable" was kept as three distinct properties. |

No dashes (§8), stock AI words (§12), sales language, chatbot residue or knowledge-limit disclaimers were found.

## What changed

- **3.1:** The three "From the … view" openings became three differently built sentences. The stakeholder sentence was split into separate sentences, and "self-hosters carry extra risk because …" makes the reason explicit.
- **3.2:** The defensive "not ranked lower because …" became a direct statement that the Medium rating needs explaining, followed by the evidence. The baseline line became "stays in the release baseline, and new effort goes elsewhere". Bold was removed from the attribute names, and "Security is the top priority" became "Security comes first". "Not an extra" became "already one of its own requirements". The encryption sentence is now in the active voice with a user as subject; the claim is unchanged.
- **3.3:** The bold-labelled bullet list became four short prose paragraphs, one per gap, each opening with its attribute. "Reveals gaps" was replaced by a sentence that states the count ("leave four gaps"; the count is from the draft's own list). "Substantial" became "a lot of".
- **3.4:** The table-description opener now states the selection criterion. "Buy a rating, not fewer defects" became "would give Actual a rating without removing any defects", in its own sentence. The ASVS sentence was split. "Only … transfer" became "only … transfer to Actual".
- **3.5:** "Therefore lives on the board" was rephrased so the table reference leads the sentence. Measures were rewritten as "X for security …" instead of bracketed labels. The roles sentence is now active ("Section 4 specifies …").
- **3.6:** "Automation helps but is not free" became "Automation has its own costs". "Some limits remain." was removed and the paragraph now opens "Even with these controls, …". "Not an audit" became "gives no audit assurance". The final short sentence was merged into the scope-level sentence.

## Deliberate overrides of the skill (contract)

- **§20 Title-case headings** kept unchanged. Headings and numbering are protected.
- **§19 Bold "High"** inside Table 3.1 kept. Table contents are protected.
- **§1 Contrasts kept where both halves carry information:**
  - "concern security rather than calculation errors": a factual scope of the advisories.
  - "rather than a full verification level": a qualification of the ASVS use.
  - "instead of in a separate document": answers the 3.3 gap of no written QA plan.
  - "WCAG 2.2 … does not deprecate 2.1": a source qualification.
- **§9 / §23 Evidence limits kept:** "no evidence found in the repository, October 2026", "private practices may exist", "Only its scope was read", "observational findings cannot predict", "public evidence only". These are genuine evidence hedges, which the contract requires keeping.
- **§6 Triads kept:** the three quality views, three stakeholder groups and three selected attributes are genuine categories.
- **§11 Passive voice kept** in method statements ("Only its scope was read", "No public result … was found"). The actor is the report itself, and the contract requires third person.
- Academic parenthetical citations were kept in APA form, not converted to links.

## Self-audit

- Mechanical checks against the frozen file:
  - In-text citation multiset identical (32 citations: author, year, suffix and locator).
  - Headings identical.
  - Table rows and captions byte-identical.
  - Direct quotations identical ("users trusting the numbers", "appropriate test coverage", "entry", "exit").
  - Zero em or en dashes.
  - `<!-- Cited -->` comment unchanged.
- Numbers, dates and identifiers are unchanged: GHSA-m2cq-xjgm-f668, 20 February 2026, CVSS 9.2, USD 2,000, 22 October 2026, WCAG 2.1/2.2 AA, standard editions. Only section cross-reference punctuation moved.
- Each claim stays attached to its original citation. No facts, sources or rankings were added.
- **Small interpretive rewordings:**
  - "self-hosters carry extra risk because their server holds bank-sync credentials" restates the original "also run a server holding bank-sync credentials".
  - "produces those properties reliably" replaces "repeatedly".
  - "have little reason/only … transfer to Actual" keeps the raw judgement.
- **Remaining tells after the second pass:**
  - Some sentence-initial "Actual …" repetition across 3.2–3.3. It is a proper-noun subject in a case study and was left.
  - "Section 4 …" cross-references appear several times by design.
  - "The plan's main cost is volunteer time" is a short topic sentence. It was kept because the evidence follows immediately.
- **Length:** the first rewrite came to 1,530 words, outside ±5%. It was cut by removing a redundant clause in 3.2, compressing the 3.5 and 3.6 explanations and dropping the "Some limits remain" run-up. No claim was removed. Final: **1,472 words** (within ±5% of 1,421).
