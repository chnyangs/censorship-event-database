# Evidence chain — `netex24-bitpapa-russia-crypto-ofac-2024-03`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9e851fb` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC's 2024-03-25 SDN designation (jy2204) of Russia-nexus virtual-currency
> exchanges Netex24 and Bitpapa, within a 15-target Russia virtual-asset-
> services action, restricted U.S.-person dealings with both crypto exchanges.
> No public CEX cascade was documented in the 14-day window. null_case:
> exchange-operator target with limited measurable cross-layer surface at draft
> time."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2024-03-25 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2204>
  - Wayback: <https://web.archive.org/web/20240325164058/https://home.treasury.gov/news/press-releases/jy2204>
  - body_hash: `sha256:7eb432311ad1e3f87cc1ebc0f9ce2037a547c4bee1e97c968971ddc6caf657d0`
  - body_path: `sources/http_captures/netex24-bitpapa-russia-crypto-ofac-2024-03/primary/web.archive.org__web-20240325000000-https-home.treasury.gov-news-press-releases-jy2204__8802ae93d9.html`
  > Treasury press release jy2204 (2024-03-25) "Treasury Designates Russian
> Companies Supporting Sanctions Evasion Through Virtual Asset Services
> and Technology Procurement". OFAC designated 13 entities + 2 individuals
> under EO 14024, including Moscow-based virtual-currency exchange operator
> TOEP (business names Netexchange / Netex24) and Bitpapa IC FZC LLC
> (Bitpapa) — both crypto exchanges that processed transactions for
> OFAC-designated Russian entities (Sberbank, Alfa-Bank, Hydra Market,
> Garantex). Wayback 20240325164058 pinned; grep verifies 6xBitpapa,
> 2xNetex24, 5x"March 25, 2024".
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20240325>
  - Wayback: <https://web.archive.org/web/20240325174522/https://ofac.treasury.gov/recent-actions/20240325>
  - body_hash: `sha256:e9df0faca4d5419d5d3dfa52b33165a6ddce79e76bc37cfd62ecd7c360f001db`
  - body_path: `sources/http_captures/netex24-bitpapa-russia-crypto-ofac-2024-03/primary/web.archive.org__web-20240325000000-https-ofac.treasury.gov-recent-actions-20240325__95986fab84.html`
  > OFAC Recent Actions page for 2024-03-25, the formal SDN-list publication
> accompanying jy2204 (Netex24 / Bitpapa and the broader Russia
> virtual-asset-services cluster). Independent primary anchor for the
> designation.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Netex24 (TOEP) + Bitpapa IC FZC LLC
- **Canonical domains**: `netex24.net`, `bitpapa.com`

> Russia-nexus virtual-currency exchanges Netex24 (TOEP / Netexchange) and
> Bitpapa IC FZC LLC, the load-bearing crypto-platform targets within the
> 13-entity + 2-individual jy2204 action. Subset enumeration: the full set of
> fintech/technology-procurement co-designees on the same action is out of
> this event's target scope.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_14d_window`

**Window**: `2024-03-25 00:00:00+00:00` → `2024-04-08 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy2204>
  - Wayback: <https://web.archive.org/web/20240325164058/https://home.treasury.gov/news/press-releases/jy2204>
  - body_hash: `sha256:7eb432311ad1e3f87cc1ebc0f9ce2037a547c4bee1e97c968971ddc6caf657d0`
  - body_path: `sources/http_captures/netex24-bitpapa-russia-crypto-ofac-2024-03/primary/web.archive.org__web-20240325000000-https-home.treasury.gov-news-press-releases-jy2204__8802ae93d9.html`
  > No public CEX policy statement explicitly naming the Netex24 / Bitpapa
> SDN entries was published by major exchanges in the 14-day
> post-designation window. Records absence of public disclosure; private
> chain-analytics KYT flagging is outside this observation's scope.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): No OONI / Censored Planet probe of netex24.net or bitpapa.com within the
- **l4_frontend** (`not_measured`): netex24.net / bitpapa.com are the exchanges' canonical domains; Wayback

## 7. Related events

- [`garantex-ofac-2022`](./garantex-ofac-2022.md)
- [`hydra-ofac-2022`](./hydra-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9e851fb`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

