# Evidence chain — `binance-com-us-customer-geofence-2019-06`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `6293bc1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

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

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `binance_com_bars_us_persons_from_trading_and_deposits`

**Timestamp**: `2019-06-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/06/14/crypto-exchange-binancecom-to-block-us-customers-from-trading/>
  - Wayback: <https://web.archive.org/web/20210921042151/https://www.coindesk.com/markets/2019/06/14/crypto-exchange-binancecom-to-block-us-customers-from-trading/>
  - body_hash: `sha256:3dee385b4d89d4fa787fb9a1f61fabe73c67393dc1a1a446b187fe75e0a322ea`
  - body_path: `sources/http_captures/binance-com-us-customer-geofence-2019-06/primary/web.archive.org__web-20210921042151-https-www.coindesk.com-markets-2019-06-14-crypto-exchange-binancecom-to-block-us-customers-from-trading__accd4baaa0.html`
  > CoinDesk: Binance's 2019-06-14 ToS update ("unable to provide
> services to any U.S. person") with Sept-12 enforcement and a
> separate Binance.US platform. attribution=direct: Binance is both
> the announcing actor and the operator of the restricted off-ramp,
> and its own ToS statement is the stated rationale.
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

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `6293bc1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

