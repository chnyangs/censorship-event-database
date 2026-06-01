# Evidence chain — `polymarket-cftc-geofence-2022-01`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `038e378` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The 2022-01-03 CFTC settlement against Blockratize Inc. d/b/a
> Polymarket ($1.4M penalty + cease-and-desist) produced a single-layer
> L4 cascade -- a US-vantage geofence at polymarket.com -- with the
> on-chain Polygon protocol contracts remaining functional. Longitudinal
> validation via the 2026-04 DOJ SDNY indictment of Master Sergeant
> Gannon Ken Van Dyke (for using classified Maduro-operation intel to
> win ~$409K on Polymarket) confirms the US-vantage geofence remained
> in place through 2026 and that VPN-bypass is well-documented.

## 1. Trigger

- **Type**: `cftc_action`
- **Actor**: `US_CFTC`
- **Timestamp**: `2022-01-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8478-22>
  - Wayback: <https://web.archive.org/web/20220103203805/https://www.cftc.gov/PressRoom/PressReleases/8478-22>
  - body_hash: `sha256:ced129f8b43464ae9b2a24d4375187c2f7fa14a963347375c13394c5163f500f`
  - body_path: `sources/http_captures/polymarket-cftc-geofence-2022-01/primary/web.archive.org__web-20220103203805-https-www.cftc.gov-PressRoom-PressReleases-8478-22__afc6e83fb6.html`
  > CFTC press release 8478-22 (2022-01-03): "CFTC Orders Event-Based
> Binary Options Markets Operator to Pay $1.4 Million Penalty." The
> Commission filed and simultaneously settled charges against
> Blockratize, Inc. d/b/a Polymarket.com (Delaware-registered, NYC-
> based) for offering off-exchange event-based binary options
> contracts and failure to obtain designation as a DCM or
> registration as a SEF. Beginning approximately June 2020,
> Polymarket operated an illegal unregistered facility for event-
> based binary options ("event markets"). The settlement order
> requires: (a) $1.4M civil monetary penalty, (b) wind-down of all
> non-compliant markets on polymarket.com, and (c) cease-and-desist
> from CEA / CFTC regulation violations. Implementation included a
> US-vantage geofence at polymarket.com.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Polymarket (Blockratize, Inc.)
- **Chains**: `polygon`
- **Canonical domains**: `polymarket.com`

> Blockratize, Inc. d/b/a Polymarket.com — single corporate entity
> (Delaware-registered, NYC-based) operating the polymarket.com
> event-market frontend and the Polygon-based prediction-market smart
> contracts. The CFTC order targets the operator entity; the on-chain
> Polymarket protocol contracts on Polygon remained functional
> post-settlement.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `polymarket_us_vantage_geofence_post_cftc_settlement`

**Timestamp**: `2022-01-03 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8478-22>
  - Wayback: <https://web.archive.org/web/20220103203805/https://www.cftc.gov/PressRoom/PressReleases/8478-22>
  - body_hash: `sha256:ced129f8b43464ae9b2a24d4375187c2f7fa14a963347375c13394c5163f500f`
  - body_path: `sources/http_captures/polymarket-cftc-geofence-2022-01/primary/web.archive.org__web-20220103203805-https-www.cftc.gov-PressRoom-PressReleases-8478-22__afc6e83fb6.html`
  > CFTC settlement order (2022-01-03) requires Polymarket to wind
> down all non-compliant event markets on polymarket.com and to
> cease-and-desist further CEA violations. The operator-side
> implementation is the US-vantage geofence on polymarket.com.
> attribution=direct because the CFTC order is the legal
> instrument compelling the frontend change. Wayback memento
> 20220103203805 captured 2026-05-20.
- **`supporting_journalism`**
  - URL: <https://thedefiant.io/news/defi/polymarket-settlement-cftc>
  - Wayback: <https://web.archive.org/web/20260516000000/https://thedefiant.io/news/defi/polymarket-settlement-cftc>
  > The Defiant (2022-01-03): "Polymarket Shuts Out U.S. Traders to
> Comply with CFTC Settlement." Same-day journalism confirming
> the operator response was a US-resident frontend ban. Wayback
> URL is a DRYRUN stub pending capture.
- **`supporting_journalism`**
  - URL: <https://www.justice.gov/opa/pr/us-soldier-charged-using-classified-information-profit-prediction-market-bets>
  - Wayback: <https://web.archive.org/web/20260424003623/https://www.justice.gov/opa/pr/us-soldier-charged-using-classified-information-profit-prediction-market-bets>
  - body_hash: `sha256:d9ca9a1d0ca42055bfb0a09a1bb5d8637e1e3a1b979e5d9a4f33893cd50b6692`
  - body_path: `sources/http_captures/polymarket-cftc-geofence-2022-01/primary/web.archive.org__web-20260424003623-https-www.justice.gov-opa-pr-us-soldier-charged-using-classified-information-profit-prediction-market-bets__32c90e5988.html`
  > DOJ SDNY press release (2026-04): "U.S. Soldier Charged With
> Using Classified Information To Profit From Prediction Market
> Bets." Master Sergeant Gannon Ken Van Dyke (US Army Special
> Forces) charged with using classified intel about Operation
> Absolute Resolve (Maduro-capture operation) to bet ~$33K on
> Polymarket markets and net ~$409,881 in profit. Court filings
> confirm: Americans are banned from Polymarket; Van Dyke
> allegedly used VPN-based circumvention. Provides 2026 evidence
> that the 2022 US-vantage geofence remained in place ~4 years
> post-settlement and that VPN-bypass is well-documented.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)
- [`bitfinex-tether-cftc-2021`](./bitfinex-tether-cftc-2021.md)
- [`bitmex-cftc-doj-2020`](./bitmex-cftc-doj-2020.md)
- [`binance-cftc-2023`](./binance-cftc-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `038e378`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

