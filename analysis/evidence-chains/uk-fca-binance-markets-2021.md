# Evidence chain — `uk-fca-binance-markets-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9494486` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:34:09Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FCA's 2021-06-26 consumer warning and First Supervisory Notice imposed
> immediate requirements on Binance Markets Limited: BML could not undertake
> regulated activity in the UK without prior FCA consent, had to display a
> prescribed notice on www.binance.com and other channels, and had to remove
> live advertising / financial promotions by 2021-06-30. The FCA later
> stated on 2021-08-25 that BML complied with all aspects of the requirements.
> No UK bank payment-rail severance claim is retained in this repaired row."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `UK_FCA`
- **Timestamp**: `2021-06-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/news-stories/consumer-warning-binance-markets-limited-and-binance-group>
  - body_hash: `sha256:4ea9e5b25281b4685156a0f03327d3e86e779e6ed03e2b8176bd4201515c37e9`
  - body_path: `sources/http_captures/uk-fca-binance-markets-2021/primary/www.fca.org.uk__news-news-stories-consumer-warning-binance-markets-limited-and-binance-group__de6cfda4a8.html`
  > UK Financial Conduct Authority (FCA) consumer warning "Consumer
> warning on Binance Markets Limited and the Binance Group" dated
> 2021-06-26. The live FCA page states that Binance Markets Limited is
> not permitted to undertake regulated activity in the UK and links the
> FCA supervisory notice. Captured and pinned with body_hash/body_path
> during the 2026-06-01 source-repair pass.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/publication/supervisory-notices/first-supervisory-notice-binance-markets-limited.pdf>
  - body_hash: `sha256:e31a4e8a06371066cc3057da5bdd8d9ada90706b5f515b92a8144e18b65d2b07`
  - body_path: `sources/http_captures/uk-fca-binance-markets-2021/primary/www.fca.org.uk__publication-supervisory-notices-first-supervisory-notice-binance-markets-limited.pdf__0e4475627e.bin`
  > FCA First Supervisory Notice to Binance Markets Limited, dated
> 2021-06-25. The notice imposed immediate requirements under FSMA,
> including a prohibition on BML carrying out regulated activities
> without prior FCA consent and a requirement to display a prescribed
> notice on www.binance.com and other communication channels by
> 2021-06-30. Captured and pinned with body_hash/body_path during the
> 2026-06-01 source-repair pass.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Markets Limited (UK)
- **Canonical domains**: `binance.com`

> Binance Markets Limited (the UK FCA-authorised entity of the Binance
> group) and the Binance communication surfaces named in the FCA First
> Supervisory Notice. The public claim is intentionally scoped to the FCA's
> regulated-activity prohibition and required customer-facing notice/removal
> steps; UK bank payment-rail cascades are not retained without replayable
> bank-side primary evidence.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 1440h

**Event label**: `bml_regulated_business_restriction_remained_in_place`

**Timestamp**: `2021-08-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/publication/supervisory-notices/first-supervisory-notice-binance-markets-limited.pdf>
  - body_hash: `sha256:e31a4e8a06371066cc3057da5bdd8d9ada90706b5f515b92a8144e18b65d2b07`
  - body_path: `sources/http_captures/uk-fca-binance-markets-2021/primary/www.fca.org.uk__publication-supervisory-notices-first-supervisory-notice-binance-markets-limited.pdf__0e4475627e.bin`
  > FCA First Supervisory Notice imposed an immediate requirement that
> BML must not carry out any regulated activities for which it had
> Part 4A permission without prior written FCA consent.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/news-stories/consumer-warning-binance-markets-limited-and-binance-group>
  - body_hash: `sha256:4ea9e5b25281b4685156a0f03327d3e86e779e6ed03e2b8176bd4201515c37e9`
  - body_path: `sources/http_captures/uk-fca-binance-markets-2021/primary/www.fca.org.uk__news-news-stories-consumer-warning-binance-markets-limited-and-binance-group__de6cfda4a8.html`
  > FCA 2021-08-25 update states that BML complied with all aspects
> of the requirements and that the requirements remained in place,
> with BML still unable to conduct regulated business in the UK.

### l4_frontend · attribution: `direct` · Δt = 1440h

**Event label**: `fca_required_binance_notice_and_promotion_removal_complied`

**Timestamp**: `2021-08-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/publication/supervisory-notices/first-supervisory-notice-binance-markets-limited.pdf>
  - body_hash: `sha256:e31a4e8a06371066cc3057da5bdd8d9ada90706b5f515b92a8144e18b65d2b07`
  - body_path: `sources/http_captures/uk-fca-binance-markets-2021/primary/www.fca.org.uk__publication-supervisory-notices-first-supervisory-notice-binance-markets-limited.pdf__0e4475627e.bin`
  > FCA First Supervisory Notice required BML to display prescribed
> wording on www.binance.com and other communication channels by
> 2021-06-30, remove live advertising and financial promotions by
> the same date, and confirm the steps taken to the FCA.
- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/news-stories/consumer-warning-binance-markets-limited-and-binance-group>
  - body_hash: `sha256:4ea9e5b25281b4685156a0f03327d3e86e779e6ed03e2b8176bd4201515c37e9`
  - body_path: `sources/http_captures/uk-fca-binance-markets-2021/primary/www.fca.org.uk__news-news-stories-consumer-warning-binance-markets-limited-and-binance-group__de6cfda4a8.html`
  > FCA 2021-08-25 update states that BML complied with all aspects
> of the requirements and that the requirements remained in place,
> with BML still unable to conduct regulated business in the UK.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9494486`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

