# Evidence chain — `media-land-volosovik-bulletproof-ofac-2025-11`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a7b40fe` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-11-19 OFAC + U.K. + Australia designation of Media Land LLC
> / Aleksandr Volosovik (OFAC recent-actions 20251119, ransomware
> bulletproof hosting) attached one Bitcoin address; native BTC has no
> issuer freeze primitive, no replayable L0 measurement was captured,
> and no public CEX cascade was pinned in the 14-day window. null_case:
> limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-11-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20251119>
  - Wayback: <https://web.archive.org/web/20251121174519/https://ofac.treasury.gov/recent-actions/20251119>
  - body_hash: `sha256:b1c32ad349917087f7302dff5f55585648ee9e6f26eef207a298087d83a80c34`
  - body_path: `sources/http_captures/media-land-volosovik-bulletproof-ofac-2025-11/primary/web.archive.org__web-20251121174519-https-ofac.treasury.gov-recent-actions-20251119__e8171e48aa.html`
  > OFAC Recent Actions page for 2025-11-19 (Cyber-related / CAATSA
> Russia-related designations): designation of Russian
> bulletproof-hosting provider Media Land LLC (St. Petersburg) and
> executives Aleksandr Volosovik (alias "Yalishanda"), Kirill
> Zatolokin, and Yulia Pankova, for enabling ransomware (LockBit,
> BlackSuit, Play) and DDoS infrastructure. One Bitcoin address is
> listed for Volosovik. Coordinated with the U.K. and Australia.
> Wayback memento 20251121174519 pinned.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0319>
  - Wayback: <https://web.archive.org/web/20260114090608/https://home.treasury.gov/news/press-releases/sb0319>
  - body_hash: `sha256:d21345ccc5aeb4b7b5f8653c375c55173c53423a3ae347c5eff20d586d670ad0`
  - body_path: `sources/http_captures/media-land-volosovik-bulletproof-ofac-2025-11/primary/web.archive.org__web-20260114090608-https-home.treasury.gov-news-press-releases-sb0319__f4d38a4e5b.html`
  > U.S. Treasury press release sb0319 (2025-11-19): "United States,
> Australia, and United Kingdom Sanction Russian Cybercrime
> Infrastructure Supporting Ransomware" — the tri-lateral Media
> Land designation. Wayback memento 20260114090608 pinned
> (archived later than the action; corroborating anchor for the
> OFAC recent-actions primary).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Media Land LLC + Aleksandr Volosovik
- **Chains**: `bitcoin`

> Media Land LLC plus executives Aleksandr Volosovik, Kirill
> Zatolokin, and Yulia Pankova (and associated front companies),
> designated as SDNs. One Bitcoin address is listed for Volosovik.
> Marked subset because the action targets the named hosting company /
> individuals and a single attached address rather than an enumerated
> complete address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-11-19 00:00:00+00:00` → `2025-12-03 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20251119>
  - Wayback: <https://web.archive.org/web/20251121174519/https://ofac.treasury.gov/recent-actions/20251119>
  - body_hash: `sha256:b1c32ad349917087f7302dff5f55585648ee9e6f26eef207a298087d83a80c34`
  - body_path: `sources/http_captures/media-land-volosovik-bulletproof-ofac-2025-11/primary/web.archive.org__web-20251121174519-https-ofac.treasury.gov-recent-actions-20251119__e8171e48aa.html`
  > No public CEX policy statement referencing the Media Land /
> Volosovik designation was pinned in the 14-day post-designation
> window in this authoring pass. Records the absence of pinned
> public disclosure; private KYT flagging is outside scope. The
> on-chain footprint is a single native-BTC address (no issuer
> freeze primitive), limiting the measurable cross-layer surface.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): Media Land is a bulletproof-hosting provider, but this event codes
- **asset_onchain** (`not_measured`): One Bitcoin address is attached to the Volosovik SDN entry, but

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a7b40fe`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

