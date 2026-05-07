# Chain-coverage structural note

Documented 2026-05-06 as part of the Phase D audit of dataset chain
representation.

## Observation

As of dataset snapshot `v0.1.0` (cutoff `2026-05-06`), across **53
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

**Solana, BNB Chain, and Polygon are not represented as target chains.**
The SEC v. Coinbase record names SOL and MATIC as securities-theory target
tokens, but the event carries no on-chain address target and therefore does
not enter this chain-denominator table.

## Interpretation

This is a coverage fact about the current admitted corpus, not a
complete-chain denominator. The admitted evidence corpus is dominated by
publicly archived OFAC SDN cases from 2018-11-28 through 2025-11-19:

1. **OFAC SDN practice is BTC/ETH/TRON-centric.** The long-tail chains
   (LTC/DASH/ZEC/XMR) appear only in the 2020-09-10 Russia-election and
   2020-09-16 Russian-cyber-theft designations, which took an
   enumerate-every-chain-the-actor-used approach.

2. **Solana/Polygon/BNB Chain addresses are absent from the admitted
   address-target events in this snapshot.** Treat that as an observed
   chain-distribution feature of the source frame, not as proof that no
   such public actions exist outside the current admission frame.

3. **The frontend-operator layer DOES include Polygon tokens** via
   Uniswap Labs' 2023-07 token-list restriction (see
   uniswap-frontend-delisting-2023), but the restriction is
   frontend-UI-level rather than protocol-level, and Polygon is not
   enumerated as a target chain.

## Implication for paper

The paper should frame Bitcoin + Ethereum + TRON as the three
"measurement-relevant" chains in the current admitted corpus. Claims
about newer L1s/L2s must be phrased as outside this snapshot's measured
address-target denominator unless a future sampling frame explicitly
enumerates those chains.

## What would change this

A future Tether freeze of USDT-SOL addresses tied to a designated actor,
or a FinCEN/OFAC action specifically naming Solana/Polygon/BNB addresses,
would be the trigger to open Solana / Polygon / BNB Chain-specific events.
Track via the Tether transparency reports / OFAC Recent Actions feed; no
action required in the current dataset state.
