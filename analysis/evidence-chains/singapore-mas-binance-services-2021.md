# Evidence chain — `singapore-mas-binance-services-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a888d9d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "MAS's 2021-09-02 Binance.com Investor Alert List / Payment Services Act
> order is retained as an attested-secondary trigger. Binance.com then
> announced Singapore-user restrictions in two replayably captured
> first-party notices: on 2021-09-05 it announced cessation of SGD trading
> pairs, SGD payment options, and Singapore app-store availability effective
> 2021-09-10; on 2021-09-27 it announced that Singapore users would lose
> access to fiat deposits, spot trading, fiat-channel crypto purchases, and
> liquid swap effective 2021-10-26. The row does not claim L0 blocking, L1
> consensus impact, L3 RPC filtering, asset-onchain action, or an
> independently pinned 2022 binance.sg shutdown observation."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `SG_MAS`
- **Timestamp**: `2021-09-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.channelnewsasia.com/business/binanace-mas-payment-services-act-investor-alert-list-2152346>
  - Wayback: <https://web.archive.org/web/20210902120336/https://www.channelnewsasia.com/business/binanace-mas-payment-services-act-investor-alert-list-2152346>
  - body_hash: `sha256:32c4408f99c135d8e334c9330e4a782fa1f8f89467cb7565ef6f70b9f4cdcfb4`
  - body_path: `sources/http_captures/singapore-mas-binance-services-2021/secondary/web.archive.org__web-20210902120336-https-www.channelnewsasia.com-business-binanace-mas-payment-services-act-investor-alert-list-2152346__f038367c14.html`
  > CNA archived 2021-09-02 reports MAS's same-day order that the
> operator of Binance.com stop providing regulated payment services
> to Singapore residents and cease soliciting such business. It also
> reports that MAS placed Binance.com on the Investor Alert List
> because Binance.com was not regulated or licensed in Singapore to
> provide payment services. This is a contemporaneous supporting
> source carrying MAS spokesperson statements; no replayable official
> MAS body artifact is retained in this repair pass, so the event is
> marked evidence_tier=attested_secondary.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance.com (SG cohort)
- **Canonical domains**: `binance.com`

> Binance.com global platform serving Singapore retail customers.
> The MAS IAL listing targets the global Binance.com entity (no
> Singapore-licensed Binance legal entity at the time of listing;
> Binance Asia Services Pte Ltd, the local entity, held an
> in-principle PSA licence application that was later withdrawn
> 2021-12). Target treated as entity-level at the Binance-SG
> cohort.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 72h

**Event label**: `sgd_pairs_payments_and_app_store_removal_announced`

**Timestamp**: `2021-09-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/a38b8ee33ba847f9b91562b8709fe539>
  - Wayback: <https://web.archive.org/web/20210905110009/https://www.binance.com/en/support/announcement/a38b8ee33ba847f9b91562b8709fe539>
  - body_hash: `sha256:b2aa10a72fef66f205df87b9ca97139c5cc2cdb1da614b21705fa62e589f1117`
  - body_path: `sources/http_captures/singapore-mas-binance-services-2021/binance/web.archive.org__web-20210905110009-https-www.binance.com-en-support-announcement-a38b8ee33ba847f9b91562b8709fe539__962711f1fb.html`
  > Binance support announcement archived 2021-09-05 states that
> Binance would cease, in Singapore, SGD trading pairs, SGD payment
> options, and app availability in the Singapore iOS and Google Play
> stores effective 2021-09-10 04:00 UTC. Attribution is plausible
> rather than direct because the announcement cites local-regulatory
> compliance but does not name MAS or the Investor Alert List in the
> retained body text.

### offramp_cex · attribution: `plausible` · Δt = 600h

**Event label**: `regulated_payment_services_access_restriction_announced`

**Timestamp**: `2021-09-27 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/34c6c158d03a4877a4e13cf0927468bc>
  - Wayback: <https://web.archive.org/web/20210927094020/https://www.binance.com/en/support/announcement/34c6c158d03a4877a4e13cf0927468bc>
  - body_hash: `sha256:cb2ec1ee0da10ae36815394bfb5c63cb658de30df521562583c9501d2cc0abcd`
  - body_path: `sources/http_captures/singapore-mas-binance-services-2021/binance/web.archive.org__web-20210927094020-https-www.binance.com-en-support-announcement-34c6c158d03a4877a4e13cf0927468bc__1d7298135a.html`
  > Binance support announcement archived 2021-09-27 states that,
> effective 2021-10-26 04:00 UTC, users in Singapore would not be
> able to access Binance.com functions including fiat deposit
> services, spot trading of cryptocurrencies, cryptocurrency
> purchases through fiat channels, and liquid swap. Attribution is
> plausible because the announcement frames the restriction as
> compliance with local regulation without explicitly naming MAS.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a888d9d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

