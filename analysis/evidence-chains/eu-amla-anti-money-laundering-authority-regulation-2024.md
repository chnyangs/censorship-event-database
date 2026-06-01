# Evidence chain — `eu-amla-anti-money-laundering-authority-regulation-2024`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `9449371` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Council adoption of EU Regulation 2024/1620 on 2024-05-30 established
> AMLA (HQ Frankfurt) as the EU-level AML/CFT supervisor, including
> future direct supervision of high-risk cross-border CASPs. Recorded as
> a null event because the supervisory regime is future-effective (CASP
> direct supervision from 2028-01-01) and produces no observable
> cross-layer behavior at trigger date."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `EU_COUNCIL`
- **Timestamp**: `2024-05-30 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1620/oj>
  - Wayback: <https://web.archive.org/web/20240619005806/https://eur-lex.europa.eu/eli/reg/2024/1620/oj>
  - body_hash: `sha256:7415f1b126df20a7e74bdc384f6fcd346b26487718061d4a40f1a16f9c327d78`
  - body_path: `sources/http_captures/eu-amla-anti-money-laundering-authority-regulation-2024/primary/web.archive.org__web-20240619005806-https-eur-lex.europa.eu-eli-reg-2024-1620-oj__aa38b2fd66.html`
  > Regulation (EU) 2024/1620 of the European Parliament and of the
> Council of 31 May 2024 establishing the Authority for Anti-Money
> Laundering and Countering the Financing of Terrorism (AMLA).
> Approved by the European Parliament on 2024-04-24 and adopted by
> the Council on 2024-05-30; published in the Official Journal of
> the European Union on 2024-06-19. AMLA seat: Frankfurt am Main,
> Germany. AMLA begins operations 2025-07-01; direct supervision of
> selected high-risk obliged entities (including high-risk Crypto-
> Asset Service Providers / CASPs operating cross-border in ≥6
> Member States) is scheduled to begin 2028-01-01 (the original
> political agreement referenced 2027 start; the final regulation
> sets first selection in 2027 with direct supervision from 2028).
> This event records the supranational regulatory trigger; no
> observed cross-layer behavior is admissible at trigger time
> because the supervisory regime is future-effective.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: EU AMLA-supervised high-risk CASP cohort (future-effective)

> Class-level: high-risk Crypto-Asset Service Providers (CASPs) operating
> cross-border in the EU that will fall under AMLA's direct supervision
> once the selection process completes (first selection scheduled 2027;
> direct supervision from 2028-01-01). Per Reg (EU) 2024/1620 selection
> criteria, AMLA will directly supervise approximately 40 of the highest-
> risk obliged entities EU-wide, of which a subset are CASPs. No address-
> or domain-level enumeration possible at trigger date; this is sector-
> wide supranational supervisory architecture. Per codebook §7, subset
> enumeration with class-level rationale (high-risk cross-border CASPs)
> is the canonical coding for class-level regulatory targets.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `amla_regulation_adopted_supervisory_regime_future_effective_no_observed_casp_change_at_trigger`

**Window**: `2024-05-30 00:00:00+00:00` → `2026-05-17 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2024/1620/oj>
  - Wayback: <https://web.archive.org/web/20240619005806/https://eur-lex.europa.eu/eli/reg/2024/1620/oj>
  - body_hash: `sha256:7415f1b126df20a7e74bdc384f6fcd346b26487718061d4a40f1a16f9c327d78`
  - body_path: `sources/http_captures/eu-amla-anti-money-laundering-authority-regulation-2024/primary/web.archive.org__web-20240619005806-https-eur-lex.europa.eu-eli-reg-2024-1620-oj__aa38b2fd66.html`
  > Council adoption of Reg (EU) 2024/1620 on 2024-05-30 creates the
> supervisory authority and selection framework but does not yet
> impose direct supervision. AMLA operational from 2025-07-01;
> direct CASP supervision from 2028-01-01. No CASP-level
> observable change at trigger date; null_event coding per codebook
> §3 (0 observed_change layers). Wayback memento 20240619005806
> captured 2026-05-21.
- **`primary_legal`**
  - URL: <https://www.amla.europa.eu/about-amla_en>
  - Wayback: <https://web.archive.org/web/2024/https://www.amla.europa.eu/about-amla_en>
  > AMLA "About" page anchors the Frankfurt am Main seat, 2025-07-01
> operational start, and the 2028 direct-supervision phase-in.
> Retained as contextual_unarchived (CDX prefix-match returns
> empty for amla.europa.eu); primary anchoring lives on the
> EUR-Lex Regulation 2024/1620 source above.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)
- [`eu-dac8-crypto-asset-reporting-directive-2023`](./eu-dac8-crypto-asset-reporting-directive-2023.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9449371`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

