# Evidence chain — `wikileaks-paypal-freeze-2010-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `6678414` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-04T04:52:47Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2010-12-04, PayPal permanently restricted the WikiLeaks
> donation merchant account (registered to the Wau-Holland-Stiftung
> pass-through), citing its Acceptable Use Policy prohibition on
> facilitating activities determined illegal. PayPal VP Osama Bedier
> subsequently (2010-12-08, Le Web Paris) acknowledged that a US
> State Department determination that WikiLeaks' activities were
> illegal under US law informed the decision. The freeze is the
> pre-Bitcoin conceptual analog of an offramp_cex / payment-rail
> closure (the only observed cascade axis in 2010 in the absence of
> any blockchain-asset substrate for WikiLeaks donations).
> Observational axis at offramp_cex (load-bearing,
> attribution=direct via PayPal's own corporate statement).
> Admission-anchor-grade promotion pending pinned archive captures."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `PAYPAL_OPERATOR`
- **Timestamp**: `2010-12-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.thepaypalblog.com/2010/12/why-paypal-restricted-wikileaks-account/>
  - Wayback: <https://web.archive.org/web/2010/https://www.thepaypalblog.com/2010/12/why-paypal-restricted-wikileaks-account/>
  > PayPal blog post 2010-12-04 ("Why PayPal restricted WikiLeaks
> account"). PayPal stated that the WikiLeaks account had been
> permanently restricted for violation of PayPal's Acceptable Use
> Policy "which states that our payment service cannot be used for
> any activities that encourage, promote, facilitate or instruct
> others to engage in illegal activity." The blog item is the
> corporate-statement anchor for the freeze action; the technical
> platform action (donate-button stopped collecting funds for
> Wau-Holland-Stiftung -> WikiLeaks routing) was effective the same
> day. DRYRUN: wayback wildcard pointer in lieu of pinned-timestamp
> snapshot; evidence_use=contextual_unarchived because no
> body_hash+body_path pair has been captured into
> sources/http_captures/wikileaks-paypal-freeze-2010-12/ in this
> session.
- **`supporting_journalism`**
  - URL: <https://www.cnn.com/2010/US/12/04/wikileaks.pay.pal/index.html>
  - Wayback: <https://web.archive.org/web/2010/https://www.cnn.com/2010/US/12/04/wikileaks.pay.pal/index.html>
  > CNN 2010-12-04 coverage ("WikiLeaks loses PayPal revenue
> service"). Independent confirmation of the trigger date and the
> platform-action scope: WikiLeaks donation account permanently
> restricted, donate button stopped collecting for the
> Wau-Holland-Stiftung pass-through to WikiLeaks.
- **`supporting_journalism`**
  - URL: <https://www.bloomberg.com/news/articles/2010-12-04/paypal-restricts-wikileaks-account-as-website-comes-under-global-scrutity>
  - Wayback: <https://web.archive.org/web/2010/https://www.bloomberg.com/news/articles/2010-12-04/paypal-restricts-wikileaks-account-as-website-comes-under-global-scrutity>
  > Bloomberg 2010-12-04 coverage ("PayPal Cuts WikiLeaks' Access to
> Funds Amid Global Scrutiny"). Second independent journalism
> confirmation of the 2010-12-04 freeze date and platform action.
- **`supporting_journalism`**
  - URL: <https://techcrunch.com/2010/12/08/paypal-wikileaks/>
  - Wayback: <https://web.archive.org/web/2010/https://techcrunch.com/2010/12/08/paypal-wikileaks/>
  > TechCrunch 2010-12-08 coverage of PayPal VP Osama Bedier's Le Web
> Paris conference admission that PayPal's freeze decision was
> influenced by a US State Department determination that
> WikiLeaks' activities were illegal under US law (the State
> Department letter, dated 2010-11-27, was sent to WikiLeaks
> rather than to PayPal; Bedier clarified PayPal was not directly
> contacted by any government agency). The Bedier admission is the
> single most-cited corporate-statement anchor in the academic
> literature on the 2010 WikiLeaks payment-rail blockade.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: WikiLeaks (donation pass-through via Wau-Holland-Stiftung)

> WikiLeaks donation pass-through PayPal account, registered to the
> Wau-Holland-Stiftung (a German non-profit foundation that operated
> as the legal/financial pass-through for WikiLeaks donations during
> 2010). Subset because the enumerated target is the single PayPal
> merchant account used by WikiLeaks for donation collection; the
> broader exclusion class is any future or alternate PayPal merchant
> account that WikiLeaks (or a successor pass-through) might attempt
> to open, given PayPal's stated Acceptable Use Policy basis for the
> permanent restriction.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `paypal_permanently_restricted_wikileaks_donation_merchant_account`

**Timestamp**: `2010-12-04 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.wikileaks.org/PayPal-freezes-WikiLeaks-donations.html>
  - Wayback: <https://web.archive.org/web/20110527212402/http://www.wikileaks.org/PayPal-freezes-WikiLeaks-donations.html>
  - body_hash: `sha256:176da1f635a85725bb3971a31c4a97abc29e332b7a7a84d092aa2417282ace67`
  - body_path: `sources/http_captures/wikileaks-paypal-freeze-2010-12/primary/web.archive.org__web-20110527212402-http-www.wikileaks.org-PayPal-freezes-WikiLeaks-donations.html__e523effd2c.html`
  > WikiLeaks official statement page documenting PayPal's
> 2010-12-04 permanent restriction of the WikiLeaks donation
> merchant account (operated by the Wau Holland Stiftung).
> Affected-org primary account of the offramp_cex freeze.
> attribution=direct: PayPal publicly confirmed the action; this
> page records it contemporaneously. The original PayPal corporate
> blog post is no longer in the Wayback Machine. Wayback
> 20110527212402 pinned.
- **`semi_primary_wayback`**
  - URL: <https://www.bloomberg.com/news/articles/2010-12-04/paypal-restricts-wikileaks-account-as-website-comes-under-global-scrutity>
  - Wayback: <https://web.archive.org/web/20150413182628/http://www.bloomberg.com/news/articles/2010-12-04/paypal-restricts-wikileaks-account-as-website-comes-under-global-scrutity>
  - body_hash: `sha256:df106cc72bf4a547cb815aa1420f505d1019160a90396c7b602addbc460dffb5`
  - body_path: `sources/http_captures/wikileaks-paypal-freeze-2010-12/primary/web.archive.org__web-20101205000000-https-www.bloomberg.com-news-articles-2010-12-04-paypal-restricts-wikileaks-account-as-website-comes-under-global-scrutity__b6ac26fa6c.html`
  > Bloomberg 2010-12-04 coverage: PayPal cut WikiLeaks' access to
> funds, citing Acceptable-Use-Policy violation. Independent
> first semi-primary anchor.
- **`semi_primary_wayback`**
  - URL: <https://www.csmonitor.com/Technology/Horizons/2010/1208/Why-did-PayPal-ditch-WikiLeaks-The-State-Department-asked-it-to>
  - Wayback: <https://web.archive.org/web/20150911222850/http://www.csmonitor.com/Technology/Horizons/2010/1208/Why-did-PayPal-ditch-WikiLeaks-The-State-Department-asked-it-to>
  - body_hash: `sha256:467aa4a7ba4a4a60d9fa775a99e9b4d63ce7567268b6ddd13e4a4c63a9ae4555`
  - body_path: `sources/http_captures/wikileaks-paypal-freeze-2010-12/primary/web.archive.org__web-20101209000000-https-www.csmonitor.com-Technology-Horizons-2010-1208-Why-did-PayPal-ditch-WikiLeaks-The-State-Department-asked-it-to__7e9b4f2d48.html`
  > Christian Science Monitor 2010-12-08 coverage recording PayPal
> VP Osama Bedier's Le Web admission that the US State Department
> determination informed the AUP enforcement decision. Independent
> second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`wikileaks-visa-europe-suspension-2010-12`](./wikileaks-visa-europe-suspension-2010-12.md)
- [`wikileaks-mastercard-suspension-2010-12`](./wikileaks-mastercard-suspension-2010-12.md)
- [`wikileaks-bank-of-america-block-2010-12`](./wikileaks-bank-of-america-block-2010-12.md)
- [`wikileaks-western-union-interdiction-2010-12`](./wikileaks-western-union-interdiction-2010-12.md)
- [`wikileaks-postfinance-account-closure-2010-12`](./wikileaks-postfinance-account-closure-2010-12.md)
- [`wikileaks-amazon-aws-eviction-2010-12`](./wikileaks-amazon-aws-eviction-2010-12.md)
- [`wikileaks-everydns-domain-termination-2010-12`](./wikileaks-everydns-domain-termination-2010-12.md)
- [`datacell-v-valitor-iceland-district-court-2012-07`](./datacell-v-valitor-iceland-district-court-2012-07.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `6678414`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

