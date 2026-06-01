# Evidence chain — `sec-shavers-btcst-2013`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `279da6b` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2013-07-23 SEC civil complaint against Trendon T. Shavers and Bitcoin
> Savings and Trust is coded as a single-layer offramp_cex observed_change:
> the SEC filing named BTCST as a Bitcoin-denominated Ponzi-scheme defendant
> and sought injunctive, disgorgement, penalty, and asset-freeze relief. The
> row does not assert frontend, network, RPC, on-chain asset, or separately
> measured post-filing receivership effects."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2013-07-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/complaints/2013/comp-pr2013-132.pdf>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/litigation/complaints/2013/comp-pr2013-132.pdf>
  - body_hash: `sha256:3652979be04509dcaba810af33a6eb31775e4197faef4c9303cd4ea92864a97c`
  - body_path: `sources/http_captures/sec-shavers-btcst-2013/sec-primary/www.sec.gov__litigation-complaints-2013-comp-pr2013-132.pdf__459b31b368.bin`
  > SEC civil complaint filed 2013-07-23 in the U.S. District Court for the
> Eastern District of Texas, Sherman Division, against Trendon T. Shavers
> and Bitcoin Savings and Trust (BTCST). The complaint alleges Shavers
> operated a Bitcoin-denominated Ponzi scheme from approximately 2011
> through 2012, soliciting investors via the Bitcoin Forum under the alias
> "pirateat40" and promising up to 7% weekly interest on Bitcoin deposits.
> BTCST raised approximately 700,000 BTC in investor funds before
> collapsing in August 2012. SOURCE-REPAIRED 2026-06-01: the live SEC PDF
> was captured locally from the redirected SEC file URL and pinned with
> body_hash/body_path. The legacy Wayback year-prefix URL remains only as a
> supplemental historical lookup.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2013-132>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/news/press-release/2013-132>
  - body_hash: `sha256:092f77e56db0d5a273eb9d948fc1fe1b048a746e7d003cf405e3d2748ad2c698`
  - body_path: `sources/http_captures/sec-shavers-btcst-2013/sec-primary/www.sec.gov__news-press-release-2013-132__ce4b503fb8.html`
  > SEC press release 2013-132 ("SEC Charges Texas Man With Running
> Bitcoin-Denominated Ponzi Scheme") announcing the civil complaint
> against Trendon T. Shavers and Bitcoin Savings and Trust. Names the
> E.D. Tex. venue, the 7%/week promised return structure, and the
> approximately 700,000 BTC raised. First major SEC enforcement action
> against a Bitcoin-denominated investment scheme. SOURCE-REPAIRED
> 2026-06-01: the live SEC press-release page was captured locally from the
> redirected SEC newsroom URL and pinned with body_hash/body_path. The
> legacy Wayback year-prefix URL remains only as a supplemental historical
> lookup.

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
  - body_hash: `sha256:3652979be04509dcaba810af33a6eb31775e4197faef4c9303cd4ea92864a97c`
  - body_path: `sources/http_captures/sec-shavers-btcst-2013/sec-primary/www.sec.gov__litigation-complaints-2013-comp-pr2013-132.pdf__459b31b368.bin`
  > SEC civil complaint (E.D. Tex.) is the legal instrument naming
> Trendon T. Shavers and Bitcoin Savings and Trust as defendants
> and seeking injunctive relief, disgorgement, and civil
> penalties for the alleged Bitcoin-denominated Ponzi scheme.
> attribution=direct because the observation event is the SEC civil
> complaint filing itself, not a separately measured post-filing
> receivership outcome. Local body_hash/body_path capture is the
> admission-grade replay anchor; the legacy Wayback year-prefix URL is
> supplemental.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2013-132>
  - Wayback: <https://web.archive.org/web/2013/https://www.sec.gov/news/press-release/2013-132>
  - body_hash: `sha256:092f77e56db0d5a273eb9d948fc1fe1b048a746e7d003cf405e3d2748ad2c698`
  - body_path: `sources/http_captures/sec-shavers-btcst-2013/sec-primary/www.sec.gov__news-press-release-2013-132__ce4b503fb8.html`
  > SEC press release 2013-132 corroborates the complaint filing
> and characterizes the action as the first major SEC enforcement
> against a Bitcoin-denominated investment scheme. Local
> body_hash/body_path capture is the admission-grade replay anchor; the
> legacy Wayback year-prefix URL is supplemental.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`btc-e-doj-2017`](./btc-e-doj-2017.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `279da6b`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

