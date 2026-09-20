# Issuer-log collection: transport checks, refused plans and completed index scan

The anonymous JSON-RPC transports tested on 2026-09-20 did not supply a usable
broad historical log range. A separately frozen Blockscout topic-index campaign
did complete the declared global block span. These are different collection
interfaces with different completeness risks. Human adjudication was not needed
to run either workflow; human references remain necessary for validity/error
estimates and final source attribution.

## Completed Blockscout index stream and matching

The final collection is documented in
[the Blockscout report](../blockscout_issuer_logs/README.md). It queried the
canonical USDC/USDT contracts and four predeclared add/remove topics over the
global span of the 18 source windows, blocks 14,477,774--24,050,082. Candidate
addresses and endpoint outcomes were not API filters.

All four declared index ranges completed in 59 pages and yielded 2,829 unique
accepted events: 450 USDC additions, 134 USDC removals, 2,035 USDT additions and
210 USDT removals. Offline matching retained all 70 cohort issuer units. Forty-nine
have indexed event associations (35 USDC and 14 USDT), covering all 35 machine
candidate addresses; 21 units have zero indexed matches. All endpoint pairs are
consistent conditional on the indexed sequences.

The indexer's pagination/range completion is **not independent chain
completeness**. Upstream independence is unverified, zero matches are not
no-action observations, endpoint consistency is not an omission test, and window
association is not causal attribution. Of the 49 matches, 0 precede the source
trigger interval, 27 occur within its day-level interval and 22 follow it.
Within-interval order is indeterminate, so these are bounded timing relations,
not exact response latencies.

## Bounded official-source checks

Exact documentation responses and hashes are under
`sources/measurement_panel/expanded_transport_sources/`. Every endpoint below is
documented by its own provider; no guessed keys, account creation, paid gateway,
transaction submission or automatic endpoint substitution occurred.

| Transport | Official source | Captured result |
| --- | --- | --- |
| Cloudflare trial | [Usage documentation](https://developers.cloudflare.com/web3/how-to/use-ethereum-gateway/) | The documented trial hostname does not resolve from this environment; chain identity fails and dependent queries are skipped. |
| Cloudflare public | [Supported networks](https://developers.cloudflare.com/web3/ethereum-gateway/reference/supported-networks/) | `https://cloudflare-eth.com/v1/mainnet` establishes chain ID 1. Historical header requests for declared blocks in 2022, 2023, 2024 and 2025 all return RPC Internal error. Separate 2022 pilot log probes at 10/100 blocks also fail; 1,000/10,000-block requests expose the documented 800-block cap, and later USDT requests encounter HTTP 429. No further Cloudflare probes followed. |
| LlamaNodes | [Official repository](https://github.com/llamanodes/web3-proxy) | The landing page returns HTTP 526; its documented public RPC returns HTTP 525 before chain identity. The official repository capture corroborates the endpoint spelling. |
| dRPC public | [Ethereum API documentation](https://drpc.org/docs/ethereum-api) | Mainnet and the fixed 2022 pilot header succeed. Log requests at 10/100/1,000 blocks cannot route to a suitable provider. A later HTTP 429 stops the remaining query immediately. |
| 1RPC public | [Current network documentation](https://docs.1rpc.io/using-the-web3-api/networks) | Current no-key URL is `https://public.1rpc.io/eth`. Mainnet and the pilot header succeed. USDC 10-block logs succeed; 100/1,000-block requests advertise a 50-block limit. USDT's 10-block query returns method unavailable. |

Cloudflare's [current setup instructions](https://developers.cloudflare.com/web3/get-started/)
require a paid subscription for a custom gateway, which was not pursued.
Its [migration guidance](https://developers.cloudflare.com/web3/reference/migration-guide/)
also describes legacy-hostname deprecation. Advertising an API method or archive
service does not prove anonymous historical access.

Raw query manifests/results are retained under `analysis/measurement_pilot/`:
`expanded_transport_feasibility_v1`, `cloudflare_public_feasibility_v1`,
`cloudflare_public_logs_only_v1`, and `drpc_1rpc_feasibility_v1`.
All are excluded method-feasibility probes on the outcome-informed Tornado Cash
training target. A failed header dependency is not reported as a failed log query;
the separate Cloudflare log-only probe explicitly documents that distinction.
The dRPC/1RPC probe uses one attempt per query, at least one second between queries,
and stops a provider immediately on its first rate limit.

dRPC and 1RPC return the same hash and timestamp as Alchemy for the pilot block:
15301835, 2022-08-08 13:30:03 UTC,
`0xe551579d3a75d54993e58987f97f7fe96cdbdf5d3712d72dfbcb2cf96ceb06ab`.
This is **cross-transport header agreement**. Upstream operator independence is
unverified, historical state methods on those two transports remain untested by
these probes, and no complete independent chain reconciliation is claimed.

## Preserved JSON-RPC first-batch plans, with zero collection requests

The existing source-defined Garantex first batch has 242,485 resolved blocks and
two issuer units. The new planner binds the candidate bundle, prior boundary
captures, exact collector source and transport library before any requests.

| Plan | Log ranges | Identity/header reads | Worst-case HTTP attempts | Frozen budget | Launch result |
| --- | ---: | ---: | ---: | ---: | --- |
| `garantex_tested10_v1/` | 48,498 | 5 | 97,006 | 200 | Refused before network access |
| `garantex_advertised100_v1/` | 4,850 | 5 | 9,710 | 200 | Refused before network access |

The 100-block Alchemy limit is advertised by captured API error bodies, not a
successful 100-block probe. The 10-block plan uses the directly tested USDC span;
issuer-specific runtime failures remain possible. The plans do not manufacture
positive or negative results. Their `launch_refusal.json` files record exactly
zero network requests. A 1-request-per-second minimum delay makes the successful
100-block case roughly 81 minutes before network latency or retries. This is a
planning bound, not measured throughput.

## Collector behavior and reuse

`scripts/collect_issuer_window_logs.py` implements deterministic contiguous block
chunks, exact raw captures, at most two total attempts per query across restarts,
and resumption from captures without overwriting them. It rechecks chain identity
and the four boundary headers against the frozen snapshots. A rate limit stops
collection without a retry. A failed chunk stops the run and remains a coverage
gap; malformed logs never become an empty valid response.

Returned logs must match contract/event signatures and requested block ranges,
have valid ABI address encoding, hashes and indices, and not be marked removed.
USDT addresses are decoded from non-indexed data. Duplicate logs use
`(transactionHash, logIndex, blockHash)`; conflicting duplicates, conflicting
block hashes, and cap-sized responses invalidate the entire affected chunk.
The partition rule and source hashes are frozen compactly; runtime expansion
does not choose ranges based on observed logs.

`requested_range_coverage_complete` becomes true only if every declared chunk
passes. It does not certify absence of silent server omissions. Independent log
completeness, human reference completion and historical bytecode reproduction
remain false, and the full-window response classification remains null.

```sh
# Planning is offline. The default200-attempt budget refuses both real plans.
python3 scripts/collect_issuer_window_logs.py plan \
  --out-dir analysis/issuer_log_plans/NEW_PLAN \
  --chunk-blocks 100 --http-budget 200
python3 scripts/collect_issuer_window_logs.py collect \
  --plan-dir analysis/issuer_log_plans/NEW_PLAN
python3 -m pytest -q tests/test_collect_issuer_window_logs.py
```

The preserved JSON-RPC profile supports only the documented Alchemy public
endpoint and the frozen one-address/two-issuer first batch. A different raw-RPC
transport or larger batch requires an explicitly reviewed profile/input extension
and a new plan. No raw-RPC full-window campaign was launched. The completed
Blockscout campaign uses its own frozen collector, page budget, validation rules
and focused tests; it does not retroactively make either refused Alchemy plan
executable.
