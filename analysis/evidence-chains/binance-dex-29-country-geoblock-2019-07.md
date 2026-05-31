# Evidence chain — `binance-dex-29-country-geoblock-2019-07`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1b889eb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance DEX's 2019-07-01 IP-geolocation geo-block of the binance.org web
> interface for users from 29 jurisdictions (the U.S. plus 28 sanctioned/
> restricted countries including Iran, Cuba, Syria, North Korea) restricted
> frontend access to the Binance DEX while leaving the underlying chain
> reachable via alternative wallets; single-layer l4_frontend observed_change
> with attribution=plausible (broad compliance geofence, no single named
> instrument)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_org_binance_dex`
- **Timestamp**: `2019-06-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/news/binance-dex-to-geoblock-traders-from-29-countries-us-included/>
  - Wayback: <https://web.archive.org/web/20190607134838/https://www.financemagnates.com/cryptocurrency/news/binance-dex-to-geoblock-traders-from-29-countries-us-included/>
  - body_hash: `sha256:628f19716d0fce5c46df4ce3fc216b4e8394f611d6aa1aee53e1f7b18676004f`
  - body_path: `sources/http_captures/binance-dex-29-country-geoblock-2019-07/primary/web.archive.org__web-20190607134838-https-www.financemagnates.com-cryptocurrency-news-binance-dex-to-geoblock-traders-from-29-countries-us-included__86aacc573c.html`
  > Finance Magnates (Wayback 20190607134838) on the Binance DEX geoblock:
> the binance.org web interface will geo-block users by IP address from
> 29 countries — the United States and 28 others including Iran, Cuba,
> Syria and North Korea — beginning July 1 2019. The captured body
> carries "29 Countries", "geoblock"/"geo-block", "July 1",
> "United States", "Iran", "Cuba", "Syria", "binance.org" and the
> IP-address mechanism. CZ clarified that binance.org (the frontend) is
> barring users, not the underlying DEX blockchain.

## 2. Target

- **Kind**: `domain`
- **Enumeration**: `subset`
- **Actor name**: Binance DEX (binance.org) — 29-country frontend geo-block
- **Canonical domains**: `binance.org`

> Target is the binance.org web interface (the Binance DEX frontend) for
> users in 29 IP-geolocated jurisdictions. Named in the coverage: United
> States, Albania, Belarus, Bosnia & Herzegovina, Burma (Myanmar), Central
> African Republic, DR Congo, North Korea, Cote d'Ivoire, Crimea (Ukraine),
> Croatia, Cuba, Iran, Iraq, Kosovo, Lebanon, Liberia, Libya, North
> Macedonia, Moldova, Serbia, Somalia, Sudan, South Sudan, Syria, Venezuela,
> Yemen, Zimbabwe. enumeration=subset because most of the 29 jurisdictions
> are not separately coded as event jurisdictions here; the U.S. is the
> load-bearing, vocab-coded jurisdiction and the others are carried as a
> text list. The DEX blockchain itself was not blocked — only the
> binance.org frontend, accessible via alternative wallets.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 576h

**Event label**: `binance_org_dex_frontend_geoblocks_29_countries`

**Timestamp**: `2019-07-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/news/binance-dex-to-geoblock-traders-from-29-countries-us-included/>
  - Wayback: <https://web.archive.org/web/20190607134838/https://www.financemagnates.com/cryptocurrency/news/binance-dex-to-geoblock-traders-from-29-countries-us-included/>
  - body_hash: `sha256:628f19716d0fce5c46df4ce3fc216b4e8394f611d6aa1aee53e1f7b18676004f`
  - body_path: `sources/http_captures/binance-dex-29-country-geoblock-2019-07/primary/web.archive.org__web-20190607134838-https-www.financemagnates.com-cryptocurrency-news-binance-dex-to-geoblock-traders-from-29-countries-us-included__86aacc573c.html`
  > Finance Magnates (announcement snapshot): binance.org frontend
> geo-block of 29 countries effective 2019-07-01. attribution=plausible
> — Binance applied the frontend geofence as a broad compliance policy
> covering the U.S. plus sanctioned/restricted jurisdictions, without a
> single named legal instrument acting on binance.org (§1.4: provider
> does not cite a specific per-trigger instrument).
- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/news/binance-dex-to-geoblock-traders-from-29-countries-us-included/>
  - Wayback: <https://web.archive.org/web/20190714020909/https://www.financemagnates.com/cryptocurrency/news/binance-dex-to-geoblock-traders-from-29-countries-us-included/>
  - body_hash: `sha256:496ae2790f494f86f4171784e5103b508cdbbf27b26e87d335a12fa4ba1b5644`
  - body_path: `sources/http_captures/binance-dex-29-country-geoblock-2019-07/primary/web.archive.org__web-20190714020909-https-www.financemagnates.com-cryptocurrency-news-binance-dex-to-geoblock-traders-from-29-countries-us-included__7902d53d42.html`
  > Second Finance Magnates Wayback snapshot (20190714, after the
> 2019-07-01 effective date) of the same article, anchoring the
> post-effective-date persistence of the binance.org frontend
> geo-block. Independent timestamp anchor for the load-bearing claim.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-com-us-customer-geofence-2019-06`](./binance-com-us-customer-geofence-2019-06.md)
- [`1inch-us-geofence-2021-09`](./1inch-us-geofence-2021-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1b889eb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

