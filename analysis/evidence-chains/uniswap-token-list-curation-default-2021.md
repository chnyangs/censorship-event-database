# Evidence chain — `uniswap-token-list-curation-default-2021`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `85e7d01` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Uniswap Labs' default token list curation policy — formalized
> 2021-07-23 alongside the synthetic-stocks delisting batch and
> after the 2021-04 Wells-notice-era regulatory-pressure cycle —
> establishes that the US-based frontend operator (Uniswap Labs)
> holds discretionary curation power over which ERC-20 tokens
> are surfaced on app.uniswap.org, separate from the autonomous
> on-chain Uniswap Protocol smart contracts. This framework row
> carries no row-local observed_change (the per-token cascade
> observations are coded on the sibling events
> uniswap-tokenized-stocks-delisting-2021-07 and
> uniswap-frontend-delisting-2023); it functions as a
> policy-scoping anchor for the Uniswap-Labs frontend-curation
> arc and as denominator control in S5 corporate-frontend
> analyses."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `uniswap_labs`
- **Timestamp**: `2021-07-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://app.uniswap.org>
  - Wayback: <https://web.archive.org/web/2021/https://app.uniswap.org>
  > Uniswap Labs operates app.uniswap.org and ships the default
> token-list catalogue that the frontend renders. The 2021
> default-token-list curation policy — formalized 2021-07-23
> alongside the synthetic-stocks delisting batch and after the
> 2021-04 Wells-notice-era regulatory-pressure cycle — establishes
> that Uniswap Labs (the US-based frontend operator) is the
> discretionary curator of which ERC-20 tokens are surfaced on
> app.uniswap.org. The on-chain Uniswap Protocol smart contracts
> (v2 / v3) remain autonomous and permissionless; the curation
> policy applies exclusively to the Uniswap-Labs-operated
> frontend UI. This row codes the **policy framework itself**
> (the discretionary curation power), not any specific per-token
> cascade — the load-bearing per-token observation for the
> 2021-07-23 cohort is the sibling event
> uniswap-tokenized-stocks-delisting-2021-07. Marked
> evidence_use=contextual_unarchived because in this DRYRUN the
> authoring LLM agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash of the policy-framework
> announcement copy; the Uniswap-Labs domain is the canonical
> corporate anchor but the precise policy / token-list curation
> page must be re-anchored during human audit before this
> citation may serve as an admission anchor.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `uniswap_v2_v3`
- **Actor name**: Uniswap Labs (frontend operator, app.uniswap.org)
- **Chains**: `ethereum`
- **Canonical domains**: `app.uniswap.org`

> The target of this row is the **policy framework** — the
> Uniswap-Labs-operated default token list at app.uniswap.org and
> the discretionary curation power that Uniswap Labs (the US-based
> frontend operator) exercises over which ERC-20 tokens are
> surfaced in the UI. enumeration=subset because the framework
> governs an open-ended ongoing class of tokens (any ERC-20 that
> Uniswap Labs's compliance review chooses to admit or exclude),
> not a closed finite enumerated set. The 2021-07-23 cohort of
> approximately 100 tokenized-equity / option / synthetic-equity
> tokens that triggered the formal articulation of this curation
> policy is enumerated separately in the sibling event
> uniswap-tokenized-stocks-delisting-2021-07. The 2023-07-21
> broader regulatory-category cohort is enumerated in the sibling
> event uniswap-frontend-delisting-2023. Target is the Uniswap
> Labs frontend operator (the entity that controls app.uniswap.org
> and the @uniswap/default-token-list repo), not the Uniswap
> Protocol smart contracts and not any specific listed token.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### l4_frontend — `default_token_list_policy_framework_articulated_without_row_local_per_token_cascade`

**Window**: `2021-07-23 00:00:00+00:00` → `2021-12-31 23:59:59+00:00`

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/token-access-app?rel=outbound>
  - body_hash: `sha256:271f576eac76deb87ad97a73936e276e5556d9845696ce89c08c8cfa54d1a14a`
  - body_path: `sources/http_captures/uniswap-token-list-curation-default-2021/v0_3_primary_repair/blog.uniswap.org__token-access-app__f02db91ba6.html`
  > Uniswap Labs' own "Token Access on app.uniswap.org" post is the
> primary corporate source for the policy framework. This row's
> observation is deliberately a coverage gap: the post anchors the
> frontend curation framework, while the per-token delisting cascade
> is recorded in the sibling tokenized-stocks event to avoid
> double-counting the same physical UI action.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`uniswap-tokenized-stocks-delisting-2021-07`](./uniswap-tokenized-stocks-delisting-2021-07.md)
- [`uniswap-frontend-delisting-2023`](./uniswap-frontend-delisting-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `85e7d01`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

