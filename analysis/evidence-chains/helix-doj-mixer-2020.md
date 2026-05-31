# Evidence chain — `helix-doj-mixer-2020`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (2 changed layer(s): `l4_frontend`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `00764cd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-16` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2020-02-11 DOJ DDC indictment of Larry Dean Harmon for operating the
> Helix Bitcoin mixer (2014-2017, $300M+ laundered) produced a 2-layer
> comparison-shape cascade in the dataset: an l4_frontend finality on the
> already-self-shuttered helix .onion service and an offramp_cex mixer-
> operator-state transition anchored by the indictment + parallel 2020-10-19
> FinCEN $60M civil money penalty. Distinct from chipmixer-doj-2023 and
> samourai-doj-2024 in that the mixer was already dark at indictment time
> and the enforcement was single-jurisdiction (US-only)."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_DC`
- **Timestamp**: `2020-02-11 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million>
  > DOJ Office of Public Affairs press release announcing the 2020-02-11
> indictment (unsealed 2020-02-13) of Larry Dean Harmon, of Akron, Ohio,
> for operating Helix, a darknet-based Bitcoin mixer that laundered over
> $300M in BTC between 2014 and 2017. Charges: conspiracy to launder
> monetary instruments, operating an unlicensed money transmitting
> business, and conducting money transmission without a DC license.
> Filed in the US District Court for the District of Columbia (DDC).
> IRS-CI and FBI Cyber Division co-investigators; FinCEN parallel CMP
> action against Harmon announced 2020-10-19 ($60M assessment).
> Helix infrastructure had already gone dark in late 2017 prior to this
> operator-state indictment.
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-announces-60-million-civil-money-penalty-against-larry-dean-harmon>
  > Companion FinCEN $60M civil-money-penalty announcement (2020-10-19)
> against Harmon for BSA / money-transmitter-registration violations
> operating Helix and Coin Ninja. Pinned for context; not retained as
> an admission anchor in this DRYRUN row.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `helix_mixer`
- **Actor name**: Helix / Coin Ninja (operated by Larry Dean Harmon)
- **Chains**: `bitcoin`
- **Canonical domains**: `grams7enufi7jmdl.onion`, `helix.grams7enufi7jmdl.onion`

> Larry Dean Harmon as named operator + the Helix Bitcoin mixer service
> (and the affiliated Coin Ninja / Grams search infrastructure). Helix
> operated 2014-2017 and was already taken offline before this 2020
> indictment of the operator. No SDN-style enumerated address set is
> attached at this event level; the indictment names specific BTC
> counterparty flows but does not publish a discrete watchlist of mixer
> addresses in the OFAC SDN style.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `helix_mixer_frontend_finality_anchored_by_operator_indictment`

**Timestamp**: `2020-02-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million>
  > DOJ press release explicitly names Harmon as the sole operator of
> Helix and confirms the service's 2014-2017 operating window. The
> indictment of the operator post-self-shutdown converts the
> frontend's terminal state into a juridically-anchored finality:
> there is no operator who can restore the .onion service after this
> arrest. attribution=direct because the DOJ release is the primary
> legal instrument naming both the operator and the service.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `helix_operator_indicted_and_arrested_mixer_state_terminal`

**Timestamp**: `2020-02-11 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.justice.gov/opa/pr/ohio-resident-charged-operating-darknet-based-bitcoin-mixer-laundered-over-300-million>
  > DOJ describes Helix's $300M+ BTC laundering operating window
> (2014-2017) and indicts Harmon as the operator. The mixer-operator
> state transitions from "shut down by operator / latent" to
> "criminally indicted with operator under arrest" — a structural
> off-ramp / venue-layer transition analogous to bitzlato-doj-2023
> but with the mixer already self-dark. attribution=direct via the
> DOJ primary-legal anchor.
- **`primary_legal`**
  - URL: <https://www.fincen.gov/news/news-releases/fincen-announces-60-million-civil-money-penalty-against-larry-dean-harmon>
  - Wayback: <https://web.archive.org/web/20260516000000/https://www.fincen.gov/news/news-releases/fincen-announces-60-million-civil-money-penalty-against-larry-dean-harmon>
  > Companion FinCEN $60M civil money penalty (2020-10-19) for BSA /
> money-transmitter-registration violations. Pinned as contextual
> corroboration of the same operator-state transition. DRYRUN
> wayback stub; replace with a verified capture + body_hash /
> body_path artifact during real human audit.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`chipmixer-doj-2023`](./chipmixer-doj-2023.md)
- [`samourai-doj-2024`](./samourai-doj-2024.md)
- [`hydra-doj-2022`](./hydra-doj-2022.md)
- [`bitzlato-doj-2023`](./bitzlato-doj-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `00764cd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

