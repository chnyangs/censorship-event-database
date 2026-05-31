# Evidence chain — `ofac-zhdanova-russian-elite-launderer-2023-11`

**Status**: `admitted` · **Stratum**: `S1_ofac_sdn` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `8583894` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-20` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OFAC designation of Ekaterina Zhdanova on 2023-11-03 — the first OFAC
> action targeting a virtual-currency-specialized concierge-laundering
> operator (rather than an exchange or anonymizer) — produced
> plausible-attribution cascade at the asset_onchain (chain-analytics
> tagging) and offramp_cex (KYT flagging at counterparty mainstream CEXes
> and at Garantex) layers; L0/L1/L3/L4 layers are structurally
> not_applicable for an individual-level designation with no canonical
> service frontend."

## 1. Trigger

- **Type**: `ofac_sdn_designation`
- **Actor**: `US_OFAC`
- **Timestamp**: `2023-11-03 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20231103>
  - Wayback: <https://web.archive.org/web/20231103212642/https://ofac.treasury.gov/recent-actions/20231103>
  - body_hash: `sha256:e17401b8bdfc3e9a4914629a4e2f4a8ed349555fceea4fa342d72a17bc8b2864`
  - body_path: `sources/http_captures/ofac-zhdanova-russian-elite-launderer-2023-11/primary/web.archive.org__web-20231103212642-https-ofac.treasury.gov-recent-actions-20231103__c454ed49f5.html`
  > OFAC Recent Actions page for 2023-11-03 ("Russia-related
> Designation"). Designation of Ekaterina ZHDANOVA (Russia-based
> individual) pursuant to Executive Order 14024. v0.3 audit
> 2026-05-20 (c) Batch C-1: Wayback memento 20231103212642 pinned
> (86278 bytes). Direct grep extracts 3 XBT addresses verbatim
> from SDN entry: 1Ljk8RNNabkZ9bfDYQBn98XfFozJhTjqcZ +
> 3685sEusmTwZBiKJ4cgV73EAhpVD1nbgbe +
> 39p8qWp1bkBNhi4vPpFTetKPtH7goqNDZf. Press release link reference:
> jy1874.
- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1874>
  - Wayback: <https://web.archive.org/web/20231103173627/https://home.treasury.gov/news/press-releases/jy1874>
  - body_hash: `sha256:77087a5e9ea09380a384cbc818d6fe470ef6f22c78dec51557056929e9318469`
  - body_path: `sources/http_captures/ofac-zhdanova-russian-elite-launderer-2023-11/primary/web.archive.org__web-20231103173627-https-home.treasury.gov-news-press-releases-jy1874__6813045f32.html`
  > Treasury press release jy1874 "Treasury Designates Virtual
> Currency Money Launderer for Russian Elites and Cybercriminals"
> (2023-11-03). Frames Zhdanova as the first OFAC action targeting
> a virtual-currency-specialized "concierge laundering" operator
> distinct from an exchange (SUEX 2021, Garantex 2022) or
> anonymizer/mixer (Blender 2022, Tornado 2022, Sinbad 2023).
> v0.3 audit 2026-05-20 (c) Batch C-1 CORRECTION: original draft
> cited jy2735 (which is actually a 2024-12-04 different action
> titled "Treasury Exposes Money Laundering Network Using Digital
> Assets to Evade Sanctions"); correct jy ID for the 2023-11-03
> Zhdanova action is jy1874, confirmed via OFAC RA HTML reference
> + Wayback memento on event day. Wayback memento 20231103173627
> pinned (169412 bytes), grep verifies 34xZhdanova + 14xjy1874 +
> 22xvirtual currency variants + 8xRyuk + 8xGarantex + 6xEkaterina
> + 4xNovember 3 + 4x2023-11-03 + 4x"2.3 million".
- **`supporting_journalism`**
  - URL: <https://www.chainalysis.com/blog/ofac-russia-crypto-money-laundering-sanctions-2023/>
  - Wayback: <https://web.archive.org/web/20231104195138/https://www.chainalysis.com/blog/ofac-russia-crypto-money-laundering-sanctions-2023/>
  - body_hash: `sha256:0a04f9797f9ef58319a2d4b12c570c2737fe56575c81a8c603a611f2429fc9b8`
  - body_path: `sources/http_captures/ofac-zhdanova-russian-elite-launderer-2023-11/primary/web.archive.org__web-20231104195138-https-www.chainalysis.com-blog-ofac-russia-crypto-money-laundering-sanctions-2023__83a0c390ae.html`
  > Chainalysis post-action analysis (2023-11-04) of the Zhdanova
> designation. v0.3 audit 2026-05-20: Wayback memento pinned
> (53346 bytes, day-after capture).
- **`supporting_journalism`**
  - URL: <https://www.elliptic.co/blog/ofac-sanctions-russian-national-for-facilitating-sanctions-evasion>
  - Wayback: <https://web.archive.org/web/20231211232112/https://www.elliptic.co/blog/ofac-sanctions-russian-national-for-facilitating-sanctions-evasion>
  - body_hash: `sha256:6ebff5c0c514d2e79519113a3b15eb7dd0928db5e101a9fbddc38f471447caf7`
  - body_path: `sources/http_captures/ofac-zhdanova-russian-elite-launderer-2023-11/primary/web.archive.org__web-20231211232112-https-www.elliptic.co-blog-ofac-sanctions-russian-national-for-facilitating-sanctions-evasion__10c3693ea4.html`
  > Elliptic post-action analysis of the Zhdanova designation.
> v0.3 audit 2026-05-20: Wayback memento 20231211232112 pinned
> (16116 bytes).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `complete`
- **Actor name**: Ekaterina Zhdanova
- **Chains**: `bitcoin`
- **Addresses**: 3 total (enumerated in event YAML)

> Individual designation of Ekaterina Zhdanova, a Russia-based natural
> person operating as a virtual-currency-specialized "concierge laundering"
> operator for Russian elites and ransomware affiliates (including Ryuk).
> v0.3 audit 2026-05-20 (c) Batch C-1: enumeration upgraded subset->complete,
> 3 XBT addresses extracted verbatim from OFAC RA 20231103 Wayback memento.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_for_individual_zhdanova_in_14d_window`

**Window**: `2023-11-03 00:00:00+00:00` → `2023-11-17 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://home.treasury.gov/news/press-releases/jy1874>
  - Wayback: <https://web.archive.org/web/20231103173627/https://home.treasury.gov/news/press-releases/jy1874>
  - body_hash: `sha256:77087a5e9ea09380a384cbc818d6fe470ef6f22c78dec51557056929e9318469`
  - body_path: `sources/http_captures/ofac-zhdanova-russian-elite-launderer-2023-11/primary/web.archive.org__web-20231103173627-https-home.treasury.gov-news-press-releases-jy1874__6813045f32.html`
  > v0.3 audit 2026-05-20: observation row recast from original
> draft's observed_change plausible (KYT flagging at counterparty
> CEXes) to observed_no_change attribution=none. Treasury jy1874
> narrates Zhdanova's counterparty exposure to mainstream CEXes
> + Garantex but absence of fresh public CEX policy statement in
> 14d post-event window is the expected null finding (matches
> sim-hyon-sop / hamas-gaza-now / al-Jamal / trickbot pattern
> for individual-target OFAC SDN). Generic KYT-flagging IS the
> standard post-SDN cascade primitive but is private/non-public
> per industry practice — not an observable per-event cascade.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`matveev-ofac-2023`](./matveev-ofac-2023.md)
- [`suex-ofac-2021`](./suex-ofac-2021.md)
- [`garantex-ofac-2022`](./garantex-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8583894`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

