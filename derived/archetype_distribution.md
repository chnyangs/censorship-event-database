# Archetype distribution report

Dataset snapshot: **v0.2.0-rc-dryrun-6** · cutoff `2026-05-16` · commit `5ba37ad` · generated `2026-05-20T00:00:00Z` (events: 105)

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
| `asset_only` | 13 | 12.4% |
| `frontend_only` | 14 | 13.3% |
| `cex_only` | 43 | 41.0% |
| `multi_layer` | 23 | 21.9% |
| `other_single_layer` | 0 | 0.0% |
| `null_event` | 12 | 11.4% |
| **total** | **105** | **100.0%** |

### 2a. `multi_layer` signatures

| Signature | Count | Events |
| --- | ---: | --- |
| `l4_frontend+offramp_cex` | 18 | `australia-asic-binance-derivatives-2023`, `belgium-fsma-binance-cease-2023`, `binance-russia-exit-commex-2023`, `bitmex-cftc-doj-2020`, `canada-csa-binance-withdrawal-2023`, `germany-bafin-binance-licence-withdrawal-2023`, `helix-doj-mixer-2020`, `india-fiu-offshore-vda-block-2023`, `kucoin-doj-2024`, `malaysia-sc-binance-disable-2021`, `netherlands-dnb-binance-warning-2021`, `sec-beaxy-platform-shutdown-2023`, `sec-burnside-bitcoin-stock-exchange-2014`, `sec-v-ripple-2020`, `sec-voorhees-satoshidice-2014`, `sinbad-doj-2024`, `singapore-mas-binance-services-2021`, `uk-fca-binance-markets-2021` |
| `asset_onchain+l4_frontend` | 2 | `chatex-ofac-2021`, `cryptex-ofac-2024` |
| `l3_rpc+l4_frontend` | 1 | `infura-alchemy-tornado-rpc-block-2022` |
| `asset_onchain+l1_consensus+l3_rpc+l4_frontend+offramp_cex` | 1 | `tornado-cash-ofac-2022` |
| `asset_onchain+l1_consensus+l3_rpc+l4_frontend` | 1 | `tornado-cash-ofac-delisting-2025` |

### 2b. Latency regime

| Regime | Count | % |
| --- | ---: | ---: |
| `synchronous` | 58 | 55.2% |
| `acute` | 15 | 14.3% |
| `delayed` | 10 | 9.5% |
| `lagged` | 10 | 9.5% |
| `none` | 12 | 11.4% |

### 2c. Archetype × latency cross-tab

| archetype \ latency | synchronous | acute | delayed | lagged | none | total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `asset_only` | 3 | 5 | 2 | 3 | 0 | 13 |
| `frontend_only` | 9 | 3 | 1 | 1 | 0 | 14 |
| `cex_only` | 31 | 3 | 5 | 4 | 0 | 43 |
| `multi_layer` | 15 | 4 | 2 | 2 | 0 | 23 |
| `other_single_layer` | 0 | 0 | 0 | 0 | 0 | 0 |
| `null_event` | 0 | 0 | 0 | 0 | 12 | 12 |

## 3. Exemplar cases

Up to 5 events per class, selected by admission tier then slug.

### `asset_only`  (13 events)

- `aeza-group-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `delayed` (t=30.4h)
- `circle-usdc-tornado-2022` · tier `empirical_case` · stratum `S5_corporate` · signature `asset_onchain` · latency `synchronous` (t=0.0h)
- `dprk-usdt-network-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `acute` (t=21.6h)
- `funnull-cdn-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `acute` (t=7.8h)
- `grinex-garantex-successor-ofac-2025` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `asset_onchain` · latency `acute` (t=21.2h)

### `frontend_only`  (14 events)

- `alphabay-hansa-doj-2017` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `l4_frontend` · latency `synchronous` (t=0.0h)
- `blender-ofac-2022` · tier `empirical_case` · stratum `S1_ofac_sdn` · signature `l4_frontend` · latency `delayed` (t=251.6h)
- `btc-e-doj-2017` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `l4_frontend` · latency `synchronous` (t=0.0h)
- `cftc-v-ooki-dao-2022` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `l4_frontend` · latency `lagged` (t=6192.0h)
- `chipmixer-doj-2023` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `l4_frontend` · latency `acute` (t=17.1h)

### `cex_only`  (43 events)

- `binance-4framework-2023` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `binance-cftc-2023` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `binance-privacy-coin-delisting-2023` · tier `empirical_case` · stratum `S5_corporate` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `binance-us-staking-end-2023` · tier `empirical_case` · stratum `S5_corporate` · signature `offramp_cex` · latency `synchronous` (t=0.0h)
- `bitfinex-cftc-retail-commodity-2016` · tier `empirical_case` · stratum `S3_doj_sec_cftc_fiod` · signature `offramp_cex` · latency `synchronous` (t=0.0h)

### `multi_layer`  (23 events)

- `cryptex-ofac-2024` · tier `anchor_case` · stratum `S1_ofac_sdn` · signature `asset_onchain+l4_frontend` · latency `acute` (t=3.6h)
- `infura-alchemy-tornado-rpc-block-2022` · tier `anchor_case` · stratum `S5_corporate` · signature `l3_rpc+l4_frontend` · latency `synchronous` (t=0.0h)
- `tornado-cash-ofac-2022` · tier `anchor_case` · stratum `S1_ofac_sdn` · signature `asset_onchain+l1_consensus+l3_rpc+l4_frontend+offramp_cex` · latency `acute` (t=2.9h)
- `australia-asic-binance-derivatives-2023` · tier `empirical_case` · stratum `S4_nation_state` · signature `l4_frontend+offramp_cex` · latency `synchronous` (t=0.0h)
- `belgium-fsma-binance-cease-2023` · tier `empirical_case` · stratum `S4_nation_state` · signature `l4_frontend+offramp_cex` · latency `synchronous` (t=0.0h)

### `other_single_layer`  (0 events)

_No events in this class in the current corpus._

### `null_event`  (12 events)

- `iran-ransomware-ofac-2018` · tier `null_case` · stratum `S1_ofac_sdn` · signature `none` · latency `none` (t=—)
- `irgc-ransomware-ofac-2022` · tier `null_case` · stratum `S1_ofac_sdn` · signature `none` · latency `none` (t=—)
- `lazarus-entity-ofac-2019` · tier `null_case` · stratum `S1_ofac_sdn` · signature `none` · latency `none` (t=—)
- `lazarus-laundering-ofac-2020` · tier `null_case` · stratum `S1_ofac_sdn` · signature `none` · latency `none` (t=—)
- `lockbit-leader-ofac-2024` · tier `null_case` · stratum `S1_ofac_sdn` · signature `none` · latency `none` (t=—)

## 4. Edge cases and review notes

- `tornado-cash-ofac-delisting-2025` is the dataset's sole reversal event. Archetype `multi_layer` is assigned by the same rule as forward events (changed-layer set); direction is NOT encoded in the archetype. Consumers drawing recovery claims from this row should carry n=1 explicitly.
- `other_single_layer` is empty in this snapshot (no L0/L1/L3-only singleton). The class remains defined so future data with a L0/L1/L3 singleton does not silently mis-classify.
- `null_event` count is 12. Each such event carries at least one `observed_no_change` row whose source supplies a falsifiable evidence anchor — per validator rule, any one of `query_hash`, `measurement_ids`, `body_hash`+`body_path`, or a structured `scope_descriptor` is sufficient (not all four, and not necessarily `scope_descriptor`). Reading the null-event count as 'censorship did not happen' still requires checking the per-layer coverage composition in `derived/layer_observability.csv` — absence of observation is NOT absence of phenomenon.
- `multi_layer` contains 23 events across 5 distinct signature(s). If signature diversity is low, claims about 'multi-layer cascade heterogeneity' should carry that caveat explicitly.
- `synchronous` (≤1h) bucket: 58 events. **10 have `trigger_is_action=true`** (all `corporate_policy_change` — trigger.timestamp and observed_change.timestamp are identical in the record, so t=0 is a record-level artifact, not a measured delta): `binance-privacy-coin-delisting-2023`, `binance-russia-exit-commex-2023`, `binance-us-staking-end-2023`, `circle-usdc-tornado-2022`, `infura-alchemy-tornado-rpc-block-2022`, `okx-privacy-token-delist-2024`, `tether-doj-pig-butchering-freeze-2023`, `tether-dprk-precommit-freeze-2025`, `tether-retroactive-sweep-2023`, `uniswap-frontend-delisting-2023`. The remaining 48 carry distinct external triggers and observed a change within 1h. When reporting latency distributions, aggregate the two subsets separately rather than collapsing them into a single 'synchronous' count.
- `lagged` (>30d) bucket: 10 events spanning 3 stratum/strata (S1_ofac_sdn, S3_doj_sec_cftc_fiod, S4_nation_state). The group is heterogeneous in trigger type; consumers citing these events should enumerate them individually rather than treat the bucket as a single mechanism. Events: `canada-csa-binance-withdrawal-2023`, `cftc-v-ooki-dao-2022`, `india-rbi-crypto-ban-2018`, `netherlands-dnb-binance-warning-2021`, `russia-election-interference-ofac-2020`, `russian-cyber-theft-ofac-2020`, `sec-v-coinbase-2023`, `sec-v-telegram-ton-2020`, `shrem-faiella-bitcoin-exchange-2014`, `tornado-cash-ofac-redesignation-2022`.

## 5. Hand-eyeball checklist

Before promoting this taxonomy to a paper claim, confirm each of the following by reading the exemplars above:

- [ ] Each exemplar is plausibly a member of its assigned class (not mis-labelled by the rules)
- [ ] No event straddles two classes semantically — if it does, the rules need a tie-breaker
- [ ] `multi_layer` signature diversity is adequate, or the report is clear about low diversity
- [ ] `null_event` members are coverage-disciplined (not just 'we didn't look')
- [ ] `other_single_layer` is empty OR surfaces are genuinely novel and warrant a new class
- [ ] `synchronous` members are not misleading — trigger ≠ reaction, even when same-hour
