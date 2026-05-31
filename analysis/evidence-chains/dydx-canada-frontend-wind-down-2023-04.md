# Evidence chain — `dydx-canada-frontend-wind-down-2023-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c3fb0ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "dYdX on 2023-04-07 17:00 UTC stopped onboarding new Canadian users to
> dydx.exchange (v3) and on 2023-04-14 17:00 UTC moved existing Canadian
> users to close-only, geofencing its frontend against Canada over the
> CSA regulatory environment — a 1-layer l4_frontend observed_change
> (attribution=direct, dYdX official blog). Structurally an S5
> corporate-policy frontend geofence sibling to the S4 CSA-driven Binance
> Canada withdrawal (canada-csa-binance-withdrawal-2023); distinct from
> the later dYdX v4 US/Canada geofence."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `DYDX_TRADING`
- **Timestamp**: `2023-04-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/canada-wind-down>
  - Wayback: <https://web.archive.org/web/20260209054353/https://dydx.exchange/blog/canada-wind-down>
  - body_hash: `sha256:2626aa386a9b161466264c834b9ade84bdd301428de3627885c571b1394ff54f`
  - body_path: `sources/http_captures/dydx-canada-frontend-wind-down-2023-04/primary/web.archive.org__web-20260209054353-https-dydx.exchange-blog-canada-wind-down__7698f7cb86.html`
  > dYdX official blog "Canada Wind Down": on 2023-04-07 at 17:00 UTC
> dYdX stopped allowing new users located in Canada to onboard; on
> 2023-04-14 at 17:00 UTC existing Canadian users were moved to
> close-only mode (withdraw / close positions only). dYdX cited the
> Canadian regulatory environment (CSA additional restrictions on
> crypto-asset contracts). The captured page confirms "April 7",
> "17:00 UTC", "close-only", "onboard", and Canada. Verified via grep
> of the pinned body. primary_corporate anchor by the acting party.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: dYdX (Canada user cohort)
- **Chains**: `ethereum`
- **Canonical domains**: `dydx.exchange`

> dYdX Canadian-resident user cohort. dYdX Trading Inc. (operator of the
> dydx.exchange v3 perpetuals frontend) is the focal target actor; the
> affected population is Canadian-located users of dydx.exchange.
> Subset-enumerated because the wind-down affected the Canadian cohort
> rather than a named address list. Distinct from the later dYdX v4
> US/Canada geofence. Sibling to the S4 canada-csa-binance-withdrawal-2023
> and the S5 okx-canada-exit-2023 / kucoin-canada-exit-2023.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = Noneh

**Event label**: `dydx_canada_frontend_geofence`

**Timestamp**: `2023-04-07 17:00:00+00:00` (precision: `hour`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://dydx.exchange/blog/canada-wind-down>
  - Wayback: <https://web.archive.org/web/20260209054353/https://dydx.exchange/blog/canada-wind-down>
  - body_hash: `sha256:2626aa386a9b161466264c834b9ade84bdd301428de3627885c571b1394ff54f`
  - body_path: `sources/http_captures/dydx-canada-frontend-wind-down-2023-04/primary/web.archive.org__web-20260209054353-https-dydx.exchange-blog-canada-wind-down__7698f7cb86.html`
  > dYdX 2023-04-07 17:00 UTC Canadian-onboarding halt + 2023-04-14
> 17:00 UTC close-only transition for existing Canadian users.
> attribution=direct: the corporate-policy trigger and the frontend
> geofence are co-authored by the same actor (dYdX), and the dYdX
> blog explicitly cites the Canadian regulatory environment as the
> reason (§1.4 provider-cites-trigger + actor co-authorship).
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/225452/dydx-ends-support-for-canadian-users>
  - Wayback: <https://web.archive.org/web/20251028235922/https://www.theblock.co/post/225452/dydx-ends-support-for-canadian-users>
  - body_hash: `sha256:ec86382ddecd3891fad98aef1dfef271f9fd068233f7394cc4063f5e9c477e3d`
  - body_path: `sources/http_captures/dydx-canada-frontend-wind-down-2023-04/primary/web.archive.org__web-20251028235922-https-www.theblock.co-post-225452-dydx-ends-support-for-canadian-users__e001b7328e.html`
  > The Block corroboration of the dYdX Canada wind-down (April 7 /
> April 14, close-only, regulatory environment). Independent
> semi-primary second anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)
- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`okx-canada-exit-2023`](./okx-canada-exit-2023.md)
- [`dydx-tornado-account-block-2022-08`](./dydx-tornado-account-block-2022-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3fb0ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

