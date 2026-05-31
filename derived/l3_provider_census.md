# L3 RPC provider denominator census

Dataset snapshot: v0.2.0-rc-dryrun-11 · cutoff `2026-06-01` · commit `97f58fa` · generated `2026-06-01T00:00:00Z`

This census is a denominator audit, not a provider-rate result. It records which provider/event-window cells have replayable public artifacts and whether any cell is rate-eligible.

- Providers / provider classes: 6
- Event windows: 2
- Provider-event rows: 12
- Rate-eligible rows: 0

## Denominator Classes

| denominator_class | rows |
| --- | ---: |
| `named_partial_only_no_conditional_rate` | 2 |
| `observability_gap` | 10 |

## Provider-Event Surface

| event_id | provider_id | surface | event artifact | denominator_class | rate eligible |
| --- | --- | --- | --- | --- | ---: |
| `tornado-cash-ofac-2022` | `alchemy` | `provider_docs_tos_status` | false | `observability_gap` | false |
| `tornado-cash-ofac-2022` | `flashbots_rpc_endpoint` | `public_git_filter_file` | true | `named_partial_only_no_conditional_rate` | false |
| `tornado-cash-ofac-2022` | `infura` | `provider_docs_tos_status` | false | `observability_gap` | false |
| `tornado-cash-ofac-2022` | `mev_blocker` | `archived_public_docs` | false | `observability_gap` | false |
| `tornado-cash-ofac-2022` | `public_rpc_long_tail` | `listed_future_provider_class` | false | `observability_gap` | false |
| `tornado-cash-ofac-2022` | `quicknode` | `provider_docs_tos_status` | false | `observability_gap` | false |
| `tornado-cash-ofac-delisting-2025` | `alchemy` | `provider_docs_tos_status` | false | `observability_gap` | false |
| `tornado-cash-ofac-delisting-2025` | `flashbots_rpc_endpoint` | `public_git_filter_file` | true | `named_partial_only_no_conditional_rate` | false |
| `tornado-cash-ofac-delisting-2025` | `infura` | `provider_docs_tos_status` | false | `observability_gap` | false |
| `tornado-cash-ofac-delisting-2025` | `mev_blocker` | `archived_public_docs` | false | `observability_gap` | false |
| `tornado-cash-ofac-delisting-2025` | `public_rpc_long_tail` | `listed_future_provider_class` | false | `observability_gap` | false |
| `tornado-cash-ofac-delisting-2025` | `quicknode` | `provider_docs_tos_status` | false | `observability_gap` | false |

## Phrasing Lock

- `named_partial_only_no_conditional_rate` supports mechanism prose only.
- `observability_gap` means no event-window provider denominator exists in v0.1.
- An L3 conditional rate remains forbidden until provider-event rows become rate-eligible.
