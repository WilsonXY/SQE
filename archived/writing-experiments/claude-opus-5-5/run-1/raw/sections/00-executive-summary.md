# Executive Summary

This report evaluates Actual Budget, a free, open-source, local-first personal finance application run by a small volunteer team. Its users need to trust the numbers it shows and the security of their financial data.

Actual has a defined workflow, with community-voted requests, pull requests, continuous integration, maintainer review and a monthly release train, but no deliberate methodology. Five candidates were scored against ten weighted criteria. Kanban scored highest (102 out of 120), ahead of DevOps (94) and Actual's current open-source model (95, used as a baseline). Kanban is therefore recommended, tailored with explicit exit policies, work-in-progress limits on review and mandatory quality gates. Its weakness is that it prescribes no technical quality practices.

The QA process focuses on three ISO/IEC 25010:2023 characteristics: Security, Reliability and Interaction capability. Public evidence shows gaps in proactive security verification, coverage measurement and accessibility testing. The proposed QA plan adopts OWASP ASVS 5.0.0, WCAG 2.2 and OpenSSF tools and embeds a Definition of Done in each Kanban stage.

IV&V adds risk-tiered independent review inside the team and external checks through coordinated disclosure and an optional funded audit. Internal review gives technical independence only, and volunteer time and donation funding remain the main limits.
