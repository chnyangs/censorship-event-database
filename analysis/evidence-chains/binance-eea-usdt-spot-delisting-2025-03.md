# Evidence chain — `binance-eea-usdt-spot-delisting-2025-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `cba4eca` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2025-03 delisting of USDT spot trading pairs (and other non-
> MiCA-compliant stablecoins) for EEA users — announced 2025-03-03,
> effective 2025-03-31 — severed the Binance spot off-ramp for USDT and
> the named non-MiCA-compliant stablecoin set in the EEA under MiCA;
> single-layer offramp_cex observed_change, attribution=direct via
> Binance's official announcement."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2025-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/bapi/composite/v1/public/cms/article/detail/query?articleCode=bcaa1f68d6a6450099056ff694ad6c46>
  - body_hash: `sha256:ab9421ce805ee409ca5d0cc720ecd4ff3a0a5887b843de0d1c5f7f73d43e4343`
  - body_path: `sources/http_captures/binance-eea-usdt-spot-delisting-2025-03/primary/www.binance.com__bapi-composite-v1-public-cms-article-detail-query__3f0c263400.json`
  > Binance official CMS API payload for announcement
> bcaa1f68d6a6450099056ff694ad6c46, "Binance Will Delist
> Non-MiCA Compliant Stablecoin Trading Pairs For EEA Users on
> 2025-03-31." The captured JSON states the announcement affects
> EEA users, cites EU stablecoin guidance / regulatory requirements,
> enumerates USDT, FDUSD, TUSD, USDP, DAI, AEUR, XUSD, and PAXG,
> and says non-MiCA-compliant spot pairs will be fully delisted
> from 2025-03-31 23:59 UTC onward. Captured 2026-06-01 via
> Binance's public CMS endpoint after the HTML page returned a
> CloudFront WAF challenge to non-browser capture.
- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - Wayback: <https://web.archive.org/web/20250401151406/https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - body_hash: `sha256:c8e6dc2f6cbf689fa951e3ff8560c97e317c1771c1d5a2a88f8714c79826fb18`
  - body_path: `sources/http_captures/binance-eea-usdt-spot-delisting-2025-03/primary/web.archive.org__web-20250401151406-https-www.financemagnates.com-cryptocurrency-binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica__5e927feefb.html`
  > Finance Magnates: Binance announced (2025-03-03) it will delist
> non-MiCA-compliant stablecoin trading pairs — including USDT spot
> pairs — for EEA users, with spot trading removed by 2025-03-31
> (margin pairs from 2025-03-27); USDT derivatives retained and
> MiCA-compliant USDC/EURI kept. Grep-confirmed: USDT/Tether/MiCA/
> delist/EEA/spot/"March 31" present in the captured body.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: Non-MiCA-compliant stablecoin spot pairs on Binance for EEA users
- **Canonical domains**: `binance.com`

> Binance's official announcement enumerates the affected
> non-MiCA-compliant stablecoin set for EEA users: USDT, FDUSD, TUSD,
> USDP, DAI, AEUR, XUSD, and PAXG. Complete enumeration of the named
> Binance EEA spot-pair delisting set; USDC, EURI, and EUR pairs remain
> available and unchanged.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 672h

**Event label**: `binance_delists_non_mica_stablecoin_spot_pairs_for_eea_users`

**Timestamp**: `2025-03-31 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/bapi/composite/v1/public/cms/article/detail/query?articleCode=bcaa1f68d6a6450099056ff694ad6c46>
  - body_hash: `sha256:ab9421ce805ee409ca5d0cc720ecd4ff3a0a5887b843de0d1c5f7f73d43e4343`
  - body_path: `sources/http_captures/binance-eea-usdt-spot-delisting-2025-03/primary/www.binance.com__bapi-composite-v1-public-cms-article-detail-query__3f0c263400.json`
  > Binance's own announcement states that, from 2025-03-31
> 23:59 UTC onward, non-MiCA-compliant spot pairs will be fully
> delisted for EEA users and users will no longer be able to
> trade those pairs. It also states that custody, withdrawal,
> deposit, and Binance Convert sale routes remain available.
> attribution=direct for the Binance-authored policy and stated
> regulatory-compliance rationale.
- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - Wayback: <https://web.archive.org/web/20250401151406/https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - body_hash: `sha256:c8e6dc2f6cbf689fa951e3ff8560c97e317c1771c1d5a2a88f8714c79826fb18`
  - body_path: `sources/http_captures/binance-eea-usdt-spot-delisting-2025-03/primary/web.archive.org__web-20250401151406-https-www.financemagnates.com-cryptocurrency-binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica__5e927feefb.html`
  > Finance Magnates: Binance USDT spot-pair EEA delisting
> (announced 2025-03-03, effective 2025-03-31; derivatives
> retained). Retained as contemporaneous corroboration of the
> Binance official CMS announcement.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`crypto-com-eu-usdt-stablecoin-delisting-2025-01`](./crypto-com-eu-usdt-stablecoin-delisting-2025-01.md)
- [`eu-mica-2023`](./eu-mica-2023.md)
- [`mica-l2-esma-eba-rts-2024`](./mica-l2-esma-eba-rts-2024.md)
- [`binance-busd-wind-down-2024`](./binance-busd-wind-down-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cba4eca`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

