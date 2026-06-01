# Evidence chain — `ripple-fincen-xrp-2015`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b524247` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> FinCEN's 2015-05-05 settlement with Ripple Labs Inc. and XRP II, LLC
> ($700,000 civil monetary penalty + non-prosecution agreement with
> US Attorney's Office N.D. Cal.) was the FIRST civil enforcement action
> by FinCEN against a virtual-currency exchanger and imposed by consent
> a structural overhaul of XRP II's BSA / AML compliance program
> (MSB registration, SAR retroactive review, customer-identification
> program, independent reviewer). The offramp_cex layer carries the
> load-bearing direct-attribution observation; other layers are
> not_applicable on construct-out-of-scope or construct-did-not-exist
> grounds.

## 1. Trigger

- **Type**: `fincen_action`
- **Actor**: `US_FINCEN`
- **Timestamp**: `2015-05-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual>
  - Wayback: <https://web.archive.org/web/20260516024709/https://www.fincen.gov/news/news-releases/fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual>
  - body_hash: `sha256:d2d4e482f4de604c69a45dab779b29cb72933f8bdd6b77124255d8582e202f8c`
  - body_path: `sources/http_captures/ripple-fincen-xrp-2015/primary/www.fincen.gov__news-news-releases-fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual__5fd00ced6f.html`
  > FinCEN press release dated 2015-05-05: "FinCEN Fines Ripple Labs
> Inc. in First Civil Enforcement Action Against a Virtual Currency
> Exchanger." Announced jointly with the US Attorney's Office for
> the Northern District of California. Core terms: (1) $700,000
> civil monetary penalty assessed by FinCEN against Ripple Labs
> Inc. and its wholly-owned subsidiary XRP II, LLC for willful
> violations of the Bank Secrecy Act (BSA), including (a) acting
> as a money services business (MSB) without registering with
> FinCEN, and (b) failing to implement and maintain an adequate
> anti-money-laundering (AML) program in connection with the sale
> of XRP virtual currency; (2) settlement agreement requiring
> Ripple Labs and XRP II to undertake remedial measures including
> appointment of an independent reviewer, enhanced AML program,
> SAR retroactive review, and structural compliance changes; (3)
> a separate non-prosecution agreement (NPA) with the US Attorney's
> Office N.D. Cal. resolving the criminal investigation, conditioned
> on the FinCEN settlement and on Ripple's adoption of the
> compliance undertakings. This is the FIRST civil enforcement
> action by FinCEN against a virtual-currency exchanger and a
> canonical historical-baseline anchor for the
> FinCEN-as-virtual-currency-regulator posture established under
> the 2013-03-18 FinCEN guidance (FIN-2013-G001).
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-ndca/pr/ripple-labs-inc-resolves-criminal-investigation>
  - Wayback: <https://web.archive.org/web/20260516024821/https://www.justice.gov/usao-ndca/pr/ripple-labs-inc-resolves-criminal-investigation>
  - body_hash: `sha256:066ed416eec851a73a57a8d20af7152539cee1b7728844f62e96114b19dcfb8e`
  - body_path: `sources/http_captures/ripple-fincen-xrp-2015/primary/www.justice.gov__usao-ndca-pr-ripple-labs-inc-resolves-criminal-investigation__b6061d36f1.html`
  > DOJ / US Attorney's Office N.D. Cal. press release page on the
> Ripple Labs criminal investigation resolution. The live
> justice.gov URL currently returns a thin shell (post-2017 DOJ
> CMS migration drift), so the load-bearing content is anchored
> via the Wayback snapshot pinned above and corroborated by the
> FinCEN press release primary anchor. The DOJ resolution
> announced concurrently with the FinCEN settlement on
> 2015-05-05 took the form of a non-prosecution agreement (NPA)
> for willful BSA violations, conditioned on the FinCEN
> settlement and on Ripple's adoption of the compliance
> undertakings.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Ripple Labs Inc. + XRP II, LLC
- **Chains**: `xrp`
- **Canonical domains**: `ripple.com`

> Two named legal entities: Ripple Labs Inc. (parent) and XRP II, LLC
> (wholly-owned subsidiary that conducted XRP sales). No on-chain
> addresses enumerated in the FinCEN action — the BSA violation theory
> is registration-and-AML-program-failure at the entity level rather
> than address-level designation. Load-bearing target for measurable
> cascade is XRP II as the FinCEN-recognized MSB whose post-settlement
> compliance program is the offramp_cex layer signal.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `xrp_ii_registered_as_msb_and_aml_program_imposed_by_consent`

**Timestamp**: `2015-05-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual>
  - Wayback: <https://web.archive.org/web/20260516024709/https://www.fincen.gov/news/news-releases/fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual>
  - body_hash: `sha256:d2d4e482f4de604c69a45dab779b29cb72933f8bdd6b77124255d8582e202f8c`
  - body_path: `sources/http_captures/ripple-fincen-xrp-2015/primary/www.fincen.gov__news-news-releases-fincen-fines-ripple-labs-inc-first-civil-enforcement-action-against-virtual__5fd00ced6f.html`
  > FinCEN press release is the legal instrument. Settlement terms
> require Ripple Labs and XRP II to (a) register XRP II as an
> MSB with FinCEN, (b) implement a written AML program with
> designated compliance officer, (c) conduct retroactive SAR
> review of prior transactions, (d) implement KYC / customer
> identification program, and (e) engage an independent reviewer
> to validate the compliance posture. Direct attribution: the
> settlement and assessment-of-civil-money-penalty text name
> these mandates as conditions of resolution.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-ndca/pr/ripple-labs-inc-resolves-criminal-investigation>
  - Wayback: <https://web.archive.org/web/20260516024821/https://www.justice.gov/usao-ndca/pr/ripple-labs-inc-resolves-criminal-investigation>
  - body_hash: `sha256:066ed416eec851a73a57a8d20af7152539cee1b7728844f62e96114b19dcfb8e`
  - body_path: `sources/http_captures/ripple-fincen-xrp-2015/primary/www.justice.gov__usao-ndca-pr-ripple-labs-inc-resolves-criminal-investigation__b6061d36f1.html`
  > DOJ N.D. Cal. press release corroborating the concurrent
> non-prosecution agreement on the willful BSA violations,
> conditioned on the FinCEN settlement and on Ripple's
> adoption of the compliance undertakings. The live
> justice.gov page is presently a thin shell after a DOJ CMS
> migration; load-bearing content is anchored via the pinned
> Wayback snapshot.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b524247`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

