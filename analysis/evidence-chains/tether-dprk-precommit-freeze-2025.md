# Evidence chain — `tether-dprk-precommit-freeze-2025`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `47f4858` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T14:27:22Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tether batch-froze a subset of DPRK-laundering USDT-TRC20 addresses on 2025-04-30 at
> identical minute-precision timestamps, 188 days before the corresponding OFAC SDN
> designation (2025-11-04). Demonstrates that asset-layer cascade can precede the legal
> cascade in time, inverting the common top-down cascade model."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2025-04-30 07:05:00+00:00` (precision: `minute`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz>
  - body_hash: `sha256:5d6317eb4970c6d1f570dc8b37892db66664fd3fab838a1ce879341facf32e50`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz__a69f3029ba.html`
  > Tether executed a batch freeze of at least two DPRK-laundering-network USDT-TRC20
> addresses on 2025-04-30 07:05 UTC. Both sampled addresses
> (TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz with 302,676 USDT frozen and
> TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3 with 285,733 USDT frozen) show identical freeze
> timestamp down to the minute, indicating a single batch operation. Tether acted 188
> days BEFORE the formal OFAC SDN designation (2025-11-04), making this a non-OFAC-
> triggered corporate policy action — the defining stratum-S5 shape.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3>
  - body_hash: `sha256:200f60acba98b02da2d51134a4d5b8b731d571ebde3c95bea99402e52462300b`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3__f1f6804eff.html`
  > Second sampled address confirming same 2025-04-30 07:05 UTC batch-freeze timestamp. Independent archival anchor.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: DPRK USDT-TRC20 cluster (subset)
- **Chains**: `tron`
- **Addresses**: 2 total (enumerated in event YAML)

> At least 2 of 53 DPRK-cluster USDT-TRC20 addresses frozen on 2025-04-30. Remaining 51
> addresses' freeze status not systematically sampled in the current release. Moving to
> enumeration=complete requires a full batch scan of the 53-address universe (the scanned
> 2/53 both showed matching 2025-04-30 07:05 UTC freeze timestamps, suggesting the
> remaining 51 were likely frozen in the same batch but this is inference, not
> measurement).

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 0h

**Event label**: `batch_freeze_dprk_cluster_pre_ofac_designation`

**Timestamp**: `2025-04-30 07:05:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/29c22d0444c84f77a861064285093eb005cef4ffd656944645766480bcd0bc78>
  - tx_hash: `29c22d0444c84f77a861064285093eb005cef4ffd656944645766480bcd0bc78`
  > Tether USDT-TRC20 addBlackList tx for TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz at 2025-04-30 07:05 UTC. Full 64-char tx hash anchored on TRON.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz>
  - body_hash: `sha256:5d6317eb4970c6d1f570dc8b37892db66664fd3fab838a1ce879341facf32e50`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TA3941uFAvmVibSkQ6fMJXxmaSNovX86mz__a69f3029ba.html`
  > Sampled address #1 — frozen balance 302,676 USDT at 2025-04-30 07:05 UTC (tx
> prefix 29c22d04...d0bc78). attribution=direct because Tether's smart-contract
> addToBlackList() call is the direct action carrying the freeze.
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3>
  - body_hash: `sha256:200f60acba98b02da2d51134a4d5b8b731d571ebde3c95bea99402e52462300b`
  - body_path: `sources/http_captures/dprk-usdt-network-ofac-2025/asset-layer-check/usdtbanlist.com__address-TYxwUhoLPF7AgfG9GaXFEp8CQi8K8KG1m3__f1f6804eff.html`
  > Sampled address #2 — frozen balance 285,733 USDT, exact same timestamp 2025-04-30
> 07:05 UTC (tx prefix bd1f7b7f). Matching minute-level timestamps across two
> independent addresses establish this as a coordinated batch operation rather
> than two coincidental freezes.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `47f4858`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

