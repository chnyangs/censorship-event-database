# Evidence chain — `nemesis-parsarad-darknet-ofac-2025-03`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a888d9d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-03-04 OFAC SDN designation of Behrouz Parsarad (Nemesis darknet-
> market administrator; 49 BTC/XMR addresses attached) is confirmed against the
> OFAC Recent Actions page; no public CEX cascade and no captured on-chain
> enforcement were documented in the 14-day window. null_case: limited
> measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-03-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250304>
  - Wayback: <https://web.archive.org/web/20250304201959/https://ofac.treasury.gov/recent-actions/20250304>
  - body_hash: `sha256:fb6757db855c58916726cfa1b22ebea67f912d7ff24597db6585ffd7fa27b495`
  - body_path: `sources/http_captures/nemesis-parsarad-darknet-ofac-2025-03/primary/web.archive.org__web-20250305000000-https-ofac.treasury.gov-recent-actions-20250304__b643fa30bc.html`
  > OFAC Recent Actions page for 2025-03-04 (Counter Narcotics
> Designation). Iran-based Behrouz Parsarad, the administrator of the
> Nemesis darknet marketplace, was designated for facilitating fentanyl
> and other drug sales; the SDN entry attaches 49 virtual-currency
> addresses (44 BTC, 5 XMR) used by Parsarad. Nemesis had ~30,000 users /
> 1,000 vendors before its servers were seized in March 2024. Wayback
> 20250304201959 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Behrouz Parsarad (Nemesis Market administrator)

> Behrouz Parsarad (Nemesis darknet-market administrator) designated as an
> SDN, with 49 crypto addresses (44 BTC, 5 XMR) attached as identifiers.
> Coded subset: the action targets the named individual plus the attached
> address set rather than an exhaustively enumerated complete on-chain
> footprint.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-03-04 00:00:00+00:00` → `2025-03-18 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250304>
  - Wayback: <https://web.archive.org/web/20250304201959/https://ofac.treasury.gov/recent-actions/20250304>
  - body_hash: `sha256:fb6757db855c58916726cfa1b22ebea67f912d7ff24597db6585ffd7fa27b495`
  - body_path: `sources/http_captures/nemesis-parsarad-darknet-ofac-2025-03/primary/web.archive.org__web-20250305000000-https-ofac.treasury.gov-recent-actions-20250304__b643fa30bc.html`
  > No public CEX policy statement referencing the Behrouz Parsarad /
> Nemesis SDN designation was published by major exchanges in the
> 14-day post-designation window. Records the absence of public
> disclosure; private chain-analytics KYT flagging of the 49 attached
> BTC/XMR addresses is outside this observation's scope.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): 49 crypto addresses (44 BTC, 5 XMR) were attached to Parsarad's SDN entry,

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a888d9d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

