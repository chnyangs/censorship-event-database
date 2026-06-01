# Evidence chain — `coinbase-irs-john-doe-summons-2016`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `2bea37a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:12:12Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2016-11-17 DOJ-Tax-Division petition for an IRS John Doe summons
> against Coinbase (authorized by N.D. Cal. on 2016-11-30) is admitted
> only for the next-day published platform petition-opposition disclosure
> by Coinbase as a US-regulated centralized exchange; the dataset does
> not claim any on-chain freeze, frontend takedown, fiat-rail disruption,
> or post-2017 narrowed-order record production at this event level."

## 1. Trigger

- **Type**: `court_civil_order`
- **Actor**: `US_DISTRICT_COURT_ND_CAL_IRS`
- **Timestamp**: `2016-11-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/court-authorizes-service-john-doe-summons-seeking-identities-us-taxpayers-who-have-used>
  - Wayback: <https://web.archive.org/web/20161130232748/https://www.justice.gov/opa/pr/court-authorizes-service-john-doe-summons-seeking-identities-us-taxpayers-who-have-used>
  - body_hash: `sha256:56a6392a45575f333467a199dcaa15db3a743f787022d6b6648fc84d4b19e335`
  - body_path: `sources/http_captures/coinbase-irs-john-doe-summons-2016/primary/web.archive.org__web-20161130232748-https-www.justice.gov-opa-pr-court-authorizes-service-john-doe-summons-seeking-identities-us-taxpayers-who-have-used__4d794ca699.html`
  > DOJ Office of Public Affairs press release dated 2016-11-30 announcing
> that a federal court in the Northern District of California, on the
> DOJ Tax Division's petition, authorized the IRS to serve a John Doe
> summons on Coinbase Inc. seeking records of all U.S. taxpayers who
> conducted convertible-virtual-currency transactions through Coinbase
> during 2013–2015. Petition was filed in N.D. Cal. on 2016-11-17 (one
> day before Coinbase's 2016-11-18 public petition-opposition blog
> post, which describes it as filed "yesterday"); the court authorized
> service on 2016-11-30. The Wayback memento from 2016-11-30 is the
> admission anchor for the press-release text. The original Wayback
> memento date is also the earliest available memento of this URL per
> the Wayback Timemap, and predates the modern justice.gov redirect to
> /archives/opa/.
- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/court-authorizes-service-john-doe-summons-seeking-identities-us-taxpayers-who-have-used>
  - body_hash: `sha256:a513884b358ba15a001ca99fbc53366262a02904c73b7aed0eaca5cfed9a77f4`
  - body_path: `sources/http_captures/coinbase-irs-john-doe-summons-2016/primary/www.justice.gov__opa-pr-court-authorizes-service-john-doe-summons-seeking-identities-us-taxpayers-who-have-used__55518cad06.html`
  > Current canonical justice.gov URL for the same press release (after
> the /archives/opa/ migration). Live capture (2026-05-16) returned a
> 3,082-byte AkamaiGHost bot-block stub rather than the press-release
> body; retained as contextual_unarchived pointer to the canonical URL.
> The Wayback memento above carries the evidentiary content. Mirrors
> the live-stub treatment in events/silk-road-doj-seizure-2013.yaml.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Coinbase Inc
- **Chains**: `bitcoin`
- **Canonical domains**: `coinbase.com`, `blog.coinbase.com`

> Coinbase Inc., a single named US-based virtual-currency exchanger
> headquartered in San Francisco, California. The IRS John Doe summons
> sought records of all US users with transactions in convertible virtual
> currency during 2013–2015. No on-chain addresses are enumerated at this
> event level; the target is the exchange entity and its US customer
> record set, not a cohort of crypto addresses.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 24h

**Event label**: `coinbase_public_opposition_to_irs_john_doe_summons`

**Timestamp**: `2016-11-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.coinbase.com/2016/11/18/protecting-customer-privacy/>
  - Wayback: <https://web.archive.org/web/20161122192010/https://blog.coinbase.com/2016/11/18/protecting-customer-privacy/>
  - body_hash: `sha256:cf1de3e7afb33b6e935ac6c2829b91ffe53f2b35df07d4d6e63044d6e41bfeee`
  - body_path: `sources/http_captures/coinbase-irs-john-doe-summons-2016/platform-response/web.archive.org__web-20161122192010-https-blog.coinbase.com-2016-11-18-protecting-customer-privacy__f1d311d433.html`
  > Coinbase's 2016-11-18 "Protecting Customer Privacy" blog post,
> captured by Wayback on 2016-11-22 (four days post-publication).
> The post states: "Our customers may be aware that the U.S.
> government filed a civil petition yesterday in federal court
> seeking disclosure of all Coinbase U.S. customers' records over
> a three year period." It commits Coinbase to oppose the petition
> in court. attribution=direct because the platform itself names
> the petition and announces the opposition stance in response.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No Coinbase.com frontend takedown or domain-state change is implicated

## 7. Related events

- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`nydfs-bitlicense-2015-06`](./nydfs-bitlicense-2015-06.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2bea37a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

