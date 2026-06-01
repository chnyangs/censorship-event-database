# Evidence chain — `uzbekistan-napp-vasp-licensing-2022-07`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4b6ca9a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T01:54:35Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2022-07-14 the Director of the National Agency of Perspective
> Projects of the Republic of Uzbekistan (NAPP) signed Order No. 32
> approving the Regulations on the procedure of licensing the
> activities of service providers in the crypto-assets turnover
> sphere (MoJ registration No. 3380 of 2022-08-15), establishing a
> mandatory domestic licensing perimeter for crypto-exchanges,
> crypto-depositories, crypto-stores, and mining pools restricted to
> Uzbek-resident legal entities. No admission-grade per-event cascade
> is pinned in this DRYRUN draft; coded null_event pending human
> audit of the offramp_cex perimeter effects."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `UZ_NAPP`
- **Timestamp**: `2022-07-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://napp.uz/en/pages/service-providers>
  - Wayback: <https://web.archive.org/web/20230320220554/https://napp.uz/en/pages/service-providers>
  - body_hash: `sha256:d6ded0214e6373a3164f2d5a40f589f95c91e5b1a130b4aee8002a16f305a386`
  - body_path: `sources/http_captures/uzbekistan-napp-vasp-licensing-2022-07/primary/web.archive.org__web-20230320220554-https-napp.uz-en-pages-service-providers__dbe062377c.html`
  > **NEW EVENT AUTHORED — DRYRUN 2026-05-17** (Wave 2.3 P2 sweep,
> S4 nation-state Central-Asia VASP-licensing discovery): authored
> by LLM agent without personally verifying Wayback / body_hash;
> origin=agent_draft and status=draft pending human review. Real
> release must replace this DRYRUN marker with a human-verified
> audit after pinning real archive anchors.
> 
> Order of the Director of the National Agency of Perspective
> Projects of the Republic of Uzbekistan (NAPP) No. 32 dated
> 2022-07-14, approving the Regulations on the procedure of
> licensing the activities of service providers in the
> crypto-assets turnover sphere (Ministry of Justice registration
> No. 3380 of 2022-08-15). The Regulations establish a mandatory
> state licensing regime for crypto-asset service providers
> (including crypto-exchanges, crypto-depositories, crypto-stores,
> and mining pools), restrict licensure to legal entities
> resident in Uzbekistan, and set a state-fee schedule (e.g.
> crypto-exchange license at 73,400 BCV multiples).
- **`semi_primary_wayback`**
  - URL: <https://manimama.eu/license-for-virtual-assets-service-providers-in-uzbekistan-prospects-for-crypto-business/>
  - Wayback: <https://web.archive.org/web/20231129050624/https://manimama.eu/license-for-virtual-assets-service-providers-in-uzbekistan-prospects-for-crypto-business/>
  - body_hash: `sha256:2936b2f7bb05390290b750e8aab384574d3a9b0d1028f72ed1d8eaec5d0439be`
  - body_path: `sources/http_captures/uzbekistan-napp-vasp-licensing-2022-07/primary/web.archive.org__web-20231129050624-https-manimama.eu-license-for-virtual-assets-service-providers-in-uzbekistan-prospects-for-crypto-business__62dcb5e029.html`
  > Manimama legal advisory describing the NAPP Order No. 32 of
> 2022-07-14 framework: Uzbek-resident legal-entity eligibility,
> state-fee schedule for crypto-exchange / crypto-depository /
> crypto-store / mining-pool licences, and NAPP as the sole
> licensing authority. DRYRUN: Wayback anchor unverified.
- **`supporting_journalism`**
  - URL: <https://www.lexology.com/library/detail.aspx?g=91e869a9-e800-455a-aa60-52d50e3d6c87>
  - Wayback: <https://web.archive.org/web/2022/https://www.lexology.com/library/detail.aspx?g=91e869a9-e800-455a-aa60-52d50e3d6c87>
  > Lexology legal note "Regulation and Licensing of Crypto
> Custodians: Uzbek perspective" describing NAPP as the regulator
> responsible for licensing crypto-asset service providers under
> the 2022 framework. DRYRUN: Wayback anchor unverified.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Republic of Uzbekistan — NAPP Order No. 32 (VASP licensing framework)
- **Canonical domains**: `napp.uz`

> Class-level target: crypto-asset service providers operating in
> or soliciting customers from Uzbekistan, comprising (a)
> crypto-exchanges, (b) crypto-depositories, (c) crypto-stores
> (over-the-counter retail), and (d) crypto-mining pools. Subset
> rather than complete because the framework's enforcement reach is
> territorially confined to Uzbekistan and to Uzbek-resident legal
> entities; offshore CEX surfaces remain reachable via consumer-side
> circumvention and are not enumerated address-by-address.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `vasp_licensing_framework_promulgated_no_admission_grade_cascade_observed`

**Window**: `2022-07-14 00:00:00+00:00` → `2026-05-17 00:00:00+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://napp.uz/en/pages/service-providers>
  - Wayback: <https://web.archive.org/web/20230320220554/https://napp.uz/en/pages/service-providers>
  - body_hash: `sha256:d6ded0214e6373a3164f2d5a40f589f95c91e5b1a130b4aee8002a16f305a386`
  - body_path: `sources/http_captures/uzbekistan-napp-vasp-licensing-2022-07/primary/web.archive.org__web-20230320220554-https-napp.uz-en-pages-service-providers__dbe062377c.html`
  > NAPP service-providers landing page describing the Order
> No. 32 (2022-07-14) framework. observation_kind=
> observed_no_change at offramp_cex: the framework creates a
> domestic licensing perimeter but no admission-grade per-event
> cascade (offshore CEX retreat, named-licensee onboarding tied
> to this trigger, address-set effects) has been pinned in this
> audit. attribution=none consistent with §1.1 (reserved
> for observed_no_change rows). Wayback memento 20230320220554
> captured 2026-05-21.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Frontend-layer observable effects (e.g. offshore CEX consumer-

## 7. Related events

- [`kazakhstan-digital-assets-law-2023-02`](./kazakhstan-digital-assets-law-2023-02.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4b6ca9a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

