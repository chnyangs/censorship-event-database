# Evidence chain — `bitfinex-tether-cftc-2021`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `295a15d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2021-10-15 CFTC press release 8450-21 packages two simultaneous
> CFTC settlements ($1.5M against iFinex / BFXNA / BFXWW for illegal
> off-exchange financed retail commodity transactions in digital
> assets, and $41M against Tether Holdings / Limited / Operations /
> International for false or misleading statements regarding USDT
> reserve backing during 2016-06 through 2019-02), each registered
> as a single direct-attribution observed_change row at the
> offramp_cex layer. The Bitfinex order also required systems and
> procedures by 2021-12-31 to prevent covered U.S. persons from
> engaging in leveraged, margined, or financed retail commodity
> transactions on the platform. The CFTC settlement is a federal
> commodities-law reserve-misrepresentation counterpart to the
> 2021-02-23 NYAG settlement, but this row does not claim the CFTC
> order created the NYAG quarterly-reporting duty. The row asserts
> neither network-layer reachability change nor any USDT
> addBlackList() on-chain action; the Tether reserve-remediation
> posture is recorded at offramp_cex (Tether-as-issuer fiat-rails
> interface), not at asset_onchain."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2021-10-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - body_hash: `sha256:e47dfb31a0775ccb4a4ad732240723f741a2230709b2c0342b9eef53bf467c88`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__PressRoom-PressReleases-8450-21__6ca0538f56.html`
  > CFTC press release 8450-21 (2021-10-15): "CFTC Orders Tether and
> Bitfinex to Pay Fines Totaling $42.5 Million." Announces two
> simultaneous CFTC administrative settlements arising from a single
> investigation of iFinex Inc., BFXNA Inc., and BFXWW Inc. (operators
> of the Bitfinex cryptocurrency exchange) and of Tether Holdings
> Limited, Tether Limited, Tether Operations Limited, and Tether
> International Limited (collectively the USDT issuer group):
> (a) $1.5M civil monetary penalty against the Bitfinex entities for
> offering illegal off-exchange financed retail commodity transactions
> in digital assets to US persons, in violation of CEA Section 4(a),
> plus operating as an unregistered Futures Commission Merchant in
> violation of CEA Section 4d; and (b) $41M civil monetary penalty
> against the Tether entities for making untrue or misleading
> statements and omissions of material fact in connection with the
> US-dollar tether (USDT) stablecoin, specifically: USDT was
> marketed as "100% backed" by USD reserves but for substantial
> portions of the 2016-06-01 through 2019-02-25 review period the
> Tether entities held insufficient fiat reserves to back USDT 1:1 and
> commingled reserve assets with operational funds, including
> through transfers to and from Bitfinex. The 2021-10-15 CFTC
> action follows the 2021-02-23 NYAG settlement (NY OAG In the
> Matter of iFinex Inc. et al.) which already imposed a $18.5M
> penalty and a prohibition on serving New York residents plus a
> quarterly USDT reserve-composition reporting obligation. The
> CFTC settlement is the federal commodities-law reserve-
> misrepresentation counterpart, but this row does not claim that
> the CFTC order itself imposed the NYAG quarterly-reporting
> obligation. SOURCE-REPAIRED 2026-06-01: the live CFTC press
> release was captured locally and pinned with body_hash/body_path.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/media/6646/enftetherholdingsorder101521/download>
  - body_hash: `sha256:b468b9aafb63849fc1d699379b58f182220b5d01202d73c603a10c575159a3ca`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__media-6646-enftetherholdingsorder101521-download__e295e95279.bin`
  > CFTC Docket No. 22-04 order against Tether Holdings Limited,
> Tether Operations Limited, Tether Limited, and Tether
> International Limited, dated 2021-10-15. The order finds
> violations of CEA Section 6(c)(1) and Regulation 180.1(a)(2),
> imposes a $41 million civil monetary penalty and cease-and-
> desist, and records Tether's represented remediation efforts,
> including reserve segregation and more automated reserve tracking
> and reporting on the Tether Transparency Page.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/media/6651/enfbfxnaincorder101521/download>
  - body_hash: `sha256:2c26ec526ea15e84fa6e242f80006121d5f36ee16a0ce85694a3a585e00e7683`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__media-6651-enfbfxnaincorder101521-download__6d43b4e1fc.bin`
  > CFTC Docket No. 22-05 order against iFinex Inc., BFXNA Inc., and
> BFXWW Inc., dated 2021-10-15. The order finds CEA Sections 4(a)
> and 4d violations and a violation of the Commission's 2016 BFXNA
> order, imposes a $1.5 million civil monetary penalty and cease-
> and-desist, and requires systems and procedures reasonably
> designed to prevent covered U.S. persons from engaging in
> leveraged, margined, or financed retail commodity transactions by
> 2021-12-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: iFinex / BFXNA / BFXWW (Bitfinex) + Tether Holdings / Tether Limited / Tether Operations / Tether International (USDT issuer)
- **Chains**: `ethereum`, `tron`, `bitcoin`
- **Canonical domains**: `bitfinex.com`, `tether.to`

> Two enforcement-target groups consolidated into a single CFTC press
> release / dual-order action: (a) the Bitfinex operator entities
> iFinex Inc., BFXNA Inc., and BFXWW Inc., named in the $1.5M
> off-exchange retail commodity transaction order; and (b) the Tether
> issuer entities Tether Holdings Limited, Tether Limited, Tether
> Operations Limited, and Tether International Limited, named in the
> $41M USDT reserve-misrepresentation order. The row enumerates only the
> corporate-entity targets named in the two CFTC orders; it does not
> enumerate individual Bitfinex customer accounts, individual USDT
> holders, or specific on-chain USDT contract addresses. Canonical
> operator-controlled frontends are bitfinex.com (exchange) and
> tether.to (issuer transparency page).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_ordered_bitfinex_us_retail_financed_commodity_product_remediation_2021`

**Timestamp**: `2021-10-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - body_hash: `sha256:e47dfb31a0775ccb4a4ad732240723f741a2230709b2c0342b9eef53bf467c88`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__PressRoom-PressReleases-8450-21__6ca0538f56.html`
  > CFTC press release 8450-21 anchors the $1.5M order against
> iFinex Inc., BFXNA Inc., and BFXWW Inc. for offering illegal
> off-exchange financed retail commodity transactions in
> digital assets to US persons in violation of CEA Section 4(a)
> and operating as an unregistered Futures Commission Merchant
> in violation of CEA Section 4d. attribution=direct because
> the CFTC order itself imposes the civil penalty and the
> cease-and-desist requirement against the Bitfinex operator
> entities. The order is the second CFTC enforcement against
> Bitfinex's financed-commodity retail product line, following
> the 2016-06-02 CFTC order against BFXNA Inc. (bitfinex-cftc-
> retail-commodity-2016) which imposed a $75,000 penalty and a
> cease-and-desist; this 2021-10-15 order extends the enforcement
> to the 2016-03-01 through 2018-12-31 review period covering activity
> that postdated the 2016 order. Local body_hash/body_path
> capture is the admission-grade replay anchor.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/media/6651/enfbfxnaincorder101521/download>
  - body_hash: `sha256:2c26ec526ea15e84fa6e242f80006121d5f36ee16a0ce85694a3a585e00e7683`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__media-6651-enfbfxnaincorder101521-download__6d43b4e1fc.bin`
  > CFTC Docket No. 22-05 is the Bitfinex administrative order. It
> imposes the $1.5 million penalty and requires Bitfinex to
> implement, as necessary, and maintain systems and procedures
> reasonably designed to prevent covered U.S. persons from
> engaging in leveraged, margined, or financed retail commodity
> transactions or providing/receiving margin funding on the
> platform by 2021-12-31.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_ordered_tether_usdt_reserve_disclosure_remediation_2021`

**Timestamp**: `2021-10-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - body_hash: `sha256:e47dfb31a0775ccb4a4ad732240723f741a2230709b2c0342b9eef53bf467c88`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__PressRoom-PressReleases-8450-21__6ca0538f56.html`
  > CFTC press release 8450-21 anchors the $41M order against
> Tether Holdings Limited, Tether Limited, Tether Operations
> Limited, and Tether International Limited for making untrue
> or misleading statements and omissions of material fact in
> connection with the US-dollar tether (USDT) stablecoin
> during the 2016-06-01 through 2019-02-25 period. The CFTC order
> imposes the $41M civil penalty and cease-and-desist and
> identifies Tether's represented reserve-remediation posture,
> including reserve segregation and more automated tracking and
> Transparency Page reporting. attribution=direct because the
> observation event is the CFTC order and associated issuer
> compliance posture. It is registered at offramp_cex
> (Tether-as-issuer fiat-rails interface) rather than
> asset_onchain because the CFTC remedy operates on the
> off-chain reserve-disclosure axis, not on the USDT
> addBlackList() on-chain primitive. Local body_hash/body_path
> capture is the admission-grade replay anchor.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/media/6646/enftetherholdingsorder101521/download>
  - body_hash: `sha256:b468b9aafb63849fc1d699379b58f182220b5d01202d73c603a10c575159a3ca`
  - body_path: `sources/http_captures/bitfinex-tether-cftc-2021/cftc-tether-primary/www.cftc.gov__media-6646-enftetherholdingsorder101521-download__e295e95279.bin`
  > CFTC Docket No. 22-04 is the Tether administrative order. It
> finds that Tether misrepresented reserve backing, imposes the
> $41 million civil monetary penalty and cease-and-desist, and
> records Tether's represented remediation efforts. The legacy
> Tether corporate-response URL is not used as a claim anchor
> because the live capture now serves a generic Tether homepage
> rather than the 2021 settlement article.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitfinex-cftc-retail-commodity-2016`](./bitfinex-cftc-retail-commodity-2016.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)
- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)
- [`binance-cftc-2023`](./binance-cftc-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `295a15d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

