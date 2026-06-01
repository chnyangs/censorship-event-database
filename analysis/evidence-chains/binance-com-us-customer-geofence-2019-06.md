# Evidence chain — `binance-com-us-customer-geofence-2019-06`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c3a88e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2019-06-14 Terms-of-Use update barring all U.S. persons from
> trading/depositing on binance.com (enforced 2019-09-12, with migration to
> the separate FinCEN-registered Binance.US) severed the global binance.com
> off-ramp for U.S. customers; single-layer offramp_cex observed_change with
> attribution=direct (Binance is both announcing actor and operator)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_holdings_limited`
- **Timestamp**: `2019-06-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/articles/360029196512>
  - Wayback: <https://web.archive.org/web/20190614192737/https://www.binance.com/en/support/articles/360029196512>
  - body_hash: `sha256:567ddd89e8f29dd0f8fb5b8190a080258bf0013dca0b944c9f3d9ea4a5b07224`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/official_support_360029196512/web.archive.org__web-20190614175800-https-www.binance.com-en-support-articles-360029196512__93d106315f.html`
  > Official Binance Support article "Terms of Use Review" (Wayback
> memento 2019-06-14 19:27:37 UTC). The captured body links to
> Binance's Terms of Use, says some users may need to furnish evidence
> that registrations are consistent with those Terms, and states that
> after 90 days, effective 2019-09-12, users not in accordance with the
> Terms would retain wallet/fund access but no longer be able to trade
> or deposit on Binance.com.
- **`primary_corporate`**
  - URL: <https://www.binance.com/agreement.html>
  - Wayback: <https://web.archive.org/web/20190614175800/https://www.binance.com/agreement.html>
  - body_hash: `sha256:cefd1bd90cacd52f998442695dfb474dc8f6cc2230a49e277b4faae81fc17a98`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/official_terms/web.archive.org__web-20190614104622-https-www.binance.com-agreement.html__3fbaa8673a.html`
  > Official Binance Terms of Use page captured by Wayback on 2019-06-14
> 17:58:00 UTC. Section 3 ("Prohibition of use") states that Binance is
> unable to provide services to any U.S. person and may restrict or deny
> services in selected jurisdictions. This primary artifact supplies the
> U.S.-person target class used by the support-announcement enforcement
> notice.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/06/14/crypto-exchange-binancecom-to-block-us-customers-from-trading/>
  - Wayback: <https://web.archive.org/web/20210921042151/https://www.coindesk.com/markets/2019/06/14/crypto-exchange-binancecom-to-block-us-customers-from-trading/>
  - body_hash: `sha256:3dee385b4d89d4fa787fb9a1f61fabe73c67393dc1a1a446b187fe75e0a322ea`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/primary/web.archive.org__web-20210921042151-https-www.coindesk.com-markets-2019-06-14-crypto-exchange-binancecom-to-block-us-customers-from-trading__accd4baaa0.html`
  > CoinDesk (Wayback 20210921042151) on Binance's 2019-06-14 Terms of Use
> update barring U.S. persons: the captured body states Binance "is
> unable to provide services to any U.S. person" and that non-compliant
> U.S. users will lose trade/deposit access on binance.com after
> "Sept. 12" (2019), with a separate FinCEN-registered Binance.US
> platform launching for the U.S. market. Captured body carries the
> "U.S. person" / "unable to provide services" / "Sept. 12" / "fincen"
> tokens.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Binance.com — U.S.-person customer geofence
- **Canonical domains**: `binance.com`

> Target is the U.S.-person user class of binance.com: all U.S. individual
> and corporate customers barred from trading/depositing on the global
> binance.com platform via the 2019-06-14 Terms-of-Use update. Complete at
> the class level (the whole U.S.-person cohort); migrated to the separate
> Binance.US platform.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_com_bars_us_persons_from_trading_and_deposits`

**Timestamp**: `2019-06-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/articles/360029196512>
  - Wayback: <https://web.archive.org/web/20190614192737/https://www.binance.com/en/support/articles/360029196512>
  - body_hash: `sha256:567ddd89e8f29dd0f8fb5b8190a080258bf0013dca0b944c9f3d9ea4a5b07224`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/official_support_360029196512/web.archive.org__web-20190614175800-https-www.binance.com-en-support-articles-360029196512__93d106315f.html`
  > Official Binance Support "Terms of Use Review" article: users not
> in accordance with Binance's Terms of Use would retain access to
> wallets and funds, but would no longer be able to trade or deposit
> on Binance.com after 90 days, effective 2019-09-12. Attribution is
> direct for the operator-state change because Binance is both the
> announcing actor and the operator of the restricted off-ramp.
- **`primary_corporate`**
  - URL: <https://www.binance.com/agreement.html>
  - Wayback: <https://web.archive.org/web/20190614175800/https://www.binance.com/agreement.html>
  - body_hash: `sha256:cefd1bd90cacd52f998442695dfb474dc8f6cc2230a49e277b4faae81fc17a98`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/official_terms/web.archive.org__web-20190614104622-https-www.binance.com-agreement.html__3fbaa8673a.html`
  > Official Binance Terms of Use, captured on the same day as the
> support notice, states that Binance is unable to provide services to
> any U.S. person. This supplies the target class for the support
> article's trade/deposit cutoff.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/06/14/crypto-exchange-binancecom-to-block-us-customers-from-trading/>
  - Wayback: <https://web.archive.org/web/20210921042151/https://www.coindesk.com/markets/2019/06/14/crypto-exchange-binancecom-to-block-us-customers-from-trading/>
  - body_hash: `sha256:3dee385b4d89d4fa787fb9a1f61fabe73c67393dc1a1a446b187fe75e0a322ea`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/primary/web.archive.org__web-20210921042151-https-www.coindesk.com-markets-2019-06-14-crypto-exchange-binancecom-to-block-us-customers-from-trading__accd4baaa0.html`
  > CoinDesk: Binance's 2019-06-14 ToS update ("unable to provide
> services to any U.S. person") with Sept-12 enforcement and a
> separate Binance.US platform. Retained as corroborating
> contemporaneous trade-press evidence after official Binance
> support and Terms artifacts were pinned.
- **`semi_primary_wayback`**
  - URL: <https://techcrunch.com/2019/06/14/binance-begins-to-restrict-us-customers/>
  - Wayback: <https://web.archive.org/web/20190614104622/https://techcrunch.com/2019/06/14/binance-begins-to-restrict-us-customers/>
  - body_hash: `sha256:d9156b1d39ca6deb4277a556ea7ef4552d783f6da1c0c5009bc02d2dabb964e2`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/primary/web.archive.org__web-20190614104622-https-techcrunch.com-2019-06-14-binance-begins-to-restrict-us-customers__1a503a0968.html`
  > TechCrunch (contemporaneous 2019-06-14 capture) corroboration of the
> Binance U.S.-customer restriction with September-12 enforcement.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`poloniex-circle-us-token-geofence-2019-05`](./poloniex-circle-us-token-geofence-2019-05.md)
- [`binance-russia-exit-commex-2023`](./binance-russia-exit-commex-2023.md)
- [`sec-v-binance-2023`](./sec-v-binance-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3a88e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

