# Evidence chain — `kraken-uk-derivatives-exit-2021`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a09b90d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Kraken Futures (Crypto Facilities Ltd) restricted UK retail customer
> access to crypto-derivatives products on or around 2021-01-06 in
> compliance with the FCA PS20/10 prohibition, retaining access only for
> customers categorised as Professional Clients under COBS 3. Primary
> observational axis is offramp_cex at the UK-retail-cohort level;
> attribution=plausible because the FCA prohibition is class-wide rather
> than Kraken-specific."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `KRAKEN_PAYWARD`
- **Timestamp**: `2021-01-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://support.kraken.com/articles/futures-trading-for-clients-in-the-united-kingdom>
  - Wayback: <https://web.archive.org/web/2021*/support.kraken.com/hc/en-us/articles/futures-trading-for-clients-in-the-united-kingdom>
  > Kraken support article "Becoming a Professional Client in the UK"
> (Kraken Futures / Crypto Facilities Ltd). Documents Kraken's
> compliance response to the FCA PS20/10 prohibition on the sale,
> marketing and distribution of crypto-derivatives to UK retail
> consumers (effective 2021-01-06): UK retail clients are restricted
> from derivatives access, and derivatives trading is available only
> to clients categorised as Professional Clients under COBS 3 of the
> FCA Handbook. DRYRUN: Wayback URL pattern asserted; pinned body-hash
> capture deferred.
- **`primary_corporate`**
  - URL: <https://support.kraken.com/articles/changes-for-clients-residing-in-the-united-kingdom>
  - Wayback: <https://web.archive.org/web/2021*/support.kraken.com/hc/en-us/articles/changes-for-clients-residing-in-the-united-kingdom>
  > Kraken support article "Changes for Clients Residing in the United
> Kingdom" -- enumerates Kraken's UK customer-facing changes following
> the FCA ban. Companion compliance notice. Wayback pinned capture
> deferred for DRYRUN.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Kraken Futures / Crypto Facilities Ltd
- **Canonical domains**: `futures.kraken.com`, `kraken.com`

> UK-resident retail customer cohort of Kraken Futures (operated by
> Crypto Facilities Ltd, the FCA-authorised Kraken subsidiary). The
> enumeration is subset because the named target is the class of UK
> retail customers (not an enumerable individual account list);
> Professional Clients under COBS 3 remained eligible.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `uk_retail_derivatives_access_restricted_to_professional_clients`

**Timestamp**: `2021-01-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://support.kraken.com/hc/en-us/articles/futures-trading-for-clients-in-the-united-kingdom>
  - Wayback: <https://web.archive.org/web/20240804114616/https://support.kraken.com/hc/en-us/articles/futures-trading-for-clients-in-the-united-kingdom>
  - body_hash: `sha256:e98ed381893bca02ae4f75c00f5122fe19f4ed1c62c891062c086f171d1a35e4`
  - body_path: `sources/http_captures/kraken-uk-derivatives-exit-2021/primary/web.archive.org__web-20210701000000-https-support.kraken.com-hc-en-us-articles-futures-trading-for-clients-in-the-united-kingdom__5703cadeee.html`
  > Kraken support article on futures/derivatives trading restrictions
> for UK clients following the FCA's 2021 retail crypto-derivatives ban.
> primary_corporate anchor. Wayback 20240804114616 pinned.
- **`semi_primary_wayback`**
  - URL: <https://blockchain.news/news/uk-financial-watchdog-fca-bans-crypto-derivatives-trading-for-retail-investors>
  - Wayback: <https://web.archive.org/web/20210420072434/https://blockchain.news/news/uk-financial-watchdog-fca-bans-crypto-derivatives-trading-for-retail-investors>
  - body_hash: `sha256:560566f07cc84c3ef64e0358e03f588a55e4b81f6be21888a6909f6a63bef4e8`
  - body_path: `sources/http_captures/kraken-uk-derivatives-exit-2021/primary/web.archive.org__web-20210701000000-https-blockchain.news-news-uk-financial-watchdog-fca-bans-crypto-derivatives-trading-for-retail-investors__6a2519e0d5.html`
  > Blockchain.news coverage of the FCA retail crypto-derivatives ban
> driving the Kraken UK derivatives exit. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a09b90d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

