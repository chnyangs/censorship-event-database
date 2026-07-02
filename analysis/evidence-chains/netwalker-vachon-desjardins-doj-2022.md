# Evidence chain — `netwalker-vachon-desjardins-doj-2022`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-03-10 DOJ announced the extradition of Sebastien
> Vachon-Desjardins to face NetWalker ransomware charges and stated that
> Canadian officers had seized 719 Bitcoin during a 2021-01-27 search. RCMP's
> same-day release states that a Canadian court ordered forfeiture of 680
> Bitcoin. This draft records the official legal arc only; it does not code a
> measured asset_onchain change until a public tx_hash or equivalent on-chain
> anchor is pinned."

## 1. Trigger

- **Type**: `doj_seizure_order`
- **Actor**: `US_DOJ_MDFL_RCMP`
- **Timestamp**: `2022-03-10 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-mdfl/pr/former-canadian-government-employee-extradited-united-states-face-charges-dozens>
  - Wayback: <http://web.archive.org/web/20220313001515/https://www.justice.gov/usao-mdfl/pr/former-canadian-government-employee-extradited-united-states-face-charges-dozens>
  - body_hash: `sha256:d37e3632adb3ae2c79f35fad71b65d3805c4ff10d3fa39faeb809b1caf4661bc`
  - body_path: `sources/http_captures/netwalker-vachon-desjardins-doj-2022/primary/web.archive.org__web-20220313001515-https-www.justice.gov-usao-mdfl-pr-former-canadian-government-employee-extradited-united-states-face-charges-dozens__eb92bb23bb.html`
  > DOJ USAO-MDFL 2022-03-10 release, captured from Wayback after the
> direct live capture returned a DOJ/Akamai interstitial. The source
> announces Vachon-Desjardins's extradition to face NetWalker
> ransomware charges and states that Canadian officers discovered and
> seized 719 Bitcoin during the 2021-01-27 Gatineau search.
- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-mdfl/pr/canadian-national-sentenced-connection-ransomware-attacks-resulting-payment-tens>
  - Wayback: <http://web.archive.org/web/20221013175841/https://www.justice.gov/usao-mdfl/pr/canadian-national-sentenced-connection-ransomware-attacks-resulting-payment-tens>
  - body_hash: `sha256:316d512531e67d1429919d83003cc7f428d0714d6934d82be006ef65bff4c477`
  - body_path: `sources/http_captures/netwalker-vachon-desjardins-doj-2022/primary/web.archive.org__web-20221013175841-https-www.justice.gov-usao-mdfl-pr-canadian-national-sentenced-connection-ransomware-attacks-resulting-payment-tens__503781fe21.html`
  > DOJ USAO-MDFL 2022-10-04 sentencing release, captured from Wayback.
> The source states that Vachon-Desjardins was sentenced to 20 years
> and ordered to forfeit USD 21.5 million; it again states that
> Canadian officers seized 719 Bitcoin during the January 2021 search.
- **`primary_government`**
  - URL: <https://www.rcmp-grc.gc.ca/en/news/2022/successful-collaboration-the-rcmp-and-the-fbi-leads-guilty-plea-and-forfeiture-34-million>
  - Wayback: <http://web.archive.org/web/20220310163440/https://www.rcmp-grc.gc.ca/en/news/2022/successful-collaboration-the-rcmp-and-the-fbi-leads-guilty-plea-and-forfeiture-34-million>
  - body_hash: `sha256:3b63d598876a78834fd9beade08d9651aadeaa4c40a0667f2035740083affaa4`
  - body_path: `sources/http_captures/netwalker-vachon-desjardins-doj-2022/primary/web.archive.org__web-20220310163440-https-www.rcmp-grc.gc.ca-en-news-2022-successful-collaboration-the-rcmp-and-the-fbi-leads-guilty-plea-and-forfeiture-34-million__8bfa8671ff.html`
  > RCMP 2022-03-10 news release, captured from Wayback after the current
> live URL redirected to the RCMP homepage. The source states that the
> RCMP search seized 719 Bitcoin and that the Canadian court ordered
> forfeiture of 680 Bitcoin plus cash and devices.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Sebastien Vachon-Desjardins / NetWalker ransomware affiliate
- **Chains**: `bitcoin`

> Target is the DOJ/RCMP-described NetWalker ransomware affiliate activity
> of Sebastien Vachon-Desjardins. Official sources give aggregate seized and
> forfeited Bitcoin counts, but this draft does not enumerate a complete
> wallet, address, victim, or exchange-provider set. The 719 BTC seizure and
> 680 BTC forfeiture are retained as official legal facts, not as measured
> on-chain actions.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `no_public_cex_cascade_documented_in_window`

**Window**: `2022-03-10 00:00:00+00:00` → `2022-03-24 23:59:59+00:00`

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-mdfl/pr/former-canadian-government-employee-extradited-united-states-face-charges-dozens>
  - Wayback: <http://web.archive.org/web/20220313001515/https://www.justice.gov/usao-mdfl/pr/former-canadian-government-employee-extradited-united-states-face-charges-dozens>
  - body_hash: `sha256:d37e3632adb3ae2c79f35fad71b65d3805c4ff10d3fa39faeb809b1caf4661bc`
  - body_path: `sources/http_captures/netwalker-vachon-desjardins-doj-2022/primary/web.archive.org__web-20220313001515-https-www.justice.gov-usao-mdfl-pr-former-canadian-government-employee-extradited-united-states-face-charges-dozens__eb92bb23bb.html`
  > null_event anchor: the DOJ extradition release (2022-03-10) documents the
> 719 BTC physical seizure and forfeiture of NetWalker affiliate
> Vachon-Desjardins' proceeds. The seizure is legally attested but no
> primary_onchain tx_hash is captured (§1.6), so no asset_onchain
> observed_change is claimed and no public CEX cascade was documented.

## 5. Honest coverage gaps

- **asset_onchain** (`not_measured`): Load-bearing unresolved layer. DOJ and RCMP official sources state that

## 7. Related events

- [`colonial-pipeline-darkside-ransom-clawback-doj-2021`](./colonial-pipeline-darkside-ransom-clawback-doj-2021.md)
- `revil-vasinskyi-polyanin-doj-2021` (draft; no rendered admitted-chain link)
- [`matveev-ofac-2023`](./matveev-ofac-2023.md)
- [`terror-financing-crypto-seizure-doj-2020`](./terror-financing-crypto-seizure-doj-2020.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

