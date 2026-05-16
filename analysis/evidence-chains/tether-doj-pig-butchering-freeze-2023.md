# Evidence chain — `tether-doj-pig-butchering-freeze-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-3` · **Dataset cutoff**: `2026-05-16` · **Source commit**: `bfb1de7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-17T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Tether's 2023-11-20 freeze of $225M USDT linked to a Southeast Asia
> pig-butchering syndicate — executed at DOJ/USSS request without any
> corresponding OFAC SDN listing — documents the DOJ-request-driven mode
> of stablecoin-issuer freeze action. Completes the 3-mode Tether
> compliance spectrum (OFAC-reactive / OFAC-preemptive / DOJ-request-only)
> at S5."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://tether.to/en/tether-freezes-225-million-linked-to-international-human-trafficking-syndicate/>
  - body_hash: `sha256:c37819595db98b24face1d35241c4c62a5fe0dc3fa6606450e17c25c6505c114`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/tether.to__en-tether-freezes-225-million-linked-to-international-human-trafficking-syndicate__ae3e393bc3.html`
  > Tether official blog post (2023-11-20): "Tether Freezes $225 Million
> Linked to International Human Trafficking Syndicate." First publicly
> announced Tether freeze action **explicitly at DOJ request** rather
> than in response to OFAC SDN designation. Coordination partners
> named: U.S. Secret Service (USSS), U.S. Department of Justice DOJ,
> and OKX exchange. Freeze covers wallets linked to "pig butchering"
> romance-scam syndicate in Southeast Asia. **No OFAC SDN listing was
> issued for the target addresses** — this is pure DOJ-request-driven
> freeze, distinct from all prior Tether freeze events in the dataset.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto>
  - body_hash: `sha256:be9f63130d3a946049f43e8cb2d8a2a4bbeb0b21fcff76600646f9a141a7d9f0`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/www.justice.gov__usao-edva-pr-united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto__3f4a45e92b.html`
  > DOJ EDVA civil forfeiture companion filing — parallel DOJ action
> seeking recovery of $112M+ in crypto connected to the same
> pig-butchering scam network. Confirms the DOJ-request framing of
> the Tether freeze: DOJ identifies targets + files civil forfeiture;
> Tether freezes USDT holdings of those targets. Second-anchor
> primary_legal artifact for the freeze's causal chain.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Pig-butchering / romance-scam network
- **Chains**: `ethereum`, `tron`

> Pig-butchering syndicate wallet cluster with ~$225M USDT total frozen.
> Tether blog post does not enumerate individual wallet addresses; the
> DOJ civil-forfeiture complaint references ~$112M+ in identified
> addresses. On-chain targets are therefore subset-enumerable through
> the DOJ civil-forfeiture filings but not complete via primary Tether
> source alone.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `tether_froze_225m_at_doj_request_non_ofac_trigger`

**Timestamp**: `2023-11-20 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://tether.to/en/tether-freezes-225-million-linked-to-international-human-trafficking-syndicate/>
  - body_hash: `sha256:c37819595db98b24face1d35241c4c62a5fe0dc3fa6606450e17c25c6505c114`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/tether.to__en-tether-freezes-225-million-linked-to-international-human-trafficking-syndicate__ae3e393bc3.html`
  > Tether blog explicitly announces the freeze + names USSS, DOJ,
> and OKX as coordination partners. Direct attribution: issuer
> itself is the actor; the action is announced simultaneously with
> execution. First concrete public example in the dataset of Tether
> executing a non-OFAC-driven freeze.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-edva/pr/united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto>
  - body_hash: `sha256:be9f63130d3a946049f43e8cb2d8a2a4bbeb0b21fcff76600646f9a141a7d9f0`
  - body_path: `sources/http_captures/tether-doj-pig-butchering-freeze-2023/primary/www.justice.gov__usao-edva-pr-united-states-files-civil-forfeiture-complaint-seeking-recovery-over-112-million-crypto__3f4a45e92b.html`
  > DOJ EDVA civil-forfeiture filing corroborating the DOJ-driven
> framing. Independent primary_legal artifact.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Tether's $225M USDT freeze across 37-39 wallets is an asset-layer

## 7. Related events

- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)
- [`tether-dprk-precommit-freeze-2025`](./tether-dprk-precommit-freeze-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-3` (commit `bfb1de7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

