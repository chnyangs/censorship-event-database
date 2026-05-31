# Evidence chain — `sec-v-coinbase-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-06` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SEC v. Coinbase is admitted only for a state-scoped Coinbase staking-service
> restriction; the dataset does not claim a Coinbase.com frontend takedown,
> named-token delisting, fiat-rail disruption, or on-chain effect."

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
- **`primary_corporate`**
  - URL: <https://www.coinbase.com/en-ca/blog/why-we-stand-by-staking>
  - body_hash: `sha256:90b5347eccdde2b60faa6097865251cc86e387e6ff04dbedf59f0dddd7d752cb`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/platform-response/www.coinbase.com__en-ca-blog-why-we-stand-by-staking__c655f5d8a8.html`
  > Coinbase post "Why we stand by staking" (2023-07-14) corroborates the
> 2023-06-06 SEC lawsuit date and records same-day state securities
> proceedings against Coinbase's retail staking services. Used here as
> the platform-side source for the scoped staking-service reaction below.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Coinbase Inc / Coinbase Global
- **Canonical domains**: `coinbase.com`, `pro.coinbase.com`

> Coinbase, Inc. + Coinbase Global, Inc. entity-level action. 13 tokens
> named as securities: SOL, ADA, MATIC, FIL, SAND, AXS, CHZ, FLOW, ICP,
> NEAR, VGX, DASH, NEXO. Staking service explicitly named as unregistered
> security. No on-chain addresses; securities-law at token/entity level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 912h

**Event label**: `retail_staking_new_funds_restricted_in_four_states`

**Timestamp**: `2023-07-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.coinbase.com/en-ca/blog/why-we-stand-by-staking>
  - body_hash: `sha256:90b5347eccdde2b60faa6097865251cc86e387e6ff04dbedf59f0dddd7d752cb`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/platform-response/www.coinbase.com__en-ca-blog-why-we-stand-by-staking__c655f5d8a8.html`
  > Coinbase states that state securities agencies opened same-day
> proceedings on 2023-06-06 and that California, New Jersey, South
> Carolina, and Wisconsin required service changes: customers in those
> states would be unable to stake additional assets while proceedings
> remained pending.
- **`primary_corporate`**
  - URL: <https://www.sec.gov/Archives/edgar/data/1679788/000167978823000106/coin-20230630.htm>
  - body_hash: `sha256:9ebcd65594f67d94e777a94f3427915d1161f72c2b28a24451592835de770f1b`
  - body_path: `sources/http_captures/sec-v-coinbase-2023/platform-response/www.sec.gov__Archives-edgar-data-1679788-000167978823000106-coin-20230630.htm__fc0eb009da.html`
  > Coinbase Q2 2023 Form 10-Q states that in July 2023 Coinbase entered
> agreements with state securities regulators in California, New
> Jersey, South Carolina, and Wisconsin under which customers in those
> states would no longer be able to stake new funds pending final
> adjudication.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): The SEC filing does not establish an L4 no-change observation. A

## 7. Related events

- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

