# Evidence chain — `zimbabwe-rbz-circular-2-2018-golix`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `038e378` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "RBZ Circular 2/2018 of 2018-05-11 ordered Zimbabwean banks to cease servicing
> cryptocurrency exchanges (named: Golix, Styx24) within 60 days, severing banking rails
> for the domestic crypto off-ramp surface. Effect carried at offramp_cex; later
> provisionally suspended by the Harare High Court."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `ZW_RBZ`
- **Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20180515000000/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - Wayback: <https://web.archive.org/web/20180514120042/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - body_hash: `sha256:bfc884d752671650f0f57eac44d179ff0bf539ab53a8a07f681964edb9bffd62`
  - body_path: `sources/http_captures/zimbabwe-rbz-circular-2-2018-golix/primary/web.archive.org__web-20180515000000-https-www.techzim.co.zw-2018-05-cryptocurrency-ban-full-statement-rbz__0c19bf61cf.html`
  > Reserve Bank of Zimbabwe (RBZ) Circular No. 2/2018 to Banking Institutions on
> Virtual Currencies, signed by Registrar of Banking Institutions, dated 2018-05-11.
> Directed all banking institutions to stop providing banking services that
> facilitate dealing in or settlement of virtual currencies (maintaining accounts,
> registering/trading/clearing, processing payments, giving loans against crypto
> tokens, or accepting them as collateral). The circular names Bitfinance (Private)
> Limited (trading as Golix) and Styx24 as the major exchanges then operating in
> Zimbabwe, and gave institutions 60 days to terminate existing relationships and
> return account balances. Full statement text captured via Techzim (Wayback memento
> 2018-05-14); the page reproduces the RBZ circular verbatim.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Golix / Styx24 and Zimbabwean crypto exchanges / users (class)

> Zimbabwean crypto exchanges and users as a class; the circular explicitly names
> Bitfinance (Private) Limited trading as Golix and Styx24 as the two major exchanges
> targeted. Banking-service severance applied to all institutions and any entity dealing
> in virtual currencies.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `banking_channel_severed_named_exchanges_golix_styx24`

**Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20180515000000/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - body_hash: `sha256:bfc884d752671650f0f57eac44d179ff0bf539ab53a8a07f681964edb9bffd62`
  - body_path: `sources/http_captures/zimbabwe-rbz-circular-2-2018-golix/primary/web.archive.org__web-20180515000000-https-www.techzim.co.zw-2018-05-cryptocurrency-ban-full-statement-rbz__0c19bf61cf.html`
  > RBZ Circular 2/2018 is the legal instrument. attribution=direct because the
> circular itself mandates the banking cut-off and explicitly names the targeted
> exchanges (Golix, Styx24).

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `038e378`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

