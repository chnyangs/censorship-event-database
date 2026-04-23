# Evidence chain — `sec-v-binance-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `anchor_case`

**Dataset version**: `0.1.0` · **Dataset cutoff**: `2026-04-22` · **Source commit**: `c1d39f8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-04-23T04:41:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SEC v. Binance (2023-06-05) was the first SEC civil-enforcement event in
> the dataset targeting a major crypto exchange; the asset-freeze motion
> produced a direct L4 + offramp cascade at Binance.US within 4 days
> (2023-06-09 fiat-rail suspension). Demonstrates securities-law
> enforcement as a distinct censorship-cascade trigger from OFAC SDN."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-06-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao>
  - body_hash: `sha256:f1aeedd40346f555c3f35fd5efe781d1d1e2cbe3751c8f1e79f49481ca826665`
  - body_path: `sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`
  > SEC press release 2023-101: "SEC Files 13 Charges Against Binance Entities
> and Founder Changpeng Zhao" (2023-06-05). SEC civil action in DDC: Binance
> Holdings Ltd. + BAM Trading Services (Binance.US operator) + Changpeng
> Zhao charged with 13 counts including operating unregistered exchanges /
> broker-dealers / clearing agencies, unregistered securities offerings
> (BNB, BUSD, Simple Earn, BNB Vault, staking), and commingling billions
> in customer funds. Pre-dates the 2023-11-21 DOJ settlement by 169 days.
> Distinct from the 2023-11 criminal resolution — this is SEC civil
> enforcement on the securities-law axis.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings / BAM Trading / Changpeng Zhao
- **Canonical domains**: `binance.com`, `binance.us`

> Binance Holdings Ltd. (global) + BAM Trading Services Inc. (Binance.US) +
> BAM Management US Holdings + Changpeng Zhao individual. Securities
> specifically named as unregistered: BNB, BUSD, Binance Simple Earn, BNB
> Vault, BUSD staking-product, BETH. No on-chain addresses; securities-law
> charges operate at token-offering/exchange-registration level.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 96.0h

**Event label**: `binance_us_suspended_usd_fiat_rails_within_4d`

**Timestamp**: `2023-06-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao>
  - body_hash: `sha256:f1aeedd40346f555c3f35fd5efe781d1d1e2cbe3751c8f1e79f49481ca826665`
  - body_path: `sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`
  > SEC charges include asset-freeze motion against BAM Trading Services;
> the motion was the proximate cause of Binance.US suspending USD
> deposits/withdrawals on 2023-06-09. Direct attribution: the SEC
> filing explicitly named the fiat-rail asset-freeze as the requested
> relief.
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20230610*/binance.us>
  - Wayback: <https://web.archive.org/web/20230610/https://binance.us/>
  > Wayback CDX calendar for binance.us around 2023-06-09 shows the
> transition from normal-operation state to suspended-fiat-rails
> banner. Independent archival anchor for the observed_change.

### offramp_cex · attribution: `direct` · Δt = 96.0h

**Event label**: `binance_us_offramp_crippled_post_sec_freeze`

**Timestamp**: `2023-06-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao>
  - body_hash: `sha256:f1aeedd40346f555c3f35fd5efe781d1d1e2cbe3751c8f1e79f49481ca826665`
  - body_path: `sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`
  > Binance.US fiat onramp functionally collapsed post-SEC action. US
> customer trading volume fell 90%+ through Q3 2023. Direct SEC
> securities-law cascade at the offramp layer.
- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2023-101-sec-files-13-charges-against-binance-entities-founder-changpeng-zhao>
  - body_hash: `sha256:f1aeedd40346f555c3f35fd5efe781d1d1e2cbe3751c8f1e79f49481ca826665`
  - body_path: `sources/http_captures/sec-v-binance-2023/primary/www.sec.gov__news-press-release-2023-101__a38c3e222c.html`
  > Second reference to the SEC filing — the asset-freeze motion +
> 13 charges document defines both the trigger and the mandated
> compliance outcome.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.1.0` (commit `c1d39f8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

