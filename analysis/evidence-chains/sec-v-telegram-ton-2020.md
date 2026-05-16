# Evidence chain — `sec-v-telegram-ton-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-7` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `5e28a89` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-21T00:00:00Z`

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
  - URL: <https://www.sec.gov/news/press-release/2020-69>
  - Wayback: <https://web.archive.org/web/2020/https://www.sec.gov/news/press-release/2020-69>
  > SEC press release 2020-69 (2020-03-24): "Court Orders Preliminary
> Injunction in Telegram Case." SDNY (Judge P. Kevin Castel) granted
> the SEC's motion for a preliminary injunction halting Telegram
> Group Inc. and TON Issuer Inc. from distributing the approximately
> 2.9 billion Gram digital tokens to the 175 initial purchasers
> (and ultimately to the secondary market) from the October 2017 -
> March 2018 private placement that raised roughly $1.7 billion.
> The court applied the Howey test plus the Gary Plastic resale-
> analysis doctrine and concluded the Gram distribution constituted
> an unregistered offering of securities under Section 5 of the
> Securities Act of 1933, because the initial purchasers stood as
> statutory underwriters reselling into a public market. This is the
> landmark SAFT-framework ("Simple Agreement for Future Tokens")
> decision: the court rejected Telegram's argument that the SAFT
> sale to accredited investors and the later token delivery were
> legally distinct transactions, holding instead that they were
> steps in a single unregistered public offering. Marked
> evidence_use=contextual_unarchived because the authoring LLM agent
> did not personally pin a Wayback snapshot timestamp or compute a
> body_hash for the press release; SEC press-release URL format is
> stable and routinely captured by Wayback, but the specific
> snapshot is to be re-pinned during human audit before this
> citation may serve as an admission anchor in its own right.
> Provisional Wayback anchor uses Wayback Machine year-prefix
> lookup.

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
  - URL: <https://www.sec.gov/news/press-release/2020-69>
  - Wayback: <https://web.archive.org/web/2020/https://www.sec.gov/news/press-release/2020-69>
  > SEC press release 2020-69 (2020-03-24) announcing the SDNY
> preliminary injunction granted by Judge P. Kevin Castel.
> The injunction halted the planned Gram distribution from
> Telegram / TON Issuer to the 175 initial purchasers and, by
> extension, the resale cascade to the public secondary
> market. attribution=direct because the SEC press release and
> the underlying SDNY order are the direct legal mechanism
> compelling the issuer-side cancellation. Provisional Wayback
> anchor uses Wayback Machine year-prefix lookup; specific
> snapshot to be re-pinned during human audit.
- **`primary_corporate`**
  - URL: <https://telegram.org/blog/what-was-ton>
  - Wayback: <https://web.archive.org/web/2020/https://telegram.org/blog/what-was-ton>
  > Telegram founder Pavel Durov's 2020-05-12 blog post
> "What was TON and why it is over" announcing termination of
> the TON project, citing the SDNY decision as the operative
> reason: a U.S. court ruled the planned Gram distribution
> could not occur even to non-U.S. purchasers, which Telegram
> interpreted as foreclosing the global mainnet launch.
> Provides the direct issuer-side timestamp of the
> cancellation event 49 days after the injunction.
> evidence_use=contextual_unarchived pending Wayback re-pin
> and body_hash capture during human audit; provisional
> Wayback anchor uses Wayback Machine year-prefix lookup.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`sec-v-coinbase-2023`](./sec-v-coinbase-2023.md)
- [`cftc-v-ooki-dao-2022`](./cftc-v-ooki-dao-2022.md)
- [`blockfi-sec-lending-2022`](./blockfi-sec-lending-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-7` (commit `5e28a89`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

