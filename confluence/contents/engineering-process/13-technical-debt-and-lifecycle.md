# Technical Debt and Service Lifecycle Management

**Status:** Approved
**Owner:** Engineering leadership / service owners
**Review cadence:** Quarterly and at service lifecycle transitions  
**Approval and effective date:** November 15, 2025

## Purpose

Make maintainability risks visible, prioritize upgrades, and retire services without leaving orphaned data, access, or dependencies.

## Debt register

Record identifier, affected service/component, description, evidence, business/technical impact, source, owner, estimated effort, dependencies, proposed action, priority, and next review date. Link temporary fixes, accepted design compromises, recurring incidents, slow build/test feedback, and end-of-support risks.

## Prioritization procedure

1. Assess security/supportability risk, incident frequency, delivery friction, cost, user impact, and urgency.
2. Identify a proportionate fix, modernization, replacement, or retirement option. State the cost of deferring and assumptions behind estimates.
3. Review the backlog with product/delivery owners at the agreed planning cadence. Allocate actual capacity and record decisions rather than maintaining an unowned wish list.
4. Implement through normal design, PR, testing, and release procedures. Verify the expected improvement against an identified baseline.
5. Close the debt record only when acceptance evidence exists; record residual limitations separately.

## Upgrade and support planning

Maintain runtime, framework, platform, and supplier support dates in the service inventory. Plan upgrades before support expiry, including compatibility testing, data migration, consumer coordination, and rollback. Escalate unsupported production components with an accountable risk decision and replacement timeline.

## Service lifecycle gates

| Stage | Required decision |
| --- | --- |
| Introduction | Purpose, sponsor, owner, architecture, expected operating cost |
| Production readiness | Acceptance, support, monitoring, recovery, and access ownership |
| Maintenance | Health, debt, supportability, value, and capacity review |
| Deprecation | Consumer inventory, replacement, notice, migration criteria |
| Retirement | Approved shutdown, data disposition, access/resource removal, closure checks |

## Retirement procedure

Confirm active consumers and obtain business/data-owner authorization. Notify affected users, complete migrations, and define retention/export/deletion requirements. Disable traffic and jobs, revoke credentials and integrations, and remove unused infrastructure, DNS, alerts, and billing resources. Verify dependency removal and data disposition, then archive required records and update inventory. Retain a contact for any mandated archived-data access.