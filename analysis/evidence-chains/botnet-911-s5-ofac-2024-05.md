# Evidence chain — `botnet-911-s5-ofac-2024-05`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4e61290` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:35:41Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-05-28 OFAC SDN designation of the 911 S5 botnet network (Yunhe Wang
> et al., virtual-currency addresses attached — the 49-address count is
> enumerated in the SDN-list entry) is confirmed against Treasury jy2375;
> no public CEX cascade and no captured on-chain freeze were documented in the
> 14-day window. null_case: limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-05-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2375>
  - Wayback: <https://web.archive.org/web/20240528232624/https://home.treasury.gov/news/press-releases/jy2375>
  - body_hash: `sha256:291f54f8b94689ff177e9d71baf66793b663990f4484ecd7e3c38bf42c1134f5`
  - body_path: `sources/http_captures/botnet-911-s5-ofac-2024-05/primary/web.archive.org__web-20240529000000-https-home.treasury.gov-news-press-releases-jy2375__708636ae49.html`
  > U.S. Treasury press release jy2375 (2024-05-28): OFAC designated three
> Chinese nationals — Yunhe Wang, Jingping Liu, and Yanni Zheng — and
> three Thailand-based entities (Spicy Code Company Limited, Tulip Biz
> Pattaya Group Company Limited, Lily Suites Company Limited) for their
> roles in the 911 S5 residential-proxy botnet (~19M compromised IPs).
> The SDN entry for Yunhe Wang attaches 49 cryptocurrency addresses as
> identifiers. Wayback 20240528232624 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: 911 S5 botnet network (Yunhe Wang et al.)

> Three individuals (Yunhe Wang, Jingping Liu, Yanni Zheng) and three Thai
> entities designated as SDNs; 49 crypto addresses attached to Yunhe Wang as
> identifiers. Coded subset: the action targets the named cybercrime network
> plus the attached address set rather than an exhaustively enumerated
> complete on-chain footprint.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-05-28 00:00:00+00:00` → `2024-06-11 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2375>
  - Wayback: <https://web.archive.org/web/20240528232624/https://home.treasury.gov/news/press-releases/jy2375>
  - body_hash: `sha256:291f54f8b94689ff177e9d71baf66793b663990f4484ecd7e3c38bf42c1134f5`
  - body_path: `sources/http_captures/botnet-911-s5-ofac-2024-05/primary/web.archive.org__web-20240529000000-https-home.treasury.gov-news-press-releases-jy2375__708636ae49.html`
  > No public CEX policy statement referencing the 911 S5 / Yunhe Wang
> SDN designation was published by major exchanges in the 14-day post-
> designation window. Records the absence of public disclosure; private
> chain-analytics KYT flagging of the 49 attached addresses is outside
> this observation's scope.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): 49 crypto addresses were attached to Yunhe Wang's SDN entry, but no

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4e61290`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

