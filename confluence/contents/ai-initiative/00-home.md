# AI Initiative

**Status:** Approved
**Owner:** AI initiative sponsor / engineering leadership
**Review cadence:** Quarterly and after material AI capability changes  
**Approval and effective date:** November 15, 2025

## Purpose and scope

Govern the selection, development, use, evaluation, and operation of AI-enabled solutions and AI-assisted engineering. Enable useful experimentation while preserving accountability, data protection, security, and verifiable quality.

This space covers internal assistants, coding agents, retrieval-augmented applications, model/API integrations, and customer-facing AI features. It complements—not replaces—the Engineering Process procedures.

## Table of contents

1. [AI Use-Case Intake and Risk Review](01-intake-and-risk.md)
2. [Responsible AI Use and Data Protection](02-responsible-use-and-data.md)
3. [AI-Assisted Engineering](03-ai-assisted-engineering.md)
4. [AI Evaluation and Assurance](04-evaluation-and-assurance.md)
5. [AI Delivery, Monitoring, and Incident Response](05-delivery-and-operations.md)
6. [AI Architecture and Integration Patterns](06-architecture-and-patterns.md)
7. [Knowledge and Retrieval Management](07-knowledge-and-retrieval.md)
8. [Prompt and Agent Configuration Management](08-prompt-and-agent-configuration.md)
9. [AI Provider Selection and Cost Management](09-providers-and-cost.md)
10. [AI Enablement and Adoption](10-enablement-and-adoption.md)

## Governance roles

| Role | Accountability |
| --- | --- |
| Initiative sponsor | Priorities, funding, acceptable risk, and release escalation |
| Use-case/product owner | Intended use, outcomes, user impact, acceptance, and ongoing ownership |
| Technical owner | Architecture, integrations, evaluation reproducibility, and operations |
| Data owner | Authorization, classification, quality, access, and retention |
| Security/privacy/legal reviewers | Risk review relevant to data, suppliers, rights, and obligations |
| Evaluation owner | Independent challenge, test design, results, and regression assessment |
| Human operator/reviewer | Verify consequential outputs and approve bounded actions |

Assign actual role holders before approving a pilot. Lack of a reviewer is a governance gap to resolve, not an implicit approval.

## Lifecycle and gates

**Intake → risk/data review → isolated prototype → evaluated pilot → release approval → monitored operation → retirement.**

Each gate requires an explicit decision, supporting evidence, and an accountable owner. Production data access, external publication, and consequential autonomous actions require authorization before use.

## Initiative registers

Maintain actual registers for approved use cases, approved tools/providers, evaluations, decisions, risks/exceptions, and incidents. Minimum record fields are defined in the linked procedures. Register entries and adoption evidence must come from real reviews; this draft does not assert any provider or use case is approved.

## Success measures

Choose baseline and target measures per use case: quality, task completion, reviewer effort, time saved, user outcomes, security/privacy failures, latency, and cost. Review benefit claims against measured outcomes rather than generated-output volume.