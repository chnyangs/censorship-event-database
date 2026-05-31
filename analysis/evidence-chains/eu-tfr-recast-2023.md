# Evidence chain — `eu-tfr-recast-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `c87d162` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:17:25Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Regulation 2023/1113 (TFR Recast), adopted 2023-05-31 alongside
> MiCA, establishes a zero-de-minimis Travel Rule for all CASP-to-CASP
> crypto-asset transfers in the EU-27 — the supranational implementation
> of FATF Recommendation 15 (2019) and a metadata-layer companion to
> MiCA's licensing framework. Effective 2024-12-30. Represents a
> supranational regulatory-framework trigger at the offramp_cex layer
> distinct from sanction-style enforcement; downstream CASP-specific
> compliance actions are expected as follow-on events."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_Council`
- **Timestamp**: `2023-05-31 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - Wayback: <https://web.archive.org/web/20260516000000/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - body_hash: `sha256:6d2fde2549fcf25aca4602a9c693eec1589740e5a83f0cb26d303c7ec90c064e`
  - body_path: `sources/http_captures/eu-tfr-recast-2023/v0_3_repair/eur-lex.europa.eu__legal-content-EN-TXT__90a91a2c77.html`
  > Regulation (EU) 2023/1113 of the European Parliament and of the
> Council of 31 May 2023 on information accompanying transfers of funds
> and certain crypto-assets (the "Transfer of Funds Regulation Recast"
> / "TFR Recast" / EU Travel Rule companion to MiCA). Extends the
> existing TFR (2015/847) to cover crypto-asset transfers between
> Crypto-Asset Service Providers (CASPs) at a zero de-minimis
> threshold: originator + beneficiary information must accompany every
> CASP-to-CASP crypto-asset transfer regardless of amount. Direct
> supranational implementation of FATF Recommendation 15 (2019) for
> the EU-27 bloc; sibling instrument to MiCA (Regulation 2023/1114)
> adopted on the same day. Effective application date 2024-12-30,
> aligned with MiCA CASP licensing phase. DRYRUN wayback stub;
> replace with a verified capture + body_hash / body_path during real
> human audit.
- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - body_hash: `sha256:6d2fde2549fcf25aca4602a9c693eec1589740e5a83f0cb26d303c7ec90c064e`
  - body_path: `sources/http_captures/eu-tfr-recast-2023/v0_3_repair/eur-lex.europa.eu__legal-content-EN-TXT__90a91a2c77.html`
  > Second citation pointer to the EUR-Lex CELEX:32023R1113 record per
> brief instruction (evidence_use: contextual_unarchived). Documents
> TFR Recast articles on originator/beneficiary info (Art. 14),
> verification duties on CASPs (Arts. 16–17), and missing-info
> procedures (Arts. 19–21). Zero-threshold distinguishes the EU
> regime from FATF's recommended de-minimis (USD/EUR 1,000) and from
> national implementations like KR FSC's KRW 1M threshold.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU-operating Crypto-Asset Service Providers (TFR-Recast-regulated)

> All EU-operating Crypto-Asset Service Providers (CASPs) — the same
> population regulated by MiCA Title V. TFR Recast obliges originating
> CASPs to collect, verify, and transmit originator + beneficiary
> information for every crypto-asset transfer between CASPs, regardless
> of transfer amount (zero de-minimis). Beneficiary CASPs are obliged to
> receive, verify, and act on missing-information cases. Sector-wide
> rather than address-enumerable; covers Binance EU operations, Coinbase
> EU, Kraken EU, Bitstamp, and all licensed EU-27 CASPs as of the
> 2024-12-30 application date.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_tfr_recast_adopted_zero_threshold_travel_rule_for_casps`

**Timestamp**: `2023-05-31 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - Wayback: <https://web.archive.org/web/20260516000000/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - body_hash: `sha256:6d2fde2549fcf25aca4602a9c693eec1589740e5a83f0cb26d303c7ec90c064e`
  - body_path: `sources/http_captures/eu-tfr-recast-2023/v0_3_repair/eur-lex.europa.eu__legal-content-EN-TXT__90a91a2c77.html`
  > Regulation (EU) 2023/1113 — the TFR Recast — adopted by the
> European Parliament and Council on 2023-05-31, published in the
> EU Official Journal on 2023-06-09, with phased application
> culminating 2024-12-30 (aligned with the MiCA CASP licensing
> regime). Imposes a zero-de-minimis Travel Rule on all
> CASP-to-CASP crypto-asset transfers in the EU: originating CASPs
> must collect and transmit originator + beneficiary information
> regardless of transfer amount. Direct supranational
> implementation of FATF Recommendation 15 (2019) at the EU-27
> level. attribution=direct because the regulation itself is the
> primary legal instrument mandating the behavior of EU-operating
> CASPs. DRYRUN wayback stub; replace with a verified capture
> during real human audit.
- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - Wayback: <https://web.archive.org/web/20260516000001/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R1113>
  - body_hash: `sha256:6d2fde2549fcf25aca4602a9c693eec1589740e5a83f0cb26d303c7ec90c064e`
  - body_path: `sources/http_captures/eu-tfr-recast-2023/v0_3_repair/eur-lex.europa.eu__legal-content-EN-TXT__90a91a2c77.html`
  > Second anchor to the EUR-Lex CELEX:32023R1113 record. Cross-reference
> for the zero-threshold provision (Art. 14) and the missing-info
> procedure (Arts. 19–21) — the structural features that
> distinguish TFR Recast from the FATF R.15 (2019) recommended
> de-minimis and from national implementations such as the KR FSC
> Travel Rule (KRW 1M ≈ USD 750 threshold). The brief specified
> evidence_use=contextual_unarchived for the EUR-Lex citation; per
> dataset convention (cf. sinbad-doj-2024) contextual_unarchived is
> only valid on trigger.citation, not on observation.sources, so a
> DRYRUN wayback stub is used here and the contextual_unarchived
> pointer is retained on trigger.citation. Replace with a verified
> capture + body_hash / body_path during real human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c87d162`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

