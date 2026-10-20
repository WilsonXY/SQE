# Research: How Actual Budget Is Developed Today (As-Is)

Purpose: give the Methodology section (2.x) an evidence base, answering whether Actual uses a formal methodology.

Source snapshot: `actualbudget/actual`, `master` branch at commit `27290a8` (2026-10-19). Unless a URL is given, paths are inside that repo. The project's docs site (actualbudget.org/docs) is built from `packages/docs/`, so these files are the same content as the website.

## Verdict (verified)

Actual Budget does **not** declare or follow any named methodology (no Scrum, no sprints, no Kanban board). It **does**, however, have a clear, documented and heavily automated *workflow*. The best description is an **emergent, volunteer-driven open-source process**, which in practice combines:

- continuous, pull-based flow of contributions (Kanban/Lean-like);
- strong engineering practices: CI, automated tests, code review (XP-like);
- a **fixed monthly release train**;
- community-driven prioritisation through voting.

## Evidence

### People and roles
- There are 8 "Main Contributors" (core maintainers) and 15 alumni. `packages/docs/docs/contributing/index.md`
- "We do not assign specific roles or responsibilities but instead allow people to choose what they want to work on." `packages/docs/docs/contributing/leadership/new-core-contributors-guide.md`
- "We do not assign issues to specific people." "All issues are open to be worked on by anyone." `contributing/index.md`
- "The mental health of the maintainers will be prioritized above all else." `contributing/index.md`
- `CODEOWNERS` maps 6 code areas to individual maintainers, who are notified of PRs in those areas.
- The original author is James Long (the copyright in `LICENSE.txt`, which is MIT licence text).

### History (verified)
- "In early 2022 James, the creator of Actual Budget, decided to close-down the commercial product and open source it." Source: [S10] Aboltins, M. J. (2025, January 2). *Roadmap for 2025*. Actual Budget. `packages/docs/blog/2025-01-02-roadmap-for-2025.md` (https://actualbudget.org/blog/roadmap-for-2025/)
- From the same post: after an initial burst of activity, "The PRs were stuck waiting for a review for months with nobody around to review them." A small volunteer group then got access to the core repositories, worked through about 50 open PRs, and built the core maintainer team. Members joined and left over time. The post also reports a Discord community of over 7,000 and "upwards of a million docker container clones per month". **This is useful evidence for 2.1 and 2.2, because review capacity is the bottleneck.**
- James Long's own announcement, "Actual is going open-source" (https://jlongster.com/actual-open-source), says Actual had been in development for over 4 years as a paid product, the hosted service would end, and users should self-host the sync server. **Exact date not verifiable:** the original URL now returns 404 (checked by the author in a browser, 2026-10-20). The author found an archive at https://archive.jlongster.com/#posts, but it couldn't be reached from the research environment, and neither could the Wayback Machine.
  - **Decision:** the report says "early 2022" and cites Actual's own blog (above), which is enough for a brief history.
  - Secondary corroboration [S15]: *Actual(ly) opening up with James Long*, The Changelog #495 (published July 1, 2022; recorded June 15, 2022). It describes Actual as built "as a business for over 4 years before" being opened up. Verified from the episode page and transcript. The transcript gives no exact open-source date.
  - The archive at archive.jlongster.com only goes up to May 2020, so it doesn't contain the 2022 post.

### Requirements and prioritisation
- Feature requests use a **voting system**: issues typed "Feature" are auto-labelled `needs votes`, auto-commented and auto-closed. The backlog is the list of `needs votes` issues sorted by 👍. `.github/workflows/issues-close-feature-requests.yml`
- Small changes can go straight to a PR. Larger features should be discussed in an issue first. `contributing/index.md`
- The feature-request template asks for: the problem ("pitch"), an ideal solution, and "teaching and learning" (discoverability and docs). `.github/ISSUE_TEMPLATE/feature-request.yml`
- There are yearly roadmap / "wish list" blog posts, e.g. `packages/docs/blog/2025-01-02-roadmap-for-2025.md` and `2025-12-20-roadmap-for-2026.md`. The 2025 roadmap was "all but one" achieved (plugins was the miss).
- Triage uses `needs triage`, `needs info` (auto-closes after 7 days), and contextual and call-to-action labels. Tech support goes to Discord. `contributing/leadership/triaging-issues.md`
- Product vision and design principles are in `PRODUCT.md` and `DESIGN.md`. Non-obvious decisions are recorded as Architecture Decision Records. `contributing/leadership/architecture-decision-records.md`

### Development and review
- Contributor workflow: read code, make small focused changes, then `yarn typecheck`, `yarn lint:fix` and the relevant tests before opening a PR. `contributing/index.md`
- Every PR needs a release-note file in `upcoming-release-notes/` (categories: Features, Enhancements, Bugfix, Maintenance). `contributing/index.md`, `.github/PULL_REQUEST_TEMPLATE.md`
- The PR template has Description, Related issue(s), Testing, and a Checklist: release notes, no regressions, a self-review, and AI-use disclosure.
- Review rules: non-controversial changes may be approved and merged straight away. Controversial ones wait "a few more days for others to review". Disagreements escalate from the two people, to the contributor team, to a public vote. `new-core-contributors-guide.md`
- `CODE_REVIEW_GUIDELINES.md` gives rules for (AI) reviewers: no new `@ts-strict-ignore`, no lint suppressions, avoid `any`, all strings i18n, minimise mocks. A `.coderabbit.yaml` AI-review config also exists.
- Stale PR automation: assigned PRs are marked stale after 14 days and closed 3 days later. WIP PRs are marked after 7 days and closed after 14. `.github/workflows/stale.yml`
- There is an AI usage policy, and from November 2025 a stance against "AI slop" PRs. `packages/docs/blog/2025-11-15-fighting-ai-slop.md`
- **Feature flags / experimental features** let large features ship in small increments to real users. Flags with no active development for over 3 months are removed. `contributing/project-details/feature-flags.md`

### Testing and CI (GitHub Actions, `.github/workflows/`)
- Build, check (lint and typecheck), unit tests (Vitest), E2E tests (Playwright), Visual Regression Tests (VRT), Electron builds, CodeQL security scanning, dependency review, bundle size comparison, CRDT version check, docs spelling, and migration warnings. `contributing/testing.md` plus the workflow file names.

### Release
- The monthly release branch is cut automatically at 17:00 UTC on the 25th of every month. `.github/workflows/cut-release-branch.yml`, `contributing/releasing.md`
- Versioning is `YY.M.patch`, e.g. 26.10.0, with patch releases for critical fixes. Monthly release posts exist continuously from 2022 to `2026-10-01-release-26-10-0.md`.
- A release needs **at least 2 other maintainers to approve**, then a manual smoke test (Docker server and desktop app), then publishing to NPM, Docker Hub, the Microsoft Store, Flathub and GitHub Releases. `contributing/releasing.md`
- Nightly and edge builds also exist (`docker-nightly.yml`, `publish-nightly-electron.yml`) and so do PR preview builds (`contributing/preview-builds.md`).

### Funding and sustainability
- Donations run through Open Collective at about USD 3,000–3,500 a month. A USD 2,000/month stipend pool pays core maintainers for **reviews and triage**, using points weighted by lines of code reviewed, counted automatically by `.github/workflows/count-points.yml`. `contributing/leadership/paying-contributors.md`
- Hosting partners such as PikaPods share revenue ("over 8000 Pikapods users"). `blog/2025-12-20-roadmap-for-2026.md`

### Product facts (for the Introduction)
- "a local-first personal finance tool. It is 100% free and open-source" with sync between devices. `README.md`
- Built around **envelope budgeting**. Users include privacy-minded budgeters, self-hosters and families. Success means "users trusting the numbers". `PRODUCT.md`
- It can be deployed four ways: PikaPods, Fly.io, self-hosted Docker, or local-only desktop apps (Windows/Mac/Linux). `README.md`
- Main packages: loot-core (core logic), desktop-client (UI), desktop-electron (desktop app) and sync-server. `README.md`, `contributing/releasing.md`
- The accessibility target is WCAG 2.1 AA. `PRODUCT.md`
