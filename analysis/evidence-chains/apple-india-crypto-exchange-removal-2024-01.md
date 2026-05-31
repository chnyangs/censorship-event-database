# Evidence chain — `apple-india-crypto-exchange-removal-2024-01`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a4484c4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2024-01-10, Apple removed offshore Virtual Digital Asset exchange
> apps (Binance, OKX, Kraken, KuCoin, MEXC Global, Bitfinex, Bittrex,
> Bitstamp) from the Apple App Store India regional storefront as a
> corporate compliance response to the FIU-IND 2023-12-28 show-cause
> notices and the MEITY section 69A URL blocking order. Observational
> axis at l4_frontend (Apple App Store IN regional removal).
> Admission-anchor-grade promotion pending pinned App Store IN
> availability snapshots."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `APPLE`
- **Timestamp**: `2024-01-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://techcrunch.com/2024/01/09/apple-crypto-apps-binance-india/>
  - Wayback: <https://web.archive.org/web/2024/https://techcrunch.com/2024/01/09/apple-crypto-apps-binance-india/>
  > TechCrunch 2024-01-09/10 coverage reporting that Apple removed
> Binance, KuCoin, OKX, Kraken, Bitstamp, MEXC Global, Bitfinex,
> Bittrex, and other offshore VDA exchange apps from the Apple App
> Store India regional storefront. Action occurred days after the
> FIU-IND 2023-12-28 show-cause notices and the MEITY section 69A
> URL blocking order. Wayback wildcard pointer (web/2024/) in lieu
> of a pinned-timestamp snapshot; evidence_use=contextual_unarchived
> because no body_hash+body_path pair has been captured into
> sources/http_captures/apple-india-crypto-exchange-removal-2024-01/
> in this session.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2024/01/10/binance-kucoin-other-exchanges-served-notice-by-indian-government-removed-from-apples-app-store>
  - Wayback: <https://web.archive.org/web/2024/https://www.coindesk.com/policy/2024/01/10/binance-kucoin-other-exchanges-served-notice-by-indian-government-removed-from-apples-app-store>
  > CoinDesk 2024-01-10 reporting on the Apple App Store India
> regional removals naming Binance, KuCoin, and the broader FIU-IND
> show-cause class. Wayback wildcard pointer in lieu of pinned
> snapshot.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/apple-india-binance-kraken-crypto-exchanges-delist-fiu-notice>
  - Wayback: <https://web.archive.org/web/2024/https://cointelegraph.com/news/apple-india-binance-kraken-crypto-exchanges-delist-fiu-notice>
  > Cointelegraph 2024-01-10 coverage confirming the Apple App Store
> India removal cascade. Notes that OKX was also pulled even though
> it was not directly named in the FIU-IND show-cause notice cohort.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Offshore VDA exchanges (Apple App Store IN regional storefront, FIU-IND cascade)
- **Canonical domains**: `binance.com`, `okx.com`, `kraken.com`, `kucoin.com`, `mexc.com`, `bitfinex.com`, `bittrex.com`, `bitstamp.net`

> Apple App Store India regional removal cohort: Binance, OKX, Kraken,
> KuCoin, MEXC Global, Bitfinex, Bittrex, Bitstamp, Huobi, Gate.io.
> Overlaps with but is not identical to the FIU-IND 2023-12-28
> show-cause cohort (OKX was removed by Apple although not in the
> FIU-IND named-nine; Huobi/Gate.io enumeration in press reporting is
> incomplete). Subset rather than complete: pinned per-app App Store IN
> availability snapshots have not been captured in this session.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `offshore_vda_exchange_apps_removed_from_apple_app_store_in_regional_storefront`

**Timestamp**: `2024-01-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://techcrunch.com/2024/01/09/apple-crypto-apps-binance-india/>
  - Wayback: <https://web.archive.org/web/20240110032452/https://techcrunch.com/2024/01/09/apple-crypto-apps-binance-india/>
  - body_hash: `sha256:7591234aa85b03f5be1fb5dc4f0628874f9817430e21e6404a052aab7d25210f`
  - body_path: `sources/http_captures/apple-india-crypto-exchange-removal-2024-01/primary/web.archive.org__web-20240110000000-https-techcrunch.com-2024-01-09-apple-crypto-apps-binance-india__ba5097b1f3.html`
  > TechCrunch 2024-01-09: Apple removed Binance and other crypto
> exchange apps from its India App Store following the Indian FIU notice.
> Independent semi-primary anchor (replaces unarchivable Binance tweet).
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/01/10/binance-kucoin-other-exchanges-served-notice-by-indian-government-removed-from-apples-app-store>
  - Wayback: <https://web.archive.org/web/20240110205329/https://www.coindesk.com/policy/2024/01/10/binance-kucoin-other-exchanges-served-notice-by-indian-government-removed-from-apples-app-store/>
  - body_hash: `sha256:136d065ee7b942d7be875ce6bbb904ddb214acc49ac804fca7a66ced6f0dbb0a`
  - body_path: `sources/http_captures/apple-india-crypto-exchange-removal-2024-01/primary/web.archive.org__web-20240111000000-https-www.coindesk.com-policy-2024-01-10-binance-kucoin-other-exchanges-served-notice-by-indian-government-removed-from-apples-app-s__dafb2ced4f.html`
  > CoinDesk 2024-01-10 corroboration of the Apple App Store India
> crypto-exchange removals per the FIU notice. Independent second semi-primary.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`india-fiu-offshore-vda-block-2023`](./india-fiu-offshore-vda-block-2023.md)
- [`google-play-india-crypto-exchange-removal-2024-01`](./google-play-india-crypto-exchange-removal-2024-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a4484c4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

