# Evidence chain — `kb-vostok-russia-drone-ofac-2024-08`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `292f041` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:47:34Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-08-23 OFAC SDN designation of KB Vostok (Russian drone developer;
> USDT-TRON address attached) is confirmed against the OFAC Recent Actions
> page; no public CEX cascade and no captured on-chain freeze were documented
> in the 14-day window. null_case: limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-08-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240823>
  - Wayback: <https://web.archive.org/web/20240824102141/https://ofac.treasury.gov/recent-actions/20240823>
  - body_hash: `sha256:75fdcf87f48e255a6a72f21fea4448bbd7440f1e238f83f0871823d0e716d72c`
  - body_path: `sources/http_captures/kb-vostok-russia-drone-ofac-2024-08/primary/web.archive.org__web-20240824120000-https-ofac.treasury.gov-recent-actions-20240823__ca41de774a.html`
  > OFAC Recent Actions page for 2024-08-23 (Russia-related Designations, a
> ~400-target tranche under EO 14024). KB VOSTOK OOO (Vostok Design
> Bureau), a Russian UAV developer whose drones are used by Russian forces
> in Ukraine, was designated; a USDT (TRON) address used to solicit
> donations and likely facilitate drone sales is attached to the SDN
> entry. Wayback 20240824102141 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KB Vostok OOO (Vostok Design Bureau)
- **Chains**: `tron`

> KB Vostok (a Russian UAV developer) designated as an SDN, with a USDT-on-
> TRON donation/sales address attached as an identifier. Coded subset: the
> action targets the named entity plus its attached address rather than an
> exhaustively enumerated complete address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-08-23 00:00:00+00:00` → `2024-09-06 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240823>
  - Wayback: <https://web.archive.org/web/20240824102141/https://ofac.treasury.gov/recent-actions/20240823>
  - body_hash: `sha256:75fdcf87f48e255a6a72f21fea4448bbd7440f1e238f83f0871823d0e716d72c`
  - body_path: `sources/http_captures/kb-vostok-russia-drone-ofac-2024-08/primary/web.archive.org__web-20240824120000-https-ofac.treasury.gov-recent-actions-20240823__ca41de774a.html`
  > No public CEX policy statement referencing the KB Vostok SDN
> designation was published by major exchanges in the 14-day post-
> designation window. Records the absence of public disclosure; private
> chain-analytics KYT flagging of the attached USDT-TRON address (whose
> inflows trace largely to the sanctioned exchange Garantex) is outside
> this observation's scope.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): A USDT-on-TRON address was attached to the KB Vostok SDN entry, but no

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `292f041`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

