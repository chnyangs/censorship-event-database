# Evidence chain — `upbit-privacy-coin-delisting-2019-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `892a0b7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Upbit's 2019-09-30 removal of transaction support for the
> XMR/DASH/ZEC/XHV/TUBE/PIVX markets (officially citing money-laundering /
> external-network concerns, with FATF guidance as contextual reporting)
> severed the Upbit off-ramp for these privacy assets;
> single-layer offramp_cex observed_change with attribution=plausible
> (soft-framework compliance inference, no named instrument)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `upbit_dunamu`
- **Timestamp**: `2019-09-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://sg-api-manager.upbit.com/api/v1/announcements/2256>
  - Wayback: <https://web.archive.org/web/20260601121553/https://sg-api-manager.upbit.com/api/v1/announcements/2256>
  - body_hash: `sha256:63f8257fc5a3388c9f3e4a851b4c45b77211748f334ee471214e8ef78caea0ad`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary-upbit-api/sg-api-manager.upbit.com__api-v1-announcements-2256__f8cff15335.json`
  > Official Upbit announcement API for notice 2256, captured 2026-06-01
> and archived to Wayback. The JSON body lists XMR, DASH, ZEC, XHV,
> TUBE and PIVX; states market trading support ceases on 2019-09-30;
> and gives the stated rationale as blocking money-laundering
> possibility and inflow from external networks. This is the
> load-bearing primary corporate anchor for the event.
- **`primary_corporate`**
  - URL: <https://sg.upbit.com/service_center/notice?id=2256>
  - Wayback: <https://web.archive.org/web/20260601121249/https://sg.upbit.com/service_center/notice?id=2256>
  - body_hash: `sha256:74f7cc89cbfcaff8c78a4d853670f1b77cf65f8a8dfdaa6a9dba32838ef1147c`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary-upbit/sg.upbit.com__service_center-notice__1947c10dcb.html`
  > Official Upbit notice shell. The rendered HTML title identifies the
> same notice and asset set; the full notice body is preserved through
> the API citation above because the public page is JavaScript-rendered.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - Wayback: <https://web.archive.org/web/20210917015654/https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - body_hash: `sha256:b3da85616fc118fd6ae92c046374901bb247c8ae3ab8eff5588830052ffb7a63`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary/web.archive.org__web-20210917015654-https-www.coindesk.com-markets-2019-09-20-south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins__f793860280.html`
  > CoinDesk 2019-09-20 corroborates the notice, identifies Upbit as
> South Korea's Upbit, and supplies the contemporaneous FATF-guidance
> context. It is retained as contextual corroboration; the primary
> corporate API citation above carries the observed delisting action.

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

- **`primary_corporate`**
  - URL: <https://sg-api-manager.upbit.com/api/v1/announcements/2256>
  - Wayback: <https://web.archive.org/web/20260601121553/https://sg-api-manager.upbit.com/api/v1/announcements/2256>
  - body_hash: `sha256:63f8257fc5a3388c9f3e4a851b4c45b77211748f334ee471214e8ef78caea0ad`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary-upbit-api/sg-api-manager.upbit.com__api-v1-announcements-2256__f8cff15335.json`
  > Official Upbit notice 2256: XMR/DASH/ZEC/XHV/TUBE/PIVX market
> trading support ended 2019-09-30, with open orders canceled and
> withdrawal support retained through 2019-10-19. attribution remains
> plausible because the legal/regulatory driver is a class-level AML
> rationale, not a named binding instrument for this exact asset set.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - Wayback: <https://web.archive.org/web/20210917015654/https://www.coindesk.com/markets/2019/09/20/south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins/>
  - body_hash: `sha256:b3da85616fc118fd6ae92c046374901bb247c8ae3ab8eff5588830052ffb7a63`
  - body_path: `sources/http_captures/upbit-privacy-coin-delisting-2019-09/primary/web.archive.org__web-20210917015654-https-www.coindesk.com-markets-2019-09-20-south-koreas-upbit-becomes-latest-exchange-to-delist-privacy-coins__f793860280.html`
  > CoinDesk 2019-09-20 corroborates the Upbit notice and supplies the
> FATF-guidance context. The action itself is now carried by the
> primary corporate Upbit API citation above.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`okex-privacy-coin-delisting-2019-09`](./okex-privacy-coin-delisting-2019-09.md)
- [`bittrex-privacy-coin-delisting-2021-01`](./bittrex-privacy-coin-delisting-2021-01.md)
- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `892a0b7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

