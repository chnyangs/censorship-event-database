# Evidence chain — `iran-government-mining-electricity-restriction-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `l1_consensus`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `e43eea7` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> *(no scoped_claim recorded — event not paper-ready)*

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `IR_TAVANIR`
- **Timestamp**: `2021-05-22 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.mehrnews.com/news/5217539/%D9%85%D8%B1%D8%A7%DA%A9%D8%B2-%D9%85%D8%AC%D8%A7%D8%B2-%D8%A7%D8%B3%D8%AA%D8%AE%D8%B1%D8%A7%D8%AC-%D8%B1%D9%85%D8%B2-%D8%A7%D8%B1%D8%B2-%D8%A7%D8%B2-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%D8%AE%D8%A7%D9%85%D9%88%D8%B4-%D9%85%DB%8C-%D8%B4%D9%88%D9%86%D8%AF>
  - body_hash: `sha256:793a9ff99ea47395e6279ac1c10dfcfd43947ba505d808b80dfc86dc38e9cf47`
  - body_path: `sources/http_captures/iran-government-mining-electricity-restriction-2021/v0_3_primary_repair/www.mehrnews.com__news-5217539-D9-85-D8-B1-D8-A7-DA-A9-D8-B2--D9-85-D8-AC-D8-A7-D8-B2--D8-A7-D8-B3-D8-AA-D8-AE-D8-B1-D8-A7-D8-AC--D8-B1-D9-85-D8-B2--D8-A7-D8-B1-D8-B2__0d4b151a2c.html`
  > Persian-language Mehr News Agency report dated 2021-05-22
> citing Tavanir / Iran electricity-industry spokesperson
> Mostafa Rajabi Mashhadi. The report states that licensed
> cryptocurrency-mining centers would be switched off from
> 2021-05-22 to reduce peak load and prevent power outages,
> and gives the licensed-center consumption figure as roughly
> 300 MW. This is state-media reporting of the Tavanir
> operational order rather than a first-party Tavanir-domain
> page; retained as primary_government for pre-human source
> repair and left for human audit to confirm the Persian
> original and source tier.
- **`supporting_journalism`**
  - URL: <https://www.cnbc.com/2021/05/26/iran-bans-bitcoin-mining-as-its-cities-suffer-blackouts.html>
  - Wayback: <https://web.archive.org/web/2021/https://www.cnbc.com/2021/05/26/iran-bans-bitcoin-mining-as-its-cities-suffer-blackouts.html>
  > CNBC contemporaneous reporting of President Rouhani's 2021-05-26
> announcement of a four-month (May–September 2021) ban on all
> cryptocurrency mining in Iran, including the 50 licensed mining
> farms operated under Tavanir (Iran Power Generation, Distribution
> and Transmission Company) authorization. Rationale: relieve summer
> electricity shortages causing rolling blackouts in major Iranian
> cities. DRYRUN: wayback stub pending body_hash + body_path capture.
- **`supporting_journalism`**
  - URL: <https://www.aljazeera.com/economy/2021/5/26/iran-bans-all-crypto-mining-after-summer-power-cuts-strike>
  - Wayback: <https://web.archive.org/web/2021/https://www.aljazeera.com/economy/2021/5/26/iran-bans-all-crypto-mining-after-summer-power-cuts-strike>
  > Al Jazeera coverage corroborating the 2021-05-26 ban announcement
> and the Tavanir / Ministry of Energy enforcement role. Notes that
> the order required licensed bitcoin miners to halt operations
> until 2021-09-22, with Tavanir conducting enforcement raids on
> unlicensed operations. DRYRUN: wayback stub.
- **`supporting_journalism`**
  - URL: <https://fortune.com/2021/05/27/iran-ban-crypto-mining-bitcoin-blackout-energy-use/>
  - Wayback: <https://web.archive.org/web/2021/https://fortune.com/2021/05/27/iran-ban-crypto-mining-bitcoin-blackout-energy-use/>
  > Fortune coverage of the Rouhani / Tavanir mining ban, noting that
> licensed mining farms consumed approximately 209 megawatts of
> power at the time of the order. DRYRUN: wayback stub.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Iranian Tavanir-licensed bitcoin mining farms (class)
- **Chains**: `bitcoin`

> Licensed Iranian bitcoin mining operations as a regulated class — 50
> Tavanir-authorized mining farms consuming approximately 209 MW at the
> time of the order. The ban also targeted unlicensed mining as an
> enforcement priority, but the formal halt order operates against the
> Tavanir-licensed population. Per-farm enumeration not captured in the
> public order text; class-level subset coded per codebook §7.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `direct` · Δt = 0h

**Event label**: `licensed_bitcoin_mining_operations_halted_summer_2021`

**Timestamp**: `2021-05-22 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_government`**
  - URL: <https://www.mehrnews.com/news/5217539/%D9%85%D8%B1%D8%A7%DA%A9%D8%B2-%D9%85%D8%AC%D8%A7%D8%B2-%D8%A7%D8%B3%D8%AA%D8%AE%D8%B1%D8%A7%D8%AC-%D8%B1%D9%85%D8%B2-%D8%A7%D8%B1%D8%B2-%D8%A7%D8%B2-%D8%A7%D9%85%D8%B1%D9%88%D8%B2-%D8%AE%D8%A7%D9%85%D9%88%D8%B4-%D9%85%DB%8C-%D8%B4%D9%88%D9%86%D8%AF>
  - body_hash: `sha256:793a9ff99ea47395e6279ac1c10dfcfd43947ba505d808b80dfc86dc38e9cf47`
  - body_path: `sources/http_captures/iran-government-mining-electricity-restriction-2021/v0_3_primary_repair/www.mehrnews.com__news-5217539-D9-85-D8-B1-D8-A7-DA-A9-D8-B2--D9-85-D8-AC-D8-A7-D8-B2--D8-A7-D8-B3-D8-AA-D8-AE-D8-B1-D8-A7-D8-AC--D8-B1-D9-85-D8-B2--D8-A7-D8-B1-D8-B2__0d4b151a2c.html`
  > Persian state-media report citing Tavanir / Iran electricity-
> industry spokesperson Mostafa Rajabi Mashhadi that licensed
> cryptocurrency-mining centers would be switched off from
> 2021-05-22 to reduce peak-load pressure and prevent outages.
> This source directly supports the licensed-mining-farm halt
> observation. Because it is not a Tavanir-domain notice, the
> source-tier assignment remains explicit for human audit.
- **`semi_primary_wayback`**
  - URL: <https://www.cnbc.com/2021/05/26/iran-bans-bitcoin-mining-as-its-cities-suffer-blackouts.html>
  - Wayback: <https://web.archive.org/web/20210526183037/https://www.cnbc.com/2021/05/26/iran-bans-bitcoin-mining-as-its-cities-suffer-blackouts.html>
  - body_hash: `sha256:e392e6b7974f570c3e77480cfffa0b115c692b63c3a2771c8d1b92b7d5311970`
  - body_path: `sources/http_captures/iran-government-mining-electricity-restriction-2021/primary/web.archive.org__web-20210526183037-https-www.cnbc.com-2021-05-26-iran-bans-bitcoin-mining-as-its-cities-suffer-blackouts.html__07cd9a0f9c.html`
  > CNBC reporting on Rouhani's 2021-05-26 four-month ban on all
> cryptocurrency mining, with Tavanir enforcing the halt order
> on 50 licensed mining farms. attribution=direct because the
> Iranian government / Tavanir publicly references the action
> and names the licensed-mining-farm class as the target
> population (codebook §1.5 boundary for nation-state
> administrative orders citing the regulated class). DRYRUN:
> wayback stub pending body_hash + body_path capture.
- **`semi_primary_wayback`**
  - URL: <https://www.aljazeera.com/economy/2021/5/26/iran-bans-all-crypto-mining-after-summer-power-cuts-strike>
  - Wayback: <https://web.archive.org/web/20210526161935/https://www.aljazeera.com/economy/2021/5/26/iran-bans-all-crypto-mining-after-summer-power-cuts-strike>
  - body_hash: `sha256:4a6748eff98e547d62f1348ca19a967c0de6fa0349304aeafdf17a303d1f8931`
  - body_path: `sources/http_captures/iran-government-mining-electricity-restriction-2021/primary/web.archive.org__web-20210526161935-https-www.aljazeera.com-economy-2021-5-26-iran-bans-all-crypto-mining-after-summer-power-cuts-strike__c2b50ffa73.html`
  > Al Jazeera contemporaneous reporting corroborates the
> 2021-05-26 ban scope, Tavanir's enforcement role, and the
> 2021-09-22 ban-window endpoint. DRYRUN: wayback stub.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`iran-ransomware-ofac-2018`](./iran-ransomware-ofac-2018.md)
- [`iran-cbi-crypto-banking-prohibition-2018`](./iran-cbi-crypto-banking-prohibition-2018.md)
- [`china-sichuan-mining-ban-2021-06`](./china-sichuan-mining-ban-2021-06.md)
- [`kazakhstan-internet-shutdown-mining-2022-01`](./kazakhstan-internet-shutdown-mining-2022-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `e43eea7`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

