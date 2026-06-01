# Evidence chain — `philippines-bsp-vasp-license-moratorium-2022-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f70cc98` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:48:55Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> BSP Resolution No. 1141 (2022-08-04, effective 2022-09-01) closed the
> regular application window for new VASP licenses in the Philippines for
> three years (later extended indefinitely from 2025-09-01), denying new
> crypto exchanges market entry. Effect carried at offramp_cex as an
> observed_change with direct attribution; the affected applicant set is
> not enumerated and no exchange-side measurement slice is pinned in this
> authoring pass.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `PH_BSP`
- **Timestamp**: `2022-09-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.bsp.gov.ph/Regulations/Issuances/2022/M-2022-035.pdf>
  - Wayback: <https://web.archive.org/web/20260531040728/https://www.bsp.gov.ph/Regulations/Issuances/2022/M-2022-035.pdf>
  - body_hash: `sha256:91dfac514d4bc41768fa0c9451095ccf38273e48a69b393d60f5939767874d1e`
  - body_path: `sources/http_captures/philippines-bsp-vasp-license-moratorium-2022-09/primary/www.bsp.gov.ph__Regulations-Issuances-2022-M-2022-035.pdf__62423443c1.bin`
  > BSP Memorandum No. M-2022-035, official primary trigger instrument
> signed 2022-08-10 by Deputy Governor Chuchi G. Fonacier. The captured
> PDF is body-hash pinned and Wayback-archived; extracted text confirms
> the suspension of new VASP licenses for three years from 2022-09-01.
- **`semi_primary_wayback`**
  - URL: <https://www.rappler.com/business/bangko-sentral-pilipinas-imposes-moratorium-virtual-asset-service-providers-licensing/>
  - Wayback: <https://web.archive.org/web/20220819111117/https://www.rappler.com/business/bangko-sentral-pilipinas-imposes-moratorium-virtual-asset-service-providers-licensing/>
  - body_hash: `sha256:48f70da56ca561fbfd2be23bf44d47450f3e7398e927b8812c26e0540073bb99`
  - body_path: `sources/http_captures/philippines-bsp-vasp-license-moratorium-2022-09/primary/web.archive.org__web-20220819111117-https-www.rappler.com-business-bangko-sentral-pilipinas-imposes-moratorium-virtual-asset-service-providers-licensing__a29fc115f0.html`
  > Rappler, "BSP imposes 3-year moratorium on virtual asset service
> providers licensing" (announced by the BSP 2022-08-12). Captured
> text confirms: "The Bangko Sentral ng Pilipinas (BSP) has imposed
> a three-year moratorium on granting licenses to new virtual asset
> service providers (VASPs)"; "Under Resolution No. 1141, dated
> August 4, the regular application window for new VASP licenses
> shall be closed for three years starting September 1, 2022,
> subject to reassessment based on market developments"; quotes BSP
> Governor Felipe Medalla. Used as the semi-primary anchor because
> the BSP's own MediaDisp.aspx press page is a JavaScript/SharePoint
> shell whose archived HTML body is not content-bearing. The official
> Memorandum No. M-2022-035 PDF is pinned above as the replayable
> primary_government trigger anchor. Wayback memento 20220819111117
> captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: New VASP-license applicants in the Philippines (class)

> Target is the class of prospective new Virtual Asset Service
> Providers (VASPs) — crypto exchanges and custodians — seeking a BSP
> license to operate in the Philippines. The moratorium closes the
> regular application window for new VASP licenses; it does not name
> specific applicants and carves out existing BSP-supervised financial
> institutions (BSFIs) with a stable-or-better SAFr rating and
> applications already past Stage 2 by 2022-08-31. subset enumeration
> with class-level rationale per codebook §7. No specific exchange
> domain is named, so canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `new_vasp_license_window_closed_three_year_moratorium`

**Timestamp**: `2022-09-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.bsp.gov.ph/Regulations/Issuances/2022/M-2022-035.pdf>
  - Wayback: <https://web.archive.org/web/20260531040728/https://www.bsp.gov.ph/Regulations/Issuances/2022/M-2022-035.pdf>
  - body_hash: `sha256:91dfac514d4bc41768fa0c9451095ccf38273e48a69b393d60f5939767874d1e`
  - body_path: `sources/http_captures/philippines-bsp-vasp-license-moratorium-2022-09/primary/www.bsp.gov.ph__Regulations-Issuances-2022-M-2022-035.pdf__62423443c1.bin`
  > BSP Memorandum No. M-2022-035 (Deputy Governor Chuchi G. Fonacier,
> signed 2022-08-10) — official primary source: suspends the grant of
> new VASP licenses for three years from 2022-09-01. Captured 2026-05-31
> (PDF, body_hash-pinned; Wayback-archived 20260531040728). Extracted
> text confirms VASP / virtual asset / three / September / 2022 / license.
- **`semi_primary_wayback`**
  - URL: <https://www.rappler.com/business/bangko-sentral-pilipinas-imposes-moratorium-virtual-asset-service-providers-licensing/>
  - Wayback: <https://web.archive.org/web/20220819111117/https://www.rappler.com/business/bangko-sentral-pilipinas-imposes-moratorium-virtual-asset-service-providers-licensing/>
  - body_hash: `sha256:48f70da56ca561fbfd2be23bf44d47450f3e7398e927b8812c26e0540073bb99`
  - body_path: `sources/http_captures/philippines-bsp-vasp-license-moratorium-2022-09/primary/web.archive.org__web-20220819111117-https-www.rappler.com-business-bangko-sentral-pilipinas-imposes-moratorium-virtual-asset-service-providers-licensing__a29fc115f0.html`
  > BSP Resolution No. 1141 (2022-08-04) closes the regular VASP
> license application window for three years from 2022-09-01.
> attribution=direct per codebook §1.1: the named actor (BSP)
> publicly issued the moratorium resolution and the action names
> the target class (new VASP licensees) and the restriction
> (window closure). The Rappler report is semi-primary because the
> BSP's own MediaDisp.aspx page is a non-content-bearing JS shell;
> the report quotes BSP Governor Medalla and cites Resolution No.
> 1141 directly.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`philippines-sec-binance-block-2024`](./philippines-sec-binance-block-2024.md)
- [`argentina-cnv-psav-registration-2024`](./argentina-cnv-psav-registration-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f70cc98`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

