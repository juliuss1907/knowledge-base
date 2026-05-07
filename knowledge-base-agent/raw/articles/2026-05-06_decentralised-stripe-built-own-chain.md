---
type: raw
source_type: article
source_url: https://www.decentralised.co/p/why-stripe-built-its-own-chain
date_ingested: 2026-05-06
tags: [#crypto, #finance, #web3]
status: processed
processed_date: 2026-05-07
---
# Why Stripe Built Its Own Chain
**Source:** Decentralised.co  
**Link:** https://www.decentralised.co/p/why-stripe-built-its-own-chain  
**Date:** May 6, 2026
---
## Tóm tắt
Stripe đang xây dựng stack thanh toán cross-border vertical integrated — từ acceptance đến settlement — để capture phần lớn $240B revenue pool của cross-border payments thay vì để các intermediaries (banks, FX desks, SWIFT) lấy phí.
---
## Context
- Stripe 2025: **$6.9B revenue**, xử lý **$1.9T** payments (~1.6% global GDP)
- Cross-border flows 2024: **$190T**, tạo ra **$240B** revenue cho banks/intermediaries
- Cost gửi $200 cross-border: **6.5%** (gấp đôi UN target 3%)
- Đây là **single largest fee pool** trong global payments
---
## 7 Layers của Cross-Border Payment
| Layer | Description | Who Owns (Before) |
|-------|-------------|-------------------|
| 1. **Acceptance** | Capture payment từ customer | Stripe |
| 2. **Orchestration** | API routing | Stripe |
| 3. **Licensing** | Regulatory coverage | Partner banks |
| 4. **Custody** | Hold funds in flight | BNY Mellon, State Street |
| 5. **FX** | Currency conversion | Correspondent banks |
| 6. **Issuance** | Stablecoin/fiat representation | Tether, Circle |
| 7. **Settlement** | Final movement | SWIFT |
**Problem:** Stripe chỉ own 2/7 layers → value leak ở mỗi step
---
## Stripe's Acquisitions & Moves
**October 2024:** Acquire **Bridge** ($1.1B)
- Money transmitter licenses across 30 US states
- Custody với BlackRock, Fidelity, Superstate
- FX desk
- USDB stablecoin
→ **Own layers 3-6**
**September 2025:** Announce **Tempo** (với Paradigm)
- Payment-focused L1 blockchain
- Ithaca team (Reth contributors) build execution
- EVM-compatible
**March 2026:** Tempo mainnet live
- Gas paid in approved stablecoins (không cần native token)
- Sub-second deterministic finality
- **$0.001/transaction**
**April 2026:** **Visa** join as anchor validator
→ **Own all 7 layers**
---
## Revenue Potential
Target 2027: **$10B/month** → **~$1B/year** additional revenue
| Layer | Revenue Estimate |
|-------|------------------|
| Licensing | $100-200M |
| FX (30bps spread) | ~$360M |
| Issuance (4-5% yield on $10B float) | ~$450M |
---
## Key Insight
> "Concept of 'domestic markets' doesn't make sense for internet businesses. The share of cross-border payments cannot be ignored anymore."
Stripe không chỉ là payment processor — đang trở thành **full-stack financial infrastructure** từ acceptance đến settlement, bypass tất cả intermediaries.
