---
type: raw
source_type: article
source_url: https://x.com/unhappyben/status/2046999944733626722
date_ingested: 2026-04-23
tags: [#crypto, #web3]
status: processed
processed_date: 2026-04-25
---
# How to Get Crypto to Fiat Without the Paper Trail

## Tóm tắt

Ben Pasternak viết về cách offramp crypto → fiat một cách private, không để lại dấu vết.

## Vấn đề

Muốn privacy nhưng CEX (Coinbase) tái tạo surveillance:
- Exchange log mọi transaction
- Bank yêu cầu proof of funds
- Toàn bộ financial map bị lộ khi cash out

Privacy coins (Monero, Zcash) không giải quyết được vì vẫn phải KYC để mua vào và cash out qua CEX.

## Giải pháp: Peer (do Ben tự build)

**Cách hoạt động:**
1. Gửi XMR → địa chỉ one-time deposit
2. USDC được sweep đến wallet mới (không có link giữa XMR và USDC)
3. Deposit USDC vào Peer → thêm username payment platform
4. Chờ counterparty gửi fiat cho mình
5. Bank chỉ thấy P2P transfer từ một người tên tuổi — không có crypto link

**Điểm hay:** Kiếm 1-3% spread khi offramp vì onramers muốn vào chain một cách private.

## Các route khác

| Asset | Route |
|---|---|
| Monero | XMR → Peer deposit address → USDC → Peer → Fiat |
| Zcash | Shielded ZEC → NEAR intents → Peer offramp (link broken at conversion) |
| Bitcoin/ETH/USDT | Gửi → Peer deposit address → Swept to USDC → Peer → Fiat |

## Privacy Pools (ETH)

- Deposit vào pool → được accept (không trong illicit set) → withdraw vào clean wallet
- Lưu ý: không thể deposit 1 ETH rồi withdraw cùng 1 ETH ngay — sẽ bị trace được
- Càng chờ lâu → anonymity càng cao

## Trích dẫn đáng chú ý

> "Onchain privacy has been solved for years, but the last mile is where everyone gave up and handed it to Coinbase. Peer fixes the last mile, and pays you to use it."

> "Privacy is normal."

