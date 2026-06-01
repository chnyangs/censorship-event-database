# Evidence chain — `nigeria-binance-network-block-2024-02`

**Status**: `admitted` · **Stratum**: `S4_nation_state` · **Shape**: `comparison` (2 changed layer(s): `l0_network`, `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `ad910b8` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T00:40:01Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Nigeria's late-Feb-2024 NCC-ordered telco block of Binance/Coinbase/
> Kraken websites (OONI-confirmed binance.com blocking from NG) plus the
> detention of two Binance executives severed Nigerian-user access at the
> l0_network and offramp_cex layers; 2-layer comparison, attribution
> plausible."

## 1. Trigger

- **Type**: `nation_state_block`
- **Actor**: `nigeria_ncc_government`
- **Timestamp**: `2024-02-26 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/02/29/nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports>
  - Wayback: <https://web.archive.org/web/20240301030622/https://www.coindesk.com/policy/2024/02/29/nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports/>
  - body_hash: `sha256:24ee7e64a8d7e22be3917a27de0862cf4980d0e59c889768a63d483f0943ab9f`
  - body_path: `sources/http_captures/nigeria-binance-network-block-2024-02/primary/web.archive.org__web-20240301000000-https-www.coindesk.com-policy-2024-02-29-nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports__bb84df58e1.html`
  > CoinDesk 2024-02-29: in late Feb 2024 Nigeria's telecoms regulator
> (NCC) ordered telcos to block access to Binance, Coinbase, and
> Kraken websites, and the government detained two Binance executives
> (Tigran Gambaryan, Nadeem Anjarwalla, 2024-02-28); CBN Governor
> Cardoso alleged Binance moved $26B in untraceable funds and blamed
> crypto for the naira's slide. Wayback 20240301030622 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance / Coinbase / Kraken (Nigeria network block)
- **Canonical domains**: `binance.com`

> Centralized crypto exchanges (Binance, Coinbase, Kraken) whose
> websites Nigerian telcos were ordered to block in late Feb 2024,
> plus Binance specifically (executive detentions). Subset: the
> named blocked exchanges + Binance as the focal target.

## 3. Changed-layer observations (supports the scoped claim)

### l0_network · attribution: `plausible` · Δt = 0h

**Event label**: `ncc_telco_block_of_binance_and_other_exchange_domains`

**Timestamp**: `2024-02-26 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/measurements?probe_cc=NG&test_name=web_connectivity&input=https%3A%2F%2Fwww.binance.com%2F&since=2024-02-25&until=2024-03-15&limit=5>
  - body_hash: `sha256:fcd25b717edd9167a1c6af75c787dfe34f17de3001838fa5eb11280bf14a9416`
  - body_path: `sources/http_captures/nigeria-binance-network-block-2024-02/primary/api.ooni.io__api-v1-measurements__11424b04af.json`
  > OONI web_connectivity measurements for binance.com from Nigerian
> vantage points, 2024-02-26..29 — all anomaly=True (blocking
> detected), coincident with the Nigerian Communications
> Commission's order to telcos to block crypto-exchange websites.
> Measurement-anchors the l0_network block.
- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/02/29/nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports>
  - Wayback: <https://web.archive.org/web/20240301030622/https://www.coindesk.com/policy/2024/02/29/nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports/>
  - body_hash: `sha256:24ee7e64a8d7e22be3917a27de0862cf4980d0e59c889768a63d483f0943ab9f`
  - body_path: `sources/http_captures/nigeria-binance-network-block-2024-02/primary/web.archive.org__web-20240301000000-https-www.coindesk.com-policy-2024-02-29-nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports__bb84df58e1.html`
  > CoinDesk 2024-02-29: Nigeria detained two Binance executives
> (Tigran Gambaryan, Nadeem Anjarwalla) amid the crackdown;
> telcos were ordered to block access to Binance/Coinbase/Kraken
> websites. Independent journalism anchor for the block + the
> offramp severance.

### offramp_cex · attribution: `plausible` · Δt = 48h

**Event label**: `nigerian_user_access_to_binance_offramp_severed`

**Timestamp**: `2024-02-28 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://www.coindesk.com/policy/2024/02/29/nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports>
  - Wayback: <https://web.archive.org/web/20240301030622/https://www.coindesk.com/policy/2024/02/29/nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports/>
  - body_hash: `sha256:24ee7e64a8d7e22be3917a27de0862cf4980d0e59c889768a63d483f0943ab9f`
  - body_path: `sources/http_captures/nigeria-binance-network-block-2024-02/primary/web.archive.org__web-20240301000000-https-www.coindesk.com-policy-2024-02-29-nigeria-detains-binance-executives-as-it-investigates-the-crypto-exchange-reports__bb84df58e1.html`
  > CoinDesk 2024-02-29: Nigeria detained two Binance executives
> (Tigran Gambaryan, Nadeem Anjarwalla) amid the crackdown;
> telcos were ordered to block access to Binance/Coinbase/Kraken
> websites. Independent journalism anchor for the block + the
> offramp severance.
- **`semi_primary_measurement`**
  - URL: <https://api.ooni.io/api/v1/measurements?probe_cc=NG&test_name=web_connectivity&input=https%3A%2F%2Fwww.binance.com%2F&since=2024-02-25&until=2024-03-15&limit=5>
  - body_hash: `sha256:fcd25b717edd9167a1c6af75c787dfe34f17de3001838fa5eb11280bf14a9416`
  - body_path: `sources/http_captures/nigeria-binance-network-block-2024-02/primary/api.ooni.io__api-v1-measurements__11424b04af.json`
  > OONI web_connectivity measurements for binance.com from Nigerian
> vantage points, 2024-02-26..29 — all anomaly=True (blocking
> detected), coincident with the Nigerian Communications
> Commission's order to telcos to block crypto-exchange websites.
> Measurement-anchors the l0_network block.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`nigeria-cbn-crypto-ban-2021`](./nigeria-cbn-crypto-ban-2021.md)
- [`philippines-sec-binance-block-2024`](./philippines-sec-binance-block-2024.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ad910b8`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

