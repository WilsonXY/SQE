# Sources Register

This file logs **every** source consulted while planning, whether or not it ends up in the report. See the rules in `AGENTS.md` → *Citations and sources*.

## Legend

**Format:** APA 7th edition. `[to verify]` marks a detail not yet confirmed.

**Status**
- **Verified**: bibliographic details confirmed from an authoritative record (publisher page, Crossref/DOI, Semantic Scholar, Open Library, or the source itself) **and** the content or abstract was read.
- **Details verified**: bibliographic details confirmed, but the content or abstract has **not** been read yet. Read it before citing.
- **Partially verified**: some details still `[to verify]`.
- **Unverified (AI memory)**: suggested from the assistant's memory and not yet checked.
- **Search snippet only**, **Unreachable**, **Not used**.

**Recency** (university rule: prefer the last 5 years; "today" = 2026-10-20, so 2021 or later)
- **Recent**: published 2021 or later. Preferred.
- **Root**: older, but the original or defining source of the concept (e.g. the creator's own book or paper). Allowed.
- **Golden**: older, but a seminal or highly cited work in the field. Allowed, with justification.
- **Old**: older and neither root nor golden. **Avoid citing**; find a recent alternative.

**Lecture slides** don't need to be cited (the author confirmed this, 2026-10-20). They are still used as guidance; see section E.

How verification was done (2026-10-20):
- Crossref API (`api.crossref.org`) and Semantic Scholar API for paper metadata and abstracts.
- Open Library API for books.
- Direct HTTP checks (curl through the environment proxy) for web pages.
- Actual's repository source files for the docs and blog content.

---

## A. Actual Budget: primary sources

All live URLs below returned **HTTP 200** on 2026-10-20 (curl via proxy). Content was read from the matching source files in `actualbudget/actual` at commit `27290a8`. The website is built from `packages/docs/`. Blog author names come from `packages/docs/blog/authors.yml`.

| ID | APA 7 reference | Status · Recency | Taken from it | Used in |
|---|---|---|---|---|
| S01 | Actual Budget. (2026). *Actual* [Computer software]. GitHub. https://github.com/actualbudget/actual | Verified · Recent | `README.md`, `PRODUCT.md`, `CODE_REVIEW_GUIDELINES.md`, `CODEOWNERS`, `LICENSE.txt` (MIT), PR and issue templates, `.github/workflows/*` (monthly cut on the 25th, voting backlog, stale PRs, points) | 1.2–1.4, 2.1 |
| S02 | Actual Budget. (n.d.). *Contributing to Actual Budget*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/ | Verified · Recent | Main contributors; "We do not assign issues to specific people"; maintainer mental health first; dev workflow; release notes | 2.1 |
| S03 | Actual Budget. (n.d.). *How to cut a release*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/releasing/ | Verified · Recent | YY.M.patch versioning; automatic cut on the 25th; ≥2 maintainer approvals; smoke tests | 2.1 |
| S04 | Actual Budget. (n.d.). *New core contributors guide*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/new-core-contributors-guide/ | Verified · Recent | No assigned roles; reviewing valued; disagreements → team → public vote | 2.1 |
| S05 | Actual Budget. (n.d.). *Triaging issues*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/triaging-issues/ | Verified · Recent | Triage labels; `needs info` auto-close after 7 days | 2.1 |
| S06 | Actual Budget. (n.d.). *Architecture decision records*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/architecture-decision-records/ | Verified · Recent | ADRs exist; bank-sync credential storage decision | 2.1, possibly 3 |
| S07 | Actual Budget. (n.d.). *Feature flags (experimental features)*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/project-details/feature-flags/ | Verified · Recent | Incremental delivery; flags removed after 3 months of inactivity | 2.1 |
| S08 | Actual Budget. (n.d.). *Paying reviewers for administrative work*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/leadership/paying-contributors/ | Verified · Recent | USD 2,000/month stipend pool; donations about USD 3,000–3,500 a month | 2.1, 2.2 |
| S09 | Actual Budget. (n.d.). *Testing*. Retrieved October 20, 2026, from https://actualbudget.org/docs/contributing/testing/ | Verified (headings only; read in full for Section 3) · Recent | Vitest, Playwright E2E, visual regression tests | 2.1, 3 |
| S10 | Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2025/ | Verified · Recent | "In early 2022 James, the creator of Actual Budget, decided to close-down the commercial product and open source it"; PRs stuck unreviewed for months; about 50 open PRs; core team formed; Discord with over 7,000 members; "upwards of a million docker container clones per month" | 1.2, 2.1, 2.2 |
| S11 | youngcw. (2025, December 20). *Roadmap for 2026*. Actual Budget. https://actualbudget.org/blog/roadmap-for-2026/ | Verified · Recent | 2025 review; roadmap achieved except plugins; stipends; over 8,000 PikaPods users. (`authors.yml` lists the name only as "youngcw", so APA uses the username.) | 1.4, 2.1 |
| S12 | Aboltins, M. J. (2025, November 15). *Fighting AI slop*. Actual Budget. https://actualbudget.org/blog/fighting-ai-slop/ | Verified (first part read) · Recent | Policy of closing fully AI-generated PRs and issues to protect maintainer time | possibly 2.2 (risk) |
| S13 | Actual Budget. (n.d.). *Welcome to Actual Budget Open Source*. https://actualbudget.org/blog/welcome-actualbudget-os | Read · **Not used** | Only covers the move to actualbudget.org | — |

> Correction (2026-10-20): S10 and S12 were first logged as "Janis, M.". The blog's `authors.yml` gives the full name **Matiss Janis Aboltins**, so the APA form is **Aboltins, M. J.** and the in-text form is **(Aboltins, 2025)**.

---

## B. Other sources about Actual Budget

| ID | APA 7 reference | Status · Recency | Notes |
|---|---|---|---|
| S14 | Long, J. (2022). *Actual is going open-source* [Blog post]. https://jlongster.com/actual-open-source | **Unreachable** · — | 404 in the author's browser. archive.jlongster.com (reachable via proxy) only holds posts up to May 2020, so the 2022 post isn't there. **Not cited.** |
| S15 | Stacoviak, A., & Santo, J. (Hosts). (2022, July 1). *Actual(ly) opening up with James Long* (No. 495) [Audio podcast episode]. In *The Changelog*. Changelog Media. https://changelog.com/podcast/495 | **Verified** (page metadata and transcript; recorded June 15, 2022) · Recent | James Long describes building Actual "as a business for over 4 years before" open-sourcing it. The transcript has no exact open-source date. **Optional** support for the history in 1.2. |
| S16 | "Actual Budget is switching to open source" [Forum thread]. https://community.tmpdir.org/t/actual-budget-is-switching-to-open-source/497 | Search snippet only · **Not used** | Second-hand claims about the creator's motives. Unreliable. |

---

## C. Methodology literature (Section 2)

### C1. Root and golden sources for each shortlisted methodology and the baseline

| ID | APA 7 reference | Status · Recency | Used for |
|---|---|---|---|
| S26 | Boehm, B. W. (1988). A spiral model of software development and enhancement. *Computer, 21*(5), 61–72. https://doi.org/10.1109/2.59 | Details verified (Crossref) · **Root** | Spiral (candidate) |
| S34 | Schwaber, K., & Sutherland, J. (2020). *The Scrum guide*. https://scrumguides.org/scrum-guide.html | Verified (page read: November 2020 version; "Scrum is a lightweight framework…"; a Scrum Team is "typically 10 or fewer people"; roles Product Owner, Scrum Master, Developers) · **Root** (the official definition; 2020 is the current version) | Scrum (candidate) |
| S35 | Beck, K., & Andres, C. (2005). *Extreme programming explained: Embrace change* (2nd ed.). Addison-Wesley. | **Verified** (copyright page of the author's excerpt PDF, 2026-10-20: "Kent Beck with Cynthia Andres", Second Edition, "Text copyright © 2005 Pearson Education, Inc.", Addison-Wesley, ISBN 0-321-27865-8; LoC CIP dated 2004, so **APA year = 2005**, the copyright year). The excerpt holds front matter, the table of contents and Chapter 1. **Content read: TOC and Ch. 1 only.** Primary practices (Ch. 7) include *Sit Together*, *Whole Team*, *Pair Programming*, *Weekly Cycle*, *Quarterly Cycle*, *Ten-Minute Build*, *Continuous Integration*, *Test-First Programming*, *Incremental Design*. Corollary practices (Ch. 9) include *Real Customer Involvement*, *Shared Code*, *Daily Deployment*. **Read Ch. 7 before citing practice details.** · **Root** | XP (candidate): co-location ("Sit Together") and weekly cycles vs a distributed volunteer team |
| S28 | Anderson, D. J. (2010). *Kanban: Successful evolutionary change for your technology business*. Blue Hole Press. | **Details verified** (Google Books page the author supplied, id RJ0VUkfUWZkC: full title as above, Blue Hole Press, 2010, ISBN 9780984521401, 261 pp.). Content not read directly. · **Root** | Kanban (candidate). **Correction:** "start with what you do now" came from AI memory and is **not verified**. Use instead Anderson's own definition as quoted in S38: Kanban "is an evolutionary change method … the process is evolutionary and incremental" (Anderson, 2010, p. 6, as cited in Ahmad et al., 2018). Better still, check p. 6 in the book itself (library) so it can be cited directly. |
| S30 | Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The science of lean software and DevOps: Building and scaling high performing technology organizations*. IT Revolution Press. | Details verified (Open Library) · **Golden** | DevOps (candidate) |
| S24 | Raymond, E. S. (1999). *The cathedral and the bazaar: Musings on Linux and open source by an accidental revolutionary*. O'Reilly. | **Details verified** (Google Books, ISBN 1565927249: full title as above, O'Reilly, 1999, 268 pp.; a revised 2001 edition also exists, ISBN 0596001088). **Content not read.** Any claim about it (e.g. "release early, release often") must be checked in the text before citing. · **Root** | OSS "Bazaar" baseline |
| S25 | Mockus, A., Fielding, R. T., & Herbsleb, J. D. (2002). Two case studies of open source software development: Apache and Mozilla. *ACM Transactions on Software Engineering and Methodology, 11*(3), 309–346. https://doi.org/10.1145/567793.567795 | **Verified** (Crossref and abstract read) · **Golden** | OSS baseline: core team size, code ownership, defect density, problem resolution in OSS |
| S29 | Poppendieck, M., & Poppendieck, T. (2003). *Lean software development: An agile toolkit*. Addison-Wesley. | Details verified (Open Library) · **Root** | Lean, as Kanban's foundation (one sentence) |

### C2. Recent sources (2021 or later) for Section 2

| ID | APA 7 reference | Status · Recency | Key point (from abstract) | Planned use |
|---|---|---|---|---|
| S36 | Kuhrmann, M., Tell, P., Hebig, R., Klünder, J., Münch, J., Linssen, O., Pfahl, D., Felderer, M., Prause, C. R., MacDonell, S. G., Nakatumba-Nabende, J., Raffo, D., Beecham, S., Tüzün, E., López, G., Paez, N., Fontdevila, D., Licorish, S. A., Küpper, S., … Richardson, I. (2022). What makes agile software development agile? *IEEE Transactions on Software Engineering, 48*(9), 3523–3539. https://doi.org/10.1109/TSE.2021.3099532 | **Verified** (abstract read) · Recent | International survey with 556 data points. Fewer than 15% of projects run purely traditional or purely agile. Processes "mutate into hybrids over time". The choice of **practices** affects agility more than the named method. | 2.4 and 2.6: justifies tailoring one methodology; critical evaluation |
| S37 | Alaidaros, H., Omar, M., & Romli, R. (2021). The state of the art of agile kanban method: Challenges and opportunities. *Independent Journal of Management & Production, 12*(8), 2535–2550. https://doi.org/10.14807/ijmp.v12i8.1482 | **Verified** (abstract read) · Recent | A literature review: Kanban's popularity is growing, but it still has open challenges and limitations. | 2.3 and 2.6: Kanban evidence and limitations |
| S38 | Ahmad, M. O., Dennehy, D., Conboy, K., & Oivo, M. (2018). Kanban in software engineering: A systematic mapping study. *Journal of Systems and Software, 137*, 96–113. https://doi.org/10.1016/j.jss.2017.11.045 | **Verified** (full-text PDF supplied by the author, read 2026-10-20) · **Golden** (the main Kanban mapping study, about 123 citations) | Reviews 382 studies, with 23 primary studies and 23 experience reports (2006–2016). Lists Kanban principles: visualise workflow, limit WIP, measure and manage flow (pp. 97–98). **Benefits (Table 13, p. 105):** visibility and transparency (16 studies), better control (12), finding impediments to flow (10), better workflow (7), fewer defects (4), better quality (4), "a lightweight intuitive method" (4). **Challenges (Table 14, p. 106):** setting up and maintaining Kanban; organisational culture; lack of supporting practices; lack of training. **Conclusion (p. 110):** Kanban "is a relatively basic flow tool that needs to be supported by additional practices". It also quotes Anderson (2010, p. 6): Kanban is "an evolutionary change method". | 2.3 (Kanban description), 2.4/2.5 (**justifies tailoring Kanban with CI and testing practices**), 2.6 (challenges) |
| S49 | Harzl, A. (2016). Combining FOSS and Kanban: An action research. In *Open Source Systems: Integrating Communities* (IFIP Advances in Information and Communication Technology, pp. 71–84) [book title `to verify`]. Springer. https://doi.org/10.1007/978-3-319-39225-7_6 | Details verified (Crossref; found via S38's reference list) · **Old** (2016, 2 citations) | Kanban used in a free/open-source software project: direct evidence for C10. Abstract not read yet. | Possibly 2.3/2.4. **Use only if no recent source on Kanban in OSS is found.** |
| S39 | Amaro, R., Pereira, R., & da Silva, M. M. (2023). Capabilities and practices in DevOps: A multivocal literature review. *IEEE Transactions on Software Engineering, 49*(2), 883–901. https://doi.org/10.1109/TSE.2022.3166626 | **Verified** (abstract read) · Recent | DevOps adoption is still inconsistent. There is a "lack of clarity" about DevOps capabilities. 93 documents reviewed, giving 37 capabilities. | 2.3 and 2.6: DevOps definition and its weakness as a full methodology |
| S40 | DORA. (2024). *Accelerate state of DevOps report 2024* (Version 2024.3). Google Cloud. https://dora.dev/research/2024/dora-report/ | **Verified** (the author's PDF covers report pp. 1–49, version 2024.3; read 2026-10-20). The authors page (p. 87) is **not** in the supplied copy, so the reference uses the group author "DORA". Add the individual authors later if the full report is available. · Recent | "Tenth DORA report"; over 39,000 professionals surveyed (p. 3). **Four keys** (p. 10): change lead time, deployment frequency, change fail rate, failed deployment recovery time. Rework rate added, giving the throughput vs stability factors (p. 11). "Stable priorities boost productivity"; unstable priorities lead to "substantial increases in burnout" (p. 6). Continuous improvement is "achieved iteratively and incrementally" (p. 7). | 2.3 (DevOps evidence); **also Assignment 2 (Software Metrics)** |
| S41 | Soares, E., Sizilio, G., Santos, J., da Costa, D. A., & Kulesza, U. (2022). The effects of continuous integration on software development: A systematic literature review. *Empirical Software Engineering, 27*(3), Article [number to verify]. https://doi.org/10.1007/s10664-021-10114-1 | **Verified** (abstract read; online 2021-03-09) · Recent | Covers 101 empirical studies. CI mostly brings positive effects (e.g. cooperation, quality assurance) but also technical and process challenges. | 2.3/2.4 (XP and DevOps practices); Section 3 |
| S42 | Song, Y., Mahmood, T., & Rehman, U. U. (2024). Selection of software development methodology by employing a multi-criteria decision-making approach based on logarithmic bipolar complex fuzzy aggregation operators. *IEEE Access, 12*, 38163–38179. https://doi.org/10.1109/ACCESS.2024.3373708 | **Verified** (abstract read) · Recent | Choosing a methodology is a multi-criteria decision problem (complexity, team size, customer collaboration, pace). Multi-criteria decision-making helps "quantify and assess these factors". | 2.2 and 2.4: **justifies using a weighted decision matrix** |
| S43 | Wessel, M., Vargovich, J., Gerosa, M. A., & Treude, C. (2023). GitHub Actions: The impact on the pull request process. *Empirical Software Engineering, 28*(6), Article [number to verify]. https://doi.org/10.1007/s10664-023-10369-w | **Verified** (abstract read) · Recent | About 30% of the top 5,000 repos use GitHub Actions. After adoption: more PR rejections and more time to accept a PR. | 2.1 (Actual's CI) and Section 3 |
| S44 | Wessel, M., Serebrenik, A., Wiese, I., Steinmacher, I., & Gerosa, M. A. (2022). Quality gatekeepers: Investigating the effects of code review bots on pull request activities. *Empirical Software Engineering, 27*(5), Article [number to verify]. https://doi.org/10.1007/s10664-022-10130-9 | **Verified** (abstract read) · Recent | In OSS projects, code review bots raise monthly merged PRs and lower non-merged PRs and developer communication. | Section 3 (Actual uses CodeRabbit) |
| S47 | Salkever, A. (2023). *Open source maintainers: Exploring the people, practices, and constraints facing the world's most critical open source software projects*. The Linux Foundation. https://doi.org/10.70828/lddj8886 | **Verified** (full PDF supplied by the author, read 2026-10-20; July 2023; foreword by Shuah Khan; CC BY-ND 4.0) · Recent | Qualitative interviews with **32 maintainers** of top-200 critical OSS projects (p. 5). Growing demands on maintainers' time mean less effort to welcome new contributors (p. 5). Infographic: not answering PRs on time discourages new contributors; "Embrace automation". **Burnout (pp. 26–27):** open-source work is never finished ("There will always be PRs and issues waiting"); consensus-heavy decision-making "may accelerate burnout"; fast-growing projects with administrative overhead are "not advisable" as "an unpaid hobby"; maintainers use bots and automation, set boundaries and step away. Conclusion: "there is no one-size-fits-all playbook" (p. 28). | 2.2 (constraints C2, C7, C8; burnout risk), 2.6. **Replaces S45** as the burnout source. |
| S45 | Raman, N., Cao, M., Tsvetkov, Y., Kästner, C., & Vasilescu, B. (2020). Stress and burnout in open source: Toward finding, understanding, and mitigating unhealthy interactions. In *Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering: New Ideas and Emerging Results* (pp. 57–60). ACM. https://doi.org/10.1145/3377816.3381732 | Verified (abstract read) · **Old** | OSS developers report high stress from feature and bug-fix demands. | **Superseded by S47. Not used.** |
| S48 | Eghbal, N. (2020). *Working in public: The making and maintenance of open source software*. Stripe Press. | Partially verified (Open Library lists the author as Nadia Asparouhova, her later name; the book was published under Nadia Eghbal `[to verify on the copy]`) · Old / possibly golden | Not read | Optional (OSS maintainership). Probably not needed. |
| S46 | Trujillo, M. Z., Hébert-Dufresne, L., & Bagrow, J. (2022). The penumbra of open source: Projects outside of centralized platforms are longer maintained, more academic and more collaborative. *EPJ Data Science, 11*(1). https://doi.org/10.1140/epjds/s13688-022-00345-7 | Verified (abstract read) · Recent | About OSS projects hosted outside GitHub. | **Not used** (not relevant enough) |

### C3. Screening-only sources (candidates that were dropped or cut)

| ID | APA 7 reference | Status · Recency | Notes |
|---|---|---|---|
| S17 | Nikitina, N., Kajko-Mattsson, M., & Strale, M. (2012). From Scrum to Scrumban: A case study of a process transition. In *2012 International Conference on Software and System Process (ICSSP)* (pp. 140–149). IEEE. https://doi.org/10.1109/ICSSP.2012.6225959 | Details verified (Crossref) · Old | Scrumban evidence. Scrumban was cut, so this is **not planned for citation**. If 2.3 needs one Scrumban citation, use S18 (recent) instead. |
| S18 | Meireles, M. A. C., Soares, K., Afonso, Á., Lobão de Araújo, L., Lobão, L., & Pinheiro, G. (2026). Scrumban in hybrid environments: An empirical investigation of organizational use and impact in development teams. *Journal of Software Engineering Research and Development, 14*(1), 498–516. https://doi.org/10.5753/jserd.2026.7887 | **Verified** (abstract read) · Recent | A field study (15 surveyed, 3 interviewed). Scrumban was adopted for coordination and workflow visibility. Shows Scrumban is real and in current use. |
| S19 | Yilmaz, M., & O'Connor, R. V. (2016). A Scrumban integrated gamification approach to guide software process improvement: A Turkish case study. *Tehnički Vjesnik, 23*(1). https://doi.org/10.17559/TV-20140922220409 | Partially verified (Crossref lists no authors; authors from the search snippet) · Old | **Not used.** |
| S20 | Banijamali, A., Dawadi, R. [to verify first name], Ahmad, M. O., Similä, J., Oivo, M., & Liukkunen, K. (2016). An empirical study on the impact of Scrumban on geographically distributed software development. In *Proceedings of the 4th International Conference on Model-Driven Engineering and Software Development* (pp. 567–577). SCITEPRESS. https://doi.org/10.5220/0005686405670577 | Details verified (Crossref) · Old | The Finland/Italy distributed study (resolved). **Not used.** |
| S21 | *Scrumban - Adaptive agile development process: Using scrumban to improve software development process* [Bachelor's thesis]. https://www.theseus.fi/handle/10024/77014 | Search snippet only · — | **Not used** (a student thesis). |
| S27 | Ladas, C. (2009). *Scrumban: Essays on kanban systems for lean software development*. Modus Cooperandi Press. | Details verified (Open Library) · Root | Scrumban origin. **Not planned** (Scrumban was cut). |
| S22 | Singer, R. (2019). *Shape Up: Stop running in circles and ship work that matters*. Basecamp. https://basecamp.com/shapeup | Details verified (Open Library: Singer, 2019, Basecamp; URL returns 200; subtitle `[to verify]`) · Root | Used only to say Shape Up was **dropped** for lack of peer-reviewed evidence. |
| S23 | Shape Up practitioner articles: Mind the Product (https://www.mindtheproduct.com/7-lessons-from-trialling-basecamps-shape-up-methodology/), HackerNoon (https://hackernoon.com/update-report-trialing-basecamps-shape-up-methodology), Curious Lab (https://curiouslab.io/blog/basecamp-shape-up-myths; https://www.curiouslab.io/blog/what-is-basecamps-shape-up-method-a-complete-overview), DEV (https://dev.to/kevinfaguiar/basecamp-and-shape-up-real-world-experience-599), Medium (https://medium.com/@dlondon4/how-we-started-implementing-basecamps-shape-up-process-and-greatly-accelerated-delivering-value-e48d356fae5b), Lucid (https://app.lucidspark.com/blog/shape-up-methodology) | Search snippets only · — | **Not cited.** Logged as the basis for "no peer-reviewed evidence". |

### C4. Release Train

| ID | APA 7 reference | Status · Recency | Notes |
|---|---|---|---|
| S32 | Scaled Agile, Inc. (n.d.). *Agile release train*. Retrieved October 20, 2026, from https://framework.scaledagile.com/agile-release-train | Verified (page read: "Agile Release Train (ART) is a team of agile teams that collaborate for product and solution development") · Recent (living page) | Explains the SAFe meaning of the term, if 2.1 needs it. |
| S31 | Khomh, F., Dhaliwal, T., Zou, Y., & Adams, B. (2012). Do faster releases improve software quality? An empirical case study of Mozilla Firefox. In *2012 9th IEEE Working Conference on Mining Software Repositories (MSR)* (pp. 179–188). IEEE. https://doi.org/10.1109/MSR.2012.6224279 | Details verified (Crossref) · Old (arguably golden for rapid releases) | **Optional.** Actual's own docs (S03) are probably enough for 2.1. |

---

## D. Still to do before writing Section 2

- ~~Read S38, S40, S47~~: **done** 2026-10-20 (the author supplied the PDFs).
- ~~Confirm book subtitles and editions for S24, S28, S35~~: **done** 2026-10-20. S35's year is corrected to **2005**.
- ~~Recent OSS-burnout source to replace S45~~: **done** (S47).
- **Fill in article numbers** for S41, S43 and S44 (shown on the Springer article pages). Can be done at writing time.
- **Before citing specific content,** read the relevant parts: S35 Ch. 7 (XP practices); S24 (Bazaar claims); S28 p. 6 (to cite Anderson directly rather than via S38).
- Optional: a **recent** source on Spiral or risk-driven development; a **recent** source on Kanban in OSS (otherwise S49, which is old).

### Supplied files (held locally, not committed)

The author supplied these PDFs on 2026-10-20. They are **not committed to the repo**, because they are copyrighted (book excerpt, Elsevier article) or licensed CC BY-ND.
- `Extreme_Programming_Explained__Embrace_Change_-_9780321278654.pdf` (S35 excerpt)
- `2024-dora-accelerate-state-of-devops-report.pdf` (S40, pp. 1–49)
- `Open_Source_Maintainers_2023_-_Report.pdf` (S47)
- `Kanban_in_software_engineering__A_systematic_mapping_study_-_1-s2.0-S0164121217302820-main.pdf` (S38)

---

## E. Module materials (not cited)

| ID | Material | Notes |
|---|---|---|
| S33 | APU lecture slides, CT051-3-3 Software Quality Engineering (L1–L12), in `Lecture Slides/` | **Not cited in the report** (the author confirmed this). Used as guidance, e.g. L2's eight selection factors. Note: L2's SDLC comparison table comes from GeeksforGeeks ("How to choose the best SDLC model for your project"). If we reuse that table's content, cite GeeksforGeeks directly (after checking it). |

---

## F. Search and verification log

| Date | Tool | Query / URL | Outcome |
|---|---|---|---|
| 2026-10-20 | git clone | github.com/actualbudget/actual (sparse) | S01–S13 |
| 2026-10-20 | WebFetch | actualbudget.org docs pages | Unreachable (DNS); later reached via curl (all 200) |
| 2026-10-20 | WebSearch | "James Long Actual budget open source announcement 2022 shutting down" | S10, S14, S15, S16; also startups.fm, player.fm, hackliberty, bizarro.dev.to (not used) |
| 2026-10-20 | WebFetch / curl | jlongster.com/actual-open-source; archive.jlongster.com; web.archive.org | 404 / archive only goes to 2020 / blocked |
| 2026-10-20 | WebSearch | "Actual is going open-source" jlongster April 2022 | S15; photoflare.io, launchpad, zenml, opensource.com, jupiterbroadcasting (unrelated, not used) |
| 2026-10-20 | WebSearch | Scrumban case study empirical "From Scrum to Scrumban" Nikitina Kajko-Mattsson | S17–S21 |
| 2026-10-20 | WebSearch | Shape Up Basecamp methodology empirical study adoption research paper | S22, S23 |
| 2026-10-20 | curl | changelog.com/podcast/495 | S15 verified |
| 2026-10-20 | Crossref API | Title lookups for S17–S20, S25, S26, S31, S36–S39, S41–S47 | Metadata verified |
| 2026-10-20 | Crossref API (2021+ filter) | Keyword searches: Kanban SLR; Kanban WIP; OSS sustainability/burnout; OSS motivation; OSS code review; DevOps SLR; DevOps capabilities; Scrum distributed; Scrum OSS; XP/CI/TDD; hybrid approaches; methodology selection | Picked: S39, S42, S43, S44, S47. Seen but not evaluated or used: Villanueva et al. 2025 (Kanban SLR, ACM WSSE); Castillo Anzules & Guaña Moya 2024 (Spanish Kanban review); Gunawan & Budiardjo 2021; Foundjem & Adams 2021; Nayanajith & Wickramarachchi 2024; Hamza et al. 2024 (two DevOps SLRs); Mumbarkar & Prasad 2022; Lenarduzzi et al. 2021 (JSS, PR acceptance; possible for Section 3); Göçmen et al. 2025; Leong et al. 2023 (Sustainability, hybrid PM); Seniv 2022/2023; Hendrick & Ramaswami 2023 (LF, maintainer security; possible for Section 3); Raj & Costa 2026; Kupari et al. 2025; Zhou 2022 |
| 2026-10-20 | Semantic Scholar API | Abstracts for S36, S39, S41, S42, S45 | Abstracts read |
| 2026-10-20 | Open Library API | S22, S24, S27, S28, S29, S30, S35, S48 | Book details verified |
| 2026-10-20 | curl | scrumguides.org; framework.scaledagile.com/agile-release-train; basecamp.com/shapeup; dora.dev 2024/2025; linuxfoundation.org/research/open-source-maintainers | Pages verified (200) |
| 2026-10-20 | curl | catb.org (Raymond's essay online) | TLS certificate mismatch; not accessed |
| 2026-10-20 | curl | sciencedirect.com (S38 abstract) | Blocked; the author later supplied the full PDF |
| 2026-10-20 | Author-supplied PDFs | S35 excerpt, S38, S40 (pp. 1–49), S47 | Read (text extraction; DORA pp. 10–12 viewed as images because of a font issue) |
| 2026-10-20 | Google Books (curl) | id RJ0VUkfUWZkC (S28); ISBN 1565927249 and 0596001088 (S24) | Details verified |
| 2026-10-20 | Open Library / catb.org (curl) | Raymond ISBN lookups | Connection reset / DNS failure; Google Books used instead |
| 2026-10-20 | Crossref API | "Combining FOSS and Kanban: An Action Research" | S49 metadata |
