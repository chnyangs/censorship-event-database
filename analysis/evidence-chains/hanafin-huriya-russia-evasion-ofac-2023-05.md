# Evidence chain — `hanafin-huriya-russia-evasion-ofac-2023-05`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `89285c6` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2023-05-19 SDN designation of John Desmond Hanafin + Huriya Private
> (Dubai), part of the jy1494 Russia-evasion action, named a single Ethereum
> address. No public CEX cascade was documented in the 14-day window.
> null_case: financial-services-facilitator target with limited measurable
> cross-layer surface at draft time."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-05-19 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1494>
  - Wayback: <https://web.archive.org/web/20230519161141/https://home.treasury.gov/news/press-releases/jy1494>
  - body_hash: `sha256:b3ee6a6ba713b4c6f7c4d1a6ca05efafc98391061e97bc1b31a7f35595965c09`
  - body_path: `sources/http_captures/hanafin-huriya-russia-evasion-ofac-2023-05/primary/web.archive.org__web-20230519000000-https-home.treasury.gov-news-press-releases-jy1494__49f614ecb7.html`
  > Treasury press release jy1494 (2023-05-19) "With Over 300 Sanctions,
> U.S. Targets Russia's Circumvention and Evasion...". Among the 22
> individuals + 104 entities designated under EO 14024 is Dubai-based
> John Desmond Hanafin (Irish national, founder/CEO of Huriya Private)
> and his firms Huriya Private FZE LLE, Huriya Private Cyprus Ltd., and
> Gold Miles Ltd. (HK), for crypto/financial-services facilitation of
> Russian sanctions evasion — moving Russian nationals' funds into UAE
> accounts. Wayback 20230519161141 pinned; grep verifies 18xHanafin,
> 20xHuriya, 8x"May 19, 2023".
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20230519>
  - Wayback: <https://web.archive.org/web/20230519152222/https://ofac.treasury.gov/recent-actions/20230519>
  - body_hash: `sha256:7d7cb183e4070782d4e18efe91394d9b59749d20d62c7481815e2f9ec8b56d0d`
  - body_path: `sources/http_captures/hanafin-huriya-russia-evasion-ofac-2023-05/primary/web.archive.org__web-20230519000000-https-ofac.treasury.gov-recent-actions-20230519__7ac3487571.html`
  > OFAC Recent Actions page for 2023-05-19, the formal SDN-list publication
> accompanying jy1494. Hanafin's SDN entry carries an Ethereum address
> identifier (0x38735f03b30FbC022DdD06ABED01F0Ca823C6a94, ~$4.9M received,
> mostly USDT, per Chainalysis). Independent primary anchor for the
> designation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: John Desmond Hanafin + Huriya Private (Dubai)
- **Chains**: `ethereum`
- **Addresses**: 1 total (enumerated in event YAML)

> John Desmond Hanafin (individual) + Huriya Private FZE LLE (Dubai) and
> affiliated firms (Huriya Private Cyprus Ltd., Gold Miles Ltd. HK). Hanafin's
> SDN entry names a single Ethereum-address identifier. Subset enumeration:
> the Hanafin/Huriya cluster is one node within a 126-target Russia-evasion
> action (jy1494); the broader action is out of scope for this event's target.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-05-19 00:00:00+00:00` → `2023-06-02 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1494>
  - Wayback: <https://web.archive.org/web/20230519161141/https://home.treasury.gov/news/press-releases/jy1494>
  - body_hash: `sha256:b3ee6a6ba713b4c6f7c4d1a6ca05efafc98391061e97bc1b31a7f35595965c09`
  - body_path: `sources/http_captures/hanafin-huriya-russia-evasion-ofac-2023-05/primary/web.archive.org__web-20230519000000-https-home.treasury.gov-news-press-releases-jy1494__49f614ecb7.html`
  > No public CEX policy statement explicitly naming the Hanafin/Huriya
> SDN entry was published by major exchanges in the 14-day
> post-designation window. Records absence of public disclosure;
> private chain-analytics KYT flagging is outside this observation's
> scope.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `89285c6`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

