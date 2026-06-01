# Evidence chain — `wikileaks-postfinance-account-closure-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b524247` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2010-12-06, PostFinance (Swiss Post's retail-banking arm)
> terminated the customer account registered as 'Assange Julian Paul,
> Geneve' — the account WikiLeaks had publicly advertised as the
> destination for the 'Julian Assange and other WikiLeaks Staff
> Defence Fund' — citing residency-verification failure under
> customer-relationship criteria. One observed_change at offramp_cex
> (load-bearing, attribution=direct, anchored on the PostFinance
> same-day media statement plus same-day Bloomberg / Al Jazeera /
> France 24 / swissinfo coverage). Discovery-ledger-only per
> temporal_tier=discovery_only_2007_2012."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `SWISSPOST_POSTFINANCE_OPERATOR`
- **Timestamp**: `2010-12-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.postfinance.ch/en/about-us/media/news-archive/2010/wikileaks.html>
  - Wayback: <https://web.archive.org/web/2010/https://www.postfinance.ch/en/about-us/media/news-archive/2010/wikileaks.html>
  > PostFinance (Swiss Post's retail-banking arm) press statement
> dated 2010-12-06 announcing closure of the customer account held
> in the name of "Assange Julian Paul, Geneve" — the account
> WikiLeaks had publicly advertised as the destination for the
> "Julian Assange and other WikiLeaks Staff Defence Fund." The
> bank's stated rationale: the customer "provided false information
> regarding his place of residence during the account opening
> process" and could not produce proof of Swiss residency,
> therefore did not meet PostFinance's customer-relationship
> criteria. PostFinance added that there would be "no criminal
> consequences" for the alleged residency misrepresentation,
> signalling that the closure was a unilateral corporate
> policy/diligence decision rather than a criminal-referral or
> regulator-directed action. DRYRUN: wayback wildcard
> (web/2010/) pointer in lieu of a pinned-timestamp snapshot;
> evidence_use=contextual_unarchived because no body_hash+body_path
> capture of the PostFinance media-archive page has been pinned
> into sources/http_captures/ in this drafting session.
- **`supporting_journalism`**
  - URL: <https://www.bloomberg.com/news/articles/2010-12-06/wikileaks-founder-assange-s-swisspost-account-closed-on-residency-question>
  - Wayback: <https://web.archive.org/web/2010/https://www.bloomberg.com/news/articles/2010-12-06/wikileaks-founder-assange-s-swisspost-account-closed-on-residency-question>
  > Bloomberg 2010-12-06 coverage ("WikiLeaks Founder's Swisspost
> Account Closed on Residency Question") confirming the closure
> date, the PostFinance "false residency information" rationale,
> and the broader-blockade interpretation context. Independent
> same-day pin on the day-level trigger timestamp.
- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/news/2010/12/6/swiss-bank-closes-wikileaks-account>
  - Wayback: <https://web.archive.org/web/2010/https://www.aljazeera.com/news/2010/12/6/swiss-bank-closes-wikileaks-account>
  > Al Jazeera 2010-12-06 coverage independently reporting the
> PostFinance closure of Assange's defence-fund account on
> residency-verification grounds and situating the action within
> the contemporaneous PayPal / MasterCard / Visa Europe blockade
> cluster.
- **`supporting_journalism`**
  - URL: <https://www.france24.com/en/20101206-swiss-bank-closes-assange-account-accuses-lying-wikileaks-paypal-post>
  - Wayback: <https://web.archive.org/web/2010/https://www.france24.com/en/20101206-swiss-bank-closes-assange-account-accuses-lying-wikileaks-paypal-post>
  > France 24 2010-12-06 coverage: "Swiss bank closes Assange's
> account, accuses him of lying." Additional independent-pin same
> day; names the WikiLeaks-advertised account ("Assange Julian
> Paul, Geneve") and the PostFinance "false residence information"
> statement.
- **`supporting_journalism`**
  - URL: <https://www.swissinfo.ch/eng/wikileaks-supporters-attack-postfinance-site/28971816>
  - Wayback: <https://web.archive.org/web/2010/https://www.swissinfo.ch/eng/wikileaks-supporters-attack-postfinance-site/28971816>
  > SWI swissinfo.ch (Swiss public-broadcaster English service) 2010
> coverage of the PostFinance closure and the same-day
> Operation-Payback DDoS retaliation against postfinance.ch.
> Swiss-jurisdiction-local journalism pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: PostFinance customer account "Assange Julian Paul, Geneve" (Julian Assange / WikiLeaks Defence Fund)

> Subset: the single PostFinance customer account registered as
> "Assange Julian Paul, Geneve" — the account WikiLeaks had publicly
> advertised on wikileaks.org as the donation destination for the
> "Julian Assange and other WikiLeaks Staff Defence Fund." This is a
> single named-account closure, not a class-wide WikiLeaks-supporter
> PostFinance customer sweep. Other PostFinance customer relationships
> held by WikiLeaks supporters or staff outside this named account are
> not enumerated here (no contemporaneous evidence of class-wide
> closure beyond the single defence-fund account).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `postfinance_closes_assange_wikileaks_defence_fund_account_citing_residency_verification_failure`

**Timestamp**: `2010-12-06 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/20110630203331/http://wikileaks.org/Banking-Blockade.html>
  - body_hash: `sha256:f43fbbf0ffec01ac89e02b2a36a332851099a64e56ccfe53b5a6e0a26e5d9f0a`
  - body_path: `sources/http_captures/wikileaks-postfinance-account-closure-2010-12/primary/web.archive.org__web-20110601000000-http-www.wikileaks.org-Banking-Blockade.html__c0a0319be1.html`
  > WikiLeaks canonical Banking-Blockade record (affected-org primary)
> documenting Swiss PostFinance's 2010-12-06 closure of Julian Assange's
> defence-fund account (citing a false-residency pretext). attribution=
> direct: PostFinance publicly confirmed the closure. The agent-drafted
> postfinance.ch news-archive URL was fabricated (no Wayback memento).
> Wayback 20110630203331 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-mastercard-suspension-2010-12`](./wikileaks-mastercard-suspension-2010-12.md)
- [`wikileaks-visa-europe-suspension-2010-12`](./wikileaks-visa-europe-suspension-2010-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b524247`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

