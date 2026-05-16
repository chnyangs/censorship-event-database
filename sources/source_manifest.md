# Source Artifact Manifest

Dataset snapshot: v0.2.0-rc-dryrun-5 · cutoff `2026-05-16` · commit `036e341` · generated `2026-05-19T00:00:00Z`

This manifest lists local source artifacts included in the release reproduction surface and records their SHA-256 hashes. Re-fetchable operator-census repository clones and large upstream dumps excluded by `.gitignore` are intentionally not listed; their retrieval policy is recorded in `sources/external_retrieval_receipts.yaml`.

- Files: 891
- Total bytes: 54272274

## By Artifact Family

| family | files |
| --- | ---: |
| `README.md` | 1 |
| `archived_htmls` | 2 |
| `asset_layer_scan` | 17 |
| `corporate_policy` | 2 |
| `external_retrieval_receipts.yaml` | 1 |
| `federal_enforcement` | 2 |
| `historical_baseline_2013_2016` | 2 |
| `http_captures` | 736 |
| `l0_datasets` | 24 |
| `l1_datasets` | 3 |
| `non_us_state` | 2 |
| `ofac_sdn_diffs` | 77 |
| `operator_census` | 1 |
| `operator_commits` | 12 |
| `source_frame_triage` | 7 |
| `supranational` | 2 |

## By Extension

| extension | files |
| --- | ---: |
| `bin` | 4 |
| `csv` | 9 |
| `diff` | 3 |
| `go` | 3 |
| `html` | 555 |
| `json` | 304 |
| `md` | 8 |
| `py` | 1 |
| `txt` | 2 |
| `yaml` | 2 |

## Exclusions

- `sources/operator_census/*/` clones are re-fetchable from `sources/operator_census/candidates.yaml` and are not release inputs. `analysis/operator_census/commits.json` is the compact tracked receipt.
- `sources/ofac_sdn_diffs/current/sdn.xml` and `sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json` are large upstream dumps excluded by `.gitignore`.
- `sources/external_retrieval_receipts.yaml` records the retrieval contract for excluded upstream inputs.
- `source_manifest.*` outputs are excluded from their own input set.
