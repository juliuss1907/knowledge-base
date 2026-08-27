---
type: concept
status: draft
main_tag: crypto
sub_tags: [ai, tools]
topic: machine-economy-crypto
sources:
  - "[[src_is-there-anything-left-build-crypto-wintermute]]"
last_updated: 2026-07-17
---

# Autonomous Agents

## Definition

Autonomous agents (tác nhân tự chủ) là các hệ thống AI hoặc robotic có khả năng hoạt động độc lập trong thời gian dài — giữ context, đưa ra quyết định, thực thi hành động, và tự quản lý resources mà không cần sự giám sát liên tục của con người.

## Key ideas

- **Continuous operation:** Khác với narrow tools, agents giữ context và làm việc unattended qua thời gian
- **Decision making:** Có thể đưa ra quyết định dựa trên context và goals
- **Transaction capability:** Có thể thực hiện giao dịch tài chính
- **Self-management:** Quản lý resources của chính mình (compute, charging, maintenance)

## Distinction: Tool vs Agent

| Tool | Agent |
|------|-------|
| Chờ lệnh | Tự hành động |
| Thụ động | Chủ động |
| Cần hướng dẫn liên tục | Giữ context và goals |
| Không quyết định | Tự quyết định |
| Không giao dịch | Tự giao dịch |

## Capabilities

### Digital Agents
- Book flights, đàm phán giá, thanh toán, xử lý refunds
- Research và tổng hợp thông tin
- Trade và quản lý portfolio
- Tương tác với other agents

### Physical Agents (Robots)
- Nhận tasks và execute
- Charge own battery
- Pay for own compute
- Route income to operator
- Learn from human video (vision-language-action models)

### Scientific Agents
- Design experiments
- Requisition reagents
- Run experiment loops
- Analyze results
- Iterate without human in the building

## Economic Impact

- **Cost of digital work collapsing:** Làm tasks viable mà trước đây không đáng thời gian người
- **Changes automation economics:** Volume of activity systems must absorb tăng đáng kể
- **New coordination patterns:** Agents coordinate với nhau không cần human intermediaries

## Infrastructure Needs

- **Payment rails:** Protocols như x402, MPP, AP2
- **Identity systems:** Agent identity without human verification
- **Authorization layers:** Permissions và scope của actions
- **Dispute resolution:** Mechanisms khi agents make mistakes
- **Risk management:** Who carries fraud risk

## Current Examples

- **Trading agents:** Automated execution dựa trên signals
- **Booking agents:** Travel planning và booking end-to-end
- **Research agents:** Scientific experiment automation
- **Warehouse robots:** Task pricing, self-charging, self-payment

## Security Concerns

- **Prompt injection attacks:** Morse-code attack trên Grok → $150K-$200K loss
- **Authorization exploits:** Agent gaining permissions beyond scope
- **Chain of trust:** AI-assisted code bugs gây $1.78M bad debt

## Related concepts

- [[machine-economy]] — nền kinh tế nơi agents hoạt động
- [[agentic-commerce]] — giao thương giữa agents

## Sources

- [[src_is-there-anything-left-build-crypto-wintermute]] — bài viết của Wintermute

## Notes
