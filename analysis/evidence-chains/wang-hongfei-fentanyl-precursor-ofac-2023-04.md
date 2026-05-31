# Evidence chain — `wang-hongfei-fentanyl-precursor-ofac-2023-04`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1b889eb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2023-04-14 OFAC designation of Wang Hongfei and PRC chemical firms
> WSBT/SXPC (fentanyl-precursor suppliers) attached a Bitcoin address (the specific
> address is enumerated in the SDN-list entry, not in press release jy1413); no public CEX cascade was documented
> in the 14-day window. null_case: precursor-network target with limited
> measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-04-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1413>
  - Wayback: <https://web.archive.org/web/20230414185648/https://home.treasury.gov/news/press-releases/jy1413>
  - body_hash: `sha256:a21590abd62b77e12a3daf32d2dedf18faaa8bc26cbc95bc63d76a4106068386`
  - body_path: `sources/http_captures/wang-hongfei-fentanyl-precursor-ofac-2023-04/primary/web.archive.org__web-20230414185648-https-home.treasury.gov-news-press-releases-jy1413__1506ea8818.html`
  > U.S. Treasury press release jy1413 (2023-04-14), "U.S. Sanctions
> Suppliers of Precursor Chemicals for Fentanyl Production." OFAC
> designated two PRC chemical firms (Wuhan Shuokang Biological
> Technology / WSBT and Suzhou Xiaoli Pharmatech / SXPC) and five
> individuals, including Wang Hongfei, a WSBT collaborator who
> controlled a Bitcoin address used to receive payments for illicit
> fentanyl-precursor sales: 3PKiHs4GY4rFg8dpppNVPXGPqMX6K2cBML.
> Wayback memento 20230414185648 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Wang Hongfei / WSBT / SXPC

> Wang Hongfei and PRC chemical firms WSBT/SXPC designated as SDNs under
> the fentanyl/counter-narcotics authority, with one Bitcoin address
> (3PKiHs4GY4rFg8dpppNVPXGPqMX6K2cBML) attributed to Wang Hongfei.
> Marked subset because the target is the named individuals/firms; the
> on-chain address is not separately re-listed in this draft pending a
> primary_onchain freeze receipt (deferred per codebook §1.6).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2023-04-14 00:00:00+00:00` → `2023-04-28 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1413>
  - Wayback: <https://web.archive.org/web/20230414185648/https://home.treasury.gov/news/press-releases/jy1413>
  - body_hash: `sha256:a21590abd62b77e12a3daf32d2dedf18faaa8bc26cbc95bc63d76a4106068386`
  - body_path: `sources/http_captures/wang-hongfei-fentanyl-precursor-ofac-2023-04/primary/web.archive.org__web-20230414185648-https-home.treasury.gov-news-press-releases-jy1413__1506ea8818.html`
  > No public CEX policy statement referencing the Wang Hongfei BTC
> address was published by major exchanges in the 14-day post-
> designation window. Observation records the absence of public
> disclosure; private chain-analytics KYT flagging is outside this
> observation's scope.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet probe in scope; the designees are
- **asset_onchain** (`not_measured`): The SDN entry attaches Bitcoin address

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1b889eb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

