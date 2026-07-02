# Evidence chain — `task-force-rusich-ofac-2022-09`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2022-09-15 OFAC E.O. 14024 designation of Task Force Rusich (a
> Russian paramilitary crowdfunding group) attached five crypto addresses
> (2 BTC, 2 ETH, 1 USDT-Tron); no public CEX cascade was documented in the
> 14-day window. null_case: paramilitary-group target with limited
> measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2022-09-15 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0954>
  - Wayback: <https://web.archive.org/web/20220916012425/https://home.treasury.gov/news/press-releases/jy0954>
  - body_hash: `sha256:1407d5948d7d5d982888f38a953d00eab01e7766bed8a6c6e47df509bb1a01e1`
  - body_path: `sources/http_captures/task-force-rusich-ofac-2022-09/primary/web.archive.org__web-20220916012425-https-home.treasury.gov-news-press-releases-jy0954__080bb3a4c1.html`
  > U.S. Treasury press release jy0954 (2022-09-15), "Treasury Targets
> Additional Facilitators of Russia's Aggression in Ukraine." Among
> 22 individuals and 2 entities designated under E.O. 14024 was Task
> Force Rusich, a neo-Nazi paramilitary group (and its leaders
> Milchakov / Petrovskiy). OFAC attached five crypto addresses (2
> BTC, 2 ETH, 1 USDT-on-Tron) tied to a Rusich military-hardware
> crowdfunding campaign for pro-Russian troops in Ukraine. Wayback
> memento 20220916012425 pinned.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220915>
  - body_hash: `sha256:22ad2861c1adbcf4036a3d5951e4af949dabff8040bfa3d07ce1db0faebf3f34`
  - body_path: `sources/http_captures/task-force-rusich-ofac-2022-09/primary/ofac.treasury.gov__recent-actions-20220915__943c5c2580.html`
  > OFAC Recent Actions page for 2022-09-15, captured locally on
> 2026-05-31. The SDN-list update names TASK FORCE RUSICH and
> enumerates five digital-currency addresses attached to the entity:
> two XBT addresses, two ETH addresses, and one USDT-on-Tron address.
> This repairs the earlier crypto-nexus source gap in the jy0954-only
> draft without relying on secondary reporting.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Task Force Rusich
- **Chains**: `bitcoin`, `ethereum`, `tron`
- **Addresses**: 5 total (enumerated in event YAML)

> Task Force Rusich designated as an SDN entity under E.O. 14024 with
> five attached crypto addresses (2 XBT, 2 ETH, 1 USDT-on-Tron), all
> enumerated verbatim from the OFAC Recent Actions page. Marked subset
> because the broader 2022-09-15 action designated many individuals and
> entities; only the Rusich crypto cohort is in scope for this event.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2022-09-15 00:00:00+00:00` → `2022-09-29 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20220915>
  - body_hash: `sha256:22ad2861c1adbcf4036a3d5951e4af949dabff8040bfa3d07ce1db0faebf3f34`
  - body_path: `sources/http_captures/task-force-rusich-ofac-2022-09/primary/ofac.treasury.gov__recent-actions-20220915__943c5c2580.html`
  > OFAC Recent Actions page for 2022-09-15, the formal SDN-list
> publication for the designation. The TASK FORCE RUSICH entry
> enumerates two XBT addresses, two ETH addresses, and one
> USDT-on-Tron address. No public CEX policy statement explicitly
> naming this five-address cohort was found in the 14-day window;
> private KYT flagging is outside this observation's scope.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy0954>
  - Wayback: <https://web.archive.org/web/20220916012425/https://home.treasury.gov/news/press-releases/jy0954>
  - body_hash: `sha256:1407d5948d7d5d982888f38a953d00eab01e7766bed8a6c6e47df509bb1a01e1`
  - body_path: `sources/http_captures/task-force-rusich-ofac-2022-09/primary/web.archive.org__web-20220916012425-https-home.treasury.gov-news-press-releases-jy0954__080bb3a4c1.html`
  > No public CEX policy statement referencing the five Rusich
> addresses was published by major exchanges in the 14-day post-
> designation window. Observation records the absence of public
> disclosure; private chain-analytics KYT flagging is outside this
> observation's scope.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet probe in scope; the designee is a
- **asset_onchain** (`not_measured`): The SDN entry attaches five addresses (2 BTC, 2 ETH, 1 USDT-Tron).

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

