# Evidence chain — `nepal-nrb-bitcoin-ban-2017-08`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `24d80a4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:03:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Nepal Rastra Bank's 2017-08-13 notice declared all bitcoin transactions illegal under
> the Foreign Exchange (Regulation) Act 1962; on 2017-10-06 the CIB arrested seven
> domestic bitcoin exchange operators, shutting the domestic exchange channel. Effect
> carried at offramp_cex (observed_change, plausible) at class level.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `NP_NRB`
- **Timestamp**: `2017-08-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <http://kathmandupost.ekantipur.com/news/2017-10-06/7-nabbed-for-running-bitcoin-exchange-business.html>
  - Wayback: <https://web.archive.org/web/20171006193823/http://kathmandupost.ekantipur.com/news/2017-10-06/7-nabbed-for-running-bitcoin-exchange-business.html>
  - body_hash: `sha256:88bbe7bbe77a4c9d12c93997c9a14771d17cdc34d9293c4a0f85451722c23163`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary/web.archive.org__web-20171006193823-http-kathmandupost.ekantipur.com-news-2017-10-06-7-nabbed-for-running-bitcoin-exchange-business.html__270840be88.html`
  > The Kathmandu Post, 2017-10-06, "7 nabbed for running bitcoin exchange
> business." Contemporaneous Nepali primary-press report of the Central
> Investigation Bureau (CIB) of Nepal Police arresting seven persons for
> running bitcoin exchange businesses — the first enforcement following the
> Nepal Rastra Bank (NRB) notice dated 2017-08-13 declaring that any kind of
> transaction in bitcoin is illegal in Nepal under Section 12 of the Foreign
> Exchange (Regulation) Act, 1962 and the Nepal Rastra Bank Act, 2002.
> Archived Wayback 2017-10-06; body_hash captured 2026-05-31.
- **`supporting_tracker`**
  - URL: <https://freemanlaw.com/cryptocurrency/nepal/>
  - Wayback: <https://web.archive.org/web/20220127132508/https://freemanlaw.com/cryptocurrency/nepal/>
  - body_hash: `sha256:6d91346a536fb5977bd65163b96302689fba8861bfac9860cebe71a4f38ab586`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/tracker/web.archive.org__web-20220127132508-https-freemanlaw.com-cryptocurrency-nepal__c5e7c8e889.html`
  > Freeman Law jurisdiction tracker corroborating the legal basis: NRB banned
> bitcoin through a notice dated 13 August 2017 pursuant to Section 12 of the
> Foreign Exchange (Regulation) Act, 1962 and the Nepal Rastra Bank Act, 2002,
> declaring all bitcoin transactions illegal. Retrospective secondary tracker;
> body_hash captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Nepali bitcoin users / exchange operators (class)
- **Chains**: `bitcoin`

> Nepali-resident bitcoin users and exchange operators as a class. The NRB notice
> declares all bitcoin transactions illegal under FX-control law; it does not
> enumerate specific exchanges. The CIB arrests targeted seven named operators of
> domestic bitcoin exchange businesses. Class-level subset framing matches the
> sibling bangladesh-bb-bitcoin-warning-2014 treatment; no specific platform
> domain is enumerated, so canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `domestic_bitcoin_exchange_channel_shut_by_nrb_ban_and_cib_arrests`

**Timestamp**: `2017-10-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <http://kathmandupost.ekantipur.com/news/2017-10-06/7-nabbed-for-running-bitcoin-exchange-business.html>
  - Wayback: <https://web.archive.org/web/20171006193823/http://kathmandupost.ekantipur.com/news/2017-10-06/7-nabbed-for-running-bitcoin-exchange-business.html>
  - body_hash: `sha256:88bbe7bbe77a4c9d12c93997c9a14771d17cdc34d9293c4a0f85451722c23163`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary/web.archive.org__web-20171006193823-http-kathmandupost.ekantipur.com-news-2017-10-06-7-nabbed-for-running-bitcoin-exchange-business.html__270840be88.html`
  > Kathmandu Post 2017-10-06: CIB of Nepal Police arrested seven persons for
> running bitcoin exchange businesses, the first enforcement of the NRB
> 2017-08-13 prohibition. attribution=plausible per codebook §1.5 (the
> enforcement is documented in contemporaneous press but the NRB primary
> legal instrument was not captured in this pass).
- **`supporting_tracker`**
  - URL: <https://freemanlaw.com/cryptocurrency/nepal/>
  - Wayback: <https://web.archive.org/web/20220127132508/https://freemanlaw.com/cryptocurrency/nepal/>
  - body_hash: `sha256:6d91346a536fb5977bd65163b96302689fba8861bfac9860cebe71a4f38ab586`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/tracker/web.archive.org__web-20220127132508-https-freemanlaw.com-cryptocurrency-nepal__c5e7c8e889.html`
  > Freeman Law tracker corroborating the FX-Act legal basis and the
> 2017-08-13 notice date.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bangladesh-bb-bitcoin-warning-2014`](./bangladesh-bb-bitcoin-warning-2014.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `24d80a4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

