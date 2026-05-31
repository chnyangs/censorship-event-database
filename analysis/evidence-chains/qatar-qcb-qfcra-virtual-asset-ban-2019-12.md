# Evidence chain — `qatar-qcb-qfcra-virtual-asset-ban-2019-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `939a17f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:50:46Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The QFC Regulatory Authority issued an ALERT dated 26 December 2019 affirming
> that Virtual Asset Services may not be conducted in or from the Qatar Financial
> Centre, barring all Authorised Firms from providing or facilitating VASP services
> (fiat-crypto exchange, custody, transfer) under QFC Law No. 7 of 2005, with a
> carve-out for regulated digital securities. Captured at class level at the
> offramp_cex layer; no specific operator enumeration claimed."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `QA_QFCRA`
- **Timestamp**: `2019-12-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.qfcra.com/wp-content/uploads/2022/07/QFC-VASPS-ALERT-pdf.pdf>
  - Wayback: <https://web.archive.org/web/20250215180029id_/https://www.qfcra.com/wp-content/uploads/2022/07/QFC-VASPS-ALERT-pdf.pdf>
  - body_hash: `sha256:0ca883a722644025bc4a119a3fc8dbf036fdade33c9eb169714dbec3f1912d57`
  - body_path: `sources/http_captures/qatar-qcb-qfcra-virtual-asset-ban-2019-12/primary/web.archive.org__web-20250215180029id_-https-www.qfcra.com-wp-content-uploads-2022-07-QFC-VASPS-ALERT-pdf.pdf__6d8181e270.bin`
  > QFC Regulatory Authority official ALERT "QFC Regulatory Authority affirms
> that Virtual Asset Services may not be conducted in or from the QFC",
> dated "Doha, Qatar, 26 December 2019" (PDF text). Verbatim: "the
> Regulatory Authority is issuing this email alert to affirm that Virtual
> Asset Services may not be conducted in or from the QFC at this time" and
> "all Authorised Firms ... are not currently permitted to provide and/or
> facilitate the provision of Virtual Asset Services or otherwise exchange,
> trade or deal in Virtual Assets, until further notice." Banned services
> enumerated: exchange between virtual assets and fiat; exchange between
> forms of virtual assets; transfer; safekeeping/administration; and
> participation in financial services related to a virtual-asset offering.
> Carve-out for digital securities/financial instruments regulated by the
> QFCRA, Qatar Central Bank, or Qatar Financial Markets Authority. Penalties
> per QFC Law No. 7 of 2005.
- **`supporting_journalism`**
  - URL: <https://www.theblock.co/linked/52087/qatar-bans-crypto-trading-report>
  - Wayback: <https://web.archive.org/web/20240620125924/https://www.theblock.co/linked/52087/qatar-bans-crypto-trading-report>
  - body_hash: `sha256:269f59abca981420c4c8fc13b9a862a09a57b52b6f84309e8325b33bf091f75e`
  - body_path: `sources/http_captures/qatar-qcb-qfcra-virtual-asset-ban-2019-12/primary/web.archive.org__web-20240620125924-https-www.theblock.co-linked-52087-qatar-bans-crypto-trading-report__33e30814aa.html`
  > The Block "Qatar Financial Centre bans crypto trading, confirms its
> regulator" (datePublished 2020-01-06) reporting the QFCRA QFC virtual-asset
> services prohibition. Contemporaneous journalism anchor.
- **`semi_primary_wayback`**
  - URL: <https://blogs.loc.gov/law/2025/01/regulation-of-cryptocurrencies-in-the-gulf-cooperation-council-gcc-countries-part-two/>
  - Wayback: <https://web.archive.org/web/20260111122810/https://blogs.loc.gov/law/2025/01/regulation-of-cryptocurrencies-in-the-gulf-cooperation-council-gcc-countries-part-two/>
  - body_hash: `sha256:24e4f1c4f40f88a3e5403432b9cfebdfbcb275cf2c926fbdabd83808dae521b4`
  - body_path: `sources/http_captures/qatar-qcb-qfcra-virtual-asset-ban-2019-12/primary/web.archive.org__web-20260111000000-https-blogs.loc.gov-law-2025-01-regulation-of-cryptocurrencies-in-the-gulf-cooperation-council-gcc-countries-part-two__4a6aef3133.html`
  > US Library of Congress (In Custodia Legis) GCC crypto-regulation survey,
> Part Two. Captured text: "in December of 2019, the Qatar Financial Centre
> Regulatory Authority (QFCRA) issued an alert prohibiting the conduct of
> virtual asset services within or from the Qatar Financial Centre (QFC).
> Penalties for violators are imposed according to QFC Law No. (7) of 2005."
> Authoritative confirmation of the December-2019 date (corrects the
> candidate-lead 2020-12-26).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: QFC Authorised Firms / VASPs (class)

> Class-level subset: all Authorised Firms and Virtual Asset Service Providers
> conducting (or facilitating) Virtual Asset Services in or from the Qatar
> Financial Centre (QFC) — exchange between virtual assets and fiat, exchange
> between virtual-asset forms, transfer, safekeeping/administration, and
> provision of financial services related to a virtual-asset offering. Excludes
> digital securities/financial instruments regulated by the QFCRA, Qatar Central
> Bank, or Qatar Financial Markets Authority. No address-level enumeration.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `virtual_asset_services_prohibited_in_qfc`

**Timestamp**: `2019-12-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.qfcra.com/wp-content/uploads/2022/07/QFC-VASPS-ALERT-pdf.pdf>
  - Wayback: <https://web.archive.org/web/20250215180029id_/https://www.qfcra.com/wp-content/uploads/2022/07/QFC-VASPS-ALERT-pdf.pdf>
  - body_hash: `sha256:0ca883a722644025bc4a119a3fc8dbf036fdade33c9eb169714dbec3f1912d57`
  - body_path: `sources/http_captures/qatar-qcb-qfcra-virtual-asset-ban-2019-12/primary/web.archive.org__web-20250215180029id_-https-www.qfcra.com-wp-content-uploads-2022-07-QFC-VASPS-ALERT-pdf.pdf__6d8181e270.bin`
  > observed_change at class level: the QFCRA ALERT prohibits all Authorised
> Firms from conducting/facilitating Virtual Asset Services in or from the
> QFC. attribution=plausible — the alert targets the Authorised-Firm /
> VASP class, not enumerated operators (codebook §1.1).
- **`semi_primary_wayback`**
  - URL: <https://blogs.loc.gov/law/2025/01/regulation-of-cryptocurrencies-in-the-gulf-cooperation-council-gcc-countries-part-two/>
  - Wayback: <https://web.archive.org/web/20260111122810/https://blogs.loc.gov/law/2025/01/regulation-of-cryptocurrencies-in-the-gulf-cooperation-council-gcc-countries-part-two/>
  - body_hash: `sha256:24e4f1c4f40f88a3e5403432b9cfebdfbcb275cf2c926fbdabd83808dae521b4`
  - body_path: `sources/http_captures/qatar-qcb-qfcra-virtual-asset-ban-2019-12/primary/web.archive.org__web-20260111000000-https-blogs.loc.gov-law-2025-01-regulation-of-cryptocurrencies-in-the-gulf-cooperation-council-gcc-countries-part-two__4a6aef3133.html`
  > LOC GCC survey confirming the December-2019 QFCRA prohibition and QFC Law
> No. 7 of 2005 penalty basis.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- `egypt-cbe-banking-law-194-prohibition-2020` (not found; no rendered admitted-chain link)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `939a17f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

