# AWS Ethereum Parquet: metadata-only feasibility

The [official AWS registry](https://registry.opendata.aws/aws-public-blockchain/)
documents anonymous access to `s3://aws-public-blockchain/v1.0/eth/` in
`us-east-2`. Its observed table prefixes are `blocks`, `contracts`, `logs`,
`token_transfers`, `traces`, and `transactions`; there is no separate receipts
prefix in this listing. The official Ethereum schema describes receipt fields
in transactions and a dedicated logs table containing emitter address, topics,
data, transaction/log identity, block number/hash and timestamp.

Actual logs partitions use `v1.0/eth/logs/date=YYYY-MM-DD/`. A separately frozen
enumeration plan binds all 18 cohort windows. Four complete year-prefix listings
enumerated 1,462 objects across 2022–2025 and selected:

- **623 distinct requested dates, all with a Parquet object**;
- **623 selected Parquet objects**;
- **340,604,328,699 stored bytes** (340.6 GB, approximately 317.2 GiB).

The precise per-window costs are in `window_object_costs.json`; overlapping dates
are counted once in the union total. `selected_objects.json` retains exact object
keys, sizes, ETags, last-modified times and storage classes. Multipart ETags are
not represented as content SHA-256 hashes. Raw listing bodies and their SHA-256
hashes are captured, including pagination completion markers. Date/object presence
does not establish that every chain log was indexed correctly.

Only **4,556 bytes** of one sample Parquet object's trailer/footer were read using
validated HTTP Range responses. The object itself is 228,528,726 bytes. The
footer has valid Parquet magic and contains all nine expected log-column names;
a full semantic Parquet schema parser was not installed or run. The provider's
schema documentation was captured separately. Range responses would have been
rejected before reading the body if the server ignored the range or exceeded
the predeclared byte bound. **No full Parquet object was downloaded.**

## Proposed filtered plan, not executed

1. Freeze the selected object manifest, exact windows, canonical issuer addresses,
   four add/remove event topics, schema version, and an explicit transfer budget.
2. Prefer an index source with validated topic pagination if available. AWS remains
   a public fallback, with a known whole-object size upper bound for this cohort.
3. For local DuckDB/Parquet access, supply only the 623 explicit HTTPS object URLs
   and select only event-identity, address, topics, data and timestamp columns.
   Filter canonical issuer addresses and the first topic; decode the USDC target
   from the indexed word and the USDT target from its non-indexed data word.
   Match all frozen candidate addresses/windows locally after acquisition.
4. Verify actual schema and row-group statistics on a separately budgeted sample
   before estimating projected transfer reduction. Predicate/column pushdown does
   not guarantee a small transfer: common token addresses may occur in every row
   group. No filtered-byte estimate is asserted here.
5. Deduplicate on transaction hash/log index/block hash, validate block/time bounds,
   detect conflicting identities, and reconcile event histories against endpoint
   states and an independently checked chain-data source before assigning any
   complete-window response label.

Athena could query the same date-partitioned source with explicit date/address/topic
predicates, but it requires an AWS account and paid query execution; it was not
used. The current result is an exact metadata cost inventory and a feasible schema
mapping, not a completed event-log extraction or a claim that human review blocks
machine collection.
