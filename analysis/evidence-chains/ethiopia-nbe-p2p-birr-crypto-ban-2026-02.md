# Evidence chain — `ethiopia-nbe-p2p-birr-crypto-ban-2026-02`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Ethiopia's NBE (2026-02-27) prohibited Birr-denominated P2P cryptocurrency
> trading; the restriction is observed at the off-ramp service perimeter
> (direct, primary_government)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `National Bank of Ethiopia (NBE)`
- **Timestamp**: `2026-02-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://nbe.gov.et/nbe_news/public-notice-notice-on-illegal-birr-paired-peer-to-peer-p2p-transactions-via-trading-platforms/>
  - body_hash: `sha256:73c1003812f6be6226a3edaee3d437a84d45ea306cb9698367bcc79ad976b6f4`
  - body_path: `sources/http_captures/ethiopia-nbe-p2p-birr-crypto-ban-2026-02/source/nbe.gov.et__nbe_news-public-notice-notice-on-illegal-birr-paired-peer-to-peer-p2p-transactions-via-trading-platforms__55afed8a69.html`
  > Captured 2026-06-08 with body_hash; replayable local primary for the action.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `ethiopia_nbe_p2p_birr_crypto_ban_2026_02_reaction`

**Timestamp**: `2026-02-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://nbe.gov.et/nbe_news/public-notice-notice-on-illegal-birr-paired-peer-to-peer-p2p-transactions-via-trading-platforms/>
  - body_hash: `sha256:73c1003812f6be6226a3edaee3d437a84d45ea306cb9698367bcc79ad976b6f4`
  - body_path: `sources/http_captures/ethiopia-nbe-p2p-birr-crypto-ban-2026-02/source/nbe.gov.et__nbe_news-public-notice-notice-on-illegal-birr-paired-peer-to-peer-p2p-transactions-via-trading-platforms__55afed8a69.html`
  > Captured primary source documents the offramp-layer restriction; attribution direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

