# Evidence chain — `mtgox-bankruptcy-tokyo-2014`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `60f1d90` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2014-02-28 Mt. Gox K.K. civil-rehabilitation filing at the
> Tokyo District Court permanently closed all Mt. Gox on/off-ramps
> (BTC, JPY, USD, EUR) and replaced the mtgox.com trading UI with
> a wind-down / Rehabilitation-Trustee announcement surface.
> Observational axes at offramp_cex and l4_frontend. Historical-
> baseline tier; not used in 2017+ comparable denominators."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MTGOX_KK`
- **Timestamp**: `2014-02-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
  - Wayback: <https://web.archive.org/web/20140310191411/https://www.mtgox.com/>
  > Mt. Gox official announcement dated 2014-02-28 (English translation):
> "On February 28, 2014, MTGOX submitted an application for the start
> of a procedure of civil rehabilitation at the Tokyo District Court,
> and the application was accepted on the same day." The PDF URL
> https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf is the
> canonical document path (mtgox.com is preserved by Mark Karpeles /
> the Rehabilitation Trustee to publish creditor notices and is still
> serving the file as of 2026-05-16, though the trading site itself
> is dead). The 2014-03-10 Wayback snapshot of the mtgox.com landing
> page is retained here as a closest-pointer replayable anchor; the
> 2014-02-28 announcement PDF itself has no Wayback memento captured
> in this session (Wayback Availability API returned empty for the
> PDF URL on 2026-05-16). evidence_use=contextual_unarchived: no
> body_hash captured this session.
- **`supporting_journalism`**
  - URL: <https://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost>
  - Wayback: <https://web.archive.org/web/20150523223011/http://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost>
  > NPR The Two-Way (2014-02-28): "Mt. Gox Files For Bankruptcy; Nearly
> $500M Of Bitcoins Lost." Contemporary press coverage of the Tokyo
> District Court civil-rehabilitation filing; reports liabilities of
> ~6.5 billion yen (~$64M at the time), ~750k customer BTC + ~100k
> Mt. Gox BTC missing (~7% of all bitcoin at the time, ~$473M).
> Wayback memento 2015-05-23 (closest archived snapshot, since
> Wayback's 2014-02-28..03-01 mementos of this exact URL were not
> located in this session).
- **`supporting_journalism`**
  - URL: <https://www.bloomberg.com/news/articles/2014-02-28/mt-gox-exchange-files-for-bankruptcy>
  - Wayback: <https://web.archive.org/web/20150215092806/http://www.bloomberg.com:80/news/articles/2014-02-28/mt-gox-exchange-files-for-bankruptcy>
  > Bloomberg (2014-02-28): "Mt. Gox Seeks Bankruptcy After $480 Million
> Bitcoin Loss." Documents the news conference at the Tokyo District
> Court at which CEO Mark Karpeles publicly apologized and confirmed
> the civil-rehabilitation (minji saisei) filing. Wayback memento
> 2015-02-15 (closest archived snapshot).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mt. Gox K.K. (MtGox Co., Ltd.)
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> Mt. Gox K.K. (MtGox Co., Ltd.), a Tokyo-incorporated bitcoin exchange
> operator. All Mt. Gox customers globally; ~750k customer BTC and
> ~100k corporate BTC plus customer JPY/USD/EUR balances frozen at
> filing. Mt. Gox was the dominant bitcoin exchange globally with
> ~70% market share at peak (2013). Subset enumeration: customer-set
> headcount and per-jurisdiction breakdown not retained at this row;
> the load-bearing target is the Mt. Gox K.K. corporate entity and
> its single canonical domain mtgox.com.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `all_onramps_offramps_permanently_closed_at_civil_rehabilitation_filing`

**Timestamp**: `2014-02-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
  - Wayback: <https://web.archive.org/web/20140307015258id_/https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
  - body_hash: `sha256:9bbf875466fc1f34b5c3834d8382e918d06a963971c59697b0c0e9c0ef276415`
  - body_path: `sources/http_captures/mtgox-bankruptcy-tokyo-2014/primary/web.archive.org__web-20140301000000id_-https-www.mtgox.com-img-pdf-20140228-announcement_eng.pdf__c6608e8b86.bin`
  > Mt. Gox official 2014-02-28 announcement (English PDF) of the
> Tokyo District Court civil-rehabilitation (bankruptcy) filing and the
> suspension of all transactions / site operations. Operator primary-
> corporate anchor; attribution=direct. Wayback 20140307015258 (raw PDF)
> pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost>
  - Wayback: <https://web.archive.org/web/20150523223011/http://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost>
  - body_hash: `sha256:f74671f0b7ae135a39be88b723c83691687f062c5a8c9e68acaf7ea8f5e9c356`
  - body_path: `sources/http_captures/mtgox-bankruptcy-tokyo-2014/primary/web.archive.org__web-20140301000000-https-www.npr.org-sections-thetwo-way-2014-02-28-283863219-mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost__69254e6f7e.html`
  > NPR 2014-02-28 coverage confirming the bankruptcy filing and the
> ~850k BTC loss. Independent semi-primary anchor.

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `trading_ui_replaced_with_wind_down_notice`

**Timestamp**: `2014-02-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
  - Wayback: <https://web.archive.org/web/20140307015258id_/https://www.mtgox.com/img/pdf/20140228-announcement_eng.pdf>
  - body_hash: `sha256:9bbf875466fc1f34b5c3834d8382e918d06a963971c59697b0c0e9c0ef276415`
  - body_path: `sources/http_captures/mtgox-bankruptcy-tokyo-2014/primary/web.archive.org__web-20140301000000id_-https-www.mtgox.com-img-pdf-20140228-announcement_eng.pdf__c6608e8b86.bin`
  > Mt. Gox official 2014-02-28 announcement (English PDF) of the
> Tokyo District Court civil-rehabilitation (bankruptcy) filing and the
> suspension of all transactions / site operations. Operator primary-
> corporate anchor; attribution=direct. Wayback 20140307015258 (raw PDF)
> pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost>
  - Wayback: <https://web.archive.org/web/20150523223011/http://www.npr.org/sections/thetwo-way/2014/02/28/283863219/mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost>
  - body_hash: `sha256:f74671f0b7ae135a39be88b723c83691687f062c5a8c9e68acaf7ea8f5e9c356`
  - body_path: `sources/http_captures/mtgox-bankruptcy-tokyo-2014/primary/web.archive.org__web-20140301000000-https-www.npr.org-sections-thetwo-way-2014-02-28-283863219-mtgox-files-for-bankruptcy-nearly-500m-of-bitcoins-lost__69254e6f7e.html`
  > NPR 2014-02-28 coverage confirming the bankruptcy filing and the
> ~850k BTC loss. Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`powell-unlicensed-bitcoin-exchange-2014`](./powell-unlicensed-bitcoin-exchange-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `60f1d90`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

