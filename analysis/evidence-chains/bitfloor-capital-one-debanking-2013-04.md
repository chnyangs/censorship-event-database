# Evidence chain — `bitfloor-capital-one-debanking-2013-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a09b90d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Capital One's ~2013-04-17 unilateral closure of BitFloor's USD bank account
> severed the exchange's fiat off-ramp and forced it to cease trading; single-
> layer offramp_cex observed_change with attribution=plausible (no public
> Capital One rationale naming BitFloor)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `capital_one`
- **Timestamp**: `2013-04-17 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.americanbanker.com/fincen-regulations-choking-bitcoin-entrepreneurs-1058606-1.html>
  - Wayback: <https://web.archive.org/web/20241130191119/https://www.americanbanker.com/fincen-regulations-choking-bitcoin-entrepreneurs-1058606-1.html>
  - body_hash: `sha256:5e4542aedb281c462119f7061b674645ca6e04fc0f2bae7ae9194c916a8291c3`
  - body_path: `sources/http_captures/bitfloor-capital-one-debanking-2013-04/primary/web.archive.org__web-20241130191119-https-www.americanbanker.com-fincen-regulations-choking-bitcoin-entrepreneurs-1058606-1.html__242252ee6d.html`
  > American Banker (PaymentsSource) 2013-04-25: BitFloor's New York
> operation ran USD deposits/withdrawals "through a Capital One bank
> account – which the bank unilaterally closed." Founder Roman Shtylman:
> "I had very little time to act between receiving the account closure
> letter and the account being closed." BitFloor was a FinCEN-registered
> MSB but not a state money transmitter; Shtylman surmised Capital One
> judged the business "not worth the risk." Body grep-confirmed: "Capital
> One", "unilaterally closed", "Shtylman". Wayback 20241130191119 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: BitFloor (US bitcoin exchange)
- **Chains**: `bitcoin`

> Single target: BitFloor, Inc. (US/New York bitcoin exchange, the then
> fourth-largest, operated by Roman Shtylman). Capital One's unilateral
> closure of BitFloor's USD bank account severed its only fiat
> deposit/withdrawal rail.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `capital_one_closes_bitfloor_usd_bank_account`

**Timestamp**: `2013-04-17 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.americanbanker.com/fincen-regulations-choking-bitcoin-entrepreneurs-1058606-1.html>
  - Wayback: <https://web.archive.org/web/20241130191119/https://www.americanbanker.com/fincen-regulations-choking-bitcoin-entrepreneurs-1058606-1.html>
  - body_hash: `sha256:5e4542aedb281c462119f7061b674645ca6e04fc0f2bae7ae9194c916a8291c3`
  - body_path: `sources/http_captures/bitfloor-capital-one-debanking-2013-04/primary/web.archive.org__web-20241130191119-https-www.americanbanker.com-fincen-regulations-choking-bitcoin-entrepreneurs-1058606-1.html__242252ee6d.html`
  > American Banker names Capital One as the bank that "unilaterally
> closed" BitFloor's USD account. attribution=plausible: the debanking
> is directly observed, but Capital One issued no public rationale
> naming BitFloor; the FinCEN-pressure / "not worth the risk" motive is
> Shtylman's contextual inference, not a stated bank rationale.
- **`semi_primary_wayback`**
  - URL: <https://bitcoinmagazine.com/markets/bitfloor-shuts-down-1366351632>
  - Wayback: <https://web.archive.org/web/20260121151931/https://bitcoinmagazine.com/markets/bitfloor-shuts-down-1366351632>
  - body_hash: `sha256:ceba4a4321475fc97fbc665c07f1c183a3457a11a2123fb1ca22f5ea3d710f92`
  - body_path: `sources/http_captures/bitfloor-capital-one-debanking-2013-04/primary/web.archive.org__web-20260121151931-https-bitcoinmagazine.com-markets-bitfloor-shuts-down-1366351632__2b2d5f7223.html`
  > Bitcoin Magazine 2013-04: founder Shtylman announced BitFloor would
> "cease all trading operations" because its US bank account was being
> closed and it could "no longer provide the same level of USD deposits
> and withdrawals." Independent corroboration of the rail loss. Body
> grep-confirmed: "cease all trading operations", "Shtylman", "USD
> deposits and withdrawals".

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`mtgox-mizuho-wire-pressure-2012`](./mtgox-mizuho-wire-pressure-2012.md)
- [`mtgox-usd-withdrawal-suspension-2013-06`](./mtgox-usd-withdrawal-suspension-2013-06.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a09b90d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

