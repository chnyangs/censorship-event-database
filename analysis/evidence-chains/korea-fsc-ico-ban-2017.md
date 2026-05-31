# Evidence chain — `korea-fsc-ico-ban-2017`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `9fed8c7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> The KR FSC 2017-09-29 joint statement imposed a full ban on all forms
> of ICOs and prohibited margin/lending crypto products at regulated
> Korean financial institutions, with the regulated Korean
> crypto-exchange sector (Upbit, Bithumb, Coinone, Korbit) complying
> across Q4-2017 / Q1-2018. The offramp_cex layer carries the
> load-bearing direct-attribution observation; L4 frontend reactions
> are consistent with the cascade but require a Wayback-capture pass
> before they may anchor a separate observed_change row.

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KR_FSC`
- **Timestamp**: `2017-09-29 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/new_press>
  - Wayback: <https://web.archive.org/web/2017/https://www.fsc.go.kr/eng/new_press>
  > South Korea Financial Services Commission (FSC) press release index
> (English site) — announcing a full ban on all forms of Initial Coin
> Offerings (ICOs) and prohibition on margin trading in crypto-assets,
> issued 2017-09-29. The FSC statement followed a joint Financial-
> Stability-Coordination meeting of the FSC, the Ministry of Strategy
> and Finance, the Bank of Korea, the National Tax Service, and the
> Korea Financial Intelligence Unit (KFIU), making Korea the second
> major Asian jurisdiction (after China's PBOC 2017-09-04 notice) to
> impose a blanket ICO ban in 2017. Core provisions: (1) ban on all
> token-issuance fundraising regardless of technical structure,
> (2) prohibition on lending and margin trading of virtual assets at
> regulated financial institutions, (3) directive to enforcement
> agencies to investigate manipulative trading and unlawful fund
> flows. The fsc.go.kr URL path format has drifted since 2017; the
> provisional Wayback anchor uses year-prefix lookup and the specific
> capture timestamp requires re-pinning during human audit before
> this citation may serve as an admission anchor in its own right.
> Marked evidence_use=contextual_unarchived pending that re-pin.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: KR ICO + crypto-margin sector (class)

> Canonical target is the KR FSC policy directive itself, addressed to
> (a) Korean crypto token issuers and ICO promoters (full ban on
> token-issuance fundraising), and (b) Korean financial institutions
> offering margin/lending products for crypto-assets (prohibition).
> Affected named exchanges in the 2017-Q4 window include Upbit, Bithumb,
> Coinone, and Korbit; these are recorded as implicit second-order
> targets in observation scope rather than enumerated in
> canonical_domains, matching the sibling china-pboc-crypto-ban-2013-12
> and china-pboc-crypto-ban-2021 convention.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `ico_fundraising_and_crypto_margin_prohibited_sector_wide`

**Timestamp**: `2017-09-29 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/new_press>
  - Wayback: <https://web.archive.org/web/2017/https://www.fsc.go.kr/eng/new_press>
  > KR FSC is the primary legal actor. Effective 2017-09-29; the
> statement bans all forms of ICOs regardless of technical
> structure and prohibits margin/lending crypto products at
> regulated Korean financial institutions. Direct attribution:
> the FSC statement itself mandates the behavior across the
> regulated Korean crypto-exchange sector (Upbit, Bithumb,
> Coinone, Korbit). The follow-on 2018-01-30 real-name banking
> mandate (KFIU 2018) operationalized the order at the
> bank-account-rail layer. Provisional wayback anchor uses
> year-prefix lookup; specific snapshot timestamp requires
> re-pinning during human audit.
- **`primary_legal`**
  - URL: <https://www.fsc.go.kr/eng/new_press>
  - Wayback: <https://web.archive.org/web/2017/https://www.fsc.go.kr/eng/new_press>
  > Second anchor to the same FSC English-site press index, marking
> the joint Financial-Stability-Coordination meeting
> (FSC + MOSF + BOK + NTS + KFIU) origin of the 2017-09-29
> announcement. The 2018-01-30 KFIU real-name banking mandate
> is the immediate downstream operational rule and is treated
> here as a coda within the same regulatory action rather than
> as a separate event.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Korean crypto exchange frontends (Upbit, Bithumb, Coinone, Korbit)

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`korea-travel-rule-2022`](./korea-travel-rule-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `9fed8c7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

