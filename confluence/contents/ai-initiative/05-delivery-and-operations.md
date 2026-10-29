# AI Delivery, Monitoring, and Incident Response

**Status:** Draft for review  
**Proposed owner:** AI technical owner / operations owner  
**Review cadence:** Quarterly and after material incidents  
**Approval and effective date:** Pending owner review

## Release baseline

Maintain a versioned release record for application code, model/provider identifier, prompts, parameters, retrieval sources/index configuration, embedding model, tool permissions, guardrails, and evaluation report. Record provider-version limitations if immutable model pinning is unavailable.

## Readiness and rollout

1. Confirm use-case/data authorization, evaluation acceptance, supplier settings, access controls, and operational owner.
2. Define usage limits, cost budget, rate limits, timeout/retry behavior, human review points, and prohibited actions.
3. Test fallback, rollback, credential revocation, and a kill switch that stops model/tool actions without depending solely on the model obeying a prompt.
4. Deploy to a bounded audience or staged traffic allocation where supported. Provide user-facing limitations and escalation paths.
5. Observe quality, safety, permissions, performance, and cost before expanding access. Record the go/no-go decision.

## Monitoring

| Area | Signals and follow-up |
| --- | --- |
| Quality | Task failures, unsupported answers, reviewer rejection, user feedback |
| Security/privacy | Injection attempts, denied access, suspicious tool actions, suspected leakage |
| Retrieval | Permission-filter failures, stale sources, indexing errors, citation validity |
| Reliability | Provider errors, timeouts, rate limiting, fallback activation |
| Performance/cost | Latency, token/request volume, per-use-case cost, budget alerts |
| Change/drift | Provider changes, input-distribution shifts, regression in evaluation samples |

Define owner-approved thresholds and alert routes per use case. Use minimized/redacted telemetry and restricted access. Do not collect full prompts and responses indiscriminately.

## AI incident procedure

1. Open an incident for suspected leakage, unauthorized actions, unsafe outputs with material impact, uncontrolled cost, or significant quality degradation.
2. Stop or restrict the affected feature, revoke tool permissions/credentials where appropriate, and preserve relevant version and audit records.
3. Assess affected users, data, downstream actions, and whether outputs were relied upon. Escalate security/privacy/legal concerns through the engineering incident process.
4. Correct affected outputs or workflows where authorized; communicate confirmed impact and mitigations without spreading sensitive content.
5. Reproduce the issue safely, implement controls, and add regression evaluations. Obtain explicit approval before re-enabling the feature.
6. Complete a blameless review and track corrective actions.

## Change and retirement

Re-evaluate material changes before release, including provider-side updates that cannot be pinned. At retirement, remove integrations and access, revoke credentials, archive required records, and delete retained data/indexes according to approved obligations. Verify downstream copies and provider deletion capabilities rather than assuming removal is automatic.

## Related procedures

[Release, Deployment, and Recovery](../engineering-process/06-release-and-recovery.md) · [Incident Management and Learning](../engineering-process/08-incident-management.md)