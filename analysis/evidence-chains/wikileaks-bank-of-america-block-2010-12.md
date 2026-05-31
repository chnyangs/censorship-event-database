# Evidence chain — `wikileaks-bank-of-america-block-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `128e1e1` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> Bank of America's public statement of 2010-12-18 announcing that
> the bank "will not process any transactions of any type that we
> have reason to believe are intended for WikiLeaks", citing
> internal-payment-policy interpretation regarding WikiLeaks
> activities deemed "inconsistent with our internal policies for
> processing payments", constitutes a discovery-ledger corporate-
> policy-change event documenting US-bank-rail off-ramp closure
> against WikiLeaks. Fifth and final constituent action of the
> December 2010 "banking blockade" cluster.

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `BANK_OF_AMERICA_OPERATOR`
- **Timestamp**: `2010-12-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://newsroom.bankofamerica.com/>
  - Wayback: <https://web.archive.org/web/2010/https://newsroom.bankofamerica.com/>
  > Bank of America public statement of 2010-12-18 announcing that
> the bank "will not process any transactions of any type that we
> have reason to believe are intended for WikiLeaks". The
> statement is widely quoted in contemporaneous wire copy
> (Reuters / AP) and direct corporate-newsroom dissemination
> was the bofa.com / newsroom.bankofamerica.com surface. The
> canonical sentence reads (as reported by Reuters and quoted in
> downstream coverage): "This decision is based upon our
> reasonable belief that WikiLeaks may be engaged in activities
> that are, among other things, inconsistent with our internal
> policies for processing payments." Specific Wayback snapshot
> pin requires re-pinning in human audit; the bofa.com newsroom
> domain anchor is contextual_unarchived in this authoring pass.
- **`supporting_journalism`**
  - URL: <https://www.reuters.com/article/idUSTRE6BH0NQ/>
  - Wayback: <https://web.archive.org/web/2010/https://www.reuters.com/article/idUSTRE6BH0NQ/>
  > Reuters wire copy of 2010-12-18 carrying the canonical Bank of
> America statement quote on the refusal to process any
> WikiLeaks-intended transactions. This wire is the originating
> public source of the "inconsistent with our internal policies"
> sentence reproduced across all downstream coverage (NBC News,
> CBS News, Al Jazeera, France 24, Huffington Post, 6abc). URL
> is the standard Reuters idUS identifier shape; specific
> Wayback snapshot timestamp requires re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://www.nbcnews.com/id/wbna40728284>
  - Wayback: <https://web.archive.org/web/2010/https://www.nbcnews.com/id/wbna40728284>
  > NBC News / msnbc.com 2010-12-18 syndication titled "Bank of
> America cuts off WikiLeaks payments". Carries the canonical
> Bank of America statement quote and frames the announcement
> as the addition of Bank of America to the existing
> PayPal/Mastercard/Visa Europe/Western Union banking-blockade
> cluster against WikiLeaks. Specific Wayback snapshot
> timestamp requires re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/economy/2010/12/18/bank-of-america-cuts-off-wikileaks>
  - Wayback: <https://web.archive.org/web/2010/https://www.aljazeera.com/economy/2010/12/18/bank-of-america-cuts-off-wikileaks>
  > Al Jazeera 2010-12-18 article titled "Bank of America cuts
> off WikiLeaks" reporting the same-day announcement with the
> canonical statement quote and cross-referencing the prior
> actions by PayPal, Mastercard, and Visa Europe. Specific
> Wayback snapshot timestamp requires re-pinning in human audit.
- **`supporting_journalism`**
  - URL: <https://www.cbsnews.com/news/bank-of-america-to-block-donations-to-wikileaks/>
  - Wayback: <https://web.archive.org/web/2010/https://www.cbsnews.com/news/bank-of-america-to-block-donations-to-wikileaks/>
  > CBS News 2010-12-18 article "Bank of America to Block
> Donations to WikiLeaks" reproducing the canonical bank
> statement and confirming the corporate-policy framing.
> Specific Wayback snapshot timestamp requires re-pinning in
> human audit.
- **`supporting_community`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/2011/https://wikileaks.org/Banking-Blockade.html>
  > WikiLeaks "Banking Blockade" page listing the December 2010
> refusals by Bank of America, PayPal, Mastercard, Visa Europe,
> and Western Union as the constituent actions of the
> coordinated "banking blockade" against WikiLeaks. Self-
> reported by the target organization but corroborated by the
> individual primary-corporate / supporting-journalism sources
> for each constituent action. Specific Wayback snapshot
> timestamp requires re-pinning in human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: WikiLeaks

> Target is WikiLeaks and its donation-collection vehicles, i.e.
> any payee or transaction that Bank of America has "reason to
> believe" is intended for WikiLeaks. enumeration=subset because
> the bank's stated criterion is belief-based rather than an
> enumerated account list; no specific WikiLeaks-controlled BofA
> account number is named in the public statement. No specific
> domain anchor is identified for the target, so canonical_domains
> is empty.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `bofa_refuses_to_process_wikileaks_intended_transactions`

**Timestamp**: `2010-12-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://wikileaks.org/Banking-Blockade.html>
  - Wayback: <https://web.archive.org/web/20110630203331/http://wikileaks.org/Banking-Blockade.html>
  - body_hash: `sha256:f43fbbf0ffec01ac89e02b2a36a332851099a64e56ccfe53b5a6e0a26e5d9f0a`
  - body_path: `sources/http_captures/wikileaks-bank-of-america-block-2010-12/primary/web.archive.org__web-20110601000000-http-www.wikileaks.org-Banking-Blockade.html__c0a0319be1.html`
  > WikiLeaks canonical Banking-Blockade record (affected-org primary)
> documenting Bank of America's 2010-12-18 announcement that it would
> stop processing transactions intended for WikiLeaks. attribution=direct:
> BofA publicly confirmed the action. The agent-drafted newsroom.
> bankofamerica.com homepage URL was non-specific. Wayback 20110630203331
> pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-visa-europe-suspension-2010-12`](./wikileaks-visa-europe-suspension-2010-12.md)
- [`wikileaks-mastercard-suspension-2010-12`](./wikileaks-mastercard-suspension-2010-12.md)
- [`wikileaks-western-union-interdiction-2010-12`](./wikileaks-western-union-interdiction-2010-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `128e1e1`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

