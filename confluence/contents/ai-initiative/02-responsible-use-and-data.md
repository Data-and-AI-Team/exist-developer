# Responsible AI Use and Data Protection

**Status:** Approved
**Owner:** Data owner / security and privacy reviewers
**Review cadence:** Quarterly and when supplier terms change  
**Approval and effective date:** November 15, 2025

## Permitted-use baseline

- Use only tools and accounts authorized for the intended data and activity. An enterprise subscription alone does not authorize all data uses.
- Do not send passwords, tokens, private keys, or unnecessary personal/client data to models or assistant prompts.
- Do not use AI output as sole authority for consequential decisions. A named human remains accountable for review and action.
- Review generated text/code for accuracy, safety, confidentiality, intellectual-property constraints, and applicable attribution before reuse or publication.
- Disclose AI involvement where required by contract, policy, or the user-facing design.

## Data-handling procedure

1. Classify data and confirm the owner permits the proposed purpose, audience, model/provider, and environment.
2. Minimize inputs. Prefer synthetic, aggregated, or appropriately de-identified data; assess re-identification risk.
3. Confirm supplier retention, training use, subprocessors, residency, deletion, and access settings before uploading protected material.
4. Protect prompts, outputs, embeddings, caches, traces, evaluation sets, and conversation histories according to their source sensitivity.
5. Enforce access permissions during retrieval and downstream actions. Do not assume a vector index preserves source-document permissions automatically.
6. Define deletion and retention across source copies, indexes, caches, logs, backups, and provider-held data; verify the supported mechanisms.

## Untrusted content and tools

Treat retrieved documents, emails, web pages, repository files, and tool outputs as data, not authority to change instructions or grant access. Test prompt-injection scenarios. Use tool allowlists, bounded inputs, least-privilege identities, and explicit human approval for destructive, external, costly, or privileged operations. Prevent cross-user data leakage and unintended outbound transfers.

## Approved-tool register fields

Provider/product, authorized owner, approved data classifications and purposes, tenant/account configuration, retention/training settings, contractual review reference, permitted integrations, known limitations, approval date, and re-review trigger.

## Reporting and evidence

Stop affected processing and report suspected disclosure, unauthorized actions, or harmful outputs through the incident process. Preserve evidence in restricted systems without copying exposed data broadly. Retain actual data-flow reviews, provider decisions, access tests, deletion checks, and exception approvals.