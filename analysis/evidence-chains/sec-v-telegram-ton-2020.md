# Evidence chain — `sec-v-telegram-ton-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `bb7ed29` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2020-03-24 SDNY preliminary injunction in SEC v. Telegram
> Group Inc. (No. 19-cv-9439, Judge Castel) is admitted as a single-
> layer offramp_cex issuer-cancellation row: Telegram's 2020-05-12
> termination of the TON project and the foreclosed Gram public-CEX
> listing cascade. The row does not claim ISP-level blocking of
> telegram.org / ton.org, a frontend takedown, on-chain admin-method
> engagement, or specific named-CEX delisting actions, because the
> Gram token never reached public distribution."

## 1. Trigger

- **Type**: `sec_action`
- **Actor**: `US_SEC`
- **Timestamp**: `2020-03-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://storage.courtlistener.com/recap/gov.uscourts.nysd.524448/gov.uscourts.nysd.524448.227.0.pdf>
  - body_hash: `sha256:f67195d0c792301b15b45b49570d282d03d31284fe0bf3d9a2a11f32e5bb7569`
  - body_path: `sources/http_captures/sec-v-telegram-ton-2020/court-telegra-primary/storage.courtlistener.com__recap-gov.uscourts.nysd.524448-gov.uscourts.nysd.524448.227.0.pdf__0ea53619d9.bin`
  > SDNY opinion and order, SEC v. Telegram Group Inc., No. 19-cv-9439,
> Document 227, filed 2020-03-24. Judge P. Kevin Castel granted the
> SEC's motion for a preliminary injunction halting Telegram Group Inc.
> and TON Issuer Inc. from distributing approximately 2.9 billion Gram
> digital tokens to 175 initial purchasers and into the secondary public
> market. The order states that the SEC showed a substantial likelihood
> of proving that Telegram's planned distribution was part of a larger
> unregistered securities-distribution scheme. SOURCE-REPAIRED
> 2026-06-01: the RECAP-hosted court PDF was captured locally and pinned
> with body_hash/body_path.
- **`primary_legal`**
  - URL: <https://www.sec.gov/news/press-release/2020-146>
  - body_hash: `sha256:52633038172226449579be044350543f7477b3e3dcd1305b941f6b88fc99305e`
  - body_path: `sources/http_captures/sec-v-telegram-ton-2020/court-telegra-primary/www.sec.gov__news-press-release-2020-146__ea8d4823cd.html`
  > SEC press release 2020-146, published 2020-06-26, announces the final
> Telegram settlement and corroborates the earlier 2020-03-24 SDNY
> preliminary injunction barring delivery of Grams. It is retained as an
> SEC-side confirmatory source; the day-level trigger anchor is the SDNY
> order above.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Telegram Group Inc. / TON Issuer Inc.
- **Canonical domains**: `telegram.org`, `ton.org`

> Telegram Group Inc. + TON Issuer Inc. (the corporate issuer entities
> named in SEC v. Telegram Group Inc., No. 19-cv-9439 (SDNY)). Subject
> matter scope: the Gram token and the approximately $1.7 billion
> October 2017 - March 2018 SAFT private placement to 175 initial
> purchasers. No on-chain addresses are enumerated because the Gram
> token never reached public distribution: the TON mainnet launch was
> halted by the preliminary injunction and Telegram terminated the TON
> project on 2020-05-12 before any token-level on-chain primitive
> became live on a public chain. The dataset row enumerates only the
> Telegram corporate issuer entities and the Gram instrument as a
> distribution that was cancelled at the issuer level.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 1176h

**Event label**: `sec_injunction_triggered_issuer_cancellation_of_gram_token_distribution_and_ton_mainnet_launch`

**Timestamp**: `2020-05-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://storage.courtlistener.com/recap/gov.uscourts.nysd.524448/gov.uscourts.nysd.524448.227.0.pdf>
  - body_hash: `sha256:f67195d0c792301b15b45b49570d282d03d31284fe0bf3d9a2a11f32e5bb7569`
  - body_path: `sources/http_captures/sec-v-telegram-ton-2020/court-telegra-primary/storage.courtlistener.com__recap-gov.uscourts.nysd.524448-gov.uscourts.nysd.524448.227.0.pdf__0ea53619d9.bin`
  > SDNY Document 227 is the legal instrument granting the preliminary
> injunction against Telegram Group Inc. and TON Issuer Inc. The order
> halted the planned Gram distribution to initial purchasers and the
> anticipated resale cascade to the public secondary market.
> attribution=direct because this court order is the legal mechanism
> Telegram later cited when terminating active involvement with TON.
- **`primary_corporate`**
  - URL: <https://telegra.ph/What-Was-TON-And-Why-It-Is-Over-05-12>
  - body_hash: `sha256:ed7559bc5ca9edf41eb00cefb445a321ceffb16ca6f5ec81cc72ee57b8e6c964`
  - body_path: `sources/http_captures/sec-v-telegram-ton-2020/court-telegra-primary/telegra.ph__What-Was-TON-And-Why-It-Is-Over-05-12__d01a38fa55.html`
  > Telegram founder Pavel Durov's 2020-05-12 Telegraph post "What Was
> TON And Why It Is Over" announces that Telegram's active involvement
> with TON is over. The post links the termination to the U.S. court
> ruling that Grams could not be distributed globally. Provides the
> direct issuer-side timestamp of the cancellation event 49 days after
> the injunction.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `bb7ed29`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

