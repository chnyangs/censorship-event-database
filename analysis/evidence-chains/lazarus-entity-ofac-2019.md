# Evidence chain — `lazarus-entity-ofac-2019`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `1a4f712` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:02:21Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of three DPRK-linked cyber entities (Lazarus Group, Bluenoroff,
> Andariel) on 2019-09-13 was entity-level with no enumerated on-chain addresses
> on the RA page. First state-sponsored-cyber-group OFAC action; historical
> anchor for the DPRK-laundering event thread."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2019-09-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20190913>
  - body_hash: `sha256:7c57efc7805c34000026f6ee9374609f5e69212a7655743e20cfcbc5c5c5440b`
  - body_path: `sources/http_captures/lazarus-entity-ofac-2019/ofac-recent-actions/ofac.treasury.gov__recent-actions-20190913__1d08e1f7ab.html`
  > OFAC Recent Actions page for 2019-09-13. Three DPRK-linked cyber entity
> designations: BLUENOROFF (a.k.a. APT 38 / STARDUST CHOLLIMA), LAZARUS GROUP
> (a.k.a. APPLEWORM / APT-C-26 / HIDDEN COBRA / ZINC / many other aliases), and
> ANDARIEL. All three under DPRK3 tag. Secondary sanctions risk flagged under
> North Korea Sanctions Regulations §510.201 and §510.210. **No on-chain
> addresses attached to the RA page** — entity-level designation only;
> addresses were surfaced later in Yinyin/Jiadong 2020-03-02 and subsequent
> DPRK-laundering events.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/sm774>
  > Treasury press release "Treasury Sanctions North Korean State-Sponsored Malicious Cyber Groups" (2019-09-13). Marked `contextual_unarchived` per validator hygiene (no replayable archive anchor); admission anchor is citation[0] (the OFAC RA page).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Lazarus Group + Bluenoroff + Andariel

> Three DPRK-linked cyber entities: BLUENOROFF, LAZARUS GROUP, ANDARIEL. No
> digital-currency addresses enumerated on the RA page. Entity-level
> designation; addresses surface in downstream events (Yinyin/Jiadong 2020,
> Lazarus laundering 2020, DPRK USDT network 2025).

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2019-09-13 00:00:00+00:00` → `2019-09-27 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20190913>
  - body_hash: `sha256:7c57efc7805c34000026f6ee9374609f5e69212a7655743e20cfcbc5c5c5440b`
  - body_path: `sources/http_captures/lazarus-entity-ofac-2019/ofac-recent-actions/ofac.treasury.gov__recent-actions-20190913__1d08e1f7ab.html`
  > No public CEX policy statement referencing the Lazarus/Bluenoroff/Andariel
> entity designations was issued by major exchanges (Binance, Coinbase, Kraken)
> in the 14-day post-designation window. Observation records absence of public
> disclosure; private chain-analytics KYT-flag workflows are outside scope.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`lazarus-laundering-ofac-2020`](./lazarus-laundering-ofac-2020.md)
- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)
- [`tether-dprk-precommit-freeze-2025`](./tether-dprk-precommit-freeze-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `1a4f712`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

