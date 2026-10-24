# Does a quality-focused assignment still justify Kanban?

**Decision update:** The author approved retaining Kanban with mandatory QA gates and the revised scores. This note records the discussion that led to the decision; the complete report versions are linked from [the reading guide](README.md).

This is a discussion note for Assignment 1, written before the methodology is settled. It is not part of the report's word count. No Humanizer pass has been applied.

## Answer to the concern

**DevOps is the closest alternative worth considering. XP offers more explicit engineering practices, but neither has been shown to give Actual better quality with fewer overall trade-offs.** That conclusion is a judgement about this project's constraints, not an experimentally established ranking.

The original matrix's **3/5 was meant to rate Kanban's support for defect prevention, not the quality of Actual Budget itself**. It was too easy to read it as saying that a lower-quality process had been selected for convenience. The report must explain the distinction and make its quality requirements non-negotiable.

Kanban organises work, limits overload and makes policies explicit. Its own guide describes applying it to an existing way of working. It does not supply a complete set of software engineering practices. Therefore, adopting a board alone would be an inadequate recommendation for this assignment. [Kanban University's official guide](https://kanban.university/kanban-guide/)

## What the alternatives add

| Approach | What it can add to Actual's quality work | Main trade-off in this project |
|---|---|---|
| Kanban | Visible review queues, limits on unfinished work, explicit conditions for accepting and releasing changes | The report must separately specify the technical checks and their owners; flow management alone cannot prevent an authorisation defect |
| XP | Test-first development, frequent integration, incremental design and close technical collaboration | Some practices need contributors to coordinate their time; remote pairing and adaptation are possible, so co-location is not an absolute barrier |
| DevOps | Continuous verification, shared responsibility for tests, and feedback between development and operation | Actual already has CI; the proposal must identify useful additions rather than count existing automation as a new benefit. Maintaining the checks and obtaining useful operational feedback still need people |

XP's creators explicitly describe adapting its practices, including trying remote pairing. The first matrix was too harsh on its distributed-work fit. [Beck and Andres's primary-practices appendix](https://www.informit.com/articles/article.aspx?p=390816&seqNum=3)

DORA's guidance is more specific than simply installing more tools: it recommends continuous automated and manual testing, exploratory and usability work, and ongoing improvement of the test suites. This gives a DevOps proposal a credible quality argument, but it does not demonstrate that Actual's security, financial integrity and accessibility would automatically be assured. [DORA's test-automation guidance](https://dora.dev/capabilities/test-automation/)

DevSecOps also deserves consideration if security is to organise the whole approach. NIST documents security integration in DevSecOps pipelines. Its cited guidance addresses software-supply-chain security, however; it does not establish that this approach would cover Actual's application permissions, calculations and accessible interactions with less volunteer effort. It needs further comparison before being added to the agreed shortlist. [NIST SP 800-204D](https://doi.org/10.6028/NIST.SP.800-204D)

## How the evaluation should change

Every candidate should retain the same baseline of Actual's existing tests, CI and review practices. The first matrix unfairly charged DevOps too much for establishing automation that is already present. It also gave XP and DevOps a quality score of 5 without establishing coverage of the three selected attributes.

The revised proposal first requires every candidate's implementation to provide:

- **Security:** relevant permission and denied-access tests, review and vulnerability handling.
- **Reliability:** relevant calculation, synchronisation, migration and recovery evidence.
- **Interaction capability:** accessible interactions and acceptance checks for important user tasks.

An implementation that cannot identify who performs these checks and what prevents an unsafe release should fail the assessment before weighted preferences are considered. A high score for low overhead must not compensate for missing essential assurance.

After that gate, the matrix can compare how each method supports the work under Actual's volunteer constraints. Higher quality weights can be tested transparently, but should be chosen for their meaning rather than adjusted until a preferred method wins.

## Recommended direction

**Retain Kanban as a provisional choice only if the report's main process intervention is managing review capacity while making the QA and IV&V controls enforceable.** This is compatible with an SQE assignment because the assurance argument remains explicit and central. It is not a claim that Kanban has the strongest built-in engineering practices.

If the intended intervention is instead to organise development around continuous engineering assurance and operational feedback, **rework the selection around DevOps** and state its additions to the existing pipeline. XP remains a credible alternative where the team can sustain its collaborative practices. The available evidence does not establish that either alternative dominates Kanban on both quality support and adoption cost.

The detailed proposed scores, assumptions and sensitivity checks are in [the reassessment](../../planning/research/methodology-quality-reassessment.md). Those scores remain unapproved. Section 2.4 and the final method-specific wording are waiting for this decision.
