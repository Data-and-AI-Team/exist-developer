# Knowledge and Retrieval Management

**Status:** Approved
**Owner:** Knowledge/data owner / AI technical owner
**Review cadence:** Quarterly and when sources or access rules change  
**Approval and effective date:** November 15, 2025

## Source inventory

For each knowledge source, record owner, purpose, authorized audience, classification, source system, document identifiers, update/deletion mechanism, retention, rights to index, and freshness target. Do not equate connector access with permission to redistribute source content.

## Ingestion procedure

1. Obtain data-owner authorization and confirm the intended users and processing providers.
2. Extract content through approved connectors, retaining source identifiers, canonical links, version/time, classification, and access metadata.
3. Exclude unsupported, unauthorized, unnecessary, or sensitive material outside the approved purpose. Handle embedded instructions as untrusted document content.
4. Clean and chunk documents using a versioned method appropriate to headings, tables, code, and document boundaries. Preserve context needed to interpret each chunk.
5. Generate embeddings with an identified model/version and record index schema, dimensions, and processing configuration.
6. Reconcile ingestion outcomes against the source inventory; route extraction failures and missing metadata to an owner.

## Retrieval and authorization

Enforce source-equivalent access for the current user or authorized service context before content is exposed to generation or returned to the user. Test group changes, denied documents, cross-user/cross-tenant access, and revoked permissions. Do not rely on the model to hide retrieved content. Apply equivalent protections to caches, snippets, citations, and debug traces.

## Quality and freshness

Maintain representative queries with relevant source expectations. Measure retrieval relevance, missing results, citation correctness, grounded answer quality, and stale-content incidents. Compare chunking, ranking, filtering, and reranking changes using held-out examples. Define conflict resolution for contradictory sources and an abstention/escalation path when evidence is insufficient.

## Update and deletion

Track source changes and tombstones; refresh within the agreed source-specific target. Remove or restrict stale versions, revoked access, deleted documents, derived chunks/embeddings, and applicable cached outputs. Validate deletion propagation. For embedding/index changes, build and evaluate a compatible index, switch deliberately, and retire obsolete copies according to retention rules.

## Evidence

Retain source approvals, ingestion configuration/version, permission tests, freshness/deletion checks, evaluation reports, and exception records. Store sensitive samples in restricted locations rather than broadly accessible documentation.

## Related procedures

[Responsible AI Use and Data Protection](02-responsible-use-and-data.md) · [AI Evaluation and Assurance](04-evaluation-and-assurance.md)