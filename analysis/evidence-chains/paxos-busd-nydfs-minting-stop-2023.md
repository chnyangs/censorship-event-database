# Evidence chain — `paxos-busd-nydfs-minting-stop-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `f70cc98` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:48:55Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-02-13 NYDFS-directed Paxos cessation of BUSD minting realizes
> as an on-chain ERC-20 SupplyController shutdown on the BUSD contract
> (0x4Fabb145d64652a948d72533023f6E7A623C7C53): the `increaseSupply`
> mint function ceases to be invoked after the 2023-02-21 cutoff, and
> total BUSD supply decreases monotonically thereafter via redemption-
> driven `decreaseSupply` burns. Coded as an S5 stablecoin-issuer
> supply-function shutdown with NYDFS as the proximate regulator,
> distinct from the OFAC-driven address-set freezes of Circle USDC
> (2022-08-08) and Tether USDT (2023-12-09)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `paxos_trust`
- **Timestamp**: `2023-02-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://paxos.com/2023/02/13/paxos-will-halt-minting-new-busd-tokens/>
  - Wayback: <https://web.archive.org/web/20260516000000/https://paxos.com/2023/02/13/paxos-will-halt-minting-new-busd-tokens/>
  > Paxos newsroom announcement (2023-02-13): "Paxos Will Halt Minting
> New BUSD Tokens." Paxos explicitly states that it will end its
> relationship with Binance for the branded BUSD stablecoin and
> cease the issuance of new BUSD tokens, citing instructions from
> the New York State Department of Financial Services (NYDFS). The
> statement also references the concurrent SEC Wells notice
> regarding BUSD. Paxos commits to continued 1:1 redemption support
> for existing BUSD holders.
- **`primary_legal`**
  - URL: <https://www.dfs.ny.gov/consumers/alerts/Paxos_and_Binance>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.dfs.ny.gov/consumers/alerts/Paxos_and_Binance>
  > NYDFS Consumer Alert: "Paxos and Binance." NYDFS confirms that it
> ordered Paxos Trust Company to cease issuance of BUSD as a result
> of unresolved issues related to Paxos's oversight of its
> relationship with Binance regarding the branded BUSD stablecoin.
> Primary legal anchor for the corporate-policy trigger; the alert
> also addresses redemption and consumer-protection assurances for
> existing BUSD holders.

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: Paxos Trust Company (BUSD issuer)
- **Chains**: `ethereum`
- **Canonical domains**: `paxos.com`, `binance.com`

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `paxos_newsroom_publishes_busd_mint_halt_announcement`

**Timestamp**: `2023-02-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://paxos.com/2023/02/13/paxos-will-halt-minting-new-busd-tokens/>
  - Wayback: <https://web.archive.org/web/20230214005251/https://paxos.com/2023/02/13/paxos-will-halt-minting-new-busd-tokens/>
  - body_hash: `sha256:20cf46d805b71b26be425f1c60930dea3d6838a1df9f7eb3a76b7584f3ba6532`
  - body_path: `sources/http_captures/paxos-busd-nydfs-minting-stop-2023/primary/web.archive.org__web-20230214000000-https-paxos.com-2023-02-13-paxos-will-halt-minting-new-busd-tokens__602cb8008a.html`
  > Paxos official statement (2023-02-13) that it will halt minting
> new BUSD tokens effective 2023-02-21 per NYDFS direction.
> primary_corporate anchor. Wayback 20230214005251 pinned.
- **`primary_legal`**
  - URL: <https://www.dfs.ny.gov/consumers/alerts/Paxos_and_Binance>
  - Wayback: <https://web.archive.org/web/20230213223852/https://www.dfs.ny.gov/consumers/alerts/Paxos_and_Binance>
  - body_hash: `sha256:e46f57f3eb0ad162ca2ab25a06f12b9ae048c1c24436850f8e5eb2a7c22ef6ec`
  - body_path: `sources/http_captures/paxos-busd-nydfs-minting-stop-2023/primary/web.archive.org__web-20230214000000-https-www.dfs.ny.gov-consumers-alerts-Paxos_and_Binance__33434460fb.html`
  > NYDFS consumer alert ordering Paxos to cease minting BUSD.
> primary_legal anchor for the regulatory censorship action.
> Wayback 20230213223852 pinned.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`circle-usdc-tornado-2022`](./circle-usdc-tornado-2022.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `f70cc98`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

