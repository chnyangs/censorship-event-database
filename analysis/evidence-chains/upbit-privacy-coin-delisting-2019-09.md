# Evidence chain — `upbit-privacy-coin-delisting-2019-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `ad034bc` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:58:50Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Upbit's 2019-09-30 removal of transaction support for the
> XMR/DASH/ZEC/XHV/TUBE/PIVX markets (citing money-laundering concerns and
> FATF guidance) severed the Upbit off-ramp for these privacy assets;
> single-layer offramp_cex observed_change with attribution=plausible
> (soft-framework compliance inference, no named instrument)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `upbit_dunamu`
- **Timestamp**: `2019-09-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - Wayback: <https://web.archive.org/web/20210917015654/https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - body_hash: `sha256:b3da85616fc118fd6ae92c046374901bb247c8ae3ab8eff5588830052ffb7a63`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary/web.archive.org__web-20210917015654-https-www.coindesk.com-markets-2019-09-20-south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins__f793860280.html`
  > CoinDesk 2019-09-20 (Wayback 20210917015654): South Korea's Upbit will
> end transaction support for six privacy coins — Monero (XMR), Dash
> (DASH), Zcash (ZEC), Haven (XHV), BitTube (TUBE) and PIVX — effective
> Monday Sept. 30 2019, citing money-laundering concerns and the FATF
> June-2019 guidance. The captured body carries "Upbit", all six assets
> (Monero/Dash/Zcash/Haven/BitTube/PIVX), "Sept. 30", "money laundering"
> and "FATF".

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: XMR + DASH + ZEC + XHV + TUBE + PIVX on Upbit
- **Chains**: `monero`, `dash`, `zcash`, `haven`, `bittube`, `pivx`

> Six privacy assets delisted from Upbit: Monero (XMR), Dash (DASH), Zcash
> (ZEC), Haven (XHV), BitTube (TUBE), PIVX. Complete enumeration of the
> delisted set per the cited coverage. The action ended Upbit transaction
> support (off-ramp) for these assets; they remain on their own chains.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 240h

**Event label**: `upbit_ends_support_for_six_privacy_coin_markets`

**Timestamp**: `2019-09-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - Wayback: <https://web.archive.org/web/20210917015654/https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - body_hash: `sha256:b3da85616fc118fd6ae92c046374901bb247c8ae3ab8eff5588830052ffb7a63`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary/web.archive.org__web-20210917015654-https-www.coindesk.com-markets-2019-09-20-south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins__f793860280.html`
  > CoinDesk 2019-09-20: Upbit XMR/DASH/ZEC/XHV/TUBE/PIVX transaction-
> support removal effective 2019-09-30 over money-laundering concerns
> and FATF guidance. attribution=plausible: the delisting is directly
> observed and Upbit cites money-laundering/FATF rationale, but that is
> a soft-framework class-level compliance inference rather than a named
> instrument acting on these specific assets.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`okex-privacy-coin-delisting-2019-09`](./okex-privacy-coin-delisting-2019-09.md)
- [`bittrex-privacy-coin-delisting-2021-01`](./bittrex-privacy-coin-delisting-2021-01.md)
- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad034bc`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

