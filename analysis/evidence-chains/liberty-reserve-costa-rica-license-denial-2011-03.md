# Evidence chain — `liberty-reserve-costa-rica-license-denial-2011-03`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `6293bc1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Costa Rica's SUGEF refused on 2011-03-07 to grant Liberty Reserve
> S.A. authorization to operate as a regulated financial entity for
> lack of transparency in funding management, creating the
> unlicensed-operation status in Costa Rica that the May 2013 US
> DOJ unsealed indictment used as the 18-USC-1960 predicate. The
> row claims only this single-layer offramp regulatory observation
> with attribution=direct; no L0/L1/L3/L4/asset-onchain effects are
> coded. Discovery-tier only: no comparable-analysis use."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `CR_SUGEF`
- **Timestamp**: `2011-03-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Liberty%20Reserve%2C%20et%20al.%20Redacted%20AUSA%20Appln%20with%20exhibits.pdf>
  - body_hash: `sha256:c68ed7755959ea657e5a3a95bc66403546527626173902275aa5b4995665731f`
  - body_path: `sources/http_captures/liberty-reserve-costa-rica-license-denial-2011-03/v0_3_primary_repair/www.justice.gov__sites-default-files-usao-sdny-legacy-2015-03-25-Liberty-20Reserve-2C-20et-20al.-20Redacted-20AUSA-20Appln-20with-20exhibits.pdf__0d5df2a97c.bin`
  > DOJ / SDNY AUSA application with exhibits in the Liberty
> Reserve matter. This scanned court-record PDF corroborates
> Liberty Reserve's inability to obtain a Costa Rican SUGEF
> money-transmitting license by November 2011 and the later
> withdrawal / purported shutdown representation to SUGEF after
> the FinCEN notice. It strengthens the unlicensed-operation
> predicate but does not independently establish the exact
> 2011-03-07 investigation-opening date; OCR and human review
> should extract the precise paragraphs before release use.
- **`supporting_journalism`**
  - URL: <https://ticotimes.net/2013/05/27/liberty-reserve-a-cyberweb-of-intrigue>
  - Wayback: <https://web.archive.org/web/2011/https://ticotimes.net/2013/05/27/liberty-reserve-a-cyberweb-of-intrigue>
  > Tico Times (San José, Costa Rica) feature reporting (2013-05-27):
> "Liberty Reserve: A cyberweb of intrigue." Documents that
> Costa Rica's Superintendencia General de Entidades Financieras
> (SUGEF) refused to license Liberty Reserve in 2011, citing
> lack of transparency and accounting of funding management.
> State prosecutor José Pablo González is quoted attributing
> the denial to opaque sourcing of the firm's funds. Reports
> that a criminal investigation in Costa Rica was opened
> 2011-03-07 following "suspicious" bank activity surfaced by
> the local banking system. evidence_use=contextual_unarchived:
> no body_hash captured in this DRYRUN authoring pass and the
> wayback URL is a 2011 wildcard pointer pending human-audit
> re-pin against a snapshotted timestamp.
- **`supporting_journalism`**
  - URL: <https://ticotimes.net/2013/05/24/millions-of-dollars-in-limbo-after-shuttering-of-digital-currency-site-liberty-reserve>
  - Wayback: <https://web.archive.org/web/2011/https://ticotimes.net/2013/05/24/millions-of-dollars-in-limbo-after-shuttering-of-digital-currency-site-liberty-reserve>
  > Tico Times reporting (2013-05-24) "Millions of dollars in
> limbo after shuttering of digital currency site Liberty
> Reserve" — corroborates the 2011 SUGEF license refusal and
> documents that Liberty Reserve continued operating without
> SUGEF certification, funneling activity through five other
> Costa Rican corporate vehicles controlled by founder Arthur
> Budovsky. This unlicensed-operation status became the
> predicate for the May 2013 US DOJ unsealed indictment (18
> USC s 1960 — operation of an unlicensed money transmitting
> business — and 18 USC s 1956 conspiracy to engage in money
> laundering). evidence_use=contextual_unarchived for the
> DRYRUN pass.
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/Liberty_Reserve>
  - Wayback: <https://web.archive.org/web/2011/https://en.wikipedia.org/wiki/Liberty_Reserve>
  > Wikipedia "Liberty Reserve" entry — secondary tertiary
> consolidation citing the 2011 SUGEF denial, the 2011-03-07
> Costa Rican criminal-investigation opening, and the
> downstream 2013 US DOJ sealed indictment. Retained as
> tertiary pointer only; not load-bearing for admission.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Liberty Reserve S.A. (Arthur Budovsky)
- **Canonical domains**: `libertyreserve.com`

> Named target: Liberty Reserve S.A. (Costa Rica corporate
> vehicle of the Liberty Reserve digital-currency service,
> operated by Arthur Budovsky). SUGEF refused to license the
> firm to operate as a regulated financial entity in Costa Rica.
> Marked subset because the SUGEF action targets the named
> Liberty Reserve corporate entity and does not enumerate the
> five additional Costa Rican shell companies through which
> Budovsky subsequently continued operations (those surface in
> the 2013 US DOJ indictment, not the 2011-03-07 SUGEF denial).
> No on-chain addresses: Liberty Reserve was a centralized
> off-chain digital-currency ledger ("LR" units backed by USD/
> EUR/gold-grams), not a blockchain token.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sugef_refuses_to_license_liberty_reserve_creating_unlicensed_operation_status`

**Timestamp**: `2011-03-07 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/sites/default/files/usao-sdny/legacy/2015/03/25/Liberty%20Reserve%2C%20et%20al.%20Redacted%20AUSA%20Appln%20with%20exhibits.pdf>
  - body_hash: `sha256:c68ed7755959ea657e5a3a95bc66403546527626173902275aa5b4995665731f`
  - body_path: `sources/http_captures/liberty-reserve-costa-rica-license-denial-2011-03/v0_3_primary_repair/www.justice.gov__sites-default-files-usao-sdny-legacy-2015-03-25-Liberty-20Reserve-2C-20et-20al.-20Redacted-20AUSA-20Appln-20with-20exhibits.pdf__0d5df2a97c.bin`
  > Scanned DOJ / SDNY court-record PDF with exhibits in the
> Liberty Reserve matter. It provides a primary legal-record
> anchor for Liberty Reserve's unlicensed Costa Rica status:
> the AUSA application describes the failure to obtain SUGEF
> licensing by November 2011 and the later withdrawal /
> purported shutdown representation. This supports the
> unlicensed-operation observation but does not replace a
> Costa Rican SUGEF resolution or establish the exact
> 2011-03-07 investigation-opening date. Human audit should
> run OCR and reconcile the Tico Times date with the court
> exhibit text.
- **`semi_primary_wayback`**
  - URL: <https://ticotimes.net/2013/05/27/liberty-reserve-a-cyberweb-of-intrigue>
  - Wayback: <https://web.archive.org/web/20140115164543/https://ticotimes.net/2013/05/27/liberty-reserve-a-cyberweb-of-intrigue>
  - body_hash: `sha256:530f9f2ebc4f742103e96b87d088857806638b76def7cd0fb9574b48be0eeaf7`
  - body_path: `sources/http_captures/liberty-reserve-costa-rica-license-denial-2011-03/primary/web.archive.org__web-20140115164543-https-ticotimes.net-2013-05-27-liberty-reserve-a-cyberweb-of-intrigue__ed891a322c.html`
  > Tico Times reporting (2013-05-27) recording that SUGEF
> (Superintendencia General de Entidades Financieras) refused
> to license Liberty Reserve in 2011 for lack of transparency
> and accounting of funding management. State prosecutor
> José Pablo González named as the public-facing source for
> the licensing-denial framing. The 2011-03-07 anchor is the
> contemporaneously reported Costa Rican criminal-investigation
> opening date triggered by the SUGEF posture. attribution=
> direct under §1.1: the regulator (CR_SUGEF) is named as the
> actor of the licensing refusal and Liberty Reserve S.A. is
> the named target. evidence_use=contextual_unarchived for the
> DRYRUN pass; human-audit must replace with a pinned SUGEF
> resolution or a snapshotted Wayback bracket of the Tico
> Times piece.
- **`semi_primary_wayback`**
  - URL: <https://ticotimes.net/2013/05/24/millions-of-dollars-in-limbo-after-shuttering-of-digital-currency-site-liberty-reserve>
  - Wayback: <https://web.archive.org/web/20140115165052/https://ticotimes.net/2013/05/24/millions-of-dollars-in-limbo-after-shuttering-of-digital-currency-site-liberty-reserve>
  - body_hash: `sha256:3d8deb79fc0bd577a03412eb2ab682cbb240e2672ce9ba670b41ed7e420991ef`
  - body_path: `sources/http_captures/liberty-reserve-costa-rica-license-denial-2011-03/primary/web.archive.org__web-20140115165052-https-ticotimes.net-2013-05-24-millions-of-dollars-in-limbo-after-shuttering-of-digital-currency-site-liberty-reserve__ddcf819897.html`
  > Tico Times (2013-05-24) corroborating reporting that
> Liberty Reserve continued operating without SUGEF
> certification after the 2011 license refusal, funneling
> activity through five additional Costa Rican corporate
> vehicles controlled by Budovsky. Establishes the
> unlicensed-operation status that the 2013 US DOJ used as
> the 18-USC-1960 predicate. evidence_use=contextual_
> unarchived.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`egold-doj-guilty-plea-2008-07`](./egold-doj-guilty-plea-2008-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `6293bc1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

