# Engineering Process

**Status:** Draft for review  
**Proposed owner:** Engineering leadership  
**Review cadence:** Quarterly and after material process changes  
**Approval and effective date:** Pending owner review

## Purpose

Provide a single entry point for engineering procedures governing how changes are designed, implemented, reviewed, tested, deployed, monitored, and supported. This space is intended for engineers, technical leads, QA, operations, security reviewers, and delivery owners.

## Engineering operating procedure documentation — table of contents

1. [SDLC and Change Management](01-sdlc-and-change-management.md) — requirements, risk assessment, design, delivery gates, and change records.
2. [Pull Requests and Code Review](02-pull-requests-and-code-review.md) — branching, pull requests, independent review, automated checks, and merge controls.
3. [Coding Standards and Secure Development](03-coding-standards.md) — maintainability, language conventions, security, dependencies, and documentation.
4. [Infrastructure and Configuration Management](04-infrastructure-and-configuration.md) — infrastructure as code, environment separation, secrets, access, and drift.
5. [Testing and Quality Assurance](05-testing-and-quality.md) — test strategy, automated/manual testing, defect handling, and acceptance evidence.
6. [Release, Deployment, and Recovery](06-release-and-recovery.md) — release authorization, deployment checks, rollback, and restore validation.
7. [Monitoring and Operational Readiness](07-monitoring-and-operations.md) — service ownership, health signals, alert routing, and runbooks.
8. [Incident Management and Learning](08-incident-management.md) — detection, severity, response, communication, recovery, and follow-up.
9. [Architecture and Technical Design Reviews](09-architecture-and-design.md) — proposals, architecture decisions, and technical sign-off.
10. [Vulnerability and Patch Management](10-vulnerability-and-patching.md) — triage, remediation, patch validation, and exceptions.
11. [Identity and Access Management](11-identity-and-access.md) — joiners/movers/leavers, privileged access, and access reviews.
12. [API and Integration Standards](12-api-and-integrations.md) — contracts, compatibility, secure integrations, and validation.
13. [Technical Debt and Service Lifecycle Management](13-technical-debt-and-lifecycle.md) — prioritization, supportability, upgrades, and retirement.

## Roles

| Role | Responsibility |
| --- | --- |
| Engineering leadership | Approve process, assign owners, resolve control exceptions |
| Technical lead/service owner | Own design, implementation quality, service risks, and runbooks |
| Engineer/change author | Implement, test, document, and prepare evidence for the change |
| Independent reviewer | Assess correctness, security, maintainability, and test coverage |
| QA/test owner | Coordinate test scope, defect reporting, and acceptance evidence |
| Operations/release owner | Validate readiness, deployment, monitoring, and recovery |
| Security/privacy reviewer | Assess relevant data, access, security, and privacy risks |
| Incident commander | Coordinate active incident response and recovery decisions |

One person may hold multiple roles where staffing requires it; identify compensating review when independent approval is not available. Record actual assignments in each service's responsibility directory.

## Using and maintaining this space

- Follow the procedures applicable to the change's risk and service context.
- Store implementation evidence in linked tickets, repositories, pipelines, and operational records.
- Each service must identify its repository, owner, environments, support coverage, dashboards, runbooks, and recovery objectives.
- Request exceptions through a tracked record with justification, risk, compensating controls, accountable approval, and expiry. Reassess before renewal.
- Review pages after incidents or significant tooling changes. Preserve Confluence page history and link material process decisions.

## Documentation evidence

This index intentionally exposes all required engineering procedure categories for screenshot evidence. Before submitting it, confirm the linked pages are approved and reflect actual practice. Keep lifecycle status visible; draft documentation must not be presented as an adopted operating procedure.