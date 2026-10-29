# Coding Standards and Secure Development

**Status:** Approved
**Owner:** Technical leads / security reviewer
**Review cadence:** Quarterly and after major platform changes  
**Approval and effective date:** November 15, 2025

## Baseline conventions

- Each repository documents supported runtime versions, setup, build/test commands, formatting/linting rules, module structure, and local development configuration.
- Use automated formatters and linters appropriate to the language. Keep checks in version control and run them in CI.
- Prefer clear names, small cohesive units, explicit interfaces, and minimal dependencies. Explain non-obvious decisions rather than narrating syntax.
- Apply consistent error handling; preserve useful diagnostic context without exposing internal details to users.
- Document public APIs, configuration variables, compatibility constraints, and significant architecture decisions.

## Secure implementation

1. Validate input at trust boundaries using explicit schemas and limits. Use parameterized database queries and context-appropriate output encoding.
2. Enforce authentication and authorization on the server for each protected operation. Test forbidden and cross-tenant access paths where applicable.
3. Keep credentials outside source code and deployable artifacts. Retrieve secrets using the approved environment mechanism.
4. Use maintained libraries for cryptography, identity, and protocol handling. Do not introduce custom cryptographic schemes.
5. Minimize collected data and apply access/retention rules. Redact sensitive values from logs, errors, traces, and test fixtures.
6. Configure bounded timeouts, retries, pagination, resource limits, and safe failure behavior for external interactions.
7. Review file handling, deserialization, outbound requests, and command execution for injection and unintended access.

## Dependencies and generated code

- Declare dependencies in manifests and use lockfiles or equivalent reproducible resolution where supported.
- Review new dependencies for necessity, provenance, maintenance, vulnerabilities, and license compatibility.
- Configure applicable dependency, secret, and static-analysis checks. Triage findings with owner, severity, remediation date, or approved exception.
- Treat copied and AI-generated code as untrusted contributions requiring understanding, review, and testing. Observe applicable license and attribution requirements.

## Done criteria and evidence

A contribution meets this standard when applicable automated checks pass, security-relevant paths are tested, peer review is complete, documentation is current, and unresolved findings have explicit disposition. Retain check results and review decisions in the PR and issue tracker.

## Repository adoption checklist

- [ ] Document language/framework-specific standards and supported versions.
- [ ] Configure formatter, linter, tests, and applicable security checks.
- [ ] Identify maintainers and dependency/vulnerability triage ownership.
- [ ] Add PR and issue templates and document approved local secret handling.