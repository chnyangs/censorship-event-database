# Completed candidate endpoint campaign

This run collected all **140 endpoint snapshots** for the frozen machine-proposed
cohort: **35 measurement units**, crossed with USDC and USDT (**70 issuer units**),
across **18 action windows**. It used **521 logical RPC queries and 521 HTTP
attempts**, with no retries, RPC response gaps or stop conditions. An offline replay
reproduced the existing artifacts without requests or changes to their bytes.
See [the execution summary](summary.json) and [the pre-request manifest](collection_manifest.json).

The first snapshot is post-block state at the first block timestamp at or after
the window's inclusive start. The last is post-block state at the final block
timestamp before its exclusive end. The first snapshot is inside the window,
not a pre-window baseline.

| Issuer | First/last blacklist words | Candidate units |
|---|---|---:|
| USDC | `0/1` | 35 |
| USDT | `0/0` | 19 |
| USDT | `0/1` | 14 |
| USDT | `1/1` | 2 |

These boundary contrasts do not establish exact change times, the absence of
intervening events, or a causal response to the source action. Equal endpoint
states are not event-level negatives. Eligibility remains machine proposed;
human adjudication, full-window logs and independent reference labels remain
incomplete. The earlier Garantex first-batch artifacts are preserved separately.

`captures/` retains content-addressed requests, raw responses, attempt metadata
and query results. `boundaries/` records adjacent timestamp checks;
`prerequisites/` records historical code/proxy/forwarding checks; `snapshots/`
holds the 140 individual state records; `windows/` records all 18 windows.
The recorded scope is
`machine_source_defined_partial_endpoint_collection_human_review_pending`.
Endpoint-campaign completion does not mean full-cohort study completion.

The subsequent [historical-interface comparison](../../historical_interface_verification/v1/README.md)
is a separate artifact and does not rewrite this run's original flags. Local
compiler reproduction and full-snapshot independent chain reconciliation remain
incomplete. See [the collection procedure](../../../docs/issuer-cohort-endpoint-collection.md)
for budgets, pacing, immutable captures and explicit resume behavior.
