# Evidence chain — `bybit-canada-exit-2023-05`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `84e7c21` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:04:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bybit's official 2023-05-30 Canada-market exit notice paused products and
> services for Canadian nationals/residents (new accounts and new positions
> unavailable from 2023-05-31; multiple spot, derivatives, earn, fiat, bot,
> and copy-trading surfaces unavailable from 2023-07-31, with residual
> wind-down through 2023-09-30). This is a single-layer offramp_cex
> observed_change with direct attribution to Bybit's corporate policy action;
> the CSA/regulatory-development framing is retained only as contextual
> rationale."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `bybit`
- **Timestamp**: `2023-05-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://announcements.bybitglobal.com/en/article/notice-on-exit-from-canadian-market-bltc1bfb8746d077fda/>
  - body_hash: `sha256:a802fe5845ac3071f4bbd7b438903a39be4c11464e5ba742737727e35b7c4699`
  - body_path: `sources/http_captures/bybit-canada-exit-2023-05/official-bybit-notice/announcements.bybitglobal.com__en-article-notice-on-exit-from-canadian-market-bltc1bfb8746d077fda__5dc8a1eae2.html`
  > Bybit official announcement, "Notice on Exit from Canadian Market,"
> published 2023-05-30. The captured page states that Bybit is
> pausing availability of products and services to Canadian nationals
> and residents; new account opening and new positions were unavailable
> from 2023-05-31, and product tables record multiple trading, fiat,
> and earn surfaces as not available from 2023-07-31, with residual
> wind-down/liquidation dates through 2023-09-30. This is the
> claim-usable primary corporate trigger and observation anchor.
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

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bybit_canadian_market_withdrawal_announced`

**Timestamp**: `2023-05-30 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://announcements.bybitglobal.com/en/article/notice-on-exit-from-canadian-market-bltc1bfb8746d077fda/>
  - body_hash: `sha256:a802fe5845ac3071f4bbd7b438903a39be4c11464e5ba742737727e35b7c4699`
  - body_path: `sources/http_captures/bybit-canada-exit-2023-05/official-bybit-notice/announcements.bybitglobal.com__en-article-notice-on-exit-from-canadian-market-bltc1bfb8746d077fda__5dc8a1eae2.html`
  > Bybit's own notice records the Canada market exit: product and
> service availability was paused for Canadian nationals and
> residents, new accounts and new positions were unavailable from
> 2023-05-31, and the notice's product table records multiple spot,
> derivatives, earn, fiat, bot, and copy-trading surfaces as not
> available from 2023-07-31, with wind-down/liquidation actions
> through 2023-09-30. attribution=direct for the Bybit-authored
> corporate exit; the CSA/regulatory-development rationale remains
> a scoped background rationale, not a claim of a named order
> compelling Bybit specifically.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/05/30/crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development>
  - Wayback: <https://web.archive.org/web/20250505011102/https://www.coindesk.com/business/2023/05/30/crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development>
  - body_hash: `sha256:7257f0b9e14465adee90ecab6f733b287974e96710d8239dcdae6fe0f1dbf17a`
  - body_path: `sources/http_captures/bybit-canada-exit-2023-05/primary/web.archive.org__web-20250505011102-https-www.coindesk.com-business-2023-05-30-crypto-exchange-bybit-exit-canada-citing-recent-regulatory-development__f6923b8b16.html`
  > CoinDesk 2023-05-30: Bybit exits Canada citing recent regulatory
> development; new onboarding stops 2023-05-31, deposit/contract deadline
> 2023-07-31, withdraw-only thereafter. Retained as corroborating
> contemporaneous reporting and regulatory-context evidence.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `84e7c21`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

