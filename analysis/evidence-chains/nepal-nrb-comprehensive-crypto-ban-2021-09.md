# Evidence chain — `nepal-nrb-comprehensive-crypto-ban-2021-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `f54a8ae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T09:44:11Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-09-09 the Nepal Rastra Bank issued an official notice declaring the
> transaction, usage, and mining of all cryptocurrency illegal in Nepal (subject
> to prosecution under the Foreign Exchange Regulation Act and the Act
> Restricting Investment Abroad), a nation-state comprehensive prohibition
> severing the legal crypto on/off-ramp surface for Nepali residents
> (offramp_cex load-bearing, attribution=plausible). The row does not claim a
> measured ISP-level block, on-chain freeze, or per-exchange withdrawal
> enumeration."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `NP_NRB`
- **Timestamp**: `2021-09-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.nrb.org.np/contents/uploads/2021/09/FXMD-Notice-03-207879-Cryptocurrency.pdf>
  - Wayback: <https://web.archive.org/web/20211018205117id_/https://www.nrb.org.np/contents/uploads/2021/09/FXMD-Notice-03-207879-Cryptocurrency.pdf>
  - body_hash: `sha256:964daea861bc92d42116c37158b9cbbd989671a8c8066d190eb12296c0647b7f`
  - body_path: `sources/http_captures/nepal-nrb-comprehensive-crypto-ban-2021-09/primary/web.archive.org__web-20211001000000id_-https-www.nrb.org.np-contents-uploads-2021-09-FXMD-Notice-03-207879-Cryptocurrency.pdf__1d830a68b4.bin`
  > Official Nepal Rastra Bank (central bank) Foreign Exchange Management
> Department notice "FXMD-Notice-03-2078/79 — Cryptocurrency कारोबार
> गैरकानूनी रहेको सम्बन्धी सूचना" ("Notice that cryptocurrency dealings are
> illegal"), published on the NRB website under 2021/09. Single-page
> Nepali-language PDF; the document is image/scan-based so its body text is
> not machine-extractable, hence specific scope wording is not asserted
> from this file directly — the English-language scope (transaction, usage,
> and mining of cryptocurrency declared illegal) is carried by the
> contemporaneous Himalayan Times report below. This citation anchors the
> existence and date of the official NRB notice. Wayback memento
> 20211018205117 captured 2026-05-31.
- **`semi_primary_wayback`**
  - URL: <https://thehimalayantimes.com/business/nrb-issues-notice-on-cryptocurrency>
  - Wayback: <https://web.archive.org/web/20210910161805/https://thehimalayantimes.com/business/nrb-issues-notice-on-cryptocurrency>
  - body_hash: `sha256:442eb013011dc622a1c94621d9ef30bef6fc2e5ca626a9b0b0e921fd3191cf0d`
  - body_path: `sources/http_captures/nepal-nrb-comprehensive-crypto-ban-2021-09/primary/web.archive.org__web-20210915000000-https-thehimalayantimes.com-business-nrb-issues-notice-on-cryptocurrency__ee4de17895.html`
  > The Himalayan Times (2021-09-10): "Nepal Rastra Bank, the banking sector
> regulator and supervisor, has issued a notice on Thursday warning that
> the transaction, usage and mining of cryptocurrency is illegal in the
> country." Grep-confirmed in captured HTML. Contemporaneous English-
> language report of the 2021-09-09 NRB notice; carries the load-bearing
> scope claim (transaction + usage + mining all declared illegal),
> escalating the 2017 banking/exchange prohibition into a comprehensive
> prohibition. Wayback memento 20210910161805 captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Nepal — NRB comprehensive cryptocurrency prohibition notice

> Class-level target: all persons, firms, companies, institutions and
> agencies inside Nepal (and Nepalis abroad) engaging in cryptocurrency
> transaction, usage, or mining. The NRB notice operates against the activity
> class rather than enumerating named exchanges/wallets; coded subset with the
> class-level rationale per codebook §7. This escalates the 2017 bitcoin/
> exchange prohibition (nepal-nrb-bitcoin-ban-2017-08) to a comprehensive
> prohibition covering trading, usage, and mining of all cryptocurrency.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `nepal_crypto_transaction_usage_mining_declared_illegal_comprehensive`

**Timestamp**: `2021-09-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://thehimalayantimes.com/business/nrb-issues-notice-on-cryptocurrency>
  - Wayback: <https://web.archive.org/web/20210910161805/https://thehimalayantimes.com/business/nrb-issues-notice-on-cryptocurrency>
  - body_hash: `sha256:442eb013011dc622a1c94621d9ef30bef6fc2e5ca626a9b0b0e921fd3191cf0d`
  - body_path: `sources/http_captures/nepal-nrb-comprehensive-crypto-ban-2021-09/primary/web.archive.org__web-20210915000000-https-thehimalayantimes.com-business-nrb-issues-notice-on-cryptocurrency__ee4de17895.html`
  > The Himalayan Times (2021-09-10) reports the NRB 2021-09-09 notice
> declaring transaction, usage and mining of cryptocurrency illegal in
> Nepal. attribution=plausible per codebook §1.5: the prohibition is
> documented in the official NRB notice and contemporaneous press, but
> the load-bearing scope claim is sourced from the English-language
> report (the official NRB PDF is image-only / non-machine-readable) and
> per-event downstream cascade (exchange retreat, ISP blocking) is not
> separately measured in this draft.
- **`primary_government`**
  - URL: <https://www.nrb.org.np/contents/uploads/2021/09/FXMD-Notice-03-207879-Cryptocurrency.pdf>
  - Wayback: <https://web.archive.org/web/20211018205117id_/https://www.nrb.org.np/contents/uploads/2021/09/FXMD-Notice-03-207879-Cryptocurrency.pdf>
  - body_hash: `sha256:964daea861bc92d42116c37158b9cbbd989671a8c8066d190eb12296c0647b7f`
  - body_path: `sources/http_captures/nepal-nrb-comprehensive-crypto-ban-2021-09/primary/web.archive.org__web-20211001000000id_-https-www.nrb.org.np-contents-uploads-2021-09-FXMD-Notice-03-207879-Cryptocurrency.pdf__1d830a68b4.bin`
  > Official NRB FXMD cryptocurrency-illegality notice (PDF) anchoring the
> existence and date of the prohibition. Image-only PDF; no specific
> text claims are asserted from this file beyond its identity as the
> official notice.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nepal-nrb-bitcoin-ban-2017-08`](./nepal-nrb-bitcoin-ban-2017-08.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f54a8ae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

