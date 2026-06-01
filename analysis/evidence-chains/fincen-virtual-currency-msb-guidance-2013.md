# Evidence chain — `fincen-virtual-currency-msb-guidance-2013`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a785639` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:36:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> FinCEN FIN-2013-G001 (2013-03-18) interpreted the Bank Secrecy
> Act's money-transmitter regulations to apply to virtual-currency
> exchangers and administrators, establishing the foundational
> regulatory predicate for the 2013-2016 US MSB-registration
> enforcement era. observation_kind=coverage_gap with attribution=
> none because the substantive cascade is dispersed across
> downstream enforcement actions (Shrem/Faiella 2014, Powell 2014,
> Ripple/XRP II 2015, Murgio/Coin.mx 2015) that each cite this
> guidance as predicate, rather than localized to a single
> observable point-in-time CEX cessation. Historical-baseline tier;
> not used in main statistical denominators.

## 1. Trigger

- **Type**: `fincen_action`
- **Actor**: `US_FINCEN`
- **Timestamp**: `2013-03-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering>
  - Wayback: <https://web.archive.org/web/20161211230410/https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering>
  - body_hash: `sha256:88b50a08bfd2262ec81c02ed26b04ccc44725055bb4942f01203b93e207b74fc`
  - body_path: `sources/http_captures/fincen-virtual-currency-msb-guidance-2013/primary/web.archive.org__web-20161211230410-https-www.fincen.gov-resources-statutes-regulations-guidance-application-fincens-regulations-persons-administering__2cc2ece59a.html`
  > FinCEN guidance FIN-2013-G001, "Application of FinCEN's
> Regulations to Persons Administering, Exchanging, or Using
> Virtual Currencies," issued 2013-03-18. The guidance interprets
> FinCEN's Bank Secrecy Act (BSA) money-services-business (MSB)
> regulations as applied to virtual currency (VC) and defines
> three role categories: (1) users (persons who obtain VC to
> purchase goods/services) — not regulated as MSBs; (2) exchangers
> (persons engaged as a business in the exchange of VC for real
> currency, funds, or other VC) — money transmitters and therefore
> MSBs subject to BSA registration, AML program, recordkeeping,
> and reporting obligations; (3) administrators (persons engaged
> as a business in issuing/redeeming VC) — money transmitters and
> therefore MSBs. The guidance is the foundational regulatory
> predicate cited as authority in nearly every subsequent US BSA
> enforcement against a virtual-currency exchanger in the
> 2013-2016 historical-baseline tier (Shrem/Faiella 2014, Powell
> 2014, Ripple/XRP II 2015, Murgio/Coin.mx 2015) and continuing
> into the 2017+ comparable-analysis era (BitMEX 2020 FinCEN
> concurrent action, Helix 2020 FinCEN consent assessment,
> Binance 2023 FinCEN settlement). evidence_use=contextual_unarchived
> because body_hash+body_path archival capture was not pinned in
> this authoring pass; the live fincen.gov URL remains publicly
> accessible and Wayback bracketing of the 2013 publication window
> is straightforward in a follow-up human-audit pass. Provisional
> year-prefix wayback anchor pending re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Virtual currency administrators and exchangers (US BSA money transmitters)
- **Chains**: `bitcoin`

> Canonical target of this guidance is the regulatory class of
> "administrators and exchangers" of virtual currency under the
> BSA, i.e. any business that exchanges VC for fiat (or for other
> VC) or that administers issuance/redemption. The class is open-
> ended by construction: any US-resident person or legal entity
> that comes within FinCEN's interpretation of "money transmitter"
> is brought under BSA registration, AML-program, recordkeeping,
> and reporting obligations prospectively. Marked enumeration=subset
> rather than complete because the class is open-ended and the
> membership set evolves with subsequent FinCEN administrative
> rulings and enforcement actions (e.g. FIN-2014-R001 mining,
> FIN-2014-R002 software development, FIN-2019-G001 CVC business-
> models guidance). actor_name labels the regulated class; no
> on-chain addresses or canonical_domains are enumerated because
> the guidance does not designate specific entities or hosts.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `vc_exchanger_class_brought_under_bsa_msb_regime_no_per_event_cascade`

**Window**: `2013-03-18 00:00:00+00:00` → `2013-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering>
  - Wayback: <https://web.archive.org/web/20161211230410/https://www.fincen.gov/resources/statutes-regulations/guidance/application-fincens-regulations-persons-administering>
  - body_hash: `sha256:88b50a08bfd2262ec81c02ed26b04ccc44725055bb4942f01203b93e207b74fc`
  - body_path: `sources/http_captures/fincen-virtual-currency-msb-guidance-2013/primary/web.archive.org__web-20161211230410-https-www.fincen.gov-resources-statutes-regulations-guidance-application-fincens-regulations-persons-administering__2cc2ece59a.html`
  > FIN-2013-G001 is the legal instrument. observation_kind=
> coverage_gap with attribution=none honestly represents the
> load-bearing role of this guidance as a regulatory predicate
> whose cascade is dispersed across multiple downstream
> enforcement actions (Shrem/Faiella 2014, Powell 2014,
> Ripple/XRP II 2015, Murgio/Coin.mx 2015) rather than a
> single observable point-in-time CEX cessation directly
> attributable to the guidance alone. The cited downstream
> enforcement actions carry their own load-bearing
> observed_change rows in their own event files; this event
> records the predicate-establishing role only. Provisional
> year-prefix wayback anchor pending re-pin in a follow-up
> human-audit pass.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`shrem-faiella-bitcoin-exchange-2014`](./shrem-faiella-bitcoin-exchange-2014.md)
- [`powell-unlicensed-bitcoin-exchange-2014`](./powell-unlicensed-bitcoin-exchange-2014.md)
- [`ripple-fincen-xrp-2015`](./ripple-fincen-xrp-2015.md)
- [`sec-shavers-btcst-2013`](./sec-shavers-btcst-2013.md)
- [`silk-road-doj-seizure-2013`](./silk-road-doj-seizure-2013.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a785639`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

