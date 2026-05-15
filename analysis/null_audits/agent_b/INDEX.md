# Null-case cross-audit · agent B · index

Auditor: agent B (independent / parallel with agent A).

Scope: 13 events with `admission_tier: null_case`. This index is a per-event verdict table; the per-event reports in the same directory carry the rubric-aligned reasoning.

| event_id | agent_verdict | confidence | headline concern |
| --- | --- | --- | --- |
| iran-ransomware-ofac-2018 | pass | high | wayback CDX digests should be spot-checked |
| irgc-ransomware-ofac-2022 | pass_with_concerns | medium | `offramp_cex.status: measured` on OFAC-RA-only substrate |
| lazarus-entity-ofac-2019 | pass_with_concerns | medium | trigger citation lacks wayback URL; same `measured` convention |
| lazarus-laundering-ofac-2020 | pass_with_concerns | medium | `analysis_notes` self-contradiction ("null_event rather than null_event") |
| lockbit-leader-ofac-2024 | pass_with_concerns | medium | `coverage.offramp_cex` lacks a substrate note |
| matveev-ofac-2023 | pass_with_concerns | medium | `asset_onchain` = `not_measured` with open SDN XML cross-reference |
| pertsev-nl-arrest-2022 | pass | high | trigger citation lacks wayback URL |
| russian-cybercrime-infra-ofac-2025 | pass_with_concerns | medium | L0/L4 consistency with Aeza/Zservers sibling events |
| sec-v-uniswap-wells-notice-2024 | **needs_human_review** | high | Wells notice was procedural & later withdrawn; L4 substrate does not directly measure app.uniswap.org |
| sichuan-silence-ofac-2024 | pass_with_concerns | medium | possible Sichuan-Silence corporate website not L4-scoped |
| sinbad-ofac-2023 | pass | high | exemplary null event; ready to stamp once CDX digests verified |
| storm-semenov-doj-2023 | pass | high | trigger citation lacks wayback URL |
| zservers-ofac-2025 | pass_with_concerns | medium | `l0_network = not_measured` lacks substrate (no negative-query artifact) |

## Verdict counts (agent B)

| bucket | n |
| --- | --- |
| `pass` | 4 |
| `pass_with_concerns` | 8 |
| `needs_human_review` | 1 |
| `fail` | 0 |

## Most-flagged cross-corpus convention question

The convention of marking `coverage.offramp_cex.status: measured` on individual-BTC null events with only the OFAC RA capture as substrate (no query log, no chain-analytics report slice, no exchange-side artifact) recurs across 7 of the 13 events (irgc, lazarus-entity, lazarus-laundering, lockbit-leader, matveev, russian-cybercrime-infra, sichuan-silence, zservers — the entity- and individual-level null events). This is internally consistent but may merit a corpus-wide convention check.

## Most-flagged single-event concern

`sec-v-uniswap-wells-notice-2024` is the only event in the set marked `needs_human_review`. The Wells notice is a pre-enforcement private staff letter, not a final enforcement action; it was later withdrawn (2025-02-25) without formal complaint filing. The L4 substrate cited as anchor (Uniswap blog + SEC press-release index absence-of-notice) does not include direct app.uniswap.org captures. See per-event report for resolution options.
