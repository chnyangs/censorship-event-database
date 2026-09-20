# Historical interface inventory and bounded metadata comparison

The inventory in `analysis/historical_interface_verification/v1/inventory.json`
was frozen from the completed endpoint campaign before external metadata
lookups. It records the observed runtime byte hashes, historical block numbers,
code-query IDs and prerequisite-file hashes for two USDC implementation
addresses and the canonical USDT contract. The original inventory describes
the pre-lookup state and remains immutable; subsequent results are separate.

`scripts/prepare_historical_interface_inventory.py` prepares the inventory and
six-GET plan. Its explicit `--fetch` mode captured three Sourcify v2 contract
responses and three HTTP 307 responses from the legacy full-match metadata
routes. Redirects were recorded as gaps and not followed. The run used six
HTTP attempts, no retries, and at least 0.5 seconds between attempts. No source
expansion, compilation or RPC calls occurred during this lookup phase.

`scripts/analyze_historical_interface_matches.py` performs an offline comparison
and writes `association_report.json`. For all three addresses, Sourcify's
indexed onchain runtime bytes match the full historical byte hash recorded by
the endpoint campaign. The supplied ABI includes the expected read function,
and its selector appears as a PUSH4 instruction in the indexed runtime. These
checks support code/address association and interface compatibility, not a
proof of the execution path or the meaning of a returned word.

All three responses report the literal `runtimeMatch` value **`match`**. This
report does not promote that value to `exact_match` or exact/full source
reproduction. Sourcify's reported recompiled runtime differs from its indexed
runtime in the declared CBOR suffix. The checked byte ranges are:

| Code address | Equal prefix `[0, end)` | Different suffix `[start, end)` |
|---|---:|---:|
| USDC implementation `0xa2327a938febf5fec13bacfb16ae10ecbc4cbdcf` | `[0, 21430)` | `[21430, 21483)` |
| USDC implementation `0x43506849d7c04f9138d1a2050bbf3a0c054402dd` | `[0, 23411)` | `[23411, 23464)` |
| USDT `0xdac17f958d2ee523a2206206994597c13d831ec7` | `[0, 11032)` | `[11032, 11075)` |

The report preserves independent hashes for both prefixes and both suffixes,
checks the declared transformation offset and trailing CBOR length, and retains
the captured response hashes and first-party URLs. It reports the observed
`match` field verbatim; no separate definition page was captured within the
frozen lookup budget.

Local compiler reproduction, exact source-metadata verification, full-snapshot
independent chain reconciliation and independent human validation remain
incomplete. The earlier campaign's records and flags are preserved. A future
compiler or source-history study requires its own frozen scope and artifacts.
