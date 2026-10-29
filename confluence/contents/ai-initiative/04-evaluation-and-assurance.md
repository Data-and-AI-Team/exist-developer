# AI Evaluation and Assurance

**Status:** Approved
**Owner:** Evaluation owner / technical owner
**Review cadence:** Before each material release and quarterly for operating use cases  
**Approval and effective date:** November 15, 2025

## Evaluation design

Define intended use, representative tasks, unacceptable outcomes, baseline, acceptance thresholds, test-set provenance, protected-data handling, and reviewer roles before evaluating. Separate development examples from a held-out evaluation set where feasible. Document uncertainty and sample limitations.

## Evaluation dimensions

| Dimension | Example checks |
| --- | --- |
| Task quality | Correctness, completeness, relevant refusal, comparison with baseline |
| Grounding | Supported claims, valid citations, source freshness, abstention when evidence is absent |
| Security | Prompt injection, tool abuse, unauthorized access, secret/data exfiltration |
| Privacy | Cross-user leakage, unnecessary disclosure, retention/deletion behavior |
| Robustness | Malformed input, missing context, provider failure, conflicting instructions |
| Human impact | Bias or uneven performance across relevant user groups and contexts |
| Operations | Latency, throughput, cost, rate limits, retries, fallback, and disable behavior |
| Agent actions | Correct tool selection, bounded permissions, approvals, side effects, repeatability |

Select checks based on the risk review; document why a dimension is not applicable instead of marking it passed without testing.

## Execution and decision

1. Freeze model/provider version where available, prompt/configuration, retrieval corpus/index, tool versions, and evaluation dataset revision.
2. Run automated tests and human review using a documented rubric. For stochastic behavior, repeat important scenarios and report variability.
3. Independently inspect a risk-appropriate sample; do not rely solely on a model grading itself.
4. Record failures, severity, root-cause hypotheses, mitigations, and regression tests.
5. Compare results with pre-agreed thresholds and baseline. Stop release on unmet blocking criteria; any accepted residual risk requires accountable approval.
6. Retest after material model, prompt, retrieval, permission, or tool changes.

## Evaluation report template

- Use case, intended audience, risk tier, evaluator, date.
- Versions, environment, dataset provenance, sample size, rubric, thresholds.
- Measured results, variability, limitations, and representative failure references.
- Security/privacy/abuse-case findings and remediation status.
- Human oversight, fallback, and operational validation results.
- Go/no-go decision, approver, conditions, residual risks, and next review trigger.

## Evidence handling

Store evaluation datasets and sensitive outputs in approved restricted locations. Publish summaries and links in this space; do not expose customer records or exploit material to an unnecessarily broad audience.