# Evidence chain — `bybit-singapore-exit-2022`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `47f4858` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T14:27:22Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Bybit Fintech Limited wound down Singapore user-facing services on
> bybit.com and relocated its global headquarters to Dubai during 2022,
> plausibly in response to the MAS regulatory environment (PSA
> licensing, 2022-01-17 retail-crypto advertising restrictions, FSM
> Act 2022 cross-border DTSP licensing). Load-bearing observational
> axis is offramp_cex at the SG retail cohort level; attribution is
> plausible because Bybit's corporate communications do not explicitly
> cite MAS as the cause."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `BYBIT_GLOBAL`
- **Timestamp**: `2022-05-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://announcements.bybit.com/>
  - Wayback: <https://web.archive.org/web/2022*/announcements.bybit.com>
  > Bybit (Bybit Fintech Limited / global) decision to wind down its
> Singapore user-facing operations and relocate its global
> headquarters to Dubai during 2022, following sustained MAS
> regulatory pressure (Payment Services Act licensing regime, MAS
> 2022-01-17 retail-crypto advertising restrictions, and the
> Financial Services and Markets Act 2022 cross-border DTSP
> licensing regime enacted 2022-04). Bybit was not on the MAS
> Investor Alert List in 2022, but its unlicensed posture under
> PSA / forthcoming FSM Act created the same operational
> constraint that drove other unlicensed offshore exchanges to
> scale back SG-user services. DRYRUN: pinned Wayback / body-hash
> captures for the Bybit Singapore-user wind-down notice and the
> Bybit Dubai HQ move announcement deferred to a non-DRYRUN
> release.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bybit (bybit.com SG cohort)
- **Canonical domains**: `bybit.com`

> Bybit Fintech Limited (global Bybit.com) Singapore-resident user
> cohort. Subset rationale: target is the SG slice of Bybit's global
> user base (Bybit had no MAS-licensed SG entity, so the "entity"
> scope is operationally the SG retail cohort served via bybit.com
> rather than a Singapore-licensed subsidiary). Class-level rationale
> follows codebook §7: subset + enumeration_note over class_level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `bybit_sg_user_services_wound_down_and_hq_to_dubai`

**Timestamp**: `2022-05-01 00:00:00+00:00` (precision: `week`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.bybit.com/en-US/help-center/bybitHC_Article?id=000001067&language=en_US>
  - Wayback: <https://web.archive.org/web/20230604203058/https://www.bybit.com/en-US/help-center/bybitHC_Article?id=000001067&language=en_US>
  - body_hash: `sha256:38d3be227c236a358fc93a7b597b47f333a0eba5b6f87243e3ac094d0022af8a`
  - body_path: `sources/http_captures/bybit-singapore-exit-2022/primary/web.archive.org__web-20220901000000-https-www.bybit.com-en-US-help-center-bybitHC_Article__61c132e572.html`
  > Bybit help-center article on service-restricted countries
> (including Singapore, following the 2022 MAS investor-protection
> restrictions). primary_corporate anchor. Wayback 20230604203058 pinned.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Bybit.com SG-geo restriction banner / KYC blocking for SG-

## 7. Related events

- [`singapore-mas-binance-services-2021`](./singapore-mas-binance-services-2021.md)
- [`singapore-mas-retail-crypto-restriction-2022`](./singapore-mas-retail-crypto-restriction-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `47f4858`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

