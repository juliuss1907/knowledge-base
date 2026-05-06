---
type: raw
source_type: article
source_url: https://x.com/jito_sol/status/2051696304456184293
date_ingested: 2026-05-06
tags: [#crypto, #web3]
status: unprocessed
---

# Jito — Why We're Building JTX

**Author:** @jito_sol  
**Link:** https://x.com/jito_sol/status/2051696304456184293

---

## Tóm tắt

Jito công bố **JTX** — trading app mới cho Solana, built cho "serious traders" không phải tourists.

---

## Vấn đề hiện tại

- Solana có infrastructure tốt nhất crypto (400ms settlement, throughput cao)
- Nhưng ecosystem vẫn xây dựng piecemeal: swap router, charting, portfolio tracker — không work together
- Traders phải dùng **5-8 different tools**, tự làm middleware
- On-chain limit orders bị broken → 4/5 traders không tin tưởng

**Hyperliquid lesson:** Blockchains ready for traditional finance. Oil perps >$1B daily, S&P contracts $100M day one. Họ làm được trên L1 inferior rails vì "care more about what happens between the click and the settlement."

---

## JTX — What It Is

| Feature | Description |
|---|---|
| **One unified surface** | Charts + Execution + Portfolio + Capital management |
| **Perceived speed** | Visual feedback matters as much as actual speed |
| **Maker limit orders** | Fill dependably, display on chart |
| **Self-custody default** | Your wallet is your wallet — can't freeze funds |
| **Built for competence** | Not for tourists, không cần tutorial |

---

## Target Audience

> "We're building for the people who have opinions about execution quality."

- Không phải ngườI cần hướng dẫn limit order là gì
- Frustrated vì tools beneath them, không phải vì trading khó
- Trust earned through quality và architecture, không phải promises

---

## Core Philosophy

- **Craft matters:** Interface response under stress, loading state communicates progress
- **Trust through architecture:** Open, verifiable, aligned với ecosystem
- **Built to last:** Not for current cycle, for global finance onboarding
