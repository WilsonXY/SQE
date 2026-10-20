# Sources Register

This file logs **every** source consulted while planning, whether or not it ends up in the report. See the rules in `AGENTS.md` → *Citations and sources*.

- Format: **APA 7th edition.** Fields marked `[to verify]` must be confirmed from the actual source before the reference is used.
- Status values:
  - **Verified**: read directly, details confirmed.
  - **Partially verified**: the content was read, but some reference details (e.g. author name or date) still need confirming.
  - **Unverified (AI memory)**: suggested from the assistant's prior knowledge and not yet checked against the source.
  - **Search snippet only**: seen in search results but the full text wasn't read.
  - **Unreachable**.
  - **Not used**.
- The References list in each report is built **only** from the sources actually cited in that report.

---

## A. Actual Budget: primary sources (project's own material)

Research method: the Actual repository was cloned (`master`, commit `27290a8`, 2026-10-19), with sparse checkout of `.github/`, root files and `packages/docs/`. The actualbudget.org website could not be reached from the research environment. Its pages are built from `packages/docs/`, so their content was read from those source files. **The author should open each live URL once in a browser before citing it.**

### S01 — Actual Budget GitHub repository
- **APA:** Actual Budget. (2026). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual
- **Accessed:** 2026-10-20. **Status:** Verified.
- **Files read** (cite individual files only if needed):
  - `README.md`: product description, install options, packages.
  - `PRODUCT.md`: users, purpose ("users trusting the numbers"), design principles, WCAG 2.1 AA target.
  - `CODE_REVIEW_GUIDELINES.md`: review rules.
  - `CODEOWNERS`: area owners.
  - `LICENSE.txt`: MIT licence text, copyright James Long.
  - `.github/PULL_REQUEST_TEMPLATE.md`, `.github/ISSUE_TEMPLATE/feature-request.yml`, `.github/ISSUE_TEMPLATE/config.yml`.
  - `.github/workflows/*`: CI list; `cut-release-branch.yml` (monthly cut on the 25th); `issues-close-feature-requests.yml` (voting backlog); `stale.yml`; `count-points.yml`.
- **Used in:** `research/actual-development-process.md`; Sections 1.2–1.4 and 2.1.

### S02 — Contributing to Actual Budget (docs page)
- **APA:** Actual Budget. (n.d.). *Contributing to Actual Budget*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/
- **Source file:** `packages/docs/docs/contributing/index.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** list of main contributors and alumni; "We do not assign issues to specific people"; "mental health of the maintainers will be prioritized"; development workflow; release-note requirement; design strategy.
- **Used in:** Section 2.1.

### S03 — How to cut a release (docs page)
- **APA:** Actual Budget. (n.d.). *How to cut a release*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/releasing
- **Source file:** `packages/docs/docs/contributing/releasing.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** YY.M.patch versioning; release branches; automatic cut on the 25th; at least 2 maintainer approvals; smoke tests; publishing channels.
- **Used in:** Section 2.1 (release train).

### S04 — New core contributors guide (docs page)
- **APA:** Actual Budget. (n.d.). *New core contributors guide*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide
- **Source file:** `packages/docs/docs/contributing/leadership/new-core-contributors-guide.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** no assigned roles; reviewing is the most valued work; PR review guidelines; disagreement escalation (two people → team → public vote).
- **Used in:** Section 2.1.

### S05 — Triaging issues (docs page)
- **APA:** Actual Budget. (n.d.). *Triaging issues*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/triaging-issues
- **Source file:** `.../leadership/triaging-issues.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** triage labels; `needs info` auto-close after 7 days; tech support redirected to Discord.
- **Used in:** Section 2.1.

### S06 — Architecture decision records (docs page)
- **APA:** Actual Budget. (n.d.). *Architecture decision records*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/architecture-decision-records
- **Source file:** `.../leadership/architecture-decision-records.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** ADRs exist; an example decision on bank-sync credential storage.
- **Used in:** `research/` (possible use in Sections 2.1 and 3).

### S07 — Feature flags (docs page)
- **APA:** Actual Budget. (n.d.). *Feature flags (experimental features)*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/project-details/feature-flags
- **Source file:** `.../project-details/feature-flags.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** incremental delivery through feature flags; flags removed after 3 months of inactivity.
- **Used in:** Section 2.1.

### S08 — Paying reviewers for administrative work (docs page)
- **APA:** Actual Budget. (n.d.). *Paying reviewers for administrative work*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors
- **Source file:** `.../leadership/paying-contributors.md`. **Status:** Verified (content); live URL `[to verify in browser]`.
- **Taken:** USD 2,000/month stipend pool; points-based; donations about USD 3,000–3,500 a month.
- **Used in:** Section 2.1 (constraints).

### S09 — Testing guide (docs page)
- **APA:** Actual Budget. (n.d.). *Testing*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/testing
- **Source file:** `.../contributing/testing.md`. **Status:** Verified (headings only so far). Read in full before using it in Section 3.
- **Taken:** Vitest unit tests, Playwright E2E tests, visual regression tests.
- **Used in:** Section 2.1; planned for Section 3.

### S10 — Roadmap for 2025 (blog post)
- **APA:** Janis, M. [to verify the author's name form; GitHub handle MatissJanis]. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025
- **Source file:** `packages/docs/blog/2025-01-02-roadmap-for-2025.md`. Also appeared in a web search. **Status:** Partially verified (content read; author name form to confirm).
- **Taken:** "In early 2022 James, the creator of Actual Budget, decided to close-down the commercial product and open source it"; PRs stuck unreviewed for months; about 50 open PRs; the volunteer core team formed; Discord with over 7,000 members; "upwards of a million docker container clones per month".
- **Used in:** Section 1.2 (history); Sections 2.1 and 2.2 (review bottleneck).

### S11 — Roadmap for 2026 (blog post)
- **APA:** youngcw. [to verify whether a real name is available]. (2025, December 20). *Roadmap for 2026*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2026
- **Source file:** `packages/docs/blog/2025-12-20-roadmap-for-2026.md`. **Status:** Partially verified.
- **Taken:** 2025 features in review; 2025 roadmap achieved except plugins; maintainer stipends; over 8,000 PikaPods users.
- **Used in:** Sections 2.1 and 1.4.

### S12 — Fighting AI slop (blog post)
- **APA:** Janis, M. [to verify]. (2025, November 15). *Fighting AI slop*. Actual Budget. https://actualbudget.org/blog/fighting-ai-slop
- **Source file:** `packages/docs/blog/2025-11-15-fighting-ai-slop.md`. **Status:** Partially verified (first part read).
- **Taken:** a policy of closing fully AI-generated PRs and issues to protect maintainer time.
- **Used in:** `research/` (possible use in Section 2.2 as a risk or constraint).

### S13 — Welcome to Actual Budget Open Source (blog post)
- **APA:** Actual Budget. (n.d. [to verify date]). *Welcome to Actual Budget Open Source*. https://actualbudget.org/blog/welcome-actualbudget-os
- **Source file:** `packages/docs/blog/welcome.md`. **Status:** Read; **not used** (it only covers the move to actualbudget.org).

---

## B. Other web sources about Actual Budget

### S14 — James Long's open-source announcement
- **APA (draft):** Long, J. (2022). *Actual is going open-source* [Blog post]. https://jlongster.com/actual-open-source
- **Status:** **Unreachable.** The URL returns 404 (checked by the author in a browser, 2026-10-20). The author found an archive at https://archive.jlongster.com/#posts, but it couldn't be reached from the research environment, and neither could the Wayback Machine. Known only from search snippets ("over 4 years" in development; hosted service ending).
- **Decision:** don't cite it. Use S10 for the history instead.

### S15 — The Changelog podcast, episode 495
- **APA (draft):** Stacoviak, A., & Santo, J. [to verify hosts] (Hosts). (2022, July [to verify day]). *[Episode title to verify]* (No. 495) [Audio podcast episode]. In *The Changelog*. Changelog Media. https://changelog.com/podcast/495
- Related listings: https://changelog.com/person/jlongster; https://dev.to/changelog/actually-opening-up
- **Status:** Search snippet only. It describes Actual as built "as a business for over 4 years before recently opening it up and making it 100% free".
- **Used in:** `research/` as secondary corroboration only. Not planned for the report unless verified.

### S16 — tmpdir community forum thread
- **Ref:** "Actual Budget is switching to open source" [Forum thread]. https://community.tmpdir.org/t/actual-budget-is-switching-to-open-source/497
- **Status:** Search snippet only. It contains second-hand claims about the creator's motives (burnout or the business failing). **Not used**, because it is unreliable.

---

## C. Methodology literature found by web search

### S17 — Nikitina et al. (2012): Scrum to Scrumban case study
- **APA:** Nikitina, N., Kajko-Mattsson, M., & Strale, M. (2012). From Scrum to Scrumban: A case study of a process transition. In *Proceedings of the 2012 International Conference on Software and System Process (ICSSP)* (pp. 140–149). [Publisher and DOI to verify]
- **Found via:** web search → DBLP listing https://dblp.uni-trier.de/pid/27/5607
- **Status:** Search snippet only (bibliographic details; full text not read).
- **Used in:** Section 2.3 screening, as proof that Scrumban passes the proof rule (Scrumban was then cut from the shortlist).

### S18 — Scrumban in hybrid environments (JSERD)
- **Ref (draft):** [Authors to verify]. (2026 [to verify]). Scrumban in hybrid environments: An empirical investigation of organizational use and impact in development teams. *Journal of Software Engineering Research and Development*. https://journals-sol.sbc.org.br/index.php/jserd/article/view/7887
- **Status:** Search snippet only (a survey of 15 team members and interviews with 3 managers; Scrumban needed adapting for hardware teams).
- **Used in:** screening evidence for Scrumban only.

### S19 — Yilmaz & O'Connor (2016): Scrumban and gamification
- **Ref (draft):** Yilmaz, M., & O'Connor, R. V. (2016). A Scrumban integrated gamification approach to guide software process improvement: A Turkish case study. *[Journal to verify]*. https://core.ac.uk/works/9783546 (also https://caa.cankaya.edu.tr/entities/publication/ab175a98-6e79-470e-a8a5-28ad26d9e916/full)
- **Status:** Search snippet only.
- **Used in:** screening evidence for Scrumban only.

### S20 — Scrumban in distributed software factories (Finland/Italy)
- **Ref:** [Title, authors and URL to verify]. Possibly one of https://doras.dcu.ie/21097 or https://researchrepository.ul.ie/entities/publication/ccd665c0-0fea-4335-8b2a-3d3b2c4d7565
- **Status:** Search snippet only. The summary said limited WIP and visibility help distributed coordination.
- **Used in:** screening evidence only.

### S21 — Scrumban bachelor's thesis (Theseus, Finland)
- **Ref:** *Scrumban - Adaptive agile development process: Using scrumban to improve software development process* [Bachelor's thesis]. https://www.theseus.fi/handle/10024/77014
- **Status:** Search snippet only. **Not used** (a student thesis is weak evidence).

### S22 — Shape Up: the book
- **APA (draft):** Singer, R. (2019). *Shape Up: Stop running in circles and ship work that matters*. Basecamp. [URL to verify, probably https://basecamp.com/shapeup]
- **Status:** Unverified (AI memory and search snippets).
- **Used in:** Section 2.3 screening, to justify **dropping** Shape Up (no peer-reviewed evidence).

### S23 — Shape Up practitioner articles (evidence of weak evidence)
- Mind the Product. *7 lessons from trialling Basecamp's 'Shape Up' methodology*. https://www.mindtheproduct.com/7-lessons-from-trialling-basecamps-shape-up-methodology/ [author and date to verify]
- Debecker, A. [to verify]. *Update report: Trialing Basecamp's Shape Up methodology*. HackerNoon. https://hackernoon.com/update-report-trialing-basecamps-shape-up-methodology [URL form to verify]
- Curious Lab. *Dispelling myths about Basecamp's Shape Up*. https://curiouslab.io/blog/basecamp-shape-up-myths
- Curious Lab. *What is Basecamp's Shape Up method?: A complete overview*. https://www.curiouslab.io/blog/what-is-basecamps-shape-up-method-a-complete-overview
- Aguiar, K. F. [to verify]. *Basecamp and Shape Up: Real world experience*. DEV Community. https://dev.to/kevinfaguiar/basecamp-and-shape-up-real-world-experience-599
- London, D. [to verify]. *How we started implementing Basecamp's Shape Up process…*. Medium. https://medium.com/@dlondon4/how-we-started-implementing-basecamps-shape-up-process-and-greatly-accelerated-delivering-value-e48d356fae5b
- Lucid. *Shape Up methodology: What it is and how to use it*. https://app.lucidspark.com/blog/shape-up-methodology
- **Status:** Search snippets only. **Not planned for citation.** They are logged as the basis for the "no peer-reviewed evidence" conclusion.

---

## D. Literature suggested from AI memory: UNVERIFIED, must be checked before use

These were named in the planning notes from the assistant's prior knowledge. **None has been checked yet.**

| ID | Draft APA reference | Mentioned for |
|---|---|---|
| S24 | Raymond, E. S. (1999). *The cathedral and the bazaar: Musings on Linux and open source by an accidental revolutionary*. O'Reilly. | Bazaar/OSS baseline |
| S25 | Mockus, A., Fielding, R. T., & Herbsleb, J. D. (2002). Two case studies of open source software development: Apache and Mozilla. *ACM Transactions on Software Engineering and Methodology, 11*(3), 309–346. | Bazaar/OSS baseline |
| S26 | Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer, 21*(5), 61–72. | Spiral |
| S27 | Ladas, C. (2009). *Scrumban: Essays on kanban systems for lean software development*. Modus Cooperandi Press. | Scrumban origin |
| S28 | Anderson, D. J. (2010). *Kanban: Successful evolutionary change for your technology business*. Blue Hole Press. | Kanban ("start with what you do now", WIP limits) |
| S29 | Poppendieck, M., & Poppendieck, T. (2003). *Lean software development: An agile toolkit*. Addison-Wesley. | Lean (folded into Kanban) |
| S30 | Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The science of lean software and DevOps*. IT Revolution Press. | DevOps evidence (DORA) |
| S31 | Khomh, F., Dhaliwal, T., Zou, Y., & Adams, B. (2012). Do faster releases improve software quality? An empirical case study of Mozilla Firefox. In *Proceedings of the 9th IEEE Working Conference on Mining Software Repositories* (pp. 179–188). IEEE. | Release train (Firefox rapid release) |
| S32 | Scaled Agile, Inc. (n.d.). *Agile release train*. SAFe framework website. | Release train term (SAFe) |

Still needed for the shortlist (to be sourced): authoritative references for **Scrum** (e.g. the Scrum Guide), **XP** (e.g. Beck's *Extreme Programming Explained*), **DevOps**, plus recent journal papers (the brief asks for topics "currently under discussion in academic journals"), e.g. hybrid and agile studies in OSS.

---

## E. Module materials

### S33 — APU lecture slides, CT051-3-3 Software Quality Engineering (L1–L6)
- **APA (draft, per slide deck):** Asia Pacific University of Technology & Innovation. (n.d.). *Process models* [Lecture slides]. CT051-3-3 Software Quality Engineering. [Check the lecturer's preferred format for citing module slides.]
- **Files:** `Lecture Slides/` (L1 Software Quality, L2 Process Models, L3 SQAP, L4 Quality Standards, L5 and L6 SQ Activities & Techniques).
- **Status:** Verified (read).
- **Used in:** the brief summary; Section 2.2 (L2's eight selection factors); Sections 3 and 4 later.
- Note: the L2 comparison table cites GeeksforGeeks ("How to choose the best SDLC model for your project"). If it is used, cite the original GeeksforGeeks page, not the slides.

---

## F. Search log

| Date | Tool | Query / URL | Outcome |
|---|---|---|---|
| 2026-10-20 | git clone | github.com/actualbudget/actual (sparse) | S01–S13 |
| 2026-10-20 | WebFetch | actualbudget.org/docs/contributing/ (+ /project-details/, /releasing) | Unreachable (DNS) → used repo source files |
| 2026-10-20 | WebSearch | "James Long Actual budget open source announcement 2022 shutting down" | S10, S14, S15, S16; also startups.fm, player.fm, hackliberty, bizarro.dev.to (not used) |
| 2026-10-20 | WebFetch | jlongster.com/actual-open-source | Unreachable (DNS); 404 in the author's browser |
| 2026-10-20 | WebFetch | archive.jlongster.com | Unreachable (DNS) |
| 2026-10-20 | WebFetch | web.archive.org (jlongster post) | Blocked |
| 2026-10-20 | WebSearch | "Actual is going open-source" jlongster April 2022 | S15; the other results were unrelated (photoflare.io, launchpad, zenml, opensource.com, jupiterbroadcasting) and not used |
| 2026-10-20 | WebSearch | Scrumban case study empirical "From Scrum to Scrumban" Nikitina Kajko-Mattsson | S17–S21 |
| 2026-10-20 | WebSearch | Shape Up Basecamp methodology empirical study adoption research paper | S22, S23 (no peer-reviewed studies found) |
