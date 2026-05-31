# Evidence chain — `aeza-group-ofac-2025`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `dbf5e31` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of the Aeza Group Russian bulletproof-hosting network on 2025-07-01
> targeted an upstream infrastructure layer rather than a consumer-facing crypto service.
> Primary observational gap: Wayback post-event snapshots of aeza.ru / aeza.net and TRX
> freeze data not yet attached."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-07-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20250701>
  - Wayback: <https://web.archive.org/web/20260421143729/https://ofac.treasury.gov/recent-actions/20250701>
  - body_hash: `sha256:af4c4f34b9a24535fa556b3e8b853f4a4fa6af44b57bde133edd57cbb2476e22`
  - body_path: `sources/http_captures/aeza-group-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20250701__4afdb9fe8c.html`
  > OFAC Recent Actions page for 2025-07-01. AEZA GROUP LLC (Russia-based bulletproof
> hosting provider) + AEZA INTERNATIONAL LTD (UK) + AEZA LOGISTIC LLC (Russia) +
> CLOUD SOLUTIONS LLC + multiple individual officers (GAST, KNYAZEV, PENZEV and
> additional directors). Websites named: aeza.ru, aeza.net, aezadns.com. One TRX
> digital-currency address attached to AEZA GROUP LLC entity entry. Tags [CAATSA -
> RUSSIA] [CYBER4].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0188>
  > Treasury press release "Treasury Sanctions Global Bulletproof Hosting Service Enabling Cybercriminals and Technology Theft" (2025-07-01).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `aeza_hosting`
- **Actor name**: Aeza Group
- **Chains**: `tron`
- **Addresses**: 1 total (enumerated in event YAML)
- **Canonical domains**: `aeza.ru`, `aeza.net`, `aezadns.com`

> Aeza is treated as an entity-level target (bulletproof hosting provider with multiple
> aliased corporate shells + affiliated individuals). 1 TRX digital-currency address was
> attached but the event is primarily an entity / infrastructure designation rather than
> address-set driven.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 30.42h

**Event label**: `tether_usdt_tron_blacklist_30h_after_ofac`

**Timestamp**: `2025-07-02 06:25:00+00:00` (precision: `minute`)

**Sources**:

- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/38ffd94e58210970bb1c5359aca6794b638530c7555eb3e10cacc3dc8c340fc9>
  - tx_hash: `38ffd94e58210970bb1c5359aca6794b638530c7555eb3e10cacc3dc8c340fc9`
  > Tether USDT-TRC20 addBlackList tx for Aeza's TRX address TU4tDFRvcKhAZ1jdihojmBWZqvJhQCnJ4F at 2025-07-02 06:25 UTC (~30h after OFAC designation).
- **`primary_corporate`**
  - URL: <https://usdtbanlist.com/address/TU4tDFRvcKhAZ1jdihojmBWZqvJhQCnJ4F>
  - body_hash: `sha256:e256728ea510f7b63a7ddf10549b9b1ca10cebdd470536e87ea66109f49e9a36`
  - body_path: `sources/http_captures/aeza-group-ofac-2025/asset-layer-check/usdtbanlist.com__address-TU4tDFRvcKhAZ1jdihojmBWZqvJhQCnJ4F.html`
  > usdtbanlist.com community tracker archival anchor.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **l4_frontend** (`not_measured`): Wayback CDX for aeza.ru / aeza.net in the 2025-06 / 2025-07 window is not included in this release (CDX API timed out during automated capture). The public claim excludes L4 until direct Wayback snapshot anchors are attached.
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `dbf5e31`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

