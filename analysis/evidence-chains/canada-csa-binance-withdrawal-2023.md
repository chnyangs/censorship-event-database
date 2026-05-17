# Evidence chain — `canada-csa-binance-withdrawal-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-17` · **Source commit**: `1d420be` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-17T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-02-22 CSA Staff Notice 21-332 enhanced pre-registration-undertaking
> framework — restricting Canadian crypto-trading-platform stablecoin offerings
> and investor-position limits — produced a 2-layer cascade for the Binance
> Canada cohort: a customer-facing market-exit announcement on binance.com
> (2023-05-12) and a corresponding offramp_cex shutdown of CAD rails and
> Canadian-resident accounts. Structurally an entity-self-withdrawal response
> to a class-wide securities-registration framework rather than a banking-rail
> cascade."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CA_CSA`
- **Timestamp**: `2023-02-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.securities-administrators.ca/news/>
  - Wayback: <https://web.archive.org/web/20230222000000*/securities-administrators.ca/news/>
  > CSA (Canadian Securities Administrators) Staff Notice 21-332
> (2023-02-22): "Canadian Securities Regulators Strengthen Approach to
> Crypto Trading Platforms with Enhanced Pre-Registration Undertakings
> Expectations." The notice updates the pre-registration-undertaking
> (PRU) framework first announced in 21-329, requiring crypto-trading
> platforms operating in Canada to file enhanced PRUs that prohibit
> offering leverage/margin trading to Canadian clients, segregate
> client assets, and restrict the holding of proprietary stablecoins
> without CSA approval. Marked evidence_use=contextual_unarchived
> because the authoring LLM agent did not personally pin a Wayback
> snapshot timestamp or compute a body_hash for the CSA news page;
> the canonical CSA news index is routinely captured by Wayback but
> the specific 2023-02-22 snapshot is to be re-pinned during human
> audit before this citation may serve as an admission anchor.
- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227>
  - Wayback: <https://web.archive.org/web/20230512000000*/binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227>
  > Binance corporate blog post (2023-05-12): "An Update on Binance in
> Canada." Binance announced it would proactively withdraw from the
> Canadian market, citing the CSA's evolving guidance — specifically
> restrictions on stablecoin offerings and investor-position limits
> introduced by the 2023-02-22 Staff Notice 21-332 — as no longer
> tenable for its Canada operations. ~80-day delta between the CSA
> notice and the Binance withdrawal announcement. Marked
> evidence_use=contextual_unarchived pending human-audit Wayback
> re-pin and body_hash capture.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Canada user cohort)
- **Canonical domains**: `binance.com`

> Canada-registered crypto-trading-platform cohort regulated by the CSA's
> pre-registration-undertaking framework. Binance is the load-bearing
> target for the observable cascade because it announced full Canada
> market exit 2023-05-12 citing the 2023-02-22 Staff Notice's revised
> stablecoin and position-limit restrictions. Other Canadian-active
> platforms (e.g., Kraken Canada, KuCoin) either filed PRUs and remained
> or exited on different timelines; this row treats the Binance-Canada
> cohort as the focal cascade leg while flagging the class-wide CSA
> posture as the trigger.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 1920h

**Event label**: `binance_canada_market_exit_announcement`

**Timestamp**: `2023-05-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227>
  - Wayback: <https://web.archive.org/web/20230512000000*/binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227>
  > Binance corporate blog post (2023-05-12) is the canonical
> customer-facing notification of Canadian market exit. The post
> explicitly cites the CSA's evolving guidance (stablecoin
> offerings, investor-position limits) introduced via the
> 2023-02-22 Staff Notice 21-332 as the precipitating cause —
> attribution=direct on this basis. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin.
- **`primary_legal`**
  - URL: <https://www.securities-administrators.ca/news/>
  - Wayback: <https://web.archive.org/web/20230222000000*/securities-administrators.ca/news/>
  > CSA Staff Notice 21-332 is the regulatory anchor for the
> frontend announcement; Binance's blog post names the CSA's
> enhanced pre-registration-undertaking expectations as the
> driving cause of withdrawal.

### offramp_cex · attribution: `direct` · Δt = 1920h

**Event label**: `binance_canada_offramp_shutdown`

**Timestamp**: `2023-05-12 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227>
  - Wayback: <https://web.archive.org/web/20230512000000*/binance.com/en/blog/ecosystem/an-update-on-binance-in-canada-3550161948550610227>
  > Binance blog post documents the operational off-boarding plan
> for Canadian-resident accounts: transition to withdraw-only
> mode and wind-down of CAD payment rails to Binance over the
> months following 2023-05-12. attribution=direct because the
> blog post explicitly ties the operational shutdown to the CSA
> regulatory framework.
- **`primary_legal`**
  - URL: <https://www.securities-administrators.ca/news/>
  - Wayback: <https://web.archive.org/web/20230222000000*/securities-administrators.ca/news/>
  > CSA Staff Notice 21-332 (2023-02-22) is the legal instrument
> imposing the enhanced pre-registration-undertaking expectations
> whose stablecoin and investor-position-limit provisions Binance
> cited as untenable for continued Canada operations.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`malaysia-sc-binance-disable-2021`](./malaysia-sc-binance-disable-2021.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1d420be`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

