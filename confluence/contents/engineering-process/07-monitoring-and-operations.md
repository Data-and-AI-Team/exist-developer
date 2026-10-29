# Monitoring and Operational Readiness

**Status:** Draft for review  
**Proposed owner:** Service owner / operations owner  
**Review cadence:** Quarterly and after significant incidents  
**Approval and effective date:** Pending owner review

## Operational readiness record

Before a service enters production, document its business purpose, accountable owner, dependency map, environments, support hours, escalation contacts, dashboards, runbooks, backup/recovery objectives, and known operational risks. Do not claim continuous support unless that coverage is actually staffed.

## Observability baseline

| Signal | Examples to select per service |
| --- | --- |
| Availability | Successful critical requests, health checks, synthetic journeys |
| Latency | User-facing response times and relevant percentiles |
| Errors | Failed requests/jobs, dependency failures, exception trends |
| Saturation | CPU/memory, queue depth, connection pools, storage/capacity |
| Business/data health | Processing delays, reconciliation failures, missing outputs |
| Security/audit | Privileged actions, authorization failures, relevant suspicious activity |

Define service-specific objectives, alert thresholds, baselines, and observation windows with the service owner. Use structured logs and correlation identifiers; minimize personal data and never log secrets. Restrict telemetry access and define retention.

## Alert lifecycle

1. Create an alert only when it has a clear actionable symptom or risk.
2. Associate it with severity, affected service, owner, support schedule, runbook, and escalation route.
3. Test delivery and acknowledgement using an approved exercise.
4. On receipt, acknowledge, assess impact, follow the runbook, and open an incident when criteria are met.
5. Record mitigation and resolution. Review recurring, noisy, or missed alerts and tune them without hiding genuine problems.

## Runbook minimum contents

- Observable symptoms and dashboard/log links.
- Safe diagnostic steps and necessary access.
- Dependency checks, common causes, and mitigation options.
- Stop conditions, recovery validation, and escalation contacts.
- Known risks of commands/actions and required approvals.

## Routine operations and evidence

Review service health, capacity, backup failures, certificate expiry, dependency health, and unresolved operational work on an owner-defined schedule. Retain readiness approval, dashboard/alert configuration references, alert delivery tests, operational review actions, and linked incidents.