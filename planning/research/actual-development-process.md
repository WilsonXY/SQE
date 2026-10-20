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

### QA practices as-is (for Section 3), checked at commit `27290a8`

**Automated checks on every PR** (`.github/workflows/`):
- `check.yml` ("Test"), on push, PR and merge queue:
  - `yarn constraints`, tsconfig reference check, `yarn lint` (oxfmt and oxlint), `yarn knip` (unused code/dependencies), `yarn typecheck`, `yarn test` (Vitest across all packages via Lage);
  - a database **migration check** (`check-migrations.ts`).
- `build.yml`: builds the API, CRDT, web, mobile, CLI and sync-server, and records build stats.
- `e2e-test.yml`, on PR and merge queue: Playwright **functional E2E** (sharded), **desktop-app E2E**, and **visual regression** (sharded, merged HTML report).
- `codeql.yml`: **CodeQL security analysis** on push to master, on PRs, and weekly (Saturday cron).
- `dependency-review.yml` on PRs. `crdt-version-check.yml` ensures the CRDT package version is bumped on PRs. `size-compare.yml` compares bundle sizes.

**Pre-commit hook:** `.husky/pre-commit` → `nano-staged`, which runs a formatter (oxfmt) and linter (oxlint --fix --type-aware) on staged files and validates package imports and tsconfig references.

**Testing guide** (S09, `contributing/testing.md`):
- Vitest unit tests, Playwright E2E, VRT; the monorepo runner is Lage.
- Best practice is "Minimize mocking".
- The PR **testing checklist**: all tests pass; "New functionality has appropriate test coverage"; E2E passes if the UI changed.

**Review standards:**
- `CODE_REVIEW_GUIDELINES.md` (S01): no new `@ts-strict-ignore`, no lint suppressions, avoid `any`, i18n for all strings, minimise mocks.
- PR template checklist (release notes, no regressions, self-review).
- AI usage policy (S50): AI-written code must still pass typecheck, lint and tests, follow the code style, and translate strings. AI use must be disclosed. Interactions with maintainers must be human.

**Release QA** (S03): at least 2 maintainer approvals plus a **manual smoke test** of the Docker server and desktop app.

**Other QA-relevant practices:**
- Feature flags (S07).
- ADRs (S06).
- Triage labels (S05).
- The design and accessibility target is WCAG 2.1 AA (`PRODUCT.md`, S01).
- Strict TypeScript (S52: "All code is written in TypeScript with strict type checking").
- SQLite with schema migrations (S52).

**Security and privacy features** (S51, `getting-started/sync.md`):
- Optional **end-to-end encryption** of budget data ("so that hosted services can't read your budget data").
- Local data is unencrypted (full-disk encryption is recommended).
- Bank-sync tokens are stored on the server outside E2EE.
- Encryption can't be turned off once on, and a lost password means unrecoverable data.

**Apparent gaps** (found by file search at commit `27290a8`; worded carefully as "no evidence found"):
- **No test coverage measurement or reporting.** There is no coverage setting in the root `vitest.config.ts`. `packages/sync-server/vitest.config.ts` has `coverage: { enabled: false }`. No coverage scripts or Codecov config. This sits oddly with the checklist item "appropriate test coverage", which has no measure behind it.
- **No automated accessibility testing.** No axe/Lighthouse dependency or config in the desktop-client, loot-core, sync-server or desktop-electron `package.json` files, despite the WCAG 2.1 AA target.
- ~~No `SECURITY.md`~~: **WRONG, corrected 2026-10-20.** A security policy **does exist**. It is an organisation-level file in `actualbudget/.github/SECURITY.md` [S62], which GitHub applies to all repos in the org, so a search of the `actual` repo alone missed it. The author confirmed it in a browser (GitHub Security tab screenshot). See *Security process* below.
- **No automated performance testing in CI.** Only `packages/loot-core/src/server/bench.ts` exists, and it isn't wired into workflows.
- **No written QA plan / SQAP.** Quality practices are spread across the docs, templates and CI.

### Security process (verified 2026-10-20)

**Security policy** [S62] (`actualbudget/.github/SECURITY.md`, raw file fetched, HTTP 200):
- Security support covers "the latest stable release of Actual and Actual Server only".
- Reports of vulnerabilities in unreleased builds are welcome.
- Reports go through **GitHub private vulnerability reporting** (`/security/advisories/new`).
- "**Do not** open a pull request with a fix or otherwise advertise the vulnerability publicly until we have had a chance to coordinate disclosure", i.e. coordinated disclosure.
- **Weaknesses:** no response-time commitment and no severity/triage process described. The policy's link to the current stable version (`https://actualbudget.github.io/docs/Release-Notes`) is **broken**: it redirects to `actualbudget.org/docs/Release-Notes`, which returns **HTTP 404** (checked 2026-10-20).

**Published security advisories.** Two sources:
- The author's screenshot of the GitHub Security tab (2026-10-20). Page 1 shows 10 advisories and there is more than one page. Severities are as published by maintainers (MatissJanis, jfdoming).
- OSV.dev API query of Actual's npm packages [S63] (2026-10-20):

| Published | ID | Severity (OSV) | Package | Summary |
|---|---|---|---|---|
| 2025-10-20 | GHSA-xvp7-8vm8-xfxx | Moderate | sync-server | GoCardless service logs sensitive data incl. bearer tokens |
| 2026-02-24 | GHSA-m2cq-xjgm-f668 | **Critical** | sync-server | Missing authentication for SimpleFIN and Pluggy AI bank-sync endpoints |
| 2026-02-27 | GHSA-qmjj-p7m9-wjrv | Moderate | sync-server | Missing authorization in sync endpoints allows cross-user budget access |
| 2026-03-10 | GHSA-27vg-33gh-4hwg | Moderate | sync-server | Authenticated path traversal |
| 2026-04-23 | GHSA-prp4-2f49-fcgp | High | sync-server | Privilege escalation via `change-password` on OpenID-migrated servers |
| 2026-06-22 | GHSA-3f62-qv96-4p78 | Moderate | sync-server | Missing authorization on `GET /secret/:name` (non-admin users can enumerate bank-sync secrets) |
| 2026-06-22 | GHSA-cq9c-6w48-qmfg | High | sync-server | Disabled OpenID users keep access through existing session tokens |
| 2026-06-22 | GHSA-xqjm-27pc-rvwm | Moderate | web | CSV formula injection in transaction export |
| 2026-06-22 | GHSA-7gh7-258j-4mpq | Moderate | cli | CSV formula injection in `--format csv` output |
| 2026-10-07 | GHSA-m62c-5q34-f3cf | High (OSV) / **Low** (repo, per screenshot) | sync-server | CORS proxy allowlist prefix bypass leaks private repos via the server's GitHub token |

The screenshot also shows advisories **not** in the OSV npm list (probably not tied to an npm package): "Electron Run As Node" (GHSA-7rvm-xjpp-63r9, Moderate), "Shared users can perform owner-only file management actions" (GHSA-23vm-ffgg-qvjr, High), "OpenID `client_secret` disclosure via broken authorization guard" (GHSA-49v6-pqjq-xw55, High), and "Path traversal vulnerability in actual-server" (GHSA-4wf8-vhhr-4gpv, Moderate).

**Pattern (analysis, to be argued in Section 3/4):**
- Most advisories are **access-control defects** (missing authentication or authorization, privilege escalation, session handling) in the **sync server**.
- Many relate to **multi-user/OpenID support**, a 2025 feature [S11]. New features led to new security defects that automated checks (CodeQL, dependency review) did not prevent before release.
- *To verify:* who reported them (the credits on each advisory page). That matters for Section 4: external reporters would be a form of *independent* verification.

**Implication for QA:** security QA today is mostly **reactive**: a good disclosure and fix process, but no evidence of proactive security testing such as authorization test suites, threat modelling or security review for features like multi-user.

### Product facts (for the Introduction)
- "a local-first personal finance tool. It is 100% free and open-source" with sync between devices. `README.md`
- Built around **envelope budgeting**. Users include privacy-minded budgeters, self-hosters and families. Success means "users trusting the numbers". `PRODUCT.md`
- It can be deployed four ways: PikaPods, Fly.io, self-hosted Docker, or local-only desktop apps (Windows/Mac/Linux). `README.md`
- Main packages: loot-core (core logic), desktop-client (UI), desktop-electron (desktop app) and sync-server. `README.md`, `contributing/releasing.md`
- The accessibility target is WCAG 2.1 AA. `PRODUCT.md`
