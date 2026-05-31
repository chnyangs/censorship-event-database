# Evidence chain — `hongkong-sfc-jpex-block-2023`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad93b7f` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `HK_SFC`
- **Timestamp**: `2023-09-13 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.sfc.hk/en/News-and-announcements/Policy-statements-and-announcements/Statement-on-JPEX>
  - Wayback: <https://web.archive.org/web/2023/https://www.sfc.hk/en/News-and-announcements/Policy-statements-and-announcements/Statement-on-JPEX>
  - body_hash: `sha256:3c0150c31eafef4ef94ff92f14dd9967ed62d143757b1a8a06c92aff0e6accd9`
  - body_path: `sources/http_captures/hongkong-sfc-jpex-block-2023/primary/web.archive.org__web-20230925044834-https-www.sfc.hk-en-News-and-announcements-Policy-statements-and-announcements-Statement-on-JPEX__d8abc51659.html`
  > Hong Kong Securities and Futures Commission (SFC) "Statement on
> JPEX" published 2023-09-13. The SFC publicly warned that JPEX
> was operating in Hong Kong without an SFC licence, that its
> claims to be regulated were false, and that the offering of
> high-return VA products contravened the Anti-Money Laundering
> and Counter-Terrorist Financing Ordinance (AMLO). The matter
> was referred to the Hong Kong Police Force for suspected
> fraud. This is the SFC's first public warning under the new
> 2023-06-01 VATP licensing regime.
- **`supporting_journalism`**
  - URL: <https://www.lexology.com/library/detail.aspx?g=2cb94d6d-15c2-4d85-866c-ae0fd5ec207e>
  - Wayback: <https://web.archive.org/web/2023/https://www.lexology.com/library/detail.aspx?g=2cb94d6d-15c2-4d85-866c-ae0fd5ec207e>
  > Lexology client alert "Pitfalls exposed: Unlicensed crypto
> exchange, JPEX, receives first public warning from SFC under
> new HK licensing regime" describing the 2023-09-13 SFC
> statement and the enforcement context.
- **`supporting_journalism`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-arrests-made-in-hong-kong-after-jpex-exchange-warning>
  - Wayback: <https://web.archive.org/web/2023/https://www.elliptic.co/blog/crypto-regulatory-affairs-arrests-made-in-hong-kong-after-jpex-exchange-warning>
  > Elliptic blog summarising the SFC warning and the 2023-09-18
> Hong Kong Police Force arrests under "Operation Iron Gate";
> contextualises HK$1.6B+ in alleged losses and 2,500+ victims
> in the initial reporting window.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: JPEX cryptocurrency exchange
- **Canonical domains**: `jp-ex.io`

> Subset enumeration: JPEX is the named enforcement target of the
> SFC 2023-09-13 public warning and the subsequent HKPF "Operation
> Iron Gate" arrests beginning 2023-09-18. JPEX-related OTC money
> changers, social-media KOLs (e.g. Joseph Lam Chok, Chan Wing),
> and platform members were swept into the same enforcement chain
> but are not exhaustively enumerated here. The full universe of
> unlicensed VATPs marketing to HK is broader; this event records
> the JPEX-specific slice.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `jpex_unlicensed_vatp_public_warning_hk_user_funds_frozen`

**Timestamp**: `2023-09-13 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sfc.hk/en/News-and-announcements/Policy-statements-and-announcements/Statement-on-JPEX>
  - Wayback: <https://web.archive.org/web/20230925044834/https://www.sfc.hk/en/News-and-announcements/Policy-statements-and-announcements/Statement-on-JPEX>
  - body_hash: `sha256:3c0150c31eafef4ef94ff92f14dd9967ed62d143757b1a8a06c92aff0e6accd9`
  - body_path: `sources/http_captures/hongkong-sfc-jpex-block-2023/primary/web.archive.org__web-20230925044834-https-www.sfc.hk-en-News-and-announcements-Policy-statements-and-announcements-Statement-on-JPEX__d8abc51659.html`
  > SFC "Statement on JPEX" 2023-09-13 — the named public
> warning that triggered the offramp-disruption chain.
> Wayback memento 20230925044834.
- **`supporting_journalism`**
  - URL: <https://www.charltonslaw.com/hong-kong-police-arrest-suspects-in-jpex-scandal/>
  - Wayback: <https://web.archive.org/web/2023/https://www.charltonslaw.com/hong-kong-police-arrest-suspects-in-jpex-scandal/>
  > Charltons Law summary "Hong Kong Police Arrest Suspects in
> JPEX Scandal" — documents the 2023-09-18 HKPF arrests
> under "Operation Iron Gate" and the HK$1.6B+ loss figure
> across 2,500+ victims.
- **`supporting_journalism`**
  - URL: <https://cointelegraph.com/news/hong-kong-regulator-sfc-crackdown-unregulated-crypto-platforms-jpex-scandal>
  - Wayback: <https://web.archive.org/web/2023/https://cointelegraph.com/news/hong-kong-regulator-sfc-crackdown-unregulated-crypto-platforms-jpex-scandal>
  > Cointelegraph reporting on HK's post-JPEX "suspicious VATP"
> list — documents the SFC's accelerated post-JPEX
> enforcement posture under the VATP licensing regime.

## 4. No-change observations (where applicable)

### l4_frontend — `jpex_hk_user_access_restrictions_post_sfc_warning`

**Window**: `2023-09-13 00:00:00+00:00` → `2023-09-20 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.sfc.hk/en/News-and-announcements/Policy-statements-and-announcements/Statement-on-JPEX>
  - Wayback: <https://web.archive.org/web/20230925044834/https://www.sfc.hk/en/News-and-announcements/Policy-statements-and-announcements/Statement-on-JPEX>
  - body_hash: `sha256:3c0150c31eafef4ef94ff92f14dd9967ed62d143757b1a8a06c92aff0e6accd9`
  - body_path: `sources/http_captures/hongkong-sfc-jpex-block-2023/primary/web.archive.org__web-20230925044834-https-www.sfc.hk-en-News-and-announcements-Policy-statements-and-announcements-Statement-on-JPEX__d8abc51659.html`
  > SFC Statement on JPEX anchors the frontend-side user-access
> restriction window (replayable). No HK-vantage jp-ex.io
> Wayback snapshot was independently pinned, so this layer is
> recorded as observed_no_change rather than observed_change.
- **`semi_primary_wayback`**
  - URL: <https://www.elliptic.co/blog/crypto-regulatory-affairs-arrests-made-in-hong-kong-after-jpex-exchange-warning>
  - Wayback: <https://web.archive.org/web/20231210072706/https://www.elliptic.co/blog/crypto-regulatory-affairs-arrests-made-in-hong-kong-after-jpex-exchange-warning>
  - body_hash: `sha256:389839a96f1a73fae6de67661e8c3510cf06bc7a780e57dcde6cecb4edb376d1`
  - body_path: `sources/http_captures/hongkong-sfc-jpex-block-2023/primary/web.archive.org__web-20231210072706-https-www.elliptic.co-blog-crypto-regulatory-affairs-arrests-made-in-hong-kong-after-jpex-exchange-warning__2983f036c2.html`
  > Elliptic blog documenting JPEX raising withdrawal fees to
> 999 USDT and HK user withdrawal halt in the days after
> the SFC warning.
- **`supporting_journalism`**
  - URL: <https://cryptodaily.co.uk/2023/09/hong-kong-sfc-opens-probe-into-jpex-exchange-one-arrested>
  - Wayback: <https://web.archive.org/web/2023/https://cryptodaily.co.uk/2023/09/hong-kong-sfc-opens-probe-into-jpex-exchange-one-arrested>
  > Crypto Daily 2023-09 reporting on the SFC probe and the
> frontend-side user-access restrictions JPEX imposed in
> the same window.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`hongkong-sfc-vatp-licensing-2023-06`](./hongkong-sfc-vatp-licensing-2023-06.md)
- [`hongkong-hkma-stablecoins-ordinance-2025`](./hongkong-hkma-stablecoins-ordinance-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad93b7f`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

