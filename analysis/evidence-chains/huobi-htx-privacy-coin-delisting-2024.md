# Evidence chain — `huobi-htx-privacy-coin-delisting-2024`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e43eea7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Huobi (Huobi Global)'s 2022-09 product-catalogue removal of
> seven privacy-asset spot-trading pairs (Dash / Decred / Firo /
> Monero / Verge / Zcash / Horizen), effective 2022-09-19 08:00
> UTC and citing the latest financial regulations, narrows the
> centralized-exchange off-ramp surface for the affected privacy
> assets in the Huobi corridor. The offramp_cex layer carries the
> load-bearing observation; L0 / L1 / L3 / l4_frontend /
> asset_onchain are not_applicable for an exchange-listing-only
> action keyed to base-chain privacy assets. The row is the
> earliest anchor of the multi-year CEX privacy-asset delisting
> wave alongside binance-privacy-coin-delisting-2023,
> okx-privacy-token-delist-2024, and
> kraken-monero-eu-delisting-2024."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `huobi_global`
- **Timestamp**: `2022-09-19 08:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/09/12/crypto-exchange-huobi-to-delist-7-privacy-coins-including-zcash-monero>
  - Wayback: <https://web.archive.org/web/20220912212806/https://www.coindesk.com/business/2022/09/12/crypto-exchange-huobi-to-delist-7-privacy-coins-including-zcash-monero/>
  - body_hash: `sha256:8861a91f14b74c88a96f024e688262aa2b9ba5a0f214a838cd913918e8b2e995`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20220913000000-https-www.coindesk.com-business-2022-09-12-crypto-exchange-huobi-to-delist-7-privacy-coins-including-zcash-monero__791141af9e.html`
  > CoinDesk 2022-09-12 report "Crypto Exchange Huobi to Delist 7
> Privacy Coins, Including Zcash, Monero" is the corporate-policy
> anchor for the trigger. Reports Huobi announced 2022-09-12 that
> it would delist seven privacy coins — Dash (DSH), Decred (DCR),
> Firo (FIRO), Monero (XMR), Verge (XVG), Zcash (ZEC), and
> Horizen (ZEN) — effective 2022-09-19 08:00 UTC, citing the
> latest financial regulations. Wayback memento 20220912212806;
> replayable body_hash pinned.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/109513/crypto-exchange-huobi-delist-7-privacy-coins-citing-latest-financial-regulations>
  - Wayback: <https://web.archive.org/web/20220912165759/https://decrypt.co/109513/crypto-exchange-huobi-delist-7-privacy-coins-citing-latest-financial-regulations>
  - body_hash: `sha256:bc1a3cd1ae472fb486f36a7004bea36ee7443d8929801a443526bd41a95f061d`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20220913000000-https-decrypt.co-109513-crypto-exchange-huobi-delist-7-privacy-coins-citing-latest-financial-regulations__e5694902e5.html`
  > Decrypt 2022-09-12 report "Crypto Exchange Huobi to Delist 7
> Privacy Coins, Citing 'Latest Financial Regulations'"
> independently corroborates the seven-coin cohort (Dash,
> Decred, Firo, Monero, Verge, Zcash, Horizen), the
> 2022-09-19 effective date, and the financial-regulations
> rationale. Wayback memento 20220912165759; replayable
> body_hash pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Huobi (Huobi Global)
- **Chains**: `dash`, `decred`, `firo`, `monero`, `verge`, `zcash`, `horizen`
- **Canonical domains**: `huobi.com`, `www.huobi.com`

> Target entity is Huobi (Huobi Global) as the centralized-exchange
> operator implementing the 2022-09 seven-coin privacy-asset
> delisting. The affected cohort is fully enumerated by the
> corporate announcement and corroborating reporting: Dash (DSH),
> Decred (DCR), Firo (FIRO), Monero (XMR), Verge (XVG), Zcash (ZEC),
> and Horizen (ZEN). Recorded as enumeration=complete because the
> announcement names the exhaustive seven-coin set and its
> effective date (2022-09-19 08:00 UTC); no broader unspecified
> class is implied. (Huobi rebranded to HTX on 2023-09-13, after
> this event; the rebrand is contextual only and does not change
> the actor-of-record for the 2022 action.)

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `huobi_spot_pair_removal_privacy_asset_cohort_2022`

**Timestamp**: `2022-09-19 08:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2022/09/12/crypto-exchange-huobi-to-delist-7-privacy-coins-including-zcash-monero>
  - Wayback: <https://web.archive.org/web/20220912212806/https://www.coindesk.com/business/2022/09/12/crypto-exchange-huobi-to-delist-7-privacy-coins-including-zcash-monero/>
  - body_hash: `sha256:8861a91f14b74c88a96f024e688262aa2b9ba5a0f214a838cd913918e8b2e995`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20220913000000-https-www.coindesk.com-business-2022-09-12-crypto-exchange-huobi-to-delist-7-privacy-coins-including-zcash-monero__791141af9e.html`
  > CoinDesk 2022-09-12 report documents Huobi's announcement
> of the seven-coin privacy-asset delisting (Dash, Decred,
> Firo, Monero, Verge, Zcash, Horizen) effective
> 2022-09-19 08:00 UTC, citing the latest financial
> regulations. Replayable Wayback memento 20220912212806.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/109513/crypto-exchange-huobi-delist-7-privacy-coins-citing-latest-financial-regulations>
  - Wayback: <https://web.archive.org/web/20220912165759/https://decrypt.co/109513/crypto-exchange-huobi-delist-7-privacy-coins-citing-latest-financial-regulations>
  - body_hash: `sha256:bc1a3cd1ae472fb486f36a7004bea36ee7443d8929801a443526bd41a95f061d`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20220913000000-https-decrypt.co-109513-crypto-exchange-huobi-delist-7-privacy-coins-citing-latest-financial-regulations__e5694902e5.html`
  > Decrypt 2022-09-12 report independently corroborates the
> seven-coin cohort, the 2022-09-19 effective date, and the
> financial-regulations rationale. Replayable Wayback
> memento 20220912165759. Second independent semi-primary
> group satisfying the offramp_cex admission threshold.
- **`semi_primary_wayback`**
  - URL: <https://coingeek.com/huobi-delists-monero-zcash-and-other-privacy-coins-amid-regulatory-pressure/>
  - Wayback: <https://web.archive.org/web/20220913190344/https://coingeek.com/huobi-delists-monero-zcash-and-other-privacy-coins-amid-regulatory-pressure/>
  - body_hash: `sha256:ed5a69a77e1ae963ff9ae12f431b4d9a6e86e55ddd56f7889430c7a76dc39104`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20220913000000-https-coingeek.com-huobi-delists-monero-zcash-and-other-privacy-coins-amid-regulatory-pressure__69b6a3cb3f.html`
  > CoinGeek 2022-09-13 report "Huobi delists Monero, Zcash
> and other privacy coins amid regulatory pressure"
> corroborates the cohort and regulatory-pressure framing.
> Replayable Wayback memento 20220913190344.
- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/huobi-to-delist-monero-and-other-privacy-coins-citing-regulatory-pressures>
  - Wayback: <https://web.archive.org/web/20220912175020/https://cointelegraph.com/news/huobi-to-delist-monero-and-other-privacy-coins-citing-regulatory-pressures>
  - body_hash: `sha256:0558a398c9131d9188966117b01c8920533d42a77bdccc32d434a0898f656c3b`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20220913000000-https-cointelegraph.com-news-huobi-to-delist-monero-and-other-privacy-coins-citing-regulatory-pressures__2951a60310.html`
  > Cointelegraph 2022-09-12 report "Huobi to delist Monero
> and other privacy coins, citing regulatory pressures"
> provides a fourth independent semi-primary corroboration
> of the cohort, effective date, and rationale. Replayable
> Wayback memento 20220912175020.
- **`supporting_tracker`**
  - URL: <https://cryptoslate.com/privacy-tokens-reach-highest-delisting-rate-in-2024-kaiko/>
  - Wayback: <https://web.archive.org/web/20241008044118/https://cryptoslate.com/privacy-tokens-reach-highest-delisting-rate-in-2024-kaiko/>
  - body_hash: `sha256:5e4e7a8c99f631e38d3c8ed6c76e4b45a8df61bef649b9b8632580c55f4d91a5`
  - body_path: `sources/http_captures/huobi-htx-privacy-coin-delisting-2024/primary/web.archive.org__web-20241001000000-https-cryptoslate.com-privacy-tokens-reach-highest-delisting-rate-in-2024-kaiko__f23b5ede1d.html`
  > Contextual only. Kaiko's 2024 privacy-coin delisting
> tally (via CryptoSlate) supplies cross-exchange
> longitudinal context on the broader CEX privacy-asset
> delisting trend but does NOT establish this 2022 Huobi
> event; it is retained at supporting-tracker tier and is
> not counted toward this observation's admission. (The
> earlier draft mistakenly used this 2024 tally as the
> primary evidence for a non-existent 2024 HTX delisting;
> see analysis_notes date-correction.)

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`binance-privacy-coin-delisting-2023`](./binance-privacy-coin-delisting-2023.md)
- [`okx-privacy-token-delist-2024`](./okx-privacy-token-delist-2024.md)
- [`kraken-monero-eu-delisting-2024`](./kraken-monero-eu-delisting-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e43eea7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

