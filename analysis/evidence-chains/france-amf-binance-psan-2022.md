# Evidence chain — `france-amf-binance-psan-2022`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `null_event` (0 changed layer(s): none) · **Tier**: `null_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `292f041` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-21` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T10:47:34Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "France AMF granted Binance France SAS a PSAN (Digital Asset Service
> Provider) registration (E2022-037) effective 2022-05-04, authorizing
> four regulated services (custody, fiat purchase/sale, crypto-crypto
> exchange, trading-platform operation). This was the first major
> Western jurisdiction to formally register a Binance entity and serves
> as the permissive counter-example to the UK-FCA-2021 GBP-rail severance
> and DE-BaFin-2023 licence withdrawal in the 2021-2023 Binance EU/UK
> regulator wave. Recorded as a null_event denominator-control row at
> offramp_cex with attribution=none."

## 1. Trigger

- **Type**: `regulatory_enforcement`
- **Actor**: `FR_AMF`
- **Timestamp**: `2022-05-04 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_government`**
  - URL: <https://www.amf-france.org/en/warnings/white-lists/daspcasp/binance-france-sas>
  - body_hash: `sha256:7151127edae427d38cbeb3b117120c85f45dc84637b6be50d88270b8cd21c15c`
  - body_path: `sources/http_captures/france-amf-binance-psan-2022/primary/www.amf-france.org__en-warnings-white-lists-daspcasp-binance-france-sas__1cb688d206.html`
  > AMF (Autorité des Marchés Financiers) public white-list entry for
> Binance France SAS, registered as a Prestataire de Services sur
> Actifs Numériques (PSAN) / Digital Asset Service Provider (DASP)
> under registration number E2022-037, effective 2022-05-04. The
> registration authorizes four regulated services: digital-asset
> custody; purchase/sale of digital assets for legal tender;
> exchange of digital assets for other digital assets; and
> operation of a digital-asset trading platform. This is a
> PERMISSIVE regulatory recognition (counter-example to
> enforcement-driven cascades), not a censorship trigger. DRYRUN:
> Wayback URL pattern asserted; body-hash capture deferred.
- **`semi_primary_wayback`**
  - URL: <https://siecledigital.fr/2022/05/05/binance-enfin-reconnu-psan-en-france/>
  - Wayback: <https://web.archive.org/web/20220505091331/https://siecledigital.fr/2022/05/05/binance-enfin-reconnu-psan-en-france/>
  - body_hash: `sha256:fa06586b35a3e6ad8c46b309cbbc2236674e29aae57c85a3df9a10c7f27940bc`
  - body_path: `sources/http_captures/france-amf-binance-psan-2022/primary/web.archive.org__web-20220505091331-https-siecledigital.fr-2022-05-05-binance-enfin-reconnu-psan-en-france__85c0e78c4b.html`
  > Siècle Digital (2022-05-05) "Binance enfin reconnu PSAN en France"
> confirms the 2022-05-04 AMF registration of Binance France SAS
> as the first major Western jurisdiction PSAN/DASP authorization
> granted to Binance. Contemporaneous press confirmation of the
> registration date.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance France SAS
- **Canonical domains**: `binance.com`

> Binance France SAS (the French legal entity of the Binance group,
> established in Montrouge in November 2021) is the registered PSAN.
> Operational effect extends, by class-level inference, to French
> retail customers of binance.com obtaining a regulated on-ramp via
> the registered French entity. Treated as entity-level at the
> Binance-France cohort; class-level rationale documented here per
> codebook §7.

## 3. Changed-layer observations (supports the scoped claim)

*No observed_change entries. This is a `null_event`; see §4 for observed_no_change evidence supporting the null claim.*

## 4. No-change observations (where applicable)

### offramp_cex — `binance_france_sas_psan_registered_no_rail_severance`

**Window**: `2022-05-04 00:00:00+00:00` → `2023-12-31 23:59:59+00:00`

**Sources**:

- **`primary_government`**
  - URL: <https://www.amf-france.org/en/warnings/white-lists/daspcasp/binance-france-sas>
  - body_hash: `sha256:7151127edae427d38cbeb3b117120c85f45dc84637b6be50d88270b8cd21c15c`
  - body_path: `sources/http_captures/france-amf-binance-psan-2022/primary/www.amf-france.org__en-warnings-white-lists-daspcasp-binance-france-sas__1cb688d206.html`
  > AMF white-list entry: Binance France SAS PSAN registration
> E2022-037 effective 2022-05-04. Affirmatively authorizes
> (does not restrict) Binance's French offramp_cex operations.
> observed_no_change row anchors the null-event status of this
> permissive regulatory recognition.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): No new geo-fence or restriction observed on binance.com in France

## 7. Related events

- [`uk-fca-binance-markets-2021`](./uk-fca-binance-markets-2021.md)
- [`germany-bafin-binance-licence-withdrawal-2023`](./germany-bafin-binance-licence-withdrawal-2023.md)
- [`eu-mica-2023`](./eu-mica-2023.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `292f041`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

