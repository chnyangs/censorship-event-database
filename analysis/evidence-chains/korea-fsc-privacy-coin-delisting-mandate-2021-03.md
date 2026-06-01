# Evidence chain — `korea-fsc-privacy-coin-delisting-mandate-2021-03`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `029a430` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T14:19:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "South Korea's FSC enforcement-decree amendment, effective March 2021 (Special
> Financial Transactions Information Act commencement 2021-03-25), bars licensed
> Korean crypto exchanges from handling privacy / 'dark' coins (Monero, Dash,
> Zcash), forcing domestic delisting of that asset class. Captured with official
> FSC/FIU HTML and PDF anchors at class level at the offramp_cex layer; no
> per-exchange or on-chain enumeration claimed."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `KR_FSC`
- **Timestamp**: `2021-03-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://fsc.go.kr/no010101/75591>
  - body_hash: `sha256:a2c7fdcad3bd103de21b2e38077b851fc63e3ee7792180b45a2f1798b8701ff2`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary-fsc-nowww/fsc.go.kr__no010101-75591__80c5090d3f.html`
  > Official FSC/FIU press release, captured 2026-06-01. The release
> states that the amended Specific Financial Transaction Information
> reporting/supervision regulation was completed and effective 2021-03-25,
> and that VASPs are prohibited from handling virtual assets whose
> transaction histories are difficult to identify and whose money-
> laundering risk is high, so-called "dark coins."
- **`primary_government`**
  - URL: <https://fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=75591&fileTy=ATTACH&fileNo=2>
  - body_hash: `sha256:010a8ed8d4c6d10d2aed336211eca9d7a6f05d7e923fb6c084d4a0a2edec15a7`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary-fsc-pdf/fsc.go.kr__comm-getFile__99d4d4b302.bin`
  > Official PDF attachment to the FSC/FIU release. The PDF text carries
> the same 2021-03-25 effective date and VASP handling prohibition for
> so-called dark coins; it is retained as a second official replayable
> anchor for the page body.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/south-korean-financial-watchdog-to-ban-privacy-coins>
  - Wayback: <https://web.archive.org/web/20260114063228/https://cointelegraph.com/news/south-korean-financial-watchdog-to-ban-privacy-coins>
  - body_hash: `sha256:0db6fbd0fde1a06682603c614aa565696119b03b0ab32e6f954305843b85f62a`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary/web.archive.org__web-20260114063228-https-cointelegraph.com-news-south-korean-financial-watchdog-to-ban-privacy-coins__3faf32edcd.html`
  > Cointelegraph "South Korean financial watchdog will ban privacy coins from
> exchanges". Captured page confirms the FSC (Financial Services Commission)
> amendment to the enforcement decree of the Special Financial Transactions /
> reporting act bars virtual-asset service providers from handling "dark
> coins" / privacy coins (names Monero and Dash), taking effect March 2021.
- **`supporting_journalism`**
  - URL: <https://www.cpomagazine.com/data-privacy/south-koreas-new-crypto-aml-law-bans-trading-of-privacy-coins-monero-zcash/>
  - Wayback: <https://web.archive.org/web/20260105125739/https://www.cpomagazine.com/data-privacy/south-koreas-new-crypto-aml-law-bans-trading-of-privacy-coins-monero-zcash/>
  - body_hash: `sha256:4a401cc50c7d3ea4f5ad5e0be211885e2e76f98c6097f32df87a35d5866c6070`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary/web.archive.org__web-20260105125739-https-www.cpomagazine.com-data-privacy-south-koreas-new-crypto-aml-law-bans-trading-of-privacy-coins-monero-zcash__fcf7d78321.html`
  > CPO Magazine "South Korea's New Crypto AML Law Bans Trading of 'Privacy
> Coins' (Monero, Zcash)". Captured page confirms the FSC enforcement-decree
> amendment forbids licensed exchanges from offering "dark coins" / privacy
> coins (names Monero and Zcash), citing money-laundering / ransomware
> traceability risk, effective March 2021.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: South Korean licensed crypto exchanges (VASP class)

> Class-level subset: all South Korean licensed virtual-asset service providers
> (crypto exchanges) and the privacy-coin / "dark coin" asset class they are
> barred from handling (named in sources: Monero (XMR), Dash, Zcash (ZEC)). The
> mandate is a handling/delisting prohibition over the exchange class; no
> address-level or per-exchange enumeration is asserted.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `privacy_coin_handling_prohibited_exchanges`

**Timestamp**: `2021-03-25 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://fsc.go.kr/no010101/75591>
  - body_hash: `sha256:a2c7fdcad3bd103de21b2e38077b851fc63e3ee7792180b45a2f1798b8701ff2`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary-fsc-nowww/fsc.go.kr__no010101-75591__80c5090d3f.html`
  > Official FSC/FIU release: VASPs are prohibited from handling
> virtual assets whose transaction histories are difficult to identify
> and whose money-laundering risk is high, so-called "dark coins."
> attribution remains plausible because the source binds the VASP /
> asset class rather than enumerating a specific exchange operator.
- **`primary_government`**
  - URL: <https://fsc.go.kr/comm/getFile?srvcId=BBSTY1&upperNo=75591&fileTy=ATTACH&fileNo=2>
  - body_hash: `sha256:010a8ed8d4c6d10d2aed336211eca9d7a6f05d7e923fb6c084d4a0a2edec15a7`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary-fsc-pdf/fsc.go.kr__comm-getFile__99d4d4b302.bin`
  > Official PDF attachment carrying the same dark-coin handling
> prohibition and effective-date text as the FSC/FIU HTML release.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/south-korean-financial-watchdog-to-ban-privacy-coins>
  - Wayback: <https://web.archive.org/web/20260114063228/https://cointelegraph.com/news/south-korean-financial-watchdog-to-ban-privacy-coins>
  - body_hash: `sha256:0db6fbd0fde1a06682603c614aa565696119b03b0ab32e6f954305843b85f62a`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary/web.archive.org__web-20260114063228-https-cointelegraph.com-news-south-korean-financial-watchdog-to-ban-privacy-coins__3faf32edcd.html`
  > observed_change at class level: FSC enforcement-decree amendment bars
> Korean exchanges from handling privacy/dark coins (Monero, Dash).
> attribution=plausible — the decree targets the exchange / asset class,
> not enumerated operators (codebook §1.1).
- **`supporting_journalism`**
  - URL: <https://www.cpomagazine.com/data-privacy/south-koreas-new-crypto-aml-law-bans-trading-of-privacy-coins-monero-zcash/>
  - Wayback: <https://web.archive.org/web/20260105125739/https://www.cpomagazine.com/data-privacy/south-koreas-new-crypto-aml-law-bans-trading-of-privacy-coins-monero-zcash/>
  - body_hash: `sha256:4a401cc50c7d3ea4f5ad5e0be211885e2e76f98c6097f32df87a35d5866c6070`
  - body_path: `sources/http_captures/korea-fsc-privacy-coin-delisting-mandate-2021-03/primary/web.archive.org__web-20260105125739-https-www.cpomagazine.com-data-privacy-south-koreas-new-crypto-aml-law-bans-trading-of-privacy-coins-monero-zcash__fcf7d78321.html`
  > Companion anchor naming Monero and Zcash as barred privacy coins under
> the FSC enforcement-decree amendment.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`korea-fsc-institutional-restriction-2017`](./korea-fsc-institutional-restriction-2017.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)
- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `029a430`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

