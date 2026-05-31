# Evidence chain — `btc-e-doj-2017`

**Status**: `admitted` · **Stratum**: `S3_doj_sec_cftc_fiod` · **Shape**: `comparison` (1 changed layer(s): `l4_frontend`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a9689fa` · **Schema**: `0.2.0` · **Event last_verified**: `2026-04-22` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "DOJ NDCA indictment of BTC-e / Alexander Vinnik on 2017-07-26 was accompanied
> by a same-day seizure of the canonical btc-e.com domain, documenting the
> earliest L4 frontend seizure in the dataset and establishing the pre-OFAC
> baseline for crypto-exchange enforcement cross-layer cascade shape."

## 1. Trigger

- **Type**: `doj_indictment`
- **Actor**: `US_DOJ_NDCA`
- **Timestamp**: `2017-07-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-ndca/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  - Wayback: <https://web.archive.org/web/20170727013407/https://www.justice.gov/usao-ndca/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  - body_hash: `sha256:2cf3684bc3a1e169adc66e01c3a615540c81a3061eedac0609422559383f0919`
  - body_path: `sources/http_captures/btc-e-doj-2017/wayback_doj_press_snapshot/web.archive.org__web-20170727013407-https-www.justice.gov-usao-ndca-pr-russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged__359babd4a6.html`
  > Wayback memento (2017-07-27 01:34 UTC, ~1 day post-event) of the
> original USAO-NDCA press release "Russian National And Bitcoin
> Exchange Charged In 21-Count Indictment For Operating Alleged
> International Money Laundering Scheme And Allegedly Laundering
> Funds From Hack Of Mt. Gox" (2017-07-26). BTC-e (Canton Business
> Corporation) 21-count indictment in NDCA, naming Alexander
> Vinnik as principal operator. Historical anchor — **earliest
> crypto-exchange enforcement event in the dataset** (predates
> OFAC's first crypto-related SDN by 16 months). v0.3 audit
> 2026-05-20 repair: URL CORRECTED from /archives/opa/pr/... to
> the original /usao-ndca/pr/... canonical form (the /archives/opa/
> form is the post-2024 DOJ CMS redirect destination that returns
> Akamai BotManager stub on live fetch); Wayback memento pinned as
> load-bearing admission anchor with body_hash 2cf3684b... (78776
> bytes real content). Grep confirms title verbatim + 19xBTC-e +
> 16xVinnik + 35xindictment variants + 39xbitcoin + 10xNorthern
> District + 8xMt. Gox + 1xCanton Business + 3xFBI. Earlier
> Akamai stub capture at body_path
> sources/http_captures/btc-e-doj-2017/primary/...__9c617c841b.html
> (sha256:510ff33e..., 2937 bytes) is retained as on-disk reference
> but no longer cited (replaced by this Wayback anchor).
- **`primary_legal`**
  - URL: <https://www.justice.gov/archives/opa/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  > Post-2024 DOJ CMS redirect destination URL. Live fetch (2026-04-22)
> returned a 2937-byte AkamaiGHost bot-block stub rather than the
> press-release body; retained as contextual_unarchived pointer to
> the modern canonical URL. The USAO-NDCA Wayback memento above
> carries the evidentiary content. Same pattern as
> events/coinbase-irs-john-doe-summons-2016.yaml.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: BTC-e (Canton Business Corporation)
- **Chains**: `bitcoin`
- **Canonical domains**: `btc-e.com`

> BTC-e entity (Canton Business Corporation) + Alexander Vinnik individual. No
> digital-currency addresses enumerated in the DOJ press release; Mt. Gox
> hack-flow BTC clusters referenced in the 21-count indictment are not attached
> here. Canonical BTC-e domain btc-e.com was seized by DOJ in parallel action.

## 3. Changed-layer observations (supports the scoped claim)

### l4_frontend · attribution: `direct` · Δt = 0h

**Event label**: `canonical_domain_seized_by_DOJ_IRSCI`

**Timestamp**: `2017-07-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.justice.gov/usao-ndca/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  - Wayback: <https://web.archive.org/web/20170727013407/https://www.justice.gov/usao-ndca/pr/russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged>
  - body_hash: `sha256:2cf3684bc3a1e169adc66e01c3a615540c81a3061eedac0609422559383f0919`
  - body_path: `sources/http_captures/btc-e-doj-2017/wayback_doj_press_snapshot/web.archive.org__web-20170727013407-https-www.justice.gov-usao-ndca-pr-russian-national-and-bitcoin-exchange-charged-21-count-indictment-operating-alleged__359babd4a6.html`
  > Wayback memento of USAO-NDCA press release substantiates the
> coordinated DOJ/FBI domain seizure of btc-e.com (parallel to
> 21-count indictment unsealing). v0.3 audit 2026-05-20: source
> REPAIRED — body_path swapped to Wayback memento (78776 bytes
> real content) replacing prior Akamai-stub capture. Note: the
> press release describes the seizure operation but the specific
> btc-e.com seizure-banner page is not separately Wayback-pinned
> in this repair; the structural seizure attestation comes from
> the DOJ release content (grep-verified: 19xBTC-e + 2xdomain +
> 3xFBI), not from a per-page banner snapshot. Future enrichment
> could add a 2017-07-26..28 btc-e.com Wayback snapshot for
> gold-standard pre/post bracketing (cf. chipmixer/samourai
> patterns). attribution=direct sound: DOJ release explicitly
> names the coordinated seizure operation.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): L0 network-layer OONI API query performed 2026-04-22. Searched the
- **offramp_cex** (`not_measured`): Chain-analytics anchors pinned 2026-04-22 as primary_corporate

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a9689fa`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

