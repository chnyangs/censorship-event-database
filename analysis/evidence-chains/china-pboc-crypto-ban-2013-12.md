# Evidence chain — `china-pboc-crypto-ban-2013-12`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `0b7e0bd` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T09:13:36Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2013-12-05, PBOC, MIIT, CBRC, CSRC, and CIRC issued Notice
> 银发〔2013〕289号, prohibiting PRC financial institutions and payment
> institutions from providing Bitcoin-related services. In this dataset the
> row is a one-layer historical-baseline S4 offramp_cex/payment-rail
> observed_change with attribution=direct, anchored in captured official
> PBOC/MIIT artifacts. It does not claim ISP blocking, consensus-layer
> effects, RPC-provider filtering, issuer asset freezes, or a separately
> measured exchange-frontend/CNY-deposit cascade."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `CN_PBOC`
- **Timestamp**: `2013-12-05 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_legal`**
  - URL: <https://www.pbc.gov.cn/tiaofasi/144941/3581332/3587306/index.html>
  - body_hash: `sha256:054dce6a61ceda31c3438ee10b9c81da2eb42c05bf487d319273b32a96c8d3a0`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2013-12/primary/www.pbc.gov.cn__tiaofasi-144941-3581332-3587306-index.html__ae42a4eb2c.html`
  > People's Bank of China official notice landing page for Notice
> 银发〔2013〕289号, naming PBOC, MIIT, CBRC, CSRC, and CIRC as
> issuing authorities and linking the official notice PDF.
> Captured locally after the legacy pbc.gov.cn path had drifted.
- **`primary_legal`**
  - URL: <https://www.pbc.gov.cn/tiaofasi/fileDir/resource/cms/2018/07/2018072615002921168.pdf>
  - body_hash: `sha256:5522c48edcffc33d96c13d41d44cfe8dfd0791c211ed93885e188a3bc15a1b9b`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2013-12/primary/www.pbc.gov.cn__tiaofasi-fileDir-resource-cms-2018-07-2018072615002921168.pdf__7180e9bb41.bin`
  > Official PBOC-hosted PDF attachment for Notice 银发〔2013〕289号.
> This is the primary legal artifact for the five-ministry notice.
- **`primary_legal`**
  - URL: <https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2013/art_d7241872221f43708e47fd30ac30eac0.html>
  - body_hash: `sha256:fd834ddbf817a7e65d70ba0e13e2ee1695dbd039e09918e1e1eee4d348c1c70a`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2013-12/primary/www.miit.gov.cn__zwgk-zcwj-wjfb-tz-art-2013-art_d7241872221f43708e47fd30ac30eac0.html__a2558c2094.html`
  > MIIT official full-text reproduction of the five-ministry notice.
> The captured body includes the operative section requiring financial
> institutions and payment institutions not to conduct Bitcoin-related
> business.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Protocol**: `bitcoin`
- **Actor name**: PRC financial institutions and payment institutions
- **Chains**: `bitcoin`

> The retained target is the regulated PRC financial-institution and
> payment-institution class covered by Notice 银发〔2013〕289号. The notice
> also imposed filing/AML obligations on Bitcoin trading websites, but
> this repaired row does not use exchange-side CNY-deposit pauses as the
> load-bearing observation because those require separate exchange or
> contemporaneous press anchors.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `financial_and_payment_institution_bitcoin_service_prohibition`

**Timestamp**: `2013-12-05 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_legal`**
  - URL: <https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2013/art_d7241872221f43708e47fd30ac30eac0.html>
  - body_hash: `sha256:fd834ddbf817a7e65d70ba0e13e2ee1695dbd039e09918e1e1eee4d348c1c70a`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2013-12/primary/www.miit.gov.cn__zwgk-zcwj-wjfb-tz-art-2013-art_d7241872221f43708e47fd30ac30eac0.html__a2558c2094.html`
  > MIIT's official full-text copy states that financial institutions
> and payment institutions must not conduct Bitcoin-related business,
> including Bitcoin registration, trading, clearing, settlement,
> payment, exchange, custody, collateral, insurance, or related
> financial-product services. attribution=direct because the primary
> legal instrument itself names the regulated service prohibition.
- **`primary_legal`**
  - URL: <https://www.pbc.gov.cn/tiaofasi/fileDir/resource/cms/2018/07/2018072615002921168.pdf>
  - body_hash: `sha256:5522c48edcffc33d96c13d41d44cfe8dfd0791c211ed93885e188a3bc15a1b9b`
  - body_path: `sources/http_captures/china-pboc-crypto-ban-2013-12/primary/www.pbc.gov.cn__tiaofasi-fileDir-resource-cms-2018-07-2018072615002921168.pdf__7180e9bb41.bin`
  > PBOC-hosted PDF copy of the same five-ministry notice, retained as
> the primary central-bank legal artifact.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): Exchange-facing website notices and CNY-deposit interruptions may be

## 7. Related events

- [`china-pboc-crypto-ban-2021`](./china-pboc-crypto-ban-2021.md)
- [`china-pboc-banks-close-exchange-accounts-2014-04`](./china-pboc-banks-close-exchange-accounts-2014-04.md)
- [`india-rbi-crypto-ban-2018`](./india-rbi-crypto-ban-2018.md)
- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`turkey-cbrt-crypto-ban-2021`](./turkey-cbrt-crypto-ban-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `0b7e0bd`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

