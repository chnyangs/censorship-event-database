# Evidence chain — `cambodia-kok-an-pig-butchering-crypto-2026`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-08` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2026-04-23 SDN designation of the Kok An / Cambodia pig-butchering
> network (sb0469) produced no public CEX cascade documented in the 14-day
> window. null_case."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2026-04-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0469>
  - body_hash: `sha256:9ff674ac200aabdabd0896c6563226e015e4e12831efecb332b4f7f65a0e8e07`
  - body_path: `sources/http_captures/cambodia-kok-an-pig-butchering-crypto-2026/source/home.treasury.gov__news-press-releases-sb0469__5a2037ecce.html`
  > Treasury press release sb0469 (2026-04-23), captured 2026-06-08 with
> body_hash; replayable local primary for the OFAC SDN designation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2026-04-23 00:00:00+00:00` → `2026-05-07 23:59:59+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://home.treasury.gov/news/press-releases/sb0469>
  - body_hash: `sha256:9ff674ac200aabdabd0896c6563226e015e4e12831efecb332b4f7f65a0e8e07`
  - body_path: `sources/http_captures/cambodia-kok-an-pig-butchering-crypto-2026/source/home.treasury.gov__news-press-releases-sb0469__5a2037ecce.html`
  > null_event anchor: OFAC SDN designation of the Kok An / Cambodia
> pig-butchering network (Treasury sb0469, 2026-04-23). No public CEX
> cascade explicitly naming the SDN entries was documented in the
> 14-day window.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

