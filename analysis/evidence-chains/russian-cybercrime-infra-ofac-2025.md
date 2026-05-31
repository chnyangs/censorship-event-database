# Evidence chain — `russian-cybercrime-infra-ofac-2025`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `ad034bc` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:58:50Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Joint US/UK/AU OFAC designation of Russian cybercrime infrastructure operators on
> 2025-11-19 attached 1 BTC address and expanded the Aeza / bulletproof-hosting designee
> network. Demonstrates sustained 2025 policy focus on hosting-layer targets."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2025-11-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20251119>
  - Wayback: <https://web.archive.org/web/20260421145405/https://ofac.treasury.gov/recent-actions/20251119>
  - body_hash: `sha256:46e63807771652434207876bb2ff300d532b707b8b26197c50570a3146372b46`
  - body_path: `sources/http_captures/russian-cybercrime-infra-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20251119__70ef558d9d.html`
  > OFAC Recent Actions page for 2025-11-19. Joint US/UK/Australia action against
> Russian cybercrime infrastructure supporting ransomware. Multiple individuals
> designated including VOLOSOVIK Aleksandr (aka Yalishanda / Ohyeahhellno /
> podzemniy1) — bulletproof hosting operator with 1 XBT address — plus MAKAROV
> Maksim (linked to AEZA GROUP), PANKOVA Yulia, ZAKIROV Ilya. Tags [CAATSA - RUSSIA]
> [CYBER4]. Follows the 2025-07-01 Aeza Group designation (AEZA GROUP LLC linkage).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0314>
  > Treasury press release "United States, Australia, and United Kingdom Sanction Russian Cybercrime Infrastructure Supporting Ransomware" (2025-11-19).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Russian bulletproof hosting operators
- **Chains**: `bitcoin`
- **Addresses**: 1 total (enumerated in event YAML)

> 1 XBT address attached to VOLOSOVIK Aleksandr (Yalishanda). Other designees (MAKAROV,
> PANKOVA, ZAKIROV) carry no on-chain addresses.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2025-11-19 00:00:00+00:00` → `2025-12-03 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20251119>
  - body_hash: `sha256:46e63807771652434207876bb2ff300d532b707b8b26197c50570a3146372b46`
  - body_path: `sources/http_captures/russian-cybercrime-infra-ofac-2025/ofac-recent-actions/ofac.treasury.gov__recent-actions-20251119__70ef558d9d.html`
  > No public CEX policy statement referencing VOLOSOVIK (Yalishanda) 1 BTC address was published by major
> exchanges (Binance, Kraken, Coinbase, Bybit) in the 14-day post-designation
> window. Observation records the absence of public disclosure; private
> chain-analytics flagging workflows (Chainalysis / Elliptic / TRM) are outside
> the scope of this observation and may have produced unpublished KYT flags.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`aeza-group-ofac-2025`](./aeza-group-ofac-2025.md)
- [`zservers-ofac-2025`](./zservers-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad034bc`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

