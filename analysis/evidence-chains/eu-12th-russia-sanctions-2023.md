# Evidence chain — `eu-12th-russia-sanctions-2023`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4ee1e3c` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:53:57Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Council Regulation 2023/2878 on 2023-12-18 extended Article 5aa of
> the Russia sanctions framework from an EUR 10K threshold to full
> prohibition on providing crypto-asset services to Russian nationals/
> residents via EU CASPs. First full-prohibition user-class sanction
> in the dataset; observational signal is exclusively at offramp_cex
> layer via CASP compliance."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `EU_Council`
- **Timestamp**: `2023-12-18 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2023/2878/oj>
  - body_hash: `sha256:aa4399798ed8607a097ada66115d43cc2a6e79f0c85fcf2f1a23222d1df6cd7b`
  - body_path: `sources/http_captures/eu-12th-russia-sanctions-2023/primary/eur-lex.europa.eu__eli-reg-2023-2878-oj__9901ec8fd4.html`
  > Council Regulation (EU) 2023/2878 of 18 December 2023 amending
> Regulation (EU) No 833/2014 concerning restrictive measures in view
> of Russia's actions destabilising the situation in Ukraine.
> Twelfth EU Russia-sanctions package. Key crypto-relevant provision:
> Article 5aa broadened to prohibit EU CASPs from providing
> crypto-asset services to Russian nationals / residents (full ban,
> down from the previous EUR 10K threshold). EU crypto exchanges
> (Binance EU, Kraken, Bitstamp) required to close or freeze Russian
> user accounts. First full-prohibition EU sanctions targeting
> individual retail crypto users rather than designated entities.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Russian nationals / residents (EU CASP customers)

> Russian nationals and residents as a class, via EU-licensed CASPs.
> No on-chain address enumeration — the target is natural persons
> identified via CASP KYC rather than wallet-level addresses.
> Downstream effect: forced closure or freeze of potentially
> tens-of-thousands of Russian-resident accounts across EU exchanges.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `eu_casps_required_to_close_russian_user_accounts`

**Timestamp**: `2023-12-18 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2023/2878/oj>
  - body_hash: `sha256:aa4399798ed8607a097ada66115d43cc2a6e79f0c85fcf2f1a23222d1df6cd7b`
  - body_path: `sources/http_captures/eu-12th-russia-sanctions-2023/primary/eur-lex.europa.eu__eli-reg-2023-2878-oj__9901ec8fd4.html`
  > EU Council Regulation 2023/2878 Article 5aa amendment is the
> primary legal instrument. EU CASPs (Binance EU, Kraken, Bitstamp,
> Bitpanda, etc.) were required to close/freeze Russian-resident
> accounts within 90 days of adoption. Direct attribution: the
> regulation mandates the account-closure behavior by name.
- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2023/2878/oj>
  - body_hash: `sha256:aa4399798ed8607a097ada66115d43cc2a6e79f0c85fcf2f1a23222d1df6cd7b`
  - body_path: `sources/http_captures/eu-12th-russia-sanctions-2023/primary/eur-lex.europa.eu__eli-reg-2023-2878-oj__9901ec8fd4.html`
  > Second anchor to same Council Regulation; context for Article 5aa
> full-prohibition extension from prior EUR 10K threshold.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4ee1e3c`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

