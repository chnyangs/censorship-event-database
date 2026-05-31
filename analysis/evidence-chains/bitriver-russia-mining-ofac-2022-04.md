# Evidence chain — `bitriver-russia-mining-ofac-2022-04`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `af3a9ed` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-04-20 OFAC designation of BitRiver AG + 10 Russia-based
> subsidiaries (the first OFAC sanction of a crypto-mining company)
> attached no on-chain addresses; no public CEX cascade was documented
> in the 14-day window. null_case: infrastructure-entity target with
> limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-04-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0731>
  - Wayback: <https://web.archive.org/web/20220430203000/https://home.treasury.gov/news/press-releases/jy0731>
  - body_hash: `sha256:29ae5daf08553def8ccf7f30a9da1516bbe9bbfd25c01bb24492c12163c778be`
  - body_path: `sources/http_captures/bitriver-russia-mining-ofac-2022-04/primary/web.archive.org__web-20220501000000-https-home.treasury.gov-news-press-releases-jy0731__70365f1f26.html`
  > U.S. Treasury press release jy0731 (2022-04-20): OFAC designated
> BitRiver AG (Switzerland-headquartered) and ten Russia-based
> subsidiaries — the FIRST OFAC designation of a cryptocurrency-
> MINING company — for operating in Russia's technology sector and
> helping Russia monetize its natural resources / evade sanctions
> via crypto mining. Wayback 20220430203000 pinned.
- **`semi_primary_wayback`**
  - URL: <https://therecord.media/us-treasury-dept-sanctions-russian-crypto-mining-giant-bitriver>
  - Wayback: <https://web.archive.org/web/20220421190013/https://therecord.media/us-treasury-dept-sanctions-russian-crypto-mining-giant-bitriver>
  - body_hash: `sha256:e251f0fa7d3dd43973cb8bd1966061cd36fa96dc60885e1decf10c1cdce692f3`
  - body_path: `sources/http_captures/bitriver-russia-mining-ofac-2022-04/primary/web.archive.org__web-20220421000000-https-therecord.media-us-treasury-dept-sanctions-russian-crypto-mining-giant-bitriver__2423a37ff1.html`
  > The Record (Recorded Future News) 2022-04-20 coverage confirming
> the first-of-its-kind OFAC designation of a crypto-mining company
> (BitRiver). Independent corroborating anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BitRiver AG + 10 Russia-based subsidiaries
- **Canonical domains**: `bitriver.com`

> BitRiver AG (Switzerland HQ) plus ten Russia-based subsidiaries
> designated as SDNs. A crypto-mining-infrastructure company (not an
> asset issuer); the OFAC entry names the corporate entities rather
> than enumerating on-chain addresses, so no addresses are attached.
> Marked subset because the action targets the named BitRiver
> corporate group rather than an enumerated complete address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2022-04-20 00:00:00+00:00` → `2022-05-04 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0731>
  - Wayback: <https://web.archive.org/web/20220430203000/https://home.treasury.gov/news/press-releases/jy0731>
  - body_hash: `sha256:29ae5daf08553def8ccf7f30a9da1516bbe9bbfd25c01bb24492c12163c778be`
  - body_path: `sources/http_captures/bitriver-russia-mining-ofac-2022-04/primary/web.archive.org__web-20220501000000-https-home.treasury.gov-news-press-releases-jy0731__70365f1f26.html`
  > No public CEX policy statement referencing the BitRiver
> corporate group was published by major exchanges in the 14-day
> post-designation window. Observation records the absence of
> public disclosure; private chain-analytics KYT flagging is
> outside this observation's scope. BitRiver is a mining
> operator (no enumerated addresses), so the measurable
> offramp-cascade surface is structurally limited.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet probe of bitriver.com within the event
- **l4_frontend** (`not_measured`): bitriver.com is the company's canonical domain; Wayback CDX

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `af3a9ed`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

