# Operator-compliance git-history census

Generated: `2026-05-08T02:57:52Z` · scanner `scripts/scan_operator_census.py` · candidates `sources/operator_census/candidates.yaml`.

Reproduction: `python3 scripts/scan_operator_census.py` (requires network for initial clone; subsequent runs reuse local clones under `sources/operator_census/<org>__<repo>/`).

## Tiered census (headline)

**A bare "X / 8 repos" rate is not interpretable** — the 8 candidates span structurally different surfaces (operator compliance file, glob-swept repo with no compliance file, schema-only registry). The honest framing tiers them:

| tier | repos | what it means |
| --- | ---: | --- |
| `confirmed_filter_file` | 2 | the candidate names a `filter_file` and that file exists on disk — operative compliance substrate — `flashbots/rpc-endpoint`, `MetaMask/eth-phishing-detect` |
| `glob_swept_matched` | 2 | no `filter_file` declared; glob sweep returned files but their operative role is not pre-confirmed — `flashbots/builder`, `trustwallet/assets` |
| `schema_or_index_only` | 1 | matched files are schemas / token-list indices, not an operative blocklist (pre-tagged in candidates.yaml) — `Uniswap/token-lists` |
| `glob_swept_zero` | 3 | no compliance-named file on disk — structurally absent in public source control — `flashbots/mev-boost-relay`, `flashbots/rbuilder`, `ethereum-lists/tokens` |

**Headline number**: known-channel substrate edits = **5** across **1** candidate(s) flagged `known_channel: true` in `candidates.yaml`. OFAC-keyword commits = **1** (narrow: subject explicitly names ofac / sdn / sanction / designate). The two are reported separately because PR #173 (the canonical 2025-04-01 Tornado-delisting deletion) lands in the substrate-edit count but not the OFAC-keyword count: its subject reads "Cleanup unused and unmaintained blacklist file" and carries no OFAC keyword.

## Summary

Columns: *OFAC-rxn* = commits whose **subject** carries a state-action keyword (ofac / sdn / sanction / designate). Path is not consulted — earlier versions matched the path and inflated counts on `server/ofacblacklist.go` for every commit including pure refactors and Docker updates. *OFAC-maint* = OFAC-rxn plus a cleanup verb. *KC-edit* = **known-channel substrate edit**: any commit on a `known_channel: true` candidate's `filter_file`, regardless of subject keyword. PR #173 lives here, even though the OFAC-keyword classifier does not see it. *Entity-hit* = commits that name a designated entity (tornado / samourai / lazarus / ...) without state-action language; requires human adjudication because phishing registries produce prefix false positives (e.g. "stormtoken.com" in 2017 long pre-dates the Storm/Semenov OFAC designation). *Generic-list* = blacklist/blocklist/denylist activity with no OFAC or entity tie (dominates phishing-scam registries). First/last-OFAC bounds the OFAC-keyword commit window.

Path discovery scans both the current checkout and historical `git log --all --name-only` output, so deleted or renamed files matching the configured patterns are included in the candidate path set.

| operator | repo | tier | clone | files | commits | OFAC-rxn | OFAC-maint | KC-edit | Entity-hit | Generic-list | first-OFAC | last-OFAC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| flashbots | `flashbots/rpc-endpoint` | confirmed_filter_file | ok | 1 | 5 | 1 | 0 | 5 | 0 | 1 | 2022-08-08 | 2022-08-08 |
| flashbots | `flashbots/mev-boost-relay` | glob_swept_zero | ok | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — | — |
| flashbots | `flashbots/rbuilder` | glob_swept_zero | ok | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — | — |
| flashbots | `flashbots/builder` | glob_swept_matched | ok | 1 | 2 | 0 | 0 | 0 | 0 | 1 | — | — |
| metamask | `MetaMask/eth-phishing-detect` | confirmed_filter_file | ok | 1 | 204341 | 0 | 0 | 0 | 8 | 1450 | — | — |
| trust_wallet | `trustwallet/assets` | glob_swept_matched | ok | 48 | 664 | 0 | 0 | 0 | 0 | 62 | — | — |
| uniswap | `Uniswap/token-lists` | schema_or_index_only | ok | 3 | 74 | 0 | 0 | 0 | 0 | 0 | — | — |
| community | `ethereum-lists/tokens` | glob_swept_zero | ok | 0 | 0 | 0 | 0 | 0 | 0 | 0 | — | — |

## Per-repo detail

### `flashbots/rpc-endpoint` — public_rpc_endpoint

- **Operator**: flashbots
- **Repo tier**: `confirmed_filter_file` (known_channel: true)
- **Clone status**: ok
- **Remote URL**: `https://github.com/flashbots/rpc-endpoint.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `main`
- **HEAD SHA**: `a7e8aa9beb22eb89bde8d60b87d3adbf6739b572`
- **Scan patterns**: `server/ofacblacklist.go`
- **Matched files** (n=1):
    - `server/ofacblacklist.go`
- **Matched current paths** (n=1): `server/ofacblacklist.go`
- **Matched historical paths** (n=1): `server/ofacblacklist.go`

**Notes**: Baseline case. Added Tornado pool addresses 2h 50m after 2022-08-08 SDN (PR #90, commit 92ab6b1f). Deleted entire 132-address map 11 days after 2025-03-21 OFAC delisting (PR #173, commit 1e9c29c). See analysis/evidence-chains/tornado-cash-ofac-{2022,delisting-2025}.md.

**Known-channel substrate edits** (every commit on the declared `filter_file`, n=5). Bookend events (file creation, deletion) appear here even when their subjects do not name OFAC.

| date | sha | path | classification | subject |
| --- | --- | --- | --- | --- |
| 2021-10-07 | `8d2c7320` | `server/ofacblacklist.go` | other | Cleaned up some code, in particular around proxying |
| 2021-10-13 | `78811172` | `server/ofacblacklist.go` | other | cleanup |
| 2022-08-08 | `92ab6b1f` | `server/ofacblacklist.go` | sanctions_reaction | update ofac black list (#90) |
| 2022-11-10 | `93bb16a8` | `server/ofacblacklist.go` | other | update docker |
| 2025-04-01 | `1e9c29c5` | `server/ofacblacklist.go` | generic_list_maintenance | Cleanup unused and unmaintained blacklist file (#173) |

_Generic list-maintenance commits (generic blacklist / blocklist / cleanup vocabulary, no OFAC keyword): 1. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `flashbots/mev-boost-relay` — mev_boost_relay

- **Operator**: flashbots
- **Repo tier**: `glob_swept_zero`
- **Clone status**: ok
- **Remote URL**: `https://github.com/flashbots/mev-boost-relay.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `main`
- **HEAD SHA**: `31fda11c06df0a646a457e6e84f7c618be873156`
- **Scan patterns**: `**/ofac*`, `**/sanctions*`, `**/blacklist*`, `**/censor*`
- **Matched files** (n=0):
- **Matched current paths** (n=0): none
- **Matched historical paths** (n=0): none

**Notes**: MEV-Boost relay reference implementation. Compliance status of the Flashbots-operated relay was a contested 2022-2023 topic (post-OFAC sanctions; "Flashbots Protect" vs "Flashbots Protect++"). Census asks whether the relay software itself ships with a filter substrate.

### `flashbots/rbuilder` — block_builder

- **Operator**: flashbots
- **Repo tier**: `glob_swept_zero`
- **Clone status**: ok
- **Remote URL**: `https://github.com/flashbots/rbuilder.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `develop`
- **HEAD SHA**: `c3301ef0f6ea182d03517309bdf679547a67be7d`
- **Scan patterns**: `**/ofac*`, `**/sanctions*`, `**/blacklist*`, `**/filter*`
- **Matched files** (n=0):
- **Matched current paths** (n=0): none
- **Matched historical paths** (n=0): none

**Notes**: Successor to flashbots/builder. A builder, not a relay — if this ships a compliance filter, it is a stronger finding than the relay layer.

### `flashbots/builder` — block_builder_deprecated

- **Operator**: flashbots
- **Repo tier**: `glob_swept_matched`
- **Clone status**: ok
- **Remote URL**: `https://github.com/flashbots/builder.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `main`
- **HEAD SHA**: `a742641e24df68bc2fc476199b012b0abce40ffe`
- **Scan patterns**: `**/ofac*`, `**/sanctions*`, `**/blacklist*`
- **Matched files** (n=1):
    - `ofac_blacklist.json`
- **Matched current paths** (n=0): none
- **Matched historical paths** (n=1): `ofac_blacklist.json`

**Notes**: Deprecated predecessor to rbuilder. History matters because the 2022-2023 compliance debate happened here.

_Generic list-maintenance commits (generic blacklist / blocklist / cleanup vocabulary, no OFAC keyword): 1. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `MetaMask/eth-phishing-detect` — wallet_blocklist

- **Operator**: metamask
- **Repo tier**: `confirmed_filter_file`
- **Clone status**: ok
- **Remote URL**: `https://github.com/MetaMask/eth-phishing-detect.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `main`
- **HEAD SHA**: `6acdac52eef871f4549fb3d7bf2da0d89834cee9`
- **Scan patterns**: `src/config.json`
- **Matched files** (n=1):
    - `src/config.json`
- **Matched current paths** (n=1): `src/config.json`
- **Matched historical paths** (n=1): `src/config.json`

**Notes**: Consensys-operated phishing blocklist consumed by the MetaMask extension. Not OFAC-keyed; tracks phishing domains and token scams. Included as a control — if filter-list maintenance timing looks similar to Flashbots' OFAC pattern, that strengthens the "public operator git-history as measurement substrate" framing even when the trigger is not OFAC.

_Generic list-maintenance commits (generic blacklist / blocklist / cleanup vocabulary, no OFAC keyword): 1450. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `trustwallet/assets` — wallet_token_index

- **Operator**: trust_wallet
- **Repo tier**: `glob_swept_matched`
- **Clone status**: ok
- **Remote URL**: `https://github.com/trustwallet/assets.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `master`
- **HEAD SHA**: `a3785ec0fc71d435d9a73e15885637c0291a825e`
- **Scan patterns**: `**/blocklist*`, `**/denylist*`, `**/blacklist*`
- **Matched files** (n=48):
    - `blockchains/arbitrum/denylist.json`
    - `blockchains/avalanchec/denylist.json`
    - `blockchains/binance/blacklist.json`
    - `blockchains/binance/denylist.json`
    - `blockchains/bnb/blacklist.json`
    - `blockchains/bsc/denylist.json`
    - `blockchains/callisto/blacklist.json`
    - `blockchains/callisto/denylist.json`
    - `blockchains/classic/blacklist.json`
    - `blockchains/classic/denylist.json`
    - `blockchains/eos/blacklist.json`
    - `blockchains/eos/denylist.json`
    - `blockchains/ethereum/blacklist.json`
    - `blockchains/ethereum/denylist.json`
    - `blockchains/fantom/denylist.json`
    - `blockchains/gochain/blacklist.json`
    - `blockchains/gochain/denylist.json`
    - `blockchains/heco/denylist.json`
    - `blockchains/neo/blacklist.json`
    - `blockchains/neo/denylist.json`
    - `blockchains/nuls/blacklist.json`
    - `blockchains/nuls/denylist.json`
    - `blockchains/ontology/blacklist.json`
    - `blockchains/ontology/denylist.json`
    - `blockchains/optimism/denylist.json`
    - `blockchains/poa/blacklist.json`
    - `blockchains/poa/denylist.json`
    - `blockchains/polygon/denylist.json`
    - `blockchains/smartchain/denylist.json`
    - `blockchains/solana/denylist.json`
    - `blockchains/terra/blacklist.json`
    - `blockchains/terra/denylist.json`
    - `blockchains/theta/blacklist.json`
    - `blockchains/theta/denylist.json`
    - `blockchains/thundertoken/blacklist.json`
    - `blockchains/thundertoken/denylist.json`
    - `blockchains/tomochain/blacklist.json`
    - `blockchains/tomochain/denylist.json`
    - `blockchains/tron/blacklist.json`
    - `blockchains/tron/denylist.json`
    - `blockchains/vechain/blacklist.json`
    - `blockchains/vechain/denylist.json`
    - `blockchains/wanchain/blacklist.json`
    - `blockchains/wanchain/denylist.json`
    - `blockchains/xdai/blacklist.json`
    - `blockchains/xdai/denylist.json`
    - `blockchains/xdc/blacklist.json`
    - `blockchains/xdc/denylist.json`
- **Matched current paths** (n=0): none
- **Matched historical paths** (n=48): `blockchains/arbitrum/denylist.json`, `blockchains/avalanchec/denylist.json`, `blockchains/binance/blacklist.json`, `blockchains/binance/denylist.json`, `blockchains/bnb/blacklist.json`, `blockchains/bsc/denylist.json`, `blockchains/callisto/blacklist.json`, `blockchains/callisto/denylist.json`, `blockchains/classic/blacklist.json`, `blockchains/classic/denylist.json`, `blockchains/eos/blacklist.json`, `blockchains/eos/denylist.json`, `blockchains/ethereum/blacklist.json`, `blockchains/ethereum/denylist.json`, `blockchains/fantom/denylist.json`, `blockchains/gochain/blacklist.json`, `blockchains/gochain/denylist.json`, `blockchains/heco/denylist.json`, `blockchains/neo/blacklist.json`, `blockchains/neo/denylist.json`, `blockchains/nuls/blacklist.json`, `blockchains/nuls/denylist.json`, `blockchains/ontology/blacklist.json`, `blockchains/ontology/denylist.json`, `blockchains/optimism/denylist.json`, `blockchains/poa/blacklist.json`, `blockchains/poa/denylist.json`, `blockchains/polygon/denylist.json`, `blockchains/smartchain/denylist.json`, `blockchains/solana/denylist.json`, `blockchains/terra/blacklist.json`, `blockchains/terra/denylist.json`, `blockchains/theta/blacklist.json`, `blockchains/theta/denylist.json`, `blockchains/thundertoken/blacklist.json`, `blockchains/thundertoken/denylist.json`, `blockchains/tomochain/blacklist.json`, `blockchains/tomochain/denylist.json`, `blockchains/tron/blacklist.json`, `blockchains/tron/denylist.json`, `blockchains/vechain/blacklist.json`, `blockchains/vechain/denylist.json`, `blockchains/wanchain/blacklist.json`, `blockchains/wanchain/denylist.json`, `blockchains/xdai/blacklist.json`, `blockchains/xdai/denylist.json`, `blockchains/xdc/blacklist.json`, `blockchains/xdc/denylist.json`

**Notes**: Public token-asset registry consumed by Trust Wallet. Changes to which tokens are shown in-wallet are a frontend-layer censorship surface.

_Generic list-maintenance commits (generic blacklist / blocklist / cleanup vocabulary, no OFAC keyword): 62. Not tabulated individually — regenerate with `--emit-all-commits` for the full local stream._

### `Uniswap/token-lists` — frontend_token_list_schema

- **Operator**: uniswap
- **Repo tier**: `schema_or_index_only`
- **Clone status**: ok
- **Remote URL**: `https://github.com/Uniswap/token-lists.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `main`
- **HEAD SHA**: `01705f94a307270b6c0fe5f55c7e66f7b92373cc`
- **Scan patterns**: `**/tokenlist*`, `**/banned*`, `**/blocklist*`
- **Matched files** (n=3):
    - `src/tokenlist.schema.json`
    - `test/__snapshots__/tokenlist.schema.test.ts.snap`
    - `test/tokenlist.schema.test.ts`
- **Matched current paths** (n=3): `src/tokenlist.schema.json`, `test/__snapshots__/tokenlist.schema.test.ts.snap`, `test/tokenlist.schema.test.ts`
- **Matched historical paths** (n=3): `src/tokenlist.schema.json`, `test/__snapshots__/tokenlist.schema.test.ts.snap`, `test/tokenlist.schema.test.ts`

**Notes**: Schema repo — the token lists themselves are distributed by individual list-issuers. Included for provenance; the primary targets are the token-list issuer repos. Pre-tagged `schema_or_index_only` so the headline census denominator does not treat its matched-files count (3 schema fixtures) as a comparable substrate to the confirmed-filter-file repos.

### `ethereum-lists/tokens` — community_token_registry

- **Operator**: community
- **Repo tier**: `glob_swept_zero`
- **Clone status**: ok
- **Remote URL**: `https://github.com/ethereum-lists/tokens.git`
- **Clone checked at**: `2026-05-08T02:57:52Z`
- **Default branch**: `master`
- **HEAD SHA**: `55622d80c18cc5cabaa8cb9a4c4214daaa9cf05e`
- **Scan patterns**: `**/deprecated*`, `**/blacklist*`
- **Matched files** (n=0):
- **Matched current paths** (n=0): none
- **Matched historical paths** (n=0): none

**Notes**: Community registry of ETH-chain tokens. Deprecations and delistings track wallet / explorer UX decisions.

## Scope and caveats

- **Classification is keyword-based**, not semantic. A commit that touches `ofacblacklist.go` with the subject *"refactor"* lands in `other`; one that is semantically sanctions-related but uses different subject words could also slip to `other`. The raw JSON emits the full (subject, path, +/-) tuple so an auditor can re-classify.
- **Negative results are scoped to the configured path patterns** in `candidates.yaml`. The scanner now includes historical deleted and renamed paths, but it still cannot see private repos or public files whose names do not match the candidate's compliance patterns.
- **Clone status `not_found`** means the repo URL did not exist or was made private since the candidate was listed. **`skipped`** means the scanner was asked to not clone (e.g. offline run). **`clone_failed`** means the clone hit a non-404 network error.
- **The `skipped_operators` list** in `candidates.yaml` names operators (bloXroute, Titan Builder, Beaverbuild, Coinbase Wallet, OpenSea, Circle, Chainflip) whose compliance logic is not in public source control. For those operators the git-history channel is structurally unavailable — a finding in its own right.
- **This census does not by itself admit events**. A sanctions-reaction commit becomes an admitted observation only when it carries body_hash + body_path + a named target (an OFAC SDN, a court order, etc.) and survives the per-event `scripts/validate.py` admission check.
