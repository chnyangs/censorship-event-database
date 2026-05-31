# Evidence chain — `bitmex-cftc-doj-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1929490` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2020-10-01 CFTC civil complaint and DOJ SDNY criminal indictment
> against BitMEX (HDR Global Trading) and co-founders Arthur Hayes,
> Benjamin Delo, Samuel Reed, and Gregory Dwyer produced a 2-layer
> cascade in the dataset: an L4 user-facing notice geo-blocking US
> retail access and an offramp_cex restriction of US-resident derivatives
> rails coupled with a globally mandatory KYC programme, resolved
> 2021-08-10 via a $100M CFTC consent order. Structurally the BSA-AML /
> KYC template later extended by the Binance and KuCoin enforcement
> paths."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2020-10-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8270-20>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8270-20>
  > CFTC press release 8270-20 (2020-10-01): "CFTC Charges BitMEX Owners
> with Illegally Operating a Cryptocurrency Derivatives Trading
> Platform and Anti-Money Laundering Violations." Civil enforcement
> complaint filed in S.D.N.Y. against five entities operating the
> BitMEX platform (HDR Global Trading Limited, 100x Holding Limited,
> ABS Global Trading Limited, Shine Effort Inc Limited, HDR Global
> Services (Bermuda) Limited) for offering illegal off-exchange
> leveraged retail commodity transactions, operating an unregistered
> FCM / DCM / SEF, and failing to implement required BSA / AML
> controls. Resolved 2021-08-10 via $100M consent order; companion
> criminal indictments by US DOJ SDNY against founders.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founders-and-executive-cryptocurrency-exchange-charged-violation-bank-secrecy-act>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founders-and-executive-cryptocurrency-exchange-charged-violation-bank-secrecy-act>
  > DOJ SDNY press release (2020-10-01): "Founders And Executive Of
> Off-Shore Cryptocurrency Derivatives Exchange Charged With Violation
> Of The Bank Secrecy Act." Criminal indictment of Arthur Hayes,
> Benjamin Delo, Samuel Reed (BitMEX co-founders) and Gregory Dwyer
> (first Head of Business Development) for willfully causing BitMEX
> to fail to establish, implement, and maintain an adequate
> anti-money-laundering program in violation of the BSA (31 U.S.C.
> Sections 5318(h) and 5322). Companion to the CFTC civil complaint
> filed the same day.
- **`primary_corporate`**
  - URL: <https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/>
  > BitMEX corporate blog post (2020-10-01): "HDR Global Trading
> Limited Response to the CFTC and FinCEN." HDR (BitMEX's parent)
> confirms the same-day US enforcement actions and commits to
> accelerated KYC verification + US-resident off-boarding. The
> post is the operator-side anchor for the L4 user-facing notice
> and the offramp_cex US-rails restriction.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BitMEX (HDR Global Trading) + Hayes / Delo / Reed / Dwyer
- **Chains**: `bitcoin`
- **Canonical domains**: `bitmex.com`

> BitMEX platform operating entities (HDR Global Trading Limited, 100x
> Holding Limited, ABS Global Trading Limited, Shine Effort Inc Limited,
> HDR Global Services (Bermuda) Limited) + named individual defendants:
> Arthur Hayes, Benjamin Delo, Samuel Reed (co-founders), Gregory Dwyer
> (Head of Business Development). Canonical exchange domain bitmex.com
> remained globally operational post-enforcement, but retail US-resident
> access was geo-blocked and full KYC verification was made mandatory
> for the global user base.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `bitmex_us_retail_geoblock_and_kyc_mandate_announcement`

**Timestamp**: `2020-10-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/>
  > HDR Global Trading's same-day operator response cited the CFTC +
> FinCEN / DOJ actions and announced (a) accelerated US-resident
> off-boarding from retail leveraged-derivative products and
> (b) the mandatory User Verification Programme (full KYC) for
> all account holders. attribution=direct because the operator
> notice explicitly references the 2020-10-01 enforcement as the
> precipitating cause.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founders-and-executive-cryptocurrency-exchange-charged-violation-bank-secrecy-act>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founders-and-executive-cryptocurrency-exchange-charged-violation-bank-secrecy-act>
  > DOJ SDNY indictment names BitMEX's failure to maintain an
> adequate BSA-compliant AML program — including the absence of
> customer identity verification — as the criminal predicate,
> providing the legal anchor for the same-day operator KYC /
> US-off-boarding notice.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bitmex_us_retail_rails_restricted_and_global_kyc_enforced`

**Timestamp**: `2020-10-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8270-20>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8270-20>
  > CFTC press release describes the platform-level enforcement:
> BitMEX operated as an unregistered FCM / DCM / SEF and offered
> illegal off-exchange leveraged retail commodity transactions to
> US persons without implementing required BSA / AML controls.
> The 2021-08-10 consent order required HDR Global Trading and
> related entities to pay $100M in civil monetary penalties and
> to refrain from US retail derivatives activity absent
> registration — structural off-ramp restriction for the US
> retail rail. attribution=direct because the CFTC order is the
> legal instrument compelling the rails change.
- **`primary_corporate`**
  - URL: <https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://blog.bitmex.com/hdr-global-trading-limited-response-to-the-cftc-and-fincen/>
  > BitMEX operator response confirms the rails-level change:
> US-resident retail access geo-blocked and global User
> Verification Programme (mandatory KYC) deployed across the
> full account base. Together with the CFTC / DOJ filings this
> establishes a direct trigger -> rails-change cascade.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`kucoin-doj-2024`](./kucoin-doj-2024.md)
- [`kraken-sec-staking-2023`](./kraken-sec-staking-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1929490`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

