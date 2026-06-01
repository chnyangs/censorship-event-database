# Evidence chain — `celsius-bankruptcy-mashinsky-doj-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `a7b40fe` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-07-13 coordinated DOJ + SEC + CFTC + FTC actions against
> Celsius Network and Alex Mashinsky codify a single-layer offramp_cex
> cascade: the centralized lending platform's withdraw-freeze (2022-06-12)
> and Chapter 11 collapse (2022-07-13) are legally disposed via criminal
> indictment + securities-fraud + commodity-pool + FTC consumer-protection
> parallels. Lender variant of the FTX twin; structurally narrower than
> the FTX exchange-plus-lender cascade."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_SDNY`
- **Timestamp**: `2023-07-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-executive-officer-celsius-network-limited-charged-multi>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-executive-officer-celsius-network-limited-charged-multi>
  > DOJ SDNY press release (2023-07-13): "Founder And Former Chief Executive
> Officer Of Celsius Network Limited Charged With Multi-Billion Dollar
> Fraud And Market Manipulation Schemes." Seven-count criminal indictment
> unsealed against Alex Mashinsky (Celsius founder/former CEO) charging
> securities fraud, commodities fraud, wire fraud, conspiracy to commit
> securities/commodities/wire fraud, market manipulation, and manipulation
> of a security. Co-defendant Roni Cohen-Pavon (former CRO) charged in
> parallel. Filed exactly 1 year after Celsius's 2022-07-13 Chapter 11
> bankruptcy petition; freeze of customer withdrawals occurred
> 2022-06-12, 31 days prior to the bankruptcy.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-127>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/news/press-release/2023-127>
  > SEC press release 2023-127 (2023-07-13): "SEC Charges Alex Mashinsky
> and Celsius Network Limited with Fraud and Unregistered Offer and
> Sale of Securities." SEC civil action in SDNY alleging Celsius's
> Earn Interest Account program constituted unregistered securities
> offerings and that Mashinsky misled investors about Celsius's core
> business and financial condition, including manipulation of CEL
> token price. Same-day parallel to DOJ indictment.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8758-23>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8758-23>
  > CFTC press release 8758-23 (2023-07-13): "CFTC Charges Alexander
> Mashinsky and Celsius Network LLC With Fraud and Material
> Misrepresentations in Massive Commodity Pool Scheme." Civil
> enforcement alleging Celsius operated an unregistered commodity
> pool and that Mashinsky made material misrepresentations about
> Celsius's safety and profitability. Same-day parallel.
- **`primary_legal`**
  - URL: <https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-action-leads-record-47-billion-imposed-judgment-against-crypto-platform-celsius>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-action-leads-record-47-billion-imposed-judgment-against-crypto-platform-celsius>
  > FTC press release (2023-07-13): "FTC Action Leads to Record $4.7
> Billion Imposed Judgment Against Crypto Platform Celsius." FTC
> secured a record-breaking imposed judgment (largest in FTC history
> at that time) against Celsius Network's holding companies, alleging
> the platform deceived consumers and unfairly endangered customer
> deposits. Same-day fourth-framework parallel.
- **`primary_legal`**
  - URL: <https://cases.stretto.com/celsius/>
  - body_hash: `sha256:b889e7875b38b8d0ad0f91f7f24388aa1f36b0af797d1ff4c094f032ac0c74f6`
  - body_path: `sources/http_captures/celsius-bankruptcy-mashinsky-doj-2023/v0_3_repair/cases.stretto.com__celsius__f15ad87980.html`
  > Celsius Network bankruptcy docket (Case No. 22-10964, S.D.N.Y.
> Bankruptcy Court): Chapter 11 petition filed 2022-07-13; the criminal
> indictment one year later runs in parallel with the ongoing
> reorganization proceedings. Pinned here as bankruptcy-context
> anchor; no specific docket entry is retained for this DRYRUN row.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Celsius Network + Alex Mashinsky + Roni Cohen-Pavon
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `celsius.network`

> Celsius Network Limited / Celsius Network LLC / Celsius Network Inc.
> (collectively "Celsius") plus founder/former CEO Alexander Mashinsky
> and former Chief Revenue Officer Roni Cohen-Pavon as named criminal
> defendants. Celsius's Earn Interest Account product and CEL token are
> the named securities/commodities. Civil parallels target Celsius entity
> + Mashinsky individually (SEC, CFTC) and Celsius holding companies
> (FTC). Off-ramp surface had already collapsed pre-indictment:
> withdraw-freeze 2022-06-12, Chapter 11 petition 2022-07-13. No on-chain
> address set; charges operate at lending-product + token-issuance +
> fraud-disclosure level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `celsius_lending_platform_collapse_codified_by_doj_sec_cftc_ftc_actions`

**Timestamp**: `2023-07-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-executive-officer-celsius-network-limited-charged-multi>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/usao-sdny/pr/founder-and-former-chief-executive-officer-celsius-network-limited-charged-multi>
  > DOJ SDNY indictment recites the Celsius withdraw-freeze
> (2022-06-12), the Chapter 11 filing (2022-07-13), and the alleged
> CEL-token market manipulation. The 7-count indictment forecloses
> executive recovery of operational control over the platform.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-127>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/news/press-release/2023-127>
  > SEC press release anchors the Earn Interest Account as an
> unregistered securities offering and ties Mashinsky's
> misrepresentations to the platform-level customer-deposit
> collapse.
- **`primary_legal`**
  - URL: <https://www.cftc.gov/PressRoom/PressReleases/8758-23>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.cftc.gov/PressRoom/PressReleases/8758-23>
  > CFTC press release anchors the commodity-pool framing and the
> material-misrepresentation conduct, complementing the SEC
> securities-law axis with the commodities-law axis.
- **`primary_legal`**
  - URL: <https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-action-leads-record-47-billion-imposed-judgment-against-crypto-platform-celsius>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-action-leads-record-47-billion-imposed-judgment-against-crypto-platform-celsius>
  > FTC press release records the record $4.7B imposed judgment
> (largest in FTC history at the time) against Celsius's holding
> companies, completing the four-framework codification of the
> platform collapse.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No admission-grade L4 frontend diff is retained at the indictment

## 7. Related events

- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)
- [`genesis-sec-gemini-earn-2023`](./genesis-sec-gemini-earn-2023.md)
- [`ftx-bankman-fried-doj-2022`](./ftx-bankman-fried-doj-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a7b40fe`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

