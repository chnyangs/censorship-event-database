# Evidence chain — `eu-belarus-crypto-services-ban-2022`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `661a63f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Regulation 2022/398 of 2022-03-09 (fifth Belarus sanctions
> package) clarifies that EU financial-sector restrictive measures on
> Belarus extend to crypto-assets (transferable-securities definitional
> clarification + loans/credit by-any-means including crypto) but does
> not introduce a dedicated Belarus crypto-wallet-cap article parallel
> to Regulation 2022/576 Article 5b on the Russia track. No load-bearing
> observed_change layer is pinned at this audit; the event is recorded
> as null_case for denominator-control purposes in the S6_supranational
> stratum."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2022-03-09 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2022/398/oj/eng>
  - Wayback: <https://web.archive.org/web/20241227061741/https://eur-lex.europa.eu/eli/reg/2022/398/oj/eng>
  - body_hash: `sha256:12688084dc441f0cbe97b3c315b0742204afd036d28182a2bf6fa9bfe4ac6cd9`
  - body_path: `sources/http_captures/eu-belarus-crypto-services-ban-2022/primary/web.archive.org__web-20241227061741-https-eur-lex.europa.eu-eli-reg-2022-398-oj-eng__5a92086b90.html`
  > Council Regulation (EU) 2022/398 of 9 March 2022 amending Regulation
> (EC) No 765/2006 concerning restrictive measures in view of the
> situation in Belarus and the involvement of Belarus in the Russian
> aggression against Ukraine. Fifth EU sanctions package against
> Belarus. Crypto-relevant clarifications: the Regulation clarifies
> that the notion of 'transferable securities' clearly includes
> crypto-assets and that loans / credit measures cover provision by
> any means including crypto-assets; aligns Belarus measures with
> the parallel Russia regime under Regulation 833/2014. URL changed
> from CELEX HTML form to ELI/OJ form during audit because CELEX HTML
> URL has no Wayback memento; the ELI/OJ form Wayback memento
> 20241227061741 captured 2026-05-21 with replayable body_hash
> sha256:12688084dc44... is the canonical anchor.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2022/03/09/eu-says-russia-belarus-sanctions-extend-to-crypto>
  - Wayback: <https://web.archive.org/web/20220309130110/https://www.coindesk.com/policy/2022/03/09/eu-says-russia-belarus-sanctions-extend-to-crypto>
  - body_hash: `sha256:356edd79abafcdde502eb075e59d8c213cc19eb52f1ced7d4c36104c709a93c6`
  - body_path: `sources/http_captures/eu-belarus-crypto-services-ban-2022/primary/web.archive.org__web-20220309130110-https-www.coindesk.com-policy-2022-03-09-eu-says-russia-belarus-sanctions-extend-to-crypto__d8695a9e3b.html`
  > CoinDesk 2022-03-09 reporting that the EU sanctions package
> adopted that day (covering both Russia and Belarus tracks)
> explicitly extends to crypto-assets. Corroborates the legal
> instrument's crypto-clarification scope. Wayback memento
> 20220309130110 captured 2026-05-21.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Belarusian nationals / residents / entities subject to EU sanctions crypto-asset clarifications

> Belarusian nationals, Belarusian residents, and legal persons /
> entities / bodies established in Belarus, addressed via EU-operating
> financial-service and crypto-asset-service providers. Article 1z of
> amended Regulation 765/2006 caps EU acceptance of deposits exceeding
> EUR 100,000 from Belarusian persons; the Regulation also clarifies
> that 'transferable securities' and the loans/credit measures cover
> crypto-assets, aligning Belarus measures with the parallel Russia
> regime. The target is a user class identified through CASP / bank
> KYC rather than wallet-level addresses; no on-chain address
> enumeration. Belarus is not in the project jurisdiction enum;
> jurisdiction encodes [EU, RU] to reflect the EU issuer plus the
> sibling-package alignment with the Russia track (Belarus operating
> as Russia's co-belligerent under the same OJ adoption window).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_load_bearing_observed_change_pinned_for_belarus_track_in_dryrun_pass`

**Window**: `2022-03-09 00:00:00+00:00` → `2022-10-06 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2022/398/oj/eng>
  - Wayback: <https://web.archive.org/web/20241227061741/https://eur-lex.europa.eu/eli/reg/2022/398/oj/eng>
  - body_hash: `sha256:12688084dc441f0cbe97b3c315b0742204afd036d28182a2bf6fa9bfe4ac6cd9`
  - body_path: `sources/http_captures/eu-belarus-crypto-services-ban-2022/primary/web.archive.org__web-20241227061741-https-eur-lex.europa.eu-eli-reg-2022-398-oj-eng__5a92086b90.html`
  > Council Regulation (EU) 2022/398 of 2022-03-09 amending
> Regulation 765/2006 (Belarus sanctions). Crypto-asset
> clarifications: 'transferable securities' clearly includes
> crypto-assets; loans/credit measures cover provision by any
> means including crypto-assets. No dedicated Belarus crypto-
> wallet-cap article (unlike the parallel Russia track's
> Regulation 2022/576 Article 5b). EU CASP / bank operator
> reactions on Belarusian-customer surfaces have not been
> captured with replayable artifacts this audit; the offramp_cex
> row records observed_no_change rather than observed_change,
> marking the event as a null_case denominator row pending future
> Wayback-capture work. EUR-Lex Wayback memento 20241227061741
> captured 2026-05-21 anchors the row.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): EU-operating CASPs plausibly added Belarusian-user-restriction

## 7. Related events

- [`eu-russia-crypto-wallet-cap-2022`](./eu-russia-crypto-wallet-cap-2022.md)
- [`eu-russia-full-crypto-wallet-ban-2022`](./eu-russia-full-crypto-wallet-ban-2022.md)
- [`eu-12th-russia-sanctions-2023`](./eu-12th-russia-sanctions-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `661a63f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

