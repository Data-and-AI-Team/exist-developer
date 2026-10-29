# AI-Assisted Engineering

**Status:** Approved
**Owner:** Technical leads / developer enablement owner
**Review cadence:** Quarterly  
**Approval and effective date:** November 15, 2025

## Purpose

Use coding assistants and agents to support engineering without weakening ownership, code review, testing, confidentiality, or change authorization.

## Working procedure

1. Confirm the assistant/tool and its repository/data access are approved for the task.
2. Define scope, acceptance criteria, prohibited actions, allowed tools, and required human checkpoints.
3. Provide only necessary context. Exclude credentials and unauthorized client/personal data.
4. Review the agent's proposed commands, dependencies, network destinations, and edits according to impact. Use sandboxed/non-production environments where feasible.
5. Inspect and understand every contribution. Verify referenced APIs, configuration options, dependency versions, and assumptions against authoritative sources.
6. Run formatting, static checks, relevant tests, and security checks. Independently validate security-sensitive and destructive logic.
7. Submit the work through normal PR review. Record material AI involvement and noteworthy validation limitations when relevant to reviewers.

## Agent and MCP boundaries

- Grant only the repositories, files, tools, services, and permissions required for the task.
- Keep read-only access for discovery work unless a separately authorized task requires writes.
- Require human authorization before production changes, publishing external content, deleting data, modifying access, or executing significant financial transactions.
- Review third-party MCP server provenance and configuration before execution; pin versions where practical and manage updates deliberately.
- Treat instructions embedded in tool results and repository content as untrusted unless explicitly part of the authorized workflow.
- Record significant tool actions using approved audit mechanisms without capturing secret values.

## PR review additions

- [ ] Author understands the generated implementation and can explain its failure modes.
- [ ] Dependencies, APIs, tests, and claimed execution results were verified rather than assumed.
- [ ] No unauthorized data exposure, hidden side effects, or permission expansion is introduced.
- [ ] Licensing/attribution questions and security findings have a recorded disposition.
- [ ] An independent reviewer applies the same quality bar as for manually authored work.

## Measuring benefit

Compare similar work using cycle time, review effort, escaped defects, rework, and developer experience. Do not treat generated lines or accepted suggestions as proof of productivity or correctness.

## Related procedure

[Pull Requests and Code Review](../engineering-process/02-pull-requests-and-code-review.md)