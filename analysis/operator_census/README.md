# Operator-compliance source-control census (v0.1)

> Addresses the P1 reviewer pivot from the 2026-04-24 multi-agent
> review (recorded in [`../../CHANGELOG.md`](../../CHANGELOG.md)):
> "scale the git-history-of-operator-repos methodology from n=1 to
> a multi-repo census".

## What this is

A reproducible scan of **8 publicly-maintained operator repositories**
for OFAC-keyed compliance activity visible in git history. Path discovery
uses both the current checkout and historical `git log --all --name-only`
paths, so deleted or renamed files matching the configured patterns are
included. The scan
inputs are pinned in
[`sources/operator_census/candidates.yaml`](../../sources/operator_census/candidates.yaml);
the scanner is
[`scripts/scan_operator_census.py`](../../scripts/scan_operator_census.py);
the local structured output is `commits.json` (ignored because it is
regenerable and can become large with `--emit-all-commits`); the
human-facing table is [`findings.md`](findings.md).

Reproduce:

```bash
python3 scripts/scan_operator_census.py          # clones missing; scans all
python3 scripts/scan_operator_census.py --no-clone  # offline; uses existing clones
python3 scripts/scan_operator_census.py --only flashbots/rpc-endpoint
```

## Result (v0.1 corpus cutoff 2026-04-24)

| Class | Count | Interpretation |
| --- | ---: | --- |
| Repos surveyed | 8 | Flashbots × 4, wallet/frontend × 3, community × 1 |
| Repos with OFAC-named current or historical files | **2** | `flashbots/rpc-endpoint` and deprecated `flashbots/builder`; only `rpc-endpoint` carries an OFAC-keyword reaction commit |
| Repos with no matching public compliance substrate under the configured current-or-historical path patterns | 3 | `flashbots/mev-boost-relay`, `flashbots/rbuilder`, `ethereum-lists/tokens` |
| Repos with list/filter substrates but **no OFAC-keyword reaction** | 4 | `flashbots/builder` (deprecated generic maintenance), `MetaMask/eth-phishing-detect` (phishing), `trustwallet/assets` (denylist files), `Uniswap/token-lists` (schema files) |
| Repos with heavy list activity but **non-OFAC** purpose | 2 | `MetaMask/eth-phishing-detect` and `trustwallet/assets`; **0 OFAC-keyword reactions, 0 OFAC-maintenance commits** under subject-only classification |
| OFAC-keyword reaction commits across entire corpus | **1** | The Flashbots 2022-08-08 PR #90 commit (subject literally contains "ofac") |

## The single OFAC-keyword reaction substrate

`flashbots/rpc-endpoint::server/ofacblacklist.go`. Full commit history
(5 commits across 3.5 years, 2021-10 → 2025-04). The classifier uses
**subject-only matching** as of v0.2 of the scanner — earlier
versions matched against the file path and incorrectly tagged every
commit on this file as a sanctions reaction (including pure refactors
and a Docker update).

| Date | SHA | Subject | v0.2 class | Editorial note |
| --- | --- | --- | --- | --- |
| 2021-10-07 | `8d2c7320` | "Cleaned up some code, in particular around proxying" (file introduced empty) | other | File creation; no OFAC content yet. |
| 2021-10-13 | `78811172` | "cleanup" | other | Refactor; non-substantive. |
| 2022-08-08 | `92ab6b1f` | **"update ofac black list (#90)"** — adds Tornado pool addresses 2h 50m after OFAC SDN | **sanctions_reaction** | The canonical paper anchor. |
| 2022-11-10 | `93bb16a8` | "update docker" (co-modifies `ofacblacklist.go`) | other | Build infra; co-touch only. |
| 2025-04-01 | `1e9c29c5` | "Cleanup unused and unmaintained blacklist file (#173)" — deletes 132-address map 11 days after OFAC delisting | generic_list_maintenance | The post-delisting deletion. The classifier reads "Cleanup" + "blacklist" but no OFAC keyword; the editorial interpretation that this is the OFAC-delisting reaction rests on the candidate-level `known_channel: true` flag and the evidence chain at [`tornado-cash-ofac-delisting-2025`](../evidence-chains/tornado-cash-ofac-delisting-2025.md), **not** on automated keyword classification. |

**Headline census number**: exactly **one** (1) commit in the entire
8-repo surveyed corpus carries an OFAC keyword in its subject. The
2025-04-01 deletion is editorially the OFAC-delisting reaction and
is anchored as such in the L3 observation of
`tornado-cash-ofac-delisting-2025.yaml`, but it is **not** counted
as an OFAC-keyword commit by the automated classifier — that is
the right behavior, because the classifier's job is to surface
*subject-level* state-action language, and the editorial layer
above it adds context the keyword classifier does not see.

The 2022-08-08 and 2025-04-01 commits are the two observations
anchoring the paper's L3 evidence in
[`tornado-cash-ofac-2022`](../evidence-chains/tornado-cash-ofac-2022.md)
and [`tornado-cash-ofac-delisting-2025`](../evidence-chains/tornado-cash-ofac-delisting-2025.md).
They are not rediscovered here; the census confirms the earlier
manual audit and locates no additional OFAC-keyword commits
anywhere else in the surveyed population.

## The structural finding

**Public source control captures an explicit OFAC-keyword reaction on
exactly one surveyed operator substrate under the configured v0.1 path
patterns (Flashbots' public RPC endpoint).** Historical path scanning
also finds a deprecated Flashbots builder `ofac_blacklist.json` and
Trust Wallet denylist substrates; neither produces an OFAC-keyword
reaction commit under subject-only classification. MetaMask's
`eth-phishing-detect` and Trust Wallet's denylist activity are heavy
list-maintenance streams, but structurally distinct from OFAC
compliance in this classifier. After the four-class classifier filters
out prefix false positives ("stormtoken.com" 2017 entries do not
indicate a Storm/Semenov OFAC reaction, which happened in 2023),
exactly one commit carries OFAC state-action language.

The paper's defensible claim from this census is therefore:

> **Under v0.1 of the paper's public-repo sampling frame, git-history
> as a crypto-censorship measurement channel is structurally narrow:
> of 8 surveyed operator repositories spanning relay / builder /
> public RPC / wallet / frontend-schema roles, only `flashbots/rpc-endpoint`
> exposes an OFAC-keyword reaction commit tied to an admitted event.
> Historical scans surface additional generic or deprecated list
> substrates, but not additional sanctions-reaction commits. The channel
> is real, reproducible, and minute-precise where it exists, but it is
> not a population-wide substrate; most operator compliance decisions
> appear outside public git or outside the configured v0.1 patterns.**

This is a *stronger* finding for the paper than a larger N of
OFAC-keyed operator repositories would be, because it sharpens the
observability-gap claim in README §1 point 5 and in C1 of
`docs/paper_claims.md`. The v0.2 follow-on would require admitting
repos beyond the v0.1 candidates list (e.g. Flashbots's SUAPP / SUAVE
repos, private-memory-pool variants, or non-US relay/builder
implementations).

## Scope and caveats

- **The census is English-repository-indexed and US-operator-dominant**
  by construction of the candidates list. Russian, Chinese, Iranian,
  and other non-US-aligned operator substrates are not surveyed.
  This is consistent with (and contributes to) the overall sampling
  frame limitation documented in `docs/paper_claims.md §0`.
- **Classification is keyword-based**, not semantic. The four
  non-OFAC classes (`sanctions_maintenance`, `entity_keyword_hit`,
  `generic_list_maintenance`, `other`) exist precisely to surface
  ambiguous cases for human review. The paper rate (OFAC-reaction)
  is built on the narrow state-action keyword set; the ambiguous
  classes are reported separately.
- **Negative results are pattern-scoped**. The scanner now includes
  deleted and renamed historical paths, but it still cannot see private
  repos, server-side configuration, or public files whose names do not
  match the candidate's v0.1 compliance patterns.
- **`clone_status = ok, files = 0`** is a substantive result: the
  repository is publicly accessible but contains no file matching
  the compliance-file patterns in `candidates.yaml`. This is the
  modal finding across this survey.
- **Out-of-scope operators** (bloXroute, Titan Builder, Beaverbuild,
  Coinbase Wallet, OpenSea, Circle, Chainflip) are listed in
  `candidates.yaml::open_work` with the reason each is not in v0.1
  (typically: no public source repo, or compliance logic is
  server-side).

## Relationship to the paper's claim-to-table matrix

- **Supports C1 (upper-layer concentration)**: the L3 numerator rows
  admitted in Tables 2/6 are the two Flashbots `ofacblacklist.go`
  edits. The census confirms no other admitted L3 observations can
  be derived from the surveyed operator population.
- **Refines the observability gap in README §1 point 5**: the gap is
  not just "L0/L1/L3 have thin measured denominators at v0.1"; it is
  "the only sanctions-reaction commit tied to an admitted event is
  the single-repo rate on `flashbots/rpc-endpoint`; historical scans
  surface additional generic/deprecated list substrates but no
  additional OFAC-keyword reaction commits." This is a measurement
  finding about the medium, not just the corpus.
- **Does not change C2 / C3 / C4 numbers** — the census does not
  admit new events; it corroborates the existing admissions.

## Next scope expansion (v0.2, open work)

A defensible v0.2 pivot would admit:

1. Non-US relay/builder implementations (Russian / East-Asian MEV
   infrastructure, where OFAC compliance is not a regulatory
   attractor but counter-compliance might be).
2. SUAPP / SUAVE repos under flashbots/ and adjacent orgs (next
   generation; compliance-policy surface is still in flux).
3. Wallet extensions beyond MetaMask (Phantom, Rabby, Coinbase
   Wallet repos where some of the blocklist logic may be public).
4. Frontend token-list issuers (the leaf repos that Uniswap's
   schema points to, not the schema repo itself).

Each expansion increases candidate count; if the v0.1 pattern holds
(n=1 admitted OFAC-keyword reaction commit across ~8 surveyed repos),
then the structural measurement claim strengthens. If v0.2 surfaces
more OFAC-keyed repos or admitted reaction commits, the paper can
upgrade from existence-proof to a mini-census-distribution — but that
upgrade is future work, not v0.1 material.
