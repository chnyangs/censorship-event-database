# Evidence chain — `google-play-india-crypto-exchange-removal-2024-01`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad910b8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:40:01Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `google_llc`
- **Timestamp**: `2024-01-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://techcrunch.com/2024/01/13/google-pulls-binance-other-global-crypto-apps-from-india-store/>
  - Wayback: <https://web.archive.org/web/2024/https://techcrunch.com/2024/01/13/google-pulls-binance-other-global-crypto-apps-from-india-store/>
  > TechCrunch (2024-01-13/14): "Google pulls Binance, other global crypto
> apps from India store." Reports Google Play India removed Binance,
> Kraken, KuCoin, Huobi, Gate.io, Bittrex, MEXC, and Bitfinex apps from
> the regional storefront, following the FIU-IND 2023-12-28 show-cause
> notices and Apple's earlier App Store India removal (2024-01-09 to
> 2024-01-10). Google's action followed Apple's by approximately four
> days. Marked evidence_use=contextual_unarchived per author constraint;
> Wayback wildcard pointer (web/2024/) in lieu of a pinned-timestamp
> snapshot; body_hash + body_path archival capture deferred to human
> audit pass.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/google-play-store-removes-binance-others-in-response-to-indian-fiu-notice>
  - Wayback: <https://web.archive.org/web/2024/https://cointelegraph.com/news/google-play-store-removes-binance-others-in-response-to-indian-fiu-notice>
  > Cointelegraph (2024-01-14): "Google Play Store removes Binance, others
> in response to Indian FIU notice." Confirms Google Play India removal
> as compliance action downstream of the FIU-IND 2023-12-28 enforcement
> cascade. Names same enumerated app set as TechCrunch coverage.
> Wayback wildcard pointer pending pinned snapshot during human audit.
- **`supporting_journalism`**
  - URL: <https://www.pymnts.com/cryptocurrency/2024/google-follows-apple-in-yanking-crypto-apps-in-india/>
  - Wayback: <https://web.archive.org/web/2024/https://www.pymnts.com/cryptocurrency/2024/google-follows-apple-in-yanking-crypto-apps-in-india/>
  > PYMNTS (2024-01-14): "Google Follows Apple in Yanking Crypto Apps in
> India." Anchors the four-day temporal gap between Apple App Store IN
> removal (2024-01-09 to 2024-01-10) and Google Play IN removal
> (2024-01-13 to 2024-01-14). Wayback wildcard pointer; pinned snapshot
> deferred.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Offshore VDA exchange apps on Google Play IN regional storefront
- **Canonical domains**: `binance.com`, `okx.com`, `kraken.com`, `kucoin.com`, `mexc.com`, `bitfinex.com`, `bittrex.com`

> Seven offshore Virtual Digital Asset (VDA) exchange apps removed from the
> Google Play India regional storefront on 2024-01-13/14: Binance, OKX,
> Kraken, KuCoin, MEXC Global, Bitfinex, and Bittrex. Subset framing
> because (a) the FIU-IND show-cause notice population was nine platforms
> (Binance, Kraken, KuCoin, Huobi, OKX, Bitstamp, MEXC Global, BitTrex,
> Gate.io) but per-platform Google Play storefront enumeration in mid-
> January press coverage names different subsets (e.g. some sources add
> Huobi and Gate.io); (b) some platforms (e.g. Binance, KuCoin) later
> re-registered with FIU-IND and partially restored Indian Play access.
> Enumeration here uses the title-line set provided in the authoring
> brief; cross-source reconciliation deferred to human audit.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `seven_offshore_vda_apps_removed_from_google_play_in_regional_storefront`

**Timestamp**: `2024-01-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://techcrunch.com/2024/01/13/google-pulls-binance-other-global-crypto-apps-from-india-store/>
  - Wayback: <https://web.archive.org/web/20240114014815/https://techcrunch.com/2024/01/13/google-pulls-binance-other-global-crypto-apps-from-india-store/>
  - body_hash: `sha256:376d00b85813d34b9cdbb57aa1d59767e2c8ac0aaffc907928a2f890f56a5ea5`
  - body_path: `sources/http_captures/google-play-india-crypto-exchange-removal-2024-01/primary/web.archive.org__web-20240114000000-https-techcrunch.com-2024-01-13-google-pulls-binance-other-global-crypto-apps-from-india-store__a736d71074.html`
  > TechCrunch 2024-01-13: Google pulled Binance and other global
> crypto apps from its India Play Store following the Indian FIU notice.
> Independent semi-primary anchor (replaces unarchivable Binance tweet).
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/google-play-store-removes-binance-others-in-response-to-indian-fiu-notice>
  - Wayback: <https://web.archive.org/web/20240114074027/https://cointelegraph.com/news/google-play-store-removes-binance-others-in-response-to-indian-fiu-notice>
  - body_hash: `sha256:9239322b05528164da8f7a565c08936ac08ea04199cebf977bd747bcb6796f96`
  - body_path: `sources/http_captures/google-play-india-crypto-exchange-removal-2024-01/primary/web.archive.org__web-20240114000000-https-cointelegraph.com-news-google-play-store-removes-binance-others-in-response-to-indian-fiu-notice__426c891ab1.html`
  > Cointelegraph 2024-01 corroboration of the Google Play India
> crypto-app removals per the FIU notice. Independent second semi-primary.

## 5. Honest coverage gaps

- **offramp_cex** (`not_measured`): Downstream INR on/off-ramp severance for IN-resident users of the

## 7. Related events

- [`india-fiu-offshore-vda-block-2023`](./india-fiu-offshore-vda-block-2023.md)
- [`apple-india-crypto-exchange-removal-2024-01`](./apple-india-crypto-exchange-removal-2024-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad910b8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

