# Evidence chain — `bcbs-cryptoasset-prudential-standard-sco60-2022`

**Status**: `admitted` · **Stratum**: `S6_supranational` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `a331305` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T04:56:33Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The BCBS final cryptoasset prudential standard (d545/SCO60, 2022-12-16)
> imposed a 1250% risk weight and a 1%-of-Tier-1-capital exposure cap on
> Group 2 (unbacked) cryptoassets for internationally-active banks,
> economically constricting the bank/off-ramp surface for the penalised
> asset class; single-layer offramp_cex observed_change with
> attribution=plausible."

## 1. Trigger

- **Type**: `supranational_regulation`
- **Actor**: `bcbs`
- **Timestamp**: `2022-12-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.bis.org/bcbs/publ/d545.pdf>
  - Wayback: <https://web.archive.org/web/20221216235557id_/https://www.bis.org/bcbs/publ/d545.pdf>
  - body_hash: `sha256:9acfcc4667ea2c1eaa4aa10433f9b3bf686ec6dd3ca4c50b182a94d9a0bda09b`
  - body_path: `sources/http_captures/bcbs-cryptoasset-prudential-standard-sco60-2022/primary/web.archive.org__web-20221216235557id_-https-www.bis.org-bcbs-publ-d545.pdf__008d2f6e87.bin`
  > BCBS final standard "Prudential treatment of cryptoasset exposures"
> (d545, consolidated as SCO60), published 2022-12-16. Establishes a
> two-group classification and applies a punitive prudential treatment
> to Group 2 cryptoassets (unbacked cryptoassets and stablecoins with
> ineffective stabilisation mechanisms): a 1250% risk weight and an
> aggregate exposure limit of 1% of a bank's Tier 1 capital. The
> captured PDF contains the strings "1250", "Tier 1", "1%", "Group 2",
> "exposure limit", and "unbacked" (grep-verified). GHOS-endorsed;
> implementation requested by 1 January 2025. Wayback 20221216235557
> pinned (id_ raw-content snapshot).
- **`primary_government`**
  - URL: <https://www.bis.org/press/p221216.htm>
  - Wayback: <https://web.archive.org/web/20260210113309/https://www.bis.org/press/p221216.htm>
  - body_hash: `sha256:fb7a445e01395325401976ed8932c8383e7199694ef9490a47347716c89f8815`
  - body_path: `sources/http_captures/bcbs-cryptoasset-prudential-standard-sco60-2022/primary/web.archive.org__web-20260210113309-https-www.bis.org-press-p221216.htm__fa704df9ff.html`
  > BIS press release (2022-12-16): "Governors and Heads of Supervision
> endorse global bank prudential standard for cryptoassets". Confirms
> the date, actor (Basel Committee / GHOS), the conservative prudential
> treatment of unbacked cryptoassets, and the 1 January 2025
> implementation date. Captured HTML contains "16 December 2022",
> "Basel Committee", "cryptoasset", "unbacked", "1 january 2025",
> "ghos" (grep-verified).

## 2. Target

- **Kind**: `asset`
- **Enumeration**: `complete`
- **Actor name**: BCBS Group 2 cryptoasset prudential treatment (1250% risk weight + 1% Tier 1 cap)

> The prudential restriction targets the class of "Group 2" cryptoassets
> (unbacked cryptoassets and stablecoins with ineffective stabilisation
> mechanisms) held by internationally-active banks. Complete enumeration of
> the prohibited/penalised asset class (the standard defines Group 2 by
> failure of the Group 1 classification conditions); the 1250% risk weight
> and 1%-of-Tier-1 exposure cap apply to all such exposures.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `bcbs_imposes_punitive_capital_treatment_on_group2_cryptoassets`

**Timestamp**: `2022-12-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.bis.org/bcbs/publ/d545.pdf>
  - Wayback: <https://web.archive.org/web/20221216235557id_/https://www.bis.org/bcbs/publ/d545.pdf>
  - body_hash: `sha256:9acfcc4667ea2c1eaa4aa10433f9b3bf686ec6dd3ca4c50b182a94d9a0bda09b`
  - body_path: `sources/http_captures/bcbs-cryptoasset-prudential-standard-sco60-2022/primary/web.archive.org__web-20221216235557id_-https-www.bis.org-bcbs-publ-d545.pdf__008d2f6e87.bin`
  > BCBS d545 (SCO60): 1250% risk weight and 1%-of-Tier-1 exposure cap
> for Group 2 cryptoassets. attribution=plausible: the standard
> mandates the punitive capital framework supranationally, but the
> binding debanking/exposure restriction is operationalised through
> national regulator implementation (requested by 1 Jan 2025), so the
> causal link to a specific access denial is mediated rather than
> self-executing.
- **`primary_government`**
  - URL: <https://www.bis.org/press/p221216.htm>
  - Wayback: <https://web.archive.org/web/20260210113309/https://www.bis.org/press/p221216.htm>
  - body_hash: `sha256:fb7a445e01395325401976ed8932c8383e7199694ef9490a47347716c89f8815`
  - body_path: `sources/http_captures/bcbs-cryptoasset-prudential-standard-sco60-2022/primary/web.archive.org__web-20260210113309-https-www.bis.org-press-p221216.htm__fa704df9ff.html`
  > BIS press release corroborating the GHOS endorsement, the
> conservative treatment of unbacked cryptoassets, and the
> 1 January 2025 implementation date.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a331305`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

