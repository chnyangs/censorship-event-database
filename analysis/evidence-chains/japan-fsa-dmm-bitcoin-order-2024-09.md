# Evidence chain — `japan-fsa-dmm-bitcoin-order-2024-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `892a0b7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `JP_FSA`
- **Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/r6/sonota/>
  - Wayback: <https://web.archive.org/web/2024/https://www.fsa.go.jp/news/r6/sonota/>
  > Japan Financial Services Agency (金融庁 / FSA) press-release index for
> Reiwa-6 (2024) "sonota" (その他 / "other") notices. On 2024-09-26 the
> FSA issued a 業務改善命令 (gyomu-kaizen-meirei / business-improvement
> order) under the Payment Services Act (資金決済法) against DMM Bitcoin
> Co., Ltd. following the 2024-05-31 private-key theft of approximately
> 4,502.9 BTC (~USD 305-482M at hack-window prices; reported variously as
> ~USD 305M, ~USD 308M, ~USD 320M depending on outlet and price window)
> from DMM Bitcoin custody — the largest single-exchange crypto theft of
> 2024 worldwide. The FSA order required DMM Bitcoin to (1) submit by
> 2024-10-28 a remediation plan addressing the absence of decentralised
> controls over private-key management, (2) clarify the
> cause-and-responsibility chain (including the Ginco vendor-side
> compromise), (3) strengthen governance over outsourced wallet-system
> providers, and (4) restore customer-protection confidence. The hack
> vector — later attributed by FBI/NPA/DC3 to DPRK-linked TraderTraitor
> actors — compromised an employee of Ginco Inc., a Tokyo-based
> wallet-software vendor managing DMM's signing infrastructure, via a
> LinkedIn-staged malicious Python "pre-employment test" delivered to a
> Ginco engineer in 2024-03 and subsequent stolen-session-cookie pivot
> in 2024-05 used to manipulate a legitimate DMM transaction. The FSA
> order is the regulatory cascade-trigger; the downstream operator-state
> change is DMM Bitcoin's announced 2024-12 wind-down and migration of
> customer accounts/assets to SBI VC Trade. DRYRUN promotion: real
> anchor is an FSA press-release index folder pointer; pinned snapshot
> timestamp and body_hash capture for the specific 2024-09-26 release
> permalink deferred to non-DRYRUN release. Marked
> evidence_use=contextual_unarchived to flag the unarchived state per
> validator policy.
- **`semi_primary_wayback`**
  - URL: <https://www.regulationasia.com/japan-fsa-issues-business-improvement-order-on-dmm-bitcoin/>
  - Wayback: <https://web.archive.org/web/20240930101400/https://www.regulationasia.com/japan-fsa-issues-business-improvement-order-on-dmm-bitcoin/>
  - body_hash: `sha256:3a4d45f45728130a33364155da381c5d5b59dddbf6512784a982846b58f7c91b`
  - body_path: `sources/http_captures/japan-fsa-dmm-bitcoin-order-2024-09/primary/web.archive.org__web-20240930101400-https-www.regulationasia.com-japan-fsa-issues-business-improvement-order-on-dmm-bitcoin__cf2fd425a7.html`
  > Regulation Asia 2024-09 coverage of the FSA business-improvement
> order: confirms the 2024-10-28 plan-submission deadline and the FSA's
> specific criticism of inadequate decentralisation of private-key
> controls at DMM Bitcoin.
- **`supporting_journalism`**
  - URL: <https://securityaffairs.com/172290/hacking/dmm-bitcoin-308m-theft-linked-north-korea.html>
  - Wayback: <https://web.archive.org/web/2024/https://securityaffairs.com/172290/hacking/dmm-bitcoin-308m-theft-linked-north-korea.html>
  > Security Affairs 2024-12 coverage of the joint FBI/NPA/DC3 attribution
> statement linking the DMM Bitcoin theft to DPRK TraderTraitor via the
> Ginco vendor compromise (LinkedIn pre-employment-test pivot,
> 2024-03 → 2024-05 session-cookie theft → DMM transaction
> manipulation). Used here as contextual attribution evidence for the
> hack vector underlying the FSA's order.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: DMM Bitcoin Co., Ltd.
- **Chains**: `bitcoin`
- **Canonical domains**: `bitcoin.dmm.com`

> DMM Bitcoin Co., Ltd. (株式会社DMM Bitcoin) — a Tokyo-based registered
> crypto-asset exchange subsidiary of DMM.com Group, treated at the
> entity-level as the named addressee of the FSA's 2024-09-26
> business-improvement order. Downstream operational effect: DMM Bitcoin
> announced 2024-12 wind-down and migration of customer accounts and
> custodied assets to SBI VC Trade Co., Ltd. (a registered VASP subsidiary
> of SBI Holdings). Ginco Inc. — the upstream wallet-software vendor whose
> employee compromise was the proximate hack vector — is referenced in the
> enumeration_note as the supply-chain origin of the breach but is not the
> addressee of the FSA's order (Ginco is referenced separately in 2024-10
> FSA system-provider registration-rule discussions, which are a distinct
> downstream policy thread tracked as informational only).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `dmm_bitcoin_winddown_and_asset_migration_to_sbi_vc_trade_per_fsa_order`

**Timestamp**: `2024-09-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsa.go.jp/news/r6/sonota/>
  - Wayback: <https://web.archive.org/web/2024/https://www.fsa.go.jp/news/r6/sonota/>
  > FSA's 2024-09-26 業務改善命令 (business-improvement order) is the
> legal instrument that compelled the customer-protection /
> remediation regime at DMM Bitcoin, culminating in the
> 2024-12 announced wind-down and migration of customer
> accounts/assets to SBI VC Trade. attribution=direct because the
> operator-state change (wind-down + migration) is the regulatory
> compliance with the FSA supervisory directive, not a downstream
> cascade. DRYRUN: Wayback anchor is an FSA press-index folder
> pointer at fsa.go.jp/news/r6/sonota; pinned snapshot timestamp
> and body_hash capture for the specific 2024-09-26 release
> permalink deferred to human audit.
- **`primary_corporate`**
  - URL: <https://bitcoin.dmm.com/news>
  - Wayback: <https://web.archive.org/web/2024/https://bitcoin.dmm.com/news>
  > DMM Bitcoin's own customer-notice news index page is the
> corporate-side primary anchor for the chain of remediation,
> wind-down, and SBI VC Trade migration announcements. DRYRUN:
> pinned snapshot timestamps and body_hash captures for each
> specific announcement permalink deferred to human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.regulationasia.com/japan-fsa-issues-business-improvement-order-on-dmm-bitcoin/>
  - Wayback: <https://web.archive.org/web/20240930101400/https://www.regulationasia.com/japan-fsa-issues-business-improvement-order-on-dmm-bitcoin/>
  - body_hash: `sha256:3a4d45f45728130a33364155da381c5d5b59dddbf6512784a982846b58f7c91b`
  - body_path: `sources/http_captures/japan-fsa-dmm-bitcoin-order-2024-09/primary/web.archive.org__web-20240930101400-https-www.regulationasia.com-japan-fsa-issues-business-improvement-order-on-dmm-bitcoin__cf2fd425a7.html`
  > Regulation Asia 2024-09-30 reporting on the FSA business-
> improvement order to DMM Bitcoin. Independent semi-primary
> anchor 1 of 2 for the offramp observation.
- **`semi_primary_wayback`**
  - URL: <https://securityaffairs.com/172290/hacking/dmm-bitcoin-308m-theft-linked-north-korea.html>
  - Wayback: <https://web.archive.org/web/20241225121737/https://securityaffairs.com/172290/hacking/dmm-bitcoin-308m-theft-linked-north-korea.html>
  - body_hash: `sha256:b7bb662fb24a152b2cf6af3f6f193ff3c7df972ec51cceea04a2396d34c226c9`
  - body_path: `sources/http_captures/japan-fsa-dmm-bitcoin-order-2024-09/primary/web.archive.org__web-20241225121737-https-securityaffairs.com-172290-hacking-dmm-bitcoin-308m-theft-linked-north-korea.html__b238dc314d.html`
  > Security Affairs 2024-12 reporting confirming the DMM Bitcoin
> wind-down + SBI VC Trade migration and the DPRK/TraderTraitor
> attribution. Independent semi-primary anchor 2 of 2.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`japan-fsa-coincheck-orders-2018`](./japan-fsa-coincheck-orders-2018.md)
- [`japan-fsa-zaif-orders-2018-09`](./japan-fsa-zaif-orders-2018-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `892a0b7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

