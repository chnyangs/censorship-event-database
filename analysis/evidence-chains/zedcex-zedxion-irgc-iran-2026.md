# Evidence chain — `zedcex-zedxion-irgc-iran-2026`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2026-01-30 SDN designation of IRGC-linked exchanges Zedcex and Zedxion (sb0375)
> produced no public CEX cascade documented in the 14-day window. attested_secondary null_case."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2026-01-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0375>
  > OFAC press release sb0375 (2026-01-30) — first designation of IRGC-linked digital
> asset exchanges Zedcex Exchange Ltd and Zedxion Exchange Ltd (both UK-registered),
> linked to Babak Morteza Zanjani. treasury.gov blocks automated capture, so this primary
> is cited contextually; the captured Elliptic analysis anchors the attested_secondary
> admission.
- **`supporting_tracker`**
  - URL: <https://www.elliptic.co/blog/ofac-sanctions-exchanges-zedcex-and-zedxion-for-assisting-in-iranian-sanctions-evasion-and-irgc-operations>
  - body_hash: `sha256:5dccacfc8d17b4dd74c3f7bbb6b9ae1892857a60a6d42a662a64579e93a842b2`
  - body_path: `sources/http_captures/zedcex-zedxion-irgc-iran-2026/secondary/www.elliptic.co__blog-ofac-sanctions-exchanges-zedcex-and-zedxion-for-assisting-in-iranian-sanctions-evasion-and-irgc-operations__e4aafa5453.html`
  > Elliptic analysis (captured 2026-06-08) of the Zedcex/Zedxion IRGC designations.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2026-01-30 00:00:00+00:00` → `2026-02-13 23:59:59+00:00`

**Sources**:

- **`supporting_tracker`**
  - URL: <https://www.elliptic.co/blog/ofac-sanctions-exchanges-zedcex-and-zedxion-for-assisting-in-iranian-sanctions-evasion-and-irgc-operations>
  - body_hash: `sha256:5dccacfc8d17b4dd74c3f7bbb6b9ae1892857a60a6d42a662a64579e93a842b2`
  - body_path: `sources/http_captures/zedcex-zedxion-irgc-iran-2026/secondary/www.elliptic.co__blog-ofac-sanctions-exchanges-zedcex-and-zedxion-for-assisting-in-iranian-sanctions-evasion-and-irgc-operations__e4aafa5453.html`
  > null_event anchor (attested_secondary): Elliptic analysis of the 2026-01-30 OFAC SDN
> designation of IRGC-linked exchanges Zedcex and Zedxion. No public CEX cascade
> explicitly naming the SDN entries was documented in the 14-day window.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

