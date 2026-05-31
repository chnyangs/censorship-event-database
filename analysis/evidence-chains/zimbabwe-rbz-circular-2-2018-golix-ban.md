# Evidence chain — `zimbabwe-rbz-circular-2-2018-golix-ban`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `97f58fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "RBZ Circular No. 2/2018 (2018-05-11) ordered all Zimbabwean banks to stop
> servicing cryptocurrency exchanges within 60 days, naming Golix/BitFinance and
> Styx24, severing the banking rail for the Zimbabwean crypto exchange sector.
> Golix obtained a High Court provisional suspension on 2018-05-24. The
> offramp_cex layer carries the load-bearing direct-attribution observation."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `ZW_RBZ`
- **Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20180512143200/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - Wayback: <https://web.archive.org/web/20180512143200/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - body_hash: `sha256:fdc71369459215066780646f02ee3aedc2a718b58cdf16a24d44e49aa0481225`
  - body_path: `sources/http_captures/zimbabwe-rbz-circular-2-2018-golix-ban/primary/web.archive.org__web-20180512143200-https-www.techzim.co.zw-2018-05-cryptocurrency-ban-full-statement-rbz__32712142e9.html`
  > Reserve Bank of Zimbabwe Circular No. 2/2018, issued 2018-05-11 by the
> Registrar of Banking Institutions (Norman Mataruka) to all banking
> institutions. The circular directs all financial institutions to stop
> using, trading, holding or transacting in virtual currencies and to stop
> providing banking services facilitating dealing in virtual currencies
> (accounts, payments, loans against crypto, collateral). Banks were given
> 60 days to exit existing relationships with cryptocurrency exchanges and
> return account balances. The circular names BitFinance (Pvt) Ltd
> (trading as Golix) and Styx24 as the major Zimbabwean crypto exchanges.
> Captured page reproduces the full RBZ statement text; archived via
> Wayback 2018-05-12 (day after issuance).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Golix / BitFinance, Styx24 + ZW banking sector (class)

> Named Zimbabwean crypto exchanges BitFinance (trading as Golix) and Styx24,
> plus the regulated banking sector ordered to debank them. The RBZ circular
> explicitly names Golix/Bitfinance and Styx24; the broader class is all
> Zimbabwean banking-rail-dependent crypto exchanges/users. Treated as subset
> (named exchanges + class-level banking sector). Golix obtained a Harare High
> Court provisional order on 2018-05-24 suspending the ban (downstream coda).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `banking_rail_severed_named_exchanges_60_day_winddown`

**Timestamp**: `2018-05-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://web.archive.org/web/20180512143200/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - Wayback: <https://web.archive.org/web/20180512143200/https://www.techzim.co.zw/2018/05/cryptocurrency-ban-full-statement-rbz/>
  - body_hash: `sha256:fdc71369459215066780646f02ee3aedc2a718b58cdf16a24d44e49aa0481225`
  - body_path: `sources/http_captures/zimbabwe-rbz-circular-2-2018-golix-ban/primary/web.archive.org__web-20180512143200-https-www.techzim.co.zw-2018-05-cryptocurrency-ban-full-statement-rbz__32712142e9.html`
  > RBZ Circular No. 2/2018 is the legal instrument (full text reproduced
> on the captured page). attribution=direct because the circular
> explicitly names Golix/BitFinance and Styx24 and orders all banks to
> stop servicing crypto exchanges within 60 days.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `97f58fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

