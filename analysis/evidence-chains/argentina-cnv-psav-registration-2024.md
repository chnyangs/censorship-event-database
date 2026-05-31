# Evidence chain — `argentina-cnv-psav-registration-2024`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `2f5abab` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:36:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Resolución General CNV N° 994/2024, published 2024-03-25,
> established the Argentine PSAV (Proveedor de Servicios de
> Activos Virtuales) registration regime under Ley 27.739. The
> cascade surface is class-level on PSAVs operating in or into
> Argentina; no exchange-side Argentina-resident cutoff is
> documented in this authoring pass, so offramp_cex carries an
> observation_kind=observed_no_change row with attribution=none.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `AR_CNV`
- **Timestamp**: `2024-03-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.boletinoficial.gob.ar/detalleAviso/primera/305110/20240325>
  - Wayback: <https://web.archive.org/web/20240326083716/https://www.boletinoficial.gob.ar/detalleAviso/primera/305110/20240325>
  - body_hash: `sha256:0ef4637e4a3961a2061738616706166f0e46058fbb912c1f01d1a856d1fa7144`
  - body_path: `sources/http_captures/argentina-cnv-psav-registration-2024/primary/web.archive.org__web-20240326083716-https-www.boletinoficial.gob.ar-detalleAviso-primera-305110-20240325__6c05882b65.html`
  > Boletín Oficial de la República Argentina — publication of
> Comisión Nacional de Valores (CNV) Resolución General N°
> 994/2024 on 2024-03-25, establishing the Registro de
> Proveedores de Servicios de Activos Virtuales (PSAV /
> Virtual Asset Service Provider Registry). The resolution
> implements Ley 27.739 (the AML modernisation law that
> amended Ley 25.246) and introduces the PSAV figure into
> Argentine financial-supervision law. A PSAV is defined as
> any individual or legal entity that, as a business, carries
> out one or more of (i) exchange between virtual assets and
> legal tender, (ii) exchange between forms of virtual assets,
> (iii) transfer of virtual assets, (iv) custody / management
> of virtual assets or instruments allowing control over such
> assets, and (v) participation in / provision of financial
> services related to a virtual-asset offer or sale. All such
> providers must register in the PSAV registry before
> commencing operations; failure to register results in a ban
> on operating in Argentina. The registry is closed to
> applicants resident, domiciled, or incorporated in
> jurisdictions on the FATF non-cooperative / high-risk list
> or in non-cooperative tax-transparency jurisdictions.
> Wayback memento 20240326083716 captured 2026-05-21.
- **`supporting_tracker`**
  - URL: <https://digitalpolicyalert.org/event/18948-implemented-cnv-resolution-on-registry-of-virtual-asset-service-providers-resolution-9942024>
  - Wayback: <https://web.archive.org/web/20250430212451/https://digitalpolicyalert.org/event/18948-implemented-cnv-resolution-on-registry-of-virtual-asset-service-providers-resolution-9942024>
  - body_hash: `sha256:0035b97d15f8cfd67f7350593bf57b741f400fbf7a98c867af43e26cdbecbed4`
  - body_path: `sources/http_captures/argentina-cnv-psav-registration-2024/primary/web.archive.org__web-20250430212451-https-digitalpolicyalert.org-event-18948-implemented-cnv-resolution-on-registry-of-virtual-asset-service-providers-resolution-994202__95ba618c7c.html`
  > Digital Policy Alert tracker entry for "Argentina: Implemented
> CNV Resolution on Registry of Virtual Asset Service Providers
> (Resolution 994/2024)", indexing the 2024-03-25 effective
> date and the FATF-aligned AML/CFT scope of the PSAV regime.
> Wayback memento 20250430212451 captured 2026-05-21.
- **`supporting_journalism`**
  - URL: <https://www.marval.com/publicacion/se-reglamenta-la-inscripcion-de-los-proveedores-de-servicios-de-activos-virtuales-15792?lang=en>
  - Wayback: <https://web.archive.org/web/2024/https://www.marval.com/publicacion/se-reglamenta-la-inscripcion-de-los-proveedores-de-servicios-de-activos-virtuales-15792?lang=en>
  > Marval, O'Farrell & Mairal (Argentine law-firm client alert)
> English-language summary of Resolución General 994/2024
> titled "Registration of Virtual Assets Service Providers Now
> Regulated", confirming the PSAV definition, the registration
> prerequisite for operating in Argentina, and the FATF
> AML/CFT alignment. Used as a translation / contextual
> anchor. Specific Wayback snapshot timestamp requires
> re-pinning in human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PSAVs operating in or into Argentina (Ley 27.739 / CNV RG 994/2024)
- **Chains**: `cross_chain`

> Target is the class of Proveedores de Servicios de Activos
> Virtuales (PSAV / Virtual Asset Service Providers) operating in
> or into Argentina — exchanges, custodians, transfer providers,
> and virtual-asset-related financial-service providers as defined
> in Ley 27.739. The resolution does not enumerate specific
> exchanges; it imposes a class-level registration prerequisite on
> the entire PSAV set. No specific Argentine or foreign exchange
> is named as the target, so canonical_domains is empty. subset
> enumeration with class-level rationale per codebook §7.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_measured_exchange_side_cutoff_of_argentine_residents`

**Window**: `2024-03-25 00:00:00+00:00` → `2024-06-23 00:00:00+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.boletinoficial.gob.ar/detalleAviso/primera/305110/20240325>
  - Wayback: <https://web.archive.org/web/20240326083716/https://www.boletinoficial.gob.ar/detalleAviso/primera/305110/20240325>
  - body_hash: `sha256:0ef4637e4a3961a2061738616706166f0e46058fbb912c1f01d1a856d1fa7144`
  - body_path: `sources/http_captures/argentina-cnv-psav-registration-2024/primary/web.archive.org__web-20240326083716-https-www.boletinoficial.gob.ar-detalleAviso-primera-305110-20240325__6c05882b65.html`
  > Resolución General CNV N° 994/2024 is the legal
> instrument. It imposes a class-level PSAV registration
> prerequisite under Ley 27.739, effective on publication
> 2024-03-25, but it does not name any specific exchange as
> having implemented an Argentina-resident cutoff in
> response. The observation_kind=observed_no_change row
> records that the cascade surface at offramp_cex is class-
> level (PSAVs as a class) rather than exchange-specific in
> the available public record. attribution=none consistent
> with observed_no_change rows per codebook §1.1. Wayback
> memento 20240326083716 captured 2026-05-21.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`argentina-uif-resolution-300-2014`](./argentina-uif-resolution-300-2014.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2f5abab`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

