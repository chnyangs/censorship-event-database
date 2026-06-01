# Evidence chain — `bybit-france-exit-2024-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `2dfaf57` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bybit's 2024-12-17 termination of withdrawal/custody services for
> French-resident users (withdraw-by 2025-01-08) severed the Bybit
> off-ramp in France amid French-regulator developments; single-layer
> offramp_cex observed_change, attribution=direct for the Bybit service
> termination (regulatory-driver specificity remains generic, not a
> Bybit-cited AMF instrument). Later reversed (AMF de-listing 2025-02-14)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `bybit`
- **Timestamp**: `2024-12-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.bybit.com/en/help-center/article/How-to-Onboard-Coinhouse-and-Manage-Your-Assets>
  - body_hash: `sha256:79e09ba4530055d5df75a1364cc8505fa826771e04b42cdbb12f51482b2b0cb6`
  - body_path: `sources/http_captures/bybit-france-exit-2024-12/official-bybit/www.bybit.com__en-help-center-article-How-to-Onboard-Coinhouse-and-Manage-Your-Assets__4d26279d3f.html`
  > Official Bybit help-center article "How to Onboard Coinhouse and
> Manage Your Assets" (last updated 2024-12-17 00:05:23). Bybit
> states that, in light of recent developments by the French
> regulator and prior restrictions in France, it would no longer
> provide withdrawal and custody services to nationals or residents
> of the French Territories starting 2025-01-08; residual balances
> above 10 USDC would be converted/transferred through Coinhouse.
- **`semi_primary_wayback`**
  - URL: <https://www.fxleaders.com/news/2024/12/17/bybit-to-end-services-in-france-key-deadlines-and-next-steps-for-users/>
  - Wayback: <https://web.archive.org/web/20250327225010/https://www.fxleaders.com/news/2024/12/17/bybit-to-end-services-in-france-key-deadlines-and-next-steps-for-users/>
  - body_hash: `sha256:8e69c8cffcc27109edd08f805b80e3477a0e5fa2bc78f5abd2b562d34ab5bdbb`
  - body_path: `sources/http_captures/bybit-france-exit-2024-12/primary/web.archive.org__web-20241218000000-https-www.fxleaders.com-news-2024-12-17-bybit-to-end-services-in-france-key-deadlines-and-next-steps-for-users__267a0afd51.html`
  > FX Leaders 2024-12-17: Bybit announced it will terminate
> withdrawal and custody services for French users, asking French
> users to withdraw before 2025-01-08 to avoid disruption. The
> French AMF had blacklisted Bybit since 2022 and in May 2024
> warned that Bybit was not authorized to provide digital-asset
> services in France; Bybit partnered with regulated French
> platform Coinhouse to return balances above 10 USDC.
- **`semi_primary_wayback`**
  - URL: <https://beincrypto.com/bybit-france-crypto-services-end-january-2025/>
  - Wayback: <https://web.archive.org/web/20241218104424/https://beincrypto.com/bybit-france-crypto-services-end-january-2025/>
  - body_hash: `sha256:350318c5ac66766b11d407a537ccd6d931e9b19d088abe6dc46428363f8e893e`
  - body_path: `sources/http_captures/bybit-france-exit-2024-12/primary/web.archive.org__web-20241218000000-https-beincrypto.com-bybit-france-crypto-services-end-january-2025__e7acda9ab1.html`
  > BeInCrypto 2024-12-18 corroboration: Bybit to end crypto
> services for French users by 2025-01-08 amid AMF regulatory
> pressure. Independent second semi-primary anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Bybit (French-user withdrawal/custody services)

> Bybit's withdrawal/custody service surface for users resident in
> France. The action geofences the Bybit offramp out of one national
> jurisdiction (France); not an asset-level delisting.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 528h

**Event label**: `bybit_ends_withdrawal_custody_services_for_french_users`

**Timestamp**: `2025-01-08 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.bybit.com/en/help-center/article/How-to-Onboard-Coinhouse-and-Manage-Your-Assets>
  - body_hash: `sha256:79e09ba4530055d5df75a1364cc8505fa826771e04b42cdbb12f51482b2b0cb6`
  - body_path: `sources/http_captures/bybit-france-exit-2024-12/official-bybit/www.bybit.com__en-help-center-article-How-to-Onboard-Coinhouse-and-Manage-Your-Assets__4d26279d3f.html`
  > Official Bybit article: Bybit states that it would no longer
> provide withdrawal and custody services to French users starting
> 2025-01-08 at 08:00 UTC. attribution=direct for the Bybit service
> termination; the regulatory-driver wording remains scoped to
> Bybit's generic "French regulator"/"relevant regulations" phrasing,
> not a named AMF instrument.
- **`semi_primary_wayback`**
  - URL: <https://www.fxleaders.com/news/2024/12/17/bybit-to-end-services-in-france-key-deadlines-and-next-steps-for-users/>
  - Wayback: <https://web.archive.org/web/20250327225010/https://www.fxleaders.com/news/2024/12/17/bybit-to-end-services-in-france-key-deadlines-and-next-steps-for-users/>
  - body_hash: `sha256:8e69c8cffcc27109edd08f805b80e3477a0e5fa2bc78f5abd2b562d34ab5bdbb`
  - body_path: `sources/http_captures/bybit-france-exit-2024-12/primary/web.archive.org__web-20241218000000-https-www.fxleaders.com-news-2024-12-17-bybit-to-end-services-in-france-key-deadlines-and-next-steps-for-users__267a0afd51.html`
  > FX Leaders 2024-12-17: Bybit French-user withdrawal/custody
> termination (deadline 2025-01-08). Retained as corroboration and
> AMF-context reporting; the official Bybit source carries the direct
> service-termination attribution.
- **`semi_primary_wayback`**
  - URL: <https://beincrypto.com/bybit-france-crypto-services-end-january-2025/>
  - Wayback: <https://web.archive.org/web/20241218104424/https://beincrypto.com/bybit-france-crypto-services-end-january-2025/>
  - body_hash: `sha256:350318c5ac66766b11d407a537ccd6d931e9b19d088abe6dc46428363f8e893e`
  - body_path: `sources/http_captures/bybit-france-exit-2024-12/primary/web.archive.org__web-20241218000000-https-beincrypto.com-bybit-france-crypto-services-end-january-2025__e7acda9ab1.html`
  > BeInCrypto corroboration of the Bybit French-user service exit.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bybit-singapore-exit-2022`](./bybit-singapore-exit-2022.md)
- [`hongkong-sfc-bybit-warning-2024`](./hongkong-sfc-bybit-warning-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2dfaf57`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

