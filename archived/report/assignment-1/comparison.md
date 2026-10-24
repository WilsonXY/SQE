# Raw, Humanizer and pstack: writing comparison

## Read the complete versions

- [Raw AI-agent draft](before/report.md)
- [Humanizer rewrite](after/report.md)
- [Pstack technical-writing + unslop rewrite](pstack/report.md)

Each file contains the full executive summary, report body, figures, tables and References. Each rewrite starts from the same frozen raw draft. Pstack did not receive the Humanizer version.

## Measured differences

| Version | Counted words | Change from raw | Word-sequence similarity to raw |
|---|---:|---:|---:|
| Raw | 4,873 | Baseline | 100% |
| Humanizer | 4,934 | +61, about 1.3% | 75.2% |
| Pstack technical-writing + unslop | 4,905 | +32, about 0.7% | 80.4% |

Counts include report headings, tables, captions, notes and text diagrams, plus the executive summary. Front-matter lists and References are excluded. All versions fit the agreed 4,750-5,250 range. Counting conventions differ between applications, so these are approximate submission counts.

Word-sequence similarity compares lower-case word tokens in order using a sequence-matching calculation. It includes the tables and figures held constant. It is an editing measure, not a quality score or an AI-detection result. Under this measure, the Humanizer rewrite changed the wording more than the pstack rewrite.

Neither rewrite simply made the report shorter. Both often replaced dense sentences with several complete sentences. The raw draft already followed the handoff's plain-language requirements, so it did not contain every stereotypical pattern a writing skill might remove.

## Reading differences

Humanizer often reorganises a paragraph around its main claim and varies the length of neighbouring sentences. Pstack often makes individual statements shorter and their subjects more explicit. The approaches overlap considerably: both favour ordinary verbs, remove unnecessary framing and retain meaningful qualifications.

These observations describe these particular outputs. One result per workflow cannot establish that a skill is generally better. Humanizer's writers already knew their sections; the pstack writer used a separate context. [The experiment method](experiment.md) records these limits and the fixed assignment requirements.

Tables, diagram code, headings, captions, numerical values and citations were held constant. The paragraph examples below show the prose differences. They are excerpts, not replacements for the complete files.

## 1. Executive summary: interpreting the scores

### Raw

> The methodology comparison selects Kanban, with 102 of 120 weighted points, ahead of DevOps at 94. The existing open-source workflow scores 95 as a non-selectable baseline. These are judgements of project fit, rather than measured quality results. Kanban's strengths are managing review queues, accommodating voluntary work and introducing explicit policies with limited ceremony. It does not provide a complete engineering assurance method.

### Humanizer

> Kanban ranks first in the methodology comparison, scoring 102 of 120 weighted points against DevOps' 94. The existing open-source workflow scores 95 as a non-selectable baseline. These scores express judgements about project fit. They do not measure the quality of Actual's software. Kanban suits voluntary participation and helps manage review queues through explicit policies and limited ceremony. The method still needs engineering assurance practices.

### Pstack technical-writing + unslop

> The methodology comparison selects Kanban, which receives 102 of 120 weighted points, followed by DevOps with 94. The existing open-source workflow receives 95 as a non-selectable baseline. These scores express judgements about project fit. They do not measure software quality. Kanban can help manage review queues, accommodate voluntary work and establish explicit policies with little ceremony. It still needs engineering assurance practices.

Both edits separate the project-fit judgement from a measured quality result. The approved scores and the baseline remain unchanged.

## 2. Introduction: the personal reason

### Raw

> I chose Actual Budget because I was looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. Finding it gave me a reason to examine the product more closely through this assignment.

### Humanizer

> I chose Actual Budget because I wanted an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. After finding it, this assignment gave me the opportunity to look at the product in more depth.

### Pstack technical-writing + unslop

> I chose Actual Budget while looking for an open-source personal finance application that I could self-host on an old laptop at home to manage and track my finances. After finding it, I wanted to examine the product more closely through this assignment.

All versions retain the old laptop, self-hosting interest and financial-management purpose. The rewrites change the sentence rhythm without inventing product-use experience.

## 3. Methodology: quality as a requirement

### Raw

> Scores in Table 3 rate methodology support, not Actual's software quality. Every option retains existing CI/tests and must meet a mandatory QA gate: relevant security, reliability and interaction checks, assigned responsibility and evidence that can block release (Section 3). The scores are analyst judgements.

### Humanizer

> Table 3 scores the support each methodology provides. It does not rate Actual's software quality. All options retain existing CI/tests and must satisfy a mandatory QA gate: relevant security, reliability and interaction checks, assigned responsibility and evidence that can block release (Section 3). The scores express analyst judgement.

### Pstack technical-writing + unslop

> Table 3 scores each methodology's support for Actual's needs. The scores are analyst judgements and do not measure software quality. Each option retains existing CI and tests and must satisfy a mandatory QA gate. That gate requires relevant security, reliability and interaction checks, assigned responsibility and evidence that can block release, as Section 3 explains.

The three versions preserve the distinction between methodology support and product quality. Pstack gives the QA requirement its own sentences; Humanizer keeps more of the explanation together.

## 4. QA: the security advisory

### Raw

> A concrete security failure illustrates the limitation. GHSA-m2cq-xjgm-f668, published on 20 February 2026, carries the maintainers' critical rating of 9.2. Missing authentication allowed access to bank balances and transactions through SimpleFIN and Pluggy.ai endpoints; the advisory contrasts these with an integration that applied authentication middleware (Actual Budget, 2026c). This supports systematic cross-integration permission checks. It does not demonstrate that the patched release remains vulnerable.

### Humanizer

> The maintainers published GHSA-m2cq-xjgm-f668 on 20 February 2026 with a critical rating of 9.2. Missing authentication allowed access to bank balances and transactions through SimpleFIN and Pluggy.ai endpoints. The advisory identifies another integration that applied authentication middleware (Actual Budget, 2026c). The inconsistency supports checking permissions systematically across integrations. This historical failure does not establish that the patched release remains vulnerable.

### Pstack technical-writing + unslop

> GHSA-m2cq-xjgm-f668 illustrates the security limitation. Published on 20 February 2026, it carries the maintainers' critical rating of 9.2. Missing authentication allowed access to bank balances and transactions through SimpleFIN and Pluggy.ai endpoints. The advisory contrasts those endpoints with an integration that used authentication middleware (Actual Budget, 2026c). This failure supports systematic permission checks across integrations. It does not establish that the patched release remains vulnerable.

Humanizer opens with the maintainer publication and rating. Pstack opens with the advisory identifier and keeps a short explanation of its relevance. Both retain the access capability, historical context and patched-release qualification.

## 5. IV&V: what independence means

### Raw

> Independence adds protection against assumptions shared by developers. NASA distinguishes technical independence, where assessors exercise judgement separately from the developer; managerial independence, where a separate organisation controls assessment decisions; and financial independence, where the assessment budget is controlled independently of development (National Aeronautics and Space Administration [NASA], n.d.). A colleague's review can provide technical separation without satisfying all three dimensions.

### Humanizer

> Independent assessment helps reviewers question developers' shared assumptions. NASA identifies three dimensions: technical independence separates assessors' judgement from the developer's; managerial independence gives a separate organisation control over assessment decisions; financial independence places the assessment budget outside development's control (National Aeronautics and Space Administration [NASA], n.d.). A colleague's review can provide technical separation while sharing the same management and funding arrangements.

### Pstack technical-writing + unslop

> Independence helps challenge assumptions that developers share. NASA distinguishes three dimensions. Technical independence allows assessors to exercise judgement separately from the developer. Managerial independence places assessment decisions under a separate organisation. Financial independence requires independent control of the assessment budget (National Aeronautics and Space Administration [NASA], n.d.). A colleague's review may provide technical separation while leaving the other dimensions unmet.

Humanizer keeps the dimensions in a connected paragraph. Pstack gives each dimension a separate sentence. All three retain the limits of a colleague's review.

## Checks and edit records

The frozen raw file hashes still match their manifest. The reference lists are byte-for-byte identical across versions. All 43 references are cited. Mechanical comparisons found no changes to headings, captions, table rows, diagrams, inline code, parenthesised citation groups or the set of numerical values.

Prose review caught and corrected wording that could turn a proposal into a finding, imply observed compromise from a vulnerability, or strengthen a recommendation into a mandatory existing practice. These corrections preserve evidential limits rather than choosing a style winner.

- [Validation record](validation.md)
- [Citation review](process-notes/citation-review.md)
- [Humanizer introduction and summary notes](process-notes/humanizer-00-01.md)
- [Humanizer methodology notes](process-notes/humanizer-02.md)
- [Humanizer QA notes](process-notes/humanizer-03.md)
- [Humanizer IV&V notes](process-notes/humanizer-04.md)
- [Pstack notes and skill adaptations](process-notes/pstack.md)

Everything remains local. No commits, pushes, pull requests or PDF assembly were performed.
