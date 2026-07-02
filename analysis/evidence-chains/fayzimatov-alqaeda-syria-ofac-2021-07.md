# Evidence chain — `fayzimatov-alqaeda-syria-ofac-2021-07`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-07-28 OFAC designated Farrukh Furkatovitch Fayzimatov and listed
> one Bitcoin/XBT address, 17a5bpKvEp1j1Trs4qTbcNZrby53JbaS9C. Treasury's
> same-day release describes Fayzimatov as soliciting donations for HTS. This
> draft models the event as an individual-BTC OFAC null_case: no issuer-admin
> asset freeze is possible and no public CEX cascade has been pinned."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2021-07-28 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20210728>
  - body_hash: `sha256:9138b98dadd6b5c229099e886b200cc61f1d649e235d2cc4ceace8e428f6f0f1`
  - body_path: `sources/http_captures/fayzimatov-alqaeda-syria-ofac-2021-07/primary/ofac.treasury.gov__recent-actions-20210728__74c2273c08.html`
  > OFAC Recent Actions page for 2021-07-28, captured locally on
> 2026-05-31. The SDN update lists Farrukh Furkatovitch Fayzimatov
> with a single Digital Currency Address - XBT:
> 17a5bpKvEp1j1Trs4qTbcNZrby53JbaS9C, under the SDGT authority.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0293>
  - body_hash: `sha256:1dbebf420a418ec8e9db7698f6e32fc6c6f03b7b4ca6f3da3ced7d93c353edb6`
  - body_path: `sources/http_captures/fayzimatov-alqaeda-syria-ofac-2021-07/primary/home.treasury.gov__news-press-releases-jy0293__b9a2c681a6.html`
  > Treasury press release "Treasury Designates Al-Qa'ida-Linked
> Financial Facilitators in Turkey and Syria" (2021-07-28), captured
> locally on 2026-05-31. The source states that Fayzimatov used social
> media to post propaganda, recruit, and solicit donations for Hay'et
> Tahrir Al-Sham, and was designated for material support to HTS.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Farrukh Furkatovitch Fayzimatov
- **Chains**: `bitcoin`
- **Addresses**: 1 total (enumerated in event YAML)

> The captured OFAC SDN update enumerates one XBT digital-currency address
> for Farrukh Furkatovitch Fayzimatov. Complete at the event-row level for
> the crypto-address cohort visible in the official OFAC source.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2021-07-28 00:00:00+00:00` → `2021-08-11 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20210728>
  - body_hash: `sha256:9138b98dadd6b5c229099e886b200cc61f1d649e235d2cc4ceace8e428f6f0f1`
  - body_path: `sources/http_captures/fayzimatov-alqaeda-syria-ofac-2021-07/primary/ofac.treasury.gov__recent-actions-20210728__74c2273c08.html`
  > No public CEX policy statement naming the Fayzimatov XBT address has
> been pinned for the 14-day post-designation window. The observation
> is limited to public-disclosure absence; private KYT flagging is not
> measured here.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`ofac-hamas-buy-cash-msb-2023-10`](./ofac-hamas-buy-cash-msb-2023-10.md)
- [`ofac-hamas-gaza-now-2024-03`](./ofac-hamas-gaza-now-2024-03.md)
- [`zheng-yan-fentanyl-ofac-2019-08`](./zheng-yan-fentanyl-ofac-2019-08.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

