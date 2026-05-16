# Evidence chain — `sec-burnside-bitcoin-stock-exchange-2014`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-10` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `36d266a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-24T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2014-12-08 SEC cease-and-desist settlement against Ethan Burnside
> and BTC Trading Corp finalized the shutdown of two unregistered
> Bitcoin/Litecoin-denominated securities-exchange venues (BTCT and
> LTC-Global) at the L4 frontend and offramp_cex layers; the row claims
> only this two-layer cessation observation and not network blocking,
> on-chain asset action, or PBS-era L1/L3 effects."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2014-12-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2014-273>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/news/press-release/2014-273>
  > SEC press release 2014-273 (2014-12-08): "SEC Sanctions Operator of
> Bitcoin-Related Stock Exchanges for Registration Violations." Charges
> Ethan Burnside and his BTC Trading Corp for operating two unregistered
> online securities exchanges denominated in Bitcoin and Litecoin: BTC
> Trading Corp (BTCT, 2012-08 to 2013-10) and LTC-Global Virtual Stock
> Exchange (2012-04 to 2013-10). Settlement: ~$68,000 in disgorgement,
> prejudgment interest, and civil penalties; two-year ban from
> association and from participating in any penny-stock offerings.
> Earliest SEC enforcement against an unregistered crypto-denominated
> securities exchange. Wayback anchor is a year-prefix lookup; specific
> snapshot timestamp requires human-audit re-pinning before this
> citation can serve as a standalone admission anchor.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9684.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/litigation/admin/2014/33-9684.pdf>
  > SEC Administrative Proceeding Order 33-9684 (Release No. 33-9684 /
> 34-73834 / Admin Proc. File No. 3-16307) instituting and settling
> cease-and-desist proceedings against Ethan Burnside and BTC Trading
> Corp. The order details (i) operation of BTCT as an unregistered
> Bitcoin-denominated stock exchange and (ii) operation of LTC-Global
> as an unregistered Litecoin-denominated stock exchange, both without
> registration as a national securities exchange under Section 5 of
> the Exchange Act. Wayback anchor is a year-prefix lookup; the
> specific snapshot timestamp requires re-pinning during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Ethan Burnside / BTC Trading Corp
- **Chains**: `bitcoin`, `litecoin`
- **Canonical domains**: `btct.co`, `ltc-global.com`

> Ethan Burnside (individual respondent) and BTC Trading Corp (corporate
> respondent), operators of the two Bitcoin/Litecoin-denominated
> unregistered securities exchanges named in the SEC order: BTC Trading
> Corp (BTCT, btct.co) and LTC-Global Virtual Stock Exchange
> (ltc-global.com). Listed-asset issuers that traded on the two venues
> are not enumerated here. Both exchanges had already ceased operations
> on 2013-10 (BTCT) and 2013-10 (LTC-Global) under operator action ahead
> of the SEC settlement; the 2014-12-08 SEC order finalized the
> enforcement posture.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `btct_unregistered_securities_exchange_frontend_shutdown`

**Timestamp**: `2014-12-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2014-273>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/news/press-release/2014-273>
  > SEC press release 2014-273 names the BTCT (btct.co) Bitcoin-
> denominated securities-exchange frontend as the public surface
> that operated without registration and was the subject of the
> cease-and-desist order. The operator-side shutdown (2013-10) was
> finalized by the 2014-12-08 settlement. attribution=direct
> because the SEC primary-legal source names the regulatory
> mandate. Wayback anchor is a year-prefix lookup; specific
> snapshot timestamp requires human-audit re-pinning.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9684.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/litigation/admin/2014/33-9684.pdf>
  > SEC Administrative Proceeding Order 33-9684 detailing the BTCT
> unregistered-exchange operation and its termination. Corroborates
> the L4 frontend shutdown observation at the primary-legal tier.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bitcoin_litecoin_denominated_securities_exchanges_terminated`

**Timestamp**: `2014-12-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2014-273>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/news/press-release/2014-273>
  > SEC press release 2014-273 documents that the BTC Trading Corp
> and LTC-Global venues operated as unregistered Bitcoin/Litecoin
> stock-exchange off-ramps and were terminated under the SEC
> cease-and-desist settlement (~$68,000 disgorgement +
> prejudgment interest + civil penalty + two-year associational
> and penny-stock bar). attribution=direct: SEC source names the
> regulatory mandate behind the off-ramp termination.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9684.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/litigation/admin/2014/33-9684.pdf>
  > SEC Administrative Proceeding Order 33-9684 details the off-ramp
> cessation at BTCT (Bitcoin-denominated) and LTC-Global (Litecoin-
> denominated). Corroborates the offramp_cex observation at the
> primary-legal tier.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`sec-beaxy-platform-shutdown-2023`](./sec-beaxy-platform-shutdown-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-10` (commit `36d266a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

