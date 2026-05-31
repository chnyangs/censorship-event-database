# Evidence chain — `bitfinex-tether-cftc-2021`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c86ca57` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2021-10-15 CFTC press release 8450-21 packages two simultaneous
> CFTC settlements ($1.5M against iFinex / BFXNA / BFXWW for illegal
> off-exchange financed retail commodity transactions in digital
> assets, and $41M against Tether Holdings / Limited / Operations /
> International for false or misleading statements regarding USDT
> reserve backing during 2016-01 through 2018-02), each registered
> as a single direct-attribution observed_change row at the
> offramp_cex layer. The CFTC settlement extends the 2021-02-23 NYAG
> disclosure-regime change to the federal commodities-law axis. The
> row asserts neither network-layer reachability change nor any
> USDT addBlackList() on-chain action; the reserve-attestation
> regime is recorded at offramp_cex (Tether-as-issuer fiat-rails
> interface), not at asset_onchain."

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2021-10-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8450-21>
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
> portions of the 2016-01 through 2018-02 review period the Tether
> entities held insufficient fiat reserves to back USDT 1:1 and
> commingled reserve assets with operational funds, including
> through transfers to and from Bitfinex. The 2021-10-15 CFTC
> action follows the 2021-02-23 NYAG settlement (NY OAG In the
> Matter of iFinex Inc. et al.) which already imposed a $18.5M
> penalty and a prohibition on serving New York residents plus a
> quarterly USDT reserve-composition reporting obligation. The
> CFTC settlement extends the disclosure-regime change to a
> federal-level commodities-law axis. Marked
> evidence_use=contextual_unarchived because the authoring LLM
> agent did not personally pin a Wayback snapshot timestamp or
> compute a body_hash for the press release; the CFTC press-release
> URL format is stable and routinely captured by Wayback, but the
> specific snapshot timestamp is to be re-pinned during human
> audit before this citation may serve as an admission anchor in
> its own right. Provisional Wayback anchor uses Wayback Machine
> 2026-05-16 timestamp prefix.
- **`primary_corporate`**
  - URL: <https://tether.to/en/tether-and-bitfinex-reach-settlement-with-cftc/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://tether.to/en/tether-and-bitfinex-reach-settlement-with-cftc/>
  > Tether corporate response statement "Tether and Bitfinex Reach
> Settlement with the CFTC" (2021-10-15) confirming the $41M
> Tether + $1.5M Bitfinex settlement without admission of
> wrongdoing, and announcing prospective compliance with the
> CFTC-imposed disclosure regime including continued quarterly
> attestation reports on USDT reserve composition. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin and
> body_hash capture during human audit. Provisional Wayback anchor
> uses Wayback Machine 2026-05-16 timestamp prefix.

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
> $41M USDT reserve-disclosure order. The row enumerates only the
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
> retail-commodity-2016) which imposed a $75,000 penalty and
> required transition to an actual-delivery margin model;
> this 2021-10-15 order extends the enforcement to the
> 2016-04 through 2018-02 review period covering activity
> that postdated the 2016 order. Provisional Wayback anchor
> uses Wayback Machine 2026-05-16 timestamp prefix.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `cftc_ordered_tether_usdt_reserve_attestation_regime_change_2021`

**Timestamp**: `2021-10-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8450-21>
  > CFTC press release 8450-21 anchors the $41M order against
> Tether Holdings Limited, Tether Limited, Tether Operations
> Limited, and Tether International Limited for making untrue
> or misleading statements and omissions of material fact in
> connection with the US-dollar tether (USDT) stablecoin
> during the 2016-01 through 2018-02 period. The CFTC order
> imposes the $41M civil penalty plus a continuing two-year
> quarterly reserve-composition reporting obligation on the
> Tether issuer group, which is the regulator-compelled
> reserve-attestation regime change registered as this
> observation. attribution=direct because the CFTC order is
> the legal instrument that imposes the new disclosure
> regime against the Tether issuer entities; the obligation
> is registered at offramp_cex (Tether-as-issuer fiat-rails
> interface) rather than asset_onchain because the CFTC
> remedy operates on the off-chain reserve-disclosure axis,
> not on the USDT addBlackList() on-chain primitive. Follows
> the 2021-02-23 NYAG settlement which imposed an analogous
> quarterly reserve-composition disclosure obligation at the
> state level; this CFTC order extends the regime to the
> federal commodities-law axis. Provisional Wayback anchor
> uses Wayback Machine 2026-05-16 timestamp prefix.
- **`primary_corporate`**
  - URL: <https://tether.to/en/tether-and-bitfinex-reach-settlement-with-cftc/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://tether.to/en/tether-and-bitfinex-reach-settlement-with-cftc/>
  > Tether corporate response statement confirming the $41M
> Tether + $1.5M Bitfinex settlement and the prospective
> adoption of the CFTC-mandated quarterly reserve-composition
> attestation regime. Corroborates the issuer-side acceptance
> of the disclosure-regime change. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin.
> Provisional Wayback anchor uses Wayback Machine 2026-05-16
> timestamp prefix.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitfinex-cftc-retail-commodity-2016`](./bitfinex-cftc-retail-commodity-2016.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)
- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)
- [`binance-cftc-2023`](./binance-cftc-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c86ca57`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

