# Evidence chain — `taiwan-fsc-aml-vasp-regime-2021-2024`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `b524247` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2024-07-31 Taiwan amended its Money Laundering Control Act to add Article 6,
> establishing a mandatory FSC AML-registration regime under which VASPs that
> have not completed registration may not provide virtual asset services and
> violators face criminal penalties (FSC implementing regulations effective
> 2024-11-30), building on the 2021-07-01 AML compliance-declaration regime.
> This created a binding domestic VASP-registration perimeter at offramp_cex; no
> admission-grade per-event cascade is pinned in this DRYRUN draft, coded
> null_event pending human audit."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `TW_FSC`
- **Timestamp**: `2024-07-31 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2024-11-17/taiwan-money-laundering-control-act-revised/>
  - Wayback: <https://web.archive.org/web/20241127044221/https://www.loc.gov/item/global-legal-monitor/2024-11-17/taiwan-money-laundering-control-act-revised/>
  - body_hash: `sha256:656925a31719529c22ffeeed1d66a1baf078e2a2a5b3d256e26761ce84687882`
  - body_path: `sources/http_captures/taiwan-fsc-aml-vasp-regime-2021-2024/primary/web.archive.org__web-20241201000000-https-www.loc.gov-item-global-legal-monitor-2024-11-17-taiwan-money-laundering-control-act-revised__3a376f6636.html`
  > US Library of Congress Global Legal Monitor (2024-11-17), "Taiwan: Money
> Laundering Control Act Revised." Captured HTML grep-confirms: "On July
> 31, 2024, Taiwan's Money Laundering Control Act (MLCA) was amended. Key
> modifications ... include adjusted penalties and the establishment of a
> registration regime for virtual asset service providers (VASPs)";
> "VASPs that have not completed the registration are not allowed to
> provide virtual asset services. Violation of article 6 by natural
> persons will result in imprisonment to a maximum of two years or
> detention, and/or fines up to NT$5 million." This is the load-bearing
> mandate: a binding registration gate (no FSC AML registration → may not
> operate) backed by criminal penalty, administered by the Financial
> Supervisory Commission (FSC). Wayback memento 20241127044221 captured
> 2026-05-31.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Taiwan — FSC mandatory VASP AML-registration regime (MLCA Art. 6)

> Class-level target: all businesses and individuals providing virtual asset
> services in Taiwan (domestic VASPs and foreign VASPs serving Taiwan, the
> latter required to incorporate a Taiwan company/branch). The MLCA Article 6
> regime operates against the VASP activity class rather than enumerating
> named operators; coded subset with class-level rationale per codebook §7.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `vasp_mandatory_registration_regime_enacted_no_admission_grade_cascade_observed`

**Window**: `2024-07-31 00:00:00+00:00` → `2026-05-31 00:00:00+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://www.loc.gov/item/global-legal-monitor/2024-11-17/taiwan-money-laundering-control-act-revised/>
  - Wayback: <https://web.archive.org/web/20241127044221/https://www.loc.gov/item/global-legal-monitor/2024-11-17/taiwan-money-laundering-control-act-revised/>
  - body_hash: `sha256:656925a31719529c22ffeeed1d66a1baf078e2a2a5b3d256e26761ce84687882`
  - body_path: `sources/http_captures/taiwan-fsc-aml-vasp-regime-2021-2024/primary/web.archive.org__web-20241201000000-https-www.loc.gov-item-global-legal-monitor-2024-11-17-taiwan-money-laundering-control-act-revised__3a376f6636.html`
  > LOC Global Legal Monitor describing the MLCA Art. 6 mandatory VASP
> registration regime (no registration → may not operate; criminal
> penalty). observation_kind=observed_no_change at offramp_cex: the
> framework creates a binding registration perimeter but no admission-
> grade per-event cascade (named-VASP retreat / onboarding halt tied to
> the 2024-07-31 trigger) has been pinned in this draft.
> attribution=none consistent with §1.1 (reserved for observed_no_change
> rows). Wayback memento 20241127044221 captured 2026-05-31.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Frontend-layer effects (unregistered-VASP geo-restrictions / exits from

## 7. Related events

- [`uzbekistan-napp-vasp-licensing-2022-07`](./uzbekistan-napp-vasp-licensing-2022-07.md)
- [`turkey-cmb-casp-licensing-law-7518-2024`](./turkey-cmb-casp-licensing-law-7518-2024.md)
- [`fatf-r15-vasp-travel-rule-2019`](./fatf-r15-vasp-travel-rule-2019.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `b524247`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

