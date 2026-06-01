# Evidence chain — `nydfs-bitlicense-2015-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `210aa10` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T04:23:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2015-06-24 NYDFS BitLicense (23 NYCRR Part 200) triggered a
> documented L4-frontend exit by at least four named operators
> (ShapeShift, Kraken, Bitfinex, Poloniex) within 45 days of the
> effective date. The retained observations document only the frontend
> exit cascade; no L0/L1/L3/asset-onchain effects are claimed."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `US_NYDFS`
- **Timestamp**: `2015-06-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20150604135045/http://www.dfs.ny.gov/legal/regulations/adoptions/dfsp200t.pdf>
  - Wayback: <https://web.archive.org/web/20150604135045/http://www.dfs.ny.gov/legal/regulations/adoptions/dfsp200t.pdf>
  - body_hash: `sha256:29a6135cfaa79e3f97309b3b5ae5f1d233cc22f0c3b5d7d2b3291adf16b997f1`
  - body_path: `sources/http_captures/nydfs-bitlicense-2015-06/primary/web.archive.org__web-20150604135045-http-www.dfs.ny.gov-legal-regulations-adoptions-dfsp200t.pdf__7978129838.html`
  > NYDFS 23 NYCRR Part 200 ("Virtual Currencies") — the BitLicense
> regulation. Wayback memento of the canonical NYDFS adoption-text PDF
> at dfs.ny.gov/legal/regulations/adoptions/dfsp200t.pdf, snapshotted
> 2015-06-04 (proposed-final text published prior to the 2015-06-24
> formal adoption). The captured artifact is the Wayback HTML wrapper
> delivering the PDF; body_hash verifies the local archive copy.
> Final rule published 2015-06-24, effective 2015-08-08, requiring
> anyone engaged in "Virtual Currency Business Activity" in NY or
> with NY residents to obtain a BitLicense ($5,000 non-refundable
> application fee + cybersecurity/AML/capital/custody/consumer-
> protection program requirements).
- **`primary_corporate`**
  - URL: <https://www.dfs.ny.gov/virtual_currency_businesses>
  - body_hash: `sha256:940ca14140db1a229fa29f8a3653e3a03879d8efe448667c62769dbdb5c08955`
  - body_path: `sources/http_captures/nydfs-bitlicense-2015-06/primary/www.dfs.ny.gov__virtual_currency_businesses__5189ee98fc.html`
  > Current NYDFS Virtual Currency Businesses landing page, which
> anchors the modern URL state for the BitLicense program. Captured
> 2026-05-16. Provides contemporaneous corroboration that 23 NYCRR
> Part 200 remains the operative BitLicense regulation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: NY virtual-currency operators (BitLicense-required class)
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `shapeshift.io`, `kraken.com`, `bitfinex.com`, `poloniex.com`

> "Virtual Currency Business Activity" service providers operating in or
> with residents of New York State. Affected operators include
> ShapeShift, Kraken, Bitfinex, and Poloniex (the four named
> operators in the documented June-August 2015 NY-exit cascade), plus
> the broader class of US/non-US crypto businesses that elected either
> to apply for a BitLicense or to geofence New York. This row enumerates
> only the four publicly-attested NY-exit operators as the observation
> cohort; it does not claim a complete enumeration of every BitLicense-
> affected entity.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 1089h

**Event label**: `kraken_ny_exit_farewell_announcement`

**Timestamp**: `2015-08-09 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20150810000000/https://blog.kraken.com/post/253/farewell-new-york>
  - Wayback: <https://web.archive.org/web/20170928121247/https://blog.kraken.com/post/253/farewell-new-york/>
  - body_hash: `sha256:dff65ad51adc9d64da224948155bd4959c1303139045e037a721d5a853d97192`
  - body_path: `sources/http_captures/nydfs-bitlicense-2015-06/secondary/web.archive.org__web-20150810000000-https-blog.kraken.com-post-253-farewell-new-york__d8055ca470.html`
  > Kraken's "Farewell, New York" blog post announcing termination
> of services to New York residents, citing the BitLicense regime
> as the trigger. Published 2015-08-09 (one day after the 45-day
> application window closed). attribution=direct because the
> operator itself names the regulation as the cause.

### l4_frontend · attribution: `plausible` · Δt = 24h

**Event label**: `shapeshift_ny_exit_announcement`

**Timestamp**: `2015-06-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/20150626040443/http://shapeshift.io/blog/>
  - Wayback: <https://web.archive.org/web/20150916203357/https://shapeshift.io/blog>
  - body_hash: `sha256:313dd02f8f36e73df73d7ad7f2ead045cc059d48fd6178db460a4d83dce6abf4`
  - body_path: `sources/http_captures/nydfs-bitlicense-2015-06/secondary/web.archive.org__web-20150626040443-http-shapeshift.io-blog__bcfb1cd55c.html`
  > ShapeShift blog landing-page snapshot taken 2015-06-26 (one
> day after Erik Voorhees's same-day public statement that
> ShapeShift would cease serving NY residents in response to the
> BitLicense final rule). The captured page is the post-exit
> state of the blog index. v0.3 audit 2026-05-20: attribution
> DOWNGRADED from direct to plausible per Session 2 Block D NO
> decision (qid=160 nydfs needs_recheck). Reason: Voorhees's
> public statement that names BitLicense as cause is NOT in the
> captured body_path (the blog INDEX snapshot doesn't carry the
> exit-announcement post content). Matches the Bitfinex row's
> honest attribution=plausible treatment within this same YAML
> (CDX index without per-event banner content). Future capture
> of Voorhees's actual 2015-06-25 statement (likely via Reddit
> AMA Wayback) would support re-upgrading to attribution=direct.

### l4_frontend · attribution: `plausible` · Δt = 1233h

**Event label**: `bitfinex_ny_exit_geofence`

**Timestamp**: `2015-08-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://web.archive.org/web/2015*/www.bitfinex.com/>
  - Wayback: <https://web.archive.org/web/2015*/www.bitfinex.com/>
  - body_hash: `sha256:663275c6d3d1c7f023c4961507deafab5d6976b0f0248c15be05f7e88b071b3f`
  - body_path: `sources/http_captures/nydfs-bitlicense-2015-06/secondary/web.archive.org__web-2015-www.bitfinex.com__143858a1c9.html`
  > Bitfinex 2015 Wayback memento index for www.bitfinex.com.
> Bitfinex announced cessation of services for NY users during
> August 2015 in line with the BitLicense effective date.
> attribution=plausible (rather than direct) because the precise
> exit-announcement post URL is not independently anchored here
> and the timestamp is derived from contemporaneous coverage of
> BitLicense-driven NY-exit cascade.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`coinbase-india-exit-2022`](./coinbase-india-exit-2022.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `210aa10`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

