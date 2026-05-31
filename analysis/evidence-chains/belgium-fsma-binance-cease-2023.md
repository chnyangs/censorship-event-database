# Evidence chain — `belgium-fsma-binance-cease-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `cd67682` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "FSMA order of 2023-06-23 directly compelled Binance to cease offering
> virtual-currency exchange and custody-wallet services to Belgian
> residents and to repatriate customer holdings from non-EEA-incorporated
> Binance entities, producing a regulator-mandated operator-state change
> at the Binance Belgian-customer cohort (offramp_cex load-bearing) and a
> Binance-corporate L4 frontend response (Belgium-geo restriction notices,
> attribution=plausible). The row does not claim ISP-level connectivity
> blocking, on-chain asset freeze, or class-wide Belgian banking-rail
> severance."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `BE_FSMA`
- **Timestamp**: `2023-06-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsma.be/en/news>
  - Wayback: <https://web.archive.org/web/2023/https://www.fsma.be/en/news>
  > Belgian Financial Services and Markets Authority (FSMA) press
> announcement dated 2023-06-23 ordering Binance to cease immediately
> all offers of virtual-currency exchange and custody-wallet services
> in Belgium, and ordering Binance to repatriate to Belgian customers
> all virtual-currency holdings and cryptographic keys held on their
> behalf by non-EEA-incorporated Binance entities. Wayback anchor is
> a 2023 calendar-folder pointer at fsma.be/en/news rather than a
> pinned snapshot of the specific press item; the press item URL slug
> is referenced in the candidate stub
> (candidate_triggers/belgium-fsma-binance-cease-2023.yaml). Marked
> evidence_use=contextual_unarchived because the authoring LLM agent
> did not personally pin a Wayback timestamp or compute a body_hash
> for the FSMA press item; the specific snapshot and body_hash must
> be re-pinned during human audit before this citation may serve as
> an admission anchor in its own right.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Belgium-facing entities)
- **Canonical domains**: `binance.com`

> Binance group entities offering virtual-currency exchange and
> custody-wallet services to Belgian residents, and (by cascade) the
> Belgian retail customer cohort of the global binance.com platform.
> The FSMA order names Binance group entities incorporated outside the
> European Economic Area (EEA) as the immediate addressees of the
> cease-and-repatriate directive; the operational effect is on Belgian
> retail users of binance.com. Treated as entity-level at the
> Binance-Belgium cohort.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_belgium_services_ordered_to_cease_and_assets_repatriated`

**Timestamp**: `2023-06-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsma.be/en/news>
  - Wayback: <https://web.archive.org/web/2023/https://www.fsma.be/en/news>
  > FSMA press release is the legal instrument naming Binance as
> addressee of the cease-and-desist and repatriation order.
> attribution=direct because the FSMA order itself compels the
> operator-state change (cessation of Belgian-facing exchange and
> custody-wallet service) and the four-month repatriation window
> for non-EEA-held customer holdings flows directly from the order.
> DRYRUN: Wayback anchor is a 2023 calendar-folder pointer; pinned
> snapshot timestamp and body_hash capture deferred to human audit.

### l4_frontend · attribution: `plausible` · Δt = 24h

**Event label**: `be_geo_specific_restriction_notices_posted`

**Timestamp**: `2023-06-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsma.be/en/news>
  - Wayback: <https://web.archive.org/web/2023/https://www.fsma.be/en/news>
  > FSMA press item is the regulatory anchor for the Binance-BE
> frontend response: Binance posted Belgium-specific user notices
> and onboarding restrictions in the days following the FSMA order.
> attribution=plausible because the frontend banner / regional
> notice is a Binance-corporate response, not a regulator-mandated
> DOM change. DRYRUN: pinned Wayback snapshot of the binance.com
> Belgium-geo notice page is deferred to human audit; the FSMA
> press item is retained here as the contextual anchor for the
> frontend response.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)
- [`philippines-sec-binance-block-2024`](./philippines-sec-binance-block-2024.md)
- [`binance-4framework-2023`](./binance-4framework-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cd67682`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

