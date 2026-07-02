# Evidence chain — `tether-ofac-iran-economic-fury-344m-freeze-2026-04`

**Status**: `admitted` · **Stratum**: `S5_corporate` · **Shape**: `comparison` (1 changed layer(s): `asset_onchain`) · **Tier**: `empirical_case`

**Dataset version**: `0.2.0-rc-dryrun-11` · **Dataset cutoff**: `2026-06-08` · **Source commit**: `ee7bf1a` · **Schema**: `0.2.0` · **Event last_verified**: `2026-05-31` · **Tool version**: `0.1.0` · **Generated**: `2026-06-25T23:48:26Z`

> ⚠️ **This output is auditable evidence, not advice.** Read [`docs/limitations-and-use.md`](../../docs/limitations-and-use.md) before using any claim below in a brief, memo, or risk model.

## Scoped claim

> "On 2026-04-23 at 12:02:36 UTC, Tether blacklisted two Tron USDT
> addresses later enumerated by OFAC for the Central Bank of Iran
> (IRGC-Qods Force / Hizballah links): TNiq9AXBp9EjUqhDhrwrfvAA8U3GUQZH81
> and TTiDLWE6fZK8okMJv6ijg42yrH6W2pjSr9. Tether/TRM describe the action
> as a ~$344M freeze, the largest on-chain freeze of Iranian sovereign
> crypto reserves on record; single-layer asset_onchain observed_change,
> attribution=direct. The per-address split and 'Economic Fury' phrasing
> are not asserted (not in captures)."

## 1. Trigger

- **Type**: `corporate_policy_change`
- **Actor**: `tether_usdt_issuer`
- **Timestamp**: `2026-04-23 00:00:00+00:00` (precision: `day`)

### Trigger citations

- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement/>
  - Wayback: <https://web.archive.org/web/20260520133449/https://tether.io/news/tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement/>
  - body_hash: `sha256:74ef9f0b7a5fe23c37c57e1c5b3649eb9fec3cbce109864401d59cce57ff6509`
  - body_path: `sources/http_captures/tether-ofac-iran-economic-fury-344m-freeze-2026-04/primary/web.archive.org__web-20260520133449-https-tether.io-news-tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement__13331ae00f.html`
  > Tether official blog: Tether "supported the U.S. Government in
> freezing $344 million USD₮ across two addresses" in coordination
> with OFAC and U.S. law enforcement; the freeze was executed after
> the addresses were identified, preventing further movement of
> funds. Primary-corporate anchor for the actor (Tether) and the
> action ($344M freeze across two addresses). Wayback 20260520133449
> pinned.
- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20260424>
  - body_hash: `sha256:327835198fb4e13ee3b43efeca177f9f50d6fe26360678db82965446b7c26661`
  - body_path: `sources/http_captures/tether-ofac-iran-economic-fury-344m-freeze-2026-04/primary/ofac.treasury.gov__recent-actions-20260424__ab9d2f176b.html`
  > OFAC Recent Actions 2026-04-24 SDN update adds two TRON digital
> currency addresses to Bank Markazi Jomhouri Islami Iran / Central
> Bank of Iran: TNiq9AXBp9EjUqhDhrwrfvAA8U3GUQZH81 and
> TTiDLWE6fZK8okMJv6ijg42yrH6W2pjSr9. This is the primary legal
> anchor for the complete two-address target set and the US/IRGC/
> Hizballah sanctions context.
- **`semi_primary_wayback`**
  - URL: <https://www.trmlabs.com/resources/blog/ofac-sanctions-crypto-addresses-associated-with-the-central-bank-of-iran-freezes-usd-344-million>
  - Wayback: <https://web.archive.org/web/20260524000757/https://www.trmlabs.com/resources/blog/ofac-sanctions-crypto-addresses-associated-with-the-central-bank-of-iran-freezes-usd-344-million>
  - body_hash: `sha256:7d958fe9098d3287131261d64ee0a063d548030368c4f39fe9254e3f6ec2e7cb`
  - body_path: `sources/http_captures/tether-ofac-iran-economic-fury-344m-freeze-2026-04/primary/web.archive.org__web-20260524000757-https-www.trmlabs.com-resources-blog-ofac-sanctions-crypto-addresses-associated-with-the-central-bank-of-iran-freezes-usd-344-millio__e726d45b35.html`
  > TRM Labs: OFAC froze ~$344.2M USDT held in two wallets attributed
> to the Central Bank of Iran, with links to the IRGC-Qods Force and
> Hizballah — described as the largest on-chain freeze of Iranian
> sovereign crypto reserves on public record. The two wallets
> collectively received ~$370M across ~1,000 transactions since
> March 2021. Independent second semi-primary anchor.

## 2. Target

- **Kind**: `address_set`
- **Enumeration**: `complete`
- **Actor name**: Central Bank of Iran USD₮ wallets (2 addresses)
- **Chains**: `tron`
- **Addresses**: 2 total (enumerated in event YAML)

> Two Tron USD₮ addresses attributed to the Central Bank of Iran
> (links to IRGC-Qods Force / Hizballah), holding ~$344M USDT. OFAC's
> 2026-04-24 SDN update enumerates the complete two-address set; both
> addresses have matching USDT AddedBlackList logs in Tron block
> 82092618.

## 3. Changed-layer observations (supports the scoped claim)

### asset_onchain · attribution: `direct` · Δt = 12.0h

**Event label**: `tether_froze_344m_usdt_central_bank_iran_two_addresses`

**Timestamp**: `2026-04-23 12:02:36+00:00` (precision: `hour_range`)

**Sources**:

- **`primary_legal`**
  - URL: <https://ofac.treasury.gov/recent-actions/20260424>
  - body_hash: `sha256:327835198fb4e13ee3b43efeca177f9f50d6fe26360678db82965446b7c26661`
  - body_path: `sources/http_captures/tether-ofac-iran-economic-fury-344m-freeze-2026-04/primary/ofac.treasury.gov__recent-actions-20260424__ab9d2f176b.html`
  > OFAC Recent Actions 2026-04-24 SDN update enumerates the two
> Central Bank of Iran TRON addresses later matched to the
> primary_onchain USDT AddedBlackList logs:
> TNiq9AXBp9EjUqhDhrwrfvAA8U3GUQZH81 and
> TTiDLWE6fZK8okMJv6ijg42yrH6W2pjSr9.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/ebe670f1518f67077d28ec4b54dd0d236a5f1edfa90651524aeb42a21e6975fe>
  - tx_hash: `ebe670f1518f67077d28ec4b54dd0d236a5f1edfa90651524aeb42a21e6975fe`
  > USDT Tron AddedBlackList(address) log for
> TNiq9AXBp9EjUqhDhrwrfvAA8U3GUQZH81 in block 82092618 at
> 2026-04-23 12:02:36 UTC. TronGrid receipt SUCCESS, USDT TRON
> contract TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t, event topic
> 42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc;
> receipt cached under sources/onchain_receipts.
- **`primary_onchain`**
  - URL: <https://tronscan.org/#/transaction/295cd606150289dc18d9e0e4d9503adb9d1b10bde9c314158f9cfa7c9928b09a>
  - tx_hash: `295cd606150289dc18d9e0e4d9503adb9d1b10bde9c314158f9cfa7c9928b09a`
  > USDT Tron AddedBlackList(address) log for
> TTiDLWE6fZK8okMJv6ijg42yrH6W2pjSr9 in block 82092618 at
> 2026-04-23 12:02:36 UTC. TronGrid receipt SUCCESS, USDT TRON
> contract TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t, event topic
> 42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc;
> receipt cached under sources/onchain_receipts.
- **`primary_corporate`**
  - URL: <https://tether.io/news/tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement/>
  - Wayback: <https://web.archive.org/web/20260520133449/https://tether.io/news/tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement/>
  - body_hash: `sha256:74ef9f0b7a5fe23c37c57e1c5b3649eb9fec3cbce109864401d59cce57ff6509`
  - body_path: `sources/http_captures/tether-ofac-iran-economic-fury-344m-freeze-2026-04/primary/web.archive.org__web-20260520133449-https-tether.io-news-tether-supports-freeze-of-more-than-344-million-in-usdt-in-coordination-with-ofac-and-u-s-law-enforcement__13331ae00f.html`
  > Tether official statement: Tether supported the U.S. Government
> in freezing $344M USD₮ across two addresses, in coordination
> with OFAC and U.S. law enforcement. attribution=direct per §1.2:
> Tether's own freeze carries the asset-layer change and OFAC's
> designation names the specific (Central Bank of Iran) target
> wallets being acted upon.
- **`semi_primary_wayback`**
  - URL: <https://www.trmlabs.com/resources/blog/ofac-sanctions-crypto-addresses-associated-with-the-central-bank-of-iran-freezes-usd-344-million>
  - Wayback: <https://web.archive.org/web/20260524000757/https://www.trmlabs.com/resources/blog/ofac-sanctions-crypto-addresses-associated-with-the-central-bank-of-iran-freezes-usd-344-million>
  - body_hash: `sha256:7d958fe9098d3287131261d64ee0a063d548030368c4f39fe9254e3f6ec2e7cb`
  - body_path: `sources/http_captures/tether-ofac-iran-economic-fury-344m-freeze-2026-04/primary/web.archive.org__web-20260524000757-https-www.trmlabs.com-resources-blog-ofac-sanctions-crypto-addresses-associated-with-the-central-bank-of-iran-freezes-usd-344-millio__e726d45b35.html`
  > TRM Labs corroboration: ~$344.2M USD₮ in two Central-Bank-of-
> Iran wallets (IRGC-Qods Force / Hizballah links), the largest
> on-chain freeze of Iranian sovereign crypto reserves on record;
> ~$370M received across ~1,000 tx since March 2021. Independent
> second semi-primary anchor.

## 5. Honest coverage gaps

*No layers are `not_measured` for this event — every applicable layer is `measured`, `partially_measured`, or `not_applicable`.*

## 7. Related events

- [`dprk-usdt-network-ofac-2025`](./dprk-usdt-network-ofac-2025.md)
- [`tether-dprk-precommit-freeze-2025`](./tether-dprk-precommit-freeze-2025.md)

## 8. How to audit this chain

1. Clone the repository at tag `v0.2.0-rc-dryrun-11` (commit `ee7bf1a`).
2. For each source above, fetch the file at its `body_path` and compute its sha256. It must match the recorded `body_hash`.
3. For each primary-onchain source, look up the `tx_hash` on the respective block explorer. The tx should exist in the block referenced or within the same day.
4. If any check fails, file an issue per [`docs/audit-protocol.md`](../../docs/audit-protocol.md).

