# Evidence chain — `genesis-sec-gemini-earn-2023`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e43eea7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-01-12 SEC Genesis + Gemini complaint over the Gemini Earn
> program is coded only as a centralized crypto lending-product
> restriction at the offramp_cex layer, paired with the 2023-01-19
> Genesis Chapter 11 estate freeze of approximately $900M of customer
> crypto held for ~340K Gemini Earn investors; it does not claim a
> frontend, L1, L3, or on-chain censorship event."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2023-01-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-7>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/news/press-release/2023-7>
  > SEC press release 2023-7 (2023-01-12): "SEC Charges Genesis and
> Gemini for the Unregistered Offer and Sale of Crypto Asset
> Securities through the Gemini Earn Lending Program." The SEC's
> civil complaint charges Genesis Global Capital, LLC and Gemini
> Trust Company, LLC for the unregistered offer and sale of
> securities to retail investors through the Gemini Earn program.
> Per the complaint, Gemini Earn raised crypto assets worth
> billions of dollars from hundreds of thousands of investors;
> at the time Genesis paused withdrawals in November 2022,
> Genesis held approximately $900 million in crypto assets from
> approximately 340,000 Gemini Earn investors.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/complaints/2023/comp-pr2023-7.pdf>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/litigation/complaints/2023/comp-pr2023-7.pdf>
  > SEC civil complaint (S.D.N.Y.) against Genesis Global Capital,
> LLC and Gemini Trust Company, LLC. Captured as the underlying
> legal instrument anchoring the unregistered-securities theory
> for the Gemini Earn lending program.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Genesis Global Capital, LLC + Gemini Trust Company, LLC (Gemini Earn)
- **Chains**: `bitcoin`, `ethereum`
- **Canonical domains**: `genesistrading.com`, `gemini.com`

> Gemini Earn lending program: Genesis Global Capital as borrower /
> lender-of-record and Gemini Trust Company as custodial offering
> counterparty. This is a lending-product / service target, not an
> on-chain address set.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `unregistered_lending_program_charged_and_terminated`

**Timestamp**: `2023-01-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-7>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/news/press-release/2023-7>
  > SEC press release 2023-7 charges Genesis and Gemini with the
> unregistered offer and sale of crypto asset securities through
> the Gemini Earn lending program; the complaint enumerates
> ~$900M owed to ~340K Gemini Earn investors as of the
> November 2022 Genesis withdrawal pause.
- **`primary_legal`**
  - URL: <https://www.sec.gov/litigation/complaints/2023/comp-pr2023-7.pdf>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/litigation/complaints/2023/comp-pr2023-7.pdf>
  > SEC civil complaint (S.D.N.Y.) is the legal instrument
> anchoring the unregistered-securities theory for the Gemini
> Earn lending program at the offramp_cex / lending-product
> surface.

### offramp_cex · attribution: `plausible` · Δt = 168h

**Event label**: `genesis_chapter_11_filing_freezes_lender_estate`

**Timestamp**: `2023-01-19 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://cases.stretto.com/genesis/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://cases.stretto.com/genesis/>
  > Genesis Global Capital, LLC (and affiliates) filed voluntary
> Chapter 11 petitions in the United States Bankruptcy Court
> for the Southern District of New York on 2023-01-19, one
> week after the SEC complaint. The bankruptcy filing
> formalizes the freeze of the lender's estate including the
> customer-owed crypto assets that backed the Gemini Earn
> program. attribution=plausible because the Ch.11 is a
> consequence of the November 2022 Genesis liquidity crisis
> (FTX exposure + 3AC contagion) and the SEC action sits at
> the same time horizon; the bankruptcy court filing is the
> replayable anchor.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2023-7>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.sec.gov/news/press-release/2023-7>
  > SEC press release explicitly notes Genesis paused withdrawals
> in November 2022 and that ~$900M in crypto assets from ~340K
> Gemini Earn investors was held by Genesis at that time. The
> SEC action and the Ch.11 estate freeze are the two halves of
> the offramp_cex platform-failure shape.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No historical Gemini / Genesis frontend diff is retained here. The

## 7. Related events

- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e43eea7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

