# Evidence chain — `t3-financial-crime-unit-launch-2024-09`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-09-10 launch of the T3 Financial Crime Unit (Tether + TRON +
> TRM Labs) operationalized a standing private-sector consortium that
> executes USDT-on-TRON enforcement freezes at law-enforcement direction
> (initial aggregate 'over USDT 12 million' frozen). Two same-day
> USDT-on-TRON AddedBlackList receipts are pinned as a representative
> subset; single-layer asset_onchain observed_change with
> attribution=plausible, carried at the institutional/subset level (no
> complete address roster asserted)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_tron_trm_labs`
- **Timestamp**: `2024-09-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-tron-and-trm-labs-establish-first-ever-private-sector-financial-crime-unit-to-combat-crypto-crime/>
  - Wayback: <https://web.archive.org/web/20240910215903/https://tether.io/news/tether-tron-and-trm-labs-establish-first-ever-private-sector-financial-crime-unit-to-combat-crypto-crime/>
  - body_hash: `sha256:23160e7ef1d31d72b5942c399d80ac2742457b5bed3eede8fa65f4ff1725a52f`
  - body_path: `sources/http_captures/t3-financial-crime-unit-launch-2024-09/primary/web.archive.org__web-20240911000000-https-tether.io-news-tether-tron-and-trm-labs-establish-first-ever-private-sector-financial-crime-unit-to-combat-crypto-crime__c18df46f05.html`
  > Official Tether.io announcement 2024-09-10 (primary_corporate):
> Tether, TRON and TRM Labs "establish the T3 Financial Crime Unit
> (T3 FCU), a first-of-its-kind initiative aimed at facilitating
> public-private collaboration to combat illicit activity associated
> with the use of USDT on the TRON blockchain." Captured body
> verifies: "In collaboration with law enforcement, [it] facilitated
> the freezing of over USDT 12 million in funds associated with a
> blackmail scam, an investment fraud scheme, and others." Wayback
> 20240910215903.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2024/09/10/tron-tether-and-trm-labs-start-financial-crime-fighting-force>
  - Wayback: <https://web.archive.org/web/20240911050312/https://www.coindesk.com/business/2024/09/10/tron-tether-and-trm-labs-start-financial-crime-fighting-force/>
  - body_hash: `sha256:a53fc43c4afcb2ec6f303a6ff33e445b3e3f966874fab10b745059599e03bc72`
  - body_path: `sources/http_captures/t3-financial-crime-unit-launch-2024-09/primary/web.archive.org__web-20240911000000-https-www.coindesk.com-business-2024-09-10-tron-tether-and-trm-labs-start-financial-crime-fighting-force__73eb34a248.html`
  > CoinDesk 2024-09-10 corroboration: "The T3 Financial Crime Unit is
> looking to clean up USDT issued on Tron"; Tron/Tether/TRM Labs start
> a financial-crime-fighting force. Independent second semi-primary
> anchor for the launch date and actor set.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `subset`
- **Actor name**: T3 Financial Crime Unit (Tether + TRON + TRM Labs)
- **Chains**: `tron`
- **Addresses**: 2 total (enumerated in event YAML)

> Target is the class of USDT-on-TRON balances subject to T3 FCU
> enforcement freezes at law-enforcement direction (executed via Tether's
> USDT blacklist admin function). The launch announcement reports an
> initial aggregate "over USDT 12 million" frozen across a blackmail scam,
> an investment-fraud scheme and others. The captured source does not
> enumerate a full frozen-address roster; this row pins two same-day
> USDT-on-TRON AddedBlackList(address) receipts as a representative subset
> only. The two addresses are NOT asserted to exhaust the launch aggregate.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `plausible` · Δt = 6.76h

**Event label**: `t3_fcu_launch_executes_usdt_tron_enforcement_freezes`

**Timestamp**: `2024-09-10 06:45:54+00:00` (precision: `second`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-tron-and-trm-labs-establish-first-ever-private-sector-financial-crime-unit-to-combat-crypto-crime/>
  - Wayback: <https://web.archive.org/web/20240910215903/https://tether.io/news/tether-tron-and-trm-labs-establish-first-ever-private-sector-financial-crime-unit-to-combat-crypto-crime/>
  - body_hash: `sha256:23160e7ef1d31d72b5942c399d80ac2742457b5bed3eede8fa65f4ff1725a52f`
  - body_path: `sources/http_captures/t3-financial-crime-unit-launch-2024-09/primary/web.archive.org__web-20240911000000-https-tether.io-news-tether-tron-and-trm-labs-establish-first-ever-private-sector-financial-crime-unit-to-combat-crypto-crime__c18df46f05.html`
  > Tether.io launch announcement: T3 FCU established to facilitate
> USDT-on-TRON enforcement freezes with law enforcement; reports
> "over USDT 12 million" frozen at launch. attribution=plausible:
> the consortium and aggregate-freeze claim are directly stated by
> the issuer, while the captured source does not enumerate the full
> address roster. The primary_onchain sources below pin a same-day
> representative subset only.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/b08e804e631be03ff779027181d7069be9135d57890fc32856d8b093c07f0c5d>
  - tx_hash: `b08e804e631be03ff779027181d7069be9135d57890fc32856d8b093c07f0c5d`
  > USDT Tron AddedBlackList(address) log for
> TYMtkQ1rdvu5XnHFsg5SWizsdr4zk8AgqS in block 65100940 at
> 2024-09-10 06:45:54 UTC. TronGrid receipt SUCCESS, USDT TRON
> contract TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t, event topic
> 42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc;
> receipt cached under sources/onchain_receipts.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/0f7c52af61004b54bc9de3ec37695c3a3d61fd135b2db29faee824386f604856>
  - tx_hash: `0f7c52af61004b54bc9de3ec37695c3a3d61fd135b2db29faee824386f604856`
  > USDT Tron AddedBlackList(address) log for
> TDSp29bjTQZjQ6qoMB9VK74NnbbhT4aPB8 in block 65100945 at
> 2024-09-10 06:46:09 UTC. TronGrid receipt SUCCESS, USDT TRON
> contract TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t, event topic
> 42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc;
> receipt cached under sources/onchain_receipts.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2024/09/10/tron-tether-and-trm-labs-start-financial-crime-fighting-force>
  - Wayback: <https://web.archive.org/web/20240911050312/https://www.coindesk.com/business/2024/09/10/tron-tether-and-trm-labs-start-financial-crime-fighting-force/>
  - body_hash: `sha256:a53fc43c4afcb2ec6f303a6ff33e445b3e3f966874fab10b745059599e03bc72`
  - body_path: `sources/http_captures/t3-financial-crime-unit-launch-2024-09/primary/web.archive.org__web-20240911000000-https-www.coindesk.com-business-2024-09-10-tron-tether-and-trm-labs-start-financial-crime-fighting-force__73eb34a248.html`
  > CoinDesk corroboration of the T3 FCU launch (USDT-on-Tron
> enforcement). Independent second anchor for the launch date and
> actor set.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tether-doj-pig-butchering-freeze-2023`](./tether-doj-pig-butchering-freeze-2023.md)
- [`tether-pig-butchering-second-wave-2024`](./tether-pig-butchering-second-wave-2024.md)
- [`tether-tron-philippines-pdea-freeze-2024`](./tether-tron-philippines-pdea-freeze-2024.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

