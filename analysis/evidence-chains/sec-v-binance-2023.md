# Evidence chain — `sec-v-binance-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `3067f79` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-06` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "SEC v. Binance produced a scoped Binance.US CEX/off-ramp platform reaction
> within the observation window; the dataset does not claim a measured L4
> frontend takedown, on-chain asset freeze, or L1/L3 effect."

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
- **Enumeration**: `complete`
- **Actor name**: Binance Holdings / BAM Trading / Changpeng Zhao
- **Canonical domains**: `binance.com`, `binance.us`

> Binance Holdings Ltd. (global) + BAM Trading Services Inc. (Binance.US) +
> BAM Management US Holdings + Changpeng Zhao individual. Securities
> specifically named as unregistered: BNB, BUSD, Binance Simple Earn, BNB
> Vault, BUSD staking-product, BETH. No on-chain addresses; securities-law
> charges operate at token-offering/exchange-registration level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 72h

**Event label**: `binance_us_platform_and_usd_rail_restrictions_after_sec_action`

**Timestamp**: `2023-06-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://support.binance.us/en/articles/9843568-binance-us-will-remove-10-trading-pairs-has-paused-otc-trading-updated>
  - body_hash: `sha256:e6d1292db455dc6a8680637449cc8a05dbf11c63618da8770937b88bcdc588e6`
  - body_path: `sources/http_captures/sec-v-binance-2023/platform-response/support.binance.us__en-articles-9843568-binance-us-will-remove-10-trading-pairs-has-paused-otc-trading-updated__0e03a1e712.html`
  > Binance.US support notice states that selected BTC/BUSD trading pairs
> would be removed on 2023-06-08 and that the OTC Trading Portal had
> been paused, while ordinary crypto trading remained available.
- **`primary_corporate`**
  - URL: <https://support.binance.us/en/articles/9843567-binance-us-will-remove-select-usd-advanced-trading-pairs>
  - body_hash: `sha256:3a20f9c26f640caba0b9e3ec228a43abc60793521137dbec563d310af8431ecb`
  - body_path: `sources/http_captures/sec-v-binance-2023/platform-response/support.binance.us__en-articles-9843567-binance-us-will-remove-select-usd-advanced-trading-pairs__852a151d2b.html`
  > Binance.US support notice records the later removal of selected USD
> advanced-trading pairs as part of the platform's crypto-only shift.
- **`supporting_journalism`**
  - URL: <https://www.theguardian.com/business/2023/jun/09/binanceus-prepares-to-suspend-us-dollar-deposits-and-withdrawals-from-exchange>
  - body_hash: `sha256:c29283b567f98d5a4f2d5ecd3ed1e188c4baa391269023c347aa85f4cf794189`
  - body_path: `sources/http_captures/sec-v-binance-2023/platform-response/www.theguardian.com__business-2023-jun-09-binanceus-prepares-to-suspend-us-dollar-deposits-and-withdrawals-from-exchange__57c8dce343.html`
  > Guardian / Reuters coverage of the Binance.US customer notice records
> suspended USD deposits, expected fiat-withdrawal-channel disruption
> as early as 2023-06-13, and the exchange's crypto-only transition
> framing days after the SEC action.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade L4 frontend diff is retained. The Binance.US

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `3067f79`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

