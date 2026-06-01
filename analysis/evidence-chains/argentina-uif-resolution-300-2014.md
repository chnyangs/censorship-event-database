# Evidence chain — `argentina-uif-resolution-300-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `029a430` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T14:19:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Resolución UIF N° 300/2014, issued 2014-07-04 and effective
> 2014-08-01, imposed STR/KYC-style reporting obligations on
> Argentine Article-20 obliged entities (sujetos obligados) in
> respect of virtual-currency operations. The cascade surface is
> class-level on Argentine obliged entities; no exchange-side
> Argentina-resident cutoff is documented in this authoring pass,
> so offramp_cex carries an observation_kind=observed_no_change
> row with attribution=none.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `AR_UIF`
- **Timestamp**: `2014-07-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <http://servicios.infoleg.gob.ar/infolegInternet/anexos/230000-234999/231930/norma.htm>
  - Wayback: <https://web.archive.org/web/20170721151950/http://servicios.infoleg.gob.ar/infolegInternet/anexos/230000-234999/231930/norma.htm>
  - body_hash: `sha256:3f76bffe0838d9eec8a6ca166950124708e04e9ea07baaf547f86cfb8c6732dd`
  - body_path: `sources/http_captures/argentina-uif-resolution-300-2014/primary/web.archive.org__web-20170721151950-http-servicios.infoleg.gob.ar-infolegInternet-anexos-230000-234999-231930-norma.htm__4df8839055.html`
  > Official text of Resolución UIF N° 300/2014 hosted on Infoleg
> (servicios.infoleg.gob.ar), the canonical Argentine legal-
> information database maintained by the Ministerio de Justicia.
> Dated 2014-07-04 and signed by the UIF (Unidad de Información
> Financiera / Financial Information Unit), the autonomous AML/CFT
> authority created by Law 25.246. The resolution defines
> "monedas virtuales" (virtual currencies) as digital
> representations of value that function as a medium of exchange,
> unit of account, and/or store of value but lack legal-tender
> status and are not issued or guaranteed by any state, and it
> requires obliged entities (sujetos obligados) enumerated in
> Article 20 of Law 25.246 — banks, financial institutions,
> exchange houses, broker-dealers, escribanos, and other
> AML-regulated counterparties — to report all virtual-currency
> operations to the UIF via the agency's online reporting portal.
> The provisions took effect on 2014-08-01. Wayback memento 20170721151950 captured 2026-05-21.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2014/07/10/argentinian-money-regulator-mandates-reporting-on-bitcoin-activity>
  - Wayback: <https://web.archive.org/web/20211209132830/https://www.coindesk.com/markets/2014/07/10/argentinian-money-regulator-mandates-reporting-on-bitcoin-activity>
  - body_hash: `sha256:867e96c0804f88234034750bb543f2798c826d577f88865e3c16c6c10a28e1c9`
  - body_path: `sources/http_captures/argentina-uif-resolution-300-2014/primary/web.archive.org__web-20211209132830-https-www.coindesk.com-markets-2014-07-10-argentinian-money-regulator-mandates-reporting-on-bitcoin-activity__ab131ea5fe.html`
  > CoinDesk English-language report dated 2014-07-10 titled
> "Argentinian Money Regulator Mandates Reporting on Bitcoin
> Activity" summarising Resolución 300/2014 for the international
> crypto press. Used here as a translation / contextual anchor
> on the obliged-entity reporting obligation and the
> 2014-08-01 effective date. Wayback memento 20211209132830 captured 2026-05-21.
- **`supporting_journalism`**
  - URL: <https://www.cronista.com/finanzasmercados/LA-UIF-expande-el-control-a-las-monedas-virtuales-20140711-0044.html>
  - Wayback: <https://web.archive.org/web/2014/https://www.cronista.com/finanzasmercados/LA-UIF-expande-el-control-a-las-monedas-virtuales-20140711-0044.html>
  > El Cronista (Argentine business newspaper) report dated
> 2014-07-11 titled "LA UIF expande el control a las monedas
> virtuales", providing contemporaneous Argentine-press
> contextual coverage of the resolution and its scope over
> obliged entities. Retained as contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Argentine Article-20 obliged entities (sujetos obligados)
- **Chains**: `bitcoin`

> Target is the class of "sujetos obligados" (obliged entities)
> enumerated in Article 20 of Law 25.246 — Argentine banks,
> financial institutions, exchange houses (casas de cambio),
> broker-dealers, escribanos, and other AML-regulated counterparties
> — when they engage in or facilitate virtual-currency operations.
> The resolution does not enumerate specific exchanges or specific
> obliged-entity counterparties; it imposes a class-level reporting
> obligation on the entire Article-20 obliged-entity set in respect
> of virtual-currency operations. No specific Argentine or foreign
> exchange is named as the target, so canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_measured_exchange_side_cutoff_of_argentine_residents`

**Window**: `2014-08-01 00:00:00+00:00` → `2014-10-30 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <http://servicios.infoleg.gob.ar/infolegInternet/anexos/230000-234999/231930/norma.htm>
  - Wayback: <https://web.archive.org/web/20170721151950/http://servicios.infoleg.gob.ar/infolegInternet/anexos/230000-234999/231930/norma.htm>
  - body_hash: `sha256:3f76bffe0838d9eec8a6ca166950124708e04e9ea07baaf547f86cfb8c6732dd`
  - body_path: `sources/http_captures/argentina-uif-resolution-300-2014/primary/web.archive.org__web-20170721151950-http-servicios.infoleg.gob.ar-infolegInternet-anexos-230000-234999-231930-norma.htm__4df8839055.html`
  > Resolución UIF 300/2014 is the legal instrument. It imposes
> STR-style reporting obligations on Article-20 obliged entities
> in respect of virtual-currency operations, effective
> 2014-08-01, but it does not name any specific exchange as
> having implemented an Argentina-resident cutoff in response.
> The observation_kind=observed_no_change row records that the
> cascade surface at offramp_cex is class-level (Argentine
> obliged entities as a class) rather than exchange-specific
> in the available public record. attribution=none consistent
> with observed_no_change rows per schema §1.1. Wayback memento 20170721151950 captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `029a430`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

