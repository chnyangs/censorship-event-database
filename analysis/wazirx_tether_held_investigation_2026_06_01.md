# WazirX / Tether held investigation - 2026-06-01

## Candidate

- Registry id: `wazirx-tether-usdt-hack-freeze-2025-01`
- Candidate date: 2025-01-17
- Actor framing: WazirX / Tether
- Layer: `asset_onchain`
- Current disposition: held, not authored

## Available local evidence

- Captured Decrypt article:
  `sources/http_captures/exact-candidate-triage-2026-06-01/review/decrypt.co__301538-wazirx-freezes-3-million-hack__228319de1c.html`
- Capture metadata:
  `sources/http_captures/exact-candidate-triage-2026-06-01/review/decrypt.co__301538-wazirx-freezes-3-million-hack__228319de1c.json`
- Registry secondary source:
  `https://www.business-standard.com/companies/start-ups/wazirx-freezes-3-million-in-usdt-nearly-7-months-after-cyberattack-125011701136_1.html`

The captured Decrypt page supports the high-level claim that WazirX reported freezing about USD 3M in USDT after
the July 2024 hack, but it does not enumerate the frozen addresses, a USDT blacklist transaction, a court exhibit,
or a Tether issuer notice. The Business Standard URL was retained as a corroborating press source but was not enough
to satisfy the asset-onchain evidence floor.

## Evidence floor

Per the admission rule implemented in `scripts/validate.py`, an `asset_onchain` observation needs at least one
`primary_onchain` source at admitted status. Press reports about an aggregate freeze amount are not sufficient for
this candidate because they do not identify the target address set or the issuer blacklist transaction.

This row can be reopened only if one of the following appears:

- A WazirX, Tether, court, administrator, or investigator artifact enumerates the frozen USDT address set.
- A USDT `AddedBlackList(address)` transaction is linked by a public source to the WazirX July 2024 theft proceeds.
- A replayable court/restructuring filing or wallet-history artifact ties a specific address set to the WazirX hack
  and to a Tether freeze action.

## Follow-up scan notes

Earlier investigation checked the Ethereum USDT `AddedBlackList(address)` topic around the candidate window
(2025-01-15 to 2025-01-20) and found date-proximate blacklist events, but no public WazirX attribution or frozen
address set. This scan was used only as triage context; it is not a source artifact for an event row unless rerun
and saved as a receipt-backed artifact.

Date-proximate ETH USDT blacklist logs seen in that triage pass:

| Date UTC | Tx hash | Target address | Balance note |
| --- | --- | --- | --- |
| 2025-01-15 20:02:47 | `0xd638b5cb029dc353c788ea6c600fc7d4fe31ee16e1c54e9c3bd097b3128cd655` | `0x4cbeb09caa4dddde613cedfe2f73a92f07fc858f` | 14,000,000 |
| 2025-01-15 20:02:47 | `0xdf0e9cbf96f10ac10edc32f544580cb478f2cffb5ae05ffbb959f6a5209c7b37` | `0xf5902e7402da82d43b2464f1514c4125bac2cfd0` | 1,000,000 |
| 2025-01-16 02:12:23 | `0xc37769014ba30aa1d5b95c8a5781a0ea35a5e3bdf5e344fb8e9051d40df34a5e` | `0x41c3b8b5cfdd29de2941dae4a956cc9f057ac767` | 148,400 |
| 2025-01-16 02:12:35 | `0x767720937a7fc50113ce80b43aec212c02ef18d663dde203b9bcb0164930f59c` | `0xe36d7e24b030fbdb556f12a83bdc85a21afa3db3` | 63,892.632553 |
| 2025-01-16 02:12:35 | `0xb65cc53f36c44f4c158ec4147232ca8e8c4e0eb41b92d04778c2d3a9e590f54c` | `0x2bc05300f6f9221e7b5f77ace9de6c0ebc28e6d4` | 70,150 |
| 2025-01-16 02:12:35 | `0x76baea8a2b45c5780203f28e6fc869f6bfdcacfeca342290032d393d0249a493` | `0x1298500214c99cc9c844c2d99d741b44a869e427` | 50,251,106.829057 |
| 2025-01-16 02:12:35 | `0x3ce795877a474f46a3bfa8eba345a2cf9d5487a5a21825b8ea8b3e68100a12d9` | `0x5095617268d07772ef684ee0f81b399f0a386ec8` | 2,992,266.546773 |
| 2025-01-16 02:12:59 | `0xca04bdd48c56c8389ad6ab9414dfe75aa2801a7341d374131fda698d3dd22182` | `0x1fc0cdc3cf9cef83136d5d0b61dfc239280c303d` | 2,245,364.22 |
| 2025-01-17 23:33:11 | `0x5e05408cc3bd50dd2d520c12d5f9df6956a405f8cc411cea017bac01d5038bcd` | `0x6df9510c5237e0de785995c8cf908588f7bc5b86` | 1,855,498.9735 |
| 2025-01-17 23:33:35 | `0x1224295e9979c974ab11d645460e13d047a7353a57416026e046d67821e3f8e6` | `0xc721190538a516ee315548dbe185cd27e94423e0` | 2,877 |
| 2025-01-17 23:33:35 | `0x2d47e484cfd414e87c70a557ead12d271fa7e98b7b1e4341b3a4745f8ece7e81` | `0x39f3bc845a4f78d63d6995567f5ebeaaec9ba29c` | 2,032 |
| 2025-01-17 23:33:35 | `0xd69dea03955a4edd7a6177caa46d898889cbeb2ac960da07bfa33092a790ee13` | `0xfb9dd8788bb1af2838b7de4492c47a94dec551ae` | 3,347 |
| 2025-01-17 23:33:35 | `0x9cfd1567040d1d1005b845130739f1c280090b9a254fde18f0e0dfa98f593ac2` | `0x5649ad8001070b3c501bd9877de5f44918086c7a` | 9,033.178071 |
| 2025-01-17 23:33:35 | `0xb60d15c2f2cd0ea0b7d7a0d6f66ae3e17a65f75d849e88cbebdbbb6b64c71598` | `0x12e88be9e4de46b85b5d7ddd2830adb6f1d7f375` | 47,114.9 |
| 2025-01-18 22:17:11 | `0x47d98cc401e1d43c550457aa1444907feaf1ffb4abf0c6cc00f69b7abcc3b6cb` | `0xf58ba47a2f8d666073ae4c9d85e6a7224c58b575` | 338,492.428797 |
| 2025-01-18 22:17:11 | `0x9c5dce68edecb042542bbcfae0ba88cef2b7d154ad81bec531946b3a45184f2f` | `0x532961b23a28a9e5a8b1769bdb3e8906fc7c7a01` | 200,000 |

Transfer spot checks did not establish WazirX linkage:

- The supposed WazirX attacker address `0x6eedf92fb92dd68a270c3205e96dccc527728066` had no matching ETH USDT
  transfers in the checked 2024-07-18 to 2025-01-20 window.
- Some date-proximate blacklist addresses had incoming USDT transfers shortly before blacklisting, but no public
  source tied those sender or recipient addresses to WazirX theft proceeds.

## Disposition

Keep the registry row as `HELD-needs-asset-onchain-txhash-or-address-set`. Do not author an event from the
current evidence. The negative result is useful: it prevents aggregate press coverage from bypassing the corpus'
asset-onchain floor, while preserving a precise reopen path if a public address set or tx hash is found later.
