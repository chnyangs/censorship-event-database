# Evidence chain — `poloniex-circle-us-token-geofence-2019-05`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f70cc98` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:48:55Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Poloniex's (Circle) 2019-05-29 disabling of trading for nine tokens
> (ARDR/BCN/DCR/GAME/GAS/LSK/NXT/OMNI/REP) for U.S. customers only severed the
> Poloniex off-ramp for these assets in the U.S. corridor; single-layer
> offramp_cex observed_change with attribution=direct for the Poloniex action
> itself. Poloniex cited generic U.S. securities-classification uncertainty,
> not a named legal instrument."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `poloniex_circle`
- **Timestamp**: `2019-05-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://medium.com/poloniex/poloniex-to-stop-offering-trading-of-9-assets-to-us-customers-all-assets-remain-available-to-b4c5703c0e9>
  - body_hash: `sha256:731147a66cc35d8d17fdd325924bc420ec0455ca344879e5a6cbd81c4bd49149`
  - body_path: `sources/http_captures/poloniex-circle-us-token-geofence-2019-05/official_medium/medium.com__circle-trader-poloniex-to-stop-offering-trading-of-9-assets-to-us-customers-all-assets-remain-available-to-b4c5703c0e9__2b2e4bf71f.html`
  > Official Poloniex Medium post, published 2019-05-16 by the Poloniex
> account. The captured body states that on 2019-05-29 at 16:00 UTC the
> ARDR, BCN, DCR, GAME, GAS, LSK, NXT, OMNI, and REP markets would be
> disabled for Poloniex customers in the U.S., while remaining available
> to non-U.S. customers. It also states the action resulted from
> regulatory uncertainty in the U.S. market and uncertainty over whether
> U.S. regulators would consider the assets securities.
- **`semi_primary_wayback`**
  - URL: <https://www.cryptoglobe.com/latest/2019/05/poloniex-will-disable-trading-for-nine-altcoins-for-u-s-customers-only/>
  - Wayback: <https://web.archive.org/web/20190523213503/https://www.cryptoglobe.com/latest/2019/05/poloniex-will-disable-trading-for-nine-altcoins-for-u-s-customers-only/>
  - body_hash: `sha256:a082154989678f094d26dbe5bed5aa54e1fdb908b2a31048d88236a664b17bda`
  - body_path: `sources/http_captures/poloniex-circle-us-token-geofence-2019-05/primary/web.archive.org__web-20190523213503-https-www.cryptoglobe.com-latest-2019-05-poloniex-will-disable-trading-for-nine-altcoins-for-u-s-customers-only__9b86ad4fbf.html`
  > CryptoGlobe (Wayback 20190523213503) on Poloniex's 2019-05-16
> announcement: Circle-owned Poloniex will disable trading for nine
> altcoins — Ardor (ARDR), Bytecoin (BCN), Decred (DCR), GameCredits
> (GAME), Gas (GAS), Lisk (LSK), Nxt (NXT), OMNI, Augur (REP) — for
> U.S. customers ONLY, effective Friday May 29 2019 16:00 UTC, citing
> regulatory (securities-classification) uncertainty. The captured body
> enumerates all nine tickers, "May 29", and the U.S.-only scope.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: Poloniex (Circle) — nine-token U.S.-customer geofence
- **Chains**: `ardor`, `bytecoin`, `decred`, `gamecredits`, `gas`, `lisk`, `nxt`, `omni`, `augur`

> Nine tokens geofenced from U.S. Poloniex customers: Ardor (ARDR),
> Bytecoin (BCN), Decred (DCR), GameCredits (GAME), Gas (GAS), Lisk (LSK),
> Nxt (NXT), OMNI, Augur (REP). Complete enumeration of the disabled asset
> set; the assets remained available to Poloniex customers in all other
> jurisdictions and continue on their own chains.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 328h

**Event label**: `poloniex_disables_nine_token_markets_for_us_customers`

**Timestamp**: `2019-05-29 16:00:00+00:00` (precision: `hour`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://medium.com/poloniex/poloniex-to-stop-offering-trading-of-9-assets-to-us-customers-all-assets-remain-available-to-b4c5703c0e9>
  - body_hash: `sha256:731147a66cc35d8d17fdd325924bc420ec0455ca344879e5a6cbd81c4bd49149`
  - body_path: `sources/http_captures/poloniex-circle-us-token-geofence-2019-05/official_medium/medium.com__circle-trader-poloniex-to-stop-offering-trading-of-9-assets-to-us-customers-all-assets-remain-available-to-b4c5703c0e9__2b2e4bf71f.html`
  > Official Poloniex post: the nine named markets would be disabled for
> Poloniex U.S. customers at 2019-05-29 16:00 UTC while remaining
> available outside the U.S. attribution=direct for the corporate
> geofence action because Poloniex names the assets, user class, and
> effective time itself. The regulatory-uncertainty rationale remains
> generic rather than tied to a named legal instrument.
- **`semi_primary_wayback`**
  - URL: <https://www.cryptoglobe.com/latest/2019/05/poloniex-will-disable-trading-for-nine-altcoins-for-u-s-customers-only/>
  - Wayback: <https://web.archive.org/web/20190523213503/https://www.cryptoglobe.com/latest/2019/05/poloniex-will-disable-trading-for-nine-altcoins-for-u-s-customers-only/>
  - body_hash: `sha256:a082154989678f094d26dbe5bed5aa54e1fdb908b2a31048d88236a664b17bda`
  - body_path: `sources/http_captures/poloniex-circle-us-token-geofence-2019-05/primary/web.archive.org__web-20190523213503-https-www.cryptoglobe.com-latest-2019-05-poloniex-will-disable-trading-for-nine-altcoins-for-u-s-customers-only__9b86ad4fbf.html`
  > CryptoGlobe: Poloniex (Circle) nine-token U.S.-customer geofence,
> effective 2019-05-29 16:00 UTC. Corroborating semi-primary replay
> source retained after the official Poloniex post was pinned.
- **`semi_primary_wayback`**
  - URL: <https://coingeek.com/poloniex-disables-markets-for-9-crypto-tokens-but-only-for-us-clients/>
  - Wayback: <https://web.archive.org/web/20190820083551/https://coingeek.com/poloniex-disables-markets-for-9-crypto-tokens-but-only-for-us-clients/>
  - body_hash: `sha256:8c36623874f82ccccfe3995879bad3ed4e384db16ff89f63d69fce4003e1bc4c`
  - body_path: `sources/http_captures/poloniex-circle-us-token-geofence-2019-05/primary/web.archive.org__web-20190820083551-https-coingeek.com-poloniex-disables-markets-for-9-crypto-tokens-but-only-for-us-clients__a8933b13ca.html`
  > CoinGeek corroboration of the Poloniex 9-token U.S.-only market
> disabling over securities-classification uncertainty. Independent
> second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-com-us-customer-geofence-2019-06`](./binance-com-us-customer-geofence-2019-06.md)
- [`sec-poloniex-unregistered-exchange-2021-08`](./sec-poloniex-unregistered-exchange-2021-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f70cc98`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

