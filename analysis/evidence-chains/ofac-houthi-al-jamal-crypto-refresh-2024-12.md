# Evidence chain — `ofac-houthi-al-jamal-crypto-refresh-2024-12`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `89285c6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The December 2024 OFAC SDN refresh of the Sa'id al-Jamal
> IRGC-QF-backed Houthi financial-facilitation network appended
> five TRON-based USDT wallet addresses to the al-Jamal SDN
> entries, with plausibly-attributed Tether USDT-TRC20 issuer
> freezes on the designated addresses (asset-layer cascade), and
> no public CEX policy-statement cascade documented in the 14-day
> post-designation window."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-12-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2757>
  - Wayback: <https://web.archive.org/web/20241219215403/https://home.treasury.gov/news/press-releases/jy2757>
  - body_hash: `sha256:89f027f4982d73898e5bda195f2ecfad965196ef595a110d5e4ea3bffaef6ff8`
  - body_path: `sources/http_captures/ofac-houthi-al-jamal-crypto-refresh-2024-12/primary/web.archive.org__web-20241219215403-https-home.treasury.gov-news-press-releases-jy2757__e58f48c10f.html`
  > Treasury press release JY2757 "Treasury Maintains Pressure on
> Houthi Procurement and Financing Schemes" (2024-12-19). OFAC
> SDN refresh expanding the Sa'id al-Jamal (IRGC-QF-backed
> Houthi financial official) network designations. v0.3 audit
> 2026-05-20 (c) Batch C-1: Wayback memento 20241219215403
> pinned (29873 bytes per CDX). Draft date 2024-12-17 CORRECTED
> to 2024-12-19 per Treasury press release + OFAC RA dates.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20241219>
  - Wayback: <https://web.archive.org/web/20241219172200/https://ofac.treasury.gov/recent-actions/20241219>
  - body_hash: `sha256:854df3a431a4b9e60578ab59f0ab91780a537b62dddc1510d8c9e98c79223d80`
  - body_path: `sources/http_captures/ofac-houthi-al-jamal-crypto-refresh-2024-12/primary/web.archive.org__web-20241219172200-https-ofac.treasury.gov-recent-actions-20241219__75f7c6f617.html`
  > OFAC Recent Actions page for 2024-12-19 listing the al-Jamal
> SDN refresh. v0.3 audit 2026-05-20 (c) Batch C-1: Wayback
> memento 20241219172200 pinned (68064 bytes). Direct grep
> confirms al-Jamal SDN entry with KHRPI alias addition + 5
> USDT TRC-20 addresses (TLNRT524dzL5FF1nJHDhYEMFpeWjLjRbz1 +
> THh5woR8qfmDsNknQ3agPYzQSiRtMnKsTh + TV5ZTpKDszLTF6XcMnPongS33pwBgF91by +
> TTAHMdqoom4f2VTWniroPWQHcTRZ4caoH4 + TFFvv7NAWmbcVfA7QN81mMvUC25TWj1WJx)
> + 7xSa'id + 7xJAMAL + 5xHAZMI + 2xAL THAWR + 1xjy2757. Co-
> designated entities: AL HAZMI EXCHANGE, MOHAMMED ALI AL THAWR
> EXCHANGE, BLU SHIPPING M SDN. BHD., MERKUR ENERGY PORT
> SERVICES, TEFCAS MARINE — all linked to AL-JAMAL Sa'id Ahmad
> Muhammad.
- **`supporting_tracker`**
  - URL: <https://www.chainalysis.com/blog/ofac-highlights-hundreds-of-millions-of-dollars-in-cryptocurrency-transactions-related-to-irgc-connected-houthi-financier-said-al-jamal/>
  - Wayback: <https://web.archive.org/web/2024/https://www.chainalysis.com/blog/ofac-highlights-hundreds-of-millions-of-dollars-in-cryptocurrency-transactions-related-to-irgc-connected-houthi-financier-said-al-jamal/>
  > Chainalysis post-action analysis tracing the al-Jamal-linked
> TRON / USDT wallet cluster referenced by the SDN refresh.
> Wayback pinning deferred to follow-up enrichment.
- **`supporting_tracker`**
  - URL: <https://www.trmlabs.com/resources/blog/us-treasury-sanctions-houthi-financial-networks-including-eight-crypto-addresses>
  - Wayback: <https://web.archive.org/web/2024/https://www.trmlabs.com/resources/blog/us-treasury-sanctions-houthi-financial-networks-including-eight-crypto-addresses>
  > TRM Labs post-action analysis of the December 2024 Houthi
> financial-network refresh. Title cites "eight crypto addresses"
> — possibly counts the 5 al-Jamal USDT addresses + additional
> addresses from broader Houthi financial-network co-
> designations. Wayback pinning deferred to follow-up enrichment.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Protocol**: `al_jamal_houthi_irgc_qf_network`
- **Actor name**: Sa'id al-Jamal Houthi / IRGC-QF financial-facilitation network
- **Chains**: `tron`
- **Addresses**: 5 total (enumerated in event YAML)

> Entity-level designation refresh of the Sa'id al-Jamal IRGC-QF-backed
> Houthi financial-facilitation network. The 2024-12-19 action appends
> 5 TRON-based USDT wallet addresses to the al-Jamal individual SDN
> entry + adds new MSB nodes (AL HAZMI EXCHANGE, MOHAMMED ALI AL THAWR
> EXCHANGE). Co-designated maritime entities (BLU SHIPPING, MERKUR
> ENERGY PORT, TEFCAS MARINE) extend the Houthi/IRGC-QF logistics
> sanctions but are not direct crypto-target entities. v0.3 audit
> 2026-05-20 (c) Batch C-1: enumeration upgraded subset->complete,
> 5 al-Jamal USDT TRC-20 addresses extracted verbatim from OFAC RA
> 2024-12-19 Wayback memento.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-12-19 00:00:00+00:00` → `2024-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2757>
  - Wayback: <https://web.archive.org/web/20241219215403/https://home.treasury.gov/news/press-releases/jy2757>
  - body_hash: `sha256:89f027f4982d73898e5bda195f2ecfad965196ef595a110d5e4ea3bffaef6ff8`
  - body_path: `sources/http_captures/ofac-houthi-al-jamal-crypto-refresh-2024-12/primary/web.archive.org__web-20241219215403-https-home.treasury.gov-news-press-releases-jy2757__e58f48c10f.html`
  > v0.3 audit 2026-05-20 (c) Batch C-1: observation row promoted
> to admitted state. Treasury jy2757 + OFAC RA 20241219 serve
> as admission-grade denominator anchors for the trigger event
> (SDN refresh + 5 USDT-TRC20 address enumeration); absence of
> fresh public CEX policy statement explicitly citing the
> al-Jamal SDN entries in the 14d post-event window is the null
> finding (industry preference for private chain-analytics
> KYT-flag workflows over public per-wallet disclosure, same
> pattern as sim-hyon-sop / hamas-buy-cash / hamas-gaza-now).
> Original draft's asset_onchain observation row
> (tether_usdt_tron_freezes_on_al_jamal_designated_wallets,
> attribution=plausible) REMOVED at promotion: validator
> requires primary_onchain for asset_onchain observed_change.
> Per-address Tronscan freeze-tx evidence deferred to follow-up.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Refresh identifies 5 TRON-based USDT wallets appended to the

## 7. Related events

- [`ofac-hamas-buy-cash-msb-2023-10`](./ofac-hamas-buy-cash-msb-2023-10.md)
- `ofac-hamas-irgc-virtual-currency-network-2024-01` (rejected; no rendered admitted-chain link)
- [`ofac-hamas-gaza-now-2024-03`](./ofac-hamas-gaza-now-2024-03.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `89285c6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

