# Read-only method-feasibility runs (2026-09-20)

All runs here are **`feasibility_pilot_excluded_from_evaluation`**. The target is an
outcome-informed Tornado Cash training address; its episode family is excluded
from evaluation. These captures establish present access to historical Ethereum
data, not historical RPC filtering, private exchange action, a full observation
window, a validated freeze transition, or an independently verified sanctions
trigger time. Human reference labels and error metrics remain pending.

The current source sidecar is
[`verified_panel.json`](../../sources/measurement_panel/verified_panel.json).
It supplements the protected proposed panel; it does not replace that panel or
constitute completed historical verification.

## Frozen runs and what they establish

| Directory | Scope and result | Interpretation |
| --- | --- | --- |
| `tornado_2022_readonly_v1/` | 30 queries across Flashbots and Alchemy; 15 valid responses, 15 gaps. Both return block 15307826 at **2022-08-09 11:52:24 UTC**, outside the predeclared August 8 slice. | Concrete mismatch between the legacy coded block and date; retain the failed setup. Flashbots' 13 contract/state/log queries returned HTTP 504; Alchemy returned those data. Valid contract responses in this run remain transport diagnostics because the date dependency failed. |
| `trigger_time_resolution_v1/` | Captured binary search for the **legacy-coded** 2022-08-08 13:30 UTC timestamp; block 15301834 is at 13:29:43 and 15301835 at 13:30:03. | Timestamp-to-block mapping, not verification of the sanctions trigger or a freeze. |
| `tornado_2022_readonly_v2/` | Amended, separately frozen slice 15301834–15301835; Alchemy returns 15/15 valid RPC responses with zero gaps. | Historical code, state, storage and narrow logs are technically accessible on this transport. Both sampled USDC and USDT blacklist states are zero and both two-block target log sets are empty. These narrow observations do not establish absence across the protocol window or a transition. |
| `log_range_feasibility_v1/` | Three predeclared USDC log spans: 10 succeeds; 1,000 and 10,000 return HTTP 400, twice each. | Public-endpoint error bodies advertise a **100-block maximum**; 100 was not itself tested. The captured generic keyed free-tier documentation gives 10, which must not be substituted for the observed public-endpoint error. |
| `publicnode_feasibility_v1/` | One additional official public transport: 1/10 queries valid (chain identity); the 2022 block returns a pruned-history error, earliest available block 15500000. Both issuer state requests and all six 10/1,000/10,000-block log requests return HTTP 403. | Independent historical reconciliation is unavailable in this environment. PublicNode is an auxiliary chain-data transport, not a new member of the studied RPC-provider panel. |

Every request attempt records exact request bytes, response bytes, response
headers, UTC retrieval time and SHA-256 hashes. Query manifests precede outcomes.
Failures receive at most two total attempts. Missing, malformed and rejected
responses are gaps, never negative enforcement observations. The original runs
are retained unchanged. In particular, v1 predates the collector-hash field; v2
binds its collector snapshot with SHA-256. Later parser hardening does not rewrite
either run or imply that they executed the newer source.

The v2 USDC implementation storage value resolves to
`0xa2327a938febf5fec13bacfb16ae10ecbc4cbdcf`; USDT's historical `deprecated()` and
`upgradedAddress()` returns are zero. Reading these slots does not reproduce
historical implementation bytecode or prove its ABI. That verification remains
required for evaluative measurement.

## Why full-window execution remains pending

A day-precision source date `d` yields the proposed half-open query interval
`[d−7 days, d+31 days)`: **38 days**, including date uncertainty. For planning
only, 12–14 seconds per block implies roughly 235,000–274,000 blocks. Separate
USDC and USDT log scans would require about 4,700–5,500 successful requests at the
public endpoint's advertised 100-block limit, or 47,000–55,000 at the directly
tested 10-block span, before retries, state checks, block-boundary searches and
independent reconciliation. Actual counts require resolved boundaries and a
verified range limit. At one request per second, the 100-block scenario alone is
roughly 1.3–1.5 hours; rate limits and failures can increase this. This is a
planning estimate, not a measured throughput or complete-window result.

No such scan was launched. The single auxiliary public transport tested here
cannot serve the required historical blocks. A broader historical log transport,
or a separately budgeted and throttled collection run with the current public
endpoint plus an independent archive source, is needed to complete the next
batch. Source-defined candidate manifests may be frozen before human review;
this pilot is not promoted into those candidates.

A separate [partial source-defined endpoint snapshot run](../issuer_candidate_snapshots/README.md)
subsequently collected four window-endpoint state words for the first frozen
nonpilot candidate. It does not close the full-window log or reconciliation gaps.

## Reuse and validation

The bounded collector refuses an existing output directory and allowlists only
read methods; it has no transaction method, credential input or paid-API path.

```sh
python3 scripts/measurement_pilot.py \
  --out-dir analysis/measurement_pilot/NEW_IMMUTABLE_RUN \
  --providers alchemy_public
python3 -m pytest -q tests/test_measurement_pilot.py
```

The tests cover bounded retries, captured hashes, missing chain identity,
malformed block and event values, non-indexed USDT event decoding, write-method
rejection, and invalid historical dependencies. **22 tests passed** after parser
hardening. Current runs remain small capability checks; there is no completed
full-window collector or full-cohort execution claim.
