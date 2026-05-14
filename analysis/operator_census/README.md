# Operator-compliance source-control census (v0.1)

> Addresses the P1 reviewer pivot from the 2026-04-24 multi-agent
> review (recorded in [`../../CHANGELOG.md`](../../CHANGELOG.md)):
> "scale the git-history-of-operator-repos methodology from n=1 to
> an explicitly scoped public-source-control scan".

## What this is

A reproducible **8-repo v0.1 public-source-control scan**
for OFAC-keyed compliance activity visible in git history. The scan
inputs are pinned in
[`sources/operator_census/candidates.yaml`](../../sources/operator_census/candidates.yaml);
the scanner is
[`scripts/scan_operator_census.py`](../../scripts/scan_operator_census.py);
the local structured output is `commits.json` (tracked in compact
signal-only form; do not commit `--emit-all-commits` full streams); the
human-facing table is [`findings.md`](findings.md).

Reproduce:

```bash
python3 scripts/scan_operator_census.py          # clones missing; scans all
python3 scripts/scan_operator_census.py --no-clone  # offline; uses existing clones
python3 scripts/scan_operator_census.py --only flashbots/rpc-endpoint
```

## Headline (v0.1 scan cutoff 2026-04-26)

A bare "X commits over Y repos" rate is **not interpretable** because
the 8 candidates span structurally different surfaces. The honest
framing tiers them, and reports two parallel headline numbers — one
narrow (subject-keyword classifier) and one wide (every commit on a
`known_channel: true` repo's `filter_file`).

### Repo tiers

| tier | n | what it means | repos |
| --- | ---: | --- | --- |
| `confirmed_filter_file` | 2 | candidate names a `filter_file` and that file exists on disk — operative compliance substrate | `flashbots/rpc-endpoint`, `MetaMask/eth-phishing-detect` |
| `glob_swept_matched` | 2 | no `filter_file` declared; glob sweep returned files but their operative role is not pre-confirmed | `flashbots/builder`, `trustwallet/assets` |
| `schema_or_index_only` | 1 | matched files are schemas / token-list indices, not an operative blocklist (pre-tagged in `candidates.yaml`) | `Uniswap/token-lists` |
| `glob_swept_zero` | 3 | **no compliance-named file on disk — structurally absent in public source control** | `flashbots/mev-boost-relay`, `flashbots/rbuilder`, `ethereum-lists/tokens` |

The 6 `flashbots/*` candidates are spread across all four tiers; the
distribution itself is a finding (the relay reference implementation,
the new builder, and the deprecated builder all sit in
`glob_swept_zero` or `glob_swept_matched`, not in
`confirmed_filter_file`).

### Headline numbers (paired)

- **Known-channel substrate edits = 5** across the **1**
  candidate flagged `known_channel: true` (`flashbots/rpc-endpoint`,
  filter_file `server/ofacblacklist.go`). This is the wide count:
  every commit touching the substrate, regardless of subject
  keyword. **PR #173 (2025-04-01, "Cleanup unused and unmaintained
  blacklist file" — the canonical Tornado-delisting deletion) is
  in this count**, along with the 2021-10-07 file-creation commit.
- **OFAC-keyword commits = 1** across the scanned 8-repo v0.1 public-source-control frame.
  This is the narrow count: subject must explicitly name
  `ofac` / `sdn` / `sanction` / `designate`. The single hit is
  Flashbots PR #90 (2022-08-08, "update ofac black list").

These two are reported separately on purpose — citing only the wide
count overstates how often subjects explicitly name OFAC; citing
only the narrow count misses both bookends of the paper's mechanism
finding (file creation and PR #173 deletion). The substrate-edit
ledger and the keyword-classifier ledger answer different questions.

## The single confirmed-filter-file OFAC substrate

`flashbots/rpc-endpoint::server/ofacblacklist.go`. All 5 commits in
order (2021-10 → 2025-04). The classifier uses **subject-only
matching** as of v0.2 of the scanner; earlier versions matched the
file path and inflated `sanctions_reaction` to 3 (including pure
refactors and a Docker update).

| Date | SHA | Subject | classifier | substrate-edit |
| --- | --- | --- | --- | --- |
| 2021-10-07 | `8d2c7320` | "Cleaned up some code, in particular around proxying" (file introduced empty) | `other` | ✓ |
| 2021-10-13 | `78811172` | "cleanup" | `other` | ✓ |
| 2022-08-08 | `92ab6b1f` | **"update ofac black list (#90)"** — adds Tornado pool addresses 2h 50m after OFAC SDN | `sanctions_reaction` | ✓ |
| 2022-11-10 | `93bb16a8` | "update docker" (co-modifies `ofacblacklist.go`) | `other` | ✓ |
| 2025-04-01 | `1e9c29c5` | "Cleanup unused and unmaintained blacklist file (#173)" — deletes 132-address map 11 days after OFAC delisting | `generic_list_maintenance` | ✓ |

PR #90 (2022-08-08) and PR #173 (2025-04-01) anchor the paper's L3
evidence in
[`tornado-cash-ofac-2022`](../evidence-chains/tornado-cash-ofac-2022.md)
and [`tornado-cash-ofac-delisting-2025`](../evidence-chains/tornado-cash-ofac-delisting-2025.md).
The scan confirms the manual audit and locates no additional
OFAC-keyword commits anywhere else in the scanned public-source-control frame.

## The structural finding

**Public source control captures compliance decisions on exactly
one confirmed-filter-file substrate (`flashbots/rpc-endpoint`);
six of the other seven repos are structurally absent or
schema-only.** The Flashbots relay, builder, and rbuilder
implementations — at the center of the 2022-2023 PBS-censorship
debate — sit in `glob_swept_zero` (relay, rbuilder) or
`glob_swept_matched` (deprecated builder). Trust Wallet's asset
index and the community-maintained Ethereum token list likewise
ship no operative compliance file. MetaMask's
`eth-phishing-detect` is the only repo with heavy
list-maintenance activity, but that activity is structurally
distinct from OFAC compliance: it is a phishing / scam /
impersonator registry, and after the four-class classifier filters
out prefix false positives ("stormtoken.com" 2017 entries do not
indicate a Storm/Semenov OFAC reaction), exactly zero commits
carry OFAC state-action language.

The paper's defensible claim from this census is therefore:

> **Under v0.1 of the paper's public-repo sampling frame,
> git-history as a crypto-censorship measurement channel is
> structurally narrow: of 8 surveyed public repositories, 1
> (`flashbots/rpc-endpoint`) carries an operative OFAC filter
> file in public source control; 5 known-channel substrate edits
> are visible across 3.5 years on that one substrate; 6 of the
> other 7 scanned repos are either glob-zero (no compliance file
> in public git) or schema-only. Most operator compliance
> decisions live server-side, not in git.**

This is *stronger* than a bare `1 / 8` rate would be: the tiering
sharpens the observability-gap claim in README §1 point 5 and in
C1 of `docs/paper_claims.md`. v0.2 follow-on would require admitting
repos beyond the v0.1 candidates list (e.g. Flashbots's
SUAPP / SUAVE repos, private-memory-pool variants, or non-US
relay/builder implementations).

## Scope and caveats

- **The census is English-repository-indexed and US-operator-dominant**
  by construction of the candidates list. Russian, Chinese, Iranian,
  and other non-US-aligned operator substrates are not surveyed.
- **Negative claims are scoped to the recorded repo HEADs and scan
  patterns.** `findings.md` and `commits.json` record remote URL, clone
  checked time, default branch, HEAD SHA, scan patterns, matched current
  paths, and matched historical paths for each candidate.
- **Classification is keyword-based**, not semantic. The five
  classes (`sanctions_reaction`, `sanctions_maintenance`,
  `entity_keyword_hit`, `generic_list_maintenance`, `other`) plus
  the orthogonal `is_known_channel_substrate_edit` flag exist
  precisely to surface ambiguous cases for human review.
- **`known_channel: true`** is an editorial promotion in
  `candidates.yaml` — it says "every commit touching this file is
  *some* form of compliance edit, regardless of subject". The
  classifier still labels the commit by its subject; the
  substrate-edit ledger is parallel.
- **`repo_tier`** is computed automatically from `filter_file` /
  glob-match results, but `candidates.yaml::repo_tier` can pre-tag
  a repo (used for `Uniswap/token-lists` → `schema_or_index_only`).
  Without the pre-tag, Uniswap would land in `glob_swept_matched`
  and inflate the matched-files count.
- **Out-of-scope operators** (bloXroute, Titan Builder,
  Beaverbuild, Coinbase Wallet, OpenSea, Circle, Chainflip) are
  listed in `candidates.yaml::open_work` with the reason each is
  not in v0.1 (typically: no public source repo, or compliance
  logic is server-side).

## Relationship to the paper's claim-to-table matrix

- **Supports C1 (upper-layer concentration)**: the L3 numerator
  rows admitted in Tables 2/6 are the two Flashbots
  `ofacblacklist.go` substrate edits (PR #90 and PR #173). The
  scan confirms no other admitted L3 observations can be derived from the
  scanned public-source-control frame.
- **Refines the observability gap in README §1 point 5**: not
  just "L0/L1/L3 have thin measured denominators at v0.1" but
  "the only operator-substrate rate visible via public source
  control sits on 1 of 8 scanned public repos, in a single tier, and
  the substrate-edit ledger across 3.5 years is 5 commits".
- **Does not change C2 / C3 / C4 numbers** — the scan does not
  admit new events; it corroborates the existing admissions and
  bounds the substrate.

## Next scope expansion (v0.2, open work)

A defensible v0.2 pivot would admit:

1. Non-US relay/builder implementations (Russian / East-Asian MEV
   infrastructure, where OFAC compliance is not a regulatory
   attractor but counter-compliance might be).
2. SUAPP / SUAVE repos under flashbots/ and adjacent orgs.
3. Wallet extensions beyond MetaMask (Phantom, Rabby, Coinbase
   Wallet repos where some of the blocklist logic may be public).
4. Frontend token-list issuers (the leaf repos that Uniswap's
   schema points to, not the schema repo itself).

Each expansion increases candidate count; if the v0.1 pattern
holds (1 `confirmed_filter_file` repo, 1 `known_channel`-flagged
substrate, 1 OFAC-keyword commit), the structural measurement
claim strengthens. If v0.2 surfaces more substrates, the paper
upgrades from existence-proof to a mini-distribution — but that
upgrade is future work, not v0.1 material.
