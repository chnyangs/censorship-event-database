# Final Collection Taskboard

Updated: 2026-05-16

Goal: exhaust the declared 2008+ source frames while preserving the same
workflow as the original corpus. The 120 admitted-quality count is a progress
milestone, not a cap. AI/agent work may complete source capture, event YAMLs,
coverage, observations, and regeneration; it must not mark agent-created rows
as human-reviewed admitted cases.

## Current State

| bucket | count | meaning |
| --- | ---: | --- |
| admitted paper corpus | 52 | Already counted by paper tables. |
| observation_closed agent drafts | 4 | Full event YAML + captures + validator pass; awaiting human admission review. |
| rejected registry rows | 1 | Retained for selection transparency. |
| candidate stubs | 17 | Pre-admission rows needing captures and full event YAMLs. |
| admitted-quality milestone | 120 | Progress marker for human-reviewable cases; not a stop rule. |

If the 4 `observation_closed` rows pass human review, the project would have
56 admitted-quality rows toward the 120 milestone. Collection continues until
the source-frame triage manifests are exhausted, even after that milestone.

## Case Completion Definition

A case is not "done" until all of the following are true:

- Candidate row exists or the source-frame provenance is otherwise recorded.
- Trigger has at least one replayable archive anchor (`body_hash+body_path` or
  Wayback).
- Event YAML exists under `events/` with schema 0.2.0 fields.
- All six layers have explicit `coverage[]` rows.
- Every retained observation has admission-grade source evidence.
- `python3 scripts/validate.py events/<id>.yaml` passes.
- `make trigger-registry` links the candidate row to the event row without
  duplicate trigger IDs.
- Generated artifacts can be rebuilt from a deterministic
  `SOURCE_DATE_EPOCH` at or after the dataset cutoff.
- Human review can later switch `status` to `admitted` and `origin` to
  `human_reviewed` without changing the empirical claim.

## Completed Agent-Draft Promotions

| event_id | stratum | status | remaining blocker |
| --- | --- | --- | --- |
| `kraken-sec-staking-2023` | S3 | observation_closed | human admission review |
| `blockfi-sec-lending-2022` | S3 | observation_closed | human admission review |
| `sec-beaxy-platform-shutdown-2023` | S3 | observation_closed | human admission review |
| `alphabay-hansa-doj-2017` | S3 | observation_closed | human admission review |

## Next Promotion Waves

| wave | focus | candidate ids | expected work |
| --- | --- | --- | --- |
| 2 | S4 non-US platform-access actions | `malaysia-sc-binance-disable-2021`, `belgium-fsma-binance-cease-2023`, `uk-fca-binance-markets-2021`, `india-fiu-offshore-vda-block-2023`, `philippines-sec-binance-block-2024` | capture regulator source plus platform/access evidence; split multi-target rows if outcomes differ |
| 3 | S6 EU Russia crypto sanctions | `eu-russia-crypto-wallet-cap-2022`, `eu-russia-full-crypto-wallet-ban-2022` | capture EU legal source plus exchange/custody implementation evidence |
| 4 | S5 corporate policy actions | `paxos-busd-nydfs-minting-stop-2023`, `okx-privacy-token-delist-2024`, `binance-russia-exit-commex-2023` | capture corporate/legal sources; add on-chain or exchange-service observations conservatively |
| 5 | S3 remaining federal enforcement | `kucoin-doj-2024`, `bitmex-cftc-doj-2020`, `helix-doj-mixer-2020` | promote only where trigger-to-reaction timing is defensible; keep Helix as candidate if no post-trigger public layer change exists |
| 6 | 2008+ source-frame backfills | monthly triage manifests | add DOJ/SEC/CFTC/FinCEN, non-US regulator, corporate, supranational, and early historical candidates until the declared frames are exhausted |
