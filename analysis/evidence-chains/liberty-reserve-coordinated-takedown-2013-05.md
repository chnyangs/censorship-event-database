# Evidence chain — `liberty-reserve-coordinated-takedown-2013-05`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c736a32` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2013-05-28 coordinated U.S. takedown of Liberty Reserve S.A.
> (DOJ SDNY indictment of 7 principals + seizure of five domains incl.
> LibertyReserve.com + Treasury/FinCEN's first Section 311 finding
> against a virtual-currency provider) produced a 2-layer cascade:
> l4_frontend (domain seizure) and offramp_cex (global service
> cessation), both attribution=direct. Historical-baseline tier."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2013-05-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/indictment-supporting-documents-us-v-liberty-reserve-et-al>
  - Wayback: <https://web.archive.org/web/20150531160601/http://www.justice.gov/usao-sdny/pr/indictment-supporting-documents-us-v-liberty-reserve-et-al>
  - body_hash: `sha256:2e13536856cb085a853e1a99bf09e3a4e04e79d829192c3a5c6528def77f8215`
  - body_path: `sources/http_captures/liberty-reserve-coordinated-takedown-2013-05/primary/web.archive.org__web-20130601000000-https-www.justice.gov-usao-sdny-pr-indictment-supporting-documents-us-v-liberty-reserve-et-al__6ed7114285.html`
  > DOJ SDNY press release / indictment-supporting-documents page
> (2013-05-28): U.S. v. Liberty Reserve et al. The Southern
> District of New York indicted seven principals/employees of
> Liberty Reserve S.A. (incl. founder Arthur Budovsky) for
> operating a $6B money-laundering enterprise, and the
> coordinated action seized five domain names including
> LibertyReserve.com, taking the platform offline. First
> prosecution of a virtual-currency provider of this scale.
> Wayback 20150531160601 pinned.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jl1956>
  - Wayback: <https://web.archive.org/web/20220913152511/https://home.treasury.gov/news/press-releases/jl1956>
  - body_hash: `sha256:585839c1c3191af94fd9b4f2b21a0694d729d02f08beb53e617b260ce48cbd17`
  - body_path: `sources/http_captures/liberty-reserve-coordinated-takedown-2013-05/primary/web.archive.org__web-20130601000000-https-home.treasury.gov-news-press-releases-jl1956__73dd02d857.html`
  > U.S. Treasury press release jl1956 (2013-05-28): Treasury/FinCEN
> identified Liberty Reserve S.A. as a financial institution of
> primary money-laundering concern under USA PATRIOT Act Section
> 311 — the FIRST use of Section 311 against a virtual-currency
> provider, proposing special measures to cut Liberty Reserve off
> from the U.S. financial system. Wayback 20220913152511 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Liberty Reserve S.A. + Arthur Budovsky
- **Canonical domains**: `libertyreserve.com`

> Liberty Reserve S.A. (Costa Rica-domiciled centralized digital-
> currency provider; "LR" units backed by a centralized ledger, no
> blockchain) and seven named principals/employees (incl. founder
> Arthur Budovsky and Vladimir Kats). The action seized five domain
> names including LibertyReserve.com. Marked subset: targets the
> named defendants + the Liberty Reserve corporate vehicle + its
> operational domains rather than an enumerated complete set of LR
> account holders. No on-chain addresses (centralized ledger).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `doj_seizes_libertyreserve_com_and_four_other_domains`

**Timestamp**: `2013-05-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/indictment-supporting-documents-us-v-liberty-reserve-et-al>
  - Wayback: <https://web.archive.org/web/20150531160601/http://www.justice.gov/usao-sdny/pr/indictment-supporting-documents-us-v-liberty-reserve-et-al>
  - body_hash: `sha256:2e13536856cb085a853e1a99bf09e3a4e04e79d829192c3a5c6528def77f8215`
  - body_path: `sources/http_captures/liberty-reserve-coordinated-takedown-2013-05/primary/web.archive.org__web-20130601000000-https-www.justice.gov-usao-sdny-pr-indictment-supporting-documents-us-v-liberty-reserve-et-al__6ed7114285.html`
  > DOJ SDNY 2013-05-28: seizure of five domain names including
> LibertyReserve.com as part of the coordinated takedown.
> attribution=direct: the DOJ directly seized the operational
> frontend domains (named state action against the named domains).

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `liberty_reserve_digital_currency_service_ceased_globally`

**Timestamp**: `2013-05-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/indictment-supporting-documents-us-v-liberty-reserve-et-al>
  - Wayback: <https://web.archive.org/web/20150531160601/http://www.justice.gov/usao-sdny/pr/indictment-supporting-documents-us-v-liberty-reserve-et-al>
  - body_hash: `sha256:2e13536856cb085a853e1a99bf09e3a4e04e79d829192c3a5c6528def77f8215`
  - body_path: `sources/http_captures/liberty-reserve-coordinated-takedown-2013-05/primary/web.archive.org__web-20130601000000-https-www.justice.gov-usao-sdny-pr-indictment-supporting-documents-us-v-liberty-reserve-et-al__6ed7114285.html`
  > The indictment + domain seizure + Section 311 finding ended
> Liberty Reserve's digital-currency service globally; the
> platform did not resume operations. attribution=direct: the
> coordinated DOJ/Treasury action is the operative state
> instrument that terminated the service.
- **`primary_legal`**
  - URL: <https://www.fincen.gov/resources/statutes-regulations/federal-register-notices/finding-liberty-reserve-sa-financial>
  - Wayback: <https://web.archive.org/web/20170619012558/https://www.fincen.gov/resources/statutes-regulations/federal-register-notices/finding-liberty-reserve-sa-financial>
  - body_hash: `sha256:0aeb6f46ce91bec0df9e85c60632b9e0337690cec3648777023b31e3c14625af`
  - body_path: `sources/http_captures/liberty-reserve-coordinated-takedown-2013-05/primary/web.archive.org__web-20130701000000-https-www.fincen.gov-resources-statutes-regulations-federal-register-notices-finding-liberty-reserve-sa-financial__f87c92b12b.html`
  > FinCEN finding that Liberty Reserve S.A. is a financial
> institution of primary money-laundering concern under PATRIOT
> Act Section 311 — the first use of Section 311 against a
> virtual-currency provider. Corroborating primary anchor for
> the offramp_cex service termination.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`liberty-reserve-costa-rica-license-denial-2011-03`](./liberty-reserve-costa-rica-license-denial-2011-03.md)
- [`egold-doj-guilty-plea-2008-07`](./egold-doj-guilty-plea-2008-07.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c736a32`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

