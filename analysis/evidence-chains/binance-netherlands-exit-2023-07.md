# Evidence chain — `binance-netherlands-exit-2023-07`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-02` · **Source commit**: `cba4eca` · **Schema**: `0.2.0` · **Event last_verified**: `2026-06-01` · **Tool version**: `0.1.0` · **Generated**: `2026-06-02T00:00:00Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "Binance's 2023-06-16 withdrawal from the Netherlands (new-user registration
> stopped immediately; trading halted 2023-07-17, withdraw-only) after failing
> to secure a Dutch VASP registration is a single-layer offramp_cex
> observed_change with attribution=direct, part of the 2023 Dutch exchange
> exodus (cf. KuCoin)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `binance`
- **Timestamp**: `2023-06-16 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/notice-on-changes-of-services-in-the-netherlands-b5a647be31cf469b87fc3337fd461ced>
  - Wayback: <https://web.archive.org/web/20230616171924/https://www.binance.com/en/support/announcement/notice-on-changes-of-services-in-the-netherlands-b5a647be31cf469b87fc3337fd461ced>
  - body_hash: `sha256:01617926483c08666d267f9f54ab30377ca18fec9f517fcc86f5360bd413631b`
  - body_path: `sources/http_captures/binance-netherlands-exit-2023-07/official-binance-wayback/web.archive.org__web-20230616171924-https-www.binance.com-en-support-announcement-notice-on-changes-of-services-in-the-netherlands-b5a647be31cf469b87fc3337fd461ced__517a24b988.html`
  > Binance Support notice, Wayback memento 2023-06-16 17:19:24 UTC:
> "Notice on Changes of Services in the Netherlands." Captured body
> contains the Binance-authored statement that Binance was leaving the
> Dutch market, would accept no new Netherlands-resident users
> immediately, and from 2023-07-17 would allow existing Dutch resident
> users only to withdraw assets, with no further purchases, trades, or
> deposits. This upgrades the trigger from semi-primary trade coverage
> to a replayable first-party corporate source.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/144920/binance-to-leave-netherlands-after-failing-to-acquire-vasp-license>
  - Wayback: <https://web.archive.org/web/20251212094859/https://decrypt.co/144920/binance-to-leave-netherlands-after-failing-to-acquire-vasp-license>
  - body_hash: `sha256:f409e0479abad2aeabc1ee9beb7596da07c4276a2dcdb945eb39b2fbaf8b8180`
  - body_path: `sources/http_captures/binance-netherlands-exit-2023-07/primary/web.archive.org__web-20251212094859-https-decrypt.co-144920-binance-to-leave-netherlands-after-failing-to-acquire-vasp-license__2fe0a699ed.html`
  > Decrypt 2023-06-16: "Binance to Leave Netherlands After Failing to
> Acquire VASP License." Binance stopped registering new Dutch users; from
> 2023-07-17 trading in the Netherlands is halted and existing users can
> only withdraw funds. Grep of captured body confirms "Binance to Leave
> Netherlands", "VASP License", "starting July 17, trading in the
> Netherlands will be halted", "no longer registering new users",
> "withdrawing funds". Wayback 20251212094859 pinned.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: Binance (Netherlands market)
- **Canonical domains**: `binance.com`

> Target is the Binance Dutch-resident retail-customer access surface.
> Subset enumeration: a national market-access withdrawal (no new users;
> trading halted 2023-07-17; withdraw-only) rather than a complete on-chain
> address set. No address-level targets; a market-level exit by a centralized
> exchange.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `direct` · Δt = 0h

**Event label**: `binance_netherlands_market_withdrawal_announced`

**Timestamp**: `2023-06-16 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`primary_corporate`**
  - URL: <https://www.binance.com/en/support/announcement/notice-on-changes-of-services-in-the-netherlands-b5a647be31cf469b87fc3337fd461ced>
  - Wayback: <https://web.archive.org/web/20230616171924/https://www.binance.com/en/support/announcement/notice-on-changes-of-services-in-the-netherlands-b5a647be31cf469b87fc3337fd461ced>
  - body_hash: `sha256:01617926483c08666d267f9f54ab30377ca18fec9f517fcc86f5360bd413631b`
  - body_path: `sources/http_captures/binance-netherlands-exit-2023-07/official-binance-wayback/web.archive.org__web-20230616171924-https-www.binance.com-en-support-announcement-notice-on-changes-of-services-in-the-netherlands-b5a647be31cf469b87fc3337fd461ced__517a24b988.html`
  > Binance first-party support notice for the Netherlands service
> changes. The captured body states that no new Dutch resident users
> would be accepted and that existing Dutch resident users would be
> withdraw-only from 2023-07-17, with purchases, trades, and deposits
> disabled. attribution=direct for Binance's own market-withdrawal
> action.
- **`semi_primary_wayback`**
  - URL: <https://decrypt.co/144920/binance-to-leave-netherlands-after-failing-to-acquire-vasp-license>
  - Wayback: <https://web.archive.org/web/20251212094859/https://decrypt.co/144920/binance-to-leave-netherlands-after-failing-to-acquire-vasp-license>
  - body_hash: `sha256:f409e0479abad2aeabc1ee9beb7596da07c4276a2dcdb945eb39b2fbaf8b8180`
  - body_path: `sources/http_captures/binance-netherlands-exit-2023-07/primary/web.archive.org__web-20251212094859-https-decrypt.co-144920-binance-to-leave-netherlands-after-failing-to-acquire-vasp-license__2fe0a699ed.html`
  > Decrypt 2023-06-16: Binance to leave the Netherlands after failing to
> acquire a VASP license; no longer registering new Dutch users; trading
> halted 2023-07-17; withdraw-only thereafter. Legacy attribution note
> superseded by the Binance primary notice added on 2026-06-01; retained
> as corroborating trade coverage.
- **`semi_primary_wayback`**
  - URL: <https://cryptoslate.com/binance-withdraws-from-netherlands-following-vasp-license-snub/>
  - Wayback: <https://web.archive.org/web/20251217033958/https://cryptoslate.com/binance-withdraws-from-netherlands-following-vasp-license-snub/>
  - body_hash: `sha256:ceec80967bddde68d8f2026112c864b047210a4f71f5459b881507d4577f149e`
  - body_path: `sources/http_captures/binance-netherlands-exit-2023-07/primary/web.archive.org__web-20251217033958-https-cryptoslate.com-binance-withdraws-from-netherlands-following-vasp-license-snub__713e9f9c2f.html`
  > CryptoSlate corroboration of the Binance Netherlands withdrawal
> following the Dutch VASP-license snub. Independent second
> semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`kucoin-netherlands-exit-2023`](./kucoin-netherlands-exit-2023.md)
- [`netherlands-dnb-binance-warning-2021`](./netherlands-dnb-binance-warning-2021.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `cba4eca`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

