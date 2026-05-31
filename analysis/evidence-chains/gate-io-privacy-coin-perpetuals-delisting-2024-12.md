# Evidence chain — `gate-io-privacy-coin-perpetuals-delisting-2024-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9fed8c7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Gate.io's 2024-12-26 removal of the XMR/DASH/ZEC/ZEN/XVG perpetual-
> contract markets (reduce-only 2024-12-25) severed the Gate.io
> derivatives off-ramp for these privacy assets; single-layer offramp_cex
> observed_change, attribution=plausible (the official notice states
> mechanics but no regulatory trigger; MiCA motive is contextual)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `gate_io`
- **Timestamp**: `2024-12-26 08:00:00+00:00` (precision: `hour`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.gate.io/announcements/article/41883>
  - Wayback: <https://web.archive.org/web/20250501041136/https://www.gate.io/announcements/article/41883>
  - body_hash: `sha256:3128754ebe1b3c468daf6a20bef3334b7c02d4ed8f1063d4d9e424c5a311ca5d`
  - body_path: `sources/http_captures/gate-io-privacy-coin-perpetuals-delisting-2024-12/primary/web.archive.org__web-20250501041136-https-www.gate.io-announcements-article-41883__c9c5355352.html`
  > Gate.io official announcement (article 41883): XMR, DASH, ZEC,
> ZEN, XVG perpetual contracts moved to reduce-only mode 2024-12-25
> and fully delisted 2024-12-26 08:00 UTC; open orders cancelled
> and remaining positions auto-settled at the 30-min average index
> price. Captured page enumerates all five tickers and the
> reduce-only/delist mechanics (grep-confirmed: XMR/DASH/ZEC/ZEN/
> XVG, "perpetual", "reduce-only", "delist").

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: XMR + DASH + ZEC + ZEN + XVG perpetuals on Gate.io
- **Chains**: `monero`, `dash`, `zcash`

> Five privacy-coin perpetual-contract markets removed from Gate.io:
> Monero (XMR), Dash (DASH), Zcash (ZEC), Horizen (ZEN), Verge (XVG).
> Complete enumeration of the delisted perpetual set per the official
> Gate.io notice; the action removes the Gate.io derivatives markets
> for these privacy assets (the underlying base-chain assets persist).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `gateio_removes_xmr_dash_zec_zen_xvg_perpetual_markets`

**Timestamp**: `2024-12-26 08:00:00+00:00` (precision: `hour`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.gate.io/announcements/article/41883>
  - Wayback: <https://web.archive.org/web/20250501041136/https://www.gate.io/announcements/article/41883>
  - body_hash: `sha256:3128754ebe1b3c468daf6a20bef3334b7c02d4ed8f1063d4d9e424c5a311ca5d`
  - body_path: `sources/http_captures/gate-io-privacy-coin-perpetuals-delisting-2024-12/primary/web.archive.org__web-20250501041136-https-www.gate.io-announcements-article-41883__c9c5355352.html`
  > Gate.io official notice (article 41883): XMR/DASH/ZEC/ZEN/XVG
> perpetual delisting (reduce-only 2024-12-25, removed 2024-12-26
> 08:00 UTC). attribution=plausible per §1.1: the delisting is
> directly observed in the issuer's own notice, but the notice
> (as captured) states delisting mechanics without naming a
> specific regulatory trigger; the MiCA privacy-coin-pressure
> motive is contextual class-level inference, not a stated cause.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bittrex-privacy-coin-delisting-2021-01`](./bittrex-privacy-coin-delisting-2021-01.md)
- [`huobi-htx-privacy-coin-delisting-2024`](./huobi-htx-privacy-coin-delisting-2024.md)
- [`okx-privacy-token-delist-2024`](./okx-privacy-token-delist-2024.md)
- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9fed8c7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

