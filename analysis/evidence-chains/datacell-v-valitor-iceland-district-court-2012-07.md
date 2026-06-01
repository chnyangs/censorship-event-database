# Evidence chain — `datacell-v-valitor-iceland-district-court-2012-07`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `08595e8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:49:53Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2012-07-12, the Reykjavik District Court (Iceland)
> ordered Valitor hf. (the Iceland Visa/Mastercard sub-processor)
> to restore the DataCell ehf. merchant gateway used to collect
> WikiLeaks donations over Visa/Mastercard card rails within
> 14 days, on pain of daily fines of ISK 800,000 for each day of
> non-compliance. The ruling is the first judicial finding
> worldwide that a card-network WikiLeaks payment blockade was
> unlawful at the merchant-services contract layer, and constitutes
> a court-ordered counter-censorship (recovery / restoration) event
> at the offramp_cex cascade axis. The cascade surface moves in the
> restoration direction, away from the 2010-12 WikiLeaks
> payment-rail blockade. Observational axis at offramp_cex
> (load-bearing, attribution=direct via the court order self-
> attesting the restoration mandate). Admission-anchor-grade
> promotion pending pinned archive captures."

## 1. Trigger

- **Type**: `court_civil_order`
- **Actor**: `IS_REYKJAVIK_DISTRICT_COURT`
- **Timestamp**: `2012-07-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fink.org/FILES/translated-judgment-valitor.pdf>
  - Wayback: <https://web.archive.org/web/20140210061023if_/http://www.fink.org/FILES/translated-judgment-valitor.pdf>
  - body_hash: `sha256:6249809726bb383b6023f7c5988edd9f1c54a15b6add541bd42a34a11bbff257`
  - body_path: `sources/http_captures/datacell-v-valitor-iceland-district-court-2012-07/v0_3_primary_repair/web.archive.org__web-20140210061023if_-http-www.fink.org-FILES-translated-judgment-valitor.pdf__8acb78b60c.bin`
  > English translation PDF of the Reykjavik District Court
> judgment in DataCell ehf. v. Valitor hf., Case E-561/2012,
> dated 2012-07-12. Captured from a timestamped Wayback PDF
> memento. The document records the payment-gateway dispute and
> the judgment ordering Valitor to open the payment gateway
> within 14 days on pain of ISK 800,000 daily fines. v0.3
> caveat: this is a translated judgment artifact hosted outside
> the Icelandic judiciary; human audit should replace or pair it
> with an official Icelandic court source if available.
- **`supporting_journalism`**
  - URL: <https://www.bloomberg.com/news/articles/2012-07-12/iceland-court-orders-valitor-to-process-wikileaks-donations-1->
  - Wayback: <https://web.archive.org/web/2012/https://www.bloomberg.com/news/articles/2012-07-12/iceland-court-orders-valitor-to-process-wikileaks-donations-1->
  > Bloomberg 2012-07-12 coverage ("Iceland Court Orders Valitor to
> Process WikiLeaks Donations"). Independent journalism anchor for
> the ruling date and the order's substantive content: the
> Reykjavik District Court directed Valitor (the Visa/Mastercard
> sub-processor in Iceland) to reopen the DataCell merchant
> gateway used for WikiLeaks donation collection, within fourteen
> days, on pain of daily fines (originally claimed at ISK 1M/day,
> reduced by the court to ISK 800,000/day for each day non-
> compliance persists). DRYRUN: wayback wildcard pointer in lieu
> of a pinned-timestamp snapshot; evidence_use=contextual_unarchived
> because no body_hash+body_path pair has been captured into
> sources/http_captures/ in this session.
- **`supporting_journalism`**
  - URL: <https://grapevine.is/news/2012/07/13/datacell-wins-case-against-valitor/>
  - Wayback: <https://web.archive.org/web/2012/https://grapevine.is/news/2012/07/13/datacell-wins-case-against-valitor/>
  > Reykjavik Grapevine 2012-07-13 coverage ("DataCell Wins Case
> Against Valitor"). Icelandic local-press anchor confirming the
> 2012-07-12 ruling, the 14-day compliance window, and the
> ISK 800,000/day daily-fine figure (down from the ISK 1,000,000/day
> prayer for relief). Also confirms Valitor was ordered to pay
> DataCell's litigation costs of ISK 1,500,000. evidence_use=
> contextual_unarchived; body_hash capture deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://rsf.org/en/court-orders-visa-subcontractor-lift-block-payments-wikileaks>
  - Wayback: <https://web.archive.org/web/2012/https://rsf.org/en/court-orders-visa-subcontractor-lift-block-payments-wikileaks>
  > Reporters Without Borders (RSF) coverage of the 2012-07-12
> Reykjavik District Court ruling, framing the decision as the
> first judicial order requiring a card-network sub-processor
> to lift a WikiLeaks-related payment block. RSF analysis treats
> the ruling as a counter-censorship precedent at the
> payment-rail layer. evidence_use=contextual_unarchived;
> body_hash capture deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.computerworld.com/article/1417186/wikileaks-donations-via-visa-and-mastercard-may-resume-icelandic-court-rules.html>
  - Wayback: <https://web.archive.org/web/2012/https://www.computerworld.com/article/1417186/wikileaks-donations-via-visa-and-mastercard-may-resume-icelandic-court-rules.html>
  > Computerworld 2012-07 coverage ("Wikileaks donations via Visa
> and MasterCard may resume, Icelandic court rules"). Independent
> English-language journalism confirmation of the ruling and its
> operational effect: WikiLeaks donations via Visa/Mastercard could
> again be processed through the DataCell merchant gateway in
> Iceland. evidence_use=contextual_unarchived; body_hash capture
> deferred to human audit.
- **`supporting_community`**
  - URL: <https://wikileaks.org/Wikileaks-has-launched-a-case.html>
  - Wayback: <https://web.archive.org/web/2012/https://wikileaks.org/Wikileaks-has-launched-a-case.html>
  > WikiLeaks press release announcing the launch of the DataCell
> case against Valitor (the predecessor procedural step to the
> 2012-07-12 ruling). Provides the counter-censorship-litigation
> framing the case was filed under: WikiLeaks/DataCell alleged
> that Valitor's December-2010 closure of the donation gateway
> violated the Visa merchant-services contract and Icelandic
> contract law. evidence_use=contextual_unarchived; body_hash
> capture deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Valitor hf. / DataCell ehf.

> Target is the Valitor-DataCell merchant-services relationship: the
> Visa/Mastercard card-network sub-processor (Valitor hf., the
> Iceland sub-processor formerly trading as Visa Iceland) and the
> DataCell ehf. merchant account used to collect WikiLeaks donations
> over Visa/Mastercard card rails. The court order operates on this
> specific bilateral merchant agreement; subset because the
> enumerated target is the single DataCell merchant account /
> merchant-services contract rather than the broader class of
> WikiLeaks-aligned merchants worldwide. The ruling is jurisdictional
> to Iceland and does not bind other card-network sub-processors in
> other countries.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `court_ordered_restoration_of_valitor_datacell_merchant_gateway_for_wikileaks_donations`

**Timestamp**: `2012-07-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fink.org/FILES/translated-judgment-valitor.pdf>
  - Wayback: <https://web.archive.org/web/20140210061023if_/http://www.fink.org/FILES/translated-judgment-valitor.pdf>
  - body_hash: `sha256:6249809726bb383b6023f7c5988edd9f1c54a15b6add541bd42a34a11bbff257`
  - body_path: `sources/http_captures/datacell-v-valitor-iceland-district-court-2012-07/v0_3_primary_repair/web.archive.org__web-20140210061023if_-http-www.fink.org-FILES-translated-judgment-valitor.pdf__8acb78b60c.bin`
  > Primary legal-content anchor for the observed restoration
> order. The translated judgment states that Valitor is bound
> within 14 days from judgment to open the DataCell payment
> gateway under the 2011-06-15 collaboration agreement, with
> daily fines of ISK 800,000 after that time. Because the
> captured artifact is an English translation hosted outside
> the court site, human audit must confirm the translation
> against an official Icelandic judgment source before any
> release-grade promotion.
- **`supporting_journalism`**
  - URL: <https://www.bloomberg.com/news/articles/2012-07-12/iceland-court-orders-valitor-to-process-wikileaks-donations-1->
  - Wayback: <https://web.archive.org/web/2012/https://www.bloomberg.com/news/articles/2012-07-12/iceland-court-orders-valitor-to-process-wikileaks-donations-1->
  > Bloomberg 2012-07-12 coverage records the Reykjavik District
> Court ruling itself: Valitor ordered to process WikiLeaks
> donations via the DataCell merchant gateway, 14-day
> compliance window, daily-fine sanction of ISK 800,000/day.
> attribution=direct because the observed change (court-ordered
> restoration of the merchant gateway) is self-attested in the
> ruling text reported by Bloomberg the day of the decision.
> observation_kind=observed_change because this is a *recovery*
> / counter-censorship event: the order moves the offramp_cex
> cascade surface from blocked (post-2010-12 Visa Europe
> suspension) back toward open. DRYRUN: wayback wildcard
> pointer in lieu of pinned-timestamp snapshot.
- **`supporting_journalism`**
  - URL: <https://grapevine.is/news/2012/07/13/datacell-wins-case-against-valitor/>
  - Wayback: <https://web.archive.org/web/2012/https://grapevine.is/news/2012/07/13/datacell-wins-case-against-valitor/>
  > Reykjavik Grapevine 2012-07-13 coverage corroborates the
> ruling date, the 14-day compliance window, and the
> ISK 800,000/day daily-fine figure (court reduced DataCell's
> claimed ISK 1,000,000/day prayer to ISK 800,000/day). Also
> records the ISK 1,500,000 litigation-costs award to DataCell.
> Independent local-press confirmation of the court-ordered
> restoration.
- **`supporting_journalism`**
  - URL: <https://rsf.org/en/court-orders-visa-subcontractor-lift-block-payments-wikileaks>
  - Wayback: <https://web.archive.org/web/2012/https://rsf.org/en/court-orders-visa-subcontractor-lift-block-payments-wikileaks>
  > RSF coverage characterising the 2012-07-12 ruling as the
> first judicial finding worldwide that a card-network
> WikiLeaks payment blockade was unlawful at the merchant-
> services contract layer. RSF analysis treats the decision
> as a counter-censorship precedent.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-visa-europe-suspension-2010-12`](./wikileaks-visa-europe-suspension-2010-12.md)
- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-mastercard-suspension-2010-12`](./wikileaks-mastercard-suspension-2010-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `08595e8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

