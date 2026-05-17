# v0.3 Ingestion Operating Report

Generated: `2026-05-17T07:33:02Z`

This report summarizes internal ingestion state. It is not a paper denominator.

## Summary

| Metric | Value |
| --- | ---: |
| Events in local ingestion state | 262 |
| Candidates | 156 |
| Verified internal rows | 105 |
| Candidate / verified ratio | 1.485714 |
| Primary-source verified rows | 0 |
| Rows requiring v0.3 re-extraction | 262 |
| Legacy draft rows | 156 |
| Pending review items | 62 |

## Sources

| Source | Kind | Schedule | Snapshots | Failures | Failure rate | Days since success | Attention |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| OFAC SDN XML | `ofac_sdn_xml` | `daily` | 1 | 0 | 0.0 | 0.023 | no |

## Entity Resolution

| Metric | Value |
| --- | ---: |
| Clusters | 0 |
| Clustered events | 0 |
| Merge decisions | 0 |
| Duplicate / merge rate | 0.0 |

## OFAC Canary

- Clean-run ready: `False`
- Reason: OFAC SDN canary has not accumulated 7 clean days yet.
- Candidate count: 0
- Pending review count: 0

## Coverage

### Evidence Languages

| Language | Evidence rows |
| --- | ---: |

### Jurisdiction Scope

| Scope | Events |
| --- | ---: |
| `AE` | 1 |
| `AR` | 2 |
| `AU` | 1 |
| `BD` | 1 |
| `BE` | 1 |
| `BO` | 1 |
| `BR` | 2 |
| `CA` | 3 |
| `CH` | 2 |
| `CN` | 9 |
| `DE` | 2 |
| `EU` | 9 |
| `EU,IS` | 1 |
| `EU,RU` | 5 |
| `EU,corporate_global` | 1 |
| `FR` | 1 |
| `HK` | 4 |
| `ID` | 2 |
| `IL` | 1 |
| `IN` | 5 |
| `IR` | 2 |
| `IS` | 2 |
| `JP` | 14 |
| `KR` | 3 |
| `KZ` | 2 |
| `MY` | 1 |
| `NG` | 1 |
| `NL` | 2 |
| `PH` | 1 |
| `RU` | 6 |
| `RU,corporate_global` | 1 |
| `SG` | 3 |
| `TH` | 2 |
| `TR` | 2 |
| `UA` | 1 |
| `UK` | 5 |
| `UK,corporate_global` | 1 |
| `UN` | 9 |
| `US` | 90 |
| `US,DE` | 1 |
| `US,DE,PL,CH,EU` | 1 |
| `US,KR,UK` | 1 |
| `US,NL` | 2 |
| `US,NL,DE` | 1 |
| `US,PT,IS,EU` | 1 |
| `US,RU` | 1 |
| `US,RU,DE` | 1 |
| `US,UK` | 2 |
| `US,UK,AU` | 3 |
| `US,UK,AU,EU` | 1 |
| `US,corporate_global` | 11 |
| `UZ` | 1 |
| `ZA` | 1 |
| `corporate_global` | 30 |
| `corporate_global,PH` | 1 |
| `corporate_global,US` | 1 |
