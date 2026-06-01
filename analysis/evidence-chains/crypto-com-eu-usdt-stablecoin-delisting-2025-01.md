# Evidence chain — `crypto-com-eu-usdt-stablecoin-delisting-2025-01`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9494486` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:34:09Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Crypto.com's 2025-01 suspension of USDT (and nine other non-MiCA-
> compliant tokens) for EEA users — purchases off 2025-01-31, full
> delisting by Q1-2025 end — severed the Crypto.com USDT off-ramp in the
> EEA under MiCA; single-layer offramp_cex observed_change,
> attribution=plausible (MiCA cause reported, no captured issuer notice
> naming a specific instrument)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `crypto_com`
- **Timestamp**: `2025-01-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.dlnews.com/articles/regulation/cryptocom-to-delist-tether-usdt-in-eu/>
  - Wayback: <https://web.archive.org/web/20260309180532/https://www.dlnews.com/articles/regulation/cryptocom-to-delist-tether-usdt-in-eu/>
  - body_hash: `sha256:a8b782cb3517021f301b0006a81cc5f6557372e79aa3cc7ad380ed67a5e002bf`
  - body_path: `sources/http_captures/crypto-com-eu-usdt-stablecoin-delisting-2025-01/primary/web.archive.org__web-20260309180532-https-www.dlnews.com-articles-regulation-cryptocom-to-delist-tether-usdt-in-eu__41acb0cd52.html`
  > DL News 2025-01-29: Crypto.com announced it will suspend USDT and
> nine other non-MiCA-compliant tokens for European-Economic-Area
> users — purchases suspended 2025-01-31, with full delisting /
> conversion to compliant assets by end of Q1 2025 — because MiCA
> requires EEA stablecoins to hold an e-money license that USDT
> lacks. Grep-confirmed: USDT/Tether/MiCA/delist/EU/Europe present
> in the captured body.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: USDT (+ 9 non-MiCA tokens) on Crypto.com for EEA users
- **Chains**: `ethereum`, `tron`

> USDT (Tether) is the load-bearing named target; Crypto.com's notice
> also covers nine further non-MiCA-compliant tokens for EEA users
> (per coverage incl. PYUSD, DAI, WBTC, PAX, PAXG and others). Coded
> as subset: USDT is the enumerated focal asset, the remaining set is
> class-level (non-MiCA-compliant stablecoins/tokens), per §7.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 48h

**Event label**: `cryptocom_suspends_usdt_and_nine_tokens_for_eea_users`

**Timestamp**: `2025-01-31 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.dlnews.com/articles/regulation/cryptocom-to-delist-tether-usdt-in-eu/>
  - Wayback: <https://web.archive.org/web/20260309180532/https://www.dlnews.com/articles/regulation/cryptocom-to-delist-tether-usdt-in-eu/>
  - body_hash: `sha256:a8b782cb3517021f301b0006a81cc5f6557372e79aa3cc7ad380ed67a5e002bf`
  - body_path: `sources/http_captures/crypto-com-eu-usdt-stablecoin-delisting-2025-01/primary/web.archive.org__web-20260309180532-https-www.dlnews.com-articles-regulation-cryptocom-to-delist-tether-usdt-in-eu__41acb0cd52.html`
  > DL News 2025-01-29: Crypto.com USDT + nine-token EEA suspension
> (purchases off 2025-01-31, full delisting by Q1-2025 end).
> attribution=plausible per §1.4 analogue: the MiCA cause is
> reported and the action is squarely a MiCA-compliance offramp
> restriction, but this is third-party trade-press coverage of a
> Crypto.com policy rather than a captured Crypto.com notice
> citing a specific MiCA instrument; class-level inference.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`mica-l2-esma-eba-rts-2024`](./mica-l2-esma-eba-rts-2024.md)
- [`binance-busd-wind-down-2024`](./binance-busd-wind-down-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9494486`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

