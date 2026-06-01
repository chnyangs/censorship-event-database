# Evidence chain — `japan-fsa-coincheck-orders-2018`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `0b7e0bd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:13:36Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The Kanto Local Finance Bureau issued business-improvement orders to
> Coincheck on 2018-01-29 and 2018-03-08 after the 2018-01-26 NEM outflow.
> The retained observation is the single-entity Coincheck offramp_cex /
> operator-state remediation path: selected crypto withdrawals and sales
> resumed on 2018-03-12, further crypto withdrawals/sales resumed in phases
> through June 2018, and new account opening plus selected deposits/purchases
> resumed on 2018-10-30 after the regulator-supervised governance and
> customer-protection remediation process. The repaired row does not claim
> a Coincheck business-suspension order, an FSA-ordered initial withdrawal
> freeze, frontend disablement, ISP/DNS blocking, on-chain asset freeze, or
> class-wide Japanese VASP suspension."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_KANTO_LOCAL_FINANCE_BUREAU`
- **Timestamp**: `2018-01-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://lfb.mof.go.jp/kantou/rizai/pagekthp0130000001_00004.html>
  - body_hash: `sha256:f44bc22a845e4a663b6512aae697185d6a831ba8fb37ba66b2f3709685f6bc54`
  - body_path: `sources/http_captures/japan-fsa-coincheck-orders-2018/primary/lfb.mof.go.jp__kantou-rizai-pagekthp0130000001_00004.html__9fee158b7a.html`
  > Kanto Local Finance Bureau administrative disposition page dated
> 2018-01-29. It states that Coincheck reported the 2018-01-26 NEM
> outflow, that the bureau found the cause analysis, customer response,
> and recurrence-prevention posture insufficient, and that it issued a
> business-improvement order under Payment Services Act article 63-16.
> Captured and pinned with body_hash/body_path during the 2026-06-01
> source-repair pass.
- **`primary_legal`**
  - URL: <https://lfb.mof.go.jp/kantou/rizai/pagekthp0130000001_00013.html>
  - body_hash: `sha256:91526375be3317873d3c6645c86ce27a9a8093ae6cd8a66a68b632df5d215ca9`
  - body_path: `sources/http_captures/japan-fsa-coincheck-orders-2018/primary/lfb.mof.go.jp__kantou-rizai-pagekthp0130000001_00013.html__b552d9d688.html`
  > Kanto Local Finance Bureau administrative disposition page dated
> 2018-03-08. It records the January report request, the 2018-01-29
> business-improvement order, the 2018-02-02 on-site inspection, and a
> second business-improvement order requiring governance, AML/CFT, risk
> review, reports on customer transactions/compensation, and effective
> controls before suspended trading/new-account functions resumed. This
> page corrects the earlier dry-run overstatement: Coincheck received a
> business-improvement order, not a business-suspension order.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Coincheck, Inc.
- **Canonical domains**: `coincheck.com`

> Coincheck, Inc. (コインチェック株式会社) — a Tokyo-based crypto-asset
> exchange operating since 2014, treated at the entity-level as the
> named addressee of the Kanto Local Finance Bureau's 2018-01-29 and
> 2018-03-08 business-improvement orders. As of 2018-01 Coincheck was
> operating under deemed-VASP transitional registration (みなし業者) under
> the Payment Services Act revision effective 2017-04 and had not yet
> received final FSA registration approval. Downstream operational
> effect: customer-facing withdrawal/sale and account-opening functions
> were restored only in phases while Coincheck implemented the
> regulator-supervised remediation plan.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 1008h

**Event label**: `coincheck_withdrawal_sale_functions_restored_in_fsa_supervised_phases`

**Timestamp**: `2018-03-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://lfb.mof.go.jp/kantou/rizai/pagekthp0130000001_00004.html>
  - body_hash: `sha256:f44bc22a845e4a663b6512aae697185d6a831ba8fb37ba66b2f3709685f6bc54`
  - body_path: `sources/http_captures/japan-fsa-coincheck-orders-2018/primary/lfb.mof.go.jp__kantou-rizai-pagekthp0130000001_00004.html__9fee158b7a.html`
  > The 2018-01-29 Kanto Local Finance Bureau order required
> fact-finding, customer response, risk-governance strengthening, and
> recurrence-prevention reporting by 2018-02-13. Used as the first
> formal supervisory trigger, not as proof that the regulator ordered
> the initial hack-response freeze.
- **`primary_corporate`**
  - URL: <https://corporate.coincheck.com/press/Vih7V6FC>
  - body_hash: `sha256:d83f35446070b04f35e9a62ff76efda7ccbc49f7f15c9ce3b3f41cbbb7f831e1`
  - body_path: `sources/http_captures/japan-fsa-coincheck-orders-2018/primary/corporate.coincheck.com__press-Vih7V6FC__48b11e9452.html`
  > Coincheck's 2018-03-12 announcement states that, after receiving
> the 2018-03-08 business-improvement order, it would resume
> withdrawals and sales for selected cryptocurrencies sequentially
> after confirming technical security, while other currencies and
> deposits/purchases/new registrations remained suspended pending
> further remediation.
- **`primary_legal`**
  - URL: <https://lfb.mof.go.jp/kantou/rizai/pagekthp0130000001_00013.html>
  - body_hash: `sha256:91526375be3317873d3c6645c86ce27a9a8093ae6cd8a66a68b632df5d215ca9`
  - body_path: `sources/http_captures/japan-fsa-coincheck-orders-2018/primary/lfb.mof.go.jp__kantou-rizai-pagekthp0130000001_00013.html__b552d9d688.html`
  > The 2018-03-08 Kanto Local Finance Bureau order required a
> fundamental governance/risk-control rebuild, reports on customer
> transactions and compensation, and effective controls before
> suspended trading and new account opening resumed.
- **`primary_corporate`**
  - URL: <https://corporate.coincheck.com/press/g9dFINgu>
  - body_hash: `sha256:e574a7d5a8edb0fd7099c0de5c06d78653c033a98c020eea6fd430e5b8e239db`
  - body_path: `sources/http_captures/japan-fsa-coincheck-orders-2018/primary/corporate.coincheck.com__press-g9dFINgu__b86be564c3.html`
  > Coincheck's 2018-10-30 announcement summarizes the staged service
> restoration: JPY withdrawals resumed in February 2018, crypto
> withdrawals and sales resumed from March through June 2018, and
> new account opening plus selected deposits/purchases resumed on
> 2018-10-30 after the remediation plan.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `0b7e0bd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

