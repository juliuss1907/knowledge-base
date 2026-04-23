---
title:
source: "https://x.com/the_smart_ape/article/2047233756046438654"
author:
  - "[[The Smart Ape 🔥 (@the_smart_ape)]]"
date_ingested: 2026-04-23
created: 2026-04-23
tags:
type: "raw"
source_type: "article"
status: "unprocessed"
---
![Hình ảnh](https://pbs.twimg.com/media/HGk8DcqW4AA0y70?format=jpg&name=large)

as you know on april 18, a north korean hacker stole [$292m](https://x.com/search?q=%24292m&src=cashtag_click) from kelp dao. 5 days later, more than half of it is already gone, fragmented across thousands of wallets, swapped through protocols that can't be paused, converging toward a very specific destination.

![Hình ảnh](https://pbs.twimg.com/media/HGkjw4dW0AAaczJ?format=jpg&name=large)

the interesting part is how you take [$292m](https://x.com/search?q=%24292m&src=cashtag_click) of stolen, traceable crypto and turn it into cash in pyongyang without anyone being able to stop you.

the point is to show why the entire modern crypto laundering pipeline works, why it's structurally unstoppable, and what the final $1 of laundered money actually buys.

# phase 1: the setup (hours before the hack)

the attacker didn't start with the drain. lazarus's playbook always begins with infrastructure work.

roughly 10 hours before the attack, 8 fresh wallets were pre-funded through tornado cash, a mixer that severs the link between money's origin and destination.

each wallet received exactly 0.1 ETH. these 8 wallets would pay the gas for everything coming next. because they were seeded via a mixer, no exchange KYC, no previous wallet history, no way to link them to any known actor. clean slate.

![Hình ảnh](https://pbs.twimg.com/media/HGklcaLXcAELGtM?format=jpg&name=large)

right before the hack, the attacker made 3 cross-chain transactions from ETH mainnet to Avalanche and Arbitrum. the goal is clearly to add gas on these L2s and test the bridge operation to make sure it will go smoothly with a larger amount.

![Hình ảnh](https://pbs.twimg.com/media/HGkm0ihWwAAMaak?format=jpg&name=large)

# phase 2: the drain

a separate attack-caller wallet (0x4966…575e) called a function named lzReceive on layerzero's EndpointV2 contract. because the verifier had been successfully lied to, the call was treated as a valid cross-chain message. kelp's bridge contract, Kelp DAO: RSETH\_OFTAdapter (0x85d…) on etherscan, immediately released 116,500 rsETH to 0x8B1.

![Hình ảnh](https://pbs.twimg.com/media/HGknihiXoAAFlWv?format=jpg&name=large)

18% of every rsETH in existence. gone in one function call.

46 minutes later, at 18:21 utc, kelp's emergency multisig paused the protocol. at 18:26 and 18:28 utc, the attacker tried to run the exact same play twice more, each one attempting to drain another 40,000 rsETH (~$100m apiece). both reverted because kelp had pulled the plug in time. the full haul could have been close to [$500m](https://x.com/search?q=%24500m&src=cashtag_click).

![Hình ảnh](https://pbs.twimg.com/media/HGkoeANXQAAiQ2M?format=jpg&name=large)

# phase 3: the aave + compound play

rsETH is a receipt token, its value dies the moment kelp pauses the bridge or blacklists the stolen tokens. the attacker had minutes to convert it into something untouchable. kelp paused 46 minutes after the drain. too late.

selling [$292m](https://x.com/search?q=%24292m&src=cashtag_click) of an illiquid restaking token on the open market would crash the price 30%+ within minutes. so he didn't sell. he used defi lending protocols as laundering primitives, and he moved fast.

the intake wallet 0x8B1 fanned the 116,500 stolen rsETH out to the 7 other branches.

![Hình ảnh](https://pbs.twimg.com/media/HGkq23aWkAAhYRr?format=jpg&name=large)

each branch then walked into aave and compound v3, deposited a chunk of the rsETH as collateral, and borrowed ETH against it.

cumulative positions across the 7 branches:

- 89,567 rsETH deposited as collateral
- roughly 82,650 WETH + 821 wstETH borrowed in return, about [$190m](https://x.com/search?q=%24190m&src=cashtag_click) of clean, liquid ethereum assets
- each branch's health factor set to 1.01-1.03, the absolute maximum the protocols would permit before liquidation

![Hình ảnh](https://pbs.twimg.com/media/HGkrkpsWwAAjoKH?format=jpg&name=large)

the attacker traded [$292m](https://x.com/search?q=%24292m&src=cashtag_click) of dirty, illiquid, flagged rsETH for [$190m](https://x.com/search?q=%24190m&src=cashtag_click) of ETH. when it eventually gets marked down to near-zero (because kelp's bridge is insolvent and those rsETH can't be redeemed), the lending protocols' depositors get the loss.

as the market realized aave was holding a [$200m](https://x.com/search?q=%24200m&src=cashtag_click)\+ bad-debt, users panic-withdrew. aave lost $8 billion in TVL in 48 hours. the biggest defi lending protocol's first real bank run, caused by one attacker using the protocol exactly as designed.

![Hình ảnh](https://pbs.twimg.com/media/HGksZiIWYAAkDPP?format=jpg&name=large)

# phase 4: consolidation and split

after the aave/compound borrowing, the 7 branches pushed their borrowed ETH to a third-tier consolidation wallet (0x5d3).

![Hình ảnh](https://pbs.twimg.com/media/HGktSMwX0AArsp_?format=jpg&name=large)

the full operational cluster now has a clear 3-tier shape:

1. tier 1 intake : 0x8B1 (also tornado-funded) receives the raw 116,500 rsETH drain
2. tier 2 operations : 7 other tornado-funded branch wallets do the aave/compound play
3. tier 3 consolidation : 0x5d3 re-aggregates ~71,000 ETH of borrowed funds for unified laundering

the funds split across two chains:

- 75,700 ETH sitting on ethereum mainnet
- 30,766 ETH sitting on arbitrum (~$71m)

arbitrum's security council voted to freeze the arbitrum half. that [$71m](https://x.com/search?q=%2471m&src=cashtag_click) was moved to a governance-controlled wallet that can only be unlocked through further governance action.

![Hình ảnh](https://pbs.twimg.com/media/HGkuG3cXEAAxIAt?format=jpg&name=large)

shortly after this freeze, the hacker moved the remaining eth on mainnet to other addresses and sped up the laundering. from these actions it's pretty clear he wasn't expecting arbitrum to pull a move like that.

![Hình ảnh](https://pbs.twimg.com/media/HGkuxG8WAAEn24r?format=jpg&name=large)

# phase 5: the first laundering wave

four days after the hack, 0x5d3 started emptying. arkham tracked 3 discrete transactions within a few hours.

timing was deliberate: european trading hours on a tuesday. us investigators asleep, european compliance desks dealing with monday pile-ups, asian exchanges winding down.

then the pattern explodes. each first-wave destination immediately fans out again, 0x62c7 pushes to ~60 freshly generated wallets, 0xD4B8 pushes to another ~60. within hours, the clean 10-wallet cluster becomes 100+ disposable addresses, all funded in parallel, each holding a slice small enough to evade detection.

![Hình ảnh](https://pbs.twimg.com/media/HGkyt1FWUAAMOnH?format=jpg&name=large)

lazarus runs HD wallet scripts, a single seed mathematically derives thousands of fresh addresses in seconds, paired with a worker pool (python + web3, ethers.js, or their own internal tooling) that signs and broadcasts the whole tree in parallel. this is the same code they've been iterating on since 2018.

by the end of this phase, the linear, traceable is gone. the 10-wallet operational cluster has exploded into 100+ fragmentation wallets, and the funds are entering privacy rails from dozens of independent origins at once.

# phase 6: thorchain. the exit machine.

the real break happens at thorchain.

thorchain is a decentralized protocol that swaps native assets across chains. you send ETH on ethereum, it returns you BTC on bitcoin.

on april 22 alone, thorchain's 24-hour swap volume hit [$460m](https://x.com/search?q=%24460m&src=cashtag_click). the protocol's normal daily volume is around [$15m](https://x.com/search?q=%2415m&src=cashtag_click). this single hack accounted for 30x the entire protocol's usage for the day.

![Hình ảnh](https://pbs.twimg.com/media/HGk1ByHXMAAnqaa?format=jpg&name=large)

on that same 24-hour window, the protocol generated $494,000 in earnings, split across bonders (node operators), LPs, the dev fund, affiliate integrators, and the marketing fund.

parallel flows went through a set of smaller but complementary privacy rails:

- umbra: a stealth-address protocol on ethereum. lets you send funds to a one-time-use address that only the recipient can compute from a shared secret. nobody watching the chain can tell who the real destination is. roughly [$78k](https://x.com/search?q=%2478k&src=cashtag_click) of initial activity was traced here before the tooling lost the thread.
- chainflip: another cross-chain dex, similar model to thorchain.
- bittorrent chain: a cheap, low-scrutiny sidechain connected to tron.
- tornado cash: the same mixer used for the original gas pre-funding. the us treasury sanctioned it in 2022.

each hop through these protocols multiplies tracing cost by ~10x. by the time you've gone through 5 layers, forensic firms can still theoretically follow every fragment, but the economic cost exceeds the value recovered.

# phase 7: bitcoin UTXO fragmentation

the ETH-to-BTC conversion via thorchain is about breaking the money into confetti.

ethereum has "accounts." your balance is a single number attached to your address. simple. bitcoin doesn't work that way. bitcoin has UTXOs, unspent transaction outputs, which are specific chunks of coin, each with its own full transaction history. every time you spend bitcoin, those chunks get split and recombined into new chunks.

![Hình ảnh](https://pbs.twimg.com/media/HGk2TmvXcAA5D5b?format=png&name=large)

imagine breaking a $100 bill into 87 pieces. then breaking each piece into 87 pieces. then doing that 7 times. technically, every fragment is still traceable back to the original bill. practically, no human forensic team can follow thousands of parallel chains in real time and assemble the picture fast enough to act.

so thorchain does two jobs at once: it moves the money across a border no sanctions can cross, and it fragments the money into untraceable dust.

# phase 8: the tron usdt rail

after bitcoin and the privacy layers, the funds reconverge on a single destination: USDT on tron.

most of you think money crime lives in BTC, it's false. it lives in USDT on tron. data shows USDT-tron carries the majority of illicit crypto volume every single year more than all other chains combined.

in the kelp flow specifically, funds are being bridged from BTC into tron, converted to USDT, then shuffled across additional tron addresses. each hop through tron is cheap enough that you can add 10 more layers of fragmentation for pennies.

# phase 9: the off-ramp. where crypto becomes cash.

at the end of every single hack, the money becomes fiat currency through a small set of specific, well-known human counterparties.

a network of OTC ("over-the-counter") brokers based in mainland china and southeast asia accepts USDT-tron deposits and pays out local-currency cash. these brokers are, in effect, unregistered banks. they aggregate flows from dozens of clients (legit and otherwise), net them internally, and settle in fiat using the chinese domestic payment rail (unionpay), which operates entirely outside the SWIFT network and western sanctions enforcement.

![Hình ảnh](https://pbs.twimg.com/media/HGk5L7xWMAAeGlC?format=jpg&name=large)

from those broker-controlled accounts, the money moves into DPRK-controlled bank accounts, often held by shell companies registered in hong kong, macau, or third-party jurisdictions. from there, it gets routed to pyongyang through a mix of hawala-style informal settlement, physical cash couriers, and procurement front companies.

the UN security council, the FBI, and the us treasury have each independently documented where these funds end up. north korea's ballistic missile program, nuclear weapons development, and evasion of international sanctions are partially funded by exactly these flows.

a 2024 UN report estimated that crypto hacks account for ~50% of the DPRK's total foreign-currency earnings, making this the primary funding mechanism for their weapons programs, ahead of coal exports, arms sales, and labor exports combined.