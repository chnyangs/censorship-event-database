# Corporate-Policy Crypto Censorship Triage Manifest — Phase A.2 Discovery

- **Generated:** 2026-05-16
- **Frame:** `s5_corporate_policy_crypto_censorship_2017_2025`
- **Scope window:** 2017-01-01 → 2025-12-31
- **Stratum:** S5_corporate (issuer / exchange / frontend / infrastructure-provider autonomous policy change)
- **Trigger type:** `corporate_policy_change` (canonical S5 value)
- **Method:** Agent-enumerated from domain knowledge of widely reported autonomous crypto-industry policy changes; cross-checked against `events/*.yaml` and `candidate_triggers/*.yaml`. No automated scraper used.
- **Output state:** Discovery only — no `events/*.yaml` files written.
- **Candidate totals:** 24 total → **P0: 7**, **P1: 11**, **P2: 6**

## Scope boundaries and exclusions

- **S5 = autonomous corporate policy change.** Regulator-triggered actions (where the issuer / exchange / frontend acted because of a specific OFAC SDN, SEC complaint, DOJ indictment, NYDFS directive, or EU sanctions package) belong to S1/S3/S4/S6 even when the proximate cause is a corporate decision. Borderline cases are noted.
- **Existing S5 events not re-enumerated:** `circle-usdc-tornado-2022`, `coinbase-india-exit-2022`, `binance-russia-exit-commex-2023`, `paxos-busd-nydfs-minting-stop-2023`, `tether-doj-pig-butchering-freeze-2023`, `tether-retroactive-sweep-2023`, `tether-dprk-precommit-freeze-2025`, `okx-privacy-token-delist-2024`, `uniswap-frontend-delisting-2023`.
- **OFAC-mechanical Tether freezes** (Tornado-Cash 2022 same-day, Hamas 2023 same-day) NOT enumerated — they are dominantly OFAC-cascade with no autonomous-policy axis distinct from already-coded events.
- **Bitfinex 2017 USDT issuer events** excluded as CFTC/NYAG-driven and covered elsewhere.
- **Bittrex Global wind-down Dec-2023** excluded as regulator-cascade post-`sec-v-bittrex-2023`.
- **OpenSea NFT delistings under NYDFS pressure (2022)** excluded — asset-issuer-layer rather than exchange.
- **Mt. Gox 2014 and pre-2017 events** excluded per scope window.
- **Tornado Cash dApp frontend takedown 2022 (Infura / Alchemy / Github)** was assessed and DOES appear as a P0 candidate here as `infura-alchemy-tornado-rpc-block-2022` because the load-bearing layer is l3_rpc and the actor is an autonomous infrastructure provider, not OFAC. This is the only OFAC-cascade S5 spinoff admitted; others (e.g. tornadocash.org domain seizure) are flagged in the federal-enforcement triage manifest at P2.

## Candidate table

| # | Slug | Actor | Trigger | Date | Target | Layers | Load-Bearing | Pri | Rationale |
|---|------|-------|---------|------|--------|--------|--------------|-----|-----------|
| 1 | `binance-us-staking-end-2023` | binance_holdings_limited | corporate_policy_change | 2023-09-19 | Binance.US — staking-on-behalf discontinuation for US customers | offramp_cex | offramp_cex | **P0** | Major autonomous US-customer staking shutdown; pairs with `kraken-sec-staking-2023` as the autonomous-vs-regulator-forced comparison anchor. |
| 2 | `binance-privacy-coin-delisting-2023` | binance_holdings_limited | corporate_policy_change | 2023-06-26 | Binance Europe — XMR/ZEC/DASH/MOB/BEAM/ZEN/NAV/FIRO delisted for EEA users | offramp_cex | offramp_cex | **P0** | First EU-wide privacy-coin delisting batch by a top-5 exchange ahead of MiCA; cohort-leader for OKX/Kraken 2024 batches; 7-coin load-bearing measurement. |
| 3 | `kraken-monero-eu-delisting-2024` | kraken_payward | corporate_policy_change | 2024-10-31 | Kraken EEA — Monero (XMR) delisting for EEA customers | offramp_cex | offramp_cex | **P0** | Kraken (top-3 US-based exchange by EU volume) explicit MiCA-anticipation Monero delisting; landmark single-coin EU offramp event. |
| 4 | `binance-busd-wind-down-2024` | binance_holdings_limited | corporate_policy_change | 2023-08-11 | Binance — full BUSD removal + auto-convert to FDUSD (operational 2024-02-29) | offramp_cex, asset_onchain | offramp_cex | **P0** | Direct downstream of `paxos-busd-nydfs-minting-stop-2023`; autonomous Binance decision to fully retire BUSD; clean two-step issuer→exchange cascade. |
| 5 | `tether-cantor-trueusd-divergence-2024` | tether_usdt_issuer | corporate_policy_change | 2024-12-13 | Tether — USDT redemption discontinuation on EOS / Algorand / Kusama / BCH-SLP / omniBTC | asset_onchain | asset_onchain | **P0** | Tether autonomous chain-level offramp retirement; 5-chain single-policy decision; clear non-regulator-triggered S5 anchor. |
| 6 | `circle-usdc-svb-policy-statement-2023` | circle_usdc_issuer | corporate_policy_change | 2023-03-11 | Circle — public commitment + redemption-policy clarification post-SVB; 3.3B USDC reserve disclosure | asset_onchain, offramp_cex | asset_onchain | P1 | Not a freeze event but an autonomous USDC issuer policy decision affecting redemption mechanics; Coinbase/Binance/Kraken offramp behavior changed in lockstep. Distinct from `circle-usdc-tornado-2022`. |
| 7 | `metamask-eth-phishing-detect-tornado-additions-2022` | consensys_metamask | corporate_policy_change | 2022-08-10 | ConsenSys MetaMask — eth-phishing-detect additions of Tornado-Cash UI domains | l4_frontend | l4_frontend | P1 | Wallet-layer compliance 48-72h post-Tornado-OFAC; MetaMask eth-phishing-detect repo commits already in `sources/operator_census/MetaMask__eth-phishing-detect`. |
| 8 | `infura-alchemy-tornado-rpc-block-2022` | consensys_infura | corporate_policy_change | 2022-08-08 | Infura (ConsenSys) + Alchemy — RPC endpoint filtering of Tornado-Cash for US clients | l3_rpc, l4_frontend | l3_rpc | **P0** | First documented L3 RPC-provider sanctioned-asset block in Ethereum history; foundational evidence; distinct from `tornado-cash-ofac-2022` because load-bearing layer is l3_rpc. |
| 9 | `trustwallet-sanctioned-token-ui-update-2022` | trustwallet_binance | corporate_policy_change | 2022-09-15 | Trust Wallet — UI removal of Tornado-Cash sanctioned ERC-20 listings | l4_frontend | l4_frontend | P1 | Binance-owned wallet token-list compliance post-Tornado-OFAC; `sources/operator_census/trustwallet__assets` already in corpus. |
| 10 | `okx-monero-global-delisting-2024` | okx_exchange | corporate_policy_change | 2024-01-05 | OKX — global Monero (XMR) spot-trading delisting | offramp_cex | offramp_cex | P1 | Possible phased delisting after the 2023-12-29 OKX batch; if 2024-01-05 is a separable operational date, this captures the dedicated XMR completion. |
| 11 | `huobi-htx-privacy-coin-delisting-2024` | huobi_htx | corporate_policy_change | 2024-09-23 | HTX (Huobi) — global delisting of XMR/DASH/ZEN/FIRO/DCR | offramp_cex | offramp_cex | P1 | Top-10 global exchange privacy-coin delisting batch Q3-2024; rounds out the 2023-2024 Binance/Kraken/OKX cohort with Asian-corridor coverage. |
| 12 | `kraken-uk-derivatives-exit-2021` | kraken_payward | corporate_policy_change | 2021-06-29 | Kraken Futures Ltd — UK-resident derivatives account closure | offramp_cex, l4_frontend | offramp_cex | P1 | Direct autonomous Kraken corporate retreat after Jan-2021 FCA PS20/10 ban; pairs with `uk-fca-binance-markets-2021`. |
| 13 | `bybit-singapore-exit-2022` | bybit_global | corporate_policy_change | 2022-03-04 | Bybit — closure of Singapore-resident accounts under MAS PSA | offramp_cex, l4_frontend | offramp_cex | P1 | Top-5-derivatives-volume exchange autonomous SG retreat; parallel to existing `singapore-mas-binance-services-2021`. |
| 14 | `kucoin-canada-exit-2023` | kucoin_exchange | corporate_policy_change | 2023-05-23 | KuCoin — closure of Canadian-resident accounts ahead of CSA crypto registration | offramp_cex | offramp_cex | P1 | KuCoin autonomous Canadian retreat in line with `canada-csa-binance-withdrawal-2023`; pre-dates `kucoin-doj-2024` by 9 months. |
| 15 | `kucoin-netherlands-exit-2023` | kucoin_exchange | corporate_policy_change | 2023-06-21 | KuCoin — closure of Netherlands-resident accounts under DNB unregistered-VASP regime | offramp_cex | offramp_cex | P2 | Verify pre-emptive vs DNB-warning-driven attribution before admission. |
| 16 | `bitstamp-greece-portugal-exit-2023` | bitstamp_exchange | corporate_policy_change | 2023-07-25 | Bitstamp — discontinuation of services in 7 token jurisdictions including small-EU geographies | offramp_cex | offramp_cex | P2 | Lower-profile autonomous regional retreat; trigger axis (cost rationalization vs jurisdiction compliance) is mixed. |
| 17 | `coinbase-japan-exit-2023` | coinbase_inc | corporate_policy_change | 2023-01-18 | Coinbase KK — full closure of Japanese operations + return of customer assets | offramp_cex | offramp_cex | P1 | Companion to existing `coinbase-india-exit-2022`; clean autonomous retreat citing market conditions. |
| 18 | `uniswap-token-list-curation-default-2021` | uniswap_labs | corporate_policy_change | 2021-07-23 | Uniswap Labs — initial ~129-token restriction on app.uniswap.org (precursor to 2023 expansion) | l4_frontend | l4_frontend | **P0** | First documented Uniswap Labs frontend token-list compliance action 2 years before the 2023 expansion; necessary longitudinal baseline; `sources/http_captures/uniswap-frontend-delisting-2021` already exists. |
| 19 | `ens-eth-domain-tornado-resolution-2022` | ens_foundation | corporate_policy_change | 2022-08-12 | ENS / GoDaddy — gateway-layer interventions affecting tornado.cash and related .eth domains | l4_frontend, l0_network | l4_frontend | P2 | Verify which downstream gateway operator (Cloudflare, GoDaddy) took the load-bearing action before admission. |
| 20 | `etherscan-tornado-cash-ui-label-2022` | etherscan_block_explorer | corporate_policy_change | 2022-08-09 | Etherscan — UI labeling + contract-interaction warnings on Tornado-Cash SDN addresses | l4_frontend | l4_frontend | P2 | Block-explorer-layer compliance is partial (warning-only). P2 pending citation lock. |
| 21 | `dydx-tornado-frontend-ban-2022` | dydx_trading | corporate_policy_change | 2022-08-10 | dYdX Trading Inc. — frontend account closures + UI deny for Tornado-interacting wallets | l4_frontend, offramp_cex | l4_frontend | P1 | First documented DEX perpetuals frontend wallet-history compliance action; pairs cleanly with `uniswap-frontend-delisting-2023` (DEX) and `infura-alchemy-tornado-rpc-block-2022` (RPC). |
| 22 | `circle-usdc-cryptex-freeze-2024` | circle_usdc_issuer | corporate_policy_change | 2024-09-26 | Circle — same-day USDC blacklist of `cryptex-ofac-2024` SDN addresses | asset_onchain | asset_onchain | P2 | Dominantly OFAC-cascade; included for symmetry with `circle-usdc-tornado-2022` if same-day-issuer-freeze class is generalized. |
| 23 | `tether-pig-butchering-second-wave-2024` | tether_usdt_issuer | corporate_policy_change | 2024-10-25 | Tether — Q4-2024 second wave of pig-butchering freezes with US Secret Service (~$28M) | asset_onchain | asset_onchain | P1 | Distinct from `tether-doj-pig-butchering-freeze-2023`; cleanly operational repeat pattern. |
| 24 | `tether-tron-philippines-pdea-freeze-2024` | tether_usdt_issuer | corporate_policy_change | 2024-08-15 | Tether — USDT-TRON freeze of $3.6M with Philippine PDEA (fentanyl trafficking) | asset_onchain | asset_onchain | P2 | Non-US-LE Tether freeze; useful for non-OFAC-attributed Tether-policy cluster; lower visibility. |

## Notes on cross-checks and uniqueness

All 24 slugs verified absent from both `events/*.yaml` and `candidate_triggers/*.yaml` at generation time. Where existing event ids are similar in name (`circle-usdc-tornado-2022`, `coinbase-india-exit-2022`, `binance-russia-exit-commex-2023`, `paxos-busd-nydfs-minting-stop-2023`, `okx-privacy-token-delist-2024`, `tether-doj-pig-butchering-freeze-2023`, `tether-retroactive-sweep-2023`, `tether-dprk-precommit-freeze-2025`, `uniswap-frontend-delisting-2023`, `kraken-sec-staking-2023`, `kucoin-doj-2024`, `singapore-mas-binance-services-2021`, `uk-fca-binance-markets-2021`, `netherlands-dnb-binance-warning-2021`, `canada-csa-binance-withdrawal-2023`), the rationale field documents the distinction (different actor / different date / different load-bearing layer / different doctrine).

The `infura-alchemy-tornado-rpc-block-2022` candidate is intentionally enumerated at S5 here despite being adjacent to `tornado-cash-ofac-2022` — the load-bearing layer (l3_rpc) and actor (autonomous infrastructure provider) are distinct from the S1 event, and the federal-enforcement triage manifest separately flagged `tornado-cash-tornadocash-org-seizure-2022` for the L4 domain-seizure axis. No overlap.

## Note on `actor` vocabulary

The following S5 actor identifiers used here are consistent with existing event YAMLs:

- `circle_usdc_issuer`, `tether_usdt_issuer`, `paxos_trust`, `paxos_busd_supply_controller` (existing in corpus)
- `binance_holdings_limited`, `coinbase_inc`, `kraken_payward`, `okx_exchange` (existing in corpus)
- `consensys_infura`, `consensys_metamask`, `trustwallet_binance`, `uniswap_labs`, `dydx_trading`, `ens_foundation`, `etherscan_block_explorer` (new — proposed S5 corporate-actor extensions; consistent vocab format; require controlled-vocab update at admission time)
- `bybit_global`, `kucoin_exchange`, `huobi_htx`, `bitstamp_exchange` (new exchange identifiers; consistent vocab format)

## Next steps (out of scope for this discovery pass)

- Promote the 7 P0 candidates first; cross-check the 7 P2 verify-before-admit items.
- For Tether wave-2 / PDEA / Cryptex freezes, evaluate whether they cleanly merit standalone S5 admission or should be absorbed into broader sweep events.
- Capture canonical citation HTML and Wayback anchors for each P0 / P1 admission per the existing event template path; attach chain-analytics data for `offramp_cex` layers and operator-commit / repo-history evidence for `l3_rpc` / `l4_frontend` layers.
