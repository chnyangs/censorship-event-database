# Evidence chain — `nepal-nrb-bitcoin-ban-2017-08`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `47f4858` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T14:27:22Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Nepal Rastra Bank's 2017-08-13 notice declared Bitcoin-related transactions illegal
> in Nepal under the central-bank and foreign-exchange legal framework; on 2017-10-06
> the CIB arrested seven domestic bitcoin exchange operators in the first captured
> downstream enforcement report. Effect carried at offramp_cex (observed_change,
> direct) at class level.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `NP_NRB`
- **Timestamp**: `2017-08-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.nrb.org.np/contents/uploads/2019/12/BitcoinNotice.pdf>
  - Wayback: <https://web.archive.org/web/20190628001730id_/https://nrb.org.np/fxm/notices/BitcoinNotice.pdf>
  - body_hash: `sha256:078c0b471d4f1588e31658a7c2e155aa90033ed586c05cdc4f9b8b2d6afb4721`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary-nrb-bitcoin-notice-live/www.nrb.org.np__contents-uploads-2019-12-BitcoinNotice.pdf__de5bdd24e0.bin`
  > Nepal Rastra Bank (Foreign Exchange Management Department) Bitcoin notice,
> captured from the migrated official NRB PDF path. Rendered PDF verifies the
> NRB seal/header, notice title, legal-basis references to the Nepal Rastra Bank
> Act and Foreign Exchange Act, and the operative instruction that Bitcoin-related
> transactions in Nepal are completely illegal and should not be conducted. The
> same PDF body is also pinned as a raw Wayback memento of the legacy NRB URL
> below (identical sha256).
- **`primary_government`**
  - URL: <https://nrb.org.np/fxm/notices/BitcoinNotice.pdf>
  - Wayback: <https://web.archive.org/web/20190628001730id_/https://nrb.org.np/fxm/notices/BitcoinNotice.pdf>
  - body_hash: `sha256:078c0b471d4f1588e31658a7c2e155aa90033ed586c05cdc4f9b8b2d6afb4721`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary-nrb-bitcoin-notice-wayback-2019-raw/web.archive.org__web-20190628001730id_-https-nrb.org.np-fxm-notices-BitcoinNotice.pdf__2489834dfd.bin`
  > Raw Wayback capture of the legacy NRB PDF URL, archived 2019-06-28. The body
> hash matches the current migrated NRB-hosted PDF exactly, giving a durable
> replayable primary-government anchor if the live URL later drifts.
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

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `domestic_bitcoin_exchange_channel_shut_by_nrb_ban_and_cib_arrests`

**Timestamp**: `2017-08-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.nrb.org.np/contents/uploads/2019/12/BitcoinNotice.pdf>
  - Wayback: <https://web.archive.org/web/20190628001730id_/https://nrb.org.np/fxm/notices/BitcoinNotice.pdf>
  - body_hash: `sha256:078c0b471d4f1588e31658a7c2e155aa90033ed586c05cdc4f9b8b2d6afb4721`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary-nrb-bitcoin-notice-live/www.nrb.org.np__contents-uploads-2019-12-BitcoinNotice.pdf__de5bdd24e0.bin`
  > Official NRB notice declaring Bitcoin-related transactions in Nepal illegal
> and instructing the public not to conduct or cause such transactions. This
> primary-government source carries attribution=direct for the class-level
> offramp/exchange-surface restriction.
- **`primary_government`**
  - URL: <https://nrb.org.np/fxm/notices/BitcoinNotice.pdf>
  - Wayback: <https://web.archive.org/web/20190628001730id_/https://nrb.org.np/fxm/notices/BitcoinNotice.pdf>
  - body_hash: `sha256:078c0b471d4f1588e31658a7c2e155aa90033ed586c05cdc4f9b8b2d6afb4721`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary-nrb-bitcoin-notice-wayback-2019-raw/web.archive.org__web-20190628001730id_-https-nrb.org.np-fxm-notices-BitcoinNotice.pdf__2489834dfd.bin`
  > Raw Wayback replay of the same official NRB notice PDF from the legacy URL;
> same sha256 as the migrated live NRB-hosted copy.
- **`semi_primary_wayback`**
  - URL: <http://kathmandupost.ekantipur.com/news/2017-10-06/7-nabbed-for-running-bitcoin-exchange-business.html>
  - Wayback: <https://web.archive.org/web/20171006193823/http://kathmandupost.ekantipur.com/news/2017-10-06/7-nabbed-for-running-bitcoin-exchange-business.html>
  - body_hash: `sha256:88bbe7bbe77a4c9d12c93997c9a14771d17cdc34d9293c4a0f85451722c23163`
  - body_path: `sources/http_captures/nepal-nrb-bitcoin-ban-2017-08/primary/web.archive.org__web-20171006193823-http-kathmandupost.ekantipur.com-news-2017-10-06-7-nabbed-for-running-bitcoin-exchange-business.html__270840be88.html`
  > Kathmandu Post 2017-10-06: CIB of Nepal Police arrested seven persons for
> running bitcoin exchange businesses, the first captured downstream
> enforcement report following the NRB 2017-08-13 prohibition. Retained as
> enforcement-context corroboration; the load-bearing attribution is the NRB
> primary notice above.
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

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `47f4858`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

