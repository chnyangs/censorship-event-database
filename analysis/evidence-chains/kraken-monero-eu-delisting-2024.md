# Evidence chain — `kraken-monero-eu-delisting-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `7542617` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Kraken (Payward, Inc.)'s 2024-10-31 15:00 UTC termination
> of Monero (XMR) spot trading and deposits for clients
> resident in the European Economic Area — closing the
> XMR/USD, XMR/EUR, XMR/BTC, and XMR/USDT pairs and
> force-converting remaining XMR balances to BTC by
> 2025-01-06 — narrows the centralized-exchange off-ramp
> surface for Monero in the Kraken EEA corridor under
> MiCA-era compliance pressure. The offramp_cex layer carries
> the load-bearing direct-attribution observation; L0 / L1 /
> L3 / l4_frontend / asset_onchain are not_applicable for a
> geofenced exchange-listing-only action keyed to a single
> base-chain privacy asset. The row is the largest 2024
> EU-jurisdictional privacy-coin delisting anchor in the
> 2023-2024 CEX privacy-asset delisting wave (alongside
> binance-privacy-coin-delisting-2023 and
> okx-privacy-token-delist-2024)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `KRAKEN_PAYWARD`
- **Timestamp**: `2024-10-31 15:00:00+00:00` (precision: `hour`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://support.kraken.com/articles/support-for-monero-xmr-in-europe>
  - Wayback: <https://web.archive.org/web/2024/https://support.kraken.com/articles/support-for-monero-xmr-in-europe>
  > Kraken (Payward, Inc.) customer-support article "Support for
> Monero (XMR) in Europe" announcing termination of XMR trading
> and deposit support for clients resident in the European
> Economic Area (EEA), effective 2024-10-31 at 15:00 UTC. The
> notice closes the XMR/USD, XMR/EUR, XMR/BTC, and XMR/USDT spot
> markets for EEA users and sets a 2024-12-31 15:00 UTC
> withdrawal deadline, after which remaining XMR balances are
> force-converted to BTC at the prevailing market rate and
> distributed back to affected users by 2025-01-06. The notice
> cites EU regulatory changes (the Markets in Crypto-Assets
> framework — Regulation (EU) 2023/1114; see related_events:
> eu-mica-2023 — and the Travel-Rule / TFR recast Regulation
> (EU) 2023/1113; see related_events: eu-tfr-recast-2023) as
> the compliance rationale for ending EEA Monero support.
> Marked evidence_use=contextual_unarchived because in this
> DRYRUN the authoring LLM agent did not personally pin a
> Wayback snapshot timestamp or compute a body_hash; the
> precise support-article URL must be re-anchored during human
> audit before this citation may serve as an admission anchor
> in its own right.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Kraken (Payward, Inc.) — EEA user cohort
- **Chains**: `monero`
- **Canonical domains**: `kraken.com`, `support.kraken.com`

> Target entity is Kraken (Payward, Inc.) as the centralized-
> exchange operator implementing the EEA-cohort Monero (XMR)
> delisting. The named affected asset is Monero (XMR) and the
> named affected pairs are XMR/USD, XMR/EUR, XMR/BTC, and
> XMR/USDT spot markets for users resident in the European
> Economic Area (EEA: the 27 EU member states plus Iceland,
> Liechtenstein, Norway). Recorded as enumeration=subset because
> (a) the action is a geofenced EEA-cohort listing restriction
> rather than a global Kraken-wide delisting, (b) the class-
> level rationale (MiCA-era privacy-asset compliance) extends
> to a broader cohort of privacy assets that Kraken did not
> enumerate in this notice, and (c) Kraken's broader 2024-2025
> EEA / EU compliance program covered additional product-
> catalogue narrowing in later notices, coded elsewhere or
> pending in the candidate ledger.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `kraken_spot_pair_removal_xmr_eea_cohort`

**Timestamp**: `2024-10-31 15:00:00+00:00` (precision: `hour`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://support.kraken.com/articles/support-for-monero-xmr-in-europe>
  - Wayback: <https://web.archive.org/web/20250614041853/https://support.kraken.com/articles/support-for-monero-xmr-in-europe>
  - body_hash: `sha256:abd500560cc8bf13d3316204c8c90ec53335e1c12205296b64bd0edd2aa0ca68`
  - body_path: `sources/http_captures/kraken-monero-eu-delisting-2024/primary/web.archive.org__web-20241101000000-https-support.kraken.com-articles-support-for-monero-xmr-in-europe__7645eb428c.html`
  > Kraken support article announcing the end of Monero (XMR) support
> for European Economic Area clients (2024 delisting). primary_corporate
> anchor; attribution=direct. Wayback 20250614041853 pinned.
- **`semi_primary_wayback`**
  - URL: <https://cryptobriefing.com/kraken-monero-delisting-eea/>
  - Wayback: <https://web.archive.org/web/20241011170704/https://cryptobriefing.com/kraken-monero-delisting-eea/>
  - body_hash: `sha256:127621aad7ec764fce7c9398df1ddc9f59a9573dd64f650374652acfe7e8cbf8`
  - body_path: `sources/http_captures/kraken-monero-eu-delisting-2024/primary/web.archive.org__web-20241101000000-https-cryptobriefing.com-kraken-monero-delisting-eea__a748e3869a.html`
  > Crypto Briefing 2024-10 coverage of the Kraken Monero EEA delisting.
> Independent semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)
- [`okx-privacy-token-delist-2024`](./okx-privacy-token-delist-2024.md)
- [`eu-mica-2023`](./eu-mica-2023.md)
- [`eu-tfr-recast-2023`](./eu-tfr-recast-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `7542617`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

