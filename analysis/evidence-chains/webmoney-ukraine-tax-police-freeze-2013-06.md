# Evidence chain — `webmoney-ukraine-tax-police-freeze-2013-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `8dbd685` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2013-06-13 the Ukrainian Ministry of Incomes and Fees (tax police)
> froze ~UAH 60M (~$7.5M) across the bank accounts of the local companies
> forming the WebMoney payment system and seized the computer equipment
> running the system, after a Kiev office search the ministry said revealed
> violations including failure to coordinate with the National Bank of
> Ukraine. The row claims only this single-layer offramp_cex observed_change
> with attribution=plausible; no L0/L1/L3/L4/asset-onchain effects are coded.
> Historical-baseline tier only: no comparable-analysis use."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `UA_MINISTRY_OF_INCOMES_AND_FEES`
- **Timestamp**: `2013-06-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://rapsinews.com/news/20130613/267751619.html>
  - Wayback: <https://web.archive.org/web/20130616045519/http://rapsinews.com/news/20130613/267751619.html>
  - body_hash: `sha256:0b6b74a691a1d13da47cc7f65a939e59d793fafd7cf85451f131761f9b252365`
  - body_path: `sources/http_captures/webmoney-ukraine-tax-police-freeze-2013-06/primary/web.archive.org__web-20130615000000-https-rapsinews.com-news-20130613-267751619.html__6577a90155.html`
  > RAPSI (Russian Legal Information Agency) report dated 2013-06-13
> 11:25 (KIEV): "Ukraine freezes $7.5 million in Web Money-linked
> companies' bank accounts." Quotes the Ukrainian Ministry of Incomes
> and Fees (tax authorities) statement: tax police searched the
> WebMoney guarantor company's Kiev office, "revealed a high number of
> violations," found the company "failed to coordinate its work with
> the National Bank of Ukraine," seized a large amount of computer
> equipment used for the system's operation, and froze "over 60 million
> Hryvnas ($7.5 million) held in the bank accounts of companies which
> were part of [the] illegal system." Captured via Wayback memento
> 20130616045519 (nearest to the 2013-06-15 date-prefix request);
> body_hash verified against the saved HTML.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: WebMoney Ukraine (WebMoney Transfer Ukrainian guarantor companies)
- **Canonical domains**: `webmoney.ru`

> Named target: the WebMoney payment system's Ukrainian operation — the
> local guarantor company / corporate vehicles operating WebMoney Transfer
> settlement in Ukraine. The Ministry of Incomes and Fees froze ~UAH 60M
> (~$7.5M) held across the bank accounts of the local companies forming the
> WebMoney system and seized the system's operating computer equipment.
> Marked subset because the action targets the (un-enumerated) set of
> Ukrainian corporate vehicles forming the WebMoney guarantor rather than a
> single named legal entity. WebMoney Transfer was a global centralized
> settlement system (WM-units backed by reserves); not a blockchain token —
> no on-chain addresses to enumerate. The frozen funds were released and the
> accounts reopened in March 2014 per later reporting.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `webmoney_ukraine_bank_accounts_frozen_and_operating_equipment_seized`

**Timestamp**: `2013-06-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://rapsinews.com/news/20130613/267751619.html>
  - Wayback: <https://web.archive.org/web/20130616045519/http://rapsinews.com/news/20130613/267751619.html>
  - body_hash: `sha256:0b6b74a691a1d13da47cc7f65a939e59d793fafd7cf85451f131761f9b252365`
  - body_path: `sources/http_captures/webmoney-ukraine-tax-police-freeze-2013-06/primary/web.archive.org__web-20130615000000-https-rapsinews.com-news-20130613-267751619.html__6577a90155.html`
  > RAPSI 2013-06-13 report quoting the Ministry of Incomes and Fees:
> office search, "high number of violations," failure to coordinate
> with the National Bank of Ukraine, seizure of operating computer
> equipment, and the freeze of "over 60 million Hryvnas ($7.5 million)"
> across the WebMoney-linked company bank accounts. attribution=
> plausible under §1.1: the freeze is causally consistent with and
> announced by the named tax authority, but the row is anchored on
> contemporaneous reporting rather than a captured primary Ministry
> administrative order, so the conservative value is retained per §8.4.
- **`semi_primary_wayback`**
  - URL: <https://rapsinews.com/news/20130614/267768004.html>
  - Wayback: <https://web.archive.org/web/20130618025849/http://rapsinews.com/news/20130614/267768004.html>
  - body_hash: `sha256:bb07f9f1aff13a0498af55fb8ea4cc91000af3a6d17f4e9b10e42a68e4b91545`
  - body_path: `sources/http_captures/webmoney-ukraine-tax-police-freeze-2013-06/secondary/web.archive.org__web-20130620000000-https-rapsinews.com-news-20130614-267768004.html__2cb597dbb6.html`
  > RAPSI 2013-06-14 follow-up "WebMoney Ukraine says tax evasion
> charges are 'absurd'" — independent corroboration of the freeze and
> the tax-evasion / unlicensed-operation basis, carrying WebMoney's
> own contestation of the charges. Second independent semi-primary
> group anchoring the same action.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`liberty-reserve-costa-rica-license-denial-2011-03`](./liberty-reserve-costa-rica-license-denial-2011-03.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8dbd685`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

