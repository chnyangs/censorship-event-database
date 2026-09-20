# Partial issuer endpoint snapshots

`garantex_2022_first_batch_v1/` is **source-defined partial collection**, separate
from the excluded Tornado Cash feasibility pilot. Before the first request, its
manifest bound the frozen candidate batch, complete candidate bundle index,
panel sidecar, collector source and transport library with SHA-256 hashes. The
candidate selection rule was earliest source-eligible nonpilot action, without
looking at issuer outcomes. The original candidate bundle remains unchanged and
human eligibility adjudication remains pending.

The selected source is the [OFAC action dated 2022-04-05](https://ofac.treasury.gov/recent-actions/20220405),
with one normalized Ethereum address crossed with canonical USDC and USDT:
`0x7ff9cfad3877f21d41da833e2f775db0569ee3d9`.
Day-precision trigger uncertainty gives the window
`[2022-03-29T00:00:00Z, 2022-05-06T00:00:00Z)`.

The bounded collector made **58 read queries, all with valid RPC responses on
the first HTTP attempt**, through the documented Alchemy public endpoint. It
verified mainnet identity, captured adjacent-block timestamp boundaries, read
historical canonical contract code and proxy/forwarding values, checked nonempty
USDC implementation code, and read four target blacklist words. No log sweep,
transaction submission, key, paid API, historical RPC behavior, or exchange
account behavior is involved.

| Snapshot | Block | UTC timestamp | USDC returned word | USDT returned word |
| --- | ---: | --- | ---: | ---: |
| First block in the window | 14477774 | 2022-03-29 00:00:02 | 0 | 0 |
| Last block before the exclusive end | 14720258 | 2022-05-05 23:59:52 | 1 | 0 |

Both USDC endpoint reads resolve the implementation storage address to
`0xa2327a938febf5fec13bacfb16ae10ecbc4cbdcf`. Both USDT endpoint reads return zero
for `deprecated()` and the zero address for `upgradedAddress()`. These code and
storage checks do not independently reproduce historical implementation bytecode
or validate its ABI. The returned words are retained as partial evidence with
that limitation. In particular, USDT's two zero words do **not** establish that
it took no action within the window; a temporary state change could lie between
the snapshots. The USDC words do not establish an action timestamp, causal link
to sanctions, or a complete transition history.

`summary.json` therefore keeps full-window logs, full-cohort execution, independent
chain reconciliation and human reference completion false, and leaves the
full-window response classification null. Eligibility, historical ABI verification,
independent chain reconciliation, and complete event histories remain required
before using these units for response rates or measurement-error estimates.

The resolved interval contains **242,485 blocks**. Separate issuer scans require
4,850 successful log queries at Alchemy public's advertised 100-block limit, or
48,498 at the directly tested 10-block span, before retries and reconciliation.
The 100-block limit comes from captured API error bodies, not a successful
100-block probe. No full scan was launched. See the
[feasibility report](../measurement_pilot/README.md) for range limits and the
single auxiliary transport's historical-access failure.

Reusing the collector requires a new run directory:

```sh
python3 scripts/collect_issuer_snapshots.py \
  --out-dir analysis/issuer_candidate_snapshots/NEW_IMMUTABLE_RUN
python3 -m pytest -q tests/test_collect_issuer_snapshots.py tests/test_measurement_pilot.py
```

The collector caps execution at 80 logical read queries and two total attempts
per query, verifies the candidate bundle before network access, and stops with
explicit gaps if chain identity, block bounds, historical code or forwarding
checks fail. The tests cover bundle tampering, immutable outputs, boundary
semantics, budget exhaustion and retention of incomplete classifications.
The combined focused suite passed **25 tests**.
