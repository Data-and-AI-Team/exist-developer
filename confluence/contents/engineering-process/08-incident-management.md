# Incident Management and Learning

**Status:** Draft for review  
**Proposed owner:** Operations owner / engineering leadership  
**Review cadence:** Quarterly and after major incidents  
**Approval and effective date:** Pending owner review

## Purpose

Coordinate service restoration, protect data, communicate impact, and learn from operational and security incidents. Service-specific support coverage and response targets must be defined and staffed before adoption.

## Initial severity guide

| Severity | Indicative impact | Coordination |
| --- | --- | --- |
| SEV1 — Critical | Broad critical-service outage, credible major compromise, or material data loss | Activate incident command and relevant security/business escalation |
| SEV2 — High | Significant degradation or partial outage with serious user impact | Named incident lead and affected service owners |
| SEV3 — Moderate | Limited impact with a viable workaround | Service-owner response; escalate if impact grows |
| SEV4 — Low | Minor issue without material immediate impact | Track through normal support/change workflow |

Reassess severity as evidence changes. Agree acknowledgement, escalation, and update targets per service; this draft does not establish an unsupported SLA.

## Response procedure

1. **Detect and record.** Open a restricted incident record where appropriate. Capture discovery time, reporter, symptoms, affected services, and initial impact.
2. **Triage and mobilize.** Assign severity, incident commander, technical lead, communications owner, and scribe. Confirm an incident channel and escalation contacts.
3. **Contain.** Prioritize safety and limit impact. Restrict compromised access or isolate affected components when authorized. Preserve relevant evidence; do not destroy logs or perform unnecessary destructive actions.
4. **Investigate and mitigate.** Maintain a timestamped timeline, hypotheses, diagnostics, and decisions. Use reviewed runbooks and link emergency changes. Separate facts from assumptions.
5. **Communicate.** State confirmed impact, mitigation status, workarounds, and next-update time. Security/privacy/legal owners decide external notification requirements; do not speculate or disclose sensitive evidence broadly.
6. **Recover and validate.** Restore critical workflows, verify data integrity and security posture, and observe agreed stability signals. Record who authorized recovery and closure.
7. **Learn and improve.** Conduct a blameless review for significant or recurring incidents. Identify contributing conditions, detection/response gaps, and corrective actions with owners and due dates.

## Incident record template

- Identifier, title, severity, status, affected service, commander.
- Detection/start/mitigation/recovery timestamps and impact summary.
- Timeline, communications, diagnostics, and evidence links.
- Changes made, approvals, recovery checks, and residual risks.
- Contributing factors and corrective actions with owner/status/due date.

## Exercises and follow-up

Exercise escalation and recovery using an approved tabletop or technical drill. Clearly label simulated incidents. Track corrective actions to verified completion, review overdue work, and update alerts, tests, and runbooks. Restrict sensitive incident details and apply the approved retention policy.