# Pull Requests and Code Review

**Status:** Approved
**Owner:** Technical leads
**Review cadence:** Quarterly  
**Approval and effective date:** November 15, 2025

## Purpose

Make code and configuration changes traceable, independently reviewed, and supported by reproducible checks before merge.

## Author workflow

1. Start a short-lived branch from the repository's designated integration branch. Reference the tracked work item in the branch or PR.
2. Keep the change focused. Split unrelated refactoring and behavior changes when practical.
3. Run formatting, linting, relevant tests, and configured security checks locally or in CI.
4. Open a PR containing purpose, linked requirement, scope, risk, test evidence, configuration/data changes, deployment implications, and rollback notes.
5. Request an independent reviewer with relevant domain knowledge. Request security or infrastructure review when those boundaries are affected.
6. Address review feedback and rerun checks after changes. Obtain renewed review for material revisions.

## Reviewer checklist

- [ ] Implementation meets acceptance criteria and handles errors, boundary conditions, and authorization.
- [ ] Code follows repository conventions and avoids unnecessary complexity or duplication.
- [ ] Tests cover the changed behavior and credible failure paths.
- [ ] Logs and errors do not reveal secrets or inappropriate personal/customer data.
- [ ] Dependencies and licenses are acceptable; no credentials or unreviewed generated artifacts are introduced.
- [ ] Database/API changes preserve compatibility or have an explicit migration plan.
- [ ] Monitoring, runbooks, deployment, and rollback implications are addressed.
- [ ] AI-generated contributions have been understood and validated by the author.

## Merge controls

- Protect designated integration/release branches using the repository platform's supported settings.
- Require at least one independent approval and the configured required CI checks. The repository owner defines additional approvals for sensitive components.
- Resolve blocking comments and avoid merging with known failing required checks.
- Restrict bypass privileges; record the reason, authorizer, and follow-up for an emergency bypass.
- Use the repository's documented merge strategy and retain the PR/work-item linkage.
- Delete obsolete branches according to repository policy; retain the review record.

## Minimum PR template

| Field | Required information |
| --- | --- |
| Objective | What changes and why; linked work item |
| Scope and risk | Components, data/access impact, compatibility |
| Validation | Test commands/pipeline links and results |
| Delivery | Configuration, migrations, rollout, rollback |
| Review | Requested reviewers and unresolved questions |

## Exceptions and evidence

Document exceptions using the space's exception process. Evidence consists of PR history, approvals, required-check results, linked work item, and any bypass authorization—not a checklist marked complete without supporting records.