# Machine-prepared current-source panel sidecar

`verified_panel.json` records 16 named source checks with exact raw captures and
hashes: 14 content assertions passed after HTTP 200, while a Coinbase policy
page returned HTTP 403 and the Binance announcement index returned empty HTTP
202 responses. The Coinbase index itself was available. Two total attempts are
the maximum for each failing source. These are source-availability and interface
checks; they are not independent human validation, historical archive completion,
provider existence intervals, or target-specific negative evidence.

Canonical Ethereum addresses are linked from issuer documentation:

| Issuer | Address | Read signature | Event address encoding |
| --- | --- | --- | --- |
| [Circle](https://developers.circle.com/stablecoins/usdc-contract-addresses) | `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48` | `isBlacklisted(address)` | Indexed topic in `Blacklisted` / `UnBlacklisted` |
| [Tether](https://tether.to/en/supported-protocols/) | `0xdac17f958d2ee523a2206206994597c13d831ec7` | `isBlackListed(address)` | Non-indexed data word in `AddedBlackList` / `RemovedBlackList` |

Exact selectors and Keccak-256 topics are in the sidecar and collector. Circle's
captured current source uses the Zeppelinos implementation slot, not an assumed
EIP-1967 slot. Tether's captured issuer-linked Etherscan source exposes
`deprecated()` and `upgradedAddress()` forwarding. Current source and a verified
source service do not independently reproduce historical bytecode; historical
implementation verification remains pending.

The four named RPC-provider records use documented public endpoints or explicit
credentialed templates. Infura and QuickNode were not queried because this pilot
does not use keys. The Alchemy public tier is distinct from its keyed service.
Disclosure indexes for Coinbase, Kraken and Binance do not expose private account
outcomes or establish historical archive coverage.

Supplementary captures outside the original sidecar are retained separately:

- `range_probe_sources/alchemy_log_limits/` captures the official
  [eth_getLogs documentation](https://www.alchemy.com/docs/reference/eth-getlogs).
  The actual public-endpoint error bodies in the range pilot advertise a
  100-block cap; do not conflate that with the generic keyed free-tier wording.
- `publicnode_official_source/attempt_1/` captures the official
  [PublicNode Ethereum page](https://ethereum.publicnode.com/) advertising
  `https://ethereum-rpc.publicnode.com`. Raw HTML SHA-256 is
  `1a281fb85194e67a9320a1094a1cf61c70c6791c723ac2d476a47f30d8cab2e9`.
  Its archive-access advertising does not establish historical availability on
  the anonymous endpoint; the captured probe failed for the required 2022 block.

See the [pilot report](../../analysis/measurement_pilot/README.md) for frozen run
results and interpretation limits. Regeneration requires a new output directory
and leaves the protected proposed panel untouched:

```sh
python3 scripts/prepare_measurement_panel.py --out-dir sources/NEW_PANEL_CAPTURE
```
