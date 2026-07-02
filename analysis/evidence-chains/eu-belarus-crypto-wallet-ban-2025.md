# Evidence chain — `eu-belarus-crypto-wallet-ban-2025`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "EU Regulation 2025/392 Article 1u (effective 2025-03-26) banned crypto
> wallet/account/custody services for Belarusians; an off-ramp service
> restriction (direct, primary_legal)."

## 1. Trigger

- **Type**: `non_us_sanctions`
- **Actor**: `European Union / Council of the EU`
- **Timestamp**: `2025-02-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2025/392/oj/eng>
  - body_hash: `sha256:0977bf65450a79aab4aa33d1a2e52fe6275cfe0ac65ab60fc1f343a109cfc63a`
  - body_path: `sources/http_captures/eu-belarus-crypto-wallet-ban-2025/source/eur-lex.europa.eu__eli-reg-2025-392-oj-eng__090d0b3ded.html`
  > Captured 2026-06-08 with body_hash; replayable local primary for the action.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `eu_belarus_crypto_wallet_ban_2025_reaction`

**Timestamp**: `2025-02-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://eur-lex.europa.eu/eli/reg/2025/392/oj/eng>
  - body_hash: `sha256:0977bf65450a79aab4aa33d1a2e52fe6275cfe0ac65ab60fc1f343a109cfc63a`
  - body_path: `sources/http_captures/eu-belarus-crypto-wallet-ban-2025/source/eur-lex.europa.eu__eli-reg-2025-392-oj-eng__090d0b3ded.html`
  > Captured primary source documents the offramp-layer restriction; attribution direct.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

