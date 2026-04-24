# Evidence chain — `sec-v-coinbase-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.1.0` · **Dataset cutoff**: `2026-04-22` · **Source commit**: `930f3d6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-04-24T03:27:37Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SEC v. Coinbase (2023-06-06) paired with SEC v. Binance (2023-06-05)
> constitutes the SEC crypto-enforcement opening. Divergent cascade
> outcomes — Coinbase.com remained operational while Binance.US fiat-rails
> collapsed — track with the asset-freeze-motion inclusion asymmetry
> between the two filings. First mention of Solana and Polygon tokens at
> enforcement-event level in the dataset."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-06-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-102>
  - body_hash: `sha256:63c2b4104f2509b022f0154b51f5a2444139d54d1292b3b35d06b7dbe6abc747`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/primary/www.sec.gov__news-press-release-2023-102__783dc1be7f.html`
  > SEC press release 2023-102 (2023-06-06): "SEC Charges Coinbase for
> Operating as an Unregistered Securities Exchange, Broker, and Clearing
> Agency." Civil action in SDNY. Key securities allegations: Coinbase
> operated as an unregistered national securities exchange, broker, and
> clearing agency since at least 2019, including offering Coinbase Stake
> as unregistered security. 13 tokens specifically named as securities
> in the complaint: SOL, ADA, MATIC, FIL, SAND, AXS, CHZ, FLOW, ICP,
> NEAR, VGX, DASH, NEXO. Filed one calendar day after SEC v. Binance
> 2023-06-05 — paired SEC offensive.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Coinbase Inc / Coinbase Global
- **Canonical domains**: `coinbase.com`, `pro.coinbase.com`

> Coinbase, Inc. + Coinbase Global, Inc. entity-level action. 13 tokens
> named as securities: SOL, ADA, MATIC, FIL, SAND, AXS, CHZ, FLOW, ICP,
> NEAR, VGX, DASH, NEXO. Staking service explicitly named as unregistered
> security. No on-chain addresses; securities-law at token/entity level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `coinbase_staking_suspended_for_us_customers_same_day`

**Timestamp**: `2023-06-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-102>
  - body_hash: `sha256:63c2b4104f2509b022f0154b51f5a2444139d54d1292b3b35d06b7dbe6abc747`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/primary/www.sec.gov__news-press-release-2023-102__783dc1be7f.html`
  > SEC charged Coinbase Stake as unregistered security; Coinbase
> suspended the staking service for US customers same day. Direct
> attribution: SEC filing explicitly named staking as the
> securities-registration violation.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-102>
  - body_hash: `sha256:63c2b4104f2509b022f0154b51f5a2444139d54d1292b3b35d06b7dbe6abc747`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/primary/www.sec.gov__news-press-release-2023-102__783dc1be7f.html`
  > Second reference — SEC complaint identifies the 13 named securities
> (SOL, ADA, MATIC, etc.); Coinbase continued listing them on US
> platform despite SEC position, creating an asymmetric stance vs
> Binance.US's more accommodating fiat-rail suspension.

## 4. No-change observations (where applicable)

### l4_frontend — `canonical_frontend_remained_operational_through_sec_action`

**Window**: `2023-06-06 00:00:00+00:00` → `2023-06-20 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-102>
  - body_hash: `sha256:63c2b4104f2509b022f0154b51f5a2444139d54d1292b3b35d06b7dbe6abc747`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/primary/www.sec.gov__news-press-release-2023-102__783dc1be7f.html`
  > SEC action sought no asset-freeze against Coinbase (unlike Binance
> 2023-06-05). Coinbase.com remained operational; US customers could
> continue trading. Non-takedown is the paper-relevant observation —
> SEC civil action does not uniformly produce L4 cascade.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-102>
  - body_hash: `sha256:63c2b4104f2509b022f0154b51f5a2444139d54d1292b3b35d06b7dbe6abc747`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/primary/www.sec.gov__news-press-release-2023-102__783dc1be7f.html`
  > Second anchor to same SEC filing; confirms no asset-freeze relief
> was requested (contrast with 2023-06-05 Binance filing).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.1.0` (commit `930f3d6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

