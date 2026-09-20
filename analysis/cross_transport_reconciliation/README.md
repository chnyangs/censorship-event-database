# Bounded cross-transport agreement

`earliest_windows_v1/plan.json` was frozen before new requests. Its exact budget
is **149 queries per provider, 298 total**, covering the earliest **6 of 18**
source-defined action windows: 16 address/action units, 32 issuer units and 64
endpoint snapshots. Collecting all 18 windows with the same prerequisites would
require 786 requests. Selection takes the largest earliest whole-window prefix
within the fixed 300-request ceiling; it does not use blacklist words or indexed
events to select targets. The selected action dates span April 2022 to May 2023.

The two fixed transports are dRPC's documented public Ethereum endpoint
`https://eth.drpc.org/` and 1RPC's current documented Ethereum endpoint
`https://public.1rpc.io/eth`. Their official documentation was captured and hashed
in `sources/measurement_panel/expanded_transport_sources/{drpc_public,one_rpc_public}/`.
The plan binds those captures, the completed source cohort, the source request
and result identities, and the collector/transport code before collection.

Per transport the plan contains one mainnet identity query, 12 exact block
headers, 36 code reads, 12 proxy-storage reads, and 88 calls (24 USDT forwarding
prerequisites and 64 target-state reads). Header comparisons require identical
block numbers, hashes and timestamps. Code comparisons use hashes of decoded
bytecode; storage/call comparisons require the same returned bytes. Target-state
queries run only after the corresponding chain, header, code and proxy/forwarding
prerequisites agree with the original capture.

Each provider/query has one attempt, with at least 0.5 seconds between live
requests. An HTTP 429 or rate-limit response stops that provider immediately;
there is no retry, alternate endpoint substitution, or selection of replacement
windows. Raw requests/responses, hashes, dependency skips and failures remain in
the artifact. Interrupted queries conservatively consume their only attempt.

`summary.json` and `results.json` record the execution outcome. Agreement is
**cross-transport agreement**, not independently verified upstream ownership or
an independent human reference. This subset does not establish full-cohort
reconciliation, complete event history, absence of unobserved issuer actions, or
causal attribution. Providers may share upstream infrastructure.

## Executed outcome

| Transport | Attempted | Matched | Matching target-state calls | Stop/gap |
| --- | ---: | ---: | ---: | --- |
| dRPC | 149 | 149 | 64 | None |
| 1RPC | 10 | 8 | 0 | One historical header returned HTTP 410; a later header returned HTTP 429 |
| Total | **159** | **157** | **64** | 139 planned 1RPC queries skipped after rate limit |

The HTTP 410 body reports a discontinued routed endpoint and directs users to
Lava's gateway; the later HTTP 429 body reports an OnFinality rate limit. These
are preserved responses from the fixed 1RPC URL, not grounds for substituting
backends or claiming that the entire public endpoint is discontinued. The
collector stopped 1RPC immediately at its first rate limit. There were no
retries or query mismatches among valid responses. The 1RPC matches comprise
mainnet identity and seven historical headers; it did not reach target-state
queries. dRPC matched all 64 selected target-state calls and their prerequisites.

```sh
python3 scripts/reconcile_issuer_snapshots.py prepare \
  --out-dir analysis/cross_transport_reconciliation/NEW_RUN --max-requests 300
python3 scripts/reconcile_issuer_snapshots.py run \
  --plan-dir analysis/cross_transport_reconciliation/NEW_RUN
python3 -m pytest -q tests/test_reconcile_issuer_snapshots.py
```

Preparation is offline and refuses an existing output directory. Running a fully
completed artifact again verifies stored request/response hashes and replays its
derived summaries without more requests. Six focused tests cover normal replay,
header disagreement, dependency skips, rate-limit stopping, budget refusal,
capture tampering, and interruption without retry.
The completed run was replayed with a transport that raises on any network use:
`summary.json` and `results.json` remained byte-identical and no requests occurred.
