# AI Use-Case Intake and Risk Review

**Status:** Approved
**Owner:** Initiative sponsor / use-case owner
**Review cadence:** Quarterly and when use or data materially changes  
**Approval and effective date:** November 15, 2025

## Intake record

Record use-case name, owner, problem, intended users, expected benefit, non-AI alternative, proposed tool/model/provider, environments, data sources/classification, retrieval sources, tool permissions, expected cost, and operational owner. Identify prohibited uses, foreseeable misuse, affected people, human oversight, and success/failure criteria.

## Risk assessment

| Proposed tier | Indicative characteristics | Review expectation |
| --- | --- | --- |
| Low | Non-sensitive inputs, advisory output, no external action | Owner approval and documented validation |
| Moderate | Internal/confidential data, workflow integration, bounded reversible actions | Technical and data-owner review; security/privacy review as applicable |
| High | Sensitive personal/client data, high-impact decisions, privileged actions, externally consequential output | Sponsor and relevant security/privacy/legal approval; enhanced evaluation and human oversight |

Use the highest applicable tier and document the rationale. These tiers are internal review guidance, not a legal classification. Escalate unclear cases rather than self-approving.

## Gate procedure

1. Confirm a real need and whether a simpler deterministic approach is preferable.
2. Map input, output, logging, retrieval, model-provider, and downstream action data flows.
3. Review data rights, purpose, confidentiality, residency, retention, provider training/use terms, and supplier dependencies.
4. Define least-privilege access, human approval points, failure handling, rollback/disable mechanisms, and evaluation scope.
5. Approve an isolated prototype using synthetic or explicitly authorized data.
6. Review prototype results and unresolved risks before approving a bounded pilot.
7. Authorize production only after the evaluation and operational readiness gates are satisfied.

## Stop conditions

Do not proceed without an accountable owner, authorized data access, acceptable supplier terms, defined oversight, or a feasible way to detect and stop unsafe behavior. Route unacceptable or unmitigated risks to the sponsor; document rejection or deferral.

## Decision and exception record

Keep decision, reviewer identities, date, scope, conditions, residual risks, evidence links, and next review trigger. An exception requires a compensating control, accountable approver, and expiry. Re-review on provider/model changes, new data, expanded audience, increased permissions, or changed intended use.