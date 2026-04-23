---
type: source
source_type: article
source_url: https://zengineer.blog/blog/research/kelp-dao-292m-vulnerability-flagged-12-days-before/
date_ingested: 2026-04-20
date_compiled: 2026-04-21
tags: [#crypto, #web3, #security]
status: active
---

# Kelp DAO $292M Hack — AI Agent Phát Hiện 12 Ngày Trước

## Tóm tắt

Kelp DAO bị hack $292M ngày 18/04/2026. Root cause: 1-of-1 DVN config — một node bị compromise thì xác thực fraud message. 12 ngày trước, một Claude Code security skill đã cảnh báo đúng vấn đề này.

## Kelp DAO là gì

Liquid restaking protocol trên EigenLayer. Users deposit ETH/stETH/ETHx, nhận rsETH (liquid restaking token) dùng được across 16+ chains.

rsETH deploy trên 16+ blockchains dùng LayerZero OFT standard. Cross-chain bridge dựa vào LayerZero DVN (Decentralized Verifier Network).

Founded by Amitej Gajjala và Dheeraj Borra (trước đó Stader Labs co-founders). Kelp launched Dec 2023, peaked $2.09B TVL.

## The Hack

- 17:35 UTC: Attacker compromise single DVN node, forge cross-chain message via lzReceive
- Mint 116,500 rsETH trên Ethereum mainnet (claimed locked assets on another chain — không tồn tại)
- Deposit stolen rsETH làm collateral trên Aave V3, Compound V3, và Euler
- Borrow ~$236M in WETH
- Route ~74,000 ETH through Tornado Cash
- 18:21 UTC: Kelp emergency pauser multisig freeze contracts (46 min response)
- Two follow-up drain attempts (~$100M each) reverted

## Aftermath

- Aave V3 absorbed ~$177M bad debt
- AAVE token crashed 10.27%
- ETH dropped 3%
- rsETH across 20+ L2 networks left with questionable backing

## AI Security Tool Đã Phát Hiện Gì (April 6, 2026)

Claude Code skill (crypto-project-security-skill) chạy audit trên Kelp DAO 12 ngày trước hack, flags:

### Finding #1: DVN Configuration Opacity

"Kelp was running 1-of-1 DVN — one node, one point of failure"

### Finding #2: Single Point of Failure Across 16 Chains

"A single point of failure in LayerZero's DVN could simultaneously affect rsETH across all 16 supported chains"

### Finding #3: Cross-Chain Governance Controls Unverified

DVN config không nằm dưới 6/8 multisig/timelock như core protocol

### Finding #4: Ronin/Harmony Attack Pattern Match

Kelp's 16-chain deployment giống Ronin — bridge security là highest-risk vector

Ronin lost $625M (5 of 9 validators compromised); Harmony lost $100M (2 of 5). Kelp chỉ có 1.

## Tại sao Traditional Audits Missed

Kelp có 5+ code audits (Code4rena, SigmaPrime, MixBytes). Nhưng code scanners không catch:
- DVN threshold configuration
- Governance gaps at operational layer
- Architectural decisions above code level

## Key Lessons

1. Code audits ≠ protocol security
2. "DVN config not disclosed" = red flag
3. Single-point-of-failure DVN = 1-of-N attack threshold minimum
4. No insurance fund + cross-chain bridge = tail risk
5. Aave accepted rsETH as collateral without bridge risk assessment

## Timeline

| Date | Event |
|---|---|
| April 6, 2026 | Security report published |
| April 18, 2026 17:35 UTC | Attacker drains 116,500 rsETH ($292M) |
| April 18, 2026 18:21 UTC | Kelp emergency pause |

## Source

https://zengineer.blog/blog/research/kelp-dao-292m-vulnerability-flagged-12-days-before/