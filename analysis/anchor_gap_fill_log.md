# Anchor gap-fill log (Phase 3)

Per-cell reproducibility log for the Phase-3 gap-fill effort on anchor
cases. One row per (event × layer × attempt). Records:

- **target**: what evidence this attempt was trying to admit,
- **method**: how we looked (Wayback CDX query / OONI API / direct fetch),
- **result**: raw outcome (count of snapshots, captured artifact body_hash,
  or "not reachable"),
- **decision**: what we did with the result (admitted observation, updated
  coverage note, deferred, ruled out),
- **TODO**: the concrete next action if the gap remains open.

Goal: whether we admitted an observation or not, the *attempt* is on the
record. A future auditor can replay every CDX query, every fetch, every
hash — and reach the same verdict.

---

## Scope

Original Phase-3 anchors (n=5): `chatex-ofac-2021`, `cryptex-ofac-2024`,
`sec-v-binance-2023`, `tornado-cash-ofac-2022`,
`tornado-cash-ofac-delisting-2025`. Current admitted paper-facing anchor
worksheets are narrower: `cryptex-ofac-2024` and
`tornado-cash-ofac-2022`. `sec-v-binance-2023` is retained only as a draft
repair candidate after source-support review.

Target layers for this phase (per the Phase-3 roadmap):

- L3 RPC filter-list pre/post snapshots for `tornado-cash-ofac-2022` and
  `tornado-cash-ofac-delisting-2025`.
- Off-ramp or frontend direct artifacts for `cryptex-ofac-2024`,
  `chatex-ofac-2021`, and the draft repair candidate
  `sec-v-binance-2023`.
- L0 network via OONI/Censored Planet for a few high-value domains;
  everything else explicitly marked `measurement gap`.

Non-goals for this phase: fully backfill 53×6. The honest `not_measured`
framing is already defensible in the paper under coverage-denominator
discipline.

---

## 1. L0 network

### 1.1 `chatex-ofac-2021` · L0 — **done (null confirmed)**

- target: OONI volunteer measurements on `chatex.com`
  2021-10-08..2021-12-08.
- method: OONI public API via `scripts/ooni_batch_query.py`.
- result: 0 measurements returned.
- artifact: `sources/l0_datasets/chatex-ofac-2021/chatex.com__ooni.json`
  (`sha256:8d0875b6f857…`).
- decision: coverage stays `not_measured`; coverage note already cites
  the artifact as a documented measurement gap. No observation admitted
  (null query result does not satisfy the `observed_no_change` anchor
  rule by itself — OONI having zero measurements ≠ OONI having
  measurements showing no reachability change).
- TODO: if Censored Planet raw ingestion is later wired in, re-run.

### 1.2 `cryptex-ofac-2024` · L0 — **done (null confirmed)**

- target: OONI measurements on `cryptex.net` 2024-08-26..2024-10-26.
- method: OONI API.
- result: 0 measurements.
- artifact: `sources/l0_datasets/cryptex-ofac-2024/cryptex.net__ooni.json`
  (`sha256:e2a0dd9d0b0e…`).
- decision: same as 1.1 — coverage stays `not_measured` with the
  artifact cited.

### 1.3 `tornado-cash-ofac-2022` · L0 — **done (null confirmed)**

- target: OONI on `app.tornado.cash`, `tornado.cash`,
  `tornadocash.eth.link` 2022-07-15..2022-10-10.
- method: OONI API (3 domains × 1 window).
- result: 0 / 3 domains returned measurements.
- artifacts: three files under
  `sources/l0_datasets/tornado-cash-ofac-2022/*.json` with body_hashes
  already pinned in the coverage note.
- decision: coverage stays `not_measured`; note already complete.

### 1.4 `tornado-cash-ofac-delisting-2025` · L0 — **deferred**

- target: OONI on `tornado.cash`, `app.tornado.cash`,
  `classic-ui.tornado.ws`, `tornadosto.tech` in a reverse-cascade window
  (proposed 2025-02-21..2025-04-21).
- method: proposed — extend `scripts/ooni_domains.json` with
  event-specific entries, run `make ooni-scan`.
- result: not executed yet. The OONI query machinery currently assumes
  one domain → one slug → one window; the `tornado.cash` and
  `app.tornado.cash` rows collide with the 2022 event.
- decision: schema extension (one domain → list of `{slug, since, until}`
  records) is a small script refactor; deferred out of scope for this
  commit. Coverage note on the delisting event is refreshed to match
  the Phase-3 measurement-gap framing.
- TODO: refactor `ooni_domains.json` to allow per-slug windows; run
  OONI for the 4 domains above; commit artifact + patch coverage note.

### 1.5 `sec-v-binance-2023` · L0 — **not_applicable**

- SEC civil enforcement action with no network-layer expectation.
  Coverage is `not_applicable`; no gap to fill.

---

## 2. L3 RPC

### 2.1 `tornado-cash-ofac-delisting-2025` · L3 — **partial (docs anchors pinned; filter-list content out of Wayback coverage)**

- target: pre/post Wayback snapshots of MEV-Blocker and Flashbots
  Protect filter-list pages bracketing 2025-03-21.
- method: Wayback CDX queries on candidate URLs; capture via
  `scripts/capture_http_artifact.py`.
- CDX results (window 2025-03-01..2025-04-30):
  - `mevblocker.io/` — CDX timed out on repeated attempts; partial
    discovery only.
  - `docs.flashbots.net/flashbots-protect/overview` — 4 snapshots found
    (20250313180739, 20250405045312, 20250419052220, 20250427202621).
  - `docs.flashbots.net/flashbots-protect/quick-start` — 5 snapshots
    found; bodies 503 on replay for pre/post candidates.
  - `docs.flashbots.net/flashbots-protect/additional-documentation/ofac`
    — **0 snapshots** in window.
  - `docs.flashbots.net/flashbots-protect/faq` — CDX timed out.
  - `docs.flashbots.net/flashbots-auction/overview` — 3 snapshots
    (support page, not filter-list).
  - `github.com/flashbots/rpc-endpoint/blob/main/application/blacklist.go`
    — **0 snapshots** (GitHub generally resists Wayback).
- artifacts captured:
  - `sources/http_captures/tornado-cash-ofac-delisting-2025/l3-wayback-brackets/web.archive.org__web-20250313180739-…overview__cb454aae12.html`
    (`sha256:1592ba0b485a20ed697c29f09c3031c309d362381177a97613157b138989d410`;
    `x-archive-orig-last-modified: 2025-03-12T21:03:49Z`).
  - `sources/http_captures/tornado-cash-ofac-delisting-2025/l3-wayback-brackets/web.archive.org__web-20250405045312-…overview__2fe331d183.html`
    (`sha256:b258da6dc24ea8b8ee351803a52e9cd92ca59b579c9a6876f2dcd68b1bcdf9c9`;
    `x-archive-orig-last-modified: 2025-04-04T18:45:04Z`).
- decision: the captured overview snapshots **do not** publish the
  OFAC filter list itself — visible body content is a generic MEV
  protection description and contains no OFAC / sanction / Tornado
  tokens. They serve only as pinned provider-docs anchors for the
  delisting window. The real filter-list source is
  `flashbots/rpc-endpoint/blacklist.go` on GitHub (git-history
  analysis, not Wayback). No new `observed_change` or `observed_no_change`
  observation admitted; coverage stays `partially_measured` with the
  existing `observed_no_change` row on MEV-Blocker plus a refreshed
  coverage note pointing at the two new anchors.
- TODO: clone `flashbots/rpc-endpoint` and diff
  `application/blacklist.go` between commits bracketing 2025-03-21 to
  confirm whether `0xc09e...` (Tornado-associated pool addresses) were
  removed from the blacklist. That git-history diff can then be
  admitted as a `primary_corporate` source for a concrete
  `observed_change` or `observed_no_change` row.

### 2.2 `tornado-cash-ofac-2022` · L3 — **confirmed not_applicable**

- target: user asked for L3 filter-list pre/post for this event too.
- method: architectural review of the L3 landscape at 2022-08-08:
  Flashbots Protect launched 2022-11-03 (post-Merge, post-event);
  MEV-Blocker launched 2023-03-27 (well after event). Infura's
  OFAC-screening policy statement came 2022-08-12 (4 days post-event)
  and was enforcement-level, not a filter list. Alchemy had no public
  filter policy in 2022.
- decision: `not_applicable` stands — the L3-as-filter-list construct
  did not exist at 2022-08-08. Coverage note already explains this
  ("Pre-Merge event… construct-did-not-exist reasoning"). A Git-history
  analysis of `flashbots/rpc-endpoint` is **not** applicable here
  because the endpoint did not exist. For completeness, a single
  observation pointing to Infura's 2022-08-12 policy statement as
  `observed_change` on L3 at `delta_hours ≈ 96` could be admitted if a
  Wayback snapshot is recovered; this is deferred.
- TODO (low priority): capture Infura's 2022-08-12 OFAC-screening
  statement from Wayback (if snapshotted). If so, L3 coverage promotes
  from `not_applicable` to `partially_measured` with an
  `observed_change`/`plausible` row. Otherwise leave `not_applicable`.

### 2.3 `cryptex-ofac-2024` · L3 — **no event-bracketing Wayback coverage**

- target: pre/post Wayback snapshots of MEV-Blocker / Flashbots Protect
  docs bracketing 2024-09-26.
- method: (not executed in this session — prioritized delisting over
  cryptex for the demo).
- decision: existing coverage note already names the ecosystem anchors.
  Promoting to `partially_measured` would need CDX queries in the
  2024-08-26..2024-10-26 window + capture. Low priority: cryptex's
  archetype is `asset_onchain+l4_frontend`; an L3 row would not
  change its classification.
- TODO: CDX + capture the same four Flashbots Protect / MEV-Blocker
  URLs for the cryptex window. Same null-coverage risk as 2.1.

### 2.4 Other anchors · L3 — **not_applicable**

- `chatex-ofac-2021` — pre-MEV-Blocker era.
- `sec-v-binance-2023` — SEC civil enforcement, no L3 expectation.

---

## 3. Off-ramp CEX

### 3.1 `chatex-ofac-2021` · offramp_cex — **deferred (needs primary-source URLs)**

- target: post-2021-11-08 CEX delisting / freeze responses naming
  Chatex or Chatex's SDN-listed addresses (Binance, Huobi, Coinbase,
  Bitfinex, Gemini).
- method: search each exchange's 2021-Q4 press releases, ToS pages, and
  compliance feed archives via Wayback.
- result: not executed.
- decision: deferred — this requires per-exchange targeted search that
  is better done with user-validated primary-source URLs than
  autonomous guessing.
- TODO: user supplies a candidate URL list (e.g. Binance listings
  announcement feed 2021-Q4, Huobi delisting feed 2021-Q4, Chainalysis
  Chatex-specific advisory). Script can then batch-capture + patch.

### 3.2 `cryptex-ofac-2024` · offramp_cex — **deferred (same)**

- target: CEX responses to 2024-09-26 SDN (Cryptex is a
  foreign-operated exchange; CEX response is how US-facing exchanges
  handled addresses tied to Cryptex).
- TODO: same pattern as 3.1.

### 3.3 `sec-v-binance-2023` · offramp_cex — **demoted to draft repair candidate**

- Current state after 2026-05-06 review: coverage `not_measured`,
  `observations: []`, `status: draft`. The SEC legal trigger is pinned, but
  legal-source-only evidence is not enough to admit a Binance.US
  platform / banking-rail state transition.
- TODO: attach primary corporate, banking-rail, or independently observable
  platform artifacts before any L4/off-ramp claim is admitted.

### 3.4 `tornado-cash-ofac-2022` · offramp_cex — **already `partially_measured` with direct observation**

- Current state: coverage `partially_measured` with
  `observed_change`/`direct`/`exchange:dydx`. The dYdX freeze/delisting
  is the canonical cited CEX response.
- TODO: optional — capture a second exchange's response (e.g. Aave's
  2022-08-09 address freeze) to broaden the off-ramp claim.

### 3.5 `tornado-cash-ofac-delisting-2025` · offramp_cex — **deferred (and expected null)**

- target: CEX responses to the 2025-03-21 delisting. Most venues do
  NOT re-list sanctioned assets post-delisting (the asset already
  left their systems in 2022). Expected result: null cascade on
  the off-ramp side for the delisting event.
- TODO: capture statements from 1-2 major CEXes confirming they did
  not alter their Tornado-related policies post-delisting; admit as
  `observed_no_change` if anchors allow.

---

## 4. Summary of this session's admitted changes

**First pass** (web / Wayback only):

| artifact | event | decision |
| --- | --- | --- |
| 2 Flashbots Protect overview Wayback captures (pre/post delisting) | `tornado-cash-ofac-delisting-2025` | pinned as anchors in L3 coverage note; no observation admitted |
| L0 coverage-note refresh | `tornado-cash-ofac-delisting-2025` | measurement-gap framing matches the other 3 anchors |

**Second pass** (git-history analysis of `flashbots/rpc-endpoint`):

The cloned repo reveals two event-local primary_corporate artifacts
that the prior web-only searches had missed:

- Commit `92ab6b1f` (2022-08-08 16:20:50 UTC, 2h 50m after the
  Tornado SDN at 13:30 UTC): PR #90 "update ofac black list" adds
  Tornado Cash pool addresses `0x722122df`, `0x8589427`,
  `0x4736dcf1`, etc. to `server/ofacblacklist.go`. This is a
  `primary_corporate` source strong enough for `direct` attribution on
  an L3 `observed_change` row.
- Commit `1e9c29c` (2025-04-01 19:28:21 UTC, 11d 19h 28m after
  the Tornado delisting): PR #173 "Cleanup unused, outdated blacklist
  defaults" deletes the entire `ofacBlacklist` map (132 addresses → 0).
  `primary_corporate` source; attribution `plausible` because the PR
  title frames the deletion as operational cleanup rather than a
  direct response to the delisting.

Captured artifacts:

- `sources/operator_commits/tornado-cash-ofac-2022/`:
  `ofacblacklist-at-92ab6b1.go` (body_hash `86c81be4…`),
  `commit-92ab6b1.meta.txt` (body_hash `0c4fafa0…`),
  `commit-92ab6b1.diff` (body_hash `220a5d31…`).
- `sources/operator_commits/tornado-cash-ofac-delisting-2025/`:
  `ofacblacklist-pre-1e9c29c.go` (body_hash `9f609132…`, 132 addresses),
  `ofacblacklist-at-1e9c29c.go` (body_hash `429579b6…`, 0 addresses),
  `commit-1e9c29c.meta.txt` (body_hash `75c7c402…`),
  `commit-1e9c29c.diff` (body_hash `d8194686…`).

Event-YAML edits:

| event | edit | derived impact |
| --- | --- | --- |
| `tornado-cash-ofac-2022` | L3 coverage: `not_applicable` → `partially_measured`. Note rewritten to acknowledge the earlier framing was incomplete (flashbots/rpc-endpoint existed at event time). | l3_rpc applicable: 8 → 9; changed(partial): 0 → 1 |
| `tornado-cash-ofac-2022` | new L3 observation: `observed_change` / `direct` / `flashbots_rpc_endpoint` / `ofac_blacklist_addition_of_tornado_pool_addresses` at `2022-08-08T16:20:50Z` (delta 2.85h). Two primary_corporate sources grouped under `flashbots-ofacblacklist-2022-08-08`. | changed_layer_count 4 → 5; signature becomes `asset_onchain+l1_consensus+l3_rpc+l4_frontend+offramp_cex` — broadest cascade in corpus |
| `tornado-cash-ofac-2022` | `time_to_first_change_hours` moves from 5.93h (asset_onchain) to 2.85h (new L3 row); still in `acute` latency band. | Table 4 Panel A bucket unchanged — stays in (1, 6]h |
| `tornado-cash-ofac-delisting-2025` | new L3 observation: `observed_change` / `plausible` / `flashbots_rpc_endpoint` / `ofac_blacklist_deletion` at `2025-04-01T19:28:21Z` (delta 283.47h). | changed_layer_count 3 → 4; signature becomes `asset_onchain+l1_consensus+l3_rpc+l4_frontend`; changed(partial) on l3_rpc: 0 → 2 |
| `tornado-cash-ofac-delisting-2025` | L0 + L3 coverage notes refreshed (first pass) plus L3 note extended to reference the new observation (second pass). | No coverage status change. |

Corpus-level impact: layer_observability counts retain two named Flashbots
partial L3 observations. Current paper-facing tables deliberately suppress an
L3 conditional rate because `l3_rpc` has no measured denominator. Earlier
draft language that reported `l3_rpc::changed_given_measured_or_partial` as a
rate is superseded: the C1 phrasing is now "two named Tornado-related
Flashbots observations; no L3 conditional rate." Archetype counts are derived
from admitted events only and should be read from `derived/archetype_distribution.md`.

## 5. Phrasing updates required in paper_claims.md

The new L3 evidence means C1 and C2 need light touch-up:

- **C1** (upper-layer concentration): add a sentence noting that
  `l3_rpc` now carries 2 observed changes (both Tornado) under
  partial-coverage discipline; the upper-layer dominance claim holds
  but the "zero L3 changes" qualifier from earlier drafts is no
  longer accurate.
- **C2** (single-layer dominance): unchanged — 35/53 single-layer
  still holds; the broader Tornado-2022 signature is a multi_layer
  event already. The new 5-layer signature does not flip the
  archetype.
- **C3 / C4** (latency distribution, trigger-is-action): unaffected;
  tornado-2022 stays hour-precision and stays in Panel A (1,6]h.
- **C5** (cross-stratum archetype presence): unchanged.
- **C6** (recovery n=1): unchanged.

No hardcoded numbers in `paper_claims.md` require editing because
C4 / §3.5 already delegate counts to Table 4.

## 5. Phase-3 priorities if you want to push further

Ordered by ROI for the paper:

1. Refactor `scripts/ooni_domains.json` to allow per-slug windows, then
   run OONI for `tornado-cash-ofac-delisting-2025`. Produces a pinned
   null artifact matching the other three anchors.
2. Git-history diff `flashbots/rpc-endpoint::blacklist.go` across
   2025-03-21. If Tornado addresses are removed in a commit within the
   event window, admit an `observed_change`/`direct` row on L3 for the
   delisting event. This single commit-level primary source would
   change the L3 archetype signature for the delisting event.
3. User-directed off-ramp primary sources for chatex / cryptex
   (3.1 / 3.2). Each admitted observation would promote the anchor
   from `cex_only=0` to `cex_only=1` in its archetype signature.

Everything below that is marginal — the paper's C1 / C2 / C5 claims
do not depend on anchor-specific cell changes; they depend on
corpus-level aggregates that are already stable.
