# Evidence chain — `sec-burnside-bitcoin-stock-exchange-2014`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a4484c4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2014-12-08 SEC cease-and-desist settlement against Ethan Burnside
> and BTC Trading Corp records that, after Commission staff contact in
> 2013-09, BTCT and LTC-Global disabled registration/trading functions,
> preserved user withdrawals, and had ceased operating by 2013-10-31; the
> settlement then imposed cease-and-desist, industry-bar, disgorgement /
> interest, and penalty remedies. The row claims only this SEC-order-
> supported L4/offramp_cex cessation observation and not network blocking,
> on-chain asset action, or PBS-era L1/L3 effects."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2014-12-08 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2014-273>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/news/press-release/2014-273>
  - body_hash: `sha256:8df90509bfb2278913febfb77097dad838daeb098dd317e0f84dd701e56477c6`
  - body_path: `sources/http_captures/sec-burnside-bitcoin-stock-exchange-2014/sec-primary/www.sec.gov__newsroom-press-releases-2014-273__10000997d5.html`
  > SEC press release 2014-273 (2014-12-08): "SEC Sanctions Operator of
> Bitcoin-Related Stock Exchanges for Registration Violations." Charges
> Ethan Burnside and his BTC Trading Corp for operating two unregistered
> online securities exchanges denominated in Bitcoin and Litecoin: BTC
> Trading Corp (BTCT, 2012-08 to 2013-10) and LTC-Global Virtual Stock
> Exchange (2012-04 to 2013-10). Settlement: ~$68,000 in disgorgement,
> prejudgment interest, and civil penalties; two-year ban from
> association and from participating in any penny-stock offerings.
> Earliest SEC enforcement against an unregistered crypto-denominated
> securities exchange. SOURCE-REPAIRED 2026-06-01: the SEC newsroom
> press release was captured locally and pinned with body_hash/body_path.
> The legacy Wayback year-prefix URL remains only as a supplemental
> historical lookup.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9685.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/litigation/admin/2014/33-9685.pdf>
  - body_hash: `sha256:aa0c6f4a9626bb46b6f1b169b9d544d5a64e3e97be8e9dcc87d09e5277bc43b0`
  - body_path: `sources/http_captures/sec-burnside-bitcoin-stock-exchange-2014/sec-primary/www.sec.gov__litigation-admin-2014-33-9685.pdf__60467c1bed.bin`
  > SEC Administrative Proceeding Order 33-9685 (Release No. 33-9685 /
> 34-73783 / IC-31366 / Admin Proc. File No. 3-16307) instituting and settling
> cease-and-desist proceedings against Ethan Burnside and BTC Trading
> Corp. The order details (i) operation of BTCT as an unregistered
> Bitcoin-denominated stock exchange and (ii) operation of LTC-Global
> as an unregistered Litecoin-denominated stock exchange, both without
> registration as a national securities exchange under Section 5 of
> the Exchange Act. It records that, in response to Commission staff's
> investigation, Burnside began winding down both websites in September
> 2013 and that both websites had ceased operating by 2013-10-31.
> SOURCE-REPAIRED 2026-06-01: the live SEC PDF was captured locally and
> pinned with body_hash/body_path. The legacy Wayback year-prefix URL
> remains only as a supplemental historical lookup.

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

**Event label**: `sec_order_recorded_btct_ltc_global_website_function_winddown`

**Timestamp**: `2014-12-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2014-273>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/news/press-release/2014-273>
  - body_hash: `sha256:8df90509bfb2278913febfb77097dad838daeb098dd317e0f84dd701e56477c6`
  - body_path: `sources/http_captures/sec-burnside-bitcoin-stock-exchange-2014/sec-primary/www.sec.gov__newsroom-press-releases-2014-273__10000997d5.html`
  > SEC press release 2014-273 names BTC Virtual Stock Exchange and
> LTC-Global Virtual Stock Exchange as the online venues that traded
> securities using Bitcoin or Litecoin without registration. It
> states that the venues operated from 2012-08 through 2013-10 and
> describes the 2014-12-08 settlement. Local body_hash/body_path
> capture is the admission-grade replay anchor; the legacy Wayback
> year-prefix URL is supplemental.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9685.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/litigation/admin/2014/33-9685.pdf>
  - body_hash: `sha256:aa0c6f4a9626bb46b6f1b169b9d544d5a64e3e97be8e9dcc87d09e5277bc43b0`
  - body_path: `sources/http_captures/sec-burnside-bitcoin-stock-exchange-2014/sec-primary/www.sec.gov__litigation-admin-2014-33-9685.pdf__60467c1bed.bin`
  > SEC Administrative Proceeding Order 33-9685 records that Burnside
> began an orderly winddown in 2013-09 after Commission staff contact,
> disabled registration and trading functions while preserving
> withdrawals, and that both websites had ceased operating by
> 2013-10-31. Timestamp is the public order date; the row does not
> claim the website winddown first occurred on 2014-12-08.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_order_finalized_btct_ltc_global_exchange_winddown_and_cease_desist`

**Timestamp**: `2014-12-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/newsroom/press-releases/2014-273>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/news/press-release/2014-273>
  - body_hash: `sha256:8df90509bfb2278913febfb77097dad838daeb098dd317e0f84dd701e56477c6`
  - body_path: `sources/http_captures/sec-burnside-bitcoin-stock-exchange-2014/sec-primary/www.sec.gov__newsroom-press-releases-2014-273__10000997d5.html`
  > SEC press release 2014-273 documents that the BTC Trading Corp
> and LTC-Global venues operated as unregistered Bitcoin/Litecoin
> stock-exchange venues and that the 2014-12-08 settlement imposed
> more than $68,000 in disgorgement, interest, and penalty plus a
> two-year industry bar. Local body_hash/body_path capture is the
> admission-grade replay anchor; the legacy Wayback year-prefix URL
> is supplemental.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/admin/2014/33-9685.pdf>
  - Wayback: <https://web.archive.org/web/2015/https://www.sec.gov/litigation/admin/2014/33-9685.pdf>
  - body_hash: `sha256:aa0c6f4a9626bb46b6f1b169b9d544d5a64e3e97be8e9dcc87d09e5277bc43b0`
  - body_path: `sources/http_captures/sec-burnside-bitcoin-stock-exchange-2014/sec-primary/www.sec.gov__litigation-admin-2014-33-9685.pdf__60467c1bed.bin`
  > SEC Administrative Proceeding Order 33-9685 records the 2013-09
> winddown after Commission staff contact, the 2013-10-31 cessation
> of both websites, and the 2014-12-08 cease-and-desist, industry
> bar, disgorgement/interest, and penalty remedies. Local
> body_hash/body_path capture is the admission-grade replay anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`sec-beaxy-platform-shutdown-2023`](./sec-beaxy-platform-shutdown-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a4484c4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

