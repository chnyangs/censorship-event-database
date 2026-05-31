# Evidence chain — `okex-privacy-coin-delisting-2019-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f58fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OKEx's Korea unit's 2019-09-16 removal of the XMR/DASH/ZEC/ZEN/SBTC markets
> (trading end 2019-10-10, withdrawals 2019-12-10) over the FATF travel rule
> severed the OKEx Korea off-ramp for these privacy assets; single-layer
> offramp_cex observed_change with attribution=plausible (FATF-travel-rule
> soft-framework compliance inference). Scoped to the Korea unit, not OKEx
> globally."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `okex_korea`
- **Timestamp**: `2019-09-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/09/16/okex-korea-drops-5-privacy-cryptocurrencies-citing-fatf-rules/>
  - Wayback: <https://web.archive.org/web/20210921011726/https://www.coindesk.com/markets/2019/09/16/okex-korea-drops-5-privacy-cryptocurrencies-citing-fatf-rules/>
  - body_hash: `sha256:23c866bff91320010984e150501ac4c1e36ee7a2f4a48d30dbd9e39134f55f66`
  - body_path: `sources/http_captures/okex-privacy-coin-delisting-2019-09/primary/web.archive.org__web-20210921011726-https-www.coindesk.com-markets-2019-09-16-okex-korea-drops-5-privacy-cryptocurrencies-citing-fatf-rules__255eadc61e.html`
  > CoinDesk 2019-09-16 (Wayback 20210921011726): OKEx's Korea unit
> delisted five privacy coins — Monero (XMR), Dash (DASH), Zcash (ZEC),
> Horizen (ZEN) and Super Bitcoin (SBTC) — citing the FATF "travel rule"
> (which privacy coins cannot satisfy). Trading support ended Oct. 10,
> withdrawals Dec. 10. The captured body carries "OKEX Korea", all five
> assets (Monero/Dash/Zcash/Horizen/Super Bitcoin, ZEN/SBTC), "FATF",
> "travel rule", "Oct. 10" and "Dec. 10". The decision applied to the
> Korea unit, not OKEx globally.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: XMR + DASH + ZEC + ZEN + SBTC on OKEx Korea
- **Chains**: `monero`, `dash`, `zcash`, `horizen`, `super_bitcoin`

> Five privacy assets delisted from OKEx Korea: Monero (XMR), Dash (DASH),
> Zcash (ZEC), Horizen (ZEN), Super Bitcoin (SBTC). Complete enumeration of
> the delisted set per the cited coverage. The action removed the OKEx Korea
> off-ramp markets for these assets; they remain on their own chains and
> (per the source) the decision was scoped to the Korea unit, not OKEx
> globally.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 576h

**Event label**: `okex_korea_removes_five_privacy_coin_markets`

**Timestamp**: `2019-10-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2019/09/16/okex-korea-drops-5-privacy-cryptocurrencies-citing-fatf-rules/>
  - Wayback: <https://web.archive.org/web/20210921011726/https://www.coindesk.com/markets/2019/09/16/okex-korea-drops-5-privacy-cryptocurrencies-citing-fatf-rules/>
  - body_hash: `sha256:23c866bff91320010984e150501ac4c1e36ee7a2f4a48d30dbd9e39134f55f66`
  - body_path: `sources/http_captures/okex-privacy-coin-delisting-2019-09/primary/web.archive.org__web-20210921011726-https-www.coindesk.com-markets-2019-09-16-okex-korea-drops-5-privacy-cryptocurrencies-citing-fatf-rules__255eadc61e.html`
  > CoinDesk 2019-09-16: OKEx Korea XMR/DASH/ZEC/ZEN/SBTC market removal
> (trading end 2019-10-10, withdrawals 2019-12-10) over the FATF travel
> rule. attribution=plausible: the delisting is directly observed and
> OKEx cites the FATF travel rule, but FATF guidance is a soft
> framework operationalized via national/exchange policy rather than a
> named instrument naming these specific assets (class-level
> compliance inference).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`upbit-privacy-coin-delisting-2019-09`](./upbit-privacy-coin-delisting-2019-09.md)
- [`bittrex-privacy-coin-delisting-2021-01`](./bittrex-privacy-coin-delisting-2021-01.md)
- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f58fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

