# Evidence chain — `eu-dac8-crypto-asset-reporting-directive-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `2079264` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T05:11:38Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Directive (EU) 2023/2226 (DAC8), adopted 2023-10-17,
> transposes the OECD Crypto-Asset Reporting Framework (CARF, 2022)
> into EU law, imposing CARF-aligned tax due diligence and
> transaction-level reporting obligations on EU-operating Reporting
> Crypto-Asset Service Providers (RCASPs). Member-State transposition
> due 2025-12-31; application 2026-01-01; first reporting 2027. As of
> the 2026-05-17 authoring date no observed RCASP-level change has
> materialized — coded null_event / null_case as the EU-level
> metadata-layer companion to MiCA (eu-mica-2023) and TFR Recast
> (eu-tfr-recast-2023), and the EU implementation child of CARF
> (oecd-carf-2022)."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_Council`
- **Timestamp**: `2023-10-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2226>
  - Wayback: <https://web.archive.org/web/20231026054908/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2226>
  - body_hash: `sha256:bc01662c10a49b15b13b6e8db7329a444a981c82acf8a909041f38fe34781437`
  - body_path: `sources/http_captures/eu-dac8-crypto-asset-reporting-directive-2023/primary/web.archive.org__web-20231026054908-https-eur-lex.europa.eu-legal-content-EN-TXT__1c7a18f9b7.html`
  > Council Directive (EU) 2023/2226 of 17 October 2023 amending
> Directive 2011/16/EU on administrative cooperation in the field of
> taxation ("DAC8"). Adopted by the Council of the European Union on
> 2023-10-17 (ECOFIN), published in the Official Journal of the
> European Union on 2023-10-24. DAC8 is the EU-level transposition
> of the OECD Crypto-Asset Reporting Framework (CARF, 2022-10-10) and
> accompanying CRS amendments, extending the EU's automatic exchange
> of information (AEOI) regime to crypto-asset transactions. Imposes
> due diligence and reporting obligations on Reporting Crypto-Asset
> Service Providers (RCASPs) defined consistently with CARF and
> substantively overlapping the MiCA CASP population. Member States
> must transpose by 2025-12-31 and apply provisions from 2026-01-01;
> first reporting cycle 2027-01-01 to 2027-09-30 covering the 2026
> calendar year. Wayback memento 20231026054908 captured 2026-05-21
> with replayable body_hash sha256:bc01662c10a4....
- **`primary_legal`**
  - URL: <https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en>
  - body_hash: `sha256:a208aa5fc193f0c7da597e32ee48fa73d1813b09732e915cd8076ed15a4aeb62`
  - body_path: `sources/http_captures/eu-dac8-crypto-asset-reporting-directive-2023/v0_3_repair/taxation-customs.ec.europa.eu__taxation-tax-transparency-cooperation-administrative-co-operation-and-mutual-assistance-directive-administrative-cooperation-dac-dac8_en__a80d919eb8.html`
  > European Commission DG TAXUD landing page for the DAC8 directive.
> Documents the 2023-10-17 Council adoption date, the 2023-10-24 OJ
> publication, the 2025-12-31 transposition deadline, the
> 2026-01-01 application date, and the 2027 first-reporting window.
> Cross-references CARF (oecd-carf-2022) as the OECD parent
> instrument and confirms RCASP scope alignment with CARF.
> contextual_unarchived per brief.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU-operating Reporting Crypto-Asset Service Providers (DAC8-regulated)

> All EU-operating Reporting Crypto-Asset Service Providers (RCASPs) as
> defined under DAC8 Annex VI, transposing the OECD CARF RCASP
> definition into EU law. The population substantively overlaps the
> MiCA CASP population (Binance EU operations, Coinbase EU, Kraken EU,
> Bitstamp, Bitpanda, and all licensed EU-27 CASPs) plus brokers,
> dealers, and crypto ATM operators captured by CARF's RCASP
> perimeter. Class-level scope: due diligence and transaction-level
> reporting obligations on RCASPs, with no address-level enumeration.
> Self-hosted (non-custodial) wallets remain out of scope at the
> protocol level, but RCASP-intermediated transfers to / from
> self-custody addresses fall within the reporting perimeter when the
> RCASP is the counterparty (same treatment as CARF).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `eu_dac8_directive_adopted_no_observed_rcasp_change_yet`

**Window**: `2023-10-17 00:00:00+00:00` → `2026-05-17 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2226>
  - Wayback: <https://web.archive.org/web/20231026054908/https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2226>
  - body_hash: `sha256:bc01662c10a49b15b13b6e8db7329a444a981c82acf8a909041f38fe34781437`
  - body_path: `sources/http_captures/eu-dac8-crypto-asset-reporting-directive-2023/primary/web.archive.org__web-20231026054908-https-eur-lex.europa.eu-legal-content-EN-TXT__1c7a18f9b7.html`
  > DAC8 adoption 2023-10-17 is a class-level, future-effective
> directive: Member-State transposition deadline 2025-12-31,
> application 2026-01-01, first reporting 2027. As of the
> authoring date (2026-05-17) no class-level RCASP behavior
> change attributable to DAC8 has been observed at the
> offramp_cex layer beyond pre-existing MiCA / TFR Recast
> compliance preparation. observed_no_change with
> attribution=none reflects this null-event posture; revisit
> when 2027 first-cycle reports surface.
- **`primary_legal`**
  - URL: <https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en>
  - body_hash: `sha256:a208aa5fc193f0c7da597e32ee48fa73d1813b09732e915cd8076ed15a4aeb62`
  - body_path: `sources/http_captures/eu-dac8-crypto-asset-reporting-directive-2023/v0_3_repair/taxation-customs.ec.europa.eu__taxation-tax-transparency-cooperation-administrative-co-operation-and-mutual-assistance-directive-administrative-cooperation-dac-dac8_en__a80d919eb8.html`
  > DG TAXUD landing page anchors the adoption / OJ-publication /
> transposition / application / first-reporting calendar. Used
> here as a second replayable pointer for the null-event posture;
> no observed RCASP-level change to date.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`oecd-carf-2022`](./oecd-carf-2022.md)
- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2079264`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

