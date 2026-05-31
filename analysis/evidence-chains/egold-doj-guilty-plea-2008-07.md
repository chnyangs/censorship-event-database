# Evidence chain — `egold-doj-guilty-plea-2008-07`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2008-07-21 DOJ guilty plea by e-Gold Ltd., Gold & Silver
> Reserve Inc., and Douglas Jackson (in US District Court for the
> District of Columbia) on conspiracy to engage in money laundering
> (18 USC s 1956(h)) and operation of an unlicensed money
> transmitting business (18 USC s 1960) produced an offramp_cex
> cascade (e-Gold's digital-gold-account service operations ceased
> and did not resume). The row claims only this single-layer
> offramp shutdown observation with attribution=plausible; no
> L0/L1/L3/L4/asset-onchain effects are coded. Discovery-tier only:
> no comparable-analysis use."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_DC`
- **Timestamp**: `2008-07-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/opa/pr/2008/July/08-crm-635.html>
  - Wayback: <https://web.archive.org/web/20091201212507/https://www.justice.gov/archive/opa/pr/2008/July/08-crm-635.html>
  - body_hash: `sha256:67e126e66c9e8cf3135d66267a567e87ff071bf6bd050204c790030bdb85068c`
  - body_path: `sources/http_captures/egold-doj-guilty-plea-2008-07/primary/web.archive.org__web-20091201212507-https-www.justice.gov-archive-opa-pr-2008-July-08-crm-635.html__a5a5bded31.html`
  > DOJ Criminal Division press release #08-635 (2008-07-21):
> "Digital Currency Business E-Gold Pleads Guilty to Money
> Laundering and Illegal Money Transmitting Charges." Records
> that Dr. Douglas Jackson (51, of Melbourne FL), principal
> director of e-Gold and CEO of Gold & Silver Reserve Inc.,
> pleaded guilty in the US District Court for the District of
> Columbia to (i) conspiracy to engage in money laundering
> (18 USC s 1956(h)) and (ii) operation of an unlicensed money
> transmitting business (18 USC s 1960(b)(1)(A), (B), and (C)).
> E-Gold Ltd. and corporate affiliate Gold & Silver Reserve Inc.
> each pleaded guilty to the same two conspiracy counts. The
> other two senior directors (Barry Downey of Baltimore; Reid
> Jackson of Melbourne FL) each pleaded guilty to felony
> violations of DC law for operating a money transmitting
> business without a license. Charges originated from a federal
> grand jury indictment returned 2007-04-24; sentencing was set
> for 2008-11-20. evidence_use=contextual_unarchived because no
> body_hash has been independently captured in this DRYRUN
> authoring pass; the justice.gov/archive page remains publicly
> accessible and a 2008 Wayback bracketing is straightforward
> in follow-up human-audit. Provisional year-prefix wayback
> anchor pending re-pin.
- **`primary_legal`**
  - URL: <https://www.secretservice.gov/press/releases/2008/07/us-secret-service-led-investigation-digital-currency-business-e-gold-pleads>
  - body_hash: `sha256:7eae7c4475c89ed0a2521bc3d7fc7e3210a003ea44d18068880e45254fd54497`
  - body_path: `sources/http_captures/egold-doj-guilty-plea-2008-07/v0_3_repair/www.secretservice.gov__press-releases-2008-07-us-secret-service-led-investigation-digital-currency-business-e-gold-pleads__fe0ccf4941.html`
  > US Secret Service press release (2008-07-21): "In U.S. Secret
> Service-Led Investigation, Digital Currency Business E-Gold
> Pleads Guilty to Money Laundering and Illegal Money
> Transmitting Charges." Documents USSS lead-agency role in the
> e-Gold investigation alongside IRS-CI and DOJ Criminal
> Division. Retained as contextual_unarchived corroborating
> pointer; the DOJ #08-635 release above is the load-bearing
> trigger anchor.
- **`primary_corporate`**
  - URL: <https://legalupdate.e-gold.com/2008/07/plea-agreement-as-to-douglas-l-jackson-20080721.html>
  > e-Gold company legal-update page (2008-07-21) publishing the
> plea agreement text as to Douglas L. Jackson under 18 USC
> ss 1956(h) and 1960(b)(1)(A), (B), and (C). Primary-corporate
> confirmation from the defendant company of the same guilty
> plea recorded in the DOJ press release. evidence_use=
> contextual_unarchived for this DRYRUN authoring pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: e-Gold Ltd. + Gold & Silver Reserve Inc. + Douglas Jackson
- **Canonical domains**: `e-gold.com`

> Named corporate defendants e-Gold Ltd. (operator of the e-gold
> digital-gold-account ledger) and Gold & Silver Reserve Inc. (its
> US affiliate handling fiat-side exchange of the e-gold unit),
> plus three named individual directors who entered guilty pleas:
> Dr. Douglas Jackson (principal director / CEO), Barry Downey, and
> Reid Jackson. e-Gold was a centralized digital-gold-account
> ledger (gold-grams as the unit of account; no blockchain, no
> decentralized consensus); therefore no on-chain addresses are
> enumerated. Marked subset because the plea targets the named
> defendants and the e-Gold corporate vehicle rather than an
> enumerated complete set of e-Gold account holders. canonical_
> domains lists the e-gold.com operational frontend.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `egold_ceases_operations_following_corporate_and_ceo_guilty_plea`

**Timestamp**: `2008-07-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/archive/opa/pr/2008/July/08-crm-635.html>
  - Wayback: <https://web.archive.org/web/2008/https://www.justice.gov/archive/opa/pr/2008/July/08-crm-635.html>
  > DOJ #08-635 press release recording e-Gold Ltd. + Gold &
> Silver Reserve Inc. + Douglas Jackson guilty pleas to
> conspiracy to engage in money laundering (18 USC s 1956(h))
> and operation of an unlicensed money transmitting business
> (18 USC s 1960). The convictions ended e-Gold's MSB-
> regulated service operations; the gold-grams transfer
> service did not resume normal operations following the
> plea and sentencing (2008-11-20). attribution=plausible
> (not direct) because the DOJ release does not itself order
> a corporate shutdown; the platform wind-down is the
> downstream corporate consequence of the conviction with
> strong temporal coincidence. evidence_use=contextual_
> unarchived for this DRYRUN authoring pass.
- **`primary_corporate`**
  - URL: <https://legalupdate.e-gold.com/2008/07/plea-agreement-as-to-douglas-l-jackson-20080721.html>
  - Wayback: <https://web.archive.org/web/2008/https://legalupdate.e-gold.com/2008/07/plea-agreement-as-to-douglas-l-jackson-20080721.html>
  > e-Gold company legal-update plea-agreement posting (2008-
> 07-21) confirming the Douglas L. Jackson guilty plea under
> 18 USC ss 1956(h) and 1960(b)(1)(A), (B), and (C).
> Primary-corporate self-attestation by the defendant
> company that the plea occurred and that the corporate
> governance of e-Gold was effectively terminated. Retained
> as a supporting anchor for the offramp_cex shutdown
> observation. evidence_use=contextual_unarchived.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`fincen-virtual-currency-msb-guidance-2013`](./fincen-virtual-currency-msb-guidance-2013.md)
- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`coin-mx-doj-murgio-2015`](./coin-mx-doj-murgio-2015.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

