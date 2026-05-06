# Chain-coverage structural note

Documented 2026-04-22 as part of the Phase D audit of dataset chain
representation.

## Observation

As of dataset snapshot `v0.1.0` (cutoff `2026-04-22`), across **51
admitted events**, target-chain distribution is:

```
bitcoin:          23
ethereum:         18
tron:              7
litecoin:          3
dash:              2
zcash:             2
bitcoin_gold:      1
bitcoin_sv:        1
ethereum_classic:  1
monero:            1
ripple:            1
```

**Solana, BNB Chain, and Polygon are not represented.** Full-text search
across all event YAMLs for "solana", "polygon", "bnb chain", "bep-20",
"bep20", and "bsc" returns zero hits.

## Interpretation

This is not a sampling gap in the current dataset state — it reflects
the actual content of the admitted corpus, which is itself dominated by
OFAC SDN practice from 2018-11-28 through 2025-11-19:

1. **OFAC SDN practice is BTC/ETH/TRON-centric.** The long-tail chains
   (LTC/DASH/ZEC/XMR) appear only in the 2020-09-10 Russia-election and
   2020-09-16 Russian-cyber-theft designations, which took an
   enumerate-every-chain-the-actor-used approach.

2. **Solana/Polygon/BNB Chain addresses have not been named in any public
   OFAC Recent Actions page in scope.** This aligns with where illicit
   flows concentrate: BTC for ransomware/darknet, ETH for Tornado-style
   mixing, TRON for DPRK USDT laundering. Solana's illicit-flow share
   remains a small fraction of that of TRON as of late 2025.

3. **The frontend-operator layer DOES include Polygon tokens** via
   Uniswap Labs' 2023-07 token-list restriction (see
   uniswap-frontend-delisting-2023), but the restriction is
   frontend-UI-level rather than protocol-level, and Polygon is not
   enumerated as a target chain.

## Implication for paper

The paper should frame Bitcoin + Ethereum + TRON as the three
"measurement-relevant" chains in the dataset, with the observation that
newer L1s and L2s remain outside OFAC crypto-enforcement practice as of
the dataset cutoff (2025-11-19). This is a genuine finding, not a
coverage limitation of the catalog.

## What would change this

A future Tether freeze of USDT-SOL addresses tied to a designated actor,
or a FinCEN/OFAC action specifically naming Solana/Polygon/BNB addresses,
would be the trigger to open Solana / Polygon / BNB Chain-specific events.
Track via the Tether transparency reports / OFAC Recent Actions feed; no
action required in the current dataset state.
