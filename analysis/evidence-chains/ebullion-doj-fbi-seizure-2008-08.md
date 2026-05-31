# Evidence chain — `ebullion-doj-fbi-seizure-2008-08`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `2f5abab` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:36:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2008-08 DOJ CDCA / FBI LA federal arrest of James Fayed and
> asset seizure against Goldfinger Coin & Bullion / e-Bullion under
> 18 USC s 1960 (unlicensed money transmitting) produced an
> offramp_cex cascade (e-Bullion's digital-gold-currency service
> ceased; e-bullion.com pulled 2008-08-05; platform did not resume).
> The row claims only this single-layer offramp shutdown observation
> with attribution=direct; no L0/L1/L3/L4/asset-onchain effects are
> coded. Discovery-tier only: no comparable-analysis use."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_CDCA`
- **Timestamp**: `2008-08-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-cdca/pr/united-states-returns-98-million-recovered-e-bullion-illegal-money-transmitting>
  - Wayback: <https://web.archive.org/web/20240515201619/https://www.justice.gov/usao-cdca/pr/united-states-returns-98-million-recovered-e-bullion-illegal-money-transmitting>
  - body_hash: `sha256:bb19746c6ef14797c959a127b899e90bc256ca6b352b3e0f62a3fe7f8f788da9`
  - body_path: `sources/http_captures/ebullion-doj-fbi-seizure-2008-08/primary/web.archive.org__web-20240515201619-https-www.justice.gov-usao-cdca-pr-united-states-returns-98-million-recovered-e-bullion-illegal-money-transmitting__c297136b99.html`
  > US Attorney's Office, Central District of California press
> release: "United States Returns $9.8 Million Recovered from
> e-Bullion Illegal Money-Transmitting Business to Victims."
> Records that James Fayed (founder of e-Bullion / Goldfinger
> Coin & Bullion of Moorpark, California) was charged in 2008
> with conducting an unlicensed money-transmitting business in
> violation of 18 USC s 1960, and that the US Attorney's Office
> for the Central District of California, working with FBI and
> IRS-CI, seized the assets of the Goldfinger group of companies
> — including the gold bullion backing e-Bullion.com on deposit
> at the Perth Mint and the Fayed family ranch in California.
> Trigger date 2008-08-01 represents the day-precision opening
> of the seizure / arrest window (Fayed in federal custody as of
> 2008-08-04 per contemporaneous trade press; e-Bullion.com
> website pulled 2008-08-05). evidence_use=contextual_unarchived
> because no body_hash has been independently captured in this
> DRYRUN authoring pass; the justice.gov press page remains
> publicly accessible and a 2008 Wayback bracketing is
> straightforward in follow-up human-audit. Provisional
> year-prefix wayback anchor pending re-pin.
- **`primary_legal`**
  - URL: <https://www.fbi.gov/contact-us/field-offices/losangeles/news/press-releases/united-states-returns-nearly-12-million-to-victims-of-illegal-money-transmitting-business-called-e-bullion>
  - Wayback: <https://web.archive.org/web/2008/https://www.fbi.gov/contact-us/field-offices/losangeles/news/press-releases/united-states-returns-nearly-12-million-to-victims-of-illegal-money-transmitting-business-called-e-bullion>
  > FBI Los Angeles Field Office press release: "United States
> Returns Nearly $12 Million to Victims of Illegal
> Money-Transmitting Business Called e-Bullion." Documents the
> FBI's investigative role alongside the US Attorney's Office
> CDCA and IRS-CI. Identifies e-Bullion as an internet-based
> digital-gold-currency platform operated without a money
> transmitter license, with roughly $35 million/month routed
> through Goldfinger Coin & Bullion / e-Bullion at the
> platform's height. Retained as primary_legal corroborating
> pointer; the CDCA press release above is the load-bearing
> trigger anchor. evidence_use=contextual_unarchived.
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/E-Bullion>
  - Wayback: <https://web.archive.org/web/2008/https://en.wikipedia.org/wiki/E-Bullion>
  > Wikipedia article on e-Bullion summarising the 2008-08
> seizure timeline: Fayed in federal custody by 2008-08-04
> facing 18 USC s 1960 charges; seizure of $60,000 cash,
> $24,000,000 in gold bullion, and rental-car credit-card
> evidence later linked to Pamela Fayed's murder; e-Bullion.com
> website taken down 2008-08-05. Tertiary corroborating
> reference for trigger-window dating; not load-bearing.
> evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: e-Bullion / Goldfinger Coin & Bullion / James Fayed
- **Canonical domains**: `e-bullion.com`

> Named target entity: e-Bullion (operated by Goldfinger Coin &
> Bullion of Moorpark, California; founder James Fayed). e-Bullion
> was an internet-based digital-gold-currency platform (gold and
> silver units transferred instantly between customer accounts),
> a 2001-launched precursor to later digital-currency platforms
> and a contemporaneous peer of e-Gold. The 2008-08 DOJ/FBI action
> seized the corporate assets of the Goldfinger group including
> the Perth-Mint-held bullion backing e-Bullion.com and the Fayed
> family ranch; e-Bullion.com itself was taken offline 2008-08-05.
> Marked subset because the action targets the named operator
> (Goldfinger / e-Bullion / Fayed) rather than an enumerated
> complete set of e-Bullion account holders. e-Bullion's gold/
> silver units were off-chain ledger entries administered by
> Goldfinger; no blockchain addresses are enumerated.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 96h

**Event label**: `ebullion_ceases_operations_following_doj_fbi_seizure_and_founder_arrest`

**Timestamp**: `2008-08-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-cdca/pr/united-states-returns-98-million-recovered-e-bullion-illegal-money-transmitting>
  - Wayback: <https://web.archive.org/web/2008/https://www.justice.gov/usao-cdca/pr/united-states-returns-98-million-recovered-e-bullion-illegal-money-transmitting>
  > CDCA US Attorney's Office press release recording the
> federal indictment, arrest, and asset seizure against
> James Fayed and the Goldfinger group operating e-Bullion
> under 18 USC s 1960 (unlicensed money transmitting). The
> seizure encompassed Perth-Mint-held bullion backing
> e-bullion.com and the operator's California ranch;
> e-bullion.com was taken offline 2008-08-05 and the platform
> did not resume. attribution=direct under §1.2/§1.4 analogue:
> the DOJ trigger names the target operator (Goldfinger /
> e-Bullion / Fayed) and the platform shutdown is within the
> publicly-knowable compliance window (≤7 days post-seizure).
> evidence_use=contextual_unarchived for this DRYRUN
> authoring pass.
- **`primary_legal`**
  - URL: <https://www.fbi.gov/contact-us/field-offices/losangeles/news/press-releases/united-states-returns-nearly-12-million-to-victims-of-illegal-money-transmitting-business-called-e-bullion>
  - Wayback: <https://web.archive.org/web/2008/https://www.fbi.gov/contact-us/field-offices/losangeles/news/press-releases/united-states-returns-nearly-12-million-to-victims-of-illegal-money-transmitting-business-called-e-bullion>
  > FBI Los Angeles Field Office press release corroborating
> the CDCA seizure and identifying e-Bullion as an
> internet-based digital-gold-currency platform routing
> ~$35M/month at peak. Supports the offramp_cex shutdown
> observation. evidence_use=contextual_unarchived.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`egold-doj-guilty-plea-2008-07`](./egold-doj-guilty-plea-2008-07.md)
- [`liberty-reserve-costa-rica-license-denial-2011-03`](./liberty-reserve-costa-rica-license-denial-2011-03.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2f5abab`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

