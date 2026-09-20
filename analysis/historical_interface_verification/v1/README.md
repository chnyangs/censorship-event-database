# Completed bounded historical-interface comparison

The [inventory](inventory.json) was frozen from the completed candidate endpoint
campaign before metadata lookups. It contains **two USDC implementation addresses
and one USDT runtime code hash**, linked to their observed historical blocks and
captured code-query IDs. Its pre-lookup status remains preserved; subsequent
execution is recorded in [the lookup summary](lookup_summary.json).

The frozen plan executed **six logical GETs and six HTTP attempts**: three
Sourcify v2 JSON captures and three HTTP 307 gaps from legacy metadata routes.
Redirects were not followed. There were no retries, source-download expansion,
RPC queries or local compilation during this lookup phase.

The [offline association report](association_report.json) establishes that
Sourcify's indexed onchain runtime bytes match the full historical runtime hash
for all three code/address combinations. All three supplied ABIs contain the
expected read function, whose selector occurs as a PUSH4 instruction in the
indexed runtime. These are code/address and interface-compatibility checks,
not proof of the execution path or a validated event-response label.

Sourcify's literal `runtimeMatch` value is **`match` for all three entries**.
The supplied recompiled runtimes differ from the indexed runtimes in their
declared CBOR suffixes. The report preserves exact offsets, prefix/suffix hashes
and transformation-length checks. This supports agreement of the executable
prefixes; it does not establish exact source-metadata verification or local
compiler reproduction. No separate match-semantics documentation page was
captured, so the provider's field is reported verbatim.

Human adjudication, full-window logs, independent reference labels and
full-snapshot independent chain reconciliation remain incomplete. The completed
[endpoint campaign](../../issuer_candidate_snapshots/cohort_endpoint_v1/README.md)
provides boundary-state contrasts, which do not establish exact change times,
absence of intervening events or causation. See
[the interface procedure](../../../docs/historical-interface-verification.md)
for the byte ranges and reproducible commands.
