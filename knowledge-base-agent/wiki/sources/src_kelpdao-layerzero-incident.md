---
type: source
source_type: article
source_url: https://layerzero.network/blog/kelpdao-incident-statement
date_ingested: 2026-04-20
date_compiled: 2026-04-21
tags: [#crypto, #web3, #security]
status: active
---

# KelpDAO Incident Statement | LayerZero (2026-04-18)

## Tóm tắt

Ngày 18/04/2026, KelpDAO bị hack ~$290M. Thủ phạm: nhóm Lazarus (DPRK). Không lây lan sang cross-chain assets khác.

## Root Cause

KelpDAO dùng 1-of-1 DVN setup — LayerZero Labs là verifier duy nhất. Đi ngược lại khuyến nghị của LayerZero là dùng multi-DVN redundancy.

## Kỹ thuật tấn công (LayerZero Labs DVN Attack)

1. Attacker xâm nhập RPC infrastructure mà LayerZero Labs DVN dùng để verify transactions
2. KHÔNG phải through protocol exploit, DVN exploit, hay key management
3. Các bước:
   - Lấy danh sách RPCs của LayerZero DVN
   - Compromise 2 independent nodes (separate clusters)
   - Swap binaries trên op-geth nodes
   - Execute RPC-spoofing attack để forge message đến DVN
   - Malicious node nói thật với external RPCs nhưng nói dối với DVN
   - DDoS các RPCs không bị compromise để trigger failover sang poisoned RPCs

## Key Points

- LayerZero protocol hoạt động đúng như thiết kế
- Modular security đã work — attack bị isolate vào single application
- LayerZero Labs DVN giờ sẽ KHÔNG sign messages từ apps dùng 1/1 DVN config
- Đang liên hệ tất cả 1/1 DVN apps để migrate

## Source

https://layerzero.network/blog/kelpdao-incident-statement