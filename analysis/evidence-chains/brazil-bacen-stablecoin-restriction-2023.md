# Evidence chain — `brazil-bacen-stablecoin-restriction-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `71b6d3d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `BR_BACEN`
- **Timestamp**: `2023-06-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm>
  - Wayback: <https://web.archive.org/web/20230614113250/https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm>
  - body_hash: `sha256:ea55c2f4b89525353673ae2f89f1f98c68c911266c42dfb45393b4ada8233f5d`
  - body_path: `sources/http_captures/brazil-bacen-stablecoin-restriction-2023/primary/web.archive.org__web-20230614113250-https-www.planalto.gov.br-ccivil_03-_ato2023-2026-2023-decreto-d11563.htm__bf339acd00.html`
  > Decreto nº 11.563, de 13 de junho de 2023 ("Decree No.
> 11,563 of June 13, 2023"), issued by the Brazilian federal
> executive, regulates Lei nº 14.478/2022 (Brazilian Virtual
> Assets Law / BVAL) by designating the Banco Central do
> Brasil (BACEN / BCB) as the competent regulator for virtual
> asset service providers (VASPs) in Brazil. The decree
> operationalizes the BVAL framework that supplies the legal
> basis for BACEN's subsequent administrative restrictions
> on BRL-pegged stablecoin issuance and offshore stablecoin
> trading. Entered into force 2023-06-20. This is the
> operational follow-on to the 2022 crypto law and the
> canonical trigger anchor for BACEN's stablecoin-framework
> authority. Wayback wildcard anchor is provisional; specific
> snapshot timestamp must be re-pinned during human audit
> before this citation may carry an admission anchor in its
> own right. Marked evidence_use=contextual_unarchived
> pending that re-pin.
- **`primary_legal`**
  - URL: <https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14478.htm>
  - Wayback: <https://web.archive.org/web/20221222113356/https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14478.htm>
  - body_hash: `sha256:7e989247268de0e5b150d3921b17a7790f22bd18e4993742a66b44614f3f8847`
  - body_path: `sources/http_captures/brazil-bacen-stablecoin-restriction-2023/primary/web.archive.org__web-20221222113356-https-www.planalto.gov.br-ccivil_03-_ato2019-2022-2022-lei-L14478.htm__31fa07c295.html`
  > Lei nº 14.478, de 21 de dezembro de 2022 (Brazilian Virtual
> Assets Law / BVAL), the underlying federal statute that
> Decreto 11.563/2023 regulates. Published 2022-12-22;
> entered into force 180 days after publication
> (~2023-06-20), coincident with Decreto 11.563/2023.
> Provided as the legislative anchor for the
> regulatory_enforcement trigger; the BVAL itself is a
> framework statute and the trigger.timestamp is pegged to
> the 2023-06-13 BACEN-empowering decree rather than the
> 2022-12-21 law. Wayback anchor provisional pending human
> audit re-pin. Marked evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2023-01-31/brazil-new-law-regulates-cryptocurrency/>
  - Wayback: <https://web.archive.org/web/2023/https://www.loc.gov/item/global-legal-monitor/2023-01-31/brazil-new-law-regulates-cryptocurrency/>
  > US Library of Congress Global Legal Monitor 2023-01-31
> digest of Lei 14.478/2022. Provided as an English-language
> framing source for the BVAL statutory perimeter that the
> 2023-06-13 BACEN decree operationalizes. Wayback anchor
> provisional pending human audit re-pin. Marked
> evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BACEN-supervised virtual-asset service providers (BRL-pegged stablecoin issuers and offshore stablecoin trading venues)
- **Chains**: `ethereum`, `tron`

> Canonical target is the BACEN-supervised virtual-asset-service-
> provider (VASP) class operating in or accessible from Brazil,
> insofar as the BVAL/Decreto 11.563 framework conditions BRL-
> pegged stablecoin issuance and offshore stablecoin trading on
> BACEN registration and supervision. This is a class-level
> regulatory perimeter: the decree does not name specific
> exchanges, issuers, addresses, or domains. enumeration=subset
> rather than complete because the framework addresses a VASP
> class without a fixed roster, matching the codebook §7 class-
> level rationale and the sibling 2014 BCB Comunicado treatment.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `bacen_decreto_11563_offshore_stablecoin_trading_perimeter`

**Window**: `2023-06-13 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm>
  - Wayback: <https://web.archive.org/web/20230614113250/https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/d11563.htm>
  - body_hash: `sha256:ea55c2f4b89525353673ae2f89f1f98c68c911266c42dfb45393b4ada8233f5d`
  - body_path: `sources/http_captures/brazil-bacen-stablecoin-restriction-2023/primary/web.archive.org__web-20230614113250-https-www.planalto.gov.br-ccivil_03-_ato2023-2026-2023-decreto-d11563.htm__bf339acd00.html`
  > Decreto 11.563/2023 grants BACEN VASP-supervisory
> authority. Wayback memento 20230614113250 captured 2026-05-21.
- **`primary_legal`**
  - URL: <https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14478.htm>
  - Wayback: <https://web.archive.org/web/20221222113356/https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14478.htm>
  - body_hash: `sha256:7e989247268de0e5b150d3921b17a7790f22bd18e4993742a66b44614f3f8847`
  - body_path: `sources/http_captures/brazil-bacen-stablecoin-restriction-2023/primary/web.archive.org__web-20221222113356-https-www.planalto.gov.br-ccivil_03-_ato2019-2022-2022-lei-L14478.htm__31fa07c295.html`
  > Lei 14.478/2022 is the underlying statute that Decreto
> 11.563/2023 operationalizes. Wayback memento 20221222113356
> captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`brazil-bcb-comunicado-25306-2014`](./brazil-bcb-comunicado-25306-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `71b6d3d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

