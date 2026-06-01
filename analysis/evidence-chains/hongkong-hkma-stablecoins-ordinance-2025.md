# Evidence chain — `hongkong-hkma-stablecoins-ordinance-2025`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `fd81985` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The Hong Kong Stablecoins Ordinance (Cap. 656) commenced operation on
> 2025-08-01, establishing the first HKMA-administered licensing regime
> for fiat-referenced stablecoin (FRS) issuers, including extraterritorial
> application to any HKD-referenced stablecoin issuer worldwide.
> Unlicensed issuance carries criminal penalties up to HK$5 million fine
> and 7 years imprisonment. Observational axes at asset_onchain (issuance-
> licensing gate) and offramp_cex (downstream HK-stablecoin fiat-rail
> severance for unlicensed issuers). Admission-anchor promotion pending
> archival anchors (pinned 2026-05-21) for HKMA, HKSAR Government, and HKMA
> implementation-notice URLs plus published HKMA licensing-register
> snapshot."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `HK_HKMA`
- **Timestamp**: `2025-08-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/>
  - Wayback: <https://web.archive.org/web/20250115063707/https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/>
  - body_hash: `sha256:dfe19a0319bb00b19e95b5a23a029e39943e255ab3cb2eb9dd79ef6f892141bd`
  - body_path: `sources/http_captures/hongkong-hkma-stablecoins-ordinance-2025/primary/web.archive.org__web-20250115063707-https-www.hkma.gov.hk-eng-key-functions-international-financial-centre-stablecoin-issuers__e4d660a0cf.html`
  > HKMA Stablecoins Ordinance regulatory regime landing page. The
> Stablecoins Ordinance (Cap. 656) was enacted by the Legislative
> Council (LegCo) of Hong Kong in May 2025 and commenced operation
> on 2025-08-01, establishing the first HKMA-administered licensing
> regime for fiat-referenced stablecoin (FRS) issuers in Hong Kong.
> Any person who, in the course of business, issues a stablecoin in
> Hong Kong or issues a stablecoin that purports to maintain a stable
> value by reference to the Hong Kong dollar (whether in or outside
> Hong Kong) must hold an HKMA-issued licence. Unlicensed issuance
> carries criminal penalties up to HK$5 million fine and 7 years
> imprisonment, plus a daily HK$100,000 continuing-offence fine.
> Wayback wildcard pointer (web/2025/) in lieu of a pinned-timestamp
> snapshot; evidence_use=contextual_unarchived per Phase C DRYRUN
> convention. Pinned archive deferred to follow-up authoring pass.
- **`primary_legal`**
  - URL: <https://www.info.gov.hk/gia/general/202506/06/P2025060600275.htm>
  - Wayback: <https://web.archive.org/web/20250624141341/https://www.info.gov.hk/gia/general/202506/06/P2025060600275.htm>
  - body_hash: `sha256:90f3fdd8696ae240e5f8effd9ae8927d232af48a8a5baf45a7e7eb924b06a892`
  - body_path: `sources/http_captures/hongkong-hkma-stablecoins-ordinance-2025/primary/web.archive.org__web-20250624141341-https-www.info.gov.hk-gia-general-202506-06-P2025060600275.htm__dec4beae1b.html`
  > HKSAR Government press release (2025-06-06) confirming that the
> Stablecoins Ordinance commences operation on 2025-08-01. Companion
> anchor to the HKMA regime landing page. Wayback wildcard pointer
> pinned 2026-05-21.
- **`primary_legal`**
  - URL: <https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/07/20250729-4/>
  - Wayback: <https://web.archive.org/web/20250729123352/https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/07/20250729-4/>
  - body_hash: `sha256:b0e317f3689c605d908d531bb44dd84fe6b21955049a99787255fa27902f3f31`
  - body_path: `sources/http_captures/hongkong-hkma-stablecoins-ordinance-2025/primary/web.archive.org__web-20250729123352-https-www.hkma.gov.hk-eng-news-and-media-press-releases-2025-07-20250729-4__281a2f1531.html`
  > HKMA 2025-07-29 press release on implementation of the regulatory
> regime for stablecoin issuers. Issued days before commencement;
> sets out licence-application transitional window of three months
> for pre-existing issuers, with provisional licences valid through
> 2026-01-31 for applicants demonstrating reasonable prospects of
> meeting the full requirements. Wayback wildcard pointer in lieu of
> pinned body_hash.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: HK-operating + HKD-referenced stablecoin issuer ecosystem (HKMA-licensed)

> All HK-operating fiat-referenced stablecoin (FRS) issuers and all
> issuers globally of stablecoins referencing the Hong Kong dollar
> (HKD-pegged). HKMA-administered licensing regime — sector-wide
> regulation, not address-level enumeration. Affects HK-incorporated
> stablecoin issuer candidates (e.g. Standard Chartered HK / Animoca /
> HKT consortium pilot, JD-HK, RD InnoTech sandbox participants) plus
> any global HKD-referenced stablecoin issuer.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `unlicensed_hk_or_hkd_stablecoin_fiat_rails_blocked`

**Timestamp**: `2025-08-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/>
  - Wayback: <https://web.archive.org/web/20250115063707/https://www.hkma.gov.hk/eng/key-functions/international-financial-centre/stablecoin-issuers/>
  - body_hash: `sha256:dfe19a0319bb00b19e95b5a23a029e39943e255ab3cb2eb9dd79ef6f892141bd`
  - body_path: `sources/http_captures/hongkong-hkma-stablecoins-ordinance-2025/primary/web.archive.org__web-20250115063707-https-www.hkma.gov.hk-eng-key-functions-international-financial-centre-stablecoin-issuers__e4d660a0cf.html`
  > HKMA stablecoin-issuers page anchors the licensing regime
> constraining unlicensed HK/HKD stablecoin fiat-rail
> integration. Wayback memento 20250115063707.
- **`primary_legal`**
  - URL: <https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/07/20250729-4/>
  - Wayback: <https://web.archive.org/web/20250729123352/https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/07/20250729-4/>
  - body_hash: `sha256:b0e317f3689c605d908d531bb44dd84fe6b21955049a99787255fa27902f3f31`
  - body_path: `sources/http_captures/hongkong-hkma-stablecoins-ordinance-2025/primary/web.archive.org__web-20250729123352-https-www.hkma.gov.hk-eng-news-and-media-press-releases-2025-07-20250729-4__281a2f1531.html`
  > Downstream HK-stablecoin fiat-rail consequence: HK CEXs and
> payment rails cannot integrate unlicensed HK-issued or HKD-
> referenced stablecoins after 2025-08-01 without exposing
> themselves to aiding-and-abetting liability under the
> Stablecoins Ordinance. Attribution=plausible because the
> regulatory anchor is documented but no archived exchange
> corporate notice has been pinned in this session. Wayback
> wildcard pointer in lieu of pinned body_hash.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`hongkong-sfc-vatp-licensing-2023-06`](./hongkong-sfc-vatp-licensing-2023-06.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `fd81985`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

