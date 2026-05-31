# Evidence chain — `kucoin-canada-exit-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `138003a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:34:18Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Under sustained OSC enforcement (2022-07-22 Capital Markets Tribunal
> order) and the 2023-02-22 CSA Staff Notice 21-332 framework, KuCoin
> on 2023-06-28 announced mandatory KYC effective 2023-07-15 for
> Canadian-resident accounts and an associated wind-down of deposit
> and trading services, producing a 1-layer offramp_cex cascade for
> the KuCoin Canada cohort. Structurally an S5 corporate-policy
> retreat sibling to the S4 CSA-driven Binance Canada withdrawal
> (canada-csa-binance-withdrawal-2023)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `KUCOIN_EXCHANGE`
- **Timestamp**: `2023-06-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.kucoin.com/news/en-kucoin-announcement-regarding-canada>
  - Wayback: <https://web.archive.org/web/2023*/kucoin.com/news/en-kucoin-announcement-regarding-canada>
  > KuCoin corporate announcement (2023-06-28) notifying Canadian
> users of mandatory KYC effective 2023-07-15 and the corresponding
> wind-down of deposit and trading services for Canadian-resident
> accounts. Captures KuCoin's self-initiated retreat from the
> Canadian retail user market following sustained OSC / CSA
> enforcement pressure (OSC Capital Markets Tribunal order
> 2022-07-22 imposing C$2M penalty + permanent participation ban
> on Mek Global / PhoenixFin / KuCoin entities, against the
> backdrop of the 2023-02-22 CSA Staff Notice 21-332 enhanced
> pre-registration-undertaking framework). Marked
> evidence_use=contextual_unarchived because the authoring LLM
> agent did not personally pin a Wayback snapshot timestamp or
> compute a body_hash for the KuCoin announcement page; the
> canonical KuCoin announcement archive is to be re-pinned during
> human audit before this citation may serve as an admission
> anchor.
- **`primary_legal`**
  - URL: <https://www.osc.ca/en/news-events/news/osc-holds-global-crypto-asset-trading-platforms-accountable>
  - Wayback: <https://web.archive.org/web/2022*/osc.ca/en/news-events/news/osc-holds-global-crypto-asset-trading-platforms-accountable>
  > OSC announcement (2022-07-22) of Capital Markets Tribunal orders
> permanently banning Mek Global Limited and PhoenixFin Pte. Ltd.
> (collectively KuCoin) from Ontario's capital markets, with C$2M
> administrative penalty plus C$96,550.35 investigation costs.
> This OSC enforcement action and the broader 2023-02-22 CSA
> pre-registration-undertaking framework collectively constitute
> the regulatory backdrop against which KuCoin chose to retreat
> from the Canadian user market in mid-2023. Marked
> evidence_use=contextual_unarchived pending human-audit Wayback
> re-pin and body_hash capture.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KuCoin (Canada user cohort)
- **Canonical domains**: `kucoin.com`

> KuCoin Canadian-resident user cohort. KuCoin (Mek Global Limited,
> Seychelles; PhoenixFin Pte. Ltd., Singapore) is the focal target
> actor; the affected population is Canadian-resident retail users
> of kucoin.com. Subset-enumerated because KuCoin's Canada exit
> affected the Canadian retail cohort rather than a fully named
> individual address list. Sibling cascade leg to
> canada-csa-binance-withdrawal-2023 from the corporate-policy
> (S5) side rather than the nation-state-block (S4) side.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `kucoin_canada_offramp_shutdown`

**Timestamp**: `2023-07-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.osc.ca/en/news-events/news/osc-holds-global-crypto-asset-trading-platforms-accountable>
  - Wayback: <https://web.archive.org/web/20230608161001/https://www.osc.ca/en/news-events/news/osc-holds-global-crypto-asset-trading-platforms-accountable>
  - body_hash: `sha256:ba9624928418b642e4e8626a3be2b6de379b9387a4cb68aaf47e94e853158fec`
  - body_path: `sources/http_captures/kucoin-canada-exit-2023/primary/web.archive.org__web-20230701000000-https-www.osc.ca-en-news-events-news-osc-holds-global-crypto-asset-trading-platforms-accountable__9fa9b90465.html`
  > Ontario Securities Commission news release on holding global
> crypto-asset trading platforms accountable to Canadian registration
> requirements - the regulatory pressure driving KuCoin's 2023 Canada
> exit. primary_legal anchor; attribution=direct. Wayback 20230608161001
> pinned. (The KuCoin corporate Canada-exit announcement URL returned no
> Wayback memento.)

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): KuCoin's announcement was a corporate-blog notification rather

## 7. Related events

- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `138003a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

