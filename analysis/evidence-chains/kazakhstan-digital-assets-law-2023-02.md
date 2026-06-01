# Evidence chain — `kazakhstan-digital-assets-law-2023-02`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l1_consensus`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4acc680` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T03:34:29Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2023-02-06 the President of the Republic of Kazakhstan signed
> Law No. 193-VII On Digital Assets, in force 2023-04-01, which
> introduced (i) a mandatory state cryptomining-licence and
> pool-accreditation regime and (ii) an AIFC-confined commercial
> digital-asset exchange registration regime. Both effects are
> attribution=direct from the legal text: unlicensed cryptomining on
> Kazakh territory and off-AIFC commercial exchange activity for
> Kazakh-vantage users become unlicensed from the in-force date.
> Load-bearing axes are l1_consensus (Kazakh mining substrate) and
> offramp_cex (Kazakh-vantage commercial exchange perimeter)."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `KZ_PRESIDENT`
- **Timestamp**: `2023-02-06 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://adilet.zan.kz/eng/docs/Z2300000193>
  - Wayback: <https://web.archive.org/web/2023/https://adilet.zan.kz/eng/docs/Z2300000193>
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-16** (Phase C S4
> nation-state CIS / Central-Asia discovery; lean run): authored
> by LLM agent without personally verifying Wayback / body_hash;
> origin=agent_draft and status=draft pending human review. Real
> release must replace this DRYRUN marker with a human-verified
> audit after pinning real archive anchors.
> 
> Republic of Kazakhstan Law No. 193-VII "On Digital Assets in the
> Republic of Kazakhstan" (О цифровых активах в Республике
> Казахстан), signed by President Kassym-Jomart Tokayev on
> 2023-02-06 and brought into force on 2023-04-01. The law
> establishes a state-licensed cryptomining regime (mandatory
> license for digital-mining operators, accreditation for digital
> mining pools, separate registration of hardware / software
> systems) and confines commercial issuance and circulation of
> unsecured digital assets to licensed exchanges within the Astana
> International Financial Centre (AIFC) jurisdiction; off-AIFC
> commercial exchange activity inside Kazakhstan becomes
> unlicensed. The companion act Law No. 194-VII (signed the same
> day) introduces electricity-supply rules and quotas for digital
> miners.
- **`supporting_journalism`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/>
  - Wayback: <https://web.archive.org/web/2023/https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/>
  > US Library of Congress Global Legal Monitor (2023-04-30) summary
> of Law No. 193-VII confirming signing on 2023-02-06 and in-force
> date 2023-04-01, and describing the mandatory mining-licence
> regime and AIFC-confined exchange-registration regime. DRYRUN:
> Wayback anchor unverified by LLM agent at authoring time.
- **`supporting_journalism`**
  - URL: <https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  - Wayback: <https://web.archive.org/web/2023/https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  > Morgan Lewis legal advisory (2023-02) describing the Digital
> Assets Law as a mandatory-licensing regime for mining and for
> commercial digital-asset exchange activity, with offshore /
> non-AIFC exchange services to Kazakh users falling outside the
> permitted perimeter. DRYRUN: Wayback anchor unverified.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Republic of Kazakhstan — Law No. 193-VII On Digital Assets
- **Canonical domains**: `aifc.kz`, `adilet.zan.kz`

> Class-level target: (a) unlicensed cryptomining operators inside
> Kazakhstan, and (b) commercial digital-asset exchange services
> operating outside the AIFC jurisdiction for Kazakh-vantage users.
> Subset rather than complete because the law's enforcement reach is
> formally limited to the territory of Kazakhstan and to entities
> that touch the Kazakh perimeter (mining infrastructure on Kazakh
> soil, or exchanges actively soliciting Kazakh customers); offshore
> CEX surfaces are reachable in practice via consumer-side
> circumvention (VPNs, peer-to-peer trades) and are not enumerated
> address-by-address.

## 3. Changed-layer observations (supports the scoped claim)

### l1_consensus · attribution: `plausible` · Δt = 1320h

**Event label**: `mandatory_mining_license_and_pool_accreditation_regime_in_force`

**Timestamp**: `2023-04-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://adilet.zan.kz/eng/docs/Z2300000193>
  - Wayback: <https://web.archive.org/web/2023/https://adilet.zan.kz/eng/docs/Z2300000193>
  > Adilet (Republican Center of Legal Information) authoritative
> English-language text of Law No. 193-VII. observation_kind=
> observed_change at l1_consensus because the law makes the
> underlying physical-substrate activity (cryptomining on
> Kazakh territory) conditional on a new state licensing /
> pool-accreditation regime that did not exist before the
> in-force date 2023-04-01. attribution=direct: the law itself
> is the change in the licensing regime; no inference step
> beyond reading the statute. DRYRUN: Wayback anchor unverified
> by LLM agent at authoring time.
- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/>
  - Wayback: <https://web.archive.org/web/20230501140021/https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/>
  - body_hash: `sha256:f9ad5f2a0639cae226f2daf8d349f871611fc84f68334e9f976cebebe59e1ad7`
  - body_path: `sources/http_captures/kazakhstan-digital-assets-law-2023-02/primary/web.archive.org__web-20230501140021-https-www.loc.gov-item-global-legal-monitor-2023-04-30-kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptom__eceb3c6808.html`
  > US Library of Congress Global Legal Monitor independent
> summary of the licensing / pool-accreditation regime.
> Semi-primary anchor 1 of 2. Wayback memento 20230501140021.
- **`semi_primary_wayback`**
  - URL: <https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  - Wayback: <https://web.archive.org/web/20230222214013/https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  - body_hash: `sha256:1df53b9ae33db13e151ecaf73c34602c7ccc47c51513c7814970f069fa5b9413`
  - body_path: `sources/http_captures/kazakhstan-digital-assets-law-2023-02/primary/web.archive.org__web-20230222214013-https-www.morganlewis.com-pubs-2023-02-kazakhstan-introduces-new-regulation-of-digital-assets__60e84f286f.html`
  > Morgan Lewis legal analysis of Kazakhstan Law 193-VII digital-
> assets regulation. Semi-primary anchor 2 of 2.

### offramp_cex · attribution: `plausible` · Δt = 1320h

**Event label**: `commercial_digital_asset_exchange_activity_confined_to_aifc_licensed_perimeter`

**Timestamp**: `2023-04-01 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://adilet.zan.kz/eng/docs/Z2300000193>
  - Wayback: <https://web.archive.org/web/2023/https://adilet.zan.kz/eng/docs/Z2300000193>
  > Adilet authoritative English-language text of Law No. 193-VII.
> observation_kind=observed_change at offramp_cex because the
> law restricts commercial issuance and circulation of
> unsecured digital assets (including exchange services) to
> AIFC-licensed entities, making prior non-AIFC commercial
> exchange activity for Kazakh-vantage users unlicensed from
> 2023-04-01. attribution=direct on the same legal-text basis.
> DRYRUN: Wayback anchor unverified.
- **`supporting_journalism`**
  - URL: <https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  - Wayback: <https://web.archive.org/web/2023/https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  > Morgan Lewis legal advisory (2023-02) corroborating the
> AIFC-confined commercial-exchange perimeter and the
> implication for offshore CEX activity serving Kazakh users.
> DRYRUN: Wayback anchor unverified.
- **`semi_primary_wayback`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/>
  - Wayback: <https://web.archive.org/web/20230501140021/https://www.loc.gov/item/global-legal-monitor/2023-04-30/kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptomining/>
  - body_hash: `sha256:f9ad5f2a0639cae226f2daf8d349f871611fc84f68334e9f976cebebe59e1ad7`
  - body_path: `sources/http_captures/kazakhstan-digital-assets-law-2023-02/primary/web.archive.org__web-20230501140021-https-www.loc.gov-item-global-legal-monitor-2023-04-30-kazakhstan-new-law-establishes-legal-framework-for-digital-assets-and-cryptom__eceb3c6808.html`
  > LoC Global Legal Monitor summary of the AIFC-confined exchange
> perimeter. Semi-primary anchor 1 of 2.
- **`semi_primary_wayback`**
  - URL: <https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  - Wayback: <https://web.archive.org/web/20230222214013/https://www.morganlewis.com/pubs/2023/02/kazakhstan-introduces-new-regulation-of-digital-assets>
  - body_hash: `sha256:1df53b9ae33db13e151ecaf73c34602c7ccc47c51513c7814970f069fa5b9413`
  - body_path: `sources/http_captures/kazakhstan-digital-assets-law-2023-02/primary/web.archive.org__web-20230222214013-https-www.morganlewis.com-pubs-2023-02-kazakhstan-introduces-new-regulation-of-digital-assets__60e84f286f.html`
  > Morgan Lewis analysis confirming commercial digital-asset
> exchange activity confined to AIFC-licensed perimeter.
> Semi-primary anchor 2 of 2.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): The law's exchange-registration regime conditions commercial

## 7. Related events

- [`kazakhstan-internet-shutdown-mining-2022-01`](./kazakhstan-internet-shutdown-mining-2022-01.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4acc680`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

