# Evidence chain — `vietnam-sbv-payment-prohibition-2017-10`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `137626c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-02` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The SBV's 2017-10-28 public statement (per Official Letter 5747/NHNN-PC, 2017-07-21) prohibited
> the issuance, supply and use of bitcoin and similar virtual currencies as a means of
> payment in Vietnam, with administrative fines and possible criminal liability from
> 2018-01-01. Effect carried at offramp_cex (observed_change, direct) at class level;
> no named exchange shutdown or user offboarding is claimed.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `VN_SBV`
- **Timestamp**: `2017-10-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://baochinhphu.vn/nhnn-cam-su-dung-bitcoin-102229280.htm>
  - body_hash: `sha256:0c03b52ce2c8a6f04146c2a9efd7d9581c72d4e8706959a933f7bcc26f3652ef`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/primary-government-v1/baochinhphu.vn__nhnn-cam-su-dung-bitcoin-102229280.htm__0209e3409f.html`
  > Bao Dien tu Chinh phu / Government Electronic Newspaper report
> published 2017-10-28 11:56, stating "Theo Ngan hang Nha nuoc
> Viet Nam" that issuing, supplying, and using bitcoin and similar
> virtual currencies as a means of payment is prohibited in Vietnam.
> The same official-government report cites Decree 101/2012 as
> amended by Decree 80/2016, the illegal-payment-instrument ban,
> administrative fines of 150-200 million VND under Decree 96/2014,
> and possible criminal liability from 2018-01-01 under Criminal
> Code Article 206. The captured body is gzip-encoded; `gzip -cd`
> grep-verified the title, NHNN attribution, prohibition language,
> fine range, and 2018-01-01 criminal-liability language.
- **`primary_government`**
  - URL: <https://www.sbv.gov.vn/w/sbv554224/-/categories/93909>
  - body_hash: `sha256:86c8042e70b51ae658ba950279819ba1697cec0e887d7a30f8088681ace20075`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/primary-government-v1/www.sbv.gov.vn__w-sbv554224---categories-93909__a8d054950b.html`
  > Official State Bank of Vietnam retrospective page captured live
> 2026-06-01. It separately describes Official Letter 5747/NHNN-PC
> dated 2017-07-21 and the 2017-10-28 SBV press statement to press
> agencies, stating that bitcoin and similar virtual currencies are
> not lawful means of payment and that issuing, supplying, and using
> them as a means of payment is prohibited in Vietnam. Local grep
> verified the 5747/NHNN-PC reference, 2017-10-28 press-statement
> reference, and payment-prohibition language.
- **`semi_primary_wayback`**
  - URL: <http://vietnamnews.vn/economy/416480/sbv-says-bitcoin-prohibited-in-viet-nam.html>
  - Wayback: <https://web.archive.org/web/20171101125722/http://vietnamnews.vn/economy/416480/sbv-says-bitcoin-prohibited-in-viet-nam.html>
  - body_hash: `sha256:f6b302500867f8bbb37ddce759ea18cbfedb89f682d4969fa75a5793599286ed`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/primary/web.archive.org__web-20171101125722-http-vietnamnews.vn-economy-416480-sbv-says-bitcoin-prohibited-in-viet-nam.html__f28874fff5.html`
  > Viet Nam News (state news agency), archived 2017-11-01, "SBV says bitcoin
> prohibited in Viet Nam." Contemporaneous report of the State Bank of Vietnam
> (SBV) 2017-10-30 statement that bitcoin and similar virtual currencies are not
> lawful means of payment, and that issuance, supply and use of them as a means
> of payment is prohibited under Decree 101/2012 (as amended by Decree
> 80/2016), with administrative fines of 150-200 million VND under Decree
> 96/2014/ND-CP, effective 2018-01-01; criminal liability possible thereafter.
> The underlying instrument is SBV Official Letter No. 5747/NHNN-PC (2017-07-21).
> body_hash captured 2026-05-31.
- **`supporting_tracker`**
  - URL: <https://freemanlaw.com/cryptocurrency/vietnam/>
  - Wayback: <https://web.archive.org/web/20220629153357/https://freemanlaw.com/cryptocurrency/vietnam/>
  - body_hash: `sha256:86bbc4324109e2f67ce9eb5f9453cf898429ffcee58ef06e363093e458032023`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/tracker/web.archive.org__web-20220629153357-https-freemanlaw.com-cryptocurrency-vietnam__2b7db4010d.html`
  > Freeman Law jurisdiction tracker corroborating that the SBV declared bitcoin
> an unlawful means of payment and that payment use is prohibited with fines.
> Retrospective secondary tracker; body_hash captured 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Vietnamese crypto users / payment providers (class)
- **Chains**: `bitcoin`

> Vietnamese-resident bitcoin/crypto users, merchants and payment-service providers
> as a class. The SBV statement prohibits the issuance, supply and use of bitcoin and
> similar virtual currencies as a means of payment; it does not enumerate specific
> exchanges. Class-level subset framing matches sibling nation-state payment-rail
> prohibition events; canonical_domains is empty.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `bitcoin_payment_use_prohibited_with_fines_by_sbv`

**Timestamp**: `2017-10-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://baochinhphu.vn/nhnn-cam-su-dung-bitcoin-102229280.htm>
  - body_hash: `sha256:0c03b52ce2c8a6f04146c2a9efd7d9581c72d4e8706959a933f7bcc26f3652ef`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/primary-government-v1/baochinhphu.vn__nhnn-cam-su-dung-bitcoin-102229280.htm__0209e3409f.html`
  > Official Government Electronic Newspaper report, 2017-10-28:
> according to the State Bank of Vietnam, issuing, supplying, and
> using bitcoin and similar virtual currencies as a means of payment
> is prohibited in Vietnam. It also states the 150-200 million VND
> administrative fine under Decree 96/2014 and possible criminal
> liability from 2018-01-01. attribution=direct for the class-level
> payment-use prohibition; this row does not claim a named exchange
> shutdown or user offboarding measurement.
- **`primary_government`**
  - URL: <https://www.sbv.gov.vn/w/sbv554224/-/categories/93909>
  - body_hash: `sha256:86c8042e70b51ae658ba950279819ba1697cec0e887d7a30f8088681ace20075`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/primary-government-v1/www.sbv.gov.vn__w-sbv554224---categories-93909__a8d054950b.html`
  > Official SBV retrospective page describing Official Letter
> 5747/NHNN-PC dated 2017-07-21 and the 2017-10-28 press statement
> to press agencies. It corroborates that bitcoin and similar virtual
> currencies were not lawful means of payment and that issuing,
> supplying, and using them as payment was prohibited.
- **`semi_primary_wayback`**
  - URL: <http://vietnamnews.vn/economy/416480/sbv-says-bitcoin-prohibited-in-viet-nam.html>
  - Wayback: <https://web.archive.org/web/20171101125722/http://vietnamnews.vn/economy/416480/sbv-says-bitcoin-prohibited-in-viet-nam.html>
  - body_hash: `sha256:f6b302500867f8bbb37ddce759ea18cbfedb89f682d4969fa75a5793599286ed`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/primary/web.archive.org__web-20171101125722-http-vietnamnews.vn-economy-416480-sbv-says-bitcoin-prohibited-in-viet-nam.html__f28874fff5.html`
  > Viet Nam News 2017-10-30 (archived 2017-11-01): SBV declared bitcoin not a
> lawful means of payment; issuance/supply/use as payment prohibited with
> 150-200 million VND fines from 2018-01-01. Retained as contemporaneous
> state-news corroboration; the official-government and SBV captures above
> now carry the load-bearing admission-grade source contract.
- **`supporting_tracker`**
  - URL: <https://freemanlaw.com/cryptocurrency/vietnam/>
  - Wayback: <https://web.archive.org/web/20220629153357/https://freemanlaw.com/cryptocurrency/vietnam/>
  - body_hash: `sha256:86bbc4324109e2f67ce9eb5f9453cf898429ffcee58ef06e363093e458032023`
  - body_path: `sources/http_captures/vietnam-sbv-payment-prohibition-2017-10/tracker/web.archive.org__web-20220629153357-https-freemanlaw.com-cryptocurrency-vietnam__2b7db4010d.html`
  > Freeman Law tracker corroborating the SBV payment-use prohibition and fines.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nepal-nrb-bitcoin-ban-2017-08`](./nepal-nrb-bitcoin-ban-2017-08.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `137626c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

