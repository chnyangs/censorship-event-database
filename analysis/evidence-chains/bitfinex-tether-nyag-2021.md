# Evidence chain — `bitfinex-tether-nyag-2021`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `a785639` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:36:40Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "The 2021-02-23 NY OAG settlement against iFinex / BFXNA / BFXWW
> and the Tether issuer entities imposes a $18.5M monetary penalty,
> a prospective prohibition on trading activity with New York
> persons or entities, and a two-year quarterly USDT reserve-
> composition reporting obligation. The row registers two
> direct-attribution observed_change observations at the offramp_cex
> layer (the NY-resident trading prohibition and the Tether
> reserve-attestation regime change). The row asserts neither
> network-layer reachability change nor any USDT addBlackList()
> on-chain action; the reserve-attestation regime is an off-chain
> disclosure obligation registered at offramp_cex on the
> Tether-as-issuer fiat-rails interface."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `US_NY_OAG`
- **Timestamp**: `2021-02-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf>
  - Wayback: <https://web.archive.org/web/20210223124635id_/https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf>
  - body_hash: `sha256:6d6e10deed411922611fb5469a24f36d17d1f3c41cd423df6705299652e935bd`
  - body_path: `sources/http_captures/bitfinex-tether-nyag-2021/primary/web.archive.org__web-20210223124635id_-https-ag.ny.gov-sites-default-files-2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf__ec36bec9cb.bin`
  > Settlement Agreement (executed 2021-02-17, publicly announced
> 2021-02-23) "In the Matter of Investigation by Letitia James,
> Attorney General of the State of New York, of iFinex Inc.,
> BFXNA Inc., BFXWW Inc., Tether Holdings Limited, Tether
> Operations Limited, Tether Limited, and Tether International
> Limited." Imposes (a) $18.5M monetary penalty payable to the
> State of New York, (b) prohibition on any further trading
> activity with New York persons or entities by Bitfinex and
> Tether, and (c) two-year quarterly reserve-composition
> reporting obligation on Tether (per-asset-class breakdown and
> loans-to-affiliates disclosure). Resolves the NY OAG inquiry
> initiated 2019-04 under New York Executive Law Section 63(12)
> and the Martin Act regarding the alleged $850M loss-coverup
> between Bitfinex and Tether. Settling parties do not admit
> wrongdoing. Marked evidence_use=contextual_unarchived because
> the authoring agent did not personally pin a Wayback snapshot
> timestamp or compute a body_hash; the ag.ny.gov PDF URL is
> stable and routinely captured by Wayback. Provisional Wayback
> anchor uses 2021 timestamp prefix pending human-audit re-pin.
- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/>
  - Wayback: <https://web.archive.org/web/2021/https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/>
  > Tether corporate response "Tether and Bitfinex reach settlement
> with New York Attorney General's Office" (2021-02-23) confirming
> the $18.5M penalty, the cessation of activity with New York
> persons, and the prospective adoption of the quarterly
> reserve-composition reporting obligation; reiterates the
> settling parties' non-admission of wrongdoing. Marked
> evidence_use=contextual_unarchived pending Wayback re-pin and
> body_hash capture during human audit.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: iFinex / BFXNA / BFXWW (Bitfinex) + Tether Holdings / Tether Operations / Tether Limited / Tether International (USDT issuer)
- **Chains**: `ethereum`, `tron`, `bitcoin`
- **Canonical domains**: `bitfinex.com`, `tether.to`

> Two enforcement-target groups consolidated into a single NY OAG
> settlement: (a) the Bitfinex operator entities iFinex Inc.,
> BFXNA Inc., and BFXWW Inc., barred from doing business with New
> York persons; and (b) the Tether issuer entities Tether Holdings
> Limited, Tether Operations Limited, Tether Limited, and Tether
> International Limited, subject to the $18.5M joint penalty, the
> NY-resident business prohibition, and a two-year quarterly
> reserve-composition reporting obligation. The row enumerates only
> the corporate-entity targets named in the settlement; it does not
> enumerate individual Bitfinex customer accounts, individual USDT
> holders, or specific on-chain USDT contract addresses. Canonical
> operator-controlled frontends are bitfinex.com (exchange) and
> tether.to (issuer transparency page).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `nyag_ordered_bitfinex_tether_ny_resident_trading_prohibition_2021`

**Timestamp**: `2021-02-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf>
  - Wayback: <https://web.archive.org/web/20210223124635id_/https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf>
  - body_hash: `sha256:6d6e10deed411922611fb5469a24f36d17d1f3c41cd423df6705299652e935bd`
  - body_path: `sources/http_captures/bitfinex-tether-nyag-2021/primary/web.archive.org__web-20210223124635id_-https-ag.ny.gov-sites-default-files-2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf__ec36bec9cb.bin`
  > NY OAG settlement agreement imposes a prospective prohibition
> on any further trading activity with New York persons or
> entities by the Bitfinex operator entities (iFinex / BFXNA /
> BFXWW) and the Tether issuer entities. attribution=direct
> because the settlement instrument itself imposes the bar.
> Bitfinex had previously implemented US-resident exit /
> geoblock at the frontend level following 2017 advisories,
> but this state-AG instrument formally pins the NY-resident
> prohibition as an admission-grade operator-state change at
> offramp_cex. Provisional Wayback anchor pending human-audit
> re-pin.
- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/>
  - Wayback: <https://web.archive.org/web/2021/https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/>
  > Tether corporate response confirming the cessation of activity
> with New York persons and the $18.5M penalty. Corroborates
> issuer-side acceptance of the NY-resident business
> prohibition. Marked evidence_use=contextual_unarchived
> pending Wayback re-pin.

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `nyag_ordered_tether_usdt_reserve_attestation_regime_change_2021`

**Timestamp**: `2021-02-23 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf>
  - Wayback: <https://web.archive.org/web/20210223124635id_/https://ag.ny.gov/sites/default/files/2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf>
  - body_hash: `sha256:6d6e10deed411922611fb5469a24f36d17d1f3c41cd423df6705299652e935bd`
  - body_path: `sources/http_captures/bitfinex-tether-nyag-2021/primary/web.archive.org__web-20210223124635id_-https-ag.ny.gov-sites-default-files-2021.02.17_-_settlement_agreement_-_execution_version.b-t_signed-c2_oag_signed.pdf__ec36bec9cb.bin`
  > Settlement imposes a two-year quarterly reserve-composition
> reporting obligation on the Tether issuer entities, requiring
> per-asset-class breakdown and loans-to-affiliates disclosure
> to be filed with NY OAG and released publicly. This is the
> regulator-compelled reserve-attestation regime change
> registered as this observation. attribution=direct because
> the settlement is the legal instrument that imposes the new
> disclosure regime against the Tether issuer entities. The
> regime predates the analogous 2021-10-15 CFTC disclosure
> regime (bitfinex-tether-cftc-2021) by ~8 months and is the
> first foundational state-AG-level USDT reserve-disclosure
> requirement. Provisional Wayback anchor pending human-audit
> re-pin.
- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/>
  - Wayback: <https://web.archive.org/web/2021/https://tether.io/news/tether-and-bitfinex-reach-settlement-with-new-york-attorney-generals-office/>
  > Tether corporate response confirming prospective adoption of
> the quarterly reserve-composition disclosure regime.
> Corroborates issuer-side acceptance of the disclosure-regime
> change. Marked evidence_use=contextual_unarchived pending
> Wayback re-pin.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`bitfinex-tether-cftc-2021`](./bitfinex-tether-cftc-2021.md)
- [`tether-retroactive-sweep-2023`](./tether-retroactive-sweep-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `a785639`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

