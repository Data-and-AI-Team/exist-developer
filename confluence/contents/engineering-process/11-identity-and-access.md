# Identity and Access Management

**Status:** Draft for review  
**Proposed owner:** Identity/platform owner / system owners  
**Review cadence:** Quarterly and after material access changes  
**Approval and effective date:** Pending owner review

## Access principles

Use named human identities, least privilege, approved strong authentication, and separate production/non-production privileges. Prefer group-based roles to scattered individual grants. Identify each system's access owner, approved role definitions, review interval, and authoritative joiner/mover/leaver notification source.

## Joiner and access request procedure

1. Record requester, identity, system/environment, business need, requested role, duration, and manager/service-owner approval.
2. Check that the role is appropriate and that sensitive or conflicting privileges receive additional review.
3. Provision through the approved identity system. Require supported strong authentication and communicate enrollment instructions without sharing credentials.
4. Verify intended access and denial of unnecessary privileges. Record the grant and expiry where applicable.

## Role changes and departures

On a role change, remove obsolete grants before or alongside adding new ones. On departure, follow the approved HR/security timing for disabling identities, ending sessions, removing group membership, and revoking personal tokens and delegated access. Transfer ownership of repositories, integrations, and operational duties. Review shared credentials accessible to the departing person and rotate them when appropriate.

## Privileged and emergency access

- Use separate privileged roles where supported; avoid routine work under administrator identities.
- Time-bound elevation and record purpose, approval, and significant administrative actions.
- Define break-glass custody, permitted triggers, notification, and post-use review. Test emergency access without exposing credentials.
- Revoke temporary elevation after use and reconcile any changes to the normal source of truth.

## Service accounts and integrations

Assign a human owner and purpose to every non-human identity. Limit scopes and accessible resources; avoid personal identities for long-lived production automation when a supported service identity exists. Store credentials in the approved mechanism, define rotation and expiry handling, and remove unused integrations. Review tokens, keys, and application grants alongside account membership.

## Periodic review and evidence

System owners review membership, privileged roles, external users, dormant accounts, and service identities on the agreed schedule. Record reviewer, scope, date, decisions, removals, and unresolved exceptions. Verify revocations rather than treating a request as proof that access was removed.