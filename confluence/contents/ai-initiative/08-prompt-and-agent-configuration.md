# Prompt and Agent Configuration Management

**Status:** Approved
**Owner:** AI technical owner / technical leads
**Review cadence:** Quarterly and with material behavior changes  
**Approval and effective date:** November 15, 2025

## Configuration inventory

Treat prompts and agent settings as deployable software assets. Version system/developer instructions, task templates, model settings, output schemas, tool definitions/scopes, retrieval configuration, iteration limits, and human-approval rules. Keep credentials outside these assets.

## Template standard

| Field | Required information |
| --- | --- |
| Identity | Name, version, owner, intended use, authorized audience |
| Inputs | Typed variables, limits, expected provenance, untrusted sections |
| Behavior | Task, scope, evidence requirements, abstention and escalation |
| Outputs | Schema/format, validation, prohibited disclosures |
| Actions | Allowed tools, permissions, limits, approvals, stop conditions |
| Assurance | Evaluation set, acceptance criteria, known limitations |

## Change procedure

1. Create a version-controlled change linked to a behavior requirement or observed failure.
2. Make instruction boundaries explicit; separate trusted instructions from user/retrieved data. Avoid credentials and sensitive examples in templates.
3. Review changes to tool access, autonomy, source selection, approval policy, and model behavior as functional/security changes.
4. Run formatting/schema checks and relevant regression evaluations. Include injection, refusal/abstention, malformed output, and tool-action cases when applicable.
5. Compare the candidate with the current configuration on quality, safety, latency, and cost. Record limitations and approval.
6. Promote the reviewed configuration through environments with a versioned release record; avoid untracked production prompt edits.
7. Observe behavior and restore the prior known configuration if rollout criteria fail.

## Runtime controls

Validate model output before consumption or tool execution. Enforce tool permissions, action limits, and approval outside prompt text. A prompt instruction is not an access-control boundary. Record the effective configuration version for each operational trace using minimized telemetry.

## Emergency changes and reuse

Use the engineering emergency-change path for urgent behavior fixes and complete retrospective review. Maintain reusable templates with owners and supported contexts; do not copy them into new applications without validating permissions, data assumptions, and evaluation relevance.

## Evidence

Retain configuration revisions, review decisions, evaluation comparisons, release identifiers, and recovery outcomes. Keep actual approval decisions distinct from instructions merely asking the model to obtain approval.