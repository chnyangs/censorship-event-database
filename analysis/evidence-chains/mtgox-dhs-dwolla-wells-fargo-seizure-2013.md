# Evidence chain — `mtgox-dhs-dwolla-wells-fargo-seizure-2013`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `b71c00e` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:15:30Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2013-05-14 DHS/HSI seizure of Mt. Gox subsidiary Mutum Sigillum's
> Dwolla account at Veridian Credit Union (paired with the 2013-05-09
> Wells Fargo seizure) closed Mt. Gox's primary USD on-ramp to US customers;
> the row claims only this single-layer offramp_cex fiat-rail closure
> observation and does not assert frontend, network, RPC, or on-chain BTC
> effects. Historical-baseline tier; not used in main statistical
> denominators."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DHS_HSI`
- **Timestamp**: `2013-05-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-md>
  - Wayback: <https://web.archive.org/web/20150228114134/http://www.justice.gov:80/usao-md>
  > US Attorney's Office, District of Maryland — the prosecuting office of
> record for the 2013-05-14 seizure warrant against Mt. Gox subsidiary
> Mutum Sigillum LLC's Dwolla account (Case 1:13-mc-01162-WMN, signed by
> US Magistrate Judge Susan K. Gauvey on affidavit of a Homeland Security
> Investigations special agent). No archived 2013 press-release URL for
> this specific seizure was located on justice.gov; the office-of-record
> landing page is retained as a contextual pointer. evidence_use=
> contextual_unarchived: no body_hash captured in this session, and the
> original 2013 warrant PDF is not exposed via a stable justice.gov URL.
- **`supporting_journalism`**
  - URL: <https://techcrunch.com/2013/05/16/mt-gox-dwolla-account-money-seizure/>
  - Wayback: <https://web.archive.org/web/20140102083717/http://techcrunch.com/2013/05/16/mt-gox-dwolla-account-money-seizure/>
  - body_hash: `sha256:630176609b63ac524ce6aaa15b87fc0c02c97fde3bd34c10a80090a18e5001c6`
  - body_path: `sources/http_captures/mtgox-dhs-dwolla-wells-fargo-seizure-2013/primary/web.archive.org__web-20140102083717-http-techcrunch.com-2013-05-16-mt-gox-dwolla-account-money-seizure__401e53cca3.html`
  > Contemporary TechCrunch coverage (2013-05-16) reporting that ICE/HSI
> had obtained a copy of the seizure warrant and confirming the basis
> of the action: Mt. Gox/Mutum Sigillum operating an unlicensed money-
> transmitting business in violation of 18 U.S.C. § 1960. Wayback memento
> 2014-01-02 captured 2026-05-20.
- **`supporting_journalism`**
  - URL: <https://thegenesisblock.com/warrant-for-mt-gox-wells-fargo-accounts-shows-additional-2-1m-seized/>
  - Wayback: <https://web.archive.org/web/20131230204444/http://thegenesisblock.com/warrant-for-mt-gox-wells-fargo-accounts-shows-additional-2-1m-seized/>
  - body_hash: `sha256:a9ff47d61214f84812f890451fbc9d2f556f35db02771eeb32a47f7e1edda915`
  - body_path: `sources/http_captures/mtgox-dhs-dwolla-wells-fargo-seizure-2013/primary/web.archive.org__web-20131230204444-http-thegenesisblock.com-warrant-for-mt-gox-wells-fargo-accounts-shows-additional-2-1m-seized__3a89a00d8b.html`
  > Genesis Block reporting on the follow-on 2013-06 Wells Fargo seizure
> warrant that brought the total seized from Mutum Sigillum / Mt. Gox
> US-vantage accounts to ~$5M. Wayback memento 2013-12-30 captured
> 2026-05-20.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mutum Sigillum LLC (Mt. Gox US subsidiary)
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> Mt. Gox US subsidiary Mutum Sigillum LLC, plus its Dwolla account (held in
> custody at Veridian Credit Union) and the predicate Wells Fargo Bank
> account opened 2011-05-20 by Mt. Gox CEO Mark Karpeles. Together these
> constituted Mt. Gox's primary USD on-ramp/off-ramp infrastructure for US
> customers in 2013. No on-chain BTC addresses are enumerated at this event
> level; the action is a fiat-rail account seizure, not a crypto-asset
> freeze.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `usd_onramp_closed_via_dwolla_account_seizure`

**Timestamp**: `2013-05-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-md>
  - Wayback: <https://web.archive.org/web/20150228114134/http://www.justice.gov:80/usao-md>
  > Direct attribution: the 2013-05-14 seizure warrant (Case 1:13-mc-
> 01162-WMN, D. Md.) explicitly named the Mutum Sigillum Dwolla
> account that constituted Mt. Gox's primary US-customer USD on-ramp.
> The action closed that rail. evidence_use=contextual_unarchived
> because the original warrant PDF is not exposed via a stable
> justice.gov URL and no body_hash was captured into
> sources/http_captures/ in this session.
- **`supporting_journalism`**
  - URL: <https://techcrunch.com/2013/05/16/mt-gox-dwolla-account-money-seizure/>
  - Wayback: <https://web.archive.org/web/20140102083717/http://techcrunch.com/2013/05/16/mt-gox-dwolla-account-money-seizure/>
  - body_hash: `sha256:630176609b63ac524ce6aaa15b87fc0c02c97fde3bd34c10a80090a18e5001c6`
  - body_path: `sources/http_captures/mtgox-dhs-dwolla-wells-fargo-seizure-2013/primary/web.archive.org__web-20140102083717-http-techcrunch.com-2013-05-16-mt-gox-dwolla-account-money-seizure__401e53cca3.html`
  > Contemporary corroboration that ICE/HSI obtained and acted on the
> warrant within 48 hours of issue. Establishes the operational
> timing of the USD on-ramp closure as direct rather than delayed.
> Wayback memento 2014-01-02 captured 2026-05-20.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)
- [`sec-shavers-btcst-2013`](./sec-shavers-btcst-2013.md)
- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`powell-unlicensed-bitcoin-exchange-2014`](./powell-unlicensed-bitcoin-exchange-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b71c00e`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

