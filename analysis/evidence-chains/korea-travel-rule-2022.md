# Evidence chain — `korea-travel-rule-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "South Korea's 2022-03-25 Travel Rule effective date imposed metadata-
> transmission requirements on all registered Korean VASPs for crypto
> transfers ≥KRW 1M, representing the first national-scale FATF
> Recommendation 16 implementation in the dataset and the strictest
> threshold globally. Paper-relevant as a metadata-layer censorship-
> adjacent regulatory event distinct from OFAC / sanction modes."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KR_FSC`
- **Timestamp**: `2022-03-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/pr010101>
  - body_hash: `sha256:3cd314107092a3609e78b723dc98e4ba7ce140bbb683b5be94a4459c8bb5cbe4`
  - body_path: `sources/http_captures/korea-travel-rule-2022/primary/www.fsc.go.kr__eng-pr010101__a21609a3b9.html`
  > Korea Financial Services Commission (FSC) press release index (English
> site) — captured as primary anchor for the KR FSC Travel Rule
> enforcement effective date 2022-03-25. Travel Rule implementation in
> South Korea: Virtual Asset Service Providers (VASPs) must collect
> and transmit originator + beneficiary information for any crypto
> transfer ≥KRW 1,000,000 (~USD 750). First Asia-jurisdiction national-
> scale Travel Rule enforcement in the dataset. Implements FATF
> Recommendation 16 domestically under the Specific Financial
> Transactions Reporting Act amendment.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Korean registered VASPs

> Registered Korean VASPs (Virtual Asset Service Providers) — as of
> 2022-03-25 approximately 26 VASPs registered under the FSC KoFIU
> licensing regime. Targets entire VASP class rather than enumerable
> addresses. Downstream effect: restriction on transfers to/from
> non-KYC-identifiable wallets (including self-custody) via regulated
> Korean exchanges.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `travel_rule_effective_across_all_kr_vasps`

**Timestamp**: `2022-03-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/pr010101>
  - body_hash: `sha256:3cd314107092a3609e78b723dc98e4ba7ce140bbb683b5be94a4459c8bb5cbe4`
  - body_path: `sources/http_captures/korea-travel-rule-2022/primary/www.fsc.go.kr__eng-pr010101__a21609a3b9.html`
  > KR FSC is the primary legal actor for Travel Rule enforcement.
> Effective 2022-03-25; immediate application to all registered
> Korean VASPs (Upbit, Bithumb, Coinone, Korbit, etc.). All crypto
> transfers ≥KRW 1M must carry originator/beneficiary KYC data.
> Direct attribution: the FSC rule itself mandates the behavior.
- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/pr010101>
  - body_hash: `sha256:3cd314107092a3609e78b723dc98e4ba7ce140bbb683b5be94a4459c8bb5cbe4`
  - body_path: `sources/http_captures/korea-travel-rule-2022/primary/www.fsc.go.kr__eng-pr010101__a21609a3b9.html`
  > Second anchor to same FSC index; FATF Recommendation 16 framework
> context. Cross-reference to Specific Financial Transactions
> Reporting Act (특정금융정보법) implementing regulations.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

