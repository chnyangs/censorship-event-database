# Evidence chain — `sinbad-ofac-2023`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `138003a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:34:18Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of the Sinbad Bitcoin mixer on
> 2023-11-29 did not cause a short-term takedown of the canonical sinbad.io frontend
> (reachable with identical content 23 hours post-event and 10 days post-event), in
> structural contrast to the Ethereum-protocol Tornado Cash 2022 case where frontend
> disruption occurred within ~22 hours."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-11-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20231129>
  - Wayback: <https://web.archive.org/web/20260421132612/https://ofac.treasury.gov/recent-actions/20231129>
  - body_hash: `sha256:ec3e5d7d3d5c0e7e5bc70c4241ccbcb57d329294be09724fdd736cd5ba3af850`
  - body_path: `sources/http_captures/sinbad-ofac-2023/ofac-recent-actions/ofac.treasury.gov__recent-actions-20231129__1876f9adb5.html`
  > OFAC Recent Actions page for 2023-11-29. SDN entry SINBAD (a.k.a. SINBAD.IO) — Bitcoin
> mixer, DPRK-linked; tags [DPRK3] [CYBER2]; designated as a Tornado Cash-successor mixer.
> 2 XBT addresses attached to the entity SDN entry; no ETH / stablecoin addresses on this
> event.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1933>
  - body_hash: `sha256:8953cd84fc18034316fcf2a5eaca663dd7669d7a603f1485f605b3f8f26351f7`
  - body_path: `sources/http_captures/sinbad-ofac-2023/v0_3_repair/home.treasury.gov__news-press-releases-jy1933__e05f867e9a.html`
  > Treasury press release "Treasury Sanctions Mixer Used by the DPRK" (2023-11-29).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Protocol**: `sinbad_io`
- **Actor name**: Sinbad
- **Chains**: `bitcoin`
- **Addresses**: 2 total (enumerated in event YAML)
- **Canonical domains**: `sinbad.io`

> Full set of 2 unique Bitcoin addresses attached to the SINBAD / SINBAD.IO SDN entity entry,
> extracted verbatim from the OFAC Recent Actions page for 2023-11-29. One Bech32 address and
> one legacy P2PKH address. Bitcoin-only target; no ETH, stablecoin, or other chain addresses
> were designated.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l4_frontend — `canonical_frontend_remained_reachable_and_unchanged_through_designation`

**Window**: `2023-11-29 00:00:00+00:00` → `2023-12-09 23:59:59+00:00`

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20231129232541/http://sinbad.io/>
  - body_hash: `sha256:c97c13e8e6f23839ea53e5bc2f8f7b3a69894fb6c72c4ee34f6174e1a2566ba4`
  - body_path: `sources/http_captures/sinbad-ofac-2023/frontend-wayback/web.archive.org__web-20231129232541-http-sinbad.io__a971040b77.html`
  > Wayback snapshot on event day 2023-11-29 at 23:25:41 UTC (≈23 hours after the OFAC
> designation was posted). Response 200, digest IS6YYGAQL2HB2VBBPESTEURU4ZVB236P. Same
> digest observed at 2023-11-30 08:09 and 2023-12-04 (revisit) per Wayback CDX —
> content was identical through early December.
- **`semi_primary_wayback`**
  - URL: <https://web.archive.org/web/20231209124309/https://sinbad.io/>
  - body_hash: `sha256:f9528eab19a8bf734e03bd9419677740b07408c22c9cbcde31a665e8ba4c83fb`
  - body_path: `sources/http_captures/sinbad-ofac-2023/frontend-wayback/web.archive.org__web-20231209124309-https-sinbad.io__65c801905c.html`
  > Second Wayback snapshot 10 days post-event (2023-12-09 12:43 UTC); 200 OK, digest
> FI6T7CEP7FCV7ODO6YLF66RALUWSH5SL — a variant of the earlier page but with matching
> core structure, demonstrating the frontend remained operational. Independent anchor
> from the event-day snapshot.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `138003a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

