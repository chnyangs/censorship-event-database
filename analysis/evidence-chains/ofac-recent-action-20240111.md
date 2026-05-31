# Evidence chain — `ofac-recent-action-20240111`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71ac901` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC Recent Action 2024-01-11 bundled Russia-related EO14024 designations
> (1 individual + 2 defense entities + 3 aircraft, none carrying crypto
> addresses), a non-substantive metadata refresh of the existing CHATEX
> cyber-related SDN entry (30 addresses unchanged from 2021-11-08), and a
> periodic Federal Civil Penalties inflation adjustment. The crypto-relevant
> content does not constitute a fresh enforcement event; cascade analysis
> for the listed addresses is anchored in `chatex-ofac-2021`."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-01-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240111>
  - Wayback: <https://web.archive.org/web/20240111161039/https://ofac.treasury.gov/recent-actions/20240111>
  - body_hash: `sha256:b70c56945d08e152f154f86af0c95865eda4d910978d653277c359b84d20e252`
  - body_path: `sources/http_captures/ofac-recent-action-20240111/primary/web.archive.org__web-20240111161039-https-ofac.treasury.gov-recent-actions-20240111__196cc1ca4d.html`
  > OFAC Recent Actions page for 2024-01-11 with title "Russia-related
> Designations and Designations Updates; Cyber-related Designation
> Update; Implementation of the Federal Civil Penalties Inflation
> Adjustment Act." v0.3 audit 2026-05-20 (c) Batch C-1: Wayback
> memento 20240111161039 pinned (94420 bytes); grep confirms 1xCHATEX
> + 59 Digital Currency Address entries (≈30 unique addresses × 2 for
> the -from-/-to- SDN diff form). Original draft cited the local
> cache file sources/ofac_sdn_diffs/recent_actions_cache/20240111.html
> (body_hash f4e2908c...) which IS valid (file present on disk) but
> replaced here with Wayback memento for citation-pattern consistency
> with other audited S1 events.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `chatex_exchange`
- **Actor name**: Chatex (administrative re-listing)
- **Chains**: `bitcoin`, `ethereum`, `ripple`
- **Addresses**: 30 total (enumerated in event YAML)
- **Canonical domains**: `chatex.com`

> The OFAC page enumerates 30 digital-currency addresses (22 XBT, 6 ETH, 1
> USDT-Omni, 1 XRP) under a "The following changes have been made to OFAC's
> SDN List" -> CHATEX block. v0.3 audit 2026-05-20 (c) Batch C-1: direct
> OFAC RA Wayback grep confirms the 30 addresses appear as 59 "Digital
> Currency Address" entries (≈30 unique × 2 for the -from-/-to- SDN diff
> form). Diff between the -from- and -to- text shows address set, alias
> list, website, and country fields are *identical*: this is a non-
> substantive metadata refresh of the CHATEX SDN entry first published
> 2021-11-08 (covered by event `chatex-ofac-2021`), not a fresh crypto
> enforcement action. enumeration upgraded pending->complete reflecting
> the verified address list. None of the other 2024-01-11 designations
> carry crypto addresses (see analysis_notes for the full per-action
> breakdown).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_fresh_cex_cascade_for_chatex_metadata_refresh`

**Window**: `2024-01-11 00:00:00+00:00` → `2024-01-25 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240111>
  - Wayback: <https://web.archive.org/web/20240111161039/https://ofac.treasury.gov/recent-actions/20240111>
  - body_hash: `sha256:b70c56945d08e152f154f86af0c95865eda4d910978d653277c359b84d20e252`
  - body_path: `sources/http_captures/ofac-recent-action-20240111/primary/web.archive.org__web-20240111161039-https-ofac.treasury.gov-recent-actions-20240111__196cc1ca4d.html`
  > OFAC Recent Actions page substantiates the trigger event
> (CHATEX SDN entry metadata refresh + Russia-related new
> additions for defense/aviation actors). The CHATEX
> re-listing introduces no new crypto addresses (already on
> SDN since 2021-11-08 per chatex-ofac-2021). No fresh public
> CEX policy statement in 14d window is the expected null
> finding for an administrative metadata refresh.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No L0 OONI / Censored Planet probe slice attached. Substrate not
- **l1_consensus** (`not_measured`): No event-specific L1 Wahrstätter / relayscan slice attached. The
- **l3_rpc** (`not_measured`): No pinned MEV-Blocker / OFAC-compliant RPC filter-list snapshot
- **l4_frontend** (`not_measured`): No Wayback bracketing of chatex.com around 2024-01-11 is attached.

## 7. Related events

- [`chatex-ofac-2021`](./chatex-ofac-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71ac901`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

