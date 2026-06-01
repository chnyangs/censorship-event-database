# Evidence chain — `brazil-bcb-comunicado-25306-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `08595e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:49:53Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `BR_BCB`
- **Timestamp**: `2014-02-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Comunicado&numero=25306>
  - Wayback: <https://web.archive.org/web/2014/https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Comunicado&numero=25306>
  > Banco Central do Brasil (BCB) Comunicado n° 25.306 dated
> 2014-02-19, titled "Esclarece sobre os riscos decorrentes da
> aquisição das chamadas 'moedas virtuais' ou 'moedas
> criptografadas' e da realização de transações com elas"
> ("Clarifies the risks arising from the acquisition of so-
> called 'virtual currencies' or 'encrypted currencies' and
> from conducting transactions with them"). The communication
> distinguishes between "moedas eletrônicas" (electronic money,
> regulated by Law No. 12,865 of 2013-10-09 and denominated in
> Brazilian reais) and "moedas virtuais" (virtual currencies,
> denominated in a unit of account distinct from sovereign-
> issued currencies). The BCB warns that virtual currencies
> are not issued, regulated, or guaranteed by a monetary
> authority, and that some have no entity responsible for
> their issuance; it notes that the volume of virtual-currency
> transactions in Brazil was still low and did not pose risks
> to the National Financial System. The Comunicado is a
> risk-disclosure advisory addressed to the Brazil-resident
> virtual-currency user class; it is not a banking-rail
> severance order, an ISP/DNS block, or an enumerated-target
> enforcement action. Wayback wildcard anchor is provisional;
> specific snapshot timestamp must be re-pinned during human
> audit before this citation may carry an admission anchor in
> its own right. Marked evidence_use=contextual_unarchived
> pending that re-pin.
- **`supporting_journalism`**
  - URL: <https://www.jusbrasil.com.br/diarios/66539047/dou-secao-3-20-02-2014-pg-105>
  - Wayback: <https://web.archive.org/web/2014/https://www.jusbrasil.com.br/diarios/66539047/dou-secao-3-20-02-2014-pg-105>
  > Diário Oficial da União (DOU) publication record for
> 2014-02-20, Seção 3, page 105, corroborating the official
> publication of Comunicado n° 25.306 in the Brazilian federal
> gazette one day after issuance. Used as a publication-date
> corroborator; specific Wayback snapshot timestamp requires
> re-pinning during human audit. Marked
> evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Brazil-resident virtual-currency users (BCB advisory class)
- **Chains**: `bitcoin`

> Canonical target is the BCB advisory directed at the Brazil-
> resident virtual-currency user class (individuals and legal
> entities acquiring or transacting in "moedas virtuais"). This
> is a class-level advisory: the Comunicado does not name
> specific exchanges, intermediaries, addresses, or domains.
> enumeration=subset rather than complete because the advisory
> addresses a population class without a fixed roster, matching
> the sibling Russia 2014-01 CBR advisory and China 2013-12 PBOC
> notice treatment of class-level central-bank dispositions.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `bcb_comunicado_25306_class_level_risk_advisory`

**Window**: `2014-02-19 00:00:00+00:00` → `2014-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Comunicado&numero=25306>
  - Wayback: <https://web.archive.org/web/2014/https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Comunicado&numero=25306>
  > BCB Comunicado n° 25.306 dated 2014-02-19 is the legal
> instrument. The Comunicado clarifies the risks of
> acquiring and transacting in virtual currencies and
> distinguishes them from electronic money regulated under
> Law No. 12,865 of 2013-10-09. Provisional Wayback anchor;
> specific snapshot timestamp requires human-audit
> re-pinning.
- **`semi_primary_wayback`**
  - URL: <https://www.legisweb.com.br/legislacao/?id=265825>
  - Wayback: <https://web.archive.org/web/20220629043447/https://www.legisweb.com.br/legislacao/?id=265825>
  - body_hash: `sha256:3a0771e0b743ba7752efef71a20c1a16f28d51bc6753cd5af711e6bc716d6632`
  - body_path: `sources/http_captures/brazil-bcb-comunicado-25306-2014/primary/web.archive.org__web-20220629043447-https-www.legisweb.com.br-legislacao__518ffabdc0.html`
  > LegisWeb federal-legislation database faithful reproduction
> of the full text of BCB Comunicado n° 25.306 (2014-02-19),
> including the moedas-eletrônicas vs moedas-virtuais
> distinction and the risk-disclosure language. The official
> bcb.gov.br comunicado URL is a JavaScript SPA that does not
> archive its content; LegisWeb is the replayable semi-primary
> anchor. Wayback memento 20220629043447 captured 2026-05-21.
- **`semi_primary_wayback`**
  - URL: <https://www.jusbrasil.com.br/diarios/66539047/dou-secao-3-20-02-2014-pg-105>
  - Wayback: <https://web.archive.org/web/2014/https://www.jusbrasil.com.br/diarios/66539047/dou-secao-3-20-02-2014-pg-105>
  > Diário Oficial da União 2014-02-20 Seção 3 publication
> record for Comunicado n° 25.306, corroborating the official
> federal-gazette publication one day after issuance. This
> DOU/Jusbrasil URL is retained only as contextual publication
> metadata because it lacks a pinned local body_hash artifact.
> The replayable full-text anchor is the separate LegisWeb source
> above.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`indonesia-bi-bitcoin-warning-2014`](./indonesia-bi-bitcoin-warning-2014.md)
- [`thailand-bot-bitcoin-prohibition-2013`](./thailand-bot-bitcoin-prohibition-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `08595e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

