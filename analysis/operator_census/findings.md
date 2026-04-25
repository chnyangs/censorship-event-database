# Operator-compliance git-history census

Generated: `2026-04-25T05:03:38Z` · scanner `scripts/scan_operator_census.py` · candidates `sources/operator_census/candidates.yaml`.

Reproduction: `python3 scripts/scan_operator_census.py` (requires network for initial clone; subsequent runs reuse local clones under `sources/operator_census/<org>__<repo>/`).

## Summary

Columns: *OFAC-rxn* = commits whose **subject** carries a state-action keyword (ofac / sdn / sanction / designate). Path is not consulted — earlier versions matched the path and inflated counts on `server/ofacblacklist.go` for every commit including pure refactors and Docker updates. *OFAC-maint* = OFAC-rxn plus a cleanup verb. The 2025-04-01 Flashbots PR #173 ("Cleanup unused and unmaintained blacklist file") falls in *Generic-list*, not OFAC-maint, because its subject names "blacklist" but no OFAC keyword; the editorial interpretation that this commit is the post-OFAC-delisting cleanup is documented in `analysis/evidence-chains/tornado-cash-ofac-delisting-2025.md`, not in this automated classifier. *Entity-hit* = commits that name a designated entity (tornado / samourai / lazarus / ...) without state-action language; requires human adjudication because phishing registries produce prefix false positives (e.g. "stormtoken.com" in 2017 long pre-dates the Storm/Semenov OFAC designation). *Generic-list* = blacklist/blocklist/denylist activity with no OFAC or entity tie (dominates phishing-scam registries). First/last-OFAC bounds the OFAC-keyed window.

Path discovery scans both the current checkout and historical `git log --all --name-only` output, so deleted or renamed files matching the configured patterns are included in the candidate path set.

| operator | repo | role | clone | files | commits | OFAC-rxn | OFAC-maint | Entity-hit | Generic-list | first-OFAC | last-OFAC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| flashbots | `flashbots/rpc-endpoint` | public_rpc_endpoint | ok | 1 | 5 | 1 | 0 | 0 | 1 | 2022-08-08 | 2022-08-08 |
| flashbots | `flashbots/mev-boost-relay` | mev_boost_relay | ok | 0 | 0 | 0 | 0 | 0 | 0 | — | — |
| flashbots | `flashbots/rbuilder` | block_builder | ok | 0 | 0 | 0 | 0 | 0 | 0 | — | — |
| flashbots | `flashbots/builder` | block_builder_deprecated | ok | 1 | 2 | 0 | 0 | 0 | 1 | — | — |
| metamask | `MetaMask/eth-phishing-detect` | wallet_blocklist | ok | 1 | 204341 | 0 | 0 | 8 | 1450 | — | — |
| trust_wallet | `trustwallet/assets` | wallet_token_index | ok | 27 | 372 | 0 | 0 | 0 | 32 | — | — |
| uniswap | `Uniswap/token-lists` | frontend_token_list_schema | ok | 3 | 74 | 0 | 0 | 0 | 0 | — | — |
| community | `ethereum-lists/tokens` | community_token_registry | ok | 0 | 0 | 0 | 0 | 0 | 0 | — | — |

## Per-repo detail

### `flashbots/rpc-endpoint` — public_rpc_endpoint

- **Operator**: flashbots
- **Clone status**: ok
- **Matched files** (n=1):
    - `server/ofacblacklist.go`

**Notes**: Baseline case. Added Tornado pool addresses 2h 50m after 2022-08-08 SDN (PR #90, commit 92ab6b1f). Deleted entire 132-address map 11 days after 2025-03-21 OFAC delisting (PR #173, commit 1e9c29c). See analysis/evidence-chains/tornado-cash-ofac-{2022,delisting-2025}.md.

**OFAC-keyed commits** (reactions=1, maintenance=0):

| date | sha | path | class | subject |
| --- | --- | --- | --- | --- |
| 2022-08-08 | `92ab6b1f` | `server/ofacblacklist.go` | sanctions_reaction | update ofac black list (#90) |

_Generic list-maintenance commits (phishing / abuse / scam registry activity, no OFAC keyword): 1. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `flashbots/mev-boost-relay` — mev_boost_relay

- **Operator**: flashbots
- **Clone status**: ok
- **Matched files** (n=0):

**Notes**: MEV-Boost relay reference implementation. Compliance status of the Flashbots-operated relay was a contested 2022-2023 topic (post-OFAC sanctions; "Flashbots Protect" vs "Flashbots Protect++"). Census asks whether the relay software itself ships with a filter substrate.

### `flashbots/rbuilder` — block_builder

- **Operator**: flashbots
- **Clone status**: ok
- **Matched files** (n=0):

**Notes**: Successor to flashbots/builder. A builder, not a relay — if this ships a compliance filter, it is a stronger finding than the relay layer.

### `flashbots/builder` — block_builder_deprecated

- **Operator**: flashbots
- **Clone status**: ok
- **Matched files** (n=1):
    - `ofac_blacklist.json`

**Notes**: Deprecated predecessor to rbuilder. History matters because the 2022-2023 compliance debate happened here.

_Generic list-maintenance commits (phishing / abuse / scam registry activity, no OFAC keyword): 1. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `MetaMask/eth-phishing-detect` — wallet_blocklist

- **Operator**: metamask
- **Clone status**: ok
- **Matched files** (n=1):
    - `src/config.json`

**Notes**: Consensys-operated phishing blocklist consumed by the MetaMask extension. Not OFAC-keyed; tracks phishing domains and token scams. Included as a control — if filter-list maintenance timing looks similar to Flashbots' OFAC pattern, that strengthens the "public operator git-history as measurement substrate" framing even when the trigger is not OFAC.

_Generic list-maintenance commits (phishing / abuse / scam registry activity, no OFAC keyword): 1450. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `trustwallet/assets` — wallet_token_index

- **Operator**: trust_wallet
- **Clone status**: ok
- **Matched files** (n=27):
    - `blockchains/arbitrum/denylist.json`
    - `blockchains/avalanchec/denylist.json`
    - `blockchains/binance/denylist.json`
    - `blockchains/callisto/denylist.json`
    - `blockchains/classic/denylist.json`
    - `blockchains/eos/denylist.json`
    - `blockchains/ethereum/denylist.json`
    - `blockchains/fantom/denylist.json`
    - `blockchains/gochain/denylist.json`
    - `blockchains/heco/denylist.json`
    - `blockchains/neo/denylist.json`
    - `blockchains/nuls/denylist.json`
    - `blockchains/ontology/denylist.json`
    - `blockchains/optimism/denylist.json`
    - `blockchains/poa/denylist.json`
    - `blockchains/polygon/denylist.json`
    - `blockchains/smartchain/denylist.json`
    - `blockchains/solana/denylist.json`
    - `blockchains/terra/denylist.json`
    - `blockchains/theta/denylist.json`
    - `blockchains/thundertoken/denylist.json`
    - `blockchains/tomochain/denylist.json`
    - `blockchains/tron/denylist.json`
    - `blockchains/vechain/denylist.json`
    - `blockchains/wanchain/denylist.json`
    - `blockchains/xdai/denylist.json`
    - `blockchains/xdc/denylist.json`

**Notes**: Public token-asset registry consumed by Trust Wallet. Changes to which tokens are shown in-wallet are a frontend-layer censorship surface.

_Generic list-maintenance commits (phishing / abuse / scam registry activity, no OFAC keyword): 32. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `Uniswap/token-lists` — frontend_token_list_schema

- **Operator**: uniswap
- **Clone status**: ok
- **Matched files** (n=3):
    - `src/tokenlist.schema.json`
    - `test/__snapshots__/tokenlist.schema.test.ts.snap`
    - `test/tokenlist.schema.test.ts`

**Notes**: Schema repo — the token lists themselves are distributed by individual list-issuers. Included for provenance; the primary targets are the token-list issuer repos.

### `ethereum-lists/tokens` — community_token_registry

- **Operator**: community
- **Clone status**: ok
- **Matched files** (n=0):

**Notes**: Community registry of ETH-chain tokens. Deprecations and delistings track wallet / explorer UX decisions.

## Scope and caveats

- **Classification is keyword-based**, not semantic. A commit that touches `ofacblacklist.go` with the subject *"refactor"* lands in `other`; one that is semantically sanctions-related but uses different subject words could also slip to `other`. The raw JSON emits the full (subject, path, +/-) tuple so an auditor can re-classify.
- **Negative results are scoped to the configured path patterns** in `candidates.yaml`. The scanner now includes historical deleted and renamed paths, but it still cannot see private repos or public files whose names do not match the candidate's compliance patterns.
- **Clone status `not_found`** means the repo URL did not exist or was made private since the candidate was listed. **`skipped`** means the scanner was asked to not clone (e.g. offline run). **`clone_failed`** means the clone hit a non-404 network error.
- **The `skipped_operators` list** in `candidates.yaml` names operators (bloXroute, Titan Builder, Beaverbuild, Coinbase Wallet, OpenSea, Circle, Chainflip) whose compliance logic is not in public source control. For those operators the git-history channel is structurally unavailable — a finding in its own right.
- **This census does not by itself admit events**. A sanctions-reaction commit becomes an admitted observation only when it carries body_hash + body_path + a named target (an OFAC SDN, a court order, etc.) and survives the per-event `scripts/validate.py` admission check.
