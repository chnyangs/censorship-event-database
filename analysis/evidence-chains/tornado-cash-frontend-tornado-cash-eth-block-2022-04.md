# Evidence chain — `tornado-cash-frontend-tornado-cash-eth-block-2022-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a9689fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-17` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The Tornado Cash team's 2022-04-15 integration of the Chainalysis
> on-chain sanctions-screening oracle contract at the tornado.cash
> frontend — blocking OFAC SDN addresses from depositing or
> withdrawing through the team-operated dapp while leaving the
> Tornado Cash smart contracts on Ethereum permissionless —
> documents the earliest L4 DeFi-frontend voluntary self-censorship
> action in the corpus, predating the 2022-08-08 OFAC SDN
> designation of Tornado Cash (tornado-cash-ofac-2022) by 116 days
> and seeding the 'frontend / protocol-layer split' archetype later
> instantiated in the 2022-08 cascade siblings
> (aave-tornado-frontend-block-2022-08,
> uniswap-balancer-tornado-frontend-block-2022-08)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tornado_cash_team`
- **Timestamp**: `2022-04-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://twitter.com/TornadoCash/status/1514904975037210632>
  - Wayback: <https://web.archive.org/web/2022/https://twitter.com/TornadoCash/status/1514904975037210632>
  > Tornado Cash official Twitter (@TornadoCash) announcement of
> 2022-04-15 stating that "Tornado Cash uses Chainalysis oracle
> contract to block OFAC sanctioned addresses from accessing the
> dapp" and that "maintaining financial privacy is essential to
> preserving our freedom, however, it should not come at the cost
> of non-compliance." The team's own corporate statement names
> the action (frontend dapp block of OFAC SDN addresses), the
> mechanism (on-chain Chainalysis sanctions-screening oracle
> contract queried at the frontend), and that the block is
> scoped to the user-facing dapp only — the underlying smart
> contract remains permissionless. DRYRUN: pinned Wayback
> snapshot and body_hash for this tweet are deferred to the
> human-audit pass; marked evidence_use=contextual_unarchived
> per validator policy for unarchived sources.
- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/tech/2022/04/15/tornado-cash-adds-chainalysis-tool-for-blocking-ofac-sanctioned-wallets-from-dapp>
  - Wayback: <https://web.archive.org/web/2022/https://www.coindesk.com/tech/2022/04/15/tornado-cash-adds-chainalysis-tool-for-blocking-ofac-sanctioned-wallets-from-dapp>
  > CoinDesk contemporaneous coverage (2022-04-15) of the Tornado
> Cash team's adoption of the Chainalysis sanctions-screening
> oracle contract at the tornado.cash frontend. Triangulation
> source for day-level timing and the Chainalysis oracle
> mechanism. Notes the action followed the 2022-04-14 OFAC
> attribution of the Ronin Bridge hack to the DPRK Lazarus
> Group — but the Tornado Cash team's action is a voluntary
> corporate-policy step, not compelled by any OFAC designation
> of Tornado Cash itself (which came 4 months later, on
> 2022-08-08; see related event tornado-cash-ofac-2022).
> DRYRUN: pinned Wayback snapshot deferred to human audit.
- **`supporting_journalism`**
  - URL: <https://cryptopotato.com/tornado-cash-reveals-using-chainalysis-oracle-contract/>
  - Wayback: <https://web.archive.org/web/2022/https://cryptopotato.com/tornado-cash-reveals-using-chainalysis-oracle-contract/>
  > CryptoPotato contemporaneous coverage of the 2022-04-15
> Tornado Cash announcement describing the Chainalysis oracle
> contract integration at the tornado.cash dapp and quoting
> co-founder Roman Semenov's subsequent clarification that the
> block applies only to the frontend, not the smart contract.
> Triangulation source for the frontend-only scope of the
> block. DRYRUN: pinned Wayback snapshot deferred to human
> audit.
- **`supporting_journalism`**
  - URL: <https://chainbulletin.com/tornado-cash-to-use-chainalysis-to-block-ofac-sanctioned-addresses>
  - Wayback: <https://web.archive.org/web/2022/https://chainbulletin.com/tornado-cash-to-use-chainalysis-to-block-ofac-sanctioned-addresses>
  > Chain Bulletin contemporaneous coverage of the 2022-04-15
> Tornado Cash voluntary frontend block, retained as
> triangulation for the actor (Tornado Cash team), the
> mechanism (Chainalysis on-chain sanctions oracle), and the
> narrow frontend-only scope. DRYRUN: pinned Wayback snapshot
> deferred to human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `tornado_cash`
- **Actor name**: Tornado Cash team (frontend operator)
- **Chains**: `ethereum`
- **Canonical domains**: `tornado.cash`, `app.tornado.cash`

> Tornado Cash team operates the tornado.cash frontend UI (the
> user-facing dapp at app.tornado.cash / tornado.cash). On
> 2022-04-15 the team integrated the Chainalysis on-chain
> sanctions-screening oracle contract at the dapp's wallet-connect
> flow, blocking any address listed on the Chainalysis-maintained
> OFAC SDN sanctions list from depositing or withdrawing through
> the official frontend. Target is the operator entity (Tornado
> Cash frontend) rather than an enumerated address set because the
> blocklist is a moving reference maintained by the Chainalysis
> oracle (snapshotting OFAC SDN cryptocurrency addresses), not a
> static published roster; subset because only the team-operated
> tornado.cash UI is in scope (the Tornado Cash smart contracts on
> Ethereum mainnet remained permissionless and unaffected, and
> third-party frontends / direct contract calls bypassed the
> block).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `plausible` · Δt = 0h

**Event label**: `tornado_cash_team_integrated_chainalysis_oracle_blocking_ofac_sdn_addresses_at_dapp`

**Timestamp**: `2022-04-15 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/tech/2022/04/15/tornado-cash-adds-chainalysis-tool-for-blocking-ofac-sanctioned-wallets-from-dapp>
  - Wayback: <https://web.archive.org/web/20220415140448/https://www.coindesk.com/tech/2022/04/15/tornado-cash-adds-chainalysis-tool-for-blocking-ofac-sanctioned-wallets-from-dapp/>
  - body_hash: `sha256:d72eac8c9ced5e98835bde3651b0267b8e2e3b937bf77232685afbc79b4b39b0`
  - body_path: `sources/http_captures/tornado-cash-frontend-tornado-cash-eth-block-2022-04/primary/web.archive.org__web-20220416000000-https-www.coindesk.com-tech-2022-04-15-tornado-cash-adds-chainalysis-tool-for-blocking-ofac-sanctioned-wallets-from-dapp__a006914c35.html`
  > CoinDesk 2022-04-15: Tornado Cash added a Chainalysis oracle to its
> own dapp frontend to block OFAC-sanctioned wallets (self-imposed
> frontend filtering). Independent semi-primary anchor (replaces
> unarchivable TornadoCash tweet).
- **`semi_primary_wayback`**
  - URL: <https://cryptopotato.com/tornado-cash-reveals-using-chainalysis-oracle-contract/>
  - Wayback: <https://web.archive.org/web/20220416160427/https://cryptopotato.com/tornado-cash-reveals-using-chainalysis-oracle-contract/>
  - body_hash: `sha256:1f730593d3376f8028aa5a38e26e656489e89df75577e592be88b7323b33caab`
  - body_path: `sources/http_captures/tornado-cash-frontend-tornado-cash-eth-block-2022-04/primary/web.archive.org__web-20220416000000-https-cryptopotato.com-tornado-cash-reveals-using-chainalysis-oracle-contract__16657ac18f.html`
  > CryptoPotato 2022-04-16 corroborating the Chainalysis-oracle
> frontend block. Independent second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`tornado-cash-ofac-2022`](./tornado-cash-ofac-2022.md)
- [`tornado-cash-storm-conviction-2025`](./tornado-cash-storm-conviction-2025.md)
- [`aave-tornado-frontend-block-2022-08`](./aave-tornado-frontend-block-2022-08.md)
- [`uniswap-balancer-tornado-frontend-block-2022-08`](./uniswap-balancer-tornado-frontend-block-2022-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a9689fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

