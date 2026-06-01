# Evidence chain — `paxos-canada-exit-2023-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `575b085` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T11:33:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Paxos's official Canada-withdrawal notice asked Canadian users to withdraw
> all balances, closed empty accounts on 2023-05-09, and disabled remaining
> accounts beginning 2023-06-02 except for access and withdrawals, leaving no
> full platform access to initiate new trades. This is a 1-layer offramp_cex
> observed_change with direct attribution to Paxos's corporate policy action;
> the CSA/OSC regulatory frame is retained as contextual rationale."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `PAXOS_TRUST`
- **Timestamp**: `2023-04-12 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://support.paxos.com/articles/3570242566-paxos-withdrawal-from-canada>
  - body_hash: `sha256:bffcd3c6765a875abff57a45dfdc3716d6217a3937298a0766c6325a1edc2196`
  - body_path: `sources/http_captures/paxos-canada-exit-2023-04/official-paxos-canada-support/support.paxos.com__hc-en-us-articles-14791919809812-Paxos-Withdrawal-from-Canada__59e2fa6332.html`
  > Paxos Knowledge Base official article, "Paxos Withdrawal from
> Canada." The captured page states that Paxos asks Canadian users to
> withdraw all balances, that accounts with no funds would be
> automatically closed on May 9, and that beginning June 2 accounts
> would be disabled except for access and withdrawals; users would not
> have full platform access to initiate new trades. This is the
> claim-usable primary corporate trigger and observation anchor.
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

### offramp_cex · attribution: `direct` · Δt = Noneh

**Event label**: `paxos_canada_offramp_shutdown`

**Timestamp**: `2023-06-02 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://support.paxos.com/articles/3570242566-paxos-withdrawal-from-canada>
  - body_hash: `sha256:bffcd3c6765a875abff57a45dfdc3716d6217a3937298a0766c6325a1edc2196`
  - body_path: `sources/http_captures/paxos-canada-exit-2023-04/official-paxos-canada-support/support.paxos.com__hc-en-us-articles-14791919809812-Paxos-Withdrawal-from-Canada__59e2fa6332.html`
  > Paxos's own support article records the Canada withdrawal path:
> users were asked to withdraw all balances, empty accounts would
> close on 2023-05-09, and beginning 2023-06-02 accounts would be
> disabled except for access and withdrawals, with no full platform
> access to initiate new trades. attribution=direct for the
> Paxos-authored corporate service restriction; the CSA/OSC
> regulatory framing remains contextual unless supported by a
> separate primary legal trigger.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/business/2023/04/12/blockchain-financial-services-firm-paxos-is-withdrawing-from-canada>
  - Wayback: <https://web.archive.org/web/20240810111740/https://www.coindesk.com/business/2023/04/12/blockchain-financial-services-firm-paxos-is-withdrawing-from-canada/>
  - body_hash: `sha256:2847886e2e270edad0e32f6d9bbfe7ccd32af9a5aaeadadfceb3a0c9b5c946d3`
  - body_path: `sources/http_captures/paxos-canada-exit-2023-04/primary/web.archive.org__web-20240810111740-https-www.coindesk.com-business-2023-04-12-blockchain-financial-services-firm-paxos-is-withdrawing-from-canada__c7eb09cb13.html`
  > Paxos 2023-06-02 disabling of Canadian accounts (empty accounts
> closed 2023-05-09). Retained as contemporaneous corroboration and
> source for the 2023-04-12 announcement date plus CSA-context frame.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Paxos's exit was a website / notice announcement rather than a

## 7. Related events

- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)
- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`okx-canada-exit-2023`](./okx-canada-exit-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `575b085`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

