# Frozen issuer candidate execution manifest

This immutable bundle freezes machine-proposed source eligibility before outcome
collection. It is NOT a human-adjudicated gold frame. `manifest.json` records
input, protocol and script hashes, UTC freeze time, selection/window rules and
counts. All original source rows remain in `source_rows.jsonl`; measurement-unit
alias collapsing does not adjudicate target identities. Updates, family ambiguity
and unclassified chain strings remain pending rather than being judged ineligible.

`issuer_query_units.jsonl` is the complete candidate queue. `first_batch.json`
selects the earliest nonpilot candidate action independently of outcomes. Both
USDC and USDT are queried for every candidate address, including zero/unknown
balances. No query has been run by this generator. Source eligibility and any
historical ABI/contract-version checks still require validation by the collector.

The trigger is a full UTC day [d,d+1), with query window [d-7,d+31). Horizon
deadlines h=1/7/14/30 are intervals [d+h,d+h+1), not invented exact times.
Do not round timestamps to produce unwarranted causal or latency precision.

Existing frozen directories cannot be regenerated in place. Use
`python scripts/prepare_issuer_candidate_manifest.py --verify` to check file hashes;
use a fresh `--out-dir` for another version. Outcome collectors write separately
and record the hash of `bundle.sha256.json`. Never place outcomes in this bundle.
