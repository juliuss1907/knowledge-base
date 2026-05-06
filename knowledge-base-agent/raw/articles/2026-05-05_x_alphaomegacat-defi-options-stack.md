---
type: raw
source_type: article
source_url: https://x.com/alphaomegacat/status/2051624010564178077
date_ingested: 2026-05-05
tags: [#crypto, #finance]
status: unprocessed
---

# The Missing Link in DeFi and Solana's Derivatives Stack

**Author:** @alphaomegacat  
**Link:** https://x.com/alphaomegacat/status/2051624010564178077

---

## Tóm tắt

Thread phân tích lịch sử options market từ TradFi đến crypto, và tại sao DeFi options vẫn chưa "break through".

---

## 1. Lịch sử Options

**Pre-listed era (pre-1973):**
- Options tồn tại dưới dạng bespoke agreements giữa các bên
- Use cases: income generation, portfolio protection, flexible exposure

**CBOE Launch (1973):**
- 26 April 1973: CBOE mở cửa với 16 stocks, 911 call contracts
- 1975: OCC trở thành clearinghouse
- 1977: Put options được approve
- 1983: Index options (SPX)

**The 2019-2023 Retail Boom:**
- Commissions → zero (late 2019)
- Mobile-first execution
- COVID: time + cash + captive audience
- Retail share: 34% (2019) → 45-48% (2023)
- **0DTE options**: 5% (2016) → 51% (Q4 2024)

---

## 2. Retail Behavior

Không phải "mature" mà là **lottery-ticket behavior**:
- Short-dated, OTM, directional, convexity-seeking
- Mua short-dated convexity, overpay weekend gamma
- **Kết quả:** Tạo inefficiency cho institutions harvest

---

## 3. Crypto Options hiện tại

| Metric | Value |
|---|---|
| Derivatives vs Spot | 75-80% perps |
| Options volume | ~1% total |
| Non-Deribit options | ~0.10% |
| 0DTE SPX (TradFi) | 51% volume |

**Vấn đề:**
- Deribit = thị trường (6 linear + 2 inverse markets)
- Deposit requirements cao → retail bị lock out
- Paradigm = 20-40% Deribit volume (OTC/RFQ)
- Price discovery happens in private RFQ, not orderbook

---

## 4. DeFi Options Landscape

**Live projects:**

| Project | Architecture | Notes |
|---|---|---|
| **Paradex** | Off-chain orderbook, on-chain settlement | Perpetual options (rented convexity with funding) |
| **AEVO** | OP-stack Conduit + Eigen DA | Token-farm dynamics, userbase attrition |
| **Derive** | L2 OP-stack + Celestia DA | Only BTC/ETH/HYPE (FalconX partnership) |
| **Ithaca** | High-volume low-margin | Structurally risky, thin margins |
| **Rysk** | 5yo contracts, RFQ | 90% volume từ HYPE/wrappers |
| **Manifest/Dual** | P2P CLOB | May capture flow từ spot P2P growth |

**Problem chung:**
- Orderbooks khó maintain (expiry × strikes = fragmentation)
- Cần incentives liên tục
- Không có retail distribution như Robinhood

---

## 5. Key Insight

> "Options can't scale... when distribution, ticket size, standardisation, and repeatable user habits align."

**Crypto hiện tại:**
- ❌ No retail distribution
- ❌ High ticket size (deposit requirements)
- ❌ No standardization for retail
- ❌ No repeatable habits

→ Thị trường vẫn là "upstairs market" như pre-2019 TradFi.
