---
type: concept
status: draft
tags: [#crypto, #finance]
related_concepts: ["DeFi-on-Prediction-Markets"]
sources: ["src_trepa-prediction-market"]
compiled_date: 2026-05-07
---

# Trepa — Numerical Prediction Market

## Mô tả

**Trepa** là prediction market độc đáo ở top-right quadrant: numerical value + accuracy-scaled payout. Khác với Polymarket (directional), Trepa yêu cầu traders submit numerical predictions và được reward theo accuracy.

## Precision Gap của Binary Markets

Polymarket/Kalshi: "Will Fed raise rates above 5.5?" — Trader A dự đoán 5.55% và Trader B dự đoán 6.5% → cùng collect $1. **Magnitude bị bỏ qua.**

## Trepa Flashpools

- 30 giây submit price prediction (BTC price)
- Entry: 1 USDC flat
- Win condition: error below median → nhận lại entry + share prize pool
- Payout weighted by accuracy (không phải direction)

## 4 Quadrants của Prediction Markets

| | Directional | Numerical |
|---|---|---|
| **Binary payout** | Polymarket, Kalshi | (empty) |
| **Accuracy-scaled** | Augur scalar (failed) | **Trepa — Alone** |

## Dominant Strategy

| Platform | Strategy | Input |
|---|---|---|
| **Polymarket** | Directional conviction | Sentiment, narrative |
| **Trepa** | Minimize absolute error | Modelling actual numerical outcome |

## Liên quan

- [[DeFi-on-Prediction-Markets]]

## Nguồn tham khảo

- Baheet @ X