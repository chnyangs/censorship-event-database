# Evidence chain — `okx-canada-exit-2023`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `offramp_cex`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-01` · **Source commit**: `4e61290` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-01T12:35:41Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "OKX on 2023-03-20 notified Canadian users that it would stop providing
> services and accepting new accounts on 2023-03-24 and require all
> Canadian positions closed and funds withdrawn by 2023-06-22, citing the
> CSA's new stablecoin / undertaking regulations — a 1-layer offramp_cex
> observed_change (attribution=plausible) for the OKX Canada cohort.
> Structurally an S5 corporate-policy retreat sibling to the S4 CSA-driven
> Binance Canada withdrawal (canada-csa-binance-withdrawal-2023)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `OKX_EXCHANGE`
- **Timestamp**: `2023-03-20 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/okx-to-cease-operations-in-canada-by-june-22-2023>
  - Wayback: <https://web.archive.org/web/20251225133547/https://cointelegraph.com/news/okx-to-cease-operations-in-canada-by-june-22-2023>
  - body_hash: `sha256:3858c9aa2ad432071a55fbc8b5cddcd0578037eef52cb5bfcc2d142c3cd25dce`
  - body_path: `sources/http_captures/okx-canada-exit-2023/primary/web.archive.org__web-20251225133547-https-cointelegraph.com-news-okx-to-cease-operations-in-canada-by-june-22-2023__0acf53d2eb.html`
  > Cointelegraph (2023-03): OKX emailed Canadian users on 2023-03-20
> stating it "will no longer provide services or allow users to open
> new accounts in Canada starting on Mar. 24, 2023, 12:00 AM EST,"
> citing "new regulations." Existing Canadian users had to close
> open options / margin / perpetual / futures positions and withdraw
> fiat or tokens by 2023-06-22. The captured page confirms the
> "Mar. 24" no-new-accounts / "no longer provide" services cut-off
> and the 2023-06-22 wind-down date. Verified via grep of the pinned
> body.

## 2. Target

- **Kind**: `entity`
- **Enumeration**: `subset`
- **Actor name**: OKX (Canada user cohort)
- **Canonical domains**: `okx.com`

> OKX Canadian-resident user cohort. OKX (Aux Cayes FinTech Co. Ltd.)
> is the focal target actor; the affected population is Canadian-resident
> retail users of okx.com. Subset-enumerated because OKX's Canada exit
> affected the Canadian retail cohort rather than a named address list.
> Sibling to the S4 canada-csa-binance-withdrawal-2023 and the S5
> kucoin-canada-exit-2023 / paxos-canada-exit-2023-04 from the
> corporate-policy side.

## 3. Changed-layer observations (supports the scoped claim)

### offramp_cex · attribution: `plausible` · Δt = Noneh

**Event label**: `okx_canada_offramp_shutdown`

**Timestamp**: `2023-03-24 00:00:00+00:00` (precision: `day`)

**Sources**:

- **`semi_primary_wayback`**
  - URL: <https://cointelegraph.com/news/okx-to-cease-operations-in-canada-by-june-22-2023>
  - Wayback: <https://web.archive.org/web/20251225133547/https://cointelegraph.com/news/okx-to-cease-operations-in-canada-by-june-22-2023>
  - body_hash: `sha256:3858c9aa2ad432071a55fbc8b5cddcd0578037eef52cb5bfcc2d142c3cd25dce`
  - body_path: `sources/http_captures/okx-canada-exit-2023/primary/web.archive.org__web-20251225133547-https-cointelegraph.com-news-okx-to-cease-operations-in-canada-by-june-22-2023__0acf53d2eb.html`
  > OKX 2023-03-24 services / new-account cut-off for Canadian users
> (full wind-down 2023-06-22). attribution=plausible: the off-ramp
> shutdown is directly observed in contemporaneous coverage, but the
> captured anchor is semi-primary (no OKX primary notice pinned), so
> the link to the specific 2023-02-22 CSA Staff Notice 21-332 is
> carried as the reporter-attributed "new regulations" rationale
> rather than a primary OKX-stated trigger.

## 5. Honest coverage gaps

- **l4_frontend** (`not_measured`): OKX's exit was communicated by email / notice rather than captured

## 7. Related events

- [`canada-csa-binance-withdrawal-2023`](./canada-csa-binance-withdrawal-2023.md)
- [`kucoin-canada-exit-2023`](./kucoin-canada-exit-2023.md)
- [`paxos-canada-exit-2023-04`](./paxos-canada-exit-2023-04.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `4e61290`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

