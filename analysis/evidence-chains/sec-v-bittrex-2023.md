# Evidence chain — `sec-v-bittrex-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `939a17f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:50:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SEC v. Bittrex (2023-04-17) is admitted only for the Bittrex US
> exchange/off-ramp wind-down + Chapter 11 freeze; the dataset does not claim
> a measured L4 frontend takedown, named-token delisting, L1/L3 effect, or
> on-chain asset freeze."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-04-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-78>
  - body_hash: `sha256:0972b223df1e70a3ed0e7878a412f78b44d5d178097da04938d37aef9505568a`
  - body_path: `sources/http_captures/sec-v-bittrex-2023/primary/www.sec.gov__news-press-release-2023-78__8f8cebb461.html`
  > SEC press release 2023-78 (2023-04-17): "SEC Charges Crypto Asset
> Trading Platform Bittrex and its Former CEO for Operating an
> Unregistered Exchange, Broker, and Clearing Agency." Civil action in
> WDWA naming Bittrex Inc., Bittrex Global GmbH, and former CEO William
> Shihara. Allegations: operating an unregistered national securities
> exchange / broker / clearing agency from 2014 through 2022; coaching
> token issuers to delete public statements likely to draw SEC scrutiny.
> Filed 17 days after Bittrex announced US-exit (2023-03-31) and 21
> days before Bittrex Inc. filed Chapter 11 (2023-05-08). Direct
> precursor to SEC v. Binance (2023-06-05) and SEC v. Coinbase
> (2023-06-06) — same unregistered-exchange/broker/clearing theory.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/complaints/2023/comp-pr2023-78.pdf>
  - body_hash: `sha256:289268cccf208638f62642fa5e7c36ee18b79eae19dd051c74c78068540cb2aa`
  - body_path: `sources/http_captures/sec-v-bittrex-2023/primary/www.sec.gov__litigation-complaints-2023-comp-pr2023-78.pdf__7d9d537543.bin`
  > SEC v. Bittrex Inc. et al. complaint PDF (WDWA, filed 2023-04-17).
> Captured as the legal-pleading anchor for the unregistered-exchange /
> broker / clearing-agency charges and the six named tokens
> (OMG, DASH, ALGO, TKN, NGC, IHT) described as crypto asset securities.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Bittrex Inc / Bittrex Global GmbH / William Shihara
- **Canonical domains**: `bittrex.com`, `global.bittrex.com`

> Bittrex Inc. (US) + Bittrex Global GmbH (Liechtenstein) + William Shihara
> (former CEO) entity / individual action. Six tokens named in the complaint
> as unregistered crypto asset securities: OMG, DASH, ALGO, TKN, NGC, IHT.
> No on-chain addresses; securities-law charges operate at
> exchange-registration / token-offering level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 312h

**Event label**: `bittrex_us_exchange_wind_down_and_chapter_11_off_ramp_freeze`

**Timestamp**: `2023-04-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20230331224349/https://bittrex.zendesk.com/hc/en-us/articles/10080271948701>
  - body_hash: `sha256:a75e689c3b0a2b1355c813fb1e64e7a84dbb66aef318c12b0d76f2363f63001b`
  - body_path: `sources/http_captures/sec-v-bittrex-2023/platform-response/web.archive.org__web-20230331224349-https-bittrex.zendesk.com-hc-en-us-articles-10080271948701__061683ac94.html`
  > Bittrex U.S. customer support article "Important Information for
> Bittrex U.S. Customers" (Wayback 2023-03-31 22:43 UTC) confirms the
> wind-down of Bittrex US operations and tells U.S. customers their
> funds are safe and available for withdrawal, citing the
> U.S. regulatory and economic environment.
- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20230401230357/https://bittrex.com/>
  - body_hash: `sha256:79af4c0fce77e3b0202b68df72b651be95b5b7a369adc15c538645cb855037a6`
  - body_path: `sources/http_captures/sec-v-bittrex-2023/platform-response/web.archive.org__web-20230401230357-https-bittrex.com__36cff035c3.html`
  > Wayback snapshot 2023-04-01 of bittrex.com carries the homepage
> banner: "Due to continued regulatory uncertainty, we have made the
> difficult decision to close our U.S. operations, effective April 30,
> 2023. All U.S. customer funds are safe and can be fully withdrawn
> immediately. This announcement does not impact non-U.S. customers
> using Bittrex Global."

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade L4 frontend diff is retained beyond the load-bearing

## 7. Related events

- [`sec-v-binance-2023`](./sec-v-binance-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `939a17f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

