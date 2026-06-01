# Evidence chain — `wikileaks-mastercard-suspension-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `137626c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "MasterCard Worldwide announced on 2010-12-06 that it was suspending
> acceptance of MasterCard-branded cards for WikiLeaks donations on
> the grounds that its rules prohibit customers from facilitating
> illegal action, severing the card-network donation channel routed
> through the DataCell ehf merchant gateway; the row is registered as
> a single-layer offramp_cex operator-policy-change observation in
> the discovery-only 2008-2012 tier and does not assert ISP-level
> network blocking, L1 consensus engagement, RPC-compliance
> filtering, asset-onchain freezing, or L4 frontend takedown by the
> card-network operator."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `MASTERCARD_OPERATOR`
- **Timestamp**: `2010-12-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.mastercard.com/>
  - Wayback: <https://web.archive.org/web/2010/https://www.mastercard.com/>
  > MasterCard Worldwide stated on 2010-12-06 that it was "in the
> process of working to suspend the acceptance of MasterCard
> cards on WikiLeaks until the situation is resolved" and that
> "MasterCard rules prohibit customers from directly or indirectly
> engaging in or facilitating any action that is illegal."
> Spokesman Chris Monteiro delivered the statement to multiple
> press outlets (Reuters, CNN Money, NPR, CBC, BBC, Guardian,
> France 24) on 2010-12-06 / 2010-12-07. The card-network
> processing suspension took effect within hours and severed the
> MasterCard-branded credit-card donation channel for WikiLeaks
> donations routed through the DataCell ehf merchant gateway in
> Iceland. MasterCard never issued a standalone press release on
> the mastercard.com newsroom; the statement exists only as a
> spokesman quotation circulated to journalists. Marked
> evidence_use=contextual_unarchived because no specific
> body_hash+body_path or pinned Wayback snapshot of the
> spokesman quotation surface was captured during this authoring
> pass; the live mastercard.com root URL remains the operator
> domain and Wayback bracketing of the 2010-12 newsroom window
> is the natural anchor for follow-up human-audit pinning.
> Provisional Wayback anchor uses Wayback Machine year-prefix
> lookup.
- **`supporting_journalism`**
  - URL: <https://money.cnn.com/2010/12/08/news/companies/mastercard_wiki/index.htm>
  - Wayback: <https://web.archive.org/web/2010/https://money.cnn.com/2010/12/08/news/companies/mastercard_wiki/index.htm>
  > CNN Money 2010-12-08 reporting on the MasterCard / Visa
> WikiLeaks suspension and the Operation Payback DDoS
> retaliation against mastercard.com. Carries the MasterCard
> spokesman statement quotation ("MasterCard rules prohibit
> customers from directly or indirectly engaging in or
> facilitating any action that is illegal") and reports on the
> same-week Anonymous-affiliated DDoS campaign that took down
> mastercard.com on 2010-12-08. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin and
> body_hash capture during human audit.
- **`supporting_journalism`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/2011/https://wikileaks.org/Banking-Blockade.html>
  > WikiLeaks "Banking Blockade" archive page enumerates the
> 2010-12 financial-intermediary actions including the
> MasterCard processing suspension. Used as the canonical
> operator-self-description anchor for the blockade timeline
> even though the page is operator-authored. Marked
> evidence_use=contextual_unarchived pending pinned-snapshot
> re-pin during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: MasterCard Worldwide
- **Canonical domains**: `wikileaks.org`

> Target is the WikiLeaks donations-acceptance surface across the
> MasterCard card-network processing rail. Concretely, MasterCard-
> branded credit/debit-card donations routed through the DataCell
> ehf merchant gateway in Iceland (which had set up card-network
> acquiring under a 2010-10 services contract to process WikiLeaks
> donations) were severed when MasterCard suspended acceptance.
> Marked enumeration=subset rather than complete because the
> operator-public statement names "WikiLeaks" as the target without
> enumerating downstream merchant-of-record entities (e.g. Sunshine
> Press Productions ehf., DataCell ehf., the Wau-Holland-Stiftung
> affiliate accounts) and because the broader WikiLeaks donations-
> infrastructure umbrella is not exhaustively listed in the
> statement. No on-chain addresses are enumerated (pre-Bitcoin
> baseline: WikiLeaks did not begin accepting Bitcoin donations
> until 2011-06). canonical_domains lists the operator-attacked
> donation-acceptance domain (wikileaks.org); chains is empty
> because no L1 chain primitive is engaged by a card-network
> operator policy change in 2010.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `mastercard_suspended_card_network_processing_of_wikileaks_donations`

**Timestamp**: `2010-12-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/20110630203331/http://wikileaks.org/Banking-Blockade.html>
  - body_hash: `sha256:f43fbbf0ffec01ac89e02b2a36a332851099a64e56ccfe53b5a6e0a26e5d9f0a`
  - body_path: `sources/http_captures/wikileaks-mastercard-suspension-2010-12/primary/web.archive.org__web-20110601000000-http-www.wikileaks.org-Banking-Blockade.html__c0a0319be1.html`
  > WikiLeaks canonical Banking-Blockade record (affected-org primary)
> documenting MasterCard's 2010-12-07 suspension of WikiLeaks payments.
> attribution=direct: MasterCard publicly confirmed the action.
> Wayback 20110630203331 pinned.
- **`semi_primary_wayback`**
  - URL: <https://money.cnn.com/2010/12/08/news/companies/mastercard_wiki/index.htm>
  - Wayback: <https://web.archive.org/web/20101209234220/http://money.cnn.com/2010/12/08/news/companies/mastercard_wiki/index.htm>
  - body_hash: `sha256:d57757d55469868e201a480f0653c80d46e1e6efbb7ec26b7fa93da15d9b049c`
  - body_path: `sources/http_captures/wikileaks-mastercard-suspension-2010-12/primary/web.archive.org__web-20101209000000-http-money.cnn.com-2010-12-08-news-companies-mastercard_wiki-index.htm__100baa7e23.html`
  > CNNMoney 2010-12-08 coverage of MasterCard halting WikiLeaks
> payments. Independent semi-primary anchor. Wayback 20101209234220 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 6. Follow-on reactions (informational, not causally attributed)

> These are cross-event reactions observed after the trigger but with `attribution: unknown` or temporal gap too large for direct causation. **They do NOT support the scoped claim above.** Tracked for cross-event anchor purposes only.

### ? — `?`

- Attribution: `unknown`
- Relationship: `?`
- Δt from trigger: `?h`

> Operation Payback (Anonymous-affiliated DDoS coalition)
> launched a coordinated distributed-denial-of-service attack
> against mastercard.com on 2010-12-08 in retaliation for the
> MasterCard processing suspension. Captured here as a
> cross-event follow-on reaction with attribution=unknown
> per reviewer Action 4 (schema 0.2.0). Does NOT count toward
> this event's empirical_shape or admission_tier accounting;
> tracked for cross-event-anchor purposes only.


## 7. Related events

- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-visa-europe-suspension-2010-12`](./wikileaks-visa-europe-suspension-2010-12.md)
- [`wikileaks-bank-of-america-block-2010-12`](./wikileaks-bank-of-america-block-2010-12.md)
- [`wikileaks-western-union-interdiction-2010-12`](./wikileaks-western-union-interdiction-2010-12.md)
- [`wikileaks-postfinance-account-closure-2010-12`](./wikileaks-postfinance-account-closure-2010-12.md)
- [`datacell-v-valitor-iceland-district-court-2012-07`](./datacell-v-valitor-iceland-district-court-2012-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `137626c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

