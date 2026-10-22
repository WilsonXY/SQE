# Executive Summary

This report evaluates Actual Budget, a free, open-source, local-first personal finance application run by a small volunteer team. Its users need correct figures and secure financial data.

Actual has a defined workflow, with community-voted requests, pull requests, continuous integration, maintainer review and a monthly release train, but no deliberate methodology. Scored against ten weighted criteria, Kanban came first among five candidates with 102 out of 120. DevOps scored 94, and Actual's current open-source model, used as a non-selectable baseline, scored 95. The report recommends Kanban with explicit exit policies, work-in-progress limits on review and mandatory quality gates. Kanban itself prescribes no technical quality practices, so those gates carry the quality work.

The QA process focuses on three ISO/IEC 25010:2023 characteristics: Security, Reliability and Interaction capability. Public evidence shows gaps in proactive security verification, coverage measurement and accessibility testing. The proposed QA plan adopts OWASP ASVS 5.0.0, WCAG 2.2 and OpenSSF tools and embeds a Definition of Done in each Kanban stage.

For IV&V, the report adds risk-tiered independent review inside the team, plus external checks through coordinated disclosure and an optional funded audit. Internal review gives technical independence only. Volunteer time and donation funding limit how far independence can go.
