# Source Artifact Manifest

Dataset snapshot: v0.2.0-rc-dryrun-2 · cutoff `2026-05-16` · commit `f8dc941` · generated `2026-05-16T12:00:00Z`

This manifest lists local source artifacts included in the release reproduction surface and records their SHA-256 hashes. Re-fetchable operator-census repository clones and large upstream dumps excluded by `.gitignore` are intentionally not listed; their retrieval policy is recorded in `sources/external_retrieval_receipts.yaml`.

- Files: 848
- Total bytes: 48541944

## By Artifact Family

| family | files |
| --- | ---: |
| `README.md` | 1 |
| `archived_htmls` | 2 |
| `asset_layer_scan` | 17 |
| `external_retrieval_receipts.yaml` | 1 |
| `http_captures` | 703 |
| `l0_datasets` | 24 |
| `l1_datasets` | 3 |
| `ofac_sdn_diffs` | 77 |
| `operator_census` | 1 |
| `operator_commits` | 12 |
| `source_frame_triage` | 7 |

## By Extension

| extension | files |
| --- | ---: |
| `bin` | 2 |
| `csv` | 9 |
| `diff` | 3 |
| `go` | 3 |
| `html` | 543 |
| `json` | 280 |
| `md` | 3 |
| `py` | 1 |
| `txt` | 2 |
| `yaml` | 2 |

## Exclusions

- `sources/operator_census/*/` clones are re-fetchable from `sources/operator_census/candidates.yaml` and are not release inputs. `analysis/operator_census/commits.json` is the compact tracked receipt.
- `sources/ofac_sdn_diffs/current/sdn.xml` and `sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json` are large upstream dumps excluded by `.gitignore`.
- `sources/external_retrieval_receipts.yaml` records the retrieval contract for excluded upstream inputs.
- `source_manifest.*` outputs are excluded from their own input set.
