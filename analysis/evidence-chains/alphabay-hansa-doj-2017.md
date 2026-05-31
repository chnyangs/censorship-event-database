# Evidence chain — `alphabay-hansa-doj-2017`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c86ca57` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2017 AlphaBay/Hansa Operation Bayonet row is coded only for public
> marketplace/platform shutdown; it does not claim transaction-level on-chain
> asset movement."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ`
- **Timestamp**: `2017-07-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/alphabay-largest-online-dark-market-shut-down>
  - body_hash: `sha256:4f90921a411efba76eb17c1320af8c9ee1950288c76b7583a6b1c8ac329d7638`
  - body_path: `sources/http_captures/alphabay-hansa-doj-2017/primary/www.justice.gov__opa-pr-alphabay-largest-online-dark-market-shut-down__afe1f984e7.html`
  > DOJ announcement of the AlphaBay seizure and shut-down, with Hansa
> market also identified as taken down through coordinated international
> law-enforcement action.
- **`primary_legal`**
  - URL: <https://www.fbi.gov/news/stories/alphabay-takedown>
  - body_hash: `sha256:89078288ae4abe8f80852eb1fe2d3bb15d6781611a51fcf396fdb7f205281970`
  - body_path: `sources/http_captures/alphabay-hansa-doj-2017/primary/www.fbi.gov__news-stories-alphabay-takedown__675e2f71fc.html`
  > FBI public case story for the AlphaBay takedown. Used as a second
> primary government source for the public takedown narrative.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: AlphaBay and Hansa
- **Chains**: `bitcoin`, `monero`, `ethereum`

> AlphaBay and Hansa darknet marketplaces as a joint Operation Bayonet
> public takedown unit. This row does not enumerate every marketplace wallet
> or seized server.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `darknet_marketplaces_seized_and_shut_down`

**Timestamp**: `2017-07-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/alphabay-largest-online-dark-market-shut-down>
  - body_hash: `sha256:4f90921a411efba76eb17c1320af8c9ee1950288c76b7583a6b1c8ac329d7638`
  - body_path: `sources/http_captures/alphabay-hansa-doj-2017/primary/www.justice.gov__opa-pr-alphabay-largest-online-dark-market-shut-down__afe1f984e7.html`
  > DOJ announcement describes AlphaBay as seized and shut down, and
> identifies coordinated action against Hansa.
- **`primary_legal`**
  - URL: <https://www.fbi.gov/news/stories/alphabay-takedown>
  - body_hash: `sha256:89078288ae4abe8f80852eb1fe2d3bb15d6781611a51fcf396fdb7f205281970`
  - body_path: `sources/http_captures/alphabay-hansa-doj-2017/primary/www.fbi.gov__news-stories-alphabay-takedown__675e2f71fc.html`
  > FBI source corroborates the public takedown framing and cryptocurrency
> marketplace context.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): DOJ/FBI sources describe cryptocurrency possession and seizures, but this

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c86ca57`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

