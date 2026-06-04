# Evidence chain — `wikileaks-wau-holland-tax-status-challenge-2010-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `6678414` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T04:52:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "In December 2010, the German Finanzamt Kassel opened an
> administrative review of the Wau Holland Stiftung's
> gemeinnuetzig (tax-exempt) status for 2010 over its project-04
> forwarding of donations to WikiLeaks, disrupting the EU-wide
> tax-deductible WikiLeaks donation rail the foundation had operated
> and presaging the formal January 2011 revocation. One
> observed_change at offramp_cex (attribution=plausible, anchored on
> Wau Holland Stiftung self-reporting and contemporaneous
> journalism). Discovery-ledger-only per temporal_tier=
> discovery_only_2007_2012."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `DE_FA_KASSEL`
- **Timestamp**: `2010-12-15 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://en.wikipedia.org/wiki/Wau_Holland_Foundation>
  - Wayback: <https://web.archive.org/web/2010/https://en.wikipedia.org/wiki/Wau_Holland_Foundation>
  > Wau Holland Foundation Wikipedia entry consolidates the
> German-tax-authority challenge timeline: the Finanzamt Kassel
> (Kassel Tax Office), which had certified the Wau Holland
> Stiftung's gemeinnuetzig (charitable / tax-exempt) status,
> opened a review in late 2010 of the foundation's project-04
> ("Enduring Freedom of Information / WikiLeaks") donation
> forwarding. The eventual administrative outcome (Kassel formally
> revoking 2010 tax-exempt status "wegen Verstosses gegen das
> Gebot der Selbstlosigkeit" / "for violation of the principle of
> altruism") was completed in January 2011, with a later Hamburg
> Tax Office retroactive revocation 2012-10-25. The 2010-12
> trigger window pins the *opening* of the Kassel review during
> the same week as the PayPal / PostFinance / MasterCard / Visa /
> Bank-of-America cascade; the formal revocation arrives one
> month later. DRYRUN: wayback wildcard pointer; tertiary source.
- **`primary_corporate`**
  - URL: <https://wauland.de/en/projects/enduring-freedom-of-information-wikileaks/>
  - Wayback: <https://web.archive.org/web/2010/https://wauland.de/en/projects/enduring-freedom-of-information-wikileaks/>
  > Wau Holland Stiftung's own project-04 ("Enduring Freedom of
> Information / WikiLeaks") project page documents the foundation
> accepting WikiLeaks-earmarked donations during 2010 and the
> subsequent multi-year negotiation with German tax authorities
> over gemeinnuetzig status. This is the affected-entity
> primary-corporate pin for the donation-forwarding-disruption
> effect, even though the formal Kassel revocation letter is not
> publicly archived.
- **`supporting_journalism`**
  - URL: <https://www.weeklystandard.com/john-rosenthal/tax-deductible-wikileaks>
  - Wayback: <https://web.archive.org/web/2010/https://www.weeklystandard.com/john-rosenthal/tax-deductible-wikileaks>
  > Contemporaneous English-language reporting ("Tax Deductible
> WikiLeaks") on the Wau Holland Foundation's role as the EU-wide
> tax-deductible donation channel for WikiLeaks, and on the
> German-tax-authority pushback that began in late 2010.
> Independent journalism pin on the actor (Finanzamt Kassel) and
> the underlying gemeinnuetzig-status question.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Wau Holland Stiftung (Wau Holland Foundation), project-04 "Enduring Freedom of Information / WikiLeaks"

> Subset: the single affected entity is the Wau Holland Stiftung
> (Wau Holland Foundation), a German gemeinnuetzige Stiftung based
> in Hamburg / Kassel that operated project-04 "Enduring Freedom of
> Information" as the EU-wide tax-deductible donation channel for
> WikiLeaks during 2009-2010. Not enumerated: other German charitable
> foundations forwarding WikiLeaks-adjacent donations (no
> contemporaneous evidence of class-wide Finanzamt sweep beyond Wau
> Holland). Effect-on-WikiLeaks-donations is one step downstream:
> the tax-status challenge disrupted the German-jurisdiction
> tax-deductible donation rail that WikiLeaks had been promoting via
> the Wau Holland project-04 page.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `finanzamt_kassel_challenges_wau_holland_2010_gemeinnuetzig_status_disrupting_wikileaks_donation_channel`

**Timestamp**: `2010-12-15 00:00:00+00:00` (precision: `week`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://en.wikipedia.org/wiki/Wau_Holland_Foundation>
  - Wayback: <https://web.archive.org/web/20110107193603/https://en.wikipedia.org/wiki/Wau_Holland_Foundation>
  - body_hash: `sha256:e4004ff8935de24162d30709abeb01177562b3e6e7960aaf893a4b625f3d2351`
  - body_path: `sources/http_captures/wikileaks-wau-holland-tax-status-challenge-2010-12/primary/web.archive.org__web-20110107193603-https-en.wikipedia.org-wiki-Wau_Holland_Foundation__23d5498fbe.html`
  > Tertiary-source consolidation of the Finanzamt Kassel review
> opening (December 2010) and the January 2011 formal
> revocation letter ("wegen Verstosses gegen das Gebot der
> Selbstlosigkeit"). attribution=plausible (not direct) per
> codebook §1: the actor (Finanzamt Kassel) is identified and
> the effect (disruption of the WikiLeaks donation forwarding
> channel) is consistent with the trigger, but no primary-
> legal pin on the Kassel letter itself is publicly archived;
> the link from review-opening to donation-channel disruption
> is one-step inferential rather than directly attested in a
> single primary document.
- **`primary_corporate`**
  - URL: <http://www.wauland.de/de/projekte/WikiLeaks/2017-12-26_Statement.html>
  - Wayback: <https://web.archive.org/web/20171227213018/http://www.wauland.de/de/projekte/WikiLeaks/2017-12-26_Statement.html>
  - body_hash: `sha256:29ae37cefe648f3306e8bd6f8fe0358ad230da3de3d26fb572a7baf8c65c69c3`
  - body_path: `sources/http_captures/wikileaks-wau-holland-tax-status-challenge-2010-12/primary/web.archive.org__web-20171227213018-http-www.wauland.de-de-projekte-WikiLeaks-2017-12-26_Statement.html__8c034d015d.html`
  > Wau Holland Stiftung WikiLeaks-project statement page (affected-
> entity primary-corporate pin). The foundation documents its
> WikiLeaks donation-forwarding role, the Finanzamt Kassel
> gemeinnuetzig (charitable-status) challenge, and the donation
> handling. The original 2010 /en/ project page is not in the
> Wayback Machine; this 2017-12-26 foundation statement (Wayback
> 20171227213018) is the earliest archivable foundation-authored
> page substantiating the same WikiLeaks/tax-status facts.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-paypal-freeze-2010-12`](./wikileaks-paypal-freeze-2010-12.md)
- [`wikileaks-postfinance-account-closure-2010-12`](./wikileaks-postfinance-account-closure-2010-12.md)
- [`wikileaks-bank-of-america-block-2010-12`](./wikileaks-bank-of-america-block-2010-12.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `6678414`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

