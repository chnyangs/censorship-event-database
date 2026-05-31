# Evidence chain — `russia-rosfinmonitoring-binance-russia-rails-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e405eb6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "No replayable Rosfinmonitoring formal enforcement artifact
> against Binance's Russia-facing RUB / P2P offramp rails during
> the 2022 calendar window has been identified at the 2026-05-17
> authoring date. The adjacent Reuters-reported April-2021
> Kostarev–Rosfin data-sharing arrangement (pre-2022), Binance's
> voluntary April-2022 EU-sanctions-driven Russia restrictions,
> and the August-2023 P2P sanctioned-bank delistings do not
> evidence a 2022 Rosfin-initiated ruble-rail enforcement order.
> Coded null_event / null_case as a S4_nation_state Russia-axis
> denominator control, sibling to russia-cbr-crypto-payment-ban-2022
> and parent to binance-russia-exit-commex-2023."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `RU_ROSFINMONITORING`
- **Timestamp**: `2022-01-01 00:00:00+00:00` (precision: `week`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.reuters.com/investigates/special-report/finance-crypto-binance-russia/>
  - Wayback: <https://web.archive.org/web/2022/https://www.reuters.com/investigates/special-report/finance-crypto-binance-russia/>
  > Reuters Special Report (2022-04-22) "How crypto giant Binance
> built ties to a Russian FSB-linked agency", reporting on the
> April 2021 meeting between Binance's Gleb Kostarev and
> Rosfinmonitoring at which Kostarev reportedly agreed to share
> client data. The Reuters reporting documents an informal,
> bilateral data-sharing arrangement preceding 2022 but does NOT
> evidence any 2022 formal Rosfin enforcement order against
> Binance ruble-rail / P2P operations. Used here as
> contextual_unarchived background anchoring the null_event
> posture. DRYRUN stub; replace with verified Wayback +
> body_hash / body_path capture during real human audit.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/business/2022/04/22/binance-denies-allegations-it-shared-russian-users-data-with-law-enforcement/>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/business/2022/04/22/binance-denies-allegations-it-shared-russian-users-data-with-law-enforcement/>
  > CoinDesk (2022-04-22) reporting Binance's public denial of the
> Reuters allegations regarding Rosfinmonitoring data-sharing.
> Used as a second contextual_unarchived anchor: Binance
> publicly contests the framing of any formal Rosfin
> compulsion, and no Rosfin-issued formal order / notice / fine
> / administrative ruling against Binance ruble rails has been
> identified in the 2022 calendar window. DRYRUN stub.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/leadership/binance--russia-openness-transparency-and-honesty-421499824684903741>
  - Wayback: <https://web.archive.org/web/20220425013842/https://www.binance.com/en/blog/leadership/binance--russia-openness-transparency-and-honesty-421499824684903741>
  - body_hash: `sha256:fc433e064fc72f12d97869e1832f7e597cb2d30fe4df44515317c2f8e7205276`
  - body_path: `sources/http_captures/russia-rosfinmonitoring-binance-russia-rails-2022/v0_3_primary_repair/web.archive.org__web-20220425000000-https-www.binance.com-en-blog-leadership-binance--russia-openness-transparency-and-honesty-421499824684903741__623eb4ba82.html`
  > Binance official blog post "Binance & Russia: Openness,
> Transparency and Honesty" archived by Wayback on
> 2022-04-25. Binance directly denies that it shared user
> data with Russian FSB-controlled agencies or regulators,
> states that it decided not to proceed with a Rosfin working
> group, and publishes its responses to Reuters questions about
> Rosfinmonitoring. Added in v0.3 primary-observation repair as
> a corporate primary source for the null posture; it supports
> the absence of a publicly acknowledged 2022 Rosfin order
> against Binance ruble/P2P rails, not the truth of every
> contested factual claim between Reuters and Binance.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance Russia-facing RUB / P2P operations (binance.com)
- **Canonical domains**: `binance.com`

> Nominal target: Binance's Russia-facing ruble-rail / RUB P2P
> operations during the 2022 calendar year. Class-level scope:
> Binance Russia-facing offramp_cex surface (binance.com RUB
> fiat onramp, Binance P2P RUB pairs, sanctioned-bank rail
> coverage). Self-custody and non-Binance ruble venues
> (Bybit, Garantex, ByBit P2P, Russian banks' own
> crypto-adjacent rails) are outside this row's scope. Per
> codebook §7 coded `subset` (no `class_level` enumeration
> value); class-level rationale documented here.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `rosfinmonitoring_binance_ruble_rails_no_specific_2022_enforcement_identified`

**Window**: `2022-01-01 00:00:00+00:00` → `2022-12-31 23:59:59+00:00`

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.reuters.com/investigates/special-report/finance-crypto-binance-russia/>
  - Wayback: <https://web.archive.org/web/2022/https://www.reuters.com/investigates/special-report/finance-crypto-binance-russia/>
  > Reuters Special Report (2022-04-22) documents the April-2021
> Kostarev–Rosfin meeting and informal data-sharing
> arrangement; it does NOT report any Rosfin-initiated formal
> enforcement order against Binance ruble rails in 2022.
> Used here as contextual_unarchived anchor for the
> null-event posture.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/04/22/binance-denies-allegations-it-shared-russian-users-data-with-law-enforcement/>
  - Wayback: <https://web.archive.org/web/20220422201638/https://www.coindesk.com/business/2022/04/22/binance-denies-allegations-it-shared-russian-users-data-with-law-enforcement/>
  - body_hash: `sha256:5d8ee1a73f2b8a6a733d89520fa03a35e9940692f446ee3fa89ca6ccc9cd821e`
  - body_path: `sources/http_captures/russia-rosfinmonitoring-binance-russia-rails-2022/primary/web.archive.org__web-20220422201638-https-www.coindesk.com-business-2022-04-22-binance-denies-allegations-it-shared-russian-users-data-with-law-enforcement__077747abc5.html`
  > CoinDesk (2022-04-22) Binance public denial. Reinforces
> the null-event posture: Binance contests the existence of
> a formal Rosfin compulsion and no Rosfin enforcement
> artifact has surfaced in the 2022 window.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/leadership/binance--russia-openness-transparency-and-honesty-421499824684903741>
  - Wayback: <https://web.archive.org/web/20220425013842/https://www.binance.com/en/blog/leadership/binance--russia-openness-transparency-and-honesty-421499824684903741>
  - body_hash: `sha256:fc433e064fc72f12d97869e1832f7e597cb2d30fe4df44515317c2f8e7205276`
  - body_path: `sources/http_captures/russia-rosfinmonitoring-binance-russia-rails-2022/v0_3_primary_repair/web.archive.org__web-20220425000000-https-www.binance.com-en-blog-leadership-binance--russia-openness-transparency-and-honesty-421499824684903741__623eb4ba82.html`
  > Binance's own 2022-04-25 response to Reuters says Binance
> had not entered into a Russia-specific data-sharing
> arrangement, had decided not to proceed with a Rosfin
> working group, and would only share data through ordinary
> law-enforcement request procedures after legal review. This
> is primary corporate evidence for the null observation that
> no public 2022 Rosfin-initiated formal enforcement order
> against Binance RUB/P2P rails was identified. It remains a
> contested-party statement and therefore does not by itself
> prove the Reuters factual dispute false.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`russia-cbr-crypto-payment-ban-2022`](./russia-cbr-crypto-payment-ban-2022.md)
- [`binance-russia-exit-commex-2023`](./binance-russia-exit-commex-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e405eb6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

