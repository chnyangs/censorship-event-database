# Evidence chain — `dkba-burma-scam-compound-ofac-2025-11`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a785639` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:36:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-11-12 OFAC designation of the DKBA + Trans Asia / Troth Star
> / Chamu Sawang (Treasury sb0312, pig-butchering scam compounds)
> named an armed group and companies with no enumerated on-chain
> addresses; no public CEX cascade was pinned in the 14-day window.
> null_case: infrastructure/entity target with limited measurable
> cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-11-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0312>
  - Wayback: <https://web.archive.org/web/20251114001806/https://home.treasury.gov/news/press-releases/sb0312>
  - body_hash: `sha256:f6fd7f18cb6c852c1119bb239c19f26ecda1a18a4fc7fd9b0c58dc9ea335b242`
  - body_path: `sources/http_captures/dkba-burma-scam-compound-ofac-2025-11/primary/web.archive.org__web-20251114001806-https-home.treasury.gov-news-press-releases-sb0312__c42392aa88.html`
  > U.S. Treasury press release sb0312 (2025-11-12): OFAC designated
> the Democratic Karen Benevolent Army (DKBA), a Burmese armed
> group, and four senior leaders, plus companies Trans Asia
> International Holding Group Thailand and Troth Star and Thai
> national Chamu Sawang, for developing and hosting Chinese-OC
> cyber-scam ("pig butchering" crypto-investment-fraud) compounds —
> including the Tai Chang compound near Myawaddy in Karen State —
> that target Americans. Part of the Scam Center Strike Force.
> Wayback memento 20251114001806 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: DKBA + Trans Asia / Troth Star / Chamu Sawang

> Democratic Karen Benevolent Army (DKBA) + four senior leaders,
> Trans Asia International Holding Group Thailand, Troth Star, and
> Chamu Sawang, designated as SDNs. Marked subset because the action
> targets the named armed group / companies / individuals rather than
> an enumerated complete address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-11-12 00:00:00+00:00` → `2025-11-26 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0312>
  - Wayback: <https://web.archive.org/web/20251114001806/https://home.treasury.gov/news/press-releases/sb0312>
  - body_hash: `sha256:f6fd7f18cb6c852c1119bb239c19f26ecda1a18a4fc7fd9b0c58dc9ea335b242`
  - body_path: `sources/http_captures/dkba-burma-scam-compound-ofac-2025-11/primary/web.archive.org__web-20251114001806-https-home.treasury.gov-news-press-releases-sb0312__c42392aa88.html`
  > No public CEX policy statement referencing the DKBA / Trans
> Asia / Troth Star designation was pinned in the 14-day
> post-designation window in this authoring pass. Records the
> absence of pinned public disclosure; private KYT flagging is
> outside scope. The SDN names an armed group / companies (no
> enumerated addresses), so the measurable offramp surface is
> structurally limited.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a785639`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

