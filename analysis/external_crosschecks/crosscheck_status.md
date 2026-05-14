# External Crosscheck Execution Status

Status enum:

- `pending` — planned but not executed for the current snapshot.
- `checked_no_conflict` — executed and did not weaken the scoped claim.
- `checked_weakened_claim` — executed and caused a claim downgrade, re-scope, or audit queue entry.
- `not_applicable` — benchmark family does not apply to the named claim/layer.

This ledger distinguishes executed crosschecks from the crosswalk plan in
`benchmark_crosswalk.yaml`. A benchmark should not be cited as validating a
claim unless its row is `checked_no_conflict` or `checked_weakened_claim` with
the resulting scope change recorded.

| Benchmark family | Current status | Applies to | Snapshot note |
| --- | --- | --- | --- |
| OONI / OONI Explorer | `checked_weakened_claim` | L0 denominator language | Committed L0 summary reports zero public OONI measurement denominators in queried cells; this supports observability-gap language, not no-blocking claims. |
| Censored Planet | `pending` | L0/L4 reachability baselines | Procedure documented, but committed CP ingestion is not present in v0.1. |
| Tornado Cash event-study literature | `pending` | Tornado-family contextual sanity checks | Useful for external context; not yet an executed ledger item for this snapshot. |
| MEV Watch / relay dashboards | `pending` | L1 relay exposure context | Current L1 evidence is sourced through admitted event records and referenced measurement lineage; dashboard crosscheck is not an executed release ledger. |
| Chainalysis-style compliance / Lumen-style transparency sources | `pending` | entity normalization and source-limit wording | Supporting context only until a row-specific public replayable source is attached. |
