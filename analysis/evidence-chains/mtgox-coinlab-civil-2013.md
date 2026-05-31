# Evidence chain — `mtgox-coinlab-civil-2013`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `eabcaae` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "CoinLab v. Mt. Gox civil complaint (filed 2013-05-02 in US
> District Court, Western District of Washington, Case
> 2:13-cv-00777-RSL) sought $75M damages for Mt. Gox's breach of
> the November 2012 North American operations agreement. The row
> records observation_kind=observed_no_change + attribution=none at
> offramp_cex over the 11-day window 2013-05-02 to 2013-05-13
> (closing one day before the federal Dwolla seizure
> mtgox-dhs-dwolla-wells-fargo-seizure-2013), because the civil
> filing itself produced no observable USD on/off-ramp change.
> null_event shape; historical-baseline tier; not used in main
> statistical denominators."

## 1. Trigger

- **Type**: `court_civil_order`
- **Actor**: `US_WDWA_COURT`
- **Timestamp**: `2013-05-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2013/05/03/coinlab-sues-mt-gox-in-us-court>
  - Wayback: <https://web.archive.org/web/2013/https://www.coindesk.com/markets/2013/05/03/coinlab-sues-mt-gox-in-us-court>
  > CoinDesk contemporaneous coverage (published 2013-05-03) of the
> CoinLab v. Mt. Gox K.K. complaint filed 2013-05-02 in the US
> District Court for the Western District of Washington
> (Case 2:13-cv-00777-RSL). $75M breach-of-contract claim over
> Mt. Gox's failure to perform under the November 2012 agreement
> granting CoinLab the exclusive right to handle North American
> bitcoin-exchange services. PACER docket is the canonical
> primary; PACER access requires login, so contemporaneous press
> coverage is used as supporting_journalism. evidence_use=
> contextual_unarchived: no body_hash captured in this session.
- **`supporting_journalism`**
  - URL: <https://www.geekwire.com/2013/bitcoin-seattles-coinlab-files-75m-suit-mt-gox-exchange-alleges-breach-contract/>
  - Wayback: <https://web.archive.org/web/20130503183139/https://www.geekwire.com/2013/bitcoin-seattles-coinlab-files-75m-suit-mt-gox-exchange-alleges-breach-contract/>
  - body_hash: `sha256:933a8dfbda5c69a6e360e62eb9d987d8a4d5319448f0ce9afaff2aeca83af52b`
  - body_path: `sources/http_captures/mtgox-coinlab-civil-2013/primary/web.archive.org__web-20130503183139-https-www.geekwire.com-2013-bitcoin-seattles-coinlab-files-75m-suit-mt-gox-exchange-alleges-breach-contract__6f0a7d3206.html`
  > GeekWire 2013-05-02 coverage from Seattle-local reporting,
> corroborating the filing date, the $75M damages figure, and
> the Western District of Washington venue. CoinLab CEO Peter
> Vessenes quoted on the breach. evidence_use=
> contextual_unarchived: no body_hash captured in this session.
- **`supporting_journalism`**
  - URL: <https://dockets.justia.com/docket/washington/wawdce/2:2013cv00777/192566>
  - Wayback: <https://web.archive.org/web/2013/https://dockets.justia.com/docket/washington/wawdce/2:2013cv00777/192566>
  > Justia docket landing page for Case 2:13-cv-00777-RSL,
> confirming the court (US District Court, Western District of
> Washington), filing date (2013-05-02), nature of suit
> (contract), and the parties (CoinLab, Inc. v. Mt. Gox K.K.
> et al.). Used as a structured-metadata pointer to the PACER
> docket. evidence_use=contextual_unarchived: no body_hash
> captured in this session.
- **`primary_legal`**
  - URL: <https://www.courtlistener.com/docket/4537232/coinlab-inc-v-mt-gox-kk/>
  - Wayback: <https://web.archive.org/web/20201111201503/https://www.courtlistener.com/docket/4537232/coinlab-inc-v-mt-gox-kk/>
  - body_hash: `sha256:eaf5dfdb9c50980f42fa1394af53b596019b18b776a3ac0476f1687ed107fa13`
  - body_path: `sources/http_captures/mtgox-coinlab-civil-2013/primary/web.archive.org__web-20201111201503-https-www.courtlistener.com-docket-4537232-coinlab-inc-v-mt-gox-kk__24b8aee1e8.html`
  > CourtListener public docket page for CoinLab, Inc. v. Mt. Gox
> K.K. et al., Case 2:13-cv-00777 in the Western District of
> Washington. Per docs/data-sources.md, CourtListener docket
> mirrors are treated as primary_legal pointers when PACER itself
> is not accessible in the public artifact. v0.3 repair note:
> direct body capture returned HTTP 403, so this remains a
> Wayback-anchored docket pointer until human audit can attach a
> PACER/RECAP body artifact.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mt. Gox K.K.
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> Mt. Gox North American user-facing operations (USD on/off-ramp,
> customer service for US/Canada users). The CoinLab suit
> challenged Mt. Gox's failure to delegate these operations to
> CoinLab under the November 2012 partnership agreement that
> granted CoinLab the exclusive right to handle North American
> bitcoin-exchange services. No on-chain BTC addresses are
> enumerated at this event level; the action is a private civil
> breach-of-contract dispute, not an asset freeze.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `civil_breach_of_contract_complaint_filed_no_offramp_change_in_pre_dwolla_window`

**Window**: `2013-05-02 00:00:00+00:00` → `2013-05-13 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.courtlistener.com/docket/4537232/coinlab-inc-v-mt-gox-kk/>
  - Wayback: <https://web.archive.org/web/20201111201503/https://www.courtlistener.com/docket/4537232/coinlab-inc-v-mt-gox-kk/>
  - body_hash: `sha256:eaf5dfdb9c50980f42fa1394af53b596019b18b776a3ac0476f1687ed107fa13`
  - body_path: `sources/http_captures/mtgox-coinlab-civil-2013/primary/web.archive.org__web-20201111201503-https-www.courtlistener.com-docket-4537232-coinlab-inc-v-mt-gox-kk__24b8aee1e8.html`
  > Public federal-docket anchor for the trigger filing and case
> nature. This source supports the bounded null observation by
> anchoring the 2013-05-02 W.D. Wash. civil contract complaint
> rather than an enforcement order, seizure, or injunction.
> The no-change claim remains deliberately narrow: no USD
> on/off-ramp closure is attributed to this civil filing in the
> 11-day window before the separate 2013-05-14 Dwolla seizure.
> Direct capture of CourtListener returned HTTP 403 in v0.3
> repair, so human audit should attach PACER/RECAP/RECAP-backed
> body_hash evidence before promotion.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/markets/2013/05/03/coinlab-sues-mt-gox-in-us-court>
  - Wayback: <https://web.archive.org/web/2013/https://www.coindesk.com/markets/2013/05/03/coinlab-sues-mt-gox-in-us-court>
  > observation_kind=observed_no_change + attribution=none
> because the civil suit sought monetary damages, not
> injunctive relief that would close a USD on/off-ramp; no
> contemporaneous CoinDesk reporting in the 11-day window
> before the 2013-05-14 federal Dwolla seizure documents any
> USD on/off-ramp change attributable to the suit itself.
> The downstream Mt. Gox cascade is attributable to the
> parallel federal Dwolla/Wells Fargo seizure
> (mtgox-dhs-dwolla-wells-fargo-seizure-2013), not to the
> civil complaint. evidence_use=contextual_unarchived: no
> body_hash captured in this session.
- **`supporting_journalism`**
  - URL: <https://www.geekwire.com/2013/bitcoin-seattles-coinlab-files-75m-suit-mt-gox-exchange-alleges-breach-contract/>
  - Wayback: <https://web.archive.org/web/2013/https://www.geekwire.com/2013/bitcoin-seattles-coinlab-files-75m-suit-mt-gox-exchange-alleges-breach-contract/>
  > GeekWire local Seattle reporting corroborating filing date,
> $75M damages figure, and W.D. Wash. venue. Establishes that
> the dispute was a private contract-damages action rather
> than a government-driven offramp closure.
> evidence_use=contextual_unarchived: no body_hash captured
> in this session.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)
- [`mtgox-usd-withdrawal-suspension-2013-06`](./mtgox-usd-withdrawal-suspension-2013-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `eabcaae`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

