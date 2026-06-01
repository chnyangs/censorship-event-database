# Evidence chain — `bittrex-privacy-coin-delisting-2021-01`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `db44253` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:52:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bittrex's 2021-01-15 removal of the Monero/Zcash/Dash trading markets
> (the first U.S.-exchange privacy-coin delisting) severed the Bittrex
> offramp for these assets; single-layer offramp_cex observed_change with
> attribution=plausible (no explicit Bittrex rationale stated)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `bittrex`
- **Timestamp**: `2021-01-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2021/01/01/bittrex-to-delist-privacy-coins-monero-dash-and-zcash>
  - Wayback: <https://web.archive.org/web/20210924223600/https://www.coindesk.com/markets/2021/01/01/bittrex-to-delist-privacy-coins-monero-dash-and-zcash/>
  - body_hash: `sha256:ba86a3e7b95a384c04b8e01c605aa340bd79d92ad1860e9b9cd27e996a379da5`
  - body_path: `sources/http_captures/bittrex-privacy-coin-delisting-2021-01/primary/web.archive.org__web-20210105000000-https-www.coindesk.com-markets-2021-01-01-bittrex-to-delist-privacy-coins-monero-dash-and-zcash__20b4279319.html`
  > CoinDesk 2021-01-01: Bittrex announced it will delist privacy
> coins Monero (XMR), Zcash (ZEC), and Dash (DASH); markets removed
> 2021-01-15 23:00 UTC. The first U.S.-based exchange to delist
> privacy coins, amid the KYC/AML compliance trend. Bittrex gave no
> explicit reason. Wayback 20210924223600 pinned.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/53012/bittrex-to-delist-privacy-coins-monero-zcash-and-dash-in-two-weeks>
  - Wayback: <https://web.archive.org/web/20210104061602/https://decrypt.co/53012/bittrex-to-delist-privacy-coins-monero-zcash-and-dash-in-two-weeks>
  - body_hash: `sha256:109fe61b58409e5e047339f2c04bef8419be3b144b219cd9f00b8603019880cd`
  - body_path: `sources/http_captures/bittrex-privacy-coin-delisting-2021-01/primary/web.archive.org__web-20210105000000-https-decrypt.co-53012-bittrex-to-delist-privacy-coins-monero-zcash-and-dash-in-two-weeks__c2b9ffb649.html`
  > Decrypt 2021-01 corroboration of the Bittrex XMR/ZEC/DASH
> delisting (effective 2021-01-15). Independent semi-primary anchor.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: Monero (XMR) + Zcash (ZEC) + Dash (DASH) on Bittrex
- **Chains**: `monero`, `zcash`, `dash`

> Three privacy-coin markets removed from Bittrex: Monero (XMR), Zcash
> (ZEC), Dash (DASH). Complete enumeration of the delisted asset set;
> the action removes the Bittrex trading/offramp markets for these
> base-chain assets (no contract; the assets remain on their own chains).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 336h

**Event label**: `bittrex_removes_xmr_zec_dash_privacy_coin_markets`

**Timestamp**: `2021-01-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2021/01/01/bittrex-to-delist-privacy-coins-monero-dash-and-zcash>
  - Wayback: <https://web.archive.org/web/20210924223600/https://www.coindesk.com/markets/2021/01/01/bittrex-to-delist-privacy-coins-monero-dash-and-zcash/>
  - body_hash: `sha256:ba86a3e7b95a384c04b8e01c605aa340bd79d92ad1860e9b9cd27e996a379da5`
  - body_path: `sources/http_captures/bittrex-privacy-coin-delisting-2021-01/primary/web.archive.org__web-20210105000000-https-www.coindesk.com-markets-2021-01-01-bittrex-to-delist-privacy-coins-monero-dash-and-zcash__20b4279319.html`
  > CoinDesk 2021-01-01: Bittrex XMR/ZEC/DASH market removal
> (effective 2021-01-15). attribution=plausible: the delisting is
> directly observed, but Bittrex gave no explicit reason, so the
> KYC/AML-compliance motive is the contextual inference rather
> than a stated rationale.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/53012/bittrex-to-delist-privacy-coins-monero-zcash-and-dash-in-two-weeks>
  - Wayback: <https://web.archive.org/web/20210104061602/https://decrypt.co/53012/bittrex-to-delist-privacy-coins-monero-zcash-and-dash-in-two-weeks>
  - body_hash: `sha256:109fe61b58409e5e047339f2c04bef8419be3b144b219cd9f00b8603019880cd`
  - body_path: `sources/http_captures/bittrex-privacy-coin-delisting-2021-01/primary/web.archive.org__web-20210105000000-https-decrypt.co-53012-bittrex-to-delist-privacy-coins-monero-zcash-and-dash-in-two-weeks__c2b9ffb649.html`
  > Decrypt corroboration of the Bittrex privacy-coin delisting.
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`kraken-monero-eu-delisting-2024`](./kraken-monero-eu-delisting-2024.md)
- [`huobi-htx-privacy-coin-delisting-2024`](./huobi-htx-privacy-coin-delisting-2024.md)
- [`okx-privacy-token-delist-2024`](./okx-privacy-token-delist-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `db44253`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

