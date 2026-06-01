# Evidence chain — `korea-fiu-isms-real-name-exchange-shutdown-2021-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1a4f712` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:02:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "South Korea's 2021-09-24 FIU registration deadline (amended Specific Financial Information
> Act) forced unregistered exchanges to shut down and certified-but-unbanked exchanges to cease
> Korean-won fiat trading; ~40 exchanges faced shutdown, four (Upbit/Bithumb/Coinone/Korbit)
> survived with full service. Effect carried at offramp_cex (class-level, partially measured)."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `KR_FIU`
- **Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications>
  - Wayback: <https://web.archive.org/web/20210924170155/https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications/>
  - body_hash: `sha256:a3bea46c09710a5d4288bbe4da6f74afbb1517ebb1d4441072178eee2c036b5f`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary/web.archive.org__web-20210924170155-https-www.coindesk.com-policy-2021-09-24-hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications__84cac51a04.html`
  > CoinDesk, 2021-09-24, reporting the 2021-09-24 South Korean Financial Intelligence
> Unit (FIU) registration deadline under the amended Act on Reporting and Use of Specific
> Financial Information. Virtual-asset service providers had to register with the FIU,
> secure real-name verified bank accounts and a security certification, and meet AML
> requirements to keep operating. Exchanges failing to register had to shut down (or, for
> those with certification but no bank partnership, cease Korean-won fiat trading). The
> captured article documents that only the four exchanges with bank partnerships
> (Upbit, Bithumb, Coinone, Korbit) could continue full won-settlement services, and
> ~40 exchanges faced shutdown. Wayback snapshot 20210924170155 (replayable body_hash).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: South Korean virtual-asset exchanges subject to FIU registration (class)

> The class of South Korean virtual-asset exchanges subject to the FIU registration regime.
> The captured source names the four survivors with full won-settlement (Upbit, Bithumb,
> Coinone, Korbit) and reports ~40 exchanges facing shutdown; the full roster of shut-down
> exchanges is not enumerated in the captured source. enumeration=subset (class-level).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `fiu_registration_deadline_forced_exchange_shutdown_and_fiat_rail_severance`

**Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications>
  - Wayback: <https://web.archive.org/web/20210924170155/https://www.coindesk.com/policy/2021/09/24/hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications/>
  - body_hash: `sha256:a3bea46c09710a5d4288bbe4da6f74afbb1517ebb1d4441072178eee2c036b5f`
  - body_path: `sources/http_captures/korea-fiu-isms-real-name-exchange-shutdown-2021-09/primary/web.archive.org__web-20210924170155-https-www.coindesk.com-policy-2021-09-24-hours-before-s-korean-registration-deadline-only-10-exchanges-have-submitted-applications__84cac51a04.html`
  > CoinDesk 2021-09-24: at the FIU deadline, unregistered exchanges had to shut down and
> certified-but-unbanked exchanges had to cease won fiat trading; four exchanges
> (Upbit, Bithumb, Coinone, Korbit) had secured bank partnerships for full service,
> ~40 faced shutdown. attribution=plausible (per §1.5/§8.4): the anchor is journalism
> reporting the FIU regime, not the FIU's own primary order, and the target is the
> exchange industry as a class. Conservative default.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`korea-fsc-institutional-restriction-2017`](./korea-fsc-institutional-restriction-2017.md)
- [`korea-fsc-ico-ban-2017`](./korea-fsc-ico-ban-2017.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1a4f712`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

