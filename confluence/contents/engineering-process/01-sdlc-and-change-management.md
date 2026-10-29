# SDLC and Change Management

**Status:** Draft for review  
**Proposed owner:** Engineering leadership / delivery owner  
**Review cadence:** Quarterly  
**Approval and effective date:** Pending owner review

## Purpose and scope

Control software, configuration, integration, and infrastructure changes from request through operational handover. Apply a risk-based workflow to normal, routine, and emergency changes.

## Procedure

1. **Register the request.** Create a tracked work item with business objective, requester, accountable owner, scope, dependencies, acceptance criteria, and affected services/data.
2. **Assess risk.** Consider customer impact, security/privacy, availability, data migration, reversibility, and external dependencies. Record risk and required reviewers. Escalate high-impact or irreversible changes to engineering leadership and relevant security/operations owners.
3. **Design.** Document architecture and API/data changes, failure modes, access boundaries, observability, testing, deployment, and recovery. Use an architecture decision record for consequential decisions.
4. **Plan delivery.** Break work into reviewable units; identify test data, environment needs, dependency changes, rollout constraints, and acceptance owner.
5. **Implement and review.** Follow the pull-request and coding procedures. Link work items, design decisions, and test results to the PR.
6. **Validate.** Execute the agreed test strategy. Resolve release-blocking defects or obtain explicit, time-bound risk acceptance from the accountable owner.
7. **Authorize release.** Record the artifact/version, reviewer, acceptance evidence, deployment owner, rollout window, rollback triggers, and recovery approach.
8. **Deploy and observe.** Follow the release procedure; compare service signals to pre-change baselines and confirm business acceptance.
9. **Close and hand over.** Link deployment outcome, known limitations, updated runbooks, ownership, and support arrangements. Track residual work separately.

## Delivery gates

| Gate | Required output | Responsible approval |
| --- | --- | --- |
| Ready for implementation | Acceptance criteria, risk assessment, proportionate design | Technical lead / delivery owner |
| Ready to merge | Independent review and passing required checks | Reviewer |
| Ready to release | Test evidence, operational readiness, rollout/recovery plan | Release owner and acceptance owner |
| Ready to close | Verified outcome, updated documentation, residual risks assigned | Service/delivery owner |

## Emergency changes

Prioritize stabilization during an incident. Record incident linkage, reason normal lead time is unavailable, authorizer, minimal validation, and rollback approach. Do not silently bypass controls. Complete retrospective peer review, testing, and documentation after stabilization, using a deadline recorded by the incident commander.

## Records and completion

Retain linked work item, design/risk review, PR, pipeline/test report, release approval, and deployment outcome according to the agreed retention policy. The change is complete when acceptance criteria and operational handover are satisfied, or remaining risks have explicit ownership and acceptance.

## Related procedures

[Pull Requests and Code Review](02-pull-requests-and-code-review.md) · [Testing and Quality Assurance](05-testing-and-quality.md) · [Release, Deployment, and Recovery](06-release-and-recovery.md)