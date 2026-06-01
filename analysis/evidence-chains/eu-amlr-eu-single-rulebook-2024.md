# Evidence chain — `eu-amlr-eu-single-rulebook-2024`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a7b40fe` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Regulation 2024/1624 (AMLR — Anti-Money Laundering Regulation /
> single rulebook), adopted 2024-05-30 alongside AMLA Regulation
> 2024/1620, replaces the patchwork of national AMLD transpositions with a
> directly-applicable EU regulation and brings CASPs into the EU AML
> obliged-entities perimeter at the regulation level. Crypto-specific
> provisions: EUR 1,000 occasional-/non-customer-transaction CDD threshold
> (Art. 19) and ban on anonymous CASP-hosted accounts and anonymity-
> enhancing instruments (Art. 79). General application 2027-07-10.
> null_event in this corpus: the regulatory trigger is registered but the
> application date is future-effective, so no downstream CASP behavioral
> change at the offramp_cex layer is yet observable."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_Council`
- **Timestamp**: `2024-05-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng>
  - body_hash: `sha256:395cad79d5aefd3b5fd5e3c69d3da304ef235700ac46adcacc4f48315198322b`
  - body_path: `sources/http_captures/eu-amlr-eu-single-rulebook-2024/v0_3_repair/eur-lex.europa.eu__eli-reg-2024-1624-oj-eng__9feffed64b.html`
  > Regulation (EU) 2024/1624 of the European Parliament and of the
> Council of 31 May 2024 on the prevention of the use of the financial
> system for the purposes of money laundering or terrorist financing
> (the "AMLR" / EU AML single rulebook). Formally adopted by the
> European Parliament and Council on 2024-05-30, signed on 2024-05-31,
> published in the EU Official Journal on 2024-06-19, entered into
> force 2024-07-09, with general application date 2027-07-10. Replaces
> the patchwork of national AML transpositions of the prior AMLD
> directives with a single, directly-applicable EU regulation. Crypto-
> specific provisions include: (1) class-level AML/CFT obligations on
> Crypto-Asset Service Providers (CASPs) as obliged entities; (2) a
> EUR 1,000 occasional-transaction / non-customer threshold for
> enhanced CDD by CASPs (Art. 19); (3) a prohibition on anonymous
> CASP-hosted accounts and anonymity-enhancing CASP-issued instruments
> (Art. 79); and (4) restrictions on CASP relationships with
> non-custodial / self-hosted wallets in defined scenarios. Sibling
> instrument to AMLA Regulation (EU) 2024/1620 adopted the same day —
> cross-reference for the supervisory architecture. Live eur-lex
> capture pre-pinned in v0_3_repair/; replayable body_hash
> sha256:395cad79d5aefd3b... attached.
- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng>
  - body_hash: `sha256:395cad79d5aefd3b5fd5e3c69d3da304ef235700ac46adcacc4f48315198322b`
  - body_path: `sources/http_captures/eu-amlr-eu-single-rulebook-2024/v0_3_repair/eur-lex.europa.eu__eli-reg-2024-1624-oj-eng__9feffed64b.html`
  > Second pointer to the EUR-Lex CELEX:32024R1624 record (AMLR), per
> brief instruction to use evidence_use=contextual_unarchived for this
> future-effective regulation. Documents the Article 19 EUR 1,000
> occasional-/non-customer-transaction threshold for CASPs and the
> Article 79 ban on anonymous CASP accounts and anonymity-enhancing
> instruments. AMLR is one of three legs of the EU AML package
> (AMLR + AMLD6 + AMLA Regulation 2024/1620); together with the
> TFR Recast (2023/1113) and MiCA (2023/1114) it forms the EU's
> post-2024 crypto AML/CFT architecture. Live eur-lex.europa.eu
> capture pre-pinned in v0_3_repair/.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU-operating Crypto-Asset Service Providers (AMLR-regulated)

> All EU-operating Crypto-Asset Service Providers (CASPs) as defined under
> MiCA Title V — the same class-level cohort covered by the TFR Recast
> (Regulation 2023/1113). AMLR adds CASPs to the EU AML/CFT "obliged
> entities" perimeter at the regulation level (no longer at the
> member-state directive-transposition level), and layers class-level
> obligations: enhanced CDD over the EUR 1,000 occasional-transaction
> threshold (Art. 19); ban on anonymous CASP accounts and anonymity-
> enhancing CASP-issued instruments (Art. 79); restrictions on CASP
> relationships with self-hosted wallets in defined scenarios. Covers
> Binance EU operations, Coinbase EU, Kraken EU, Bitstamp, and all
> licensed EU-27 CASPs as of the 2027-07-10 application date. Sector-wide
> rather than address-enumerable.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `eu_amlr_single_rulebook_adopted_future_effective_2027`

**Window**: `2024-05-30 00:00:00+00:00` → `2026-05-17 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng>
  - body_hash: `sha256:395cad79d5aefd3b5fd5e3c69d3da304ef235700ac46adcacc4f48315198322b`
  - body_path: `sources/http_captures/eu-amlr-eu-single-rulebook-2024/v0_3_repair/eur-lex.europa.eu__eli-reg-2024-1624-oj-eng__9feffed64b.html`
  > Regulation (EU) 2024/1624 — the AMLR / EU AML single rulebook —
> adopted by the European Parliament and Council on 2024-05-30,
> published in the EU Official Journal on 2024-06-19, with general
> application 2027-07-10. AMLR replaces the patchwork of national
> AML transpositions of the prior AMLD directives with a directly-
> applicable EU regulation, and brings CASPs into the EU AML/CFT
> "obliged entities" perimeter at the regulation level with
> class-level obligations: enhanced CDD over the EUR 1,000
> occasional-/non-customer-transaction threshold (Art. 19); ban on
> anonymous CASP-hosted accounts and anonymity-enhancing CASP-issued
> instruments (Art. 79); restrictions on CASP relationships with
> self-hosted wallets in defined scenarios. Sibling instrument to
> AMLA Regulation (EU) 2024/1620 (anti-money-laundering authority)
> adopted the same day, which establishes the supervisory body that
> will directly supervise selected high-risk CASPs across the
> EU-27. observation_kind=observed_no_change with attribution=none
> because the application date (2027-07-10) is in the future
> relative to this dataset snapshot — the regulatory trigger is
> registered but no downstream CASP behavioral change at the
> offramp layer can yet be observed. Live eur-lex capture
> pre-pinned in v0_3_repair/ with replayable body_hash.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)
- [`eu-dac8-crypto-asset-reporting-directive-2023`](./eu-dac8-crypto-asset-reporting-directive-2023.md)
- [`eu-amla-anti-money-laundering-authority-regulation-2024`](./eu-amla-anti-money-laundering-authority-regulation-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a7b40fe`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

