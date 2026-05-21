---
type: post
title: "Hermes + Polymarket - how i built a self-learning BTC up/down trading agent 100$ → 5000$ ( guide )"
url: https://x.com/0xMovez/status/2049891014249431141
author: Movez (@0xMovez)
date_published: 2026-05-17
date_ingested: 2026-05-20
status: processed
compiled_at: 2026-05-21
compiled_to: [[wiki/sources/src_hermes-polymarket-btc-trading-agent.md]]
source: X / Twitter
---

# Hermes + Polymarket - how i built a self-learning BTC up/down trading agent 100$ → 5000$ ( guide )

**Tác giả:** Movez (@0xMovez)  
**Nguồn:** X / Twitter  
**Ngày đăng:** 2026-05-17

---

## Thị trường Polymarket Crypto UP/DOWN

Trading bots/agents trên Polymarket đã tạo ra hơn **$60M lợi nhuận** trong 2025-2026. **77%** trong số đó đến từ thị trường Crypto UP/DOWN — nhờ vào các **inefficiencies liên tục** trong phân khúc này.

Thị trường không ngừng phát triển: để duy trì lợi nhuận, bạn cần hoặc liên tục tìm kiếm inefficiencies mới, hoặc xây dựng **self-learning agents** tự động hóa việc đó.

## Tại sao chọn Hermes?

**Hermes Agent** là agent tự học mã nguồn mở đạt hơn **100,000 GitHub stars** trong chưa đầy 2 tháng. Đến ngày 27/04/2026, repo Hermes đã vượt qua Anthropic's Claude Code về tổng số stars — tín hiệu rõ ràng về độ hữu ích của framework này.

Hermes được phát triển bởi **NousResearch** (AI research lab được Paradigm đầu tư $70M), creators của Nomos & Psyche — ra mắt ngày 25/02/2026, với **built-in self-learning loop** giúp agent càng chạy càng thông minh.

## Kiến trúc 3 lớp của Hermes

| Lớp | Chức năng |
|-----|-----------|
| **Knowledge Layer** | Built-in memory, session search, LLM-Wiki skill, optional Honcho integration — Agent không chỉ trả lời mà còn **tích lũy kiến thức theo thời gian** |
| **Execution Layer** | Multi-agent profiles, child agents, tool system, MCP support, persistent machine access — Agent không chỉ phản hồi mà còn **phân rã tasks, chạy song song, và delegate** |
| **Output Layer** | Cron jobs, gateway delivery (Telegram/Slack/Discord), Web UI, file output — Kết quả **chảy vào workflow thực**, không bị mắc kẹt trong chat window |

## 5 loại trading bot trên Polymarket Crypto UP/DOWN

| Loại bot | Cơ chế | Win rate |
|----------|--------|----------|
| **Arbitrage (Pair Cost)** | Mua cả hai phía (YES + NO) khi tổng giá dưới $1, chốt lời $0.02–$0.04 risk-free | 95–98% |
| **DCA Bot** | Chờ một phía giảm dưới $0.35, trung bình giá xuống đến khi cost < $0.99 | — |
| **Momentum / Latency Bot** | Monitor BTC spot price trên Binance/Coinbase, vào Polymarket trong khoảng delay repricing | — |
| **Market Maker** | Đặt lệnh hai chiều trên market 5-phút BTC, capture spread | — |
| **AI/ML Bot (Synth SDK)** | Dùng Bittensor AI forecast probabilities 20 phút trước đóng market với edge 10%+ | — |

## Ví dụ bots thành công

- **Gabagool22** — Arbitrage bot huyền thoại: $1.2K → **$868K**
- **Sharky6999** — Bot ổn định nhất: **$852K PnL**, win rate 95.2%
- **[redacted]** — HFT bot mới: **$728K** trong một tháng

## Setup Hermes qua Atomic (macOS)

**Atomic** là native macOS AI assistant — không phải browser tab, không phải CLI wrapper, không phải "ChatGPT với nút bấm". Đây là autonomous agent với **tay, mắt, bộ nhớ, và workspace thực**.

Atomic cung cấp:
- 100+ integrations
- Thư viện skills pre-installed lớn
- Persistent memory
- Support tất cả major AI models (Claude, ChatGPT, Gemini)
- **One-click setup**

### Các bước cơ bản

1. **Cài đặt Atomic app** hoặc chạy trên Cloud
2. **Chọn Hermes agent** từ main page
3. **Connect model API** — có thể dùng local models (Gemma, Qwen, GLM) miễn phí hoặc paid APIs (Claude, OpenAI Codex, Google AI)
4. **Bắt đầu build** trading logic qua Chat tab hoặc CLI

### Gợi ý model

Sau update OpenAI gần nhất, tác giả chọn **Codex** làm code engine cho agent logic — chỉ cần mua ChatGPT Plus plan và connect vào Atomic.

## Mục tiêu

Xây dựng core trading logic cho Hermes Agent trên thị trường crypto UP/DOWN — sau đó, thông qua **live trades** và **self-learning capability**, để AI làm phần nặng nh nhọc.

> *"All these factors together make Hermes the brain (not just the hands) of your trading setup - letting it adapt to market conditions rather than blindly following instructions you set once."*
