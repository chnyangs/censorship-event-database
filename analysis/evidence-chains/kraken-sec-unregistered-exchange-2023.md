# Evidence chain — `kraken-sec-unregistered-exchange-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ff0c8be` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:07:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-11-20 SEC unregistered-exchange action against Kraken is retained
> as a null-control comparator: the SEC action occurred, Kraken issued a
> same-day response stating that client products and services continued, and
> the dataset does not admit any Kraken frontend takedown, token delisting,
> fiat-rail disruption, on-chain asset freeze, or L1/L3 effect for this event."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-237>
  - body_hash: `sha256:54d889d68c895c04a684b3b1272203287842228a1c8fe24931437185f388430a`
  - body_path: `sources/http_captures/kraken-sec-unregistered-exchange-2023/primary/www.sec.gov__news-press-release-2023-237__a3b13547f9.html`
  > SEC press release 2023-237, dated 2023-11-20, announcing the civil
> action against Payward Inc. and Payward Ventures Inc. for allegedly
> operating Kraken as an unregistered securities exchange, broker,
> dealer, and clearing agency. Captured locally 2026-06-01 with
> replayable body_hash/body_path. This is the legal trigger; it is
> distinct from the February 2023 Kraken staking settlement.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Kraken / Payward Inc. + Payward Ventures Inc.
- **Canonical domains**: `kraken.com`, `blog.kraken.com`

> Payward Inc. and Payward Ventures Inc., the two Kraken operating entities
> named in the SEC complaint. The action is an entity-level securities-law
> registration case, not a token delisting, frontend block, fiat-rail
> cutoff, or on-chain asset action.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_contemporaneous_kraken_service_withdrawal_after_sec_unregistered_exchange_complaint`

**Window**: `2023-11-20 00:00:00+00:00` → `2023-12-20 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-237>
  - body_hash: `sha256:54d889d68c895c04a684b3b1272203287842228a1c8fe24931437185f388430a`
  - body_path: `sources/http_captures/kraken-sec-unregistered-exchange-2023/primary/www.sec.gov__news-press-release-2023-237__a3b13547f9.html`
  > REJECTION/NULL-control legal trigger anchor. The SEC source
> establishes the enforcement action and target entities, but does not
> identify a Kraken service withdrawal, frontend block, fiat-rail
> cutoff, or on-chain asset action.
- **`primary_corporate`**
  - URL: <https://blog.kraken.com/news/kraken-continues-to-fight-for-its-mission-and-crypto-innovation-in-the-united-states>
  - body_hash: `sha256:2d1f67aa6b9412788d49bc3a4952918c315672168cc1bf5a1bfce067e66cbb70`
  - body_path: `sources/http_captures/kraken-sec-unregistered-exchange-2023/primary/blog.kraken.com__news-kraken-continues-to-fight-for-its-mission-and-crypto-innovation-in-the-united-states__eb2c51915d.html`
  > Kraken's same-day corporate response to the SEC complaint states
> that the action did not change the products or client services then
> offered by Kraken. Used here as replayable support for observed
> no-change, not as a positive observed_change event.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade kraken.com service-page or supported-asset frontend

## 7. Related events

- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`sec-v-bittrex-2023`](./sec-v-bittrex-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ff0c8be`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

