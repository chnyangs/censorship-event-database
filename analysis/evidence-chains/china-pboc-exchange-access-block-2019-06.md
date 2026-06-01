# Evidence chain — `china-pboc-exchange-access-block-2019-06`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `8dbd685` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2019-11-14 the PBOC Shanghai Bureau ordered district regulators to probe and rectify
> local cryptocurrency trading/promotion services and overseas-ICO distributors, a 2019
> re-enforcement of China's 2017 exchange/ICO ban. Effect carried at offramp_cex
> (class-level, partially measured); no replayable L0 measurement captured."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC_SHANGHAI`
- **Timestamp**: `2019-11-14 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20191126000000/https://technode.com/2019/11/25/chinas-regulators-launch-all-around-crackdown-on-cryptocurrency/>
  - Wayback: <https://web.archive.org/web/20191128215110/https://technode.com/2019/11/25/chinas-regulators-launch-all-around-crackdown-on-cryptocurrency/>
  - body_hash: `sha256:a037751523e22bd2292daa22aacfa2b359fe8d39880f39f2b2474b8351155227`
  - body_path: `sources/http_captures/china-pboc-exchange-access-block-2019-06/primary/web.archive.org__web-20191126000000-https-technode.com-2019-11-25-chinas-regulators-launch-all-around-crackdown-on-cryptocurrency__300169d4f1.html`
  > PBOC Shanghai issued a notice on 2019-11-14 ordering regulators in each district
> of Shanghai to thoroughly probe local cryptocurrency-related services and entities
> promoting/distributing tokens from overseas ICOs, as part of an "all-around"
> crackdown campaign led by China's internet-financial-risk rectification group
> (Beijing Youth Daily / state media reporting). The campaign re-enforced the 2017
> exchange/ICO ban against venues and services that had resurged. Captured via
> TechNode (Wayback memento 2019-11-28).

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Shanghai-district crypto trading/promotion services + overseas-ICO promoters (class)

> Local Shanghai-district cryptocurrency-related service providers and overseas-ICO
> token promoters/distributors as a class. The PBOC Shanghai notice ordered district
> regulators to probe and rectify these services; no specific exchange is named in the
> reporting (class-level target).

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = 0h

**Event label**: `pboc_shanghai_ordered_probe_rectification_of_local_crypto_services`

**Timestamp**: `2019-11-14 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`supporting_journalism`**
  - URL: <https://web.archive.org/web/20191126000000/https://technode.com/2019/11/25/chinas-regulators-launch-all-around-crackdown-on-cryptocurrency/>
  - body_hash: `sha256:a037751523e22bd2292daa22aacfa2b359fe8d39880f39f2b2474b8351155227`
  - body_path: `sources/http_captures/china-pboc-exchange-access-block-2019-06/primary/web.archive.org__web-20191126000000-https-technode.com-2019-11-25-chinas-regulators-launch-all-around-crackdown-on-cryptocurrency__300169d4f1.html`
  > attribution=plausible (not direct): the strong source is journalism reporting
> the PBOC Shanghai notice, not the primary Chinese-language notice text, and the
> notice orders a probe/rectification of local services as a class rather than
> naming specific exchanges. Conservative coding per codebook §8.4.

## 5. Honest coverage gaps

- **l0_network** (`not_measured`): Candidate framed this as a Great-Firewall website-access block (June 2019 PBOC

## 7. Related events

- [`china-pboc-exchange-shutdown-2017-09`](./china-pboc-exchange-shutdown-2017-09.md)
- [`china-ico-ban-2017-09`](./china-ico-ban-2017-09.md)
- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `8dbd685`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

