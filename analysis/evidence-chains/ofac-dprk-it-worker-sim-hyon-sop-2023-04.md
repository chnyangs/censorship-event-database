# Evidence chain — `ofac-dprk-it-worker-sim-hyon-sop-2023-04`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ff0c8be` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:07:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2023-04-24 SDN designation of Sim Hyon Sop (DPRK national, KKBC deputy
> representative) named a single EVM wallet (0x4f47bc49...96270c) duplicated across
> ETH / Arbitrum / BSC chain entries. First major individual-IT-worker DPRK proxy
> SDN with named cryptocurrency wallets. Cross-layer cascade not yet measured at
> draft time; serves as the EVM-multi-chain transition datapoint between
> lazarus-laundering-ofac-2020 (BTC-only) and dprk-usdt-network-ofac-2025 (USDT-TRON
> concentrated)."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-04-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230424>
  - Wayback: <https://web.archive.org/web/20230424145345/https://ofac.treasury.gov/recent-actions/20230424>
  - body_hash: `sha256:fb454dfc2c02d46f8a89a992af2666e452415d7fec92440d6a28379fed393f6e`
  - body_path: `sources/http_captures/ofac-dprk-it-worker-sim-hyon-sop-2023-04/primary/web.archive.org__web-20230424145345-https-ofac.treasury.gov-recent-actions-20230424__31961d71fb.html`
  > OFAC Recent Actions page for 2023-04-24. Three individuals designated under
> DPRK-related authorities (DPRK3 / EO 13382): Sim Hyon Sop (DPRK national, KKBC
> deputy representative), Wu Huihui (PRC OTC trader), and Cheng Hung Man (HK OTC
> facilitator). Sim Hyon Sop's SDN entry carries named digital-currency addresses
> on ETH / ARB / BSC. Wu Huihui entry carries 17 BTC addresses. This is the first
> major OFAC SDN action naming an individual DPRK-state IT-worker financial proxy
> with enumerated cryptocurrency wallets. v0.3 audit 2026-05-20 (c) Batch C-1:
> Wayback memento 20230424145345 pinned (90951 bytes), grep verifies 13xNorth
> Korea + 3x0x4f47bc + 2xDPRK + 1xSIM Hyon + 1xKWANGSON. 3 EVM entries confirmed
> (user-facts 4 was incorrect — only the single canonical hex appears 3 times
> across ETH/ARB/BSC chain prefixes).
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1435>
  - Wayback: <https://web.archive.org/web/20230424174539/https://home.treasury.gov/news/press-releases/jy1435>
  - body_hash: `sha256:a2a293441f8ea50363e2cdf5accba88beba14c5a4b9ae86d29b1182735bafd79`
  - body_path: `sources/http_captures/ofac-dprk-it-worker-sim-hyon-sop-2023-04/primary/web.archive.org__web-20230424174539-https-home.treasury.gov-news-press-releases-jy1435__a9c0188e29.html`
  > Treasury press release jy1435 "Treasury Targets Actors Facilitating Illicit DPRK
> Financial Activity in Support of Weapons Programs" (2023-04-24). Names Sim Hyon
> Sop's role as KKBC deputy representative coordinating millions in financial
> transfers (including virtual currency from DPRK IT workers fraudulently employed
> overseas) on behalf of the DPRK regime's WMD / ballistic-missile programs.
> v0.3 audit 2026-05-20 (c) Batch C-1: Wayback memento 20230424174539 pinned
> (184482 bytes), grep verifies 68xDPRK + 14xjy1435 + 10xKKBC + 4xApril 24 +
> 4x2023-04-24 + 2xWu Huihui + 2xSim Hyon Sop + 2xKwangson + 2xCheng Hung.
- **`primary_legal`**
  - URL: <https://www.federalregister.gov/documents/2023/04/27/2023-08944/notice-of-ofac-sanctions-actions>
  - Wayback: <https://web.archive.org/web/20230427165305/https://www.federalregister.gov/documents/2023/04/27/2023-08944/notice-of-ofac-sanctions-actions>
  - body_hash: `sha256:244695c8282bf6000389b3efa767bbd43e9bf19845648690061a1bad0974875d`
  - body_path: `sources/http_captures/ofac-dprk-it-worker-sim-hyon-sop-2023-04/primary/web.archive.org__web-20230427165305-https-www.federalregister.gov-documents-2023-04-27-2023-08944-notice-of-ofac-sanctions-actions__ded306096a.html`
  > Federal Register Notice 2023-08944 (published 2023-04-27) formalizing the
> 2023-04-24 OFAC sanctions actions. v0.3 audit 2026-05-20 (c) Batch C-1:
> Wayback memento 20230427165305 pinned (204208 bytes), grep verifies
> 26x2023-08944 + 9xNorth Korea + 3x0x4f47bc + 2xKWANGSON + 2xDPRK +
> 1xWU HUIHUI + 1xSIM Hyon + 2xApril 24.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Sim Hyon Sop (KKBC deputy representative)
- **Chains**: `ethereum`, `arbitrum`, `bsc`
- **Addresses**: 1 total (enumerated in event YAML)

> Sim Hyon Sop SDN entry (DPRK national, KKBC deputy representative). The OFAC
> designation enumerates digital-currency addresses across multiple chains. Per
> public reporting (Chainalysis, TRM, OpenSanctions), Sim's entry carries the same
> EVM-format wallet duplicated across ETH / ARB / BSC chain prefixes (treated as
> three distinct SDN-list entries). The user's facts cite "4 crypto addresses" for
> Sim — only 3 EVM entries are independently confirmable from public reporting at
> draft time. Subset enumeration with class-level rationale: Sim individual + KKBC
> proxy role + named EVM wallet (one canonical hex across ETH/ARB/BSC). Companion
> Wu Huihui (17 BTC) and Cheng Hung Man entries are out of scope for this event's
> target (Sim is the primary DPRK-state-proxy individual; Wu/Cheng are PRC/HK OTC
> facilitators on the same RA page and could be split into sibling events).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-04-24 00:00:00+00:00` → `2023-05-08 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230424>
  - Wayback: <https://web.archive.org/web/20230424145345/https://ofac.treasury.gov/recent-actions/20230424>
  - body_hash: `sha256:fb454dfc2c02d46f8a89a992af2666e452415d7fec92440d6a28379fed393f6e`
  - body_path: `sources/http_captures/ofac-dprk-it-worker-sim-hyon-sop-2023-04/primary/web.archive.org__web-20230424145345-https-ofac.treasury.gov-recent-actions-20230424__31961d71fb.html`
  > Coverage gap at draft time: no public CEX policy statement explicitly naming
> Sim Hyon Sop's SDN entry has been pinned. Observation recorded for
> completeness; attribution=none until either (a) a 14d post-event public CEX
> announcement scan is completed and observed_no_change can be substantiated, or
> (b) a specific CEX deposit-block / account-freeze cite is pinned.
> v0.3 audit 2026-05-20 (c) Batch C-1: source body_path swapped from
> contextual_unarchived to Wayback memento; coverage_gap observation kind
> unchanged (still no public CEX cite pinned, deferred enrichment).

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Sim's named EVM wallet (0x4f47bc49...96270c) is a USDC / USDT / stablecoin-eligible

## 7. Related events

- [`lazarus-entity-ofac-2019`](./lazarus-entity-ofac-2019.md)
- [`lazarus-laundering-ofac-2020`](./lazarus-laundering-ofac-2020.md)
- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ff0c8be`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

