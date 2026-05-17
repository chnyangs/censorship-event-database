# Data Sources — Complete Inventory

Every external data source this project reads from, organized by purpose. Each entry: URL, free / paid, coverage notes, how we use it, known issues.

> This is the source of truth. [methodology.md](methodology.md) and [example-tornado-cash-2022.md](example-tornado-cash-2022.md) both dereference names into specific URLs via this document.

---

## 0. Scope reminder — what counts as an "event"

An **event** is a discrete, actor-attributable action with legal / policy / commercial authority, affecting identified addresses / protocols / assets.

Included:

- **Policy**: OFAC designations, EU sanctions, UN resolutions, UK OFSI listings.
- **Legal**: court orders (freeze, seizure, injunction), DOJ indictments, SEC / CFTC actions.
- **Corporate**: Circle / Tether blacklisting, exchange delistings, frontend delistings.
- **National infrastructure**: country-level bans with a named directive (e.g. PBOC 2021 crypto ban).

Not included:

- **Chronic / continuous censorship** (GFW blocking Etherscan since ~2019) — that is *state*, not an *event*. Belongs to Geo-Monitor (project P2).
- **Anonymous / unattributable actions** — no actor, can't verify.
- **Accidental outages** unless a public investigation attributes them to censorship intent.
- **MEV / frontrunning** unless it crosses into deliberate address-level filtering.

The event-study method requires discrete triggers + precise timestamps + attributable actors. These three are hard constraints.

---

## 1. Trigger discovery sources

How we find out that an event has happened. Each source has a watcher script in `scripts/watchers/`.

### 1.1 US sanctions — OFAC

| What | URL | Notes |
| --- | --- | --- |
| Recent actions pages | `https://ofac.treasury.gov/recent-actions/YYYYMMDD` | One URL per action date. Stable. |
| SDN list (current XML) | `https://www.treasury.gov/ofac/downloads/sdn.xml` | Authoritative current state. No history. |
| SDN / data schemas doc | `https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-list-data-formats-data-schemas` | Describes the XML schema. |
| Sanctions List Search | `https://sanctionssearch.ofac.treas.gov/` | UI-only, not machine-readable at scale. |

**Historical SDN (for backfill)** — preferred order of use:

1. **Treasury Sanctions List Service (official, 2022+)** — Treasury states that SLS provides an archive of OFAC sanctions-list XML dating back to 2022. Use this first whenever the event date is on or after 2022-01-01.
2. **OpenSanctions** — `https://www.opensanctions.org/datasets/us_ofac_sdn/`. Useful for cross-regime enumeration and older historical normalization, but secondary to the official Treasury archive when the official archive exists.
3. **Build your own**: daily cron that GETs `sdn.xml`, commits to a private git repo, then `git diff` between any two dates. Start today so the archive grows forward; backfill via Wayback for the past.
4. **Wayback Machine for past SDN XML**:
   ```sh
   curl "http://web.archive.org/cdx/search/cdx?url=treasury.gov/ofac/downloads/sdn.xml&output=json&from=2018&to=2025"
   ```
   Coverage is not guaranteed day-by-day but is dense enough for major events.

### 1.2 US criminal / civil enforcement

| What | URL | Notes |
| --- | --- | --- |
| DOJ press releases | `https://www.justice.gov/news` | RSS available. Keyword filter: `cryptocurrency`, `virtual currency`, `mixer`, `blockchain`. |
| DOJ Criminal Division | `https://www.justice.gov/criminal` | Sub-section for broader context. |
| SEC press releases | `https://www.sec.gov/news/pressreleases` | RSS available. |
| SEC EDGAR | `https://www.sec.gov/cgi-bin/browse-edgar` | For corporate filings (8-K, etc.) that reveal sanctions impact. |
| CFTC press room | `https://www.cftc.gov/PressRoom` | DeFi / crypto enforcement actions. |
| FinCEN news | `https://www.fincen.gov/news-releases` | BSA / AML related actions. |
| CourtListener / RECAP | `https://www.courtlistener.com/api/rest/v4/` | Free API with federal docket history. Keyword + party-name search. API key required. |
| PACER (direct) | `https://pacer.uscourts.gov/` | Authoritative federal docket. Paid per-page (~$0.10). |

### 1.3 Non-US regulators

| What | URL | Notes |
| --- | --- | --- |
| EU sanctions | `https://eur-lex.europa.eu/` | EUR-Lex has full text of EU regulations. Search by CELEX ID. |
| EU consolidated sanctions list | `https://webgate.ec.europa.eu/fsd/fsf` | Financial Sanctions Files, XML downloads. |
| OpenSanctions (aggregates) | `https://www.opensanctions.org/datasets/` | EU, UK, UN, many others — same platform as OFAC. |
| UK OFSI consolidated list | `https://www.gov.uk/government/publications/financial-sanctions-consolidated-list-of-targets` | Official UK sanctions list. |
| UK gov news | `https://www.gov.uk/search/news-and-communications` | Filter by department (e.g. HM Treasury, FCA). |
| UN Security Council sanctions | `https://www.un.org/securitycouncil/sanctions/information` | |
| Japan FSA | `https://www.fsa.go.jp/en/news/` | English section, limited. |
| Singapore MAS | `https://www.mas.gov.sg/news` | |
| Canada OSFI / GAC | `https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/` | |
| Russian Central Bank | `https://cbr.ru/eng/` | Use machine translation cautiously. |

### 1.4 Corporate policy triggers

| What | URL | Notes |
| --- | --- | --- |
| Circle blog | `https://www.circle.com/blog` | Issuer communications about USDC. |
| Tether transparency page | `https://tether.to/en/transparency/` | USDT-related announcements. |
| Uniswap governance forum | `https://gov.uniswap.org/` | Front-end delisting discussions. |
| Aave governance forum | `https://governance.aave.com/` | Governance-driven freeze / pause votes. |
| Compound governance | `https://www.comp.xyz/` | |
| MakerDAO forum | `https://forum.makerdao.com/` | DAI-specific blacklist / freeze discussions. |
| dYdX blog | `https://dydx.exchange/blog` | Exchange-level actions. |

---

## 2. L0 — Network / internet-layer censorship

| What | URL | Coverage | Notes |
| --- | --- | --- | --- |
| **Censored Planet** (raw) | `https://data.censoredplanet.org/raw` | 170+ countries, biweekly scans since 2018 | Raw tar files; slow but no access barrier. |
| **Censored Planet** (BigQuery) | request via `https://censoredplanet.org/data` | Same as raw | Faster queries; BQ access on request. Cite dataset names after you get access — do not hard-code. |
| **OONI** API | `https://api.ooni.io/api/v1/measurements` | Volunteer probes, 200+ countries | Public, no key. Has `domain`, `input`, `probe_cc` filters. |
| **OONI Explorer** (human UI) | `https://explorer.ooni.org/` | Same data | Cross-check before admitting an observation. |
| **GFWatch** | (research project; check `https://gfwatch.org/`) | China GFW DNS injection specifically | Publishes datasets of blocked domains. URL may move — check academic paper mirrors. |
| **IODA** | `https://ioda.inetintel.cc.gatech.edu/` | Country-level connectivity outages | Useful for "was there a wider outage we shouldn't attribute to our event?" |
| **CAIDA** BGP data | `https://www.caida.org/catalog/datasets/bgpstream/` | Routing anomalies | For AS-level events (rare but relevant). |
| **Cloudflare Radar** | `https://radar.cloudflare.com/` | Traffic patterns by country | Outage / attack detection, some API access. |
| **NetBlocks** | `https://netblocks.org/` | Monitoring org, publishes reports + Twitter | Qualitative; use as supporting_journalism. |
| **Access Now "KeepItOn"** | `https://www.accessnow.org/keepiton/` | Shutdown reports | Annual + ad-hoc; primarily qualitative. |
| **ISP notices / gov directives** | case-specific | varies | Highest-quality L0 evidence when available. |

**Pipeline note**: for each target domain, query Censored Planet and OONI in parallel; use them first to establish an observed reachability change. Only then consider attribution to the trigger, using government directives / ISP notices and outage controls from IODA / Cloudflare Radar.

---

## 3. L1 — Consensus-layer filtering

### 3.1 Ethereum (primary coverage)

| What | URL | Notes |
| --- | --- | --- |
| **mevwatch.info** | `https://www.mevwatch.info` | Dashboard on OFAC-compliance rate by relay. Not machine-API-friendly; scrape + Wayback for historical. |
| **censorship.pics** | `https://censorship.pics` | Wahrstätter dashboard, more granular filtering stats. |
| **mevboost.pics** | `https://mevboost.pics` | Block-by-block relay / builder attribution. |
| **relayscan.io** | `https://www.relayscan.io` | Relay health + filtering. Publishes CSV. |
| **Flashbots transparency** | `https://transparency.flashbots.net/` | Flashbots' own stats. Primary-corporate source for that relay specifically. |
| **Relay data APIs** | per-relay, e.g. `https://boost-relay.flashbots.net/relay/v1/data/bidtraces/proposer_payload_delivered` | Each major relay exposes this standardized endpoint. Go directly for highest-fidelity. |
| **Beaconcha.in** | `https://beaconcha.in` | Validator-level info, execution payloads. |
| **rated.network** | `https://www.rated.network` | Validator reputation + inclusion metrics. |
| **Wahrstätter GitHub** | `https://github.com/nerolation` | Toni Wahrstätter's account — repos with raw CSV / parquet for MEV-Boost, censorship, etc. Check for `ethereum-pbs-data` and variants. |
| **Self-run node** | run `geth` / `nethermind` + `mev-boost` | For observations not yet captured in public dashboards. Last resort. |

### 3.2 Non-Ethereum L1 — honest scope note

**Coverage is limited**. For events affecting other chains, L1 observations may be unavailable. Record explicitly:

```yaml
- layer: l1_consensus
  chain: bitcoin
  coverage: not_available
  reason: "No public dataset equivalent to mevwatch exists for Bitcoin mining pool filtering."
```

Available data where it exists:

| Chain | What's measurable | Source |
| --- | --- | --- |
| **Bitcoin** | Mining pool attribution per block | `mempool.space`, `https://blockchain.info/blocks` — but filtering analysis is ad-hoc research, no dashboard. |
| **Bitcoin mempool** | `mempool.space` live view | Snapshot only; no historical filter studies. |
| **Solana** | Leader identity per slot | Solana Explorer — leader schedule is public. No filtering dataset. |
| **Cosmos / IBC** | Relayer behavior | No public dataset. |
| **Polygon / BSC** | Validator set, but centralized | Ad-hoc; no PBS equivalent. |

**Decision**: Event DB will record Ethereum L1 observations fully; for other chains, record structured `coverage: not_available` stubs. This is an explicit limitation that goes into the paper.

---

## 4. L3 — RPC endpoint filtering

The RPC layer is where most "everyday users" feel censorship, via Infura / Alchemy / QuickNode / similar providers rejecting calls.

### 4.1 Provider ToS / blog / docs

| Provider | Blog | Docs | Terms of Service |
| --- | --- | --- | --- |
| Infura | `https://www.infura.io/blog` | `https://docs.infura.io` | `https://www.infura.io/terms` |
| Alchemy | `https://www.alchemy.com/blog` | `https://docs.alchemy.com` | `https://www.alchemy.com/terms` |
| QuickNode | `https://www.quicknode.com/blog` | `https://www.quicknode.com/docs` | `https://www.quicknode.com/terms-of-service` |
| Ankr | `https://www.ankr.com/blog/` | `https://www.ankr.com/docs/` | |
| Chainstack | `https://chainstack.com/blog/` | `https://docs.chainstack.com/` | |
| Pocket Network (Pokt) | `https://www.pokt.network/blog/` | | |
| GetBlock | `https://getblock.io/blog/` | | |
| BlastAPI | `https://blastapi.io/blog/` | | |

Pipeline: poll each blog RSS + Wayback CDX for ToS / docs page at weekly cadence during active windows; look for language changes referencing target or sanctions.

### 4.2 Public reproducibility tests

To confirm "the provider is blocking calls affecting target X," send a deterministic test call:

```sh
# Example: test if an RPC provider rejects calls involving a specific address
curl -X POST https://mainnet.infura.io/v3/$INFURA_KEY \
  -H "content-type: application/json" \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_call","params":[{"to":"<target_address>","data":"0x..."},"latest"]}'
```

Record the response. A policy-level rejection has a specific error shape (HTTP 403 or a JSON-RPC error with provider-specific code). This is primary_corporate evidence (it's the provider's own server response).

**Compliance caveat**: only test with **publicly documented target addresses from admitted events**, and only for measurement — never to circumvent. Log all tests to `sources/rpc_test_log.csv` for audit.

### 4.3 Community signals

| Source | What | Use as |
| --- | --- | --- |
| Ethereum StackExchange | `https://ethereum.stackexchange.com/` | Search for provider-rejection questions | supporting |
| Reddit r/ethdev, r/ethereum | | Developer reports | supporting |
| GitHub issues on wallet repos | e.g. `https://github.com/MetaMask/metamask-extension/issues` | User-reported failures | supporting |
| Flashbots Protect | `https://docs.flashbots.net/flashbots-protect/overview` | RPC that deliberately *avoids* OFAC-compliant relays; its presence is itself a signal | primary_corporate |

---

## 5. L4 — Frontend / dApp UI delisting

### 5.1 Wayback Machine — the core tool

| Endpoint | Purpose |
| --- | --- |
| `https://web.archive.org/save/<url>` | POST-style save endpoint. Submits URL to Wayback. |
| `http://web.archive.org/cdx/search/cdx?url=<pattern>&from=<yyyymmdd>&to=<yyyymmdd>&output=json` | List all snapshots of a URL / URL pattern in a time window. |
| `https://web.archive.org/web/YYYYMMDDhhmmss*/<url>` | Load a specific archived snapshot. |
| Wayback Machine API (`availability`) | `http://archive.org/wayback/available?url=<url>&timestamp=<YYYYMMDD>` — get closest snapshot. |

### 5.2 Open-source frontend repos

For open-source dApp frontends, GitHub history beats Wayback (higher timestamp precision):

| dApp | Repo | What to watch |
| --- | --- | --- |
| Uniswap interface | `https://github.com/Uniswap/interface` | Code-level geofencing, token filters |
| Uniswap default token list | `https://github.com/Uniswap/default-token-list` | Token delistings |
| Aave interface | `https://github.com/aave/interface` | Asset freezes, geofence logic |
| Compound interface | `https://github.com/compound-finance/palisade` (and others) | |
| Curve interface | `https://github.com/curvefi/curve-frontend` | |
| 1inch dApp | `https://github.com/1inch/` (multiple repos) | |
| SushiSwap | `https://github.com/sushiswap/sushiswap-interface` (history) | |

For each: `git log --since=<trigger-2wk> --until=<trigger+8wk>` on the relevant paths.

### 5.3 Token lists ecosystem

| What | URL | Notes |
| --- | --- | --- |
| tokenlists.org | `https://tokenlists.org` | Standard for EVM token metadata. Many lists have commit history. |
| CoinGecko lists | `https://www.coingecko.com/en/api` | Historical market pair availability. |
| CoinMarketCap lists | `https://coinmarketcap.com/api` | Paid API for deep historical. |

### 5.4 Geofencing / hosting config

| Source | What | How |
| --- | --- | --- |
| Cloudflare Workers config (if repo open) | Country-based routing rules | Search repo for `country`, `cf.country`, etc. |
| Vercel / Netlify config | `vercel.json`, `netlify.toml` in frontend repos | Geo rules sometimes here. |
| Actual IP-geo test | fetch the frontend from VPS in multiple countries | Complements Wayback (which doesn't carry geo context). |

### 5.5 NFT platforms (for events touching NFTs)

| Platform | Take-down list source | Notes |
| --- | --- | --- |
| OpenSea | Policy page + periodic removal lists | Format changes; Wayback heavily. |
| Blur | Blog + public removals | |
| LooksRare | Blog | |
| Magic Eden | Blog | |

### 5.6 Code hosting / domain / app distribution

These are necessary for incidents where enforcement lands on the software distribution path rather than only on the frontend itself.

| Source family | URL / entry point | Use |
| --- | --- | --- |
| GitHub repository history | `https://github.com/<org>/<repo>` | Commit-level delist / geofence changes, repo takedowns, release disappearance |
| GitHub org / repo availability via Wayback | `https://web.archive.org/` snapshots of GitHub pages | Evidence that a repo or org disappeared between two times |
| GitHub transparency / policy pages | `https://docs.github.com/en/site-policy` | Context on takedown mechanisms; not event evidence by itself |
| Registrar / RDAP | registrar-specific RDAP or ICANN lookup | Domain status changes, registrar transfer, serverHold / clientHold |
| Certificate Transparency | `https://crt.sh/` | Confirm domain / subdomain issuance and timeline around hosting changes |
| DNS history providers | SecurityTrails, RiskIQ, passive DNS where available | Recover historical A / CNAME / NS changes when frontend hosting moved |
| Apple App Store | `https://apps.apple.com/` | App removals / regional availability changes for wallet or exchange apps |
| Google Play | `https://play.google.com/store` | Android app removals / regional availability changes |

**Completeness note**: these sources are especially important for Tornado Cash-like incidents involving GitHub org disablement, registrar action, or software-distribution chokepoints. Without them, L4 is incomplete for high-profile enforcement events.

---

## 6. Asset-layer — on-chain freeze / blacklist

### 6.1 Block explorers

| Chain | Explorer API |
| --- | --- |
| Ethereum | `https://api.etherscan.io` |
| BSC | `https://api.bscscan.com` |
| Polygon | `https://api.polygonscan.com` |
| Arbitrum | `https://api.arbiscan.io` |
| Optimism | `https://api-optimistic.etherscan.io` |
| Avalanche | `https://api.snowtrace.io` |
| Base | `https://api.basescan.org` |
| Tron | `https://api.trongrid.io` |
| Bitcoin | `https://mempool.space/api` (no admin methods on BTC, but freezes can happen at ERC-20-wrapped level) |

### 6.2 Admin-method topics per stablecoin

For on-chain queries, topic0 is precomputed `keccak256` of the event signature:

| Token | Contract (proxy) | Event | topic0 | Chain |
| --- | --- | --- | --- | --- |
| USDC | `0xA0b86991c6218b36c1d19d4a2e9EB0cE3606eB48` | `Blacklisted(address)` | `0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855` | Ethereum |
| USDC | same | `UnBlacklisted(address)` | separate topic | Ethereum |
| USDT | `0xdAC17F958D2ee523a2206206994597C13D831ec7` | `AddedBlackList(address)` | separate topic | Ethereum |
| USDT | same | `RemovedBlackList(address)` | separate topic | Ethereum |
| DAI | `0x6B175474E89094C44Da98b954EedeAC495271d0F` | Non-standard — MakerDAO uses Emergency Shutdown, no per-address blacklist | — | Ethereum |
| BUSD (deprecated) | `0x4Fabb145d64652a948d72533023f6E7A623C7C53` | `Blacklisted(address)` | | Ethereum |
| FRAX | `0x853d955aCEf822Db058eb8505911ED77F175b99e` | No blacklist (non-custodial) | — | Ethereum |
| LUSD | Liquity's LUSD — no blacklist | — | — | Ethereum |
| USDe (Ethena) | `0x4c9EDD5852cd905f086C759E8383e09bff1E68B3` | TBD — verify at event time | | Ethereum |

**Always verify topic0 at query time** — upgradeable proxies can change implementation. A reliable check: compute `keccak256(signature)` fresh and compare against events observed in a known block range.

### 6.3 Issuer transparency pages

| Issuer | URL |
| --- | --- |
| Circle (USDC) | `https://www.circle.com/en/transparency` |
| Tether (USDT) | `https://tether.to/en/transparency/` |
| Paxos (USDP, BUSD) | `https://paxos.com/attestations/` |
| BUSD historical | Binance transparency pages — historical on Wayback |
| MakerDAO | `https://forum.makerdao.com/` (governance) |
| Ethena (USDe) | `https://ethena.fi/` |

---

## 7. Off-ramp — CEX delistings / withdrawal freezes

### 7.1 Exchange announcement archives

| Exchange | Announcements URL | Machine-readable? |
| --- | --- | --- |
| Binance | `https://www.binance.com/en/support/announcement` | Has RSS, paginated by tag. |
| Coinbase | `https://blog.coinbase.com` | RSS. |
| Kraken | `https://blog.kraken.com` | RSS. |
| OKX | `https://www.okx.com/help/section/announcements-latest-announcements` | HTML only. |
| Bitfinex | `https://www.bitfinex.com/announcements` | HTML only. |
| Bybit | `https://announcements.bybit.com/en/` | HTML only. |
| KuCoin | `https://www.kucoin.com/news/categories/listing` | HTML only. |
| Crypto.com | `https://crypto.com/product-news` | |
| Gemini | `https://www.gemini.com/blog` | RSS. |
| Gate.io | `https://www.gate.io/articlelist/en` | |
| dYdX | `https://dydx.exchange/blog` | RSS. |

### 7.2 Exchange API snapshots

Periodic snapshot + diff for trading-pair presence:

| Exchange | Endpoint |
| --- | --- |
| Binance | `https://api.binance.com/api/v3/exchangeInfo` |
| Coinbase | `https://api.pro.coinbase.com/products` |
| Kraken | `https://api.kraken.com/0/public/AssetPairs` |
| OKX | `https://www.okx.com/api/v5/public/instruments?instType=SPOT` |
| Bybit | `https://api.bybit.com/v5/market/instruments-info?category=spot` |

Schedule: daily snapshot to `sources/cex_api_snapshots/YYYY-MM-DD/<exchange>.json`.

### 7.3 Withdrawal status (harder to observe)

Often not on public API. Use:

- Exchange support center pages (Wayback diff).
- User report triangulation on Reddit / Twitter — supporting evidence only.
- Direct withdrawal attempt (only with authorized test accounts) — rarely feasible.

---

## 8. Archival

| Service | URL | Use |
| --- | --- | --- |
| Wayback Machine save | `https://web.archive.org/save/<url>` | Primary. POST-style. |
| Wayback CDX | `http://web.archive.org/cdx/search/cdx` | Historical snapshot enumeration. |
| archive.today | `https://archive.ph` | Secondary, captures pages Wayback refuses (JS-heavy). |
| Local WARC | `warcio` Python library | Fallback when both refuse. Store in `sources/archived_htmls/`. |
| On-chain receipt local cache | any archive node + `eth_getTransactionReceipt` | Store in `sources/onchain_receipts/`. Insulates against node changes. |

---

## 9. Attribution / translation (for non-English sources)

| What | URL | Notes |
| --- | --- | --- |
| DeepL API | `https://www.deepl.com/pro-api` | For non-English press releases. Paid. |
| Google Cloud Translation | `https://cloud.google.com/translate` | Paid. |
| Translated-by-hand log | `sources/translations/` | Record translator + original text always. |

Rule: machine-translated text is never a primary source. It is a pointer to where to find the original, which a human reader can verify.

---

## 10. Cross-cutting indexes

| Index | URL | Use |
| --- | --- | --- |
| OpenSanctions | `https://www.opensanctions.org/` | Consolidated sanctions across regimes. Primary for cross-regime enumeration; secondary to official archives when those exist. |
| Chainalysis public reports | `https://www.chainalysis.com/reports/` | Supporting only (private data reported). |
| Elliptic public reports | `https://www.elliptic.co/resources` | Supporting only. |
| TRM Labs blog | `https://www.trmlabs.com/resources` | Supporting only. |

These aggregators never serve as primary or semi-primary sources on their own — they are citation trails back to the underlying events.

---

## 11. Source-type mapping

Converting sources above to the taxonomy in methodology §2.3:

| Source family | Default type |
| --- | --- |
| OFAC, EU, UN, UK sanctions pages | `primary_legal` |
| Court filings (PACER, CourtListener) | `primary_legal` |
| SEC / CFTC / DOJ press releases | `primary_legal` |
| Non-legal ministry / utility / central-bank notices | `primary_government` |
| Circle / Tether / Paxos blogs + transparency | `primary_corporate` |
| Exchange announcements | `primary_corporate` |
| dApp provider blog / ToS changes | `primary_corporate` |
| Etherscan (and chain explorers) via API | `primary_onchain` (when fetching finalized logs / receipts) |
| Self-run chain node queries | `primary_onchain` |
| Censored Planet, OONI | `semi_primary_measurement` |
| Wahrstätter / mevwatch / relayscan | `semi_primary_measurement` |
| Wayback Machine snapshot of a `primary_*` page | `semi_primary_wayback` |
| GitHub commit history of open-source frontend | `semi_primary_measurement` (commits are author-signed, timestamp-attestable) |
| GitHub repo / org disappearance observed via Wayback | `semi_primary_wayback` |
| RDAP / registrar status records | `semi_primary_measurement` unless directly issued by the registrar as a primary notice |
| News outlets (Reuters, Bloomberg, CoinDesk, The Block) | `supporting_journalism` |
| Forum posts, Reddit, Twitter, Ethereum StackExchange | `supporting_community` |

---

## 12. Access / cost summary

All free:

- OFAC SLS, DOJ, SEC, EUR-Lex, UK gov (web scraping).
- OpenSanctions (non-commercial).
- Censored Planet raw tars.
- OONI.
- Etherscan basic tier (5 req/s, ample for this project).
- Wayback Machine.
- GitHub (within rate limit).
- Exchange public announcement pages.

Potentially paid / rate-limited depending on depth:

- Passive DNS / historical DNS vendors.
- App store monitoring services if historical regional availability is needed at scale.

Requires registration but free:

- Censored Planet BigQuery.
- CourtListener API key.
- Etherscan / BscScan / etc API key.

Paid (rarely needed):

- PACER (~$0.10 / page cap at $3 / doc, waived under $30 / qtr).
- DeepL / Google Translate (only for specific translations).

**Total recurring cost for this project**: ~$0 / month baseline, ~$20 / month if heavy PACER use during a backfill sprint.
