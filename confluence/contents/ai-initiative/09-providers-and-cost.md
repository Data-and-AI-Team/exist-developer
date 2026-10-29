# AI Provider Selection and Cost Management

**Status:** Approved
**Owner:** Initiative sponsor / procurement and AI technical owners
**Review cadence:** Quarterly and before material supplier changes  
**Approval and effective date:** November 15, 2025

## Selection criteria

Evaluate providers against a representative approved workload, not marketing benchmarks alone. Record quality, security/privacy terms, supported regions, retention/training settings, contractual requirements, availability/support, model lifecycle, rate limits, integration effort, portability, and total operating cost.

## Provider decision procedure

1. Define use-case requirements, data classifications, traffic assumptions, quality thresholds, and budget owner.
2. Review supplier terms, rights, subprocessors, residency, deletion options, and tenant controls with relevant stakeholders.
3. Test shortlisted providers/models using the same representative evaluation and realistic operational limits.
4. Compare measured task success, reviewer effort, latency, failure behavior, and full cost. Record trade-offs and dependency risks.
5. Obtain approval for the specific product, configuration, data, region, and purpose. Add it to the approved-tool register.
6. Plan for model retirement, provider outage, contract expiry, and export/deletion needs. Validate fallback quality separately before enabling it.

## Cost model

Estimate workload volume multiplied by measured unit consumption and current supplier prices. Include input/output tokens or requests, embeddings, retrieval/storage, tools, hosting, network transfer, retries, evaluation runs, observability, and human review. Document pricing date, currency, assumptions, and taxes/commitments where relevant. Report cost per successfully completed task as well as total spend.

## Operating controls

- Assign usage and billing ownership per application/environment; distinguish development, evaluation, and production spend.
- Set service-specific request/token/tool limits, budgets, alerts, and an escalation/stop policy. Billing alerts alone do not enforce a hard cap.
- Bound retries, concurrency, fan-out, and agent iterations. Monitor abnormal usage and failed-task costs.
- Use caching or lower-cost routing only when data protection and quality requirements permit. Re-evaluate routed models and fallback paths.
- Review forecasts and actual spend at an agreed cadence; investigate variances and update capacity assumptions.

## Evidence

Retain selection scorecards, representative test results, supplier approval, dated cost assumptions, budget decisions, usage reports, and lifecycle notices. Do not invent savings or mark a provider approved without an actual decision.