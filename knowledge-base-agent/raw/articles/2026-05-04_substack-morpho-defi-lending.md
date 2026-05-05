---
type: raw
source_type: article
source_url: https://open.substack.com/pub/afoxinweb3/p/morpho
date_ingested: 2026-05-04
tags: [#crypto, #finance]
status: processed
processed_date: 2026-05-05
---

# Morpho — DeFi Lending Juggernaut

**Tác giả:** A Fox in Web3  
**Nguồn:** Substack  
**Ngày:** 2026-04-09  
**Link gốc:** https://open.substack.com/pub/afoxinweb3/p/morpho

---

## Tóm tắt

Morpho là DeFi lending protocol với **$11 tỷ+ deposits** và **1.4 triệu users**, được hỗ trợ bởi Ethereum Foundation và các tên tuổi lớn trong crypto.

---

## Kiến trúc 2 lớp

| Lớp | Chức năng | Chi tiết |
|---|---|---|
| **Morpho Markets** | Nơi borrowing diễn ra | Permissionless — ai cũng có thể tạo market với collateral, oracle, interest rate tùy chọn |
| **Morpho Vaults** | Nơi lending/earn yield | ERC-4626 standard, deposits được allocate qua nhiều markets bởi "curators" (risk experts) |

**Isolation design:** Mỗi market tách biệt — nếu có vấn đề ở một market, không ảnh hưởng toàn protocol.

---

## Cách sử dụng

**Lending (Vaults):**
1. Vào app.morpho.org → Vaults
2. Chọn vault (xem curator, assets, allocation, historic performance)
3. Deposit → earn yield tự động
4. Withdraw anytime

**Borrowing (Markets):**
1. Chọn Markets → chọn market (vd: cbBTC collateral → borrow USDC)
2. Xem interest rate, liquidation threshold (vd: <86% collateral = liquidated)
3. Deposit collateral → borrow

---

## Điểm nổi bật

**Composable (ERC-4626):**
- Các protocol khác có thể plug straight vào Morpho Vaults
- Không cần custom integrations
- **Yieldseeker** là một ví dụ — tự động tìm vault tốt nhất trên Morpho và 10+ protocols khác

**Real World Assets (RWA):**
- Isolated market design phù hợp cho RWA
- Problem với một loại RWA collateral không ảnh hưởng protocol

---

## Sự kiện quan trọng gần đây

| Sự kiện | Chi tiết |
|---|---|
| **Ethereum Foundation** | Deposit **3,400 ETH** trực tiếp vào Morpho Vaults (treasury strategy) |
| **Apollo Global Management** | TradFi firm với **$938B AUM** — đồng ý acquire **9% MORPHO token supply** trong 4 năm |

→ Cả builders của Ethereum và nearly-trillion-dollar TradFi institution cùng đặt conviction vào Morpho.

---

## Bottom line

Morpho đang trở thành **lending infrastructure layer** của DeFi — essential primitive mà developers và protocols build on top.

Từ một app nhỏ ngồi trên Aave/Compound, Morpho đã trở thành một trong những protocol quan trọng nhất trong DeFi today.
