# Source Artifact Manifest

Dataset snapshot: v0.1.0 · cutoff `2026-05-06` · commit `5b8d353` · generated `2026-05-14T11:24:13Z`

This manifest lists local source artifacts included in the release reproduction surface and records their SHA-256 hashes. Re-fetchable operator-census repository clones and large upstream dumps excluded by `.gitignore` are intentionally not listed; their retrieval policy is recorded in `sources/external_retrieval_receipts.yaml`.

- Files: 790
- Total bytes: 46356377

## By Artifact Family

| family | files |
| --- | ---: |
| `README.md` | 1 |
| `archived_htmls` | 2 |
| `asset_layer_scan` | 17 |
| `external_retrieval_receipts.yaml` | 1 |
| `http_captures` | 652 |
| `l0_datasets` | 24 |
| `l1_datasets` | 3 |
| `ofac_sdn_diffs` | 77 |
| `operator_census` | 1 |
| `operator_commits` | 12 |

## By Extension

| extension | files |
| --- | ---: |
| `csv` | 3 |
| `diff` | 3 |
| `go` | 3 |
| `html` | 524 |
| `json` | 250 |
| `md` | 2 |
| `py` | 1 |
| `txt` | 2 |
| `yaml` | 2 |

## Exclusions

- `sources/operator_census/*/` clones are re-fetchable from `sources/operator_census/candidates.yaml` and are not release inputs. `analysis/operator_census/commits.json` is the compact tracked receipt.
- `sources/ofac_sdn_diffs/current/sdn.xml` and `sources/ofac_sdn_diffs/opensanctions/us_ofac_sdn.ftm.json` are large upstream dumps excluded by `.gitignore`.
- `sources/external_retrieval_receipts.yaml` records the retrieval contract for excluded upstream inputs.
- `source_manifest.*` outputs are excluded from their own input set.
