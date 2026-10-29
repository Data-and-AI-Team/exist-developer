# AI Architecture and Integration Patterns

**Status:** Draft for review  
**Proposed owner:** AI technical owner / architecture lead  
**Review cadence:** Quarterly and when solution boundaries change  
**Approval and effective date:** Pending owner review

## Pattern selection

Start with the task, evidence needs, data sensitivity, permitted actions, and failure tolerance—not the availability of a model. Compare a non-AI baseline before selecting additional complexity.

| Pattern | Appropriate starting point | Key trade-off |
| --- | --- | --- |
| Deterministic workflow | Explicit rules, exact calculations, stable schemas | Predictable behavior but limited handling of ambiguity |
| Model-assisted generation/classification | Language tasks with bounded human-reviewed outputs | Variability and unsupported claims need evaluation |
| Retrieval-augmented generation | Answers grounded in authorized, changing knowledge | Retrieval quality, source permissions, freshness |
| Tool-using agent | Tasks needing dynamic selection of bounded actions | Higher side-effect, permission, and recovery complexity |
| Fine-tuning | Demonstrated task/style adaptation not met by simpler methods | Training rights, dataset quality, evaluation, lifecycle cost |
| Hybrid | Language interpretation around deterministic business logic | Clear boundaries between suggestion and execution |

## Architecture procedure

1. Define task success, prohibited outcomes, latency/cost budget, expected load, and data boundaries.
2. Document model/provider, retrieval, tool execution, identity propagation, storage, and telemetry flows.
3. Select the simplest viable pattern. Record alternatives and why retrieval, agentic actions, or fine-tuning are necessary.
4. Keep authorization, business invariants, calculation, and consequential action checks outside the model where feasible. Treat model output as untrusted input to downstream systems.
5. Define structured-output validation, iteration limits, timeouts, failure fallback, and disable/recovery behavior.
6. Prototype uncertain assumptions with authorized data; compare results and total operational cost with the baseline.
7. Obtain proportionate technical/risk review and complete evaluation before release.

## Agent boundary checklist

- [ ] Tool scopes, allowed destinations, execution identity, and approval points are explicit.
- [ ] Untrusted retrieval cannot independently expand privileges or authorize actions.
- [ ] Loops, fan-out, token usage, tool calls, and external cost have enforced limits.
- [ ] Partial failures, duplicate writes, interrupted sessions, and compensation are handled.
- [ ] Operators can inspect decisions and stop execution without relying on prompt compliance.

## Records

Retain architecture/data-flow diagrams, decision rationale, prototype measurements, risk review, and evaluation links. Revisit the pattern when intended use, data access, autonomy, or scale changes.

## Related procedures

[AI Evaluation and Assurance](04-evaluation-and-assurance.md) · [Architecture and Technical Design Reviews](../engineering-process/09-architecture-and-design.md)