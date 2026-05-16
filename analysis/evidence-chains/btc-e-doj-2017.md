# Evidence chain — `btc-e-doj-2017`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-8` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `f18bc7a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-22T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ NDCA indictment of BTC-e / Alexander Vinnik on 2017-07-26 was accompanied
> by a same-day seizure of the canonical btc-e.com domain, documenting the
> earliest L4 frontend seizure in the dataset and establishing the pre-OFAC
> baseline for crypto-exchange enforcement cross-layer cascade shape."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_NDCA`
- **Timestamp**: `2017-07-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  - body_hash: `sha256:510ff33edce09e1fda4ddadc38bf0092933ef779ad9bde0c665419f685651a85`
  - body_path: `sources/http_captures/btc-e-doj-2017/primary/www.justice.gov__archives-opa-pr-russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged__9c617c841b.html`
  > DOJ OPA press release "Russian National and Bitcoin Exchange Charged in 21-Count
> Indictment for Operating Alleged International Money Laundering Scheme and
> Allegedly Laundering Funds From Hack of Mt. Gox" (2017-07-26). BTC-e (Canton
> Business Corporation) 21-count indictment in NDCA, naming Alexander Vinnik as
> principal operator. Historical anchor — **earliest crypto-exchange enforcement
> event in the dataset** (predates OFAC's first crypto-related SDN by 16 months).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BTC-e (Canton Business Corporation)
- **Chains**: `bitcoin`
- **Canonical domains**: `btc-e.com`

> BTC-e entity (Canton Business Corporation) + Alexander Vinnik individual. No
> digital-currency addresses enumerated in the DOJ press release; Mt. Gox
> hack-flow BTC clusters referenced in the 21-count indictment are not attached
> here. Canonical BTC-e domain btc-e.com was seized by DOJ in parallel action.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `canonical_domain_seized_by_DOJ_IRSCI`

**Timestamp**: `2017-07-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  - body_hash: `sha256:510ff33edce09e1fda4ddadc38bf0092933ef779ad9bde0c665419f685651a85`
  - body_path: `sources/http_captures/btc-e-doj-2017/primary/www.justice.gov__archives-opa-pr-russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged__9c617c841b.html`
  > DOJ press release explicitly states domain seizure in coordinated parallel
> action. Primary legal artifact for the observed_change.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-8` (commit `f18bc7a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

