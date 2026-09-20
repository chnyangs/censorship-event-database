# Ethiopia and Thailand: bounded L0 evidence follow-up

Executed 20 September 2026. These are **machine proposals, not human review**. No event YAML, coverage label, schema, or readiness result was changed. The two event-window measurement denominators remain **unknown**.

This file preserves the initial bounded retrieval batches. The subsequent [daily-frame and raw-recovery report](../l0_ooni_raw_recovery/README.md) records complete query pagination and nine recovered Ethiopian raw measurements. Those later records resolve part of the retrieval gap; they do not establish an independent-probe or population denominator, actual Thai execution, or human-adjudicated censorship outcomes.

## Source corrections

| Event | Supported finding | Unsupported existing inference |
| --- | --- | --- |
| Ethiopia, exchange websites | The cached [Addis Insight report](https://addisinsight.net/2025/11/06/binance-confirms-talks-with-ethiopian-regulators-as-website-access-gets-restricted/) is dated 6 November 2025 and describes restrictions during roughly the preceding three weeks. | 1 October at day precision, an exact onset, a zero-hour response, and a directly established ISP/DNS mechanism. The report does not supply probe counts, ASNs, raw tests, or a first-party NBE/FIS order. |
| Thailand, five exchanges | [SEC announcement 134/2025](https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=12047), dated 29 May, names Bybit, 1000X, CoinEx, OKX and XT.COM and announces MDES access restrictions scheduled for 28 June. [SEC reminder 160/2025](https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=12048), dated 26 June, repeats the plan. | Treating the scheduled date as a measured network-block onset or a zero-hour reaction. The May 30 CoinDesk article and both official notices precede implementation. |

The per-event `*.proposal.json` files preserve the canonical YAML hashes and spell out proposed semantics. The Ethiopian relative phrase is not converted to an exact date by subtracting 21 days. The Thai date is a local calendar date; its UTC day interval is not an implementation timestamp. The official list bounds the **announced platforms**, not every domain or actual affected user.

The SEC notices were initially available through the web browser tool while the early direct HTTP notice requests returned 403. Later read-only requests with explicit browser headers and the public SEC-search referer returned **HTTP 200 original HTML** for both English notices: SECID 12047 in `official-sec-warning/` (SHA-256 `b6926f82f7e47e8d568b92b2db5e97c511b49dde9ac74e87d48c86a449c23b8c`) and SECID 12048 in `official-sec-captured/` (`d7422faba55eb4a363c0a3f428701db919e3298390c6cb80d2b33608b3cf3431`). These directories are under `sources/http_captures/thailand-sec-unlicensed-exchange-block-2025-06/`; their request headers, response metadata and body hashes are retained. The official search page in `official-sec-search/` also returned 200. It is discovery evidence only: the captured page displays results 1–10 of 11, so no exhaustive-search claim is made.

`sec_ooni_browser_response_20260920.json` remains a separate browser-rendered text artifact, **not original HTML**. Earlier 403 bodies and later failed-attempt manifests remain retrieval-gap provenance and are excluded from substantive notice evidence. In particular, the failed PDF request does not establish that the requested PDF exists or concerns this event. The successful HTML notices support the announcement and scheduled effect, not actual network execution. The old secondary-source HTML hashes were verified. Addis Insight also returned a new HTTP 200 capture, whose bytes differ from the old cached page; both remain separately identified.

## Measurement retrieval

| Country scope | Broad discovery window (`since`, `until`) | Explicit root domains | Event-window denominator / ASN count / independent probe count / network failures |
| --- | --- | --- | --- |
| ET | 2025-09-15 to 2025-12-07 | binance.com, okx.com, bybit.com | unknown / unknown / unknown / unknown |
| TH | 2025-05-15 to 2025-07-29 | bybit.com, 1000x.live, coinex.com, okx.com, xt.com | unknown / unknown / unknown / unknown |

These windows are retrieval scopes, not estimates of when blocking began. Each domain and its `www.` hostname was queried with country and `web_connectivity` filters. A second bounded batch used exact `https://HOST/` inputs. The exact-input fallback does not cover HTTP, other paths (including OKX `/th`), or other subdomains. Each batch had 16 queries and at most two pages per query; domain queries used limit 500 and a 25-second timeout, exact-input queries limit 100 and a 40-second timeout. **All 32 event-window queries timed out.** No measurement row was obtained for either complete event window.

Additional read-only diagnostics produced two successful responses:

- `ET`, `domain=binance.com`, 2025-11-06 to 2025-11-07 returned HTTP 200 with `metadata.count=0` and an empty result list. This establishes an empty response for that narrow query only; it does not establish country-wide or event-window absence of tests, successful access, or absence of blocking.
- A **country-wide**, untargeted TH `web_connectivity` aggregation for 2025-06-28 to 2025-06-29 returned 10,118 measurements (`anomaly_count=498`, `confirmed_count=36`, `failure_count=211`, `ok_count=9373`). These values concern all queried Thai web tests, **not the five exchanges**, and cannot supply their denominator. The response exposes no distinct-device count or ASN breakdown.

The narrow TH target query, latest-index diagnostic, and two domain-specific aggregate queries timed out. Two attempted API-documentation URLs returned 404. The initial batches recorded 44 direct HTTP requests: 36 timeouts, three 403s, two 404s, and three 200s. The separately captured SEC follow-up recorded eight additional requests: three 200s (two notice bodies and the search page) and five 403 failures. The combined retained request count is 52; these later source-page requests do not change the 32 failed event-window measurement queries. No retry was interpreted as an independent measurement. Browser-tool requests are separately preserved and excluded from these HTTP counts.

The local inventory inspected 41 cached JSON index artifacts under `sources/l0_datasets` and OONI-named HTTP captures. None contained a matching country/domain row within these windows. This is a bounded cache inventory, not an assertion that no external historical measurements exist.

`query_summary.json` and its CSV expose null event-window denominators, ASN/probe counts and network-failure counts. `retrieved_rows=0` is a count of rows acquired by this run, not a fabricated historical zero. Public OONI index ASNs would represent networks, not independent probe devices. Anomaly flags alone would still require raw test/control review before a blocking conclusion.

## What remains necessary

Obtain a successful historical index/export for each named target and country, recording URL variants, UTC query bounds, pagination completeness, measurement IDs, ASNs, dates, outcome/failure fields, and raw/control records. Then adjudicate comparable pre/post tests and alternative explanations. Do not use today's reachability as historical evidence. These runs leave historical availability unresolved because of retrieval failures; they do not prove that suitable historical data are absent.

The Thailand source correction can improve documentation of a planned legal action now. It cannot close a network-execution gate. Ethiopia still needs independent verification of action, timing, actor, and technical outcome. Neither case can be repaired by replacing missing measurement with a zero, deleting the record, or labeling journalism as a partial probe denominator.

## Versioned migration proposal v0.1

Target a **new schema release** (version assigned during migration), preserving schema 0.2.0 snapshots and a migration ledger. This is a proposal only, not a change to the current validator.

1. Separate `registry_admission` (a documented action/report) from `measurement_eligibility` and a per-surface `measurement_status`. An admitted registry entry may have no validated technical outcome. Keep it in registry totals and report its gap; include it in a measurement denominator only when the declared protocol supports inclusion.
2. Represent `announcement`, `scheduled_effect`, `reported_effect`, and `observed_effect` as distinct stages. Require instrument/source provenance for legal stages and measurement/support provenance for observed technical stages. Never manufacture an observed effect to satisfy admission.
3. Add typed time values: `point`, `local_calendar_date`, `interval`, `approximate_relative`, and `unknown`, with timezone, source phrase and reference date where applicable. A latency requires compatible observed/trigger stages with defensible times; otherwise it remains null or explicitly interval-censored.
4. Allow an explicit `coverage_gap` for an admitted registry record, with reason `retrieval_failed`, `not_queried`, `no_measurements_in_declared_query`, or `insufficient_measurement_support`. These reasons are distinct. A successful empty query is not an observed negative; `not_applicable` requires a separate applicability rationale.
5. Update the admission validator's current mandatory `observed_change`/`observed_no_change` rule and its ban on admitted `coverage_gap` jointly with the schema. Preserve strict support checks on any claimed technical observation. Give registry integrity and measurement readiness separate outcomes, and report all unresolved records in the release manifest.

Review the sidecars against the frozen YAML hashes before applying such a migration. Leave human decisions and reviewer identity fields unfilled. This proposal does not authorize silently interpreting old `partially_measured` labels under the new semantics.

## Artifacts and reproduction

Raw responses and original request manifests live in `sources/evidence_repairs/l0_followup/`, with the later SEC captures in the three successful and five failed `official-sec*` directories described above. `artifact_hashes.json` binds these retained source/analysis artifacts, the final retrieval script/tests, and `capture_http_artifact.py` with its focused tests. It is an artifact-integrity manifest, not proof of source truth or human review. The first domain run did not record a script hash; the exact-URL run's script hash is recorded in `retrieval_findings.json`. Later CLI additions do not imply those runs used the final script version. The later SEC capture metadata records the actual request headers but does not bind a contemporaneous collector-source hash; the final script hash is a reproduction aid, not retroactive run provenance.

To repeat a bounded batch into a new directory:

```sh
python scripts/retrieve_l0_evidence_repairs.py --queries-only --query-mode domain --max-pages 2 --limit 500 --timeout 25 --out-dir /tmp/l0-domain-recheck
python scripts/retrieve_l0_evidence_repairs.py --queries-only --query-mode exact_https --max-pages 2 --limit 100 --timeout 40 --out-dir /tmp/l0-exact-recheck
pytest -q tests/test_retrieve_l0_evidence_repairs.py
```

The focused tests use synthetic fixtures for failures, empty responses, incomplete pagination, malformed responses, duplicate measurements, and probe-count uncertainty. They do not create measurement evidence.
