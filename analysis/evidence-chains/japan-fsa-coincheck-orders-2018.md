# Evidence chain — `japan-fsa-coincheck-orders-2018`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c3fb0ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Japan FSA's 2018-01-29 business-improvement order and 2018-03-08
> business-suspension order against Coincheck (following the
> 2018-01-26 NEM hack of approximately ¥58 billion / USD 530M)
> directly compelled the Coincheck operator-state change of customer-
> withdrawal-rail freeze (both crypto-asset and JPY fiat withdrawals)
> for approximately five months between January and approximately
> June 2018. The row does not claim frontend-disable, ISP/DNS-level
> connectivity blocking, on-chain asset-layer freeze, or class-wide
> Japanese VASP-cohort suspension — only the single-entity
> Coincheck-cohort offramp_cex load-bearing axis under the Payment
> Services Act supervisory regime."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2018-01-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/29/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/29/sonota/>
  > Japan Financial Services Agency (金融庁 / FSA) press-release index for
> Heisei-29 (2017/2018) "sonota" (その他 / "other") notices. On
> 2018-01-29 the FSA issued a 業務改善命令 (gyomu-kaizen-meirei /
> business-improvement order) under the Payment Services Act (資金決済法)
> against Coincheck, Inc. following the 2018-01-26 NEM hack in which
> approximately ¥58 billion (~USD 530M) of NEM (XEM) was stolen from
> Coincheck hot wallets. The order required Coincheck to (1) submit a
> plan for facts-finding, victim-compensation, and root-cause analysis,
> (2) strengthen its risk-management framework, and (3) restore
> confidence in customer protection. A follow-on 業務停止命令
> (gyomu-teishi-meirei / business-suspension order) was issued
> 2018-03-08 partially suspending Coincheck's operations except for
> customer-fund-return / withdrawal-processing activities. Coincheck
> withdrawals (both crypto and JPY) were frozen for approximately
> five months between January and approximately June 2018 across the
> cascade of FSA supervisory actions. First major Asian post-Mt-Gox
> FSA supervisory cascade and the formative case for Japan's
> registered-VASP regulatory model. DRYRUN promotion: real anchor is
> an FSA press-release index folder pointer; pinned snapshot
> timestamp and body_hash capture for the specific 2018-01-29 and
> 2018-03-08 release permalinks deferred to non-DRYRUN release.
> Marked evidence_use=contextual_unarchived to flag the unarchived
> state per validator policy.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Coincheck, Inc.
- **Canonical domains**: `coincheck.com`

> Coincheck, Inc. (コインチェック株式会社) — a Tokyo-based crypto-asset
> exchange operating since 2014, treated at the entity-level as the
> named addressee of the FSA's 2018-01-29 business-improvement order and
> the 2018-03-08 business-suspension order. As of 2018-01 Coincheck was
> operating under deemed-VASP transitional registration (みなし業者) under
> the Payment Services Act revision effective 2017-04 and had not yet
> received final FSA registration approval. Downstream operational
> effect: freeze of customer withdrawals (both crypto and JPY) for
> approximately five months pending the FSA-supervised remediation plan.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `coincheck_withdrawal_rail_frozen_per_fsa_orders`

**Timestamp**: `2018-01-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/29/sonota/>
  - Wayback: <https://web.archive.org/web/2018/https://www.fsa.go.jp/news/29/sonota/>
  > FSA's 2018-01-29 業務改善命令 (business-improvement order) is the
> legal instrument that compelled the initial customer-protection /
> remediation regime at Coincheck; the cascade-completing
> 2018-03-08 業務停止命令 (business-suspension order) extended the
> operational suspension. attribution=direct because the
> operator-state change (withdrawal-rail freeze) is the regulatory
> compliance with the FSA supervisory directives, not a downstream
> cascade. DRYRUN: Wayback anchor is an FSA press-index folder
> pointer at fsa.go.jp/news/29/sonota; pinned snapshot timestamp
> and body_hash capture for the specific 2018-01-29 and
> 2018-03-08 release permalinks deferred to human audit.
- **`primary_corporate`**
  - URL: <https://coincheck.com/info/news>
  - Wayback: <https://web.archive.org/web/2018/https://coincheck.com/info/news>
  > Coincheck's own customer-notice news index page is the
> corporate-side primary anchor for the chain of withdrawal-
> suspension and customer-compensation announcements (the NEM
> self-compensation announcement at ¥88.549/XEM, the JPY-
> withdrawal resumption notice in approximately mid-2018, and
> the subsequent acquisition by Monex Group 2018-04). DRYRUN:
> pinned snapshot timestamps and body_hash captures for each
> specific Coincheck-announcement permalink deferred to human
> audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3fb0ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

