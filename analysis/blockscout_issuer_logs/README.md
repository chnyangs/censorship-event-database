# Issuer event indexing and offline cohort matching

The source-defined collection covers the global span of the 18 frozen action
windows: Ethereum blocks **14477774–24050082**, inclusive. Requests filter only
canonical issuer contracts and all four predeclared add/remove event topics.
Candidate target addresses and observed endpoint words do not enter API filters.
The current official Blockscout controller and chain-query implementation were
captured before topic-stream collection, including descending cursor semantics.

## Preserved run history

- `capability_v1/`: four HTTP 422 responses exposed an invalid initial
  `items_count=0`; the API requires at least 1. No event results were accepted.
- `capability_v2/`: corrected seed counter 50; all 12 bounded pages succeeded.
  Cursor order, exact event topics, issuer identity and ABI address/data layout
  passed. The USDC removal stream reached older history and terminated on page 3.
- `full_streams_v1/`: **zero requests**, superseded before execution. It froze the
  older collector and invalid seed; `superseded_before_requests.json` explains why
  it was replaced. The original plan remains unchanged.
- `full_streams_v2/`: completed in **59 successful pages**, within the separately
  frozen ceiling of 200 pages per stream / 800 total. There were no HTTP/RPC gaps
  or rate limits. One attempt per page, at least one second between requests,
  strict same-host HTTPS redirects and immediate rate-limit stopping apply.

| Stream | Pages | Accepted events in the declared span | Termination |
| --- | ---: | ---: | --- |
| USDC Blacklisted | 10 | 450 | Endpoint exhausted |
| USDC UnBlacklisted | 3 | 134 | Endpoint exhausted |
| USDT AddedBlackList | 41 | 2,035 | Valid descending page crossed the lower bound |
| USDT RemovedBlackList | 5 | 210 | Endpoint exhausted |
| Total | 59 | **2,829** | All four declared index ranges covered |

Raw pages, exact request URLs and hashes are retained. A page must have strictly
descending `(block_number, index)` values, valid cursor continuation, matching
contract/topic, valid event address encoding, and transaction/block identity.
Events outside the declared lower bound are used only to establish that paging
crossed the boundary and are excluded from accepted event output. USDC addresses
are decoded from indexed topics; USDT addresses come from non-indexed data.

## Offline window-matching indexed events

The formal matcher is `scripts/match_blockscout_issuer_logs.py`.
`cohort_matches_v2/window_matches.jsonl` retains **all 70 issuer units** representing
35 machine-proposed address/action units, including zero matches. Matching uses
issuer, affected address and each frozen window's inclusive block bounds.

- **49 issuer units** contain a matching indexed event: **35 USDC and 14 USDT**.
- These are **49 event associations / 49 unique event identities**, covering
  all **35 machine candidate addresses**. There were no duplicate input event rows.
- The other **21 issuer units have zero indexed matches**. That is not a no-action
  label or a validated negative.
- All **70 endpoint-word pairs are consistent conditional on the indexed event
  sequences**. Endpoint words are post-block state: events at the first endpoint
  block are retained as matches but excluded from replay because the initial word
  already reflects that block. Replay covers `(first block, last block]`.

The matcher preserves ordered add/remove sequences and separate counts for every
unit. Input event identities are deduplicated by transaction hash/log index/block
hash; conflicting duplicates fail. Repeated attribution to overlapping candidate
windows would remain separate associations and would be counted separately from
unique event identities.

Timing uses each frozen candidate's `trigger_earliest_utc` and
`trigger_latest_exclusive_utc`, rather than treating the action URL's date as an
exact trigger timestamp. Of the 49 matching events, **0 precede the trigger
interval, 27 fall within it, and 22 follow it**. Ordering within the trigger-day
interval is indeterminate. For an indexed block timestamp `e` and trigger
interval `[t0, t1)`, each event records delay bounds `(e - t1, e - t0]`; these
are not exact response latencies. `cohort_matches_v1/` preserves the earlier
matching output before these interval summaries were added.

**Index-range completeness is not independently verified chain completeness.**
Blockscout is a different index transport, with unverified upstream independence.
Schema/pagination validation and endpoint-word consistency do not prove absence
of silent index omissions, reproduce historical bytecode, validate human source
eligibility, or establish that sanctions caused an issuer action. All independent
chain-completeness, human-reference and causal-attribution flags remain false;
response classifications remain null.

## Reproduction

```sh
python3 scripts/match_blockscout_issuer_logs.py \
  --out-dir analysis/blockscout_issuer_logs/NEW_OFFLINE_MATCH_RUN
python3 -m pytest -q tests/test_match_indexed_issuer_events.py \
  tests/test_collect_blockscout_issuer_logs.py
```

Offline replay to a temporary directory produced byte-identical `summary.json`,
`window_matches.jsonl` and frozen `matcher_source.py`. Input/source hashes in the
matching manifest were identical; only its new preparation timestamp differed.
The matcher has nine focused tests and the collector eleven, all passing. This
replay makes no network requests and does not overwrite the original artifacts.

The [AWS metadata-only fallback](../public_blockchain_discovery/aws_eth_v1/README.md)
contains an exact 623-object / 340.6-GB inventory for the same 18 windows. No full
Parquet object was downloaded.
