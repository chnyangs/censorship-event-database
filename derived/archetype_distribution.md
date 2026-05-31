# Archetype distribution report

Dataset snapshot: **v0.2.0-rc-dryrun-11** · cutoff `2026-06-01` · commit `e2b6fd9` · generated `2026-06-01T00:00:00Z` (events: 368)

## 1. Classification rules (deterministic, priority-ordered)

```
if changed_layer_count == 0:
    → null_event
elif changed_layer_count >= 2:
    → multi_layer
elif changed_layers == {asset_onchain}:
    → asset_only
elif changed_layers == {l4_frontend}:
    → frontend_only
elif changed_layers == {offramp_cex}:
    → cex_only
else:
    → other_single_layer   # L0 / L1 / L3 singleton safety class
```

Latency-regime (bands on `time_to_first_change_hours`): `synchronous` ≤ 1h · `acute` ≤ 30h · `delayed` ≤ 30d · `lagged` > 30d · `none` = no timed observed_change.

## 2. Distribution

| Archetype | Count | % |
| --- | ---: | ---: |
| `asset_only` | 14 | 3.8% |
| `frontend_only` | 46 | 12.5% |
| `cex_only` | 167 | 45.4% |
| `multi_layer` | 38 | 10.3% |
| `other_single_layer` | 7 | 1.9% |
| `null_event` | 96 | 26.1% |
| **total** | **368** | **100.0%** |

### 2a. `multi_layer` signatures

| Signature | Count | Events |
| --- | ---: | --- |
| `l4_frontend+offramp_cex` | 26 | `australia-asic-binance-derivatives-2023`, `belgium-fsma-binance-cease-2023`, `binance-russia-exit-commex-2023`, `bitmex-cftc-doj-2020`, `canada-csa-binance-withdrawal-2023`, `cryptex-uaps-pm2btc-ivanov-shakhmametov-doj-2024`, `dydx-tornado-account-block-2022-08`, `garantex-besciokov-mira-serda-doj-2025`, `germany-bafin-binance-licence-withdrawal-2023`, `helix-doj-mixer-2020`, `india-fiu-offshore-vda-block-2023`, `indonesia-bappebti-illegal-exchange-block-2023`, `kucoin-doj-2024`, `liberty-reserve-coordinated-takedown-2013-05`, `malaysia-sc-binance-disable-2021`, `mtgox-bankruptcy-tokyo-2014`, `netherlands-dnb-binance-warning-2021`, `sec-beaxy-platform-shutdown-2023`, `sec-burnside-bitcoin-stock-exchange-2014`, `sec-v-ripple-2020`, `sec-voorhees-satoshidice-2014`, `sinbad-doj-2024`, `singapore-mas-binance-services-2021`, `singapore-mas-retail-crypto-restriction-2022`, `uk-fca-binance-markets-2021`, `uk-fca-crypto-promotion-rule-2023` |
| `l3_rpc+l4_frontend` | 3 | `infura-alchemy-tornado-rpc-block-2022`, `infura-metamask-donetsk-luhansk-block-2022-03`, `metamask-snaps-region-restrictions-2023-09` |
| `asset_onchain+l4_frontend` | 2 | `chatex-ofac-2021`, `cryptex-ofac-2024` |
| `l1_consensus+offramp_cex` | 2 | `china-state-council-mining-crackdown-2021-05`, `kazakhstan-digital-assets-law-2023-02` |
| `l0_network+offramp_cex` | 2 | `nigeria-binance-network-block-2024-02`, `philippines-sec-binance-block-2024` |
| `asset_onchain+offramp_cex` | 1 | `tether-doj-pig-butchering-freeze-2023` |
| `asset_onchain+l1_consensus+l3_rpc+l4_frontend+offramp_cex` | 1 | `tornado-cash-ofac-2022` |
| `asset_onchain+l1_consensus+l3_rpc+l4_frontend` | 1 | `tornado-cash-ofac-delisting-2025` |

### 2b. Latency regime

| Regime | Count | % |
| --- | ---: | ---: |
| `synchronous` | 211 | 57.3% |
| `acute` | 18 | 4.9% |
| `delayed` | 27 | 7.3% |
| `lagged` | 14 | 3.8% |
| `none` | 98 | 26.6% |

### 2c. Archetype × latency cross-tab

| archetype \ latency | synchronous | acute | delayed | lagged | none | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `asset_only` | 3 | 6 | 2 | 3 | 0 | 14 |
| `frontend_only` | 38 | 4 | 3 | 1 | 0 | 46 |
| `cex_only` | 136 | 4 | 20 | 7 | 0 | 167 |
| `multi_layer` | 28 | 4 | 2 | 3 | 1 | 38 |
| `other_single_layer` | 6 | 0 | 0 | 0 | 1 | 7 |
| `null_event` | 0 | 0 | 0 | 0 | 96 | 96 |

## 3. Exemplar cases

Up to 5 events per class, selected by admission tier then slug.

### `asset_only`  (14 events)

- `aeza-group-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `delayed` (t=30.4h)
- `circle-usdc-cryptex-freeze-2024` · tier `empirical_case` · stratum `S5_corporate` · signature `asset_onchain` · latency `acute` (t=27.0h)
- `circle-usdc-tornado-2022` · tier `empirical_case` · stratum `S5_corporate` · signature `asset_onchain` · latency `synchronous` (t=0.0h)
- `dprk-usdt-network-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `acute` (t=21.6h)
- `funnull-cdn-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `acute` (t=7.8h)

### `frontend_only`  (46 events)

- `1inch-us-geofence-2021-09` · tier `empirical_case` · stratum `S5_corporate` · signature `l4_frontend` · latency `synchronous` (t=0.0h)
- `aave-arc-fireblocks-whitelist-2022-01` · tier `empirical_case` · stratum `S5_corporate` · signature `l4_frontend` · latency `synchronous` (t=0.0h)
- `aave-tornado-frontend-block-2022-08` · tier `empirical_case` · stratum `S5_corporate` · signature `l4_frontend` · latency `synchronous` (t=0.0h)
- `alphabay-hansa-doj-2017` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `l4_frontend` · latency `synchronous` (t=0.0h)
- `apple-india-crypto-exchange-removal-2024-01` · tier `empirical_case` · stratum `S5_corporate` · signature `l4_frontend` · latency `synchronous` (t=0.0h)

### `cex_only`  (167 events)

- `1mdc-egold-account-freeze-2007-04` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `algeria-finance-law-2018-crypto-prohibition` · tier `empirical_case` · stratum `S4_nation_state` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `argentina-bcra-banks-crypto-services-ban-2022-05` · tier `empirical_case` · stratum `S4_nation_state` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `bcbs-cryptoasset-prudential-standard-sco60-2022` · tier `empirical_case` · stratum `S6_supranational` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `binance-4framework-2023` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `offramp_cex` · latency `synchronous` (t=0.0h)

### `multi_layer`  (38 events)

- `cryptex-ofac-2024` · tier `anchor_case` · stratum `S1_ofac_sdn` · signature `asset_onchain+l4_frontend` · latency `acute` (t=3.6h)
- `dydx-tornado-account-block-2022-08` · tier `anchor_case` · stratum `S5_corporate` · signature `l4_frontend+offramp_cex` · latency `synchronous` (t=0.0h)
- `garantex-besciokov-mira-serda-doj-2025` · tier `anchor_case` · stratum `S3_doj_sec_cftc_fiod` · signature `l4_frontend+offramp_cex` · latency `synchronous` (t=0.0h)
- `infura-alchemy-tornado-rpc-block-2022` · tier `anchor_case` · stratum `S5_corporate` · signature `l3_rpc+l4_frontend` · latency `synchronous` (t=0.0h)
- `tornado-cash-ofac-2022` · tier `anchor_case` · stratum `S1_ofac_sdn` · signature `asset_onchain+l1_consensus+l3_rpc+l4_frontend+offramp_cex` · latency `acute` (t=2.9h)

### `other_single_layer`  (7 events)

- `china-inner-mongolia-mining-ban-2021-05` · tier `empirical_case` · stratum `S4_nation_state` · signature `l1_consensus` · latency `synchronous` (t=0.0h)
- `china-sichuan-mining-ban-2021-06` · tier `empirical_case` · stratum `S4_nation_state` · signature `l1_consensus` · latency `none` (t=—)
- `cloudflare-ethereum-gateway-tornado-block-2022-08` · tier `empirical_case` · stratum `S5_corporate` · signature `l3_rpc` · latency `synchronous` (t=0.0h)
- `iran-government-mining-electricity-restriction-2021` · tier `empirical_case` · stratum `S4_nation_state` · signature `l1_consensus` · latency `synchronous` (t=0.0h)
- `kazakhstan-internet-shutdown-mining-2022-01` · tier `empirical_case` · stratum `S4_nation_state` · signature `l1_consensus` · latency `synchronous` (t=0.0h)

### `null_event`  (96 events)

- `al-law-hezbollah-crypto-ofac-2024-03` · tier `null_case` · stratum `S1_ofac_sdn` · signature `none` · latency `none` (t=—)
- `argentina-cnv-psav-registration-2024` · tier `null_case` · stratum `S4_nation_state` · signature `none` · latency `none` (t=—)
- `argentina-uif-resolution-300-2014` · tier `null_case` · stratum `S4_nation_state` · signature `none` · latency `none` (t=—)
- `bangladesh-bb-bitcoin-warning-2014` · tier `null_case` · stratum `S4_nation_state` · signature `none` · latency `none` (t=—)
- `bitmex-fincen-2024` · tier `null_case` · stratum `S3_doj_sec_cftc_fiod` · signature `none` · latency `none` (t=—)

## 4. Edge cases and review notes

- `tornado-cash-ofac-delisting-2025` is the dataset's sole reversal event. Archetype `multi_layer` is assigned by the same rule as forward events (changed-layer set); direction is NOT encoded in the archetype. Consumers drawing recovery claims from this row should carry n=1 explicitly.
- **7 event(s)** landed in `other_single_layer` — a singleton change at L0 / L1 / L3. This class exists as a safety catch; if populated, expand the taxonomy rather than leave it here: `china-inner-mongolia-mining-ban-2021-05`, `china-sichuan-mining-ban-2021-06`, `cloudflare-ethereum-gateway-tornado-block-2022-08`, `iran-government-mining-electricity-restriction-2021`, `kazakhstan-internet-shutdown-mining-2022-01`, `russia-mining-regional-ban-2024-12`, `venezuela-sunacrip-mining-exchange-halt-2023-03`
- `null_event` count is 96. Each such event carries at least one `observed_no_change` row whose source supplies a falsifiable evidence anchor — per validator rule, any one of `query_hash`, `measurement_ids`, `body_hash`+`body_path`, or a structured `scope_descriptor` is sufficient (not all four, and not necessarily `scope_descriptor`). Reading the null-event count as 'censorship did not happen' still requires checking the per-layer coverage composition in `derived/layer_observability.csv` — absence of observation is NOT absence of phenomenon.
- `multi_layer` contains 38 events across 8 distinct signature(s). If signature diversity is low, claims about 'multi-layer cascade heterogeneity' should carry that caveat explicitly.
- `synchronous` (≤1h) bucket: 211 events. **68 have `trigger_is_action=true`** (all `corporate_policy_change` — trigger.timestamp and observed_change.timestamp are identical in the record, so t=0 is a record-level artifact, not a measured delta): `1inch-us-geofence-2021-09`, `aave-arc-fireblocks-whitelist-2022-01`, `aave-tornado-frontend-block-2022-08`, `apple-india-crypto-exchange-removal-2024-01`, `apple-uniswap-wallet-app-store-rejection-2023-03`, `augur-v2-us-uk-geofence-2020-07`, `binance-busd-wind-down-2024`, `binance-com-us-customer-geofence-2019-06`, `binance-hamas-account-freeze-israel-2023-10`, `binance-netherlands-exit-2023-07`, `binance-nigeria-naira-services-end-2024-03`, `binance-palestinian-accounts-seizure-israel-2023-11`, `binance-privacy-coin-delisting-2023`, `binance-russia-exit-commex-2023`, `binance-russia-gunmaker-asset-freeze-ukraine-2022-08`, `binance-uk-new-user-halt-2023-10`, `binance-us-staking-end-2023`, `bitcoinica-shutdown-2012-05`, `bitfloor-capital-one-debanking-2013-04`, `bybit-canada-exit-2023-05`, `bybit-singapore-exit-2022`, `circle-usdc-tornado-2022`, `cloudflare-ethereum-gateway-tornado-block-2022-08`, `coinbase-eu-usdt-stablecoin-delisting-2024-12`, `coinbase-japan-exit-2023`, `dydx-tornado-account-block-2022-08`, `etherscan-tornado-cash-ui-label-2022`, `gate-io-privacy-coin-perpetuals-delisting-2024-12`, `gemini-netherlands-exit-2023-11`, `google-play-india-crypto-exchange-removal-2024-01`, `huobi-htx-privacy-coin-delisting-2024`, `infura-alchemy-tornado-rpc-block-2022`, `infura-metamask-donetsk-luhansk-block-2022-03`, `kraken-monero-eu-delisting-2024`, `kraken-uk-derivatives-exit-2021`, `metamask-eth-phishing-detect-tornado-additions-2022`, `metamask-snaps-region-restrictions-2023-09`, `mtgox-bankruptcy-tokyo-2014`, `mtgox-usd-withdrawal-suspension-2013-06`, `okx-india-exit-2024-03`, `okx-privacy-token-delist-2024`, `opensea-iran-cuba-sanctions-block-2022`, `pancakeswap-sanctioned-country-frontend-geofence-2022`, `paxos-busd-nydfs-minting-stop-2023`, `pecunix-bullion-transfer-2008`, `pump-fun-uk-fca-geofence-2024-12`, `shapeshift-mandatory-kyc-anonymity-end-2018-09`, `tether-doj-pig-butchering-freeze-2023`, `tether-dprk-precommit-freeze-2025`, `tether-garantex-usdt-freeze-2025-03`, `tether-pig-butchering-second-wave-2024`, `tether-retroactive-sweep-2023`, `tornado-cash-frontend-tornado-cash-eth-block-2022-04`, `tornado-cash-github-takedown-2022-08`, `tornado-cash-tornadocash-org-seizure-2022`, `tradehill-dwolla-payment-cutoff-2012-02`, `uniswap-balancer-tornado-frontend-block-2022-08`, `uniswap-frontend-delisting-2023`, `uniswap-tokenized-stocks-delisting-2021-07`, `upbit-bithumb-regulatory-delisting-purge-2021-06`, `wikileaks-amazon-aws-eviction-2010-12`, `wikileaks-bank-of-america-block-2010-12`, `wikileaks-everydns-domain-termination-2010-12`, `wikileaks-mastercard-suspension-2010-12`, `wikileaks-paypal-freeze-2010-12`, `wikileaks-postfinance-account-closure-2010-12`, `wikileaks-visa-europe-suspension-2010-12`, `wikileaks-western-union-interdiction-2010-12`. The remaining 143 carry distinct external triggers and observed a change within 1h. When reporting latency distributions, aggregate the two subsets separately rather than collapsing them into a single 'synchronous' count.
- `lagged` (>30d) bucket: 14 events spanning 4 stratum/strata (S1_ofac_sdn, S3_doj_sec_cftc_fiod, S4_nation_state, S5_corporate). The group is heterogeneous in trigger type; consumers citing these events should enumerate them individually rather than treat the bucket as a single mechanism. Events: `canada-csa-binance-withdrawal-2023`, `cftc-v-ooki-dao-2022`, `etoro-us-ada-trx-delisting-2021-12`, `india-rbi-crypto-ban-2018`, `kazakhstan-digital-assets-law-2023-02`, `nepal-nrb-bitcoin-ban-2017-08`, `netherlands-dnb-binance-warning-2021`, `paxos-canada-exit-2023-04`, `russia-election-interference-ofac-2020`, `russian-cyber-theft-ofac-2020`, `sec-v-coinbase-2023`, `sec-v-telegram-ton-2020`, `shrem-faiella-bitcoin-exchange-2014`, `tornado-cash-ofac-redesignation-2022`.

## 5. Hand-eyeball checklist

Before promoting this taxonomy to a paper claim, confirm each of the following by reading the exemplars above:

- [ ] Each exemplar is plausibly a member of its assigned class (not mis-labelled by the rules)
- [ ] No event straddles two classes semantically — if it does, the rules need a tie-breaker
- [ ] `multi_layer` signature diversity is adequate, or the report is clear about low diversity
- [ ] `null_event` members are coverage-disciplined (not just 'we didn't look')
- [ ] `other_single_layer` is empty OR surfaces are genuinely novel and warrant a new class
- [ ] `synchronous` members are not misleading — trigger ≠ reaction, even when same-hour
