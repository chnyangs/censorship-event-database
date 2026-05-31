# Evidence chain — `binance-eea-usdt-spot-delisting-2025-03`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f1c99dd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2025-03 delisting of USDT spot trading pairs (and other non-
> MiCA-compliant stablecoins) for EEA users — announced 2025-03-03,
> effective 2025-03-31, derivatives retained — severed the Binance spot
> off-ramp for USDT in the EEA under MiCA; single-layer offramp_cex
> observed_change, attribution=plausible (MiCA cause reported, no captured
> Binance notice naming a specific instrument)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2025-03-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - Wayback: <https://web.archive.org/web/20250401151406/https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - body_hash: `sha256:c8e6dc2f6cbf689fa951e3ff8560c97e317c1771c1d5a2a88f8714c79826fb18`
  - body_path: `sources/http_captures/binance-eea-usdt-spot-delisting-2025-03/primary/web.archive.org__web-20250401151406-https-www.financemagnates.com-cryptocurrency-binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica__5e927feefb.html`
  > Finance Magnates: Binance announced (2025-03-03) it will delist
> non-MiCA-compliant stablecoin trading pairs — including USDT spot
> pairs — for EEA users, with spot trading removed by 2025-03-31
> (margin pairs from 2025-03-27); USDT derivatives retained and
> MiCA-compliant USDC/EURI kept. Grep-confirmed: USDT/Tether/MiCA/
> delist/EEA/spot/"March 31" present in the captured body.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `subset`
- **Actor name**: USDT spot pairs (+ non-MiCA stablecoins) on Binance for EEA users
- **Chains**: `ethereum`, `tron`

> USDT (Tether) spot trading pairs are the load-bearing named target;
> Binance's action covers nine non-MiCA-compliant stablecoins for EEA
> users (incl. FDUSD, TUSD, USDP, DAI, AEUR, UST, USTC, PAXG). Coded
> as subset: USDT is the enumerated focal asset, the remaining set is
> class-level (non-MiCA-compliant stablecoins), per §7.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 672h

**Event label**: `binance_delists_usdt_spot_pairs_for_eea_users`

**Timestamp**: `2025-03-31 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - Wayback: <https://web.archive.org/web/20250401151406/https://www.financemagnates.com/cryptocurrency/binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica/>
  - body_hash: `sha256:c8e6dc2f6cbf689fa951e3ff8560c97e317c1771c1d5a2a88f8714c79826fb18`
  - body_path: `sources/http_captures/binance-eea-usdt-spot-delisting-2025-03/primary/web.archive.org__web-20250401151406-https-www.financemagnates.com-cryptocurrency-binance-finally-delists-tether-usdt-from-european-spot-trading-in-compliance-with-mica__5e927feefb.html`
  > Finance Magnates: Binance USDT spot-pair EEA delisting
> (announced 2025-03-03, effective 2025-03-31; derivatives
> retained). attribution=plausible per §1.4 analogue: the MiCA
> cause is reported and the action is a MiCA-compliance offramp
> restriction, but this is trade-press coverage of a Binance
> policy rather than a captured Binance notice citing a specific
> MiCA instrument; class-level inference.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`crypto-com-eu-usdt-stablecoin-delisting-2025-01`](./crypto-com-eu-usdt-stablecoin-delisting-2025-01.md)
- [`eu-mica-2023`](./eu-mica-2023.md)
- [`mica-l2-esma-eba-rts-2024`](./mica-l2-esma-eba-rts-2024.md)
- [`binance-busd-wind-down-2024`](./binance-busd-wind-down-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f1c99dd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

