# Evidence chain — `al-law-hezbollah-crypto-ofac-2024-03`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `96a9483` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2024-03-26 SDN designation (jy2209) of Hizballah/IRGC-QF crypto
> financier Tawfiq Muhammad Sa'id al-Law named a single USDT-on-Tron address
> (TWBAPzpP...wkWG). No public CEX cascade was documented in the 14-day window.
> null_case: individual crypto-financier target with limited measurable
> cross-layer surface at draft time; a future Tether-Tron freeze confirmation
> could elevate an asset_onchain row to direct under codebook §1.2."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-03-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2209>
  - Wayback: <https://web.archive.org/web/20240326154347/https://home.treasury.gov/news/press-releases/jy2209>
  - body_hash: `sha256:604a162d4136ca4ec092e06ebcc6d950e844db40c4451096febb3b5035764ba5`
  - body_path: `sources/http_captures/al-law-hezbollah-crypto-ofac-2024-03/primary/web.archive.org__web-20240326000000-https-home.treasury.gov-news-press-releases-jy2209__314cf7a7bf.html`
  > Treasury press release jy2209 (2024-03-26) "Treasury Targets Qods Force,
> Houthi, and Hizballah Finance and Trade Facilitators". OFAC designated
> Lebanon-based Syrian money exchanger Tawfiq Muhammad Sa'id al-Law under
> EO 13224 for providing Hizballah with digital wallets to receive funds
> from IRGC-QF commodity sales and for facilitating cryptocurrency
> transfers for sanctioned Hizballah operators. Wayback 20240326154347
> pinned; grep verifies 8xal-Law, 4xAl-Law, 5x"March 26, 2024".
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240326>
  - Wayback: <https://web.archive.org/web/20240326151735/https://ofac.treasury.gov/recent-actions/20240326>
  - body_hash: `sha256:0908e9a28cbb264de13f22a0e57a6b2d8e0eb1ae906e7669dcef96747abcb15e`
  - body_path: `sources/http_captures/al-law-hezbollah-crypto-ofac-2024-03/primary/web.archive.org__web-20240326000000-https-ofac.treasury.gov-recent-actions-20240326__cf3fe7dad6.html`
  > OFAC Recent Actions page for 2024-03-26, the formal SDN-list publication
> accompanying jy2209. Al-Law's SDN entry carries a USDT-on-Tron address
> identifier (TWBAPzpPiZarfVsY2BLXeaLhNHurn4wkWG), previously seized by
> Israel's NBCTF (~$1.7M, July 2023). Independent primary anchor for the
> designation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Tawfiq Muhammad Sa'id al-Law (Hizballah/IRGC-QF crypto financier)
- **Chains**: `tron`
- **Addresses**: 1 total (enumerated in event YAML)

> Tawfiq Muhammad Sa'id al-Law (Lebanon-based Syrian money exchanger),
> Hizballah/IRGC-QF crypto financier. His SDN entry names a single USDT-on-Tron
> address identifier. Subset enumeration: al-Law is the crypto-financier node
> within the broader jy2209 Qods-Force/Houthi/Hizballah action; the
> transportation/tanker co-designees are out of this event's target scope.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-03-26 00:00:00+00:00` → `2024-04-09 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240326>
  - Wayback: <https://web.archive.org/web/20240326151735/https://ofac.treasury.gov/recent-actions/20240326>
  - body_hash: `sha256:0908e9a28cbb264de13f22a0e57a6b2d8e0eb1ae906e7669dcef96747abcb15e`
  - body_path: `sources/http_captures/al-law-hezbollah-crypto-ofac-2024-03/primary/web.archive.org__web-20240326000000-https-ofac.treasury.gov-recent-actions-20240326__cf3fe7dad6.html`
  > No public CEX policy statement explicitly naming al-Law's SDN entry
> was published by major exchanges in the 14-day post-designation
> window. Records absence of public disclosure; private chain-analytics
> KYT flagging is outside this observation's scope.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `96a9483`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

