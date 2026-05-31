# Evidence chain — `fatf-targeted-update-va-vasp-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c86ca57` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FATF's 2023-06-27 'Virtual Assets: Targeted Update on
> Implementation of the FATF Standards on VAs and VASPs' is the
> third major FATF update post-R.15 (2019) and post-2021 Targeted
> Update, documenting that 75% of evaluated jurisdictions are only
> partially or not compliant with R.15/INR.15 and that >50% of 151
> surveyed jurisdictions had taken no Travel Rule implementation
> steps. Coded as null_event / null_case at the corpus's
> resolution: no per-event observed_change cascade is directly
> attributable to the 2023-06-27 publication date; downstream
> member-state implementations (EU TFR 2023, national VASP rule
> updates) are tracked as separate child events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `FATF`
- **Timestamp**: `2023-06-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-update-virtual-assets-vasps-2023.html>
  - Wayback: <https://web.archive.org/web/2023*/https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-update-virtual-assets-vasps-2023.html>
  > FATF "Virtual Assets: Targeted Update on Implementation of the
> FATF Standards on VAs and VASPs" published 2023-06-27. Third
> major FATF update on virtual assets post-R.15 2019 and post the
> 2021-10-28 Updated Guidance. Headline finding: based on 98 FATF
> mutual evaluation / follow-up reports, 75% of jurisdictions are
> only partially or not compliant with R.15/INR.15; more than half
> of the 151 jurisdictions that responded to FATF's 2023 survey
> had taken no steps toward implementing the Travel Rule. The
> update also reviews emerging risks (DeFi, P2P, NFTs, unhosted
> wallets, stablecoins) and references the February 2023 FATF
> roadmap to improve R.15 implementation, with a follow-up review
> committed for June 2024.
- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/June2023-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf>
  - body_hash: `sha256:7b18b74c5c292990ec5192179042391880f852f46778c590a6fb0b28ffe79e6b`
  - body_path: `sources/http_captures/fatf-targeted-update-va-vasp-2023/primary/www.fatf-gafi.org__content-dam-fatf-gafi-guidance-June2023-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf__aaf79c8ed7.bin`
  > Full PDF of the June 2023 Targeted Update. Live fatf-gafi.org
> capture 2026-05-21 (no Wayback memento accessible; live PDF
> canonical, 1.24MB).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: FATF-jurisdiction VASP / DeFi / stablecoin ecosystem

> Class-level Travel Rule / R.15 implementation review at the FATF
> member-state VASP layer. Per §7 codebook, class-level regulatory
> updates are encoded as enumeration=subset with the class-level
> rationale documented here. No address-level enumeration; binding
> force is via member-state implementation (mutual evaluation +
> grey-listing pressure). Downstream affected entities include
> centralized exchanges, custodians, stablecoin issuers, and any
> DeFi / NFT / P2P facilitator within the FATF functional-test
> perimeter (control or sufficient influence over a VA arrangement).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `fatf_2023_targeted_update_r15_implementation_review`

**Window**: `2023-06-27 00:00:00+00:00` → `2024-06-30 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/guidance/June2023-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf>
  - body_hash: `sha256:7b18b74c5c292990ec5192179042391880f852f46778c590a6fb0b28ffe79e6b`
  - body_path: `sources/http_captures/fatf-targeted-update-va-vasp-2023/primary/www.fatf-gafi.org__content-dam-fatf-gafi-guidance-June2023-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf__aaf79c8ed7.bin`
  > FATF 2023-06-27 Targeted Update PDF — class-level R.15 /
> Travel Rule implementation-lag review (DeFi, P2P, NFTs,
> unhosted wallets, stablecoins). No per-event observed_change
> cascade attributable at the corpus's resolution; downstream
> effects manifest via national implementations tracked as
> separate child events. Live fatf-gafi.org PDF captured
> 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`fatf-targeted-update-va-vasp-2021`](./fatf-targeted-update-va-vasp-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c86ca57`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

