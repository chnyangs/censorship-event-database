# Evidence chain — `binance-russia-exit-commex-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b6c6fae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-09-27 Binance Holdings Limited Russia-market divestiture to
> CommEX is retained as a narrowed CEX/off-ramp market-exit observation:
> Binance's own PRNewswire release announced the sale of the entirety of
> its Russia business, up-to-one-year off-boarding for existing Russian
> users, redirection of some Russian KYC'd new-user registration to CommEX,
> and sunset of all Binance exchange services and business lines in Russia
> over the following months. The row does not claim a replayably measured
> Binance/CommEX L4 frontend change, RUB-specific rail shutdown, L0
> network blocking, L1 consensus impact, L3 RPC filtering, or asset-onchain
> freeze."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance_holdings_limited`
- **Timestamp**: `2023-09-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html>
  - body_hash: `sha256:a6cdb7081b51df793a5beefc20866e02cf41d33d0141f1ddade7c9f94f102200`
  - body_path: `sources/http_captures/binance-russia-exit-commex-2023/primary/www.prnewswire.com__news-releases-binance-fully-exits-russia-with-sale-to-commex-301940042.html__e360ad5131.html`
  > Binance-issued PRNewswire release dated 2023-09-27 announcing that
> Binance had agreed to sell the entirety of its Russia business to
> CommEX. The release states that existing Russian-user off-boarding
> would take up to one year, that some Russian KYC'd new-user
> registration would be redirected to CommEX, and that Binance would
> sunset all exchange services and business lines in Russia over the
> following months. Captured locally 2026-06-01 with replayable
> body_hash/body_path.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Holdings Limited (Russia market) / CommEX
- **Canonical domains**: `binance.com`, `commex.com`

> Binance Holdings Limited Russia-market business line and the affected
> Russian-user migration corridor to CommEX. This repaired row no longer
> treats Russian-localized Binance pages, in-account notifications, a
> CommEX landing page, or RUB-specific P2P rails as independently
> measured surfaces. The retained target is the source-supported
> corporate divestiture, Russian-user off-boarding, new-user redirection,
> and sunset of Binance exchange services and business lines in Russia.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_russia_business_sale_user_offboarding_and_exchange_service_sunset`

**Timestamp**: `2023-09-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.prnewswire.com/news-releases/binance-fully-exits-russia-with-sale-to-commex-301940042.html>
  - body_hash: `sha256:a6cdb7081b51df793a5beefc20866e02cf41d33d0141f1ddade7c9f94f102200`
  - body_path: `sources/http_captures/binance-russia-exit-commex-2023/primary/www.prnewswire.com__news-releases-binance-fully-exits-russia-with-sale-to-commex-301940042.html__e360ad5131.html`
  > Binance-issued PRNewswire release states that Binance entered an
> agreement to sell its entire Russia business to CommEX, with
> existing Russian-user off-boarding over up to one year, some
> Russian KYC'd new-user registrations redirected to CommEX, and all
> Binance exchange services and business lines in Russia sunset over
> the following months. Attribution is direct because Binance is the
> announcing actor and operator of the divested Russia-market
> exchange services.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): The previous row treated Binance Russian-locale frontend notices and

## 7. Related events

- [`binance-4framework-2023`](./binance-4framework-2023.md)
- [`eu-russia-crypto-wallet-cap-2022`](./eu-russia-crypto-wallet-cap-2022.md)
- [`eu-russia-full-crypto-wallet-ban-2022`](./eu-russia-full-crypto-wallet-ban-2022.md)
- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)
- [`coinbase-india-exit-2022`](./coinbase-india-exit-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b6c6fae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

