# Evidence chain — `ethiopia-nbe-exchange-website-block-2025-11`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l0_network`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Ethiopia's NBE/FIS restricted access to crypto-exchange websites (Binance,
> OKX, Bybit) from ~late October 2025; an L0 network block (plausible,
> attested_secondary)."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `National Bank of Ethiopia (NBE) / Financial Intelligence Service (FIS)`
- **Timestamp**: `2025-10-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://addisinsight.net/2025/11/06/binance-confirms-talks-with-ethiopian-regulators-as-website-access-gets-restricted/>
  - body_hash: `sha256:0f879dd9a24d203ddbdf3aa6efe0eaee926c82c932a6ed5c1e76d49cb6f9ba07`
  - body_path: `sources/http_captures/ethiopia-nbe-exchange-website-block-2025-11/source/addisinsight.net__2025-11-06-binance-confirms-talks-with-ethiopian-regulators-as-website-access-gets-restricted__e31e7f4729.html`
  > Captured 2026-06-08 with body_hash; replayable contemporaneous secondary source.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

### l0_network · attribution: `plausible` · Δt = 0h

**Event label**: `isp_block_of_exchange_websites`

**Timestamp**: `2025-10-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://addisinsight.net/2025/11/06/binance-confirms-talks-with-ethiopian-regulators-as-website-access-gets-restricted/>
  - body_hash: `sha256:0f879dd9a24d203ddbdf3aa6efe0eaee926c82c932a6ed5c1e76d49cb6f9ba07`
  - body_path: `sources/http_captures/ethiopia-nbe-exchange-website-block-2025-11/source/addisinsight.net__2025-11-06-binance-confirms-talks-with-ethiopian-regulators-as-website-access-gets-restricted__e31e7f4729.html`
  > Ethiopia NBE/FIS restricted access to crypto-exchange websites
> (Binance, OKX, Bybit) from ~late October 2025. attribution plausible:
> news-reported, no first-party ISP/operator confirmation.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

