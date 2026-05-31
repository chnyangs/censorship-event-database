# Evidence chain — `japan-fsa-ftx-japan-suspension-2022-11`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `75fb128` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan's 2022-11-10 Kanto Local Finance Bureau business-suspension
> order, business-improvement order, and order to retain assets
> domestically against FTX Japan KK (issued one day before the US
> parent's 2022-11-11 Chapter 11 filing) directly compelled the
> FTX Japan operator-state change of customer-withdrawal-rail freeze
> (both crypto-asset and JPY fiat withdrawals) and Japan-domestic
> retention of customer-segregated assets across the 2022-11-09 to
> 2023-02-20 window, with recovery via the 2023-02-21 customer-asset
> refund channel through the Liquid Japan web platform. The row does
> not claim frontend-disable, ISP/DNS-level connectivity blocking,
> on-chain asset-layer freeze, or class-wide Japanese VASP-cohort
> suspension — only the single-entity FTX-Japan-cohort offramp_cex
> load-bearing axis under the Payment Services Act and Financial
> Instruments and Exchange Act supervisory regime."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA_KANTO_LFB`
- **Timestamp**: `2022-11-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/r4/sonota/20221110/20221110.html>
  - Wayback: <https://web.archive.org/web/20221110133726/https://www.fsa.go.jp/news/r4/sonota/20221110/20221110.html>
  - body_hash: `sha256:b6f3ea01c02af429023fc0fc450507d60122a154aa4ba41d0288120c2efc6300`
  - body_path: `sources/http_captures/japan-fsa-ftx-japan-suspension-2022-11/primary/web.archive.org__web-20221110133726-https-www.fsa.go.jp-news-r4-sonota-20221110-20221110.html__ccc0cd2d3a.html`
  > Japan Financial Services Agency (金融庁 / FSA) press release dated
> 2022-11-10 titled "FTX Japan株式会社に対する行政処分について"
> (Administrative Disposition Against FTX Japan KK). On 2022-11-10 the
> Kanto Local Finance Bureau (関東財務局), acting under delegated FSA
> authority, issued against FTX Japan KK (a registered Japanese crypto-
> asset exchange service provider and Type-I Financial Instruments
> Business Operator):
>   (1) a 業務停止命令 (gyomu-teishi-meirei / business-suspension order)
>       under the Payment Services Act (資金決済法 / PSA) and the
>       Financial Instruments and Exchange Act (金融商品取引法 / FIEA),
>       suspending crypto-asset exchange services and new customer-
>       asset acceptance from 2022-11-10 through 2022-12-09 (~30 days);
>   (2) a 業務改善命令 (gyomu-kaizen-meirei / business-improvement
>       order) under the PSA and FIEA, requiring FTX Japan to (a)
>       identify the status of customers and customer assets, (b)
>       strive to protect customer assets, and (c) communicate
>       appropriately with customers regarding asset-protection; with
>       a written business-improvement-plan due 2022-11-16 and
>       monthly progress reports thereafter;
>   (3) a 資産の国内保有命令 (shisan-no-kokunai-hoyu-meirei /
>       order to retain assets domestically) under FIEA preventing
>       FTX Japan from transferring customer-segregated assets out
>       of Japan to the US FTX Trading Ltd. estate.
> The orders were precipitated by FTX Japan's 2022-11-09 unilateral
> halt of customer asset withdrawals (citing parent-company policy
> following the US FTX.com liquidity crisis) while continuing to
> accept new deposits and execute crypto trades — a structural
> mismatch that the regulator determined violated Japanese customer-
> protection rules. Trigger lands one day before the US parent's
> 2022-11-11 Chapter 11 filing (Case 22-11068, D. Del.), making this
> the cleanest cross-border parent-cascade case in the corpus where
> Japanese customer-asset-segregation rules (the PSA-mandated
> 分別管理 / trust-based separation regime and the FIEA-mandated
> Japan-domestic-retention) forced FTX Japan to refund Japanese
> customers ahead of US estate proceedings rather than have those
> assets pooled into the global Chapter 11 estate. DRYRUN: Wayback
> anchor is a wildcard pointer to 2022; pinned snapshot timestamp +
> body_hash capture for the specific 2022-11-10 FSA release
> permalink deferred to human audit.
- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/en/news/2022/20221111/20221110.html>
  - Wayback: <https://web.archive.org/web/20221111104403/https://www.fsa.go.jp/en/news/2022/20221111/20221110.html>
  - body_hash: `sha256:2fba95df79d0ce107168518af5b2d74ce5731c21dcbb139c6acf6226ec8a2a6b`
  - body_path: `sources/http_captures/japan-fsa-ftx-japan-suspension-2022-11/primary/web.archive.org__web-20221111104403-https-www.fsa.go.jp-en-news-2022-20221111-20221110.html__ca531aa851.html`
  > FSA English-language version of the 2022-11-10 release titled
> "Administrative Actions against FTX Japan, Inc." Documents the
> identical business-suspension order, business-improvement order,
> and asset-domestic-retention order issued by the Kanto Local
> Finance Bureau under the PSA and FIEA. English-language anchor
> retained for accessibility and cross-checks against the Japanese-
> language primary. DRYRUN: Wayback anchor is a wildcard pointer;
> pinned snapshot timestamp + body_hash capture deferred to human
> audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: FTX Japan KK
- **Canonical domains**: `ftxjp.co`, `liquid.com`

> FTX Japan KK (FTX Japan株式会社) — the Japanese subsidiary of FTX
> Trading Ltd., headquartered in Minato-ku, Tokyo. As of 2022-11-10
> FTX Japan was a registered crypto-asset exchange service provider
> (暗号資産交換業者) under the Payment Services Act (Kanto Local
> Finance Bureau registration No. 00004) and a Type-I Financial
> Instruments Business Operator (第一種金融商品取引業者) under the
> Financial Instruments and Exchange Act, acquired by FTX Trading
> Ltd. in 2022-02 via purchase of Liquid Group (the former Liquid
> Japan / Quoine Corporation entity). The target slice is the single
> Japanese subsidiary; sibling Liquid Global (the non-Japan Liquid
> operations) and the US/international FTX entities are out of scope
> for this row. Load-bearing observation is the Japan-jurisdiction
> offramp_cex withdrawal-rail freeze followed by the
> Japanese-customer asset refund channel via the Liquid Japan web
> platform (the structural counterfactual to the US Chapter 11
> estate pooling).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `ftx_japan_withdrawal_rail_frozen_and_assets_held_domestically_per_kanto_lfb_orders`

**Timestamp**: `2022-11-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/r4/sonota/20221110/20221110.html>
  - Wayback: <https://web.archive.org/web/20221110133726/https://www.fsa.go.jp/news/r4/sonota/20221110/20221110.html>
  - body_hash: `sha256:b6f3ea01c02af429023fc0fc450507d60122a154aa4ba41d0288120c2efc6300`
  - body_path: `sources/http_captures/japan-fsa-ftx-japan-suspension-2022-11/primary/web.archive.org__web-20221110133726-https-www.fsa.go.jp-news-r4-sonota-20221110-20221110.html__ccc0cd2d3a.html`
  > FSA 2022-11-10 Japanese-language release: Kanto LFB issued the
> 業務停止命令 (PSA + FIEA) suspending crypto-asset exchange
> services from 2022-11-10 to 2022-12-09, the 業務改善命令
> (PSA + FIEA) requiring a written business-improvement plan by
> 2022-11-16, and the 資産の国内保有命令 (FIEA) compelling
> domestic retention of customer-segregated assets. The
> operator-state change (withdrawal-rail freeze + JP-domestic
> asset retention) is the direct compliance with these orders.
> Cleanest cross-border parent-cascade case in the corpus:
> Japanese customer-segregation rules forced FTX Japan to
> refund Japanese customers ahead of the US Chapter 11 estate
> pooling. DRYRUN: pinned snapshot timestamp + body_hash
> capture deferred to human audit.
- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/en/news/2022/20221111/20221110.html>
  - Wayback: <https://web.archive.org/web/20221111104403/https://www.fsa.go.jp/en/news/2022/20221111/20221110.html>
  - body_hash: `sha256:2fba95df79d0ce107168518af5b2d74ce5731c21dcbb139c6acf6226ec8a2a6b`
  - body_path: `sources/http_captures/japan-fsa-ftx-japan-suspension-2022-11/primary/web.archive.org__web-20221111104403-https-www.fsa.go.jp-en-news-2022-20221111-20221110.html__ca531aa851.html`
  > FSA English-language version "Administrative Actions against
> FTX Japan, Inc." corroborates the Japanese-language primary
> and is retained as the accessibility anchor. DRYRUN: pinned
> snapshot timestamp + body_hash capture deferred to human
> audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2022/11/10/ftx-japan-ordered-by-regulator-to-suspend-operations-following-withdrawal-halt>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/policy/2022/11/10/ftx-japan-ordered-by-regulator-to-suspend-operations-following-withdrawal-halt>
  > CoinDesk (2022-11-10): "FTX Japan to Go Into 'Close-Only' Mode
> Following Regulator's Order to Suspend Operations." Documents
> the 2022-11-09 withdrawal halt and the 2022-11-10 Kanto LFB
> response in English-language journalism, useful as the
> interpretive bridge between the Japanese-language FSA primary
> and the international FTX collapse narrative. DRYRUN: pinned
> snapshot timestamp + body_hash capture deferred to human
> audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)
- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `75fb128`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

