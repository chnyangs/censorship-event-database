# Evidence chain — `evil-corp-ofac-2024-10`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `0785824` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:44:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2024-10-01 tri-lateral OFAC SDN designation of Evil Corp members/
> facilitators (incl. Eduard Benderskiy) is confirmed against Treasury jy2623;
> the entry names individuals/entities (no enumerated on-chain addresses) and
> no public CEX cascade was documented in the 14-day window. null_case:
> limited measurable cross-layer surface."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-10-01 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2623>
  - Wayback: <https://web.archive.org/web/20241002115708/https://home.treasury.gov/news/press-releases/jy2623>
  - body_hash: `sha256:acff2559861b6e13bb3fbf6287c8f36d612174bdedac3744c5dc9b7d2c67663a`
  - body_path: `sources/http_captures/evil-corp-ofac-2024-10/primary/web.archive.org__web-20241002120000-https-home.treasury.gov-news-press-releases-jy2623__f5d9c9c476.html`
  > U.S. Treasury press release jy2623 (2024-10-01): OFAC designated seven
> individuals and two entities tied to the Russia-based Evil Corp
> cybercrime syndicate (Dridex / BitPaymer) in a tri-lateral action with
> the UK FCDO and Australia DFAT. Named individuals include Eduard
> Benderskiy (former FSB Spetsnaz, the state-nexus enabler), Viktor
> Yakubets, Aleksandr and Sergey Ryzhenkov, Aleksey Shchetinin, Beyat
> Ramazanov, and Vadim Pogodin; entities Vympel-Assistance LLC and Solar-
> Invest LLC. Wayback 20241002115708 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Evil Corp (additional members and facilitators)

> Seven individuals and two entities tied to the Evil Corp cybercrime
> syndicate designated as SDNs in a tri-lateral US/UK/AU action. Coded subset:
> the action targets the named members and facilitators of the syndicate
> rather than an exhaustively enumerated on-chain address set.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-10-01 00:00:00+00:00` → `2024-10-15 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2623>
  - Wayback: <https://web.archive.org/web/20241002115708/https://home.treasury.gov/news/press-releases/jy2623>
  - body_hash: `sha256:acff2559861b6e13bb3fbf6287c8f36d612174bdedac3744c5dc9b7d2c67663a`
  - body_path: `sources/http_captures/evil-corp-ofac-2024-10/primary/web.archive.org__web-20241002120000-https-home.treasury.gov-news-press-releases-jy2623__f5d9c9c476.html`
  > No public CEX policy statement referencing the 2024-10-01 Evil Corp
> tri-lateral designation was published by major exchanges in the
> 14-day post-designation window. Records the absence of public
> disclosure; private chain-analytics KYT flagging is outside this
> observation's scope. The designation names individuals/entities with
> no enumerated on-chain addresses, so the measurable offramp-cascade
> surface is structurally limited.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `0785824`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

