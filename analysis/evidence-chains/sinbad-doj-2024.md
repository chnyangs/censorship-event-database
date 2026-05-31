# Evidence chain — `sinbad-doj-2024`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `2f5abab` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T13:36:54Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2025-01-10 DOJ Office of Public Affairs unsealing of the NDGA
> grand-jury indictment of Roman Vitalyevich Ostapenko, Alexander
> Evgenievich Oleynik, and Anton Vyachlavovich Tarasov for operating the
> Sinbad.io Bitcoin mixer produced a 2-layer comparison-shape cascade in
> the dataset: an l4_frontend finality anchored by the operator
> indictment (atop the prior 2023-11-27 FBI + Netherlands FIOD + Finland
> NBI domain seizure) and an offramp_cex mixer-operator-state transition
> (2 of 3 operators arrested 2024-12-01; Tarasov at large). Distinct from
> sinbad-ofac-2023 (OFAC SDN designation 2023-11-29) and from
> chipmixer-doj-2023 / samourai-doj-2024 in that the enforcement was
> time-split: multi-jurisdictional infrastructure seizure ~13 months
> before the single-jurisdictional US-only operator indictment."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_NDGA`
- **Timestamp**: `2025-01-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering>
  > DOJ Office of Public Affairs press release "Operators of Cryptocurrency
> Mixers Charged with Money Laundering" (2025-01-10). A federal grand
> jury in the Northern District of Georgia (NDGA) returned an indictment
> on 2025-01-07 charging three Russian nationals — Roman Vitalyevich
> Ostapenko (55), Alexander Evgenievich Oleynik (44), and Anton
> Vyachlavovich Tarasov (32) — for their roles operating the
> cryptocurrency mixing services Blender.io and Sinbad.io. Ostapenko
> and Oleynik were arrested 2024-12-01; Tarasov remains at large.
> Counts: conspiracy to commit money laundering (max 20y) +
> operating an unlicensed money transmitting business (max 5y/count).
> The press release also references the prior 2023-11-27 coordinated
> domain seizure of Sinbad.io by FBI + Netherlands FIOD + Finland NBI.
> Investigative agencies named: FBI (lead). DRYRUN wayback stub;
> replace with a verified capture + body_hash / body_path during real
> human audit.
- **`primary_legal`**
  - URL: <https://complianceconcourse.willkie.com/articles/federal-jury-indicts-blender-io-and-sinbad-io-operators-on-money-laundering-charges/>
  - body_hash: `sha256:21b3f14cbdc6c0aa5e0088e06b99656b45317029f790115b8ace789a0bce6f39`
  - body_path: `sources/http_captures/sinbad-doj-2024/v0_3_repair/complianceconcourse.willkie.com__articles-federal-jury-indicts-blender-io-and-sinbad-io-operators-on-money-laundering-charges__ed2df721c1.html`
  > Willkie Compliance Concourse compliance writeup summarizing the
> 2025-01-07 grand-jury indictment and confirming defendant identities
> (Ostapenko / Oleynik / Tarasov) plus NDGA venue. Pinned as
> contextual_unarchived corroboration of the DOJ press release.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `sinbad_io`
- **Actor name**: Sinbad (sinbad.io)
- **Chains**: `bitcoin`
- **Canonical domains**: `sinbad.io`

> Sinbad.io was a Bitcoin mixer marketed as a Tornado Cash successor for
> the Bitcoin chain; per OFAC and DOJ, it served as the "preferred mixing
> service" of the DPRK Lazarus Group and processed proceeds from the 2022
> Harmony Horizon Bridge and Axie Infinity / Ronin Bridge hacks plus
> ransomware funds. The Sinbad service was founded in September 2022 by
> an operator using the alias "Mehdi" (per WIRED 2024 reporting); the
> 2025-01-07 NDGA indictment names three Russian nationals as operators
> — Ostapenko, Oleynik, and Tarasov — without resolving whether the
> "Mehdi" persona maps to any of the three. Target identified by
> canonical domain sinbad.io and the operator-state of the indicted
> natural persons. The indictment does not publish an OFAC-SDN-style
> enumerated address set at the event level; address-set enumeration
> lives on the sibling sinbad-ofac-2023 row (2 BTC addresses).

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `sinbad_frontend_seizure_finality_anchored_by_operator_indictment`

**Timestamp**: `2025-01-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering>
  > DOJ press release explicitly states that on 2023-11-27 "Sinbad.io
> was taken down through law enforcement action" coordinated by the
> FBI, Netherlands FIOD, and Finland NBI, and that the 2025-01-07
> NDGA indictment of Ostapenko / Oleynik / Tarasov follows that
> prior infrastructure seizure. The operator-indictment forecloses
> any near-term restoration of the canonical sinbad.io frontend
> under the indicted operators; attribution=direct because the DOJ
> release is the primary legal instrument naming both the operators
> and the prior domain-seizure operation. DRYRUN wayback stub;
> replace with a verified capture during real human audit.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `sinbad_operator_indicted_two_of_three_arrested`

**Timestamp**: `2025-01-10 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/operators-cryptocurrency-mixers-charged-money-laundering>
  > DOJ release names the indicted Sinbad operators (Roman Vitalyevich
> Ostapenko, Alexander Evgenievich Oleynik, Anton Vyachlavovich
> Tarasov) and confirms Ostapenko + Oleynik were arrested on
> 2024-12-01; Tarasov remains at large. The mixer-operator-state
> transitions from "service seized but operators uncharged" to
> "operators criminally indicted with 2 of 3 arrested" — a
> structural off-ramp / venue-layer transition analogous to
> helix-doj-mixer-2020 (single-jurisdiction post-shutdown
> indictment) and bitzlato-doj-2023 (operator-state takedown).
> attribution=direct via the DOJ primary-legal anchor.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI probe coverage of sinbad.io is effectively absent

## 7. Related events

- [`sinbad-ofac-2023`](./sinbad-ofac-2023.md)
- [`chipmixer-doj-2023`](./chipmixer-doj-2023.md)
- [`helix-doj-mixer-2020`](./helix-doj-mixer-2020.md)
- [`samourai-doj-2024`](./samourai-doj-2024.md)
- [`blender-ofac-2022`](./blender-ofac-2022.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `2f5abab`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

