# Evidence chain — `egold-doj-indictment-2007-04`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `93a10f9` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:50:49Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2007-04-27 DOJ indictment of e-Gold Ltd., Gold & Silver Reserve Inc.,
> and principals (18 USC s 1960 + s 1956(h)) placed the pre-Bitcoin
> digital-currency MSB under federal enforcement (offramp_cex
> observed_change, attribution plausible); the seminal since-2007 anchor,
> resolved at the 2008 guilty plea. Discovery-tier only."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_DC`
- **Timestamp**: `2007-04-27 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html>
  - Wayback: <https://web.archive.org/web/20091201225327/http://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html>
  - body_hash: `sha256:44f71f8a576076e415daef9c169b3e44c998b1538a1e7d48a0c9d839609e7cdb`
  - body_path: `sources/http_captures/egold-doj-indictment-2007-04/primary/web.archive.org__web-20070601000000-https-www.justice.gov-archive-opa-pr-2007-April-07_crm_301.html__10dd69e8c1.html`
  > DOJ press release #07-301 (returned 2007-04-24, unsealed 2007-04-27):
> "Digital Currency Business E-Gold Indicted for Money Laundering and
> Illegal Money Transmitting." A four-count federal grand-jury
> indictment charged e-Gold Ltd., Gold & Silver Reserve Inc., and
> principals Douglas Jackson, Reid Jackson, and Barry Downey with
> conspiracy to launder money (18 USC s 1956(h)), conspiracy to
> operate an unlicensed money transmitting business, and operating
> such a business (18 USC s 1960). The SEMINAL pre-Bitcoin
> digital-currency enforcement action; the 2008-07-21 guilty plea
> (egold-doj-guilty-plea-2008-07) is the resolution stage. Wayback
> 20091201225327 pinned.
- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - Wayback: <https://web.archive.org/web/20170328035206/https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - body_hash: `sha256:3f32e6096bc756a52f7d8473f62012c1126ab1706f81b3716fbeb507b06d3c5d`
  - body_path: `sources/http_captures/egold-doj-indictment-2007-04/primary/web.archive.org__web-20120101000000-https-www.justice.gov-archive-criminal-cybercrime-press-releases-2007-egoldIndict.htm__9f05621822.html`
  > DOJ Computer Crime & Intellectual Property Section (CCIPS) copy of
> the 2007-04-27 e-Gold indictment release. Corroborating primary
> anchor. Wayback 20170328035206 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: e-Gold Ltd. + Gold & Silver Reserve Inc. + Douglas Jackson (2007 indictment)
- **Canonical domains**: `e-gold.com`

> Named corporate defendants e-Gold Ltd. (operator of the e-gold
> digital-gold-account ledger) and Gold & Silver Reserve Inc. (US
> fiat-side affiliate), plus three named individual directors (Douglas
> Jackson, Reid Jackson, Barry Downey). e-Gold was a centralized
> digital-gold-account ledger (gold-grams unit; no blockchain), so no
> on-chain addresses are enumerated. Subset: the named defendants + the
> e-Gold corporate vehicle.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `egold_operations_restricted_under_federal_indictment`

**Timestamp**: `2007-04-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html>
  - Wayback: <https://web.archive.org/web/20091201225327/http://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html>
  - body_hash: `sha256:44f71f8a576076e415daef9c169b3e44c998b1538a1e7d48a0c9d839609e7cdb`
  - body_path: `sources/http_captures/egold-doj-indictment-2007-04/primary/web.archive.org__web-20070601000000-https-www.justice.gov-archive-opa-pr-2007-April-07_crm_301.html__10dd69e8c1.html`
  > DOJ 2007-04-27 indictment of e-Gold + principals (18 USC s 1960
> + s 1956(h)). attribution=plausible: the indictment is the
> enforcement action that placed e-Gold's MSB operations under
> legal restriction; the full operational cessation is the
> downstream consequence resolved at the 2008 plea.
- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - Wayback: <https://web.archive.org/web/20170328035206/https://www.justice.gov/archive/criminal/cybercrime/press-releases/2007/egoldIndict.htm>
  - body_hash: `sha256:3f32e6096bc756a52f7d8473f62012c1126ab1706f81b3716fbeb507b06d3c5d`
  - body_path: `sources/http_captures/egold-doj-indictment-2007-04/primary/web.archive.org__web-20120101000000-https-www.justice.gov-archive-criminal-cybercrime-press-releases-2007-egoldIndict.htm__9f05621822.html`
  > DOJ CCIPS copy of the indictment release. Corroborating anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`egold-doj-guilty-plea-2008-07`](./egold-doj-guilty-plea-2008-07.md)
- [`liberty-reserve-coordinated-takedown-2013-05`](./liberty-reserve-coordinated-takedown-2013-05.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `93a10f9`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

