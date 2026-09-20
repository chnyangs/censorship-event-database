# Source-defined issuer endpoint collection

`python scripts/collect_issuer_cohort_snapshots.py` reads the existing frozen
`analysis/issuer_candidate_manifest/` bundle and writes a new run in
`analysis/issuer_candidate_snapshots/cohort_endpoint_v1/`. The earlier Garantex
first-batch run is preserved. This campaign includes all 35 machine-proposed
measurement units, each crossed with canonical USDC and USDT, across 18 action
windows. Source adjudication remains pending. Existing pilot-family exclusions,
family ambiguities, updates and unclassified records retain their frozen
dispositions; the collector does not reconsider them from measured outcomes.

The manifest is written before requests and binds the complete candidate-bundle
index, panel, collector and transport source hashes. Selection is independent
of token balance and measured states. Each address is read at the first block
whose timestamp is at least the window start, and the last block whose timestamp
is before its exclusive end. These are post-block states **inside** the window.
They are not a pre-window baseline. Equal endpoint states do not establish that
no intervening event occurred; different endpoints do not establish the time,
reason or causal attribution of any change.

The collector shares timestamp-boundary searches and identical issuer/block
prerequisite reads. Searches finish with adjacent blocks straddling each UTC
boundary. Mainnet chain ID, historical canonical contract code, USDC proxy slot
and implementation code, and USDT forwarding metadata are checked before state
reads. Valid return shapes do not reproduce historical implementation bytecode
or independently reconcile chain data. This endpoint collector does not collect
full-window logs, human references or response classifications. Separate
Blockscout index traversal and a partial cross-transport campaign have since
executed; the [validation progress report](../analysis/validation_progress/README.md)
checks those stages separately. Independent chain completeness and human
reference labels remain unestablished.

The fixed ceiling is 1,400 distinct logical RPC queries and at most two HTTP
attempts per query (2,800 total). Every HTTP request starts at least 0.15 seconds
after the preceding start, including retries. HTTP 429 or an RPC rate-limit
signal stops the campaign; three consecutive logical RPC gaps also stop it.
There is no automatic endpoint substitution. Gaps are retained, never converted
to negative outcomes.

For interruption recovery, use the same command with `--resume`. The collector
refuses changed code, inputs or configuration and verifies stored request and
response hashes before issuing resumed requests. Captures and completed query,
boundary, prerequisite and snapshot records are immutable. An attempt whose
start was recorded but whose capture is incomplete consumes one of the two
attempts; it is never silently repeated. A process lock prevents concurrent
writers. Recorded provider rate errors are terminal for that run rather than
silently cleared on resume. A changed design or provider requires a newly named
run with its own manifest.

Progress records are printed after each action window. `snapshots/` retains
individual endpoint records and `summaries/` retains content-addressed summaries
of each execution/resumption, including exact incomplete unit IDs. A final
`summary.json` is created only when all 70 issuer units have two valid endpoint
snapshots. “Endpoint snapshot campaign complete” covers these endpoint reads
only; `full_cohort_execution`, `full_window_logs_complete`, human validation,
and independent chain reconciliation remain false.
