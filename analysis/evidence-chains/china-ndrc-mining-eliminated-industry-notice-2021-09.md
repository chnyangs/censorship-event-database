# Evidence chain — `china-ndrc-mining-eliminated-industry-notice-2021-09`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `75fb128` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2021-09-24 China's NDRC issued a notice ordering the cryptocurrency-mining industry
> phased out (deemed an 'outdated' industry) and its financial/investment/electricity/tax
> support channels cut. Effect carried at offramp_cex (class-level support severance, partially
> measured via captured journalism); l1_consensus hashrate effect not measured in this draft."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_NDRC`
- **Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading>
  - Wayback: <https://web.archive.org/web/20210925053628/https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading/>
  - body_hash: `sha256:b505020728a83401e6239e5abc8dffcf164838a7254c78a93d8af14abf8541a9`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary/web.archive.org__web-20210925053628-https-www.coindesk.com-policy-2021-09-24-china-tightens-crypto-mining-crackdown-bans-trading__98e697480d.html`
  > CoinDesk, 2021-09-24, "China Tightens Crypto Mining Crackdown, Bans Trading."
> Reports that China's top state-planning body, the National Development and Reform
> Commission (NDRC), posted a separate "Notice on Rectifying Virtual Currency Mining."
> The notice aims to dispose of the "hidden risks" in crypto mining as China pursues
> its carbon-neutrality goals; while it does not outlaw mining outright, it orders local
> authorities to clamp down on illegal mining and to gradually phase out the industry —
> mining is to be deemed an "outdated" industry. The captured article additionally
> documents that the same day a parallel inter-agency PBOC notice declared all crypto
> transactions illegal (that parallel action is a SEPARATE corpus event,
> china-pboc-crypto-ban-2021; this event is scoped strictly to the NDRC mining notice).
> Wayback snapshot 20210925053628 (replayable body_hash).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Chinese cryptocurrency mining enterprises + their financial/energy support channels (class)
- **Chains**: `bitcoin`

> The Chinese cryptocurrency-mining industry as a class — operators, and the financial /
> investment / electricity / tax support channels that sustain them. The NDRC notice
> directs the industry to be phased out (deemed an "outdated" industry) and orders local
> authorities to cut off support to mining enterprises. Class-level target; no enumerated
> roster of mining firms in the captured source. enumeration=subset.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `ndrc_ordered_phase_out_and_support_severance_for_mining_industry`

**Timestamp**: `2021-09-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading>
  - Wayback: <https://web.archive.org/web/20210925053628/https://www.coindesk.com/policy/2021/09/24/china-tightens-crypto-mining-crackdown-bans-trading/>
  - body_hash: `sha256:b505020728a83401e6239e5abc8dffcf164838a7254c78a93d8af14abf8541a9`
  - body_path: `sources/http_captures/china-ndrc-mining-eliminated-industry-notice-2021-09/primary/web.archive.org__web-20210925053628-https-www.coindesk.com-policy-2021-09-24-china-tightens-crypto-mining-crackdown-bans-trading__98e697480d.html`
  > CoinDesk 2021-09-24: NDRC "Notice on Rectifying Virtual Currency Mining" orders the
> industry phased out (deemed "outdated") and support channels (financial, investment,
> electricity, tax) cut. attribution=plausible (per codebook §1.5/§8.4): the anchor is
> journalism reporting the NDRC notice, not the NDRC's own Chinese-language primary
> notice text, and the target is the mining industry as a class rather than named
> enterprises. Conservative default applied.

## 5. Honest coverage gaps

- **l1_consensus** (`not_measured`): The notice's downstream effect manifests in global Bitcoin hashrate (China-hosted

## 7. Related events

- [`china-state-council-mining-crackdown-2021-05`](./china-state-council-mining-crackdown-2021-05.md)
- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `75fb128`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

