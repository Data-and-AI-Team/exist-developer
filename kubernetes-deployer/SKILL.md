---
name: kubernetes-deployer
description: Use when creating, reviewing, or deploying Kubernetes manifests, with particular attention to safe secret handling.
---

# Kubernetes Deployer

## Secret Findings in the Examples

The example manifests contain no literal production credentials. `examples/secrets.example.yml` defines a Docker registry Secret with three credential-bearing fields inside `.dockerconfigjson`:

- `username` is the GitHub Container Registry account name.
- `password` is a GitHub token that requires only `read:packages` access.
- `auth` is the Base64 encoding of `username:token`. Base64 is an encoding, not encryption, so this value exposes the same credentials as `username` and `password` when populated.

The checked-in values are explicit `REPLACE_WITH_*` placeholders. Never replace them with real credentials in a tracked manifest. The use of `stringData` makes populated values plaintext in the YAML source even though Kubernetes converts them to Base64-encoded `data` when storing the Secret.

The same example file also defines the `presales-automation-secrets` Opaque Secret. Its placeholders cover PostgreSQL database and administrator credentials, separate PostgreSQL application credentials, MinIO root credentials, and OpenAI and Azure OpenAI API keys. Treat every populated value in this document as sensitive except the PostgreSQL database name, which is configuration but remains grouped with the deployment's secret inputs.

`examples/app.yml` and `examples/ui.yml` reference `dksh-registry-secret` through `imagePullSecrets`; these references do not expose the secret value. `examples/ingress.yml` references the cert-manager-managed `dksh-public-tls` Secret by name; it also does not expose TLS key material. The application environment values currently shown in `examples/app.yml` are non-secret configuration.

## Secret Handling Requirements

- Keep only placeholder Secret manifests in source control.
- Supply real values at deployment time through an approved secret manager, External Secrets Operator, Sealed Secrets, or a CI/CD secret store.
- If creating the registry Secret directly, use `kubectl create secret docker-registry` with values sourced from protected environment variables or secure files, without writing credentials to a tracked manifest or command log.
- Grant registry tokens the minimum required scope and use a dedicated machine identity where possible.
- Reference application credentials with `secretKeyRef` or mounted Secret volumes; do not put them in literal `env.value` fields, ConfigMaps, annotations, labels, image names, or command arguments.
- Restrict RBAC access to Secrets and enable encryption at rest for the Kubernetes API data store.
- If a real credential is committed, revoke or rotate it immediately, remove it from repository history, and audit its use. Deleting only the current file is insufficient.
- Before committing manifests, scan for private keys, tokens, passwords, connection strings, populated `Secret.data`, and populated `Secret.stringData` values.
