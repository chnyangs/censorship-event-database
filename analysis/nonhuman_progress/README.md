# Non-human research execution (2026-09-20)

The machine-executable collection has advanced from an excluded feasibility
pilot to a complete endpoint campaign, a complete declared Blockscout index
scan, offline event matching, bounded public-disclosure collection, an OONI
metadata frame with raw-record recovery, and partial cross-transport agreement.
Human eligibility and source-support adjudication remain
separate dependencies. Collection completion at one evidence channel never
turns that channel into a human reference or a causal label.

## Current results

| Evidence stage | Executed result | Interpretation boundary |
| --- | --- | --- |
| Official OFAC frame | 715/715 enumerated 2022--2025 Recent Actions pages retrieved; four annual histories; 416 machine-extracted ETH source entries on 28 pages; 154 distinct address strings | Listing-surface exhaustion is not worldwide completeness. Source entries can repeat aliases and old/new update rows; they are not event or target counts. |
| Frozen machine cohort | 35 address/action measurement units in 18 action windows, crossed with USDC and USDT for 70 issuer units; all 35 current candidates are machine-proposed additions | Human eligibility, target identity and action direction remain unadjudicated. The manifest retains 33 pending action rows, 16 family ambiguities, 332 pilot-family exclusions and four unresolved-chain hex rows. |
| Endpoint campaign | 521 read-only requests produced 140/140 valid first/last snapshots: USDC 35 `0/1`; USDT 19 `0/0`, 14 `0/1`, and 2 `1/1` | Both endpoints lie inside each declared window. A contrast does not identify an exact transition or its cause; equal endpoints do not rule out intervening events. |
| Historical interfaces | Six bounded metadata GETs produced three Sourcify v2 captures and three recorded HTTP 307 gaps; all three indexed runtime hashes match the captured historical runtime bytes, and each expected read selector is ABI-compatible and present as `PUSH4` | Sourcify's literal `match` is reported verbatim. Recompiled full runtimes differ in declared CBOR suffixes; exact source-metadata verification and local compiler reproduction are false. |
| Indexed issuer events | Four predeclared Blockscout topic streams were exhausted or crossed the declared lower bound in 59 pages, yielding 2,829 unique accepted events in blocks 14,477,774--24,050,082 | Declared index-range completeness is not independently verified chain completeness. Upstream operator independence remains unverified. |
| Cohort/event association | Offline matching retains all 70 issuer units. Forty-nine contain indexed events (35 USDC, 14 USDT), covering all 35 candidate addresses; 21 issuer units have zero matches. Event timing relative to the day-level trigger interval is 0 before, 27 within and 22 after | Zero indexed matches are not no-action labels. Within-day order is indeterminate; bounded event time is not exact response latency. Association with a source window does not establish OFAC causation. |
| Cross-transport reconciliation | A frozen earliest-six-window prefix selected 16 measurement units, 32 issuer units and 64 endpoint states. dRPC matched all 149 planned identity/header/code/storage/forwarding/state queries. 1RPC matched 8 of 10 attempts before HTTP 410 then 429 stopped that provider | This establishes partial cross-transport agreement for the 64 selected endpoint-state calls through dRPC. It is not full-cohort reconciliation, provider-independence evidence or a second human reference. |
| Public disclosures | 105 target/operator units (35 targets × Coinbase, Kraken and Binance). Kraken's 18 windows were enumerable: 35 units had no exact frozen alias/address match. Coinbase and Binance produced 70 archive-access gaps | The Kraken result is scoped only to currently enumerable WordPress HTML in the declared windows. It does not show absence of all historical disclosure, account action or private enforcement. Gaps are not negatives. |
| OONI metadata and raw retrieval | The frozen frame contains 624 country/day/domain queries. The main run completed 615 and the outcome-independent retry completed the same nine gaps, for 624/624 effective query completion. Nine metadata rows were returned for Ethiopia (eight anomaly flags, all from AS24757); Thailand returned zero. All nine raw API URLs timed out twice. A bounded JSONL S3 scan could not recover UID-bearing records, then a format-specific POST-archive scan recovered and identity-validated all nine selected UIDs from six objects (17,774,579 compressed bytes) | Metadata availability, anomaly flags and identity-valid raw records do not establish censorship. One ASN is not nine independent probes. Zero Thai rows do not establish access. Raw/control fields are retained for review; `censorship_finding` and `human_review_complete` remain null/false. |
| Joint evaluation | Legacy missingness diagnostics and a reference-gated evaluator exist | No independently adjudicated reference artifact is available, so error rates, correction effects and final domain comparisons remain uncomputed. |

The generated [validation progress report](../validation_progress/README.md),
schema `1.1.0`, cross-checks these stages offline and records per-input hashes. Its null values
mean that an optional artifact or human reference is unavailable; they are not
converted to zero observations. The current input set includes the partial
cross-transport run and all three OONI raw-retrieval stages; it keeps their
counts separate because they concern the same selected observations. Frozen
inventories, request accounting and retained raw POST hashes are checked;
complete compressed S3 objects were streamed and hashed but not retained, so
their full byte streams cannot be rehashed offline from this artifact.

## Reproducible artifacts

- [Official frame](../validation_frame/README.md): `make validation-frame-offline`.
- [Frozen candidate manifest](../issuer_candidate_manifest/README.md):
  `make issuer-candidate-verify`.
- [Endpoint campaign](../issuer_candidate_snapshots/cohort_endpoint_v1/README.md):
  raw requests, boundaries, prerequisites and 140 snapshot records.
- [Historical-interface comparison](../historical_interface_verification/v1/README.md):
  frozen inventory, captures and byte/ABI association report.
- [Blockscout streams and matcher](../blockscout_issuer_logs/README.md):
  raw pages plus an offline matcher that preserves zero-match units.
- [Cross-transport run](../cross_transport_reconciliation/earliest_windows_v1/summary.json):
  frozen prefix, exact attempted/skipped queries and transport-level matches.
- [Disclosure collection](../disclosure_collection/README.md): bounded archive
  enumeration with operator-specific gap accounting.
- [OONI follow-up](../evidence_repairs/l0_followup/README.md): official-source
  corrections, metadata queries and raw-retrieval limits.
- [OONI raw recovery](../evidence_repairs/l0_ooni_raw_recovery/README.md): separate
  API, JSONL and POST-archive outcomes for the same nine selected UIDs.
- [OONI POST-archive fallback](../../sources/evidence_repairs/l0_ooni_postcan_v2/summary.json):
  nine exact UID/hash/metadata identity matches, retained for review without a
  machine censorship label.
- [Joint evaluator](../joint_validation/README.md): `make joint-validation`.
- [Claim--evidence audit](claim-evidence-audit.md): wording that each artifact
  can and cannot support.

Run `make validation-progress` to rebuild the offline cross-check and manuscript
macros without making network requests. Artifact and source hashes establish byte
identity and procedure provenance; they do not establish semantic truth.

## Remaining work

The OONI raw-object fallback is complete: its successful POST-archive pass repairs
the nine raw API retrieval gaps at the identity layer. It does not create probe
representativeness, a population denominator or a censorship conclusion. Local
compiler reproduction, full-cohort independent transport coverage, independently
verified chain completeness, and the Coinbase/Binance archive gaps remain
explicit limitations unless new bounded evidence resolves them.

Human-dependent work is narrower and decisive:

1. adjudicate source eligibility, target identity, additions/removals/updates and
   the unresolved family/chain rows without using outcome measurements;
2. provide blinded source-support and outcome-reference labels, preserve reviewer
   disagreements, review the retained OONI raw/control fields, and compute
   reliability and error estimates only afterward;
3. interpret the same-unit joint comparison and approve final domain, causality
   and release claims.

The legacy event YAML and the user-provided human-review directory remain
unchanged. Readiness failures must remain visible until their evidence and human
gates are actually satisfied.

## Verification scope

`checks.json` is the machine-readable status snapshot. It supersedes the earlier
first-batch-only snapshot and binds the current summaries by SHA-256. Focused
offline tests and JSON/diff checks are recorded there. A successful LaTeX build
or software test does not close a human evidence gate.
