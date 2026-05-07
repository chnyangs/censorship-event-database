# Worked example — Tornado Cash OFAC designation (2022-08-08)

End-to-end walkthrough of the methodology (see [methodology.md](methodology.md)) on the canonical pilot event. After working through this document you can reproduce the `events/tornado-cash-ofac-2022.yaml` entry exactly and have a playbook for every future event.

> **Reading note**: URLs marked `[real]` are stable data sources verified to exist and return the intended response shape. URLs marked `[illustrative]` are template patterns — run the preceding step first to get the exact URL. Any hash / tx / block number in this doc is a **placeholder** (written as `<…>`) unless explicitly marked `[confirmed]`; replace with the value you observe when running the query.

---

## Step 0 — tools & accounts

One-time setup.

| Need | Why | How |
| --- | --- | --- |
| `curl`, `jq` | Generic HTTP + JSON | pre-installed on macOS |
| `python3` with `requests`, `web3` | On-chain queries, Wayback save API | `pip install requests web3 pyyaml` |
| Etherscan API key | On-chain event logs, free tier ample | register at etherscan.io/apis |
| OONI API access | No key needed | public |
| Censored Planet raw data | No key for raw; BQ needs request | request at `https://censoredplanet.org/data` |
| Wayback Machine | No key for save API | `https://web.archive.org/save/<url>` |
| `git`, archive disk space ~5 GB | Wayback backup + WARC | — |

Create a `.env` in repo root:

```sh
ETHERSCAN_API_KEY=...
OONI_API_BASE=https://api.ooni.io
WAYBACK_USER_AGENT="chain-censorship-measurement/0.1 (contact: you@example.com)"
```

---

## Step 1 — discover & verify the trigger

### 1.1 Primary legal source — OFAC announcement

```sh
curl -L -o raw/ofac-20220808-announcement.html \
  "https://ofac.treasury.gov/recent-actions/20220808"        # [real]
```

This is the OFAC press release. Parse to extract: action type (`DESIGNATION`), date, target entity name, and the full list of designated addresses (they appear in the body as `Digital Currency Address - ETH 0x…`).

### 1.2 SDN XML diff — authoritative address list

OFAC publishes the SDN list as XML. The file at `https://www.treasury.gov/ofac/downloads/sdn.xml` [real] is only the *current* state, so for a historical diff you need an archive source. Preferred order:

- **Treasury Sanctions List Service (official, preferred for 2022+)** — Treasury states that SLS provides XML archive access dating back to 2022. Use this first for the 2022-08-08 event.
- **OpenSanctions** — `https://www.opensanctions.org/datasets/us_ofac_sdn/` [real]. Useful fallback / cross-check with bulk downloads in JSON / CSV.
- **Wayback Machine** (fallback for direct XML): use the availability API to find the closest snapshot before and after the trigger date, then download each and diff:

  ```sh
  curl "http://archive.org/wayback/available?url=treasury.gov/ofac/downloads/sdn.xml&timestamp=20220807" | jq .
  curl "http://archive.org/wayback/available?url=treasury.gov/ofac/downloads/sdn.xml&timestamp=20220809" | jq .
  ```

- **Roll your own archive** for events going forward (daily cron committing `sdn.xml` to a private git). For backfill, prefer Treasury SLS for 2022+.

For this event, fetch the 2022-08-07 and 2022-08-09 SDN snapshots via either path and diff:

```sh
# Using OpenSanctions bulk export (exact filename depends on their current layout — check the dataset page):
curl -o raw/ofac-sdn-20220807.json "https://data.opensanctions.org/datasets/20220807/us_ofac_sdn/entities.ftm.json"
curl -o raw/ofac-sdn-20220809.json "https://data.opensanctions.org/datasets/20220809/us_ofac_sdn/entities.ftm.json"
# Then compare entity sets (jq):
jq -r '.id' raw/ofac-sdn-20220809.json | sort > /tmp/after.txt
jq -r '.id' raw/ofac-sdn-20220807.json | sort > /tmp/before.txt
comm -23 /tmp/after.txt /tmp/before.txt > /tmp/added-entities.txt
```

Grep the added entities for `tornado` (case-insensitive). You will find on the order of ~40 addresses (original August 2022 listing; a second batch came November 2022 — that is a separate event). Extract each ETH address from the `addresses[]` or `topics[]` fields in the entity records.

### 1.3 Contemporaneous journalism (supporting, not sufficient alone)

```sh
curl -L -o raw/reuters-20220808.html \
  "https://www.reuters.com/technology/us-treasury-sanctions-virtual-currency-mixer-tornado-cash-2022-08-08/"   # [real]
```

### 1.4 Trigger timestamp resolution

Precision: the OFAC press release does not carry an hour stamp, but:

- The SDN XML publication time is encoded in the archive repo's commit timestamp.
- Reuters article publication time is in its `<meta property="article:published_time">`.

For this event both agree: **2022-08-08 between 13:00–14:00 UTC**. Record as:

```yaml
trigger:
  timestamp: 2022-08-08T13:30:00Z
  timestamp_precision: hour
  timestamp_sources:
    - sdn_xml_commit: <commit_sha_from_archive_repo>
    - reuters_published: 2022-08-08T13:47:00Z
```

### 1.5 Archive everything touched

Immediately POST each URL above to the Wayback save API:

```sh
for url in \
  "https://ofac.treasury.gov/recent-actions/20220808" \
  "https://www.reuters.com/technology/us-treasury-sanctions-virtual-currency-mixer-tornado-cash-2022-08-08/" ; do
  curl -A "$WAYBACK_USER_AGENT" \
       "https://web.archive.org/save/$url" -o /dev/null -w "%{url_effective}\n"
done
```

Record the returned `x-archive-redirect-to` headers (they contain the timestamped snapshot URL). Store in `sources/wayback_index.csv`.

---

## Step 2 — define the target set

From §1.2 SDN diff, produce a concrete `target.addresses[]`. For the 2022-08-08 listing this is ~40 Ethereum addresses — the main pools plus some router / relayer addresses.

Save to `events/tornado-cash-ofac-2022.yaml` draft under `target.addresses`. Also populate:

- `target.protocol: tornado_cash`
- `target.chains: [ethereum]`
- `target.canonical_domains: [tornado.cash, tornadocash.eth.link, app.tornado.cash]`   # used for L0 and L4 lookups
- `jurisdiction: [US]`

---

## Step 3 — collect layer observations

Open the observation window: `[2022-08-07T13:30Z, 2022-10-03T13:30Z]` (trigger − 24h to trigger + 8 weeks).

### 3.1 Asset layer — the easy one first

USDC is issued by Circle and is an asset-layer actor to test in this worked example. USDC's proxy address on Ethereum is **`0xA0b86991c6218b36c1d19d4a2e9EB0cE3606eB48`** [confirmed]. Its blacklist method emits the event:

```
Blacklisted(address indexed _account)
event topic0: 0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855   # [confirmed, keccak256 of signature]
```

Query all `Blacklisted` events in the observation window where the blacklisted address is in our target set:

```sh
# Ethereum block heights at the window bounds (approximate):
#   2022-08-07 13:30 UTC ≈ block 15303100
#   2022-10-03 13:30 UTC ≈ block 15674200

curl -G "https://api.etherscan.io/api" \
  --data-urlencode "module=logs" \
  --data-urlencode "action=getLogs" \
  --data-urlencode "fromBlock=15303100" \
  --data-urlencode "toBlock=15674200" \
  --data-urlencode "address=0xA0b86991c6218b36c1d19d4a2e9EB0cE3606eB48" \
  --data-urlencode "topic0=0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855" \
  --data-urlencode "apikey=$ETHERSCAN_API_KEY" \
  > raw/usdc-blacklist-events.json
```

Filter locally with `jq` for blacklisted addresses in `target.addresses`. For Tornado Cash you will find **multiple blacklist events within hours of the trigger** — record each as an `observations[]` entry. Example entry after parsing:

```yaml
- layer: asset_onchain
  actor: circle_usdc
  event: address_blacklisted
  target_address: 0x8589427373D6D84E98730D7795D8f6f8731FDA16
  timestamp: 2022-08-08T19:25:35Z        # from block.timestamp
  block: 15307826                         # [placeholder; take from jq output]
  tx: 0x...
  delta_from_trigger_hours: 5.93
  precision: second
  sources:
    - type: primary_onchain
      chain: ethereum
      tx_hash: 0x...
      block: 15307826
      onchain_receipt_hash: sha256:...    # computed after saving receipt locally
    - type: primary_corporate
      url: https://www.circle.com/blog/...
      wayback: https://web.archive.org/web/20220809.../https://www.circle.com/blog/...
```

**Single primary_onchain source is admissible at this layer** (per methodology §5). Corporate source is added for redundancy.

Repeat the same scoped query against USDT (`0xdAC17F958D2ee523a2206206994597C13D831ec7` [confirmed]; blacklist method emits `AddedBlackList(address)` event, different topic). If the target-address/window scan returns no matching admin events, record an anchored `observed_no_change` row for that exact scope:

```yaml
- layer: asset_onchain
  actor: tether_usdt
  event: no_action_observed
  window: [2022-08-07T13:30Z, 2022-10-03T13:30Z]
  sources:
    - type: primary_onchain
      note: "full-window scan of USDT admin methods returned zero matches against target.addresses"
```

### 3.2 L1 — relay / builder filtering

Use `mevwatch.info` historical view. MEV-Watch exposes per-relay OFAC-compliance statistics; its data ultimately derives from `relayscan.io`.

```sh
# mevwatch renders a static page; fetch the archived version around the trigger
curl -L -o raw/mevwatch-20220810.html \
  "https://web.archive.org/web/20220810000000*/mevwatch.info"   # [real, CDX pattern]
# or the live aggregate page:
curl -L -o raw/mevwatch-current.html "https://www.mevwatch.info"
```

Wahrstätter also publishes the raw data on GitHub. Locate the relevant dataset:

- `https://github.com/nerolation` [real] — Toni Wahrstätter's repos, includes `ethereum-pbs-data` and related datasets with CSV exports.

A per-block-per-relay dataset lets you compute:

- For each Tornado-interacting transaction in the observation window, which relay's builder won the slot.
- Inclusion-delay distribution vs matched controls.

Because mevwatch's numerator is "blocks that can be OFAC-censored", the cleanest admission evidence is the relay's own policy declaration captured on Wayback plus an independent measurement dataset:

```sh
# Flashbots relay policy around the trigger:
curl "http://web.archive.org/cdx/search/cdx?url=flashbots.net/*&from=20220808&to=20221001&output=json" \
  > raw/flashbots-cdx.json                                # [real]
```

Pick the first snapshot that references OFAC or Tornado Cash in its policy page, record as observation:

```yaml
- layer: l1_consensus
  actor: relay:flashbots
  event: ofac_compliant_policy_declared
  timestamp: 2022-08-12T00:00:00Z         # earliest wayback snapshot showing the policy
  precision: day
  sources:
    - type: semi_primary_wayback
      url: https://web.archive.org/web/20220812.../https://docs.flashbots.net/flashbots-auction/...
    - type: semi_primary_measurement
      dataset: nerolation/ethereum-pbs-data
      file: relay_compliance.csv
      rows_range: [2022-08-08, 2022-09-08]
```

Do the same for `bloxroute_max_profit`, `bloxroute_regulated`, `manifold`, `eden`, `blocknative`.

### 3.3 L3 — RPC rejections (Infura, Alchemy)

Infura's acceptable use changes are not in a public repo, but:

- Their docs site has Wayback snapshots:
  ```sh
  curl "http://web.archive.org/cdx/search/cdx?url=infura.io/terms/*&from=20220808&to=20221001&output=json" \
    > raw/infura-terms-cdx.json
  ```
- Their announcement blog: `https://www.infura.io/blog` [real], CDX similarly.
- Alchemy announcement: `https://www.alchemy.com/blog` [real].

For Infura on Tornado Cash, look for the mid-August 2022 blog post confirming that Infura and Alchemy had blocked Tornado RPC calls. This is well-attested in contemporaneous reporting — but we still require two sources:

1. Archived Infura / Alchemy blog post.
2. Independently reproducible rejection: take any Tornado-related `eth_call` and hit the Infura public endpoint. If it returns a policy-rejection error (HTTP 403 or JSON-RPC error with specific code), that is the reproduction.

```sh
curl -X POST https://mainnet.infura.io/v3/<your_project_id> \
  -H "content-type: application/json" \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"<a_sanctioned_tornado_address>","data":"0x..."},"latest"]}'
```

If you get a policy rejection, record the response body as `sources[].inline_response`. If you get a regular result (they have relaxed the filter since the Van Loon delisting), record the change as a second event (RPC filter lifted post-2025-03-21).

```yaml
- layer: l3_rpc
  actor: rpc:infura
  event: rpc_policy_change_affecting_target
  timestamp: 2022-08-10T00:00:00Z
  precision: day
  observation_kind: observed_change
  attribution: plausible
  sources:
    - type: primary_corporate
      url: https://www.infura.io/blog/<slug>
      wayback: https://web.archive.org/web/20220811.../...
    - type: primary_corporate
      inline_response:
        http_status: 403
        jsonrpc_error_code: <provider_specific_code>
        body_hash: sha256:...
```

**Note**: primary_corporate + supporting_journalism does **not** satisfy admission by itself. For L3, use a second provider-controlled artifact (for example a reproduced rejection response) or an independent semi-primary measurement artifact.

### 3.4 L4 — frontend delisting

Two frontends are relevant:

1. `tornado.cash` — official Tornado Cash UI.
2. `app.uniswap.org`, `app.aave.com`, etc. — for collateral delistings triggered by the designation.

For the Tornado UI:

```sh
# 1. Find all Wayback snapshots in the window
curl "http://web.archive.org/cdx/search/cdx?url=tornado.cash/*&from=20220807&to=20221003&output=json&collapse=timestamp:8" \
  > raw/tornado-cdx.json

# 2. Diff snapshots 24h before vs 24h after to find deletions
python3 scripts/wayback_diff.py \
  --url https://tornado.cash \
  --before 20220807 \
  --after 20220809
```

The well-known outcome: the UI became inaccessible within ~36h (domain seized, GitHub org disabled). GitHub action documented at:

- `https://github.com/tornadocash/tornado-core` → now returns 404. Wayback has historical snapshots that end in August 2022.

For Uniswap token delistings:

```sh
# Uniswap default token list is a public git-tracked repo
git clone https://github.com/Uniswap/default-token-list raw/uniswap-tokens
cd raw/uniswap-tokens
git log --since=2022-08-07 --until=2022-10-03 --oneline -- src/tokens
# Inspect commits that remove / blacklist tokens associated with Tornado
```

This is the **highest-precision layer** (commit timestamps are minute-accurate, and repos give exact diffs). Record observations at that precision.

### 3.5 L0 — country-level blocking

Scoping note: the relevant L0 question is not a global no-blocking claim; it is whether the selected non-US probe/window/domain cells return measurements for this event.

Two data sources:

**Censored Planet** — request BigQuery access at `https://censoredplanet.org/data` [real]. Once granted, the scan tables are in the `censoredplanet-*` project. Typical query pattern (approximate — run `bq ls` once you have access to confirm dataset name):

```sql
SELECT scan_date, country, domain, result_type, reachable
FROM censoredplanet.satellite.scan
WHERE scan_date BETWEEN DATE('2022-08-01') AND DATE('2022-10-15')
  AND domain IN ('tornado.cash', 'tornadocash.eth.link', 'app.tornado.cash')
ORDER BY scan_date, country
```

Or use the raw tar archives at `https://data.censoredplanet.org/raw` [real] and grep offline.

**OONI** — public API, no authentication:

```sh
curl "https://api.ooni.io/api/v1/measurements?domain=tornado.cash&since=2022-08-07&until=2022-10-03&limit=500" \
  > raw/ooni-tornado.json                                 # [real]
```

For each query cell, first decide whether a measurement denominator exists.
If OONI/CP returns no rows for the selected domain/window/country cell, record
coverage only; do not create an `observed_no_change` row:

```yaml
- layer: l0_network
  status: not_measured
  provider_scope: public_measurement_archive
  note: OONI query returned no measurements for the selected domain/window; no L0 rate or no-blocking claim is reportable.
```

Only if the query returns measurement rows should you create an L0
observation, and then the denominator must be scoped to the returned
countries, domains, and time window.

### 3.6 Off-ramp — CEX reactions

dYdX and Aave Arc both took visible actions on Tornado-associated addresses within days.

- dYdX announcement: `https://dydx.exchange/blog` [real], find Aug 2022 post.
- Aave: forum post at `https://governance.aave.com/` [real] and on-chain freeze of Tornado-related accounts via `PermissionManager`.
- Uniswap token delistings — already captured under L4.

Admit per-exchange:

```yaml
- layer: offramp_cex
  actor: exchange:dydx
  event: addresses_banned
  timestamp: 2022-08-10T14:00:00Z
  precision: hour
  sources:
    - type: primary_corporate
      url: https://dydx.exchange/blog/...
      wayback: https://web.archive.org/web/20220811.../...
    - type: semi_primary_measurement
      endpoint: /compliance-status-or-api-snapshot
      body_hash: sha256:...
```

---

## Step 4 — verify

Run the schema validator and the citation checker:

```sh
python3 scripts/validate.py events/tornado-cash-ofac-2022.yaml
python3 scripts/verify_citations.py events/tornado-cash-ofac-2022.yaml
```

The verifier re-fetches every Wayback URL, recomputes content hashes, and confirms each observation has ≥ 1 primary or ≥ 2 semi-primary sources.

---

## Step 5 — final event YAML (skeleton)

After all layers are processed:

```yaml
id: tornado-cash-ofac-2022
trigger:
  type: ofac_sdn_designation
  actor: US_OFAC
  timestamp: 2022-08-08T13:30:00Z
  timestamp_precision: hour
  citation:
    - url: https://ofac.treasury.gov/recent-actions/20220808
      wayback: https://web.archive.org/web/20220808.../https://ofac.treasury.gov/recent-actions/20220808
    - sdn_xml_snapshot: <official_or_archived_snapshot_id>
target:
  kind: address_set
  addresses: [0x8589427373D6D84E98730D7795D8f6f8731FDA16, ...]  # ~40
  protocol: tornado_cash
  chains: [ethereum]
  canonical_domains: [tornado.cash, app.tornado.cash, tornadocash.eth.link]
jurisdiction: [US]

observations:
  # ~5-10 asset_onchain entries (USDC blacklist txs + USDT null)
  # ~5-8 l1_consensus entries (one per relay)
  # ~3 l3_rpc entries (Infura, Alchemy, maybe QuickNode)
  # ~3 l4_frontend entries (tornado.cash takedown, Uniswap token-list, GitHub org)
  # l0_network coverage only unless public measurement rows exist
  # ~3-5 offramp_cex entries (dYdX, Aave, Binance, etc.)

recovery:
  - layer: asset_onchain
    resolved: false
  - layer: l3_rpc
    resolved_timestamp: 2025-03-21T00:00:00Z
    citation: [tornado-cash-ofac-delisting-2025]
  - layer: l4_frontend
    resolved_timestamp: 2025-03-25T00:00:00Z  # approximate re-emergence of community UIs

analysis_notes: |
  Canonical cross-layer cascade. Primary wave completed within 8h across
  asset, L3, and L4 layers. L0 remains an observability gap in the
  current OONI-derived artifact: archived query windows returned no
  measurement denominator. This event is the benchmark for the
  "US-privacy-tool designation" cascade shape.

tags: [sanctions, privacy_tool, stablecoin_freeze, us_doj_concurrent]
version: 1.0
last_verified: 2026-04-21
```

---

## Step 6 — real-time analog

For a 2026 event, the same workflow can be assisted by watchers (§8.1 in methodology), but production cron is not assumed here. Watchers may post a stub and collection scripts may be rerun during the observation window; trigger triage, evidence interpretation, and admission review remain manual responsibilities.

Concretely, for the stablecoin blacklist layer (§3.1), the daily watch is an `eth_subscribe` on the `Blacklisted` topic filtered to the USDC proxy, rather than a one-shot `getLogs`. For L4 frontend, a daily `cdx` call on each target domain captures new snapshots.

---

## Appendix — inventory of external endpoints

| Layer | Endpoint | Free? | Rate limit? |
| --- | --- | --- | --- |
| Trigger (OFAC) | `ofac.treasury.gov/recent-actions/*` | yes | — |
| Trigger (OFAC SDN XML archive) | `github.com/gboddin/us-sanctions-ofac-archive` | yes | GitHub rate limit |
| Trigger (DOJ) | `justice.gov/news` + RSS | yes | — |
| Trigger (CourtListener) | `courtlistener.com/api/rest/v3/` | yes w/ key | 5000/h |
| L0 (Censored Planet) | `censoredplanet.org/data`, BQ `censoredplanet.*` | yes, request access | BQ quotas |
| L0 (OONI) | `api.ooni.io/api/v1/measurements` | yes | generous |
| L1 (Wahrstätter) | `github.com/nerolation/*`, `censorship.pics`, `mevwatch.info` | yes | — |
| L1 (relayscan) | `relayscan.io` + CSV exports | yes | — |
| L3 (Infura/Alchemy ToS) | provider blog + Wayback CDX | yes | Wayback generous |
| L4 (frontends) | `web.archive.org/cdx/search/cdx` + github | yes | Wayback generous |
| Asset (Etherscan) | `api.etherscan.io` | yes w/ key | 5 calls/s free tier |
| Asset (any chain RPC) | any archive node, e.g. Infura / public RPCs | yes | varies |
| Off-ramp (CEX) | exchange blogs + Wayback CDX | yes | — |
| Archival (Wayback save) | `web.archive.org/save/<url>` | yes | ~15 saves/min sustained |

---

## Running checklist for this single event

- [ ] §1.1 OFAC announcement archived.
- [ ] §1.2 SDN XML diff extracted, target addresses list committed to YAML.
- [ ] §1.5 Wayback snapshots recorded for all external URLs in `trigger.citation`.
- [ ] §3.1 USDC blacklist events queried and per-address observations recorded.
- [ ] §3.1 USDT null observation recorded.
- [ ] §3.2 Per-relay policy observations (≥ 5 relays).
- [ ] §3.3 Infura + Alchemy RPC observations, both ToS-and-reproduction verified.
- [ ] §3.4 tornado.cash frontend takedown + Uniswap default-token-list diff + GitHub org takedown.
- [ ] §3.5 Censored Planet + OONI L0 query cells recorded as coverage; add observations only where a measurement denominator exists.
- [ ] §3.6 dYdX, Aave, Binance, Circle-corporate-statement.
- [ ] §4 `validate.py` + `verify_citations.py` both green.
- [ ] Event YAML committed to `events/tornado-cash-ofac-2022.yaml`.
- [ ] Entry added to `CHANGELOG.md`.

When this checklist is complete, one pilot event is done. Four more to go before locking the schema.
