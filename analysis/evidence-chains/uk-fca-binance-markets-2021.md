# Evidence chain — `uk-fca-binance-markets-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-2` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `f8dc941` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-16T12:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FCA consumer warning of 2021-06-26 that Binance Markets Limited is not
> permitted to undertake regulated activity in the UK precipitated a
> class-wide GBP payment-rail severance from major UK retail banks
> (Barclays 2021-07-05, Santander 2021-07-13, others) to Binance over the
> following 8 weeks. Primary observational axis is offramp_cex at the
> UK-Binance cohort level; secondary L4-frontend response (UK-geo
> restriction banners on binance.com/en) attached with plausible
> attribution."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `UK_FCA`
- **Timestamp**: `2021-06-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/news-stories/binance-markets-limited>
  - Wayback: <https://web.archive.org/web/20210626155014/https://www.fca.org.uk/news/news-stories/binance-markets-limited>
  > UK Financial Conduct Authority (FCA) consumer warning "Binance Markets
> Limited" dated 2021-06-26. States that "Binance Markets Limited is not
> permitted to undertake any regulated activity in the UK." Companion
> statement to the FCA's supervisory notice imposing requirements on
> Binance Markets Ltd (the UK FCA-registered Binance entity). DRYRUN
> promotion: replayable Wayback URL is asserted in the FCA news feed;
> body-hash capture deferred to a follow-on pass before non-DRYRUN
> release. Marked contextual_unarchived to flag the unarchived state
> explicitly.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Markets Limited (UK)
- **Canonical domains**: `binance.com`

> Binance Markets Limited (the UK-FCA-registered entity of the Binance group)
> and, by cascade, UK retail customers of the global binance.com platform.
> The FCA notice targets a single legal entity (BML) but its operational
> effect is on the UK Binance customer base via downstream bank payment-rail
> cutoffs. Target treated as entity-level at the Binance-UK cohort.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 216h

**Event label**: `gbp_payment_rails_to_binance_severed_class_wide`

**Timestamp**: `2021-07-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fca.org.uk/news/news-stories/binance-markets-limited>
  - Wayback: <https://web.archive.org/web/20210626155014/https://www.fca.org.uk/news/news-stories/binance-markets-limited>
  > FCA consumer warning is the regulatory anchor. The notice itself
> does not legally compel UK banks to block payment rails, but
> contemporaneous bank statements (Barclays 2021-07-05) cited the
> FCA warning as the reason for the block. attribution=direct at
> the FCA-warning-as-trigger level; bank responses are the
> immediate cascade.
- **`supporting_journalism`**
  - URL: <https://www.ft.com/content/27e91a07-6b35-4e62-a9c4-1bf4d2cf5fff>
  - Wayback: <https://web.archive.org/web/20210706153500/https://www.ft.com/content/27e91a07-6b35-4e62-a9c4-1bf4d2cf5fff>
  > Financial Times "Barclays blocks UK card payments to Binance
> cryptocurrency exchange" (2021-07-05). Documents the first
> major UK retail bank citing the FCA action and blocking card
> payments to Binance. Marked contextual_unarchived for DRYRUN;
> body-hash capture deferred.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/technology/santander-stops-uk-payments-binance-2021-07-13/>
  - Wayback: <https://web.archive.org/web/20210713200000/https://www.reuters.com/technology/santander-stops-uk-payments-binance-2021-07-13/>
  > Reuters report (2021-07-13) on Santander UK halting payments to
> Binance. Second major UK retail bank to act post-FCA notice;
> confirms the class-wide payment-rail severance pattern.

### l4_frontend · attribution: `plausible` · Δt = 24h

**Event label**: `uk_geo_specific_restriction_banners_posted`

**Timestamp**: `2021-06-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/binance-markets-limited-and-the-fca-uk-2bb6f1c121f74ae0a05bbcc4dbf94135>
  - Wayback: <https://web.archive.org/web/20210627000000*/binance.com/en/support/announcement/binance-markets-limited-and-the-fca-uk-2bb6f1c121f74ae0a05bbcc4dbf94135>
  > Binance UK announcement posted on binance.com/en in the days
> after the FCA notice, clarifying that Binance Markets Limited
> was a "separate legal entity" from binance.com and that
> binance.com itself was not subject to the FCA notice.
> Functional UK-customer restrictions followed in subsequent
> months. attribution=plausible because the frontend banner is
> a Binance-corporate response, not a regulator-mandated
> change. DRYRUN: Wayback URL pattern asserted; pinned snapshot
> capture deferred.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-2` (commit `f8dc941`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

