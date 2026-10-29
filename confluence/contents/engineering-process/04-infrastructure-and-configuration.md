# Infrastructure and Configuration Management

**Status:** Approved
**Owner:** Platform/operations owner
**Review cadence:** Quarterly  
**Approval and effective date:** November 15, 2025

## Scope

Provisioning and changes to hosting, networking, identity, databases, storage, deployment platforms, and runtime configuration across development, test, staging, and production.

## Environment and access baseline

- Maintain an environment/service inventory with owner, purpose, data classification, network boundaries, dependencies, backup arrangements, and support coverage.
- Separate production and non-production access and credentials. Do not copy production data into lower environments without approved protection and authorization.
- Use named identities, least privilege, approved strong authentication, and tracked privileged access. Remove access on role change or departure and periodically review it.
- Store secrets in an approved secret-management mechanism. Record rotation ownership and procedure; do not place secrets in repository configuration, images, or documentation.

## Change procedure

1. Record scope, target environment, risk, expected cost/capacity effect, dependencies, and recovery plan in the work item.
2. Express repeatable infrastructure changes as version-controlled code where supported. Document any necessary manual operations.
3. Generate and review a plan/diff. Check destructive operations, public exposure, identities, encryption, retention, availability, and configuration defaults.
4. Validate in a non-production environment, including deployment and rollback/recreation behavior.
5. Obtain peer review and required release authorization before production apply.
6. Apply through the approved identity/pipeline. Protect state files and prevent conflicting applies where tooling supports locking.
7. Verify actual state, service health, access boundaries, and monitoring. Update inventory and runbooks.

## Configuration and drift

- Keep non-secret configuration versioned with documented defaults and environment overrides.
- Validate configuration at startup/deployment and fail safely on missing mandatory settings.
- Compare deployed state with desired state on a service-defined schedule; record drift findings and remediation.
- For emergency console changes, capture the operator, reason, time, and commands/actions, then reconcile the source of truth.
- Review patching and end-of-support risks; assign remediation work and risk acceptance where needed.

## Backups and recovery

Define service-specific recovery point and recovery time objectives with the business owner. Configure backup protection, access, retention, and failure alerts accordingly. Test restores into an isolated environment and retain observed results; backup success alone does not demonstrate recoverability.

## Required evidence

Inventory entry, reviewed infrastructure/configuration change, plan/apply record, access approval, secret-rotation reference where applicable, verification results, drift actions, and restore-test records. Link records without exposing secret values.