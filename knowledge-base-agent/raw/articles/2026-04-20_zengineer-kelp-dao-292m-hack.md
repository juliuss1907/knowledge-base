---
type: raw
source_type: article
source_url: https://zengineer.blog/blog/research/kelp-dao-292m-vulnerability-flagged-12-days-before/
date_ingested: 2026-04-20
tags: [#crypto, #web3, #security]
status: processed
processed_date: 2026-04-21
---
# Kelp DAO's $292M Hack: What an AI Agent Caught 12 Days Early

## What Is Kelp DAO?

Kelp DAO is a liquid restaking protocol built on EigenLayer. Users deposit ETH or liquid staking tokens (stETH, ETHx) into Kelp's contracts, which delegate those assets to EigenLayer operators for restaking. Users receive rsETH, a liquid restaking token usable across chains.

Kelp deploys rsETH on 16+ blockchains using LayerZero's OFT (Omnichain Fungible Token) standard. The cross-chain bridge relies on LayerZero's DVN (Decentralized Verifier Network) to validate messages.

Founded by Amitej Gajjala and Dheeraj Borra (previously Stader Labs co-founders), Kelp launched December 2023, peaked at $2.09B TVL, governed by a 6/8 multisig with 10-day timelock.

## The Hack

On April 18, 2026, attackers drained 116,500 rsETH (~$292M) — largest DeFi exploit of 2026.

**Root cause:** Configuration flaw — 1-of-1 DVN setup. One compromised node could approve fraudulent cross-chain messages.

**Attack timeline:**
- 17:35 UTC: Attacker compromised single DVN node, forged cross-chain message via lzReceive
- Minted 116,500 rsETH on Ethereum mainnet (claimed locked assets on another chain — they never existed)
- Deposited stolen rsETH as collateral on Aave V3, Compound V3, and Euler
- Borrowed ~$236M in WETH
- Routed ~74,000 ETH through Tornado Cash
- 18:21 UTC: Kelp emergency pauser multisig froze contracts (46 min response)
- Two follow-up drain attempts (~$100M each) reverted — the pause saved ~$200M more

**Aftermath:**
- Aave V3 absorbed ~$177M bad debt
- AAVE token crashed 10.27%
- ETH dropped 3%
- rsETH across 20+ L2 networks left with questionable backing

## What the AI Security Tool Caught — April 6, 2026

A Claude Code skill (crypto-project-security-skill) ran an audit on Kelp DAO 12 days before the hack. The report identified the exact attack surface:

### Finding #1: DVN Configuration Opacity (Prescient Signal)

Report flagged: "LayerZero DVN configuration not publicly disclosed"

Kelp was running 1-of-1 DVN — one node, one point of failure. The tool couldn't determine exact threshold (because Kelp never disclosed it), but called out this opacity as a red flag.

### Finding #2: Single Point of Failure Across 16 Chains (Direct Hit)

Report flagged: "A single point of failure in LayerZero's DVN could simultaneously affect rsETH across all 16 supported chains"

This is exactly what happened — the spoofed message compromised all chains where rsETH was deployed.

### Finding #3: Cross-Chain Governance Controls Unverified

Report flagged: Governance controls over OFT configuration may not fall under the same 6/8 multisig/timelock as core protocol.

In reality, DVN config was clearly not under rigorous governance — single admin key controlled it.

### Finding #4: Ronin/Harmony Attack Pattern Match (Direct Hit)

Report flagged: Kelp's 16-chain deployment similar to Ronin's architecture — bridge security was the highest-risk vector.

Ronin lost $625M (5 of 9 validators compromised); Harmony lost $100M (2 of 5 validators). Kelp had only 1 validator.

## Why Traditional Code Audits Missed This

Kelp had 5+ code audits from Code4rena, SigmaPrime, MixBytes. But code scanners can't catch:
- DVN threshold configuration
- Governance gaps at operational layer (bridge configs, oracle parameters)
- Architectural decisions above code level

## Key Lessons

1. **Code audits ≠ protocol security** — configuration and governance risks sit above code
2. **"DVN config not disclosed" = red flag** — should have pulled risk score lower
3. **Single-point-of-failure DVN = 1-of-N attack threshold minimum** — industry minimum is 2-of-3
4. **No insurance fund + cross-chain bridge = tail risk** — downstream protocols absorb the loss
5. **Aave accepted rsETH as collateral without bridge risk assessment** — downstream risk was not priced

## Timeline

| Date | Event |
|---|---|
| April 6, 2026 | Security report published — flags DVN opacity, single point of failure, Ronin pattern match |
| April 18, 2026 17:35 UTC | Attacker forges cross-chain message, drains 116,500 rsETH ($292M) |
| April 18, 2026 18:21 UTC | Kelp emergency pause activated (46 min response) |

## References

- crypto-project-security-skill: https://github.com/truenorth-lj/crypto-project-security-skill
- Full Kelp report: https://github.com/truenorth-lj/crypto-project-security-skill/blob/main/docs/examples/kelp-liquid-restaking.md
