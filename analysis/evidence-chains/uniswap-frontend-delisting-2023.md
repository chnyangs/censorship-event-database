# Evidence chain — `uniswap-frontend-delisting-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-05-31` · **Source commit**: `c87d162` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-05-31T14:17:25Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Uniswap Labs' 2023-07-21 restriction of more than 100 ERC-20 tokens from
> the app.uniswap.org frontend UI — without corresponding action at the
> Uniswap Protocol (smart-contract) layer — documents a standalone
> L4-only frontend-operator compliance action. Paper-relevant as the
> clearest example of frontend/protocol decoupling in the dataset."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `uniswap_labs`
- **Timestamp**: `2023-07-21 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/>
  - body_hash: `sha256:f894f9c87ad84496a487fca0d0cefed890e99cfdc139ae22de189f6d3405b27c`
  - body_path: `sources/http_captures/uniswap-frontend-delisting-2023/primary/blog.uniswap.org__capture__c164666676.html`
  > Uniswap Labs official blog (blog.uniswap.org) — captured landing page as
> primary anchor for Uniswap Labs corporate actions. On 2023-07-21
> Uniswap Labs announced the token-list restriction on app.uniswap.org
> covering more than 100 tokens (ERC-20 regulatory-categorized tokens
> including XMR-wrapped, privacy-adjacent, and certain SEC-securities-
> flagged tokens). The Uniswap Protocol (smart contracts on-chain)
> remained unaffected — the restriction is exclusively on the
> Uniswap-operated frontend UI.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `uniswap_v2_v3`
- **Actor name**: Uniswap Labs (frontend operator)
- **Chains**: `ethereum`
- **Canonical domains**: `app.uniswap.org`

> More than 100 ERC-20 tokens restricted from display / swap in the
> Uniswap-Labs-hosted frontend (app.uniswap.org). Restrictions target
> various regulatory categories: XMR wrapped tokens, certain
> privacy-coin wraps, tokens with SEC-securities flags, FTX-related
> tokens. Not a complete enumeration — Uniswap publishes internal
> token-list criteria but not the full restricted set publicly.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `uniswap_labs_restricted_100_plus_tokens_from_frontend_ui`

**Timestamp**: `2023-07-21 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://blog.uniswap.org/>
  - body_hash: `sha256:f894f9c87ad84496a487fca0d0cefed890e99cfdc139ae22de189f6d3405b27c`
  - body_path: `sources/http_captures/uniswap-frontend-delisting-2023/primary/blog.uniswap.org__capture__c164666676.html`
  > Uniswap Labs blog is the canonical corporate-statement source. The
> 2023-07 token-list restriction was announced directly by Uniswap
> Labs compliance team, naming the regulatory categories but not the
> full token list. Direct attribution: the frontend operator chose to
> exclude the tokens from its UI for compliance reasons.
- **`semi_primary_measurement`**
  - URL: <https://github.com/Uniswap/token-lists>
  - Wayback: <https://web.archive.org/web/2023/https://github.com/Uniswap/token-lists>
  - body_hash: `sha256:7f74d95b70d4fde33a4aced832dd61be5827b156a6959e9e0a9b35863ddf605a`
  - body_path: `sources/http_captures/uniswap-frontend-delisting-2023/token-lists-local/github.com__Uniswap-token-lists__12917a3e9f.html`
  > Uniswap token-lists repo (github.com/Uniswap/token-lists) — the
> technical substrate for frontend token filtering. Commit history
> around 2023-07 shows the restricted-token list updates. Independent
> semi-primary measurement anchor via the open-source repo.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `c87d162`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

