# OONI metadata and raw-record recovery

Collected on 20 September 2026. **Nine historical raw measurements were recovered and matched to the frozen metadata. These are machine-prepared evidence, not human-adjudicated censorship findings.** Canonical event YAML and readiness decisions were not edited.

## Retrieval scope and outcome

The daily metadata frame contains 624 country/domain/day queries: Ethiopia (`ET`), 15 September through 6 December 2025 inclusive, for `binance.com`, `okx.com`, and `bybit.com`; Thailand (`TH`), 15 May through 28 July 2025 inclusive, for `bybit.com`, `1000x.live`, `coinex.com`, `okx.com`, and `xt.com`. Query end bounds are exclusive. These are discovery windows, not estimated blocking onsets.

The main run completed 615 queries. A separately preserved retry of every and only the nine incomplete queries completed all nine and returned no additional rows. The raw protocol validates both runs' identities, hashes and pagination accounting. Its union retains every distinct metadata row acquired by either run, with provenance from both; completion updates never discard original rows or filter on anomaly flags. The effective metadata frame is 624/624 complete under those API query parameters.

Nine metadata rows concern Ethiopia: six Binance and three Bybit tests, across eight report IDs and one ASN (`AS24757`). Six tests started on 15 October, one on 16 October, and two on 1 November 2025. Both HTTP and HTTPS inputs occur. There are no retrieved Thai target rows and no Ethiopian OKX rows in this frame. Empty query results are **measurement-coverage gaps**, not observations of successful access or absence of blocking. The nine rows are a retrieved-record count; they are not independent devices or a population denominator.

| Retrieval stage | Preserved result |
|---|---|
| Raw-measurement API v1 | All nine URLs attempted; 18 attempts timed out; zero identity-valid raw responses. |
| S3 JSONL v1 | Six complete prefix listings; six objects, 17,465,310 compressed bytes and 992 JSONL rows streamed; zero exact UID matches. Preserved as a format limitation. |
| S3 postcan v2 | Six objects from the same captured listings, 17,774,579 compressed bytes and 992 members streamed; all nine exact UID members recovered and identity-validated. |

The API and JSONL failures remain unchanged. They are not added to the recovered nine rows as extra measurements. No API, listing, or JSONL request was repeated for postcan v2.

## Why the postcan format was necessary

The [official OONI uploader](https://github.com/ooni/api/blob/master/newapi/ooni_api_uploader.py) writes the uploaded measurement content into JSONL and stores the UID separately in an index. It also archives original POST files whose basenames contain the UID. The [official data client](https://github.com/ooni/data/blob/main/oonidata/src/oonidata/dataclient.py) recovers that UID from postcan filenames. The [receiving handler](https://github.com/ooni/api/blob/master/newapi/ooniapi/probe_services.py) derives the UID timestamp and hourly directory from the same UTC upload time. The frozen prefix selection uses that upload hour, not the probe's measurement-start time.

JSONL v1 recorded no UID-presence diagnostics; its zero exact matches alone cannot establish which fields every streamed record contained. The official producer code supplies the format explanation. No JSONL absence result is used as substantive evidence.

Postcan v2 was frozen before object requests. It retained the original nine-UID selection and used the already captured object inventory. Each compressed object received one anonymous HTTPS GET, paced at least one second apart, with the frozen ETag in `If-Match`; returned ETag and Content-Length were checked before streaming. The frozen total was below the 100,000,000-byte cap. Both gzip integrity and complete compressed-stream length were checked.

Tar members were streamed without filesystem extraction; absolute/traversal paths and symbolic/hard links were rejected. For each retained POST, the exact member basename matched the UID, the first 16 hexadecimal characters of SHA-512 over the original POST bytes matched its UID suffix, and country, ASN, report ID, input URL, test name and measurement-start time matched the frozen metadata. The original POST bytes and per-record SHA-256 are retained. The UID is explicitly derived from its archive member, not invented as an original content field. All nine records passed; there were no identity mismatches.

## Review remains separate

`review_fields.json` beside each retained POST preserves original `test_keys`, controls, test helpers and failure fields. Original automated `blocking` values are `dns` in four records, `http-failure` in four, and `false` in one; original `accessible` is false in eight and true in one. These values are review cues, **not an 8/9 censorship rate**. Three of the four DNS-labelled records also expose `dns_consistency="consistent"`, illustrating why the full controls and request traces require review.

One ASN and eight report IDs do not establish independent probe count, geographic or provider coverage, a causal effect, or an exact implementation time. The Ethiopian source's uncertain relative onset remains unresolved. Thailand has no target measurements in the declared metadata frame. Human identity/source adjudication, comparable pre/post coverage, alternate explanations and any revised readiness decision remain outstanding. Current reachability was never substituted for historical tests.

## Artifacts

- Metadata main/retry: `analysis/evidence_repairs/l0_ooni_daily_v1/` and `l0_ooni_daily_retry_v1/`.
- Frozen raw/API, JSONL and postcan protocols: `analysis/evidence_repairs/l0_ooni_raw_protocol_v1/`, `l0_ooni_s3_protocol_v1/`, and `l0_ooni_postcan_protocol_v2/`.
- Preserved runs: `sources/evidence_repairs/l0_ooni_raw_v1/`, `l0_ooni_s3_v1/`, and `l0_ooni_postcan_v2/`.
- Matched originals and controls: postcan `records/*/post.json` and `review_fields.json`; member/object/identity provenance: `uid_results.json`.
- `summary.json` provides the bounded stage counts. `artifact_hashes.json` binds this report, collectors/tests and preserved raw-recovery protocols/runs. Source metadata bodies are additionally bound by the raw protocol's source hashes.

Full compressed objects were hashed during streaming and discarded; only matching POST content is archived. Re-running a collector requires a new output directory. Frozen collector/helper copies preserve the code used by each protocol; no prior run may be overwritten or silently relabelled.

Focused synthetic checks: `pytest -q tests/test_collect_ooni_raw_measurements.py tests/test_retry_ooni_daily_gaps.py tests/test_collect_ooni_s3_fallback.py tests/test_collect_ooni_postcan_fallback.py`. Tests exercise selection, hashes, pagination, size refusal, identity, gzip truncation, tar path/link rejection and preservation of missingness; synthetic fixtures are not research evidence.
