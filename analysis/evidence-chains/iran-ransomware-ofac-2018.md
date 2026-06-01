# Evidence chain — `iran-ransomware-ofac-2018`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad910b8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:40:01Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC first on-chain sanction (2018-11-28 Iran ransomware facilitators) produced no
> observable cross-layer cascade. The targeted individuals' associated website (enexchanger.com)
> persisted unchanged through a 20-day window bracketing the designation. Direct asset-layer
> reactions are structurally impossible (Bitcoin native chain, no issuer freeze) and L1 / L3
> Ethereum layers did not yet have OFAC-relevant infrastructure."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2018-11-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20181128>
  - Wayback: <https://web.archive.org/web/20260421140931/https://ofac.treasury.gov/recent-actions/20181128>
  - body_hash: `sha256:cd4dc480fb0a3659458f82d30e107a61fb1059f933464d43472c228fe4bc4c40`
  - body_path: `sources/http_captures/iran-ransomware-ofac-2018/ofac-recent-actions/ofac.treasury.gov__recent-actions-20181128__d39d4e5882.html`
  > OFAC Recent Actions page for 2018-11-28. **Historically the first-ever SDN entries to
> include digital-currency addresses** ("for the First Time Identifies Associated Digital
> Currency Addresses" per the press-release title). Two Iranian individuals:
> Mohammad GHORBANIYAN (aka EnExchanger, website enexchanger.com) and Ali KHORASHADIZADEH
> — SamSam-ransomware facilitators. Each carries one XBT address. Tag [CYBER2].
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm556>
  - body_hash: `sha256:5237f74b36ca761cd2b6056b69cee173aaf8675de4c037bdb03dfa35fa1fa96b`
  - body_path: `sources/http_captures/iran-ransomware-ofac-2018/v0_3_repair/home.treasury.gov__news-press-releases-sm556__328e97f0bd.html`
  > Treasury press release "Treasury Designates Iran-Based Financial Facilitators of Malicious Cyber Activity and for the First Time Identifies Associated Digital Currency Addresses" (2018-11-28).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: GHORBANIYAN + KHORASHADIZADEH
- **Chains**: `bitcoin`
- **Addresses**: 2 total (enumerated in event YAML)
- **Canonical domains**: `enexchanger.com`

> 2 unique Bitcoin addresses — one per individual SDN entry. The historical anchor of the
> entire dataset: the first on-chain sanction action in OFAC's history.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l4_frontend — `redirect_shell_unchanged_pre_and_post_designation`

**Window**: `2018-11-23 00:00:00+00:00` → `2018-12-12 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20181123094507/http://enexchanger.com/>
  - body_hash: `sha256:dcb7c6e97a55aba3e84245fe4bbff63e4255e33eff0e2feb5f682cab834dd1a7`
  - body_path: `sources/http_captures/iran-ransomware-ofac-2018/frontend-wayback/web.archive.org__web-20181123094507-http-enexchanger.com__cf3a7b8821.html`
  > Pre-event Wayback snapshot 2018-11-23 (5 days before designation). 303 redirect with
> digest 4WO4P3H4OIGHSLGBJG2L3SGKLOED3WNU per CDX.
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20181212063124/http://www.enexchanger.com/>
  - body_hash: `sha256:85842344f112567e6cb7de348a9b3343957a448154d327b14e50eb14966450f2`
  - body_path: `sources/http_captures/iran-ransomware-ofac-2018/frontend-wayback/web.archive.org__web-20181212063124-http-www.enexchanger.com__b9cb6763bc.html`
  > Post-event Wayback snapshot 2018-12-12 (14 days after designation). 303 redirect
> with digest JQ4LSL5LOS2KX6REN2UWAGNQBX5GEK4C; differs from pre-event digest because
> it resolves the www. subdomain (different Host header path), but structurally the
> same redirect-shell shape. The domain operator did not shut it down and US-side
> infrastructure (DNS / CDN / registrar) did not enforce the OFAC listing against the
> cleartext domain.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): (no note)
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad910b8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

