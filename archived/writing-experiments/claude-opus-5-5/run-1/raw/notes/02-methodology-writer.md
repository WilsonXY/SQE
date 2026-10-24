# Methodology writer notes: Section 2 (raw)

Output: `RUN/raw/sections/02-methodology.md`. Final word count: **1,453** (`count_words.py`), about 4% over the ~1,400 target. Two trimming passes took it down from 1,640. The remaining excess sits mainly in the two figures and the two tables, which the plan requires in the body.

## Sources cited (21)

S01, S02, S03, S04, S07, S08, S10, S18, S22, S25, S26, S34, S36, S37, S38, S39, S42, S47, S105, S108, S109.

- XP practices are cited via **S105** (the creators' primary-practices appendix, read in full), not S35, because only S35's table of contents and Chapter 1 were read.
- The OSS baseline is cited via **S108** (Raymond 2000, version 3.0, which was read), not S24 (the unread 1999 book).
- Kanban scope and policies are cited via **S109** (official guide) and S38 (pp. 98, 106, 110). S28 (Anderson) is not cited.
- S30 (*Accelerate*) is not cited because it was not read. DevOps is cited via S39 only. S40 was dropped in trimming.
- S22 (Shape Up) is cited only to name the method that was dropped. Its bibliographic details are verified; the content was not read, and no content claim is made. S23 is not cited.
- Re-opened during writing, with no new sources: S03 (release order confirmed: two other maintainers approve, then merge, tag and publish, then smoke test before un-drafting and announcing) and S109 (the guide states Kanban is "not a methodology nor a process framework" and is applied to an existing way of working).

## Evidence gaps and qualifications

- **No paragraph locators for web-page quotes.** The draft avoids direct quotes from S10 and S109; it paraphrases them instead. Quotes kept: S02 "above all else" (no para. number; the coordinator may need one or should paraphrase), S47 "may accelerate" (pp. 26–27; the register gives the range, not a single page) and S38 p. 110 "relatively basic flow tool...".
- "Names no methodology" is limited to Actual's contributing documentation, worded as "no evidence found, October 2026".
- Regulatory compliance not being scored rests on an uncited analyst statement ("Actual is not a regulated financial institution"). This comes from the agreed plan, but no source in the pack states it explicitly.
- The C10 = 3 and baseline comparisons are stated as analyst judgement; the draft does not claim measured superiority.
- No material evidence gap blocked writing.

## Decisions made within the plan

- The full approved matrix is copied exactly into the body as Table 2.2 (totals 72/81/82/102/94/95). Criteria and weights are in Table 2.1, with labels shortened from `02-methodology.md`.
- The QA gate (Security, Reliability, Interaction capability) is stated as a precondition before scoring, as in the reassessment file.
- Kanban's 7-point margin over the baseline is decomposed from the matrix: C8 +6, C7 +3, C5 +2, C6 +2, C9 −2, C10 −4. The text says it "rests mainly on flow control (C8) and lower overhead (C7), partly offset by weaker evidence (C10)". The earlier proposal had attributed it to C5/C8; the decomposition shows C7 matters more than C5.
- The equal-weight check (42/50 against 39) is reported. The quality-first sensitivity result is mentioned only qualitatively in 2.6 ("raised well beyond the agreed 1–3 scale ... only narrowly"), without the diagnostic weights.
- The board columns are named exactly as the IV&V writer was told: Requirements/triage, Design, Build/PR, Verify, Release train, Operate/maintain. The WIP limit sits on Verify. The QA gate is Verify's exit policy. Risk is recorded at triage, but risk tiers are left for Section 4 to define.
- The WIP limit has no number. It is "set from observed review throughput", because no evidence supports a specific value. The monthly flow review at the release cut is this report's proposal.
- Lean is screened out with one clause ("overlaps heavily with Kanban") and no citation, because S29 was not read.

## Questions for the coordinator

1. Is 1,453 words acceptable, or should Section 2 be cut to about 1,400? The next cuts would be the longlist sentence in 2.3 or the equal-weight sentence in 2.4.
2. The S02 quote "above all else" has no paragraph locator. Should a para. number be added at assembly, or should it be paraphrased?
