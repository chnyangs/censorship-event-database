# Evidence chain — `mtgox-mizuho-wire-pressure-2012`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `24d80a4` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:03:45Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "No discrete 2012-12 Mizuho Bank action against Mt. Gox K.K.'s
> JPY/USD wire-transfer rails is documented in the secondary
> sources consulted (Mt. Gox Wikipedia, Bilzin Sumberg
> jurisdictional retrospective on Greene v. Mizuho). The
> documented Mizuho correspondent-banking severance against
> Mt. Gox begins 2013-06-20 onward, coincident with the
> Mt. Gox USD withdrawal suspension. This row records
> observation_kind=observed_no_change + attribution=none at
> offramp_cex over the 2012-12 calendar month as a negative
> finding. null_event shape; discovery-tier; not used in
> main statistical denominators."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MIZUHO_BANK`
- **Timestamp**: `2012-12-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.govinfo.gov/content/pkg/USCOURTS-ilnd-1_14-cv-01437/pdf/USCOURTS-ilnd-1_14-cv-01437-0.pdf>
  - body_hash: `sha256:aa699e996b793579856c915cccebbb05ce7036b7073729264528ed8d4dcf9cb1`
  - body_path: `sources/http_captures/mtgox-mizuho-wire-pressure-2012/v0_3_primary_repair/www.govinfo.gov__content-pkg-USCOURTS-ilnd-1_14-cv-01437-pdf-USCOURTS-ilnd-1_14-cv-01437-0.pdf__4871bc7a90.bin`
  > GovInfo copy of the Northern District of Illinois order in
> Greene v. MtGox Inc. et al., No. 1:14-cv-01437, Doc. 200
> (2016-03-14). The court summarizes the pleaded Mizuho/Mt.
> Gox banking facts and states that by mid-2013 Mizuho was no
> longer processing international wire withdrawals for Mt. Gox.
> Used as primary legal evidence that the public legal record
> locates the documented Mizuho wire-withdrawal cutoff in
> mid-2013, not in the 2012-12 null-event window recorded
> here. This source supports the negative finding only; it
> does not create a 2012-12 observed_change event.
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/Mt._Gox>
  - Wayback: <https://web.archive.org/web/2012/https://en.wikipedia.org/wiki/Mt._Gox>
  > Mt. Gox Wikipedia entry — consulted for the Mizuho banking-
> relationship timeline. The article documents Mizuho Bank's
> pressure on Mt. Gox to close the corporate banking account
> as beginning from 20 June 2013 onward (concurrent with the
> Mt. Gox USD withdrawal suspension), not from December 2012.
> Used here as a negative-finding anchor for the null_event
> coding. evidence_use=contextual_unarchived: no body_hash
> captured this session.
- **`supporting_journalism`**
  - URL: <https://www.bilzin.com/we-think-big/insights/publications/2019/09/jurisdictional-lessons-from-mt-gox-cryptocurrency>
  - Wayback: <https://web.archive.org/web/2012/https://www.bilzin.com/we-think-big/insights/publications/2019/09/jurisdictional-lessons-from-mt-gox-cryptocurrency>
  > Bilzin Sumberg "Jurisdictional Lessons from Mt. Gox
> Cryptocurrency Litigation" (2019-09) — legal practitioner
> retrospective on Greene v. Mizuho Bank. Locates the
> substantive Mizuho-Mt.Gox correspondent-banking severance
> in mid-2013 (post-2013-06-20 USD suspension), not in
> December 2012. Supports the null_event finding for any
> 2012-12 Mizuho corporate-policy-change trigger.
> evidence_use=contextual_unarchived.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Mt. Gox K.K.
- **Chains**: `bitcoin`
- **Canonical domains**: `mtgox.com`

> Hypothetical 2012-12 Mizuho Bank correspondent-banking action
> against Mt. Gox K.K.'s JPY/USD wire-transfer rails. No
> enumeration is possible because no such discrete 2012-12
> action is documented in the consulted sources. Class-level
> scope would have covered Mt. Gox K.K.'s corporate banking
> account at Mizuho's Tokyo branch and the international wire-
> withdrawal flow for Mt. Gox USD customers.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_documented_2012_12_mizuho_action_against_mtgox_wire_rails`

**Window**: `2012-12-01 00:00:00+00:00` → `2012-12-31 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.govinfo.gov/content/pkg/USCOURTS-ilnd-1_14-cv-01437/pdf/USCOURTS-ilnd-1_14-cv-01437-0.pdf>
  - body_hash: `sha256:aa699e996b793579856c915cccebbb05ce7036b7073729264528ed8d4dcf9cb1`
  - body_path: `sources/http_captures/mtgox-mizuho-wire-pressure-2012/v0_3_primary_repair/www.govinfo.gov__content-pkg-USCOURTS-ilnd-1_14-cv-01437-pdf-USCOURTS-ilnd-1_14-cv-01437-0.pdf__4871bc7a90.bin`
  > Primary legal anchor for the observed_no_change coding.
> The court order describes Mizuho's relationship with Mt.
> Gox and places the documented halt of international wire
> withdrawals by Mizuho in mid-2013. That placement supports
> this row's bounded negative finding that no discrete
> 2012-12 Mizuho action was located in the public legal
> record. It is not coded as direct proof of a 2012-12
> action.
- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/Mt._Gox>
  - Wayback: <https://web.archive.org/web/2012/https://en.wikipedia.org/wiki/Mt._Gox>
  > observation_kind=observed_no_change + attribution=none.
> Mt. Gox Wikipedia article documents Mizuho's pressure on
> Mt. Gox as beginning 2013-06-20 onward (concurrent with
> the USD withdrawal suspension), not in December 2012.
> No specific 2012-12 Mizuho action against Mt. Gox's
> wire rails is documented. The 2012-12 trigger asserted
> by the authoring brief is not corroborated by any
> consulted source. evidence_use=contextual_unarchived:
> no body_hash captured this session.
- **`supporting_journalism`**
  - URL: <https://www.bilzin.com/we-think-big/insights/publications/2019/09/jurisdictional-lessons-from-mt-gox-cryptocurrency>
  - Wayback: <https://web.archive.org/web/2012/https://www.bilzin.com/we-think-big/insights/publications/2019/09/jurisdictional-lessons-from-mt-gox-cryptocurrency>
  > Bilzin Sumberg 2019-09 retrospective on Greene v. Mizuho
> litigation places the Mizuho-Mt.Gox correspondent-
> banking severance in mid-2013. No 2012-12 antecedent
> action is documented. Corroborates the null_event
> finding.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-coinlab-civil-2013`](./mtgox-coinlab-civil-2013.md)
- [`mtgox-dhs-dwolla-wells-fargo-seizure-2013`](./mtgox-dhs-dwolla-wells-fargo-seizure-2013.md)
- [`mtgox-usd-withdrawal-suspension-2013-06`](./mtgox-usd-withdrawal-suspension-2013-06.md)
- [`mtgox-bankruptcy-tokyo-2014`](./mtgox-bankruptcy-tokyo-2014.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `24d80a4`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

