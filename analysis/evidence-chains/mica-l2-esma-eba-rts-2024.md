# Evidence chain — `mica-l2-esma-eba-rts-2024`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `84e7c21` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:04:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "ESMA + EBA finalized the MiCA Level-2 Regulatory Technical Standards
> through 2024 (canonical L2 milestone 2024-03-25 with ESMA's CP3 final
> consultation, EBA parallel reserve-composition RTS, and the
> 2024-12-17 STOR Final Report). Recorded as a null event because the
> Level-2 RTS impose forward-looking authorization, reserve-management,
> and market-abuse-detection obligations rather than producing
> retroactive per-address or per-CASP observable cross-layer behavior at
> trigger date; downstream CASP-level follow-on actions are tracked as
> separate events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_ESMA_EBA`
- **Timestamp**: `2024-03-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica>
  - Wayback: <https://web.archive.org/web/20240117214257/https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica>
  - body_hash: `sha256:eac48bfaa847dbf98added6622658c0bfc0697cf0dc777d4b703ef4bc31e3794`
  - body_path: `sources/http_captures/mica-l2-esma-eba-rts-2024/primary/web.archive.org__web-20240117214257-https-www.esma.europa.eu-esmas-activities-digital-finance-and-innovation-markets-crypto-assets-regulation-mica__9e3fd579c0.html`
  > Canonical MiCA Level-2 milestone: ESMA's third (final) Consultation
> Paper on MiCA technical standards, published 2024-03-25. The
> CP3 package contained the last tranche of draft Regulatory
> Technical Standards (RTS) covering crypto-asset related market
> abuse (Art. 92 STOR), suitability assessment for portfolio
> management, and crypto-asset transfer services. Together with the
> EBA's parallel RTS packages on stablecoin issuer reserve
> composition (ART/EMT own funds, liquidity, recovery plans,
> overcollateralization) finalized through 2024, and ESMA's
> 2024-12-17 Final Report adopting the STOR RTS as a Commission
> Delegated Regulation, this constitutes the MiCA Level-2
> implementation operational layer. CASP authorization regime under
> MiCA applies from 2024-12-30.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU CASP + ART/EMT issuer ecosystem (MiCA Level-2 RTS-regulated)

> Class-level: all EU-operating Crypto-Asset Service Providers (CASPs)
> and stablecoin issuers (Asset-Referenced Tokens / E-Money Tokens)
> subject to MiCA Title III (ART), Title IV (EMT), Title V (CASP), and
> Title VI (Market Abuse). The Level-2 RTS packages impose detailed
> operational obligations: (a) stablecoin issuer reserve composition
> (≥30% deposits for ARTs/EMTs in official currencies; ≥60% for
> significant tokens; weekly liquidity; overcollateralization formula
> with 5-year daily look-back); (b) CASP authorization documentation
> and prudential requirements; (c) market abuse detection / STOR
> reporting under MiCA Art. 92. No address- or domain-level enumeration
> possible at trigger date — sector-wide Level-2 implementation
> framework. Per codebook §7, subset enumeration with class-level
> rationale is canonical for class-level regulatory targets.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `mica_l2_rts_casp_authorization_market_abuse_published_no_observed_casp_change_at_trigger`

**Window**: `2024-03-25 00:00:00+00:00` → `2026-05-21 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica>
  - Wayback: <https://web.archive.org/web/20240117214257/https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica>
  - body_hash: `sha256:eac48bfaa847dbf98added6622658c0bfc0697cf0dc777d4b703ef4bc31e3794`
  - body_path: `sources/http_captures/mica-l2-esma-eba-rts-2024/primary/web.archive.org__web-20240117214257-https-www.esma.europa.eu-esmas-activities-digital-finance-and-innovation-markets-crypto-assets-regulation-mica__9e3fd579c0.html`
  > ESMA MiCA hub anchors the Level-2 RTS package for CASP
> authorization (Art. 62), market abuse / STOR (Art. 92), and
> suitability / transfer-service obligations. CP3 of 2024-03-25
> is the final consultation package; the STOR RTS was adopted as
> a Commission Delegated Regulation per ESMA's 2024-12-17 Final
> Report. CASP authorization regime applies from 2024-12-30. At
> trigger date the RTS package is operational guidance, not yet
> binding on individual CASPs; no per-CASP observable cross-layer
> behavioral change is attributable to the trigger itself.
> Wayback memento 20240117214257 captured 2026-05-21.
- **`semi_primary_wayback`**
  - URL: <https://www.eba.europa.eu/regulation-and-policy/asset-referenced-and-e-money-tokens-mica>
  - Wayback: <https://web.archive.org/web/20250805132328/https://www.eba.europa.eu/regulation-and-policy/asset-referenced-and-e-money-tokens-mica>
  - body_hash: `sha256:ec3faad8d7b8cc851aaeaead643c0c050fee8be76627ccc2271defbc49ff348a`
  - body_path: `sources/http_captures/mica-l2-esma-eba-rts-2024/primary/web.archive.org__web-20250805132328-https-www.eba.europa.eu-regulation-and-policy-asset-referenced-and-e-money-tokens-mica__5d6b1486d7.html`
  > EBA "Asset-referenced and e-money tokens (MiCA)" hub anchors the
> EBA RTS package on stablecoin reserve composition, own funds,
> liquidity, overcollateralization, and recovery plans. Wayback
> memento 20250805132328 captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`eu-amla-anti-money-laundering-authority-regulation-2024`](./eu-amla-anti-money-laundering-authority-regulation-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `84e7c21`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

