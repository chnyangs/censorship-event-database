# Evidence chain — `binance-monero-global-delisting-2024-02`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `1e151cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T12:31:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2024-02-06 global delisting of Monero (XMR) — all XMR spot
> pairs removed as of 2024-02-20, within an ANT/MULTI/VAI/XMR batch, XMR
> -~30% — severed the Binance off-ramp for XMR worldwide; single-layer
> offramp_cex observed_change, attribution=plausible (Binance stated only
> a generic periodic-review rationale). Distinct from the 2023-06 Binance
> EU privacy-asset delisting."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2024-02-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2024/02/06/binance-to-delist-monero-privacy-token-xmr-slides>
  - Wayback: <https://web.archive.org/web/20250911142709/https://www.coindesk.com/markets/2024/02/06/binance-to-delist-monero-privacy-token-xmr-slides>
  - body_hash: `sha256:bbc323c99e91135ebd5ea34ec58d7e99ec63afe434fbcffe034ccb355dae7cb4`
  - body_path: `sources/http_captures/binance-monero-global-delisting-2024-02/primary/web.archive.org__web-20250911142709-https-www.coindesk.com-markets-2024-02-06-binance-to-delist-monero-privacy-token-xmr-slides__4b64544058.html`
  > CoinDesk 2024-02-06: Binance announced it will stop listing the
> privacy token Monero (XMR) as of Feb. 20 2024, along with Aragon
> (ANT), Multichain (MULTI) and Vai (VAI). Monero slumped about 30%
> to a 20-month low on the news. The notice cited Binance's periodic
> review "to ensure that [each digital asset] continues to meet" its
> listing standards. Wayback 20250911142709.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/276176/binance-delisting-monero>
  - Wayback: <https://web.archive.org/web/20240207035541/https://www.theblock.co/post/276176/binance-delisting-monero>
  - body_hash: `sha256:33f4c71dd5e945bcbffb4b047ed5cc947eac7485c59723404cdd107f60779fca`
  - body_path: `sources/http_captures/binance-monero-global-delisting-2024-02/primary/web.archive.org__web-20240207035541-https-www.theblock.co-post-276176-binance-delisting-monero__cc3f5e5a64.html`
  > The Block 2024-02-07 corroboration: Binance to delist Monero (XMR)
> on Feb. 20 alongside Aragon, Multichain and Vai, after previously
> adding a monitoring tag; XMR dropped ~15% on the day of the
> announcement. Independent second semi-primary anchor.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: Monero (XMR) on Binance (global spot delisting)
- **Chains**: `monero`

> Monero (XMR) spot markets on Binance, delisted as of 2024-02-20 within
> a four-token batch (XMR + Aragon/ANT + Multichain/MULTI + Vai/VAI).
> This row scopes the privacy-coin censorship case (XMR), the only
> privacy asset in the batch; the other three (ANT/MULTI/VAI) are
> non-privacy delistings in the same notice and are not the
> privacy-coin-delisting subject here, so enumeration=subset relative to
> the full notice. XMR is an independent base-chain asset (no
> issuer/contract); the action removes the Binance trading markets.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 336h

**Event label**: `binance_removes_xmr_global_spot_markets_privacy_coin_delisting`

**Timestamp**: `2024-02-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/markets/2024/02/06/binance-to-delist-monero-privacy-token-xmr-slides>
  - Wayback: <https://web.archive.org/web/20250911142709/https://www.coindesk.com/markets/2024/02/06/binance-to-delist-monero-privacy-token-xmr-slides>
  - body_hash: `sha256:bbc323c99e91135ebd5ea34ec58d7e99ec63afe434fbcffe034ccb355dae7cb4`
  - body_path: `sources/http_captures/binance-monero-global-delisting-2024-02/primary/web.archive.org__web-20250911142709-https-www.coindesk.com-markets-2024-02-06-binance-to-delist-monero-privacy-token-xmr-slides__4b64544058.html`
  > CoinDesk 2024-02-06: Binance global XMR delisting (markets cease
> Feb. 20), within an ANT/MULTI/VAI/XMR batch; XMR fell ~30%.
> attribution=plausible: the delisting is directly observed but
> Binance's notice states only a generic periodic-review rationale,
> not an explicit privacy-coin/regulatory reason, so the
> compliance motive is contextual inference.
- **`semi_primary_wayback`**
  - URL: <https://www.theblock.co/post/276176/binance-delisting-monero>
  - Wayback: <https://web.archive.org/web/20240207035541/https://www.theblock.co/post/276176/binance-delisting-monero>
  - body_hash: `sha256:33f4c71dd5e945bcbffb4b047ed5cc947eac7485c59723404cdd107f60779fca`
  - body_path: `sources/http_captures/binance-monero-global-delisting-2024-02/primary/web.archive.org__web-20240207035541-https-www.theblock.co-post-276176-binance-delisting-monero__cc3f5e5a64.html`
  > The Block 2024-02-07 corroboration of the Binance XMR Feb. 20
> delisting (after a prior monitoring tag). Independent second
> semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)
- [`bittrex-privacy-coin-delisting-2021-01`](./bittrex-privacy-coin-delisting-2021-01.md)
- [`kraken-monero-eu-delisting-2024`](./kraken-monero-eu-delisting-2024.md)
- `okx-monero-global-delisting-2024` (rejected; no rendered admitted-chain link)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1e151cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

