# Evidence chain — `paxos-canada-exit-2023-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `432aaf5` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Paxos on 2023-04-12 announced withdrawal from the Canadian market
> effective 2023-06-02 (empty accounts closed 2023-05-09), disabling
> Canadian-resident accounts to withdraw-only amid the CSA's 2023-02-22
> undertaking framework — a 1-layer offramp_cex observed_change
> (attribution=plausible) for the Paxos Canada cohort. Structurally an S5
> corporate-policy retreat sibling to the S4 CSA-driven Binance Canada
> withdrawal (canada-csa-binance-withdrawal-2023)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `PAXOS_TRUST`
- **Timestamp**: `2023-04-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/04/12/blockchain-financial-services-firm-paxos-is-withdrawing-from-canada>
  - Wayback: <https://web.archive.org/web/20240810111740/https://www.coindesk.com/business/2023/04/12/blockchain-financial-services-firm-paxos-is-withdrawing-from-canada/>
  - body_hash: `sha256:2847886e2e270edad0e32f6d9bbfe7ccd32af9a5aaeadadfceb3a0c9b5c946d3`
  - body_path: `sources/http_captures/paxos-canada-exit-2023-04/primary/web.archive.org__web-20240810111740-https-www.coindesk.com-business-2023-04-12-blockchain-financial-services-firm-paxos-is-withdrawing-from-canada__c7eb09cb13.html`
  > CoinDesk (2023-04-12): Paxos announced on its website that it is
> withdrawing from the Canadian market effective 2023-06-02. Accounts
> with no funds were auto-closed on 2023-05-09; all other accounts
> were disabled on 2023-06-02 (after which Canadian users could still
> withdraw funds but not initiate new trades). The exit followed the
> CSA's 2023-02-22 enhanced pre-registration-undertaking framework
> (the stablecoin / value-referenced-crypto-asset deposit
> restrictions). The captured page confirms the Canada withdrawal,
> the 2023-06-02 effective date, and the CSA regulatory context.
> Verified via grep of the pinned body.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Paxos (Canada user cohort)
- **Canonical domains**: `paxos.com`

> Paxos Canadian-resident user cohort. Paxos (Paxos Trust Company /
> crypto-brokerage and stablecoin-issuance businesses) is the focal
> target actor; the affected population is Canadian-resident users of
> the Paxos platform. Subset-enumerated because the exit affected the
> Canadian retail cohort rather than a named address list. Sibling to
> the S4 canada-csa-binance-withdrawal-2023 and the S5
> kucoin-canada-exit-2023 / okx-canada-exit-2023.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `paxos_canada_offramp_shutdown`

**Timestamp**: `2023-06-02 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/04/12/blockchain-financial-services-firm-paxos-is-withdrawing-from-canada>
  - Wayback: <https://web.archive.org/web/20240810111740/https://www.coindesk.com/business/2023/04/12/blockchain-financial-services-firm-paxos-is-withdrawing-from-canada/>
  - body_hash: `sha256:2847886e2e270edad0e32f6d9bbfe7ccd32af9a5aaeadadfceb3a0c9b5c946d3`
  - body_path: `sources/http_captures/paxos-canada-exit-2023-04/primary/web.archive.org__web-20240810111740-https-www.coindesk.com-business-2023-04-12-blockchain-financial-services-firm-paxos-is-withdrawing-from-canada__c7eb09cb13.html`
  > Paxos 2023-06-02 disabling of Canadian accounts (empty accounts
> closed 2023-05-09). attribution=plausible: the off-ramp shutdown
> is directly observed in contemporaneous coverage, but the captured
> anchor is semi-primary (no Paxos primary notice pinned), so the
> link to the 2023-02-22 CSA framework is the reporter-attributed
> rationale rather than a primary Paxos-stated trigger.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Paxos's exit was a website / notice announcement rather than a

## 7. Related events

- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)
- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`okx-canada-exit-2023`](./okx-canada-exit-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `432aaf5`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

