# Evidence chain — `uk-hmrc-bitcoin-vat-brief-09-14-2014`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `c3a88e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> HMRC Revenue & Customs Brief 09/14 of 2014-03-03 ("Bitcoin
> and other cryptocurrencies") set HMRC's position that bitcoin
> mining is outside the scope of VAT, that bitcoin-fiat exchange
> transactions and the associated arrangement fees are VAT-exempt,
> and that normal VAT applies to suppliers of goods or services
> sold in exchange for bitcoin valued in sterling at the
> transaction point. The instrument is facilitative rather than
> restrictive; no UK-resident exchange-side cutoff is documented
> in the 180-day post-publication window, so offramp_cex carries
> an observation_kind=observed_no_change row with attribution=none.

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `UK_HMRC`
- **Timestamp**: `2014-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.gov.uk/government/publications/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies>
  - Wayback: <https://web.archive.org/web/20150213042659/https://www.gov.uk/government/publications/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies>
  - body_hash: `sha256:10b1c7cd21bbd80ace15a00ff6ba9917c933293966020a973300d0973422244f`
  - body_path: `sources/http_captures/uk-hmrc-bitcoin-vat-brief-09-14-2014/primary/web.archive.org__web-20150213042659-https-www.gov.uk-government-publications-revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies-revenue-and-customs-bri__c23be9b633.html`
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-17 (Wave 2.3 P2)**:
> authored by LLM agent without personally verifying
> Wayback/body_hash; origin=agent_draft and status=draft
> pending human review. Real release must replace this DRYRUN
> marker with a human-verified audit after pinning real
> archive anchors.
> 
> HMRC Revenue & Customs Brief 09/14 ("Bitcoin and other
> cryptocurrencies") published 2014-03-03 by HM Revenue &
> Customs setting out HMRC's position on the tax treatment
> of income from and charges in connection with activities
> involving bitcoin and other similar cryptocurrencies,
> specifically for VAT, Corporation Tax, Income Tax, and
> Capital Gains Tax. Key VAT positions: (i) income from
> bitcoin mining is generally outside the scope of VAT
> because mining is not an economic activity for VAT
> purposes (insufficient link between services provided and
> consideration received); (ii) when bitcoin is exchanged
> for sterling or foreign currencies, no VAT is due on the
> value of the bitcoins themselves, and exchange-side fees
> for arranging or carrying out such transactions are also
> VAT-exempt; (iii) VAT applies in the normal way to
> suppliers of goods or services sold in exchange for
> bitcoin, with the supply valued in sterling at the
> transaction point. HMRC framed the VAT guidance as
> provisional pending further EU regulatory development;
> the position was subsequently aligned with the CJEU's
> 2015-10-22 Hedqvist judgment (C-264/14) treating bitcoin
> exchange as a VAT-exempt financial-services transaction.
- **`supporting_journalism`**
  - URL: <https://www.taxjournal.com/articles/hmrc-issues-guidance-bitcoin-06032014>
  - Wayback: <https://web.archive.org/web/2014/https://www.taxjournal.com/articles/hmrc-issues-guidance-bitcoin-06032014>
  > Tax Journal 2014-03-06 contemporaneous summary "HMRC
> issues guidance on bitcoin", corroborating the 2014-03-03
> publication date and the VAT-exemption framing for
> bitcoin-fiat exchange transactions. evidence_use=
> contextual_unarchived; Wayback snapshot requires
> re-pinning during human audit.
- **`supporting_journalism`**
  - URL: <https://bitcoinmagazine.com/business/hmrc-bitcoin-1394563237>
  - Wayback: <https://web.archive.org/web/2014/https://bitcoinmagazine.com/business/hmrc-bitcoin-1394563237>
  > Bitcoin Magazine 2014-03 report "HMRC Publicize Pro
> Bitcoin Stance", contemporaneous English-crypto-press
> coverage characterising Brief 09/14 as a favourable
> clarification compared with the 2013 informal HMRC
> position (which had reportedly treated bitcoin trades
> as VAT-bearing single-purpose vouchers). Used as
> corroborating secondary tracker source.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: UK-resident bitcoin / cryptocurrency transacting parties
- **Chains**: `bitcoin`

> Class-level target: UK-resident persons and businesses
> engaged in bitcoin and other cryptocurrency activities for
> UK tax purposes — bitcoin miners, exchange operators
> (bitcoin-fiat exchange services), and suppliers of goods or
> services accepting bitcoin as consideration. The brief
> states a tax-treatment interpretation that applies to the
> entire class of UK-resident cryptocurrency-transacting
> parties under the Value Added Tax Act 1994, the Corporation
> Tax Acts, and the Income / Capital Gains Tax framework.
> No specific exchange or miner is named as a target;
> canonical_domains is empty. Class-level subset framing
> matches the sibling bangladesh-bb-bitcoin-warning-2014 and
> iceland-cbi-foreign-exchange-bitcoin-2014 treatment.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_measured_exchange_side_cutoff_of_uk_residents_post_hmrc_brief_09_14`

**Window**: `2014-03-03 00:00:00+00:00` → `2014-08-30 00:00:00+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://www.gov.uk/government/publications/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies>
  - Wayback: <https://web.archive.org/web/20150213042659/https://www.gov.uk/government/publications/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies/revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies>
  - body_hash: `sha256:10b1c7cd21bbd80ace15a00ff6ba9917c933293966020a973300d0973422244f`
  - body_path: `sources/http_captures/uk-hmrc-bitcoin-vat-brief-09-14-2014/primary/web.archive.org__web-20150213042659-https-www.gov.uk-government-publications-revenue-and-customs-brief-9-2014-bitcoin-and-other-cryptocurrencies-revenue-and-customs-bri__c23be9b633.html`
  > gov.uk publication of Revenue & Customs Brief 09/14
> establishes the tax-treatment position (VAT-exempt
> bitcoin-fiat exchange; mining outside scope of VAT;
> normal VAT on goods/services sold for bitcoin). The
> brief is facilitative rather than restrictive — it
> clarifies tax treatment to enable rather than
> constrain UK cryptocurrency activity — and does not
> direct any exchange-side cutoff. observation_kind=
> observed_no_change at offramp_cex because no UK
> exchange is documented as cutting off UK-resident
> accounts within the 180-day window post-publication.
> attribution=none per validator rule for
> observed_no_change. Wayback snapshot requires
> re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://www.taxjournal.com/articles/hmrc-issues-guidance-bitcoin-06032014>
  - Wayback: <https://web.archive.org/web/2014/https://www.taxjournal.com/articles/hmrc-issues-guidance-bitcoin-06032014>
  > Tax Journal 2014-03-06 secondary coverage corroborates
> the VAT-exemption framing and the 2014-03-03
> publication date, and characterises the brief as a
> clarifying rather than restrictive instrument. No
> UK-resident exchange cutoff is reported in this or
> contemporaneous coverage. Wayback snapshot requires
> re-pinning in human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eba-virtual-currencies-opinion-eba-op-2014-08`](./eba-virtual-currencies-opinion-eba-op-2014-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c3a88e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

