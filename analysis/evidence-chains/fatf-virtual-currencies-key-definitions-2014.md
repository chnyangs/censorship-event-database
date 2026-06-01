# Evidence chain — `fatf-virtual-currencies-key-definitions-2014`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c736a32` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The FATF 2014-06-26 report "Virtual Currencies — Key Definitions
> and Potential AML/CFT Risks" introduced a shared FATF-level
> taxonomy ("exchanger", "administrator", "convertible / non-
> convertible VC", "centralised / decentralised VC") and a
> preliminary risk-framing for AML/CFT exposures of virtual
> currency activity, establishing the foundational supranational
> predicate guidance for the five-year regulatory development arc
> culminating in the 2019-06-21 FATF R.15 INR Travel Rule
> extension to VASPs (fatf-r15-vasp-travel-rule-2019). The 2014
> report does not itself impose binding VASP obligations;
> observation_kind=observed_no_change with attribution=plausible
> at the supranational standard-setting axis honestly represents
> the dispersed pre-regime predicate role. Historical-baseline
> tier; not used in main statistical denominators.

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `FATF`
- **Timestamp**: `2014-06-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-currency-key-definitions-and-potential-aml-cft-risks.pdf>
  - body_hash: `sha256:c2aed2a0bb4233b1f743110618ed5e4d530ef74483a187c7d76fd1a530215c2e`
  - body_path: `sources/http_captures/fatf-virtual-currencies-key-definitions-2014/primary/www.fatf-gafi.org__content-dam-fatf-gafi-reports-Virtual-currency-key-definitions-and-potential-aml-cft-risks.pdf__40c190be0a.bin`
  > FATF report "Virtual Currencies — Key Definitions and Potential
> AML/CFT Risks," published 2014-06-26 by the Financial Action Task
> Force (FATF) plenary in Paris. The report is the first FATF
> instrument to engage virtual currencies (VC) substantively at
> the supranational standard-setting layer. It establishes a
> shared taxonomy ("virtual currency", "convertible / non-
> convertible VC", "centralised / decentralised VC", "exchanger",
> "administrator", "user", "miner") and a preliminary risk
> assessment of money-laundering and terrorist-financing exposures
> associated with virtual currency activity. The report is non-
> binding guidance — it does not amend the FATF Recommendations
> and does not impose Travel Rule or VASP obligations — but it
> establishes the conceptual scaffolding ("exchanger" as the
> regulatory locus, convertibility as the risk axis) that anchors
> the subsequent five-year regulatory development arc:
> (a) the 2015-06 FATF "Guidance for a Risk-Based Approach to
> Virtual Currencies"; (b) the 2018-10 FATF Recommendations
> amendments adding the VASP definition into the glossary;
> (c) the 2019-06-21 FATF Plenary adoption of the Interpretive
> Note to Recommendation 15 extending the Travel Rule to VASPs
> (fatf-r15-vasp-travel-rule-2019). This 2014 report is therefore
> the predicate guidance for the global FATF VASP regime.
> Live fatf-gafi.org PDF captured 2026-05-21 with replayable
> body_hash sha256:c2aed2a0bb42... (558KB, no Wayback memento
> accessible across 2014-2024).
- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-currency-definitions-aml-cft-risk.html>
  - Wayback: <https://web.archive.org/web/2014/https://www.fatf-gafi.org/en/publications/Methodsandtrends/Virtual-currency-definitions-aml-cft-risk.html>
  > FATF publication landing page for the same June 2014 report,
> retained as a secondary anchor for the publication record. The
> landing page provides the canonical FATF citation metadata.
> Retained as contextual_unarchived; primary anchoring lives on
> the PDF citation above.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Virtual currency exchangers and administrators (global FATF class)

> Canonical target of this 2014 FATF report is the open-ended
> regulatory class of "virtual currency exchangers and administrators"
> as defined in the report glossary. Exchangers are "natural or legal
> persons engaged as a business in the exchange of virtual currency
> for real currency, funds, or other forms of virtual currency"; the
> report flags exchangers as the primary regulatory access point
> where AML/CFT obligations can be attached. Administrators are
> "persons engaged as a business in issuing/redeeming a centralised
> virtual currency". The class is open-ended by construction and
> operates at the supranational standard-setting layer; binding
> force is mediated entirely by downstream member-state
> implementation following the later 2019 R.15 INR adoption.
> Marked enumeration=subset rather than complete because the class
> is open-ended and pre-regime — the 2014 report names categories
> without enumerating member entities or addresses. actor_name
> labels the regulated class; no on-chain addresses or
> canonical_domains are enumerated because the report does not
> designate specific entities or hosts. Schema enum target.kind has
> no regulatory_class value; entity is the closest schema match and
> matches the precedent set by fincen-virtual-currency-msb-guidance-
> 2013 and fatf-r15-vasp-travel-rule-2019.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `vc_exchanger_administrator_class_defined_supranational_predicate_guidance`

**Window**: `2014-06-26 00:00:00+00:00` → `2019-06-21 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fatf-gafi.org/content/dam/fatf-gafi/reports/Virtual-currency-key-definitions-and-potential-aml-cft-risks.pdf>
  - body_hash: `sha256:c2aed2a0bb4233b1f743110618ed5e4d530ef74483a187c7d76fd1a530215c2e`
  - body_path: `sources/http_captures/fatf-virtual-currencies-key-definitions-2014/primary/www.fatf-gafi.org__content-dam-fatf-gafi-reports-Virtual-currency-key-definitions-and-potential-aml-cft-risks.pdf__40c190be0a.bin`
  > FATF 2014-06-26 report is the supranational risk-framing
> predicate instrument. observation_kind=observed_no_change
> honestly represents the load-bearing role of this report:
> it introduces the taxonomy ("exchanger", "administrator",
> "convertible / non-convertible VC") that anchors the later
> regulatory regime but does not itself impose binding VASP
> obligations or Travel Rule transmission. The substantive
> regulatory cascade is dispersed across the 2014→2019 arc
> (2015-06 RBA guidance, 2018-10 VASP definition added to
> Recommendations, 2019-06-21 R.15 INR Travel Rule adoption)
> rather than localized to a single point-in-time CEX
> cessation directly attributable to the 2014 report alone.
> attribution=none at the class-level supranational
> standard-setting axis: the 2014 report introduces taxonomy
> and risk-framing but produces no direct measurable off-ramp
> effect in the 2014-06-26 to 2019-06-21 pre-regime window
> (window field). The validator requires attribution=none on
> observed_no_change rows; the user authoring brief suggested
> attribution=plausible to express "dispersed pre-regime
> guidance," which is documented in analysis_notes but cannot
> be expressed at the observation-row level under the
> schema's observed_no_change attribution constraint.
> Live fatf-gafi.org PDF captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)
- [`eba-virtual-currencies-opinion-eba-op-2014-08`](./eba-virtual-currencies-opinion-eba-op-2014-08.md)
- [`fincen-virtual-currency-msb-guidance-2013`](./fincen-virtual-currency-msb-guidance-2013.md)
- [`oecd-carf-2022`](./oecd-carf-2022.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c736a32`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

