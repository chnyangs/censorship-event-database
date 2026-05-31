# Evidence chain — `oko-design-bureau-russia-drone-ofac-2024-05`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c3fb0ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-05-01 OFAC SDN designation of OKO Design Bureau (Russian drone
> developer soliciting crypto donations) is confirmed against the OFAC Recent
> Actions page; no public CEX cascade and no captured on-chain freeze were
> documented in the 14-day window. null_case: limited measurable cross-layer
> surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-05-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240501>
  - Wayback: <https://web.archive.org/web/20240501233749/https://ofac.treasury.gov/recent-actions/20240501>
  - body_hash: `sha256:d86b78737856f92eb040d3fa50142a4beb6f14e9224ff9dfdbc24d431beb4332`
  - body_path: `sources/http_captures/oko-design-bureau-russia-drone-ofac-2024-05/primary/web.archive.org__web-20240502000000-https-ofac.treasury.gov-recent-actions-20240501__211173fbf1.html`
  > OFAC Recent Actions page for 2024-05-01 (Russia-related Designations,
> part of a ~300-target Russia sanctions tranche under EO 14024). OKO
> DESIGN BUREAU (OOO "KB OKO"), a St. Petersburg UAV developer founded in
> 2022, was designated; the SDN entry attaches crypto addresses the firm
> used to solicit donations via a Telegram channel to fund drone
> production for the war in Ukraine. Wayback 20240501233749 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: OKO Design Bureau (OOO KB OKO)

> OKO Design Bureau (a Russian UAV developer) designated as an SDN, with a
> small set of crypto addresses attached as identifiers for the donation-
> solicitation wallets. Coded subset: the action targets the named entity
> plus its attached addresses rather than an exhaustively enumerated complete
> address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-05-01 00:00:00+00:00` → `2024-05-15 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240501>
  - Wayback: <https://web.archive.org/web/20240501233749/https://ofac.treasury.gov/recent-actions/20240501>
  - body_hash: `sha256:d86b78737856f92eb040d3fa50142a4beb6f14e9224ff9dfdbc24d431beb4332`
  - body_path: `sources/http_captures/oko-design-bureau-russia-drone-ofac-2024-05/primary/web.archive.org__web-20240502000000-https-ofac.treasury.gov-recent-actions-20240501__211173fbf1.html`
  > No public CEX policy statement referencing the OKO Design Bureau SDN
> designation was published by major exchanges in the 14-day post-
> designation window. Records the absence of public disclosure; private
> chain-analytics KYT flagging is outside this observation's scope. The
> attached donation wallets raised well under USD 1,000, so the
> measurable offramp-cascade surface is structurally limited.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Crypto donation addresses were attached to the OKO SDN entry, but no

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3fb0ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

