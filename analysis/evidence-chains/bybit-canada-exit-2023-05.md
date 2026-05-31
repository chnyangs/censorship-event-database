# Evidence chain — `bybit-canada-exit-2023-05`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8b35609` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bybit's 2023-05-30 withdrawal from the Canadian market (onboarding stop
> 2023-05-31, deposit/contract deadline 2023-07-31) following the CSA's
> tightened crypto-platform regime is a single-layer offramp_cex
> observed_change with attribution=plausible, part of the 2023 exchange exodus
> from Canada (cf. Binance/KuCoin)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `bybit`
- **Timestamp**: `2023-05-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/05/30/crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development>
  - Wayback: <https://web.archive.org/web/20250505011102/https://www.coindesk.com/business/2023/05/30/crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development>
  - body_hash: `sha256:7257f0b9e14465adee90ecab6f733b287974e96710d8239dcdae6fe0f1dbf17a`
  - body_path: `sources/http_captures/bybit-canada-exit-2023-05/primary/web.archive.org__web-20250505011102-https-www.coindesk.com-business-2023-05-30-crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development__f6923b8b16.html`
  > CoinDesk 2023-05-30: "Crypto Exchange Bybit Exits Canada Citing Recent
> Regulatory Development." Bybit stops onboarding from 2023-05-31; existing
> Canadian customers have until 2023-07-31 to make new deposits / enter new
> contracts, then may only withdraw or reduce positions after the closing
> date. Grep of captured body confirms "Bybit Exits Canada", "from May 31",
> "until July 31 to make new deposits", "withdraw or reduce their positions".
> Wayback 20250505011102 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bybit (Canadian market)
- **Canonical domains**: `bybit.com`

> Target is the Bybit Canadian-resident retail-customer access surface.
> Subset enumeration: the action enumerates a national market-access
> withdrawal (no new accounts; deposit/contract deadline; withdraw-only
> thereafter) rather than a complete on-chain address set. No address-level
> targets; a market-level exit by a centralized exchange.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `bybit_canadian_market_withdrawal_announced`

**Timestamp**: `2023-05-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/05/30/crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development>
  - Wayback: <https://web.archive.org/web/20250505011102/https://www.coindesk.com/business/2023/05/30/crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development>
  - body_hash: `sha256:7257f0b9e14465adee90ecab6f733b287974e96710d8239dcdae6fe0f1dbf17a`
  - body_path: `sources/http_captures/bybit-canada-exit-2023-05/primary/web.archive.org__web-20250505011102-https-www.coindesk.com-business-2023-05-30-crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development__f6923b8b16.html`
  > CoinDesk 2023-05-30: Bybit exits Canada citing recent regulatory
> development; new onboarding stops 2023-05-31, deposit/contract deadline
> 2023-07-31, withdraw-only thereafter. attribution=plausible: the market
> withdrawal is directly observed and Bybit cites a "regulatory
> development," but the captured CoinDesk report (not a Bybit primary
> notice) is the anchor and does not enumerate the specific CSA
> provisions, so the regulatory-cause framing is contextual.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8b35609`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

