# Evidence chain — `augur-v2-us-uk-geofence-2020-07`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `9849c58` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T12:14:39Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> As of this repair pass, primary Augur launch-window artifacts confirm
> generic jurisdictional-compliance disclaimer language but do not
> confirm the previously drafted US/UK Augur v2 frontend geofence; the
> candidate remains a draft coverage_gap pending primary evidence.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `FORECAST_FOUNDATION`
- **Timestamp**: `2020-07-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://augur.net/disclaimer/>
  - Wayback: <https://web.archive.org/web/20200806153113/https://augur.net/disclaimer/>
  - body_hash: `sha256:d4c71248c4e940cf061df9fd99c5da07577c1fe66a69ab9381ac946b0459bc18`
  - body_path: `sources/http_captures/augur-v2-us-uk-geofence-2020-07/v0_3_primary_repair/web.archive.org__web-20200801000000-https-www.augur.net-disclaimer__113e5a0d64.html`
  > Augur Client Disclaimer, archived 2020-08-06 and internally
> dated "Last Updated: July 28th, 2020". This primary corporate
> artifact documents the official Augur v2 client disclaimer:
> Augur is an open-source protocol, users are responsible for
> jurisdictional compliance, and use may be illegal depending on
> jurisdiction and contemplated use. It does not enumerate a
> US/UK frontend geofence.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/tech/2020/07/28/5-years-after-launch-predictions-market-platform-augur-releases-version-2>
  - Wayback: <https://web.archive.org/web/2020/https://www.coindesk.com/tech/2020/07/28/5-years-after-launch-predictions-market-platform-augur-releases-version-2>
  > CoinDesk 2020-07-28 coverage anchors the Augur v2 launch date.
> It is retained only as launch-date context; it does not supply
> primary evidence for a US/UK frontend geofence.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `augur_v2`
- **Actor name**: Forecast Foundation / PM Research Augur v2 client surface
- **Chains**: `ethereum`
- **Canonical domains**: `augur.net`, `predictions.global`

> The prior draft framed the target as US-vantage and UK-vantage
> users of canonical Augur v2 frontends. This repair pass could not
> pin a primary Forecast Foundation / PM Research / Augur client
> artifact that enumerates that country set or an actual geofence.
> The retained target is therefore the candidate canonical-UI
> geofence claim itself, pending source discovery or retirement.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = Noneh

**Event label**: `augur_v2_us_uk_geofence_primary_confirmation_gap`

**Timestamp**: `2020-07-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://augur.net/disclaimer/>
  - Wayback: <https://web.archive.org/web/20200806153113/https://augur.net/disclaimer/>
  - body_hash: `sha256:d4c71248c4e940cf061df9fd99c5da07577c1fe66a69ab9381ac946b0459bc18`
  - body_path: `sources/http_captures/augur-v2-us-uk-geofence-2020-07/v0_3_primary_repair/web.archive.org__web-20200801000000-https-www.augur.net-disclaimer__113e5a0d64.html`
  > Primary corporate repair anchor. The 2020 Augur Client
> Disclaimer supports a conservative coverage_gap: it confirms
> the official client shipped with jurisdictional-compliance
> warnings, but it does not confirm the previous draft's US/UK
> geofence claim. This source is therefore not a positive
> observed_change anchor.
- **`supporting_tracker`**
  - URL: <https://en.wikipedia.org/wiki/Augur_(software)>
  - Wayback: <https://web.archive.org/web/2020/https://en.wikipedia.org/wiki/Augur_(software)>
  > Tertiary source that motivated the original source-discovery
> row. It is retained only to explain why the candidate exists;
> it cannot support a paper observation without a primary Augur
> or replayable measurement anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`polymarket-cftc-geofence-2022-01`](./polymarket-cftc-geofence-2022-01.md)
- [`1inch-us-geofence-2021-09`](./1inch-us-geofence-2021-09.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9849c58`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

