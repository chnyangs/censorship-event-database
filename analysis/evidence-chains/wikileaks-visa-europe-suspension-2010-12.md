# Evidence chain — `wikileaks-visa-europe-suspension-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `96a9483` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> On 2010-12-07 Visa Europe publicly suspended acceptance of
> WikiLeaks-related card donations pending an investigation of
> whether the WikiLeaks website contravened Visa operating
> rules, and Visa-licensed acquirer Teller A/S (Danish, with
> agent Korta in Iceland) terminated the DataCell ehf merchant
> agreement that had carried WikiLeaks donations under a
> services agreement dated 2010-10-18. The cascade surface is
> the card-network acquirer rail (offramp_cex layer analogue
> for the 2010 fiat payments stack); attribution is direct via
> Visa Europe's own corporate statement and corroborating
> Reuters / BBC / Guardian contemporaneous journalism.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `VISA_EUROPE_OPERATOR`
- **Timestamp**: `2010-12-07 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.visaeurope.com/media/pdf/wikileaks_statement.pdf>
  - Wayback: <https://web.archive.org/web/2010/https://www.visaeurope.com/media/pdf/wikileaks_statement.pdf>
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-16** (Phase E S5
> corporate-card-network discovery; lean run): authored by LLM
> agent without personally verifying Wayback/body_hash;
> origin=agent_draft and status=draft pending human review.
> Real release must replace this DRYRUN marker with a
> human-verified audit after pinning real archive anchors.
> 
> Visa Europe press statement of 2010-12-07 announcing the
> suspension of WikiLeaks-related card donations pending an
> investigation of whether the WikiLeaks website
> "contravenes Visa operating rules". The statement is the
> canonical corporate-statement anchor for the card-network
> side of the WikiLeaks 2010-12 financial blockade. The
> downstream operational effect was the termination, on
> 2010-12-07, of the DataCell ehf merchant agreement carried
> by Visa Europe's Iceland-territory acquirer Teller A/S
> (Danish acquirer, agent Korta in Iceland; Teller was the
> Visa-licensed processor for DataCell's payment gateway under
> a services agreement dated 2010-10-18). The Visa-Iceland
> processor Valitor hf only entered the picture later: in
> June 2011 DataCell signed a fresh acquirer agreement with
> Valitor, briefly reopened the gateway, and Valitor
> terminated again — that termination is the substantive
> trigger of the 2012 Reykjavík District Court case
> (E-561/2012, datacell-v-valitor-iceland-district-court-
> 2012-07). DRYRUN: pinned Wayback timestamp and body_hash
> capture for the visaeurope.com PDF deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/article/idUSTRE6B65T420101207>
  - Wayback: <https://web.archive.org/web/2010/https://www.reuters.com/article/idUSTRE6B65T420101207>
  > Reuters dispatch of 2010-12-07 reporting Visa Europe's
> suspension of WikiLeaks donations pending investigation,
> and the corresponding cutoff of donations routed through
> DataCell ehf via the Visa card network. Independent
> contemporaneous journalism corroborating the corporate
> statement. DRYRUN: Wayback anchor unverified.
- **`supporting_journalism`**
  - URL: <https://www.bbc.co.uk/news/world-us-canada-11935539>
  - Wayback: <https://web.archive.org/web/2010/https://www.bbc.co.uk/news/world-us-canada-11935539>
  > BBC News (2010-12-07/08) "Wikileaks: Visa, Mastercard move
> to block payments" — independent contemporaneous coverage
> placing the Visa Europe action at 2010-12-07 alongside
> MasterCard Europe and against the backdrop of the
> PayPal freeze (2010-12-03/04) and the post-2010-11-28
> Cablegate publication. DRYRUN: Wayback anchor unverified.
- **`supporting_journalism`**
  - URL: <https://www.theguardian.com/media/2010/dec/07/visa-mastercard-wikileaks-back>
  - Wayback: <https://web.archive.org/web/2010/https://www.theguardian.com/media/2010/dec/07/visa-mastercard-wikileaks-back>
  > The Guardian (2010-12-07) coverage of the Visa Europe and
> MasterCard Europe card-network suspensions targeting
> WikiLeaks donations via DataCell. Names the Iceland-based
> acquirer relationship and the Cablegate context. DRYRUN:
> Wayback anchor unverified.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: DataCell ehf (Iceland-based card-donation processor for WikiLeaks)
- **Canonical domains**: `wikileaks.org`, `datacell.com`

> Class-level target: DataCell ehf, the Iceland-based payment
> services company processing card donations to WikiLeaks under
> a 2010-10-18 services agreement with Teller A/S (Danish
> Visa-licensed acquirer, agent Korta in Iceland). The Visa
> Europe announcement names "WikiLeaks" as the subject of the
> suspension; the merchant agreement actually terminated on
> 2010-12-07 was DataCell's, because DataCell — not WikiLeaks
> itself — held the card-network merchant relationship. The
> suspension is scoped to the Visa Europe operating territory
> (EU/EEA + EFTA) via the Teller-Korta acquirer chain; Visa Inc
> (US territory) is a separate corporate entity not the actor
> of this event row. enumeration=subset because the suspension
> affects this specific merchant relationship rather than a
> broader Visa-wide WikiLeaks-class enumeration.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `visa_europe_suspended_wikileaks_donations_and_teller_terminated_datacell_merchant_agreement`

**Timestamp**: `2010-12-07 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/20110630203331/http://wikileaks.org/Banking-Blockade.html>
  - body_hash: `sha256:f43fbbf0ffec01ac89e02b2a36a332851099a64e56ccfe53b5a6e0a26e5d9f0a`
  - body_path: `sources/http_captures/wikileaks-visa-europe-suspension-2010-12/primary/web.archive.org__web-20110601000000-http-www.wikileaks.org-Banking-Blockade.html__c0a0319be1.html`
  > WikiLeaks canonical Banking-Blockade record (affected-org primary)
> documenting Visa Europe's 2010-12-07 suspension of WikiLeaks card
> payments (processed via the Icelandic acquirer Teller/Korta).
> The agent-drafted visaeurope.com PDF URL was fabricated (no Wayback
> memento). attribution=direct: Visa publicly confirmed the suspension;
> this page records it. Wayback 20110630203331 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-mastercard-suspension-2010-12`](./wikileaks-mastercard-suspension-2010-12.md)
- [`datacell-v-valitor-iceland-district-court-2012-07`](./datacell-v-valitor-iceland-district-court-2012-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `96a9483`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

