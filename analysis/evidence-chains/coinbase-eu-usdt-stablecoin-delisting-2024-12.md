# Evidence chain — `coinbase-eu-usdt-stablecoin-delisting-2024-12`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9964436` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Coinbase Europe / Coinbase Germany's 2024-12-13 delisting of six
> non-MiCA-compliant stablecoins (USDT, PAX, PYUSD, GUSD, GYEN, DAI) for
> EEA retail users severed the Coinbase EEA-retail off-ramp for these
> assets; single-layer offramp_cex observed_change with attribution=direct
> (Coinbase's own announced MiCA-compliance policy). USDC/EURC remained."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `coinbase`
- **Timestamp**: `2024-12-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/296453/coinbase-europe-delists-usdt>
  - Wayback: <https://web.archive.org/web/20241213163322/https://decrypt.co/296453/coinbase-europe-delists-usdt>
  - body_hash: `sha256:e7ade1d8a5346105268ac240ccf8b73012f337ee3cd5b37f62bf8081cf151732`
  - body_path: `sources/http_captures/coinbase-eu-usdt-stablecoin-delisting-2024-12/primary/web.archive.org__web-20241214000000-https-decrypt.co-296453-coinbase-europe-delists-usdt__385f3445ea.html`
  > Decrypt 2024-12 (memento 2024-12-13): "Coinbase Europe Delists USDT,
> Other Stablecoins Citing EU Compliance." Captured body verifies:
> "Starting Dec. 13, Coinbase Europe users will be restricted from
> trading and receiving" the affected stablecoins; "Other than USDT,
> retail customers on Coinbase Europe and Coinbase Germany will see
> the delisting of Paxos Standard Price (PAX)," PYUSD, GUSD, GYEN
> ("first regulated Japanese YEN stablecoin"), and DAI; driven by
> MiCA non-compliant-stablecoin rules. Wayback 20241213163322.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/coinbase-delist-non-compliant-stablecoins-mica>
  - Wayback: <https://web.archive.org/web/20241004134144/https://cointelegraph.com/news/coinbase-delist-non-compliant-stablecoins-mica>
  - body_hash: `sha256:3c1735ba40d0739c4b3a4df229bbefa699f1c8e753ade2c1bcaf8c45e238f7c9`
  - body_path: `sources/http_captures/coinbase-eu-usdt-stablecoin-delisting-2024-12/primary/web.archive.org__web-20241005000000-https-cointelegraph.com-news-coinbase-delist-non-compliant-stablecoins-mica__76a4dd625d.html`
  > Cointelegraph 2024-10-04 (the earlier announcement): "Coinbase to
> restrict noncompliant stablecoins"; USDT "like Tether's USDt (USDT),
> which may be forced off the Coinbase platform" under MiCA. Captured
> body verifies the MiCA-driven delisting plan. Independent second
> semi-primary anchor (announcement → 2024-12-13 effective date).

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: USDT + PAX + PYUSD + GUSD + GYEN + DAI on Coinbase EEA retail

> Six stablecoins delisted for EEA retail users on Coinbase Europe and
> Coinbase Germany: USDT (Tether), PAX (Paxos Standard), PYUSD (PayPal
> USD), GUSD (Gemini Dollar), GYEN (GMO-Z.com JPY), and DAI (Maker
> Protocol). Complete enumeration of the delisted set; the action removes
> the Coinbase EEA-retail trading markets for these non-MiCA-compliant
> stablecoins. USDC and EURC (MiCA-compliant) remained supported.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `coinbase_eea_retail_delists_non_mica_compliant_stablecoins`

**Timestamp**: `2024-12-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/296453/coinbase-europe-delists-usdt>
  - Wayback: <https://web.archive.org/web/20241213163322/https://decrypt.co/296453/coinbase-europe-delists-usdt>
  - body_hash: `sha256:e7ade1d8a5346105268ac240ccf8b73012f337ee3cd5b37f62bf8081cf151732`
  - body_path: `sources/http_captures/coinbase-eu-usdt-stablecoin-delisting-2024-12/primary/web.archive.org__web-20241214000000-https-decrypt.co-296453-coinbase-europe-delists-usdt__385f3445ea.html`
  > Decrypt: "Starting Dec. 13, Coinbase Europe users will be
> restricted from trading and receiving" USDT and (for retail on
> Coinbase Europe/Coinbase Germany) PAX/PYUSD/GUSD/GYEN/DAI under
> MiCA. attribution=direct: the delisting is Coinbase's own announced
> policy with an explicit stated MiCA-compliance rationale.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/coinbase-delist-non-compliant-stablecoins-mica>
  - Wayback: <https://web.archive.org/web/20241004134144/https://cointelegraph.com/news/coinbase-delist-non-compliant-stablecoins-mica>
  - body_hash: `sha256:3c1735ba40d0739c4b3a4df229bbefa699f1c8e753ade2c1bcaf8c45e238f7c9`
  - body_path: `sources/http_captures/coinbase-eu-usdt-stablecoin-delisting-2024-12/primary/web.archive.org__web-20241005000000-https-cointelegraph.com-news-coinbase-delist-non-compliant-stablecoins-mica__76a4dd625d.html`
  > Cointelegraph corroboration of the MiCA-driven Coinbase
> non-compliant-stablecoin delisting plan (announced 2024-10-04).
> Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`eu-mica-2023`](./eu-mica-2023.md)
- [`mica-l2-esma-eba-rts-2024`](./mica-l2-esma-eba-rts-2024.md)
- [`binance-busd-wind-down-2024`](./binance-busd-wind-down-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9964436`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

