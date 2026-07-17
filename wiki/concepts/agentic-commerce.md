---
type: concept
status: draft
main_tag: crypto
sub_tags: [ai, tools]
topic: machine-economy-crypto
sources:
  - "[[src_is-there-anything-left-to-build-in-crypto-wintermute]]"
last_updated: 2026-07-17
---

# Agentic Commerce

## Definition

Agentic commerce (giao thương tác nhân) là hình thức giao dịch và thương mạI diễn ra giữa các autonomous agents — các tác nhân AI hoặc robotic có khả năng tự chủ trong việc đàm phán, thanh toán, và thực thI hợp đồng mà không cần sự can thiệp của con ngườI trong vòng lặp.

## Key ideas

- **The Hard Part:** Không phảI agent có thể thanh toán hay không, mà là:
  - Who holds authority when the agent is wrong
  - Who carries the fraud risk
  - How this reaches merchants without rebuilding checkout
- **Shape đang được định hình:** Authorization layers, agent identity, neutral routing between rails, markets where agents buy their own compute, data, and access
- **Business model:** Better teams charge cho authorization và risk reduction thay vì cut của payment value — làm business viable trước khi agent volume thực sự lớn

## Challenges

### Security
- Agent wallets đã là live attack surface
- **May 2026:** Attacker dùng Morse-code prompt injection để Grok output transfer instruction, automated trading agent execute on-chain → mất ~$150K-$200K trước khi recovery (SlowMist)

### Liability
- Vấn đề chưa được giảI quyết: who is responsible when AI-touched system fails
- **Feb 2026:** AI-assisted smart contract code có oracle bug gây $1.78M bad debt event trên Moonwell — nothing in review chain caught it

## Building Blocks

### Economic Layer for Agents
- Authorization layers — xác thực agent có quyền gì
- Agent identity — định danh tác nhân tự chủ
- Neutral routing between rails — không phụ thuộc vào một provider
- Markets cho compute, data, access — nơI agents tự mua resources

### Physical AI Integration
- Robots cần wallets để:
  - Fund their own compute
  - Pay for charging và maintenance
  - Get paid for work they do
- **"The wallet is missing, not the hands"**

## Opportunity

Phần lớn hoạt động hiện tạI nằm ở components: foundation models, robot hardware, stablecoins, exchanges. Các markets này đã crowded.

**Opportunity nằm ở what connects them** — rails cho transaction, coordination, và trust giữa machines.

## Related concepts

- [[machine-economy]] — nền kinh tế máy móc rộng hơn
- [[autonomous-agents]] — các tác nhân thực hiện commerce

## Sources

- [[src_is-there-anything-left-to-build-in-crypto-wintermute]] — bàI viết của Wintermute

## Notes
