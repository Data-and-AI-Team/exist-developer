# Architecture and Technical Design Reviews

**Status:** Approved
**Owner:** Architecture lead / technical leads
**Review cadence:** Quarterly and after significant architecture changes  
**Approval and effective date:** November 15, 2025

## Purpose and scope

Make consequential technical decisions explicit, reviewable, and traceable before implementation. Apply this procedure to new services, major integrations, trust-boundary changes, significant data-model changes, and changes with material availability or cost impact. Routine changes may reference an existing approved design.

## Design proposal

| Section | Required information |
| --- | --- |
| Context | Problem, stakeholders, constraints, assumptions, acceptance criteria |
| Architecture | Components, interfaces, deployment topology, data flows, trust boundaries |
| Alternatives | Feasible options, including simpler approaches, and selection rationale |
| Quality attributes | Availability, performance, security, privacy, maintainability, accessibility |
| Operations | Ownership, telemetry, capacity, recovery, support requirements |
| Delivery | Migration, compatibility, rollout, rollback, estimated effort and cost |
| Open risks | Unresolved questions, validation needed, and accountable owners |

## Review procedure

1. Author a proportionate proposal linked to the work item. Include diagrams and explicit failure modes rather than only a happy-path component list.
2. Identify affected service owners and reviewers for security, data, infrastructure, and integration boundaries.
3. Validate uncertain assumptions through a bounded spike, benchmark, or supplier clarification. Record findings and limitations.
4. Review the design for complexity, access boundaries, operability, compatibility, cost, and recovery. Capture feedback and decisions in the tracked proposal.
5. Resolve blocking questions or obtain explicit risk acceptance from the authorized owner. Record approval scope and conditions before implementation proceeds.
6. Publish an architecture decision record for consequential choices. Link it from the repository and relevant service documentation.
7. Check the implemented design against the approved proposal before release; review material deviations.

## Architecture decision record

Record identifier, title, status, date, decision owner, context, options, selected decision, consequences, and supporting evidence. Use proposed, accepted, superseded, or deprecated status. Preserve earlier decisions and link the replacing decision rather than rewriting the historical rationale.

## Completion and evidence

Retain the proposal, review discussion, approval, decision records, validation results, and implementation references. Reopen review when constraints, trust boundaries, intended use, or material assumptions change. Track unresolved design debt with an owner and review date.

## Related procedures

[SDLC and Change Management](01-sdlc-and-change-management.md) · [Infrastructure and Configuration Management](04-infrastructure-and-configuration.md)