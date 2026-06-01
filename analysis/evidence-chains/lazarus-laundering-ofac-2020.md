# Evidence chain — `lazarus-laundering-ofac-2020`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `34b152d` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T05:22:19Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of two DPRK-laundering Chinese nationals on 2020-03-02 attached 20
> Bitcoin addresses to SDN; cross-layer cascade is structurally unmeasurable (Bitcoin native,
> individuals). Serves as a datapoint for the individual-BTC-sanction class."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2020-03-02 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20200302>
  - Wayback: <https://web.archive.org/web/20260421141654/https://ofac.treasury.gov/recent-actions/20200302>
  - body_hash: `sha256:52785ac24ed108c94962601d6957ba440702bc7eafc4b816dc02a41246b927b3`
  - body_path: `sources/http_captures/lazarus-laundering-ofac-2020/ofac-recent-actions/ofac.treasury.gov__recent-actions-20200302__65d2ac091f.html`
  > OFAC Recent Actions page for 2020-03-02. Two Chinese nationals laundering crypto for
> DPRK/Lazarus designated: LI Jiadong (aka blackjack1987 / khaleesi) with 12 XBT, and
> TIAN Yinyin (aka snowsjohn) with 8 XBT. Tags [DPRK3] [CYBER2] (Linked To: LAZARUS
> GROUP). Total 20 unique XBT addresses.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm924>
  > Treasury press release "Treasury Sanctions Individuals Laundering Cryptocurrency for Lazarus Group" (2020-03-02).

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: LI Jiadong + TIAN Yinyin
- **Chains**: `bitcoin`
- **Addresses**: 20 total (enumerated in event YAML)

> 20 unique Bitcoin addresses across 2 Chinese individuals (12 + 8).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2020-03-02 00:00:00+00:00` → `2020-03-16 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20200302>
  - body_hash: `sha256:52785ac24ed108c94962601d6957ba440702bc7eafc4b816dc02a41246b927b3`
  - body_path: `sources/http_captures/lazarus-laundering-ofac-2020/ofac-recent-actions/ofac.treasury.gov__recent-actions-20200302__65d2ac091f.html`
  > No public CEX policy statement referencing the 20 Lazarus-laundering BTC addresses
> was published in the 14-day window post-designation. This is the honest empirical
> null for individual-level BTC-only designations from 2020-era OFAC actions: the
> offramp-CEX cascade, if any occurred, happened through private
> chain-analytics-driven KYC flags rather than public corporate statements.
> attribution=none because an absence-of-public-announcement is not causally
> attributable to the OFAC action — it reflects the industry's preference for
> private compliance workflows over public disclosure for this event class.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`lazarus-entity-ofac-2019`](./lazarus-entity-ofac-2019.md)
- [`sichuan-silence-ofac-2024`](./sichuan-silence-ofac-2024.md)
- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `34b152d`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

