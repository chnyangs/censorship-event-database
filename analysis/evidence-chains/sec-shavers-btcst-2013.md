# Evidence chain — `sec-shavers-btcst-2013`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `c3fb0ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2013-07-23 SEC civil complaint against Trendon T. Shavers and Bitcoin
> Savings and Trust ended BTCST as an operating Bitcoin-denominated investment
> scheme via subsequent court-ordered asset freeze and receivership; the row
> claims only this single-layer offramp_cex operator-state-change observation
> and does not assert frontend, network, RPC, or on-chain asset effects."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2013-07-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/complaints/2013/comp-pr2013-132.pdf>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/litigation/complaints/2013/comp-pr2013-132.pdf>
  > SEC civil complaint filed 2013-07-23 in the U.S. District Court for the
> Eastern District of Texas, Sherman Division, against Trendon T. Shavers
> and Bitcoin Savings and Trust (BTCST). The complaint alleges Shavers
> operated a Bitcoin-denominated Ponzi scheme from approximately 2011
> through 2012, soliciting investors via the Bitcoin Forum under the alias
> "pirateat40" and promising up to 7% weekly interest on Bitcoin deposits.
> BTCST raised approximately 700,000 BTC in investor funds before
> collapsing in August 2012. Marked evidence_use=contextual_unarchived
> because the authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash for the PDF; the SEC litigation-PDF URL
> format is stable and routinely captured by Wayback, but the specific
> snapshot timestamp is to be re-pinned during human audit before this
> citation may serve as an admission anchor in its own right. Provisional
> Wayback anchor uses Wayback Machine year-prefix lookup.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2013-132>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/news/press-release/2013-132>
  > SEC press release 2013-132 ("SEC Charges Texas Man With Running
> Bitcoin-Denominated Ponzi Scheme") announcing the civil complaint
> against Trendon T. Shavers and Bitcoin Savings and Trust. Names the
> E.D. Tex. venue, the 7%/week promised return structure, and the
> approximately 700,000 BTC raised. First major SEC enforcement action
> against a Bitcoin-denominated investment scheme. Marked
> evidence_use=contextual_unarchived pending a human-audit Wayback re-pin
> and body_hash capture. Provisional Wayback anchor uses Wayback Machine
> year-prefix lookup.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Bitcoin Savings and Trust (BTCST) / Trendon T. Shavers
- **Chains**: `bitcoin`

> Bitcoin Savings and Trust (BTCST) entity plus Trendon T. Shavers
> individual (alias "pirateat40"). No on-chain BTC addresses are
> enumerated at this event level; the ~700,000 BTC raised across the
> 2011-2012 scheme period is referenced in the complaint but specific
> deposit/withdrawal cluster addresses are not pinned here. BTCST was
> operated as an unregistered investment scheme advertised on the
> Bitcoin Forum (bitcointalk.org); it had no public canonical exchange
> domain in the conventional sense, so canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sec_civil_complaint_filed_against_btcst_operator`

**Timestamp**: `2013-07-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/complaints/2013/comp-pr2013-132.pdf>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/litigation/complaints/2013/comp-pr2013-132.pdf>
  > SEC civil complaint (E.D. Tex.) is the legal instrument naming
> Trendon T. Shavers and Bitcoin Savings and Trust as defendants
> and seeking injunctive relief, disgorgement, and civil
> penalties for the alleged Bitcoin-denominated Ponzi scheme.
> attribution=direct because the SEC complaint names the
> operator-state change (cessation as an operating investment
> scheme) and the court order to freeze BTCST assets followed
> directly from this filing. Provisional Wayback anchor; specific
> snapshot timestamp requires human-audit re-pinning.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2013-132>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/news/press-release/2013-132>
  > SEC press release 2013-132 corroborates the complaint filing
> and characterizes the action as the first major SEC enforcement
> against a Bitcoin-denominated investment scheme. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin.
> Provisional Wayback anchor uses year-prefix lookup.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3fb0ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

