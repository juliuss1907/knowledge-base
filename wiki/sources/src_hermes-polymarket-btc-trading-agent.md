---
type: source
original: "[[raw/posts/2026-05-20_0xmovez-hermes-polymarket-btc-trading-agent.md]]"
main_tag: crypto
sub_tags: [automation, tools, tutorial]
topic: hermes-polymarket-trading-agent
date_ingested: 2026-05-20
date_compiled: 2026-05-21
url: https://x.com/0xMovez/status/2049891014249431141
author: Movez (@0xMovez)
---

# Hermes + Polymarket - how i built a self-learning BTC up/down trading agent 100$ → 5000$ ( guide )

## Metadata

- **Author:** Movez (@0xMovez)
- **Published:** 2026-05-17
- **Source:** X / Twitter
- **URL:** https://x.com/0xMovez/status/2049891014249431141
- **Type:** post

## Summary

Hướng dẫn xây dựng self-learning trading agent sử dụng Hermes Agent framework trên Polymarket Crypto UP/DOWN markets. Tác giả chia sẻ kiến trúc 3 lớp của Hermes, 5 loại trading bot phổ biến trên Polymarket, và ví dụ bots thành công với PnL hàng trăm nghìn USD. Trading bots đã tạo ra hơn $60M lợi nhuận trên Polymarket trong 2025-2026, với 77% đến từ thị trường Crypto UP/DOWN.

## Key points

- Trading bots trên Polymarket đã tạo ra hơn **$60M lợi nhuận** trong 2025-2026, 77% từ Crypto UP/DOWN markets
- **Hermes Agent** là framework tự học mã nguồn mở đạt 100,000+ GitHub stars trong 2 tháng, vượt qua Claude Code
- Phát triển bởi NousResearch (Paradigm đầu tư $70M), ra mắt 25/02/2026 với built-in self-learning loop
- Kiến trúc 3 lớp: Knowledge Layer (memory, wiki), Execution Layer (multi-agent, MCP), Output Layer (cron, gateway)
- 5 loại bot: Arbitrage (95-98% win rate), DCA, Momentum/Latency, Market Maker, AI/ML (Synth SDK)
- Ví dụ thành công: Gabagool22 ($1.2K → $868K), Sharky6999 ($852K PnL, 95.2% win rate)
- **Atomic** là native macOS AI assistant cho Hermes — 100+ integrations, persistent memory, one-click setup
- Có thể dùng local models (Gemma, Qwen, GLM) miễn phí hoặc paid APIs (Claude, Codex, Gemini)
- Mục tiêu: Xây dựng core logic, sau đó để AI tự học từ live trades thay vì hard-code rules

## Concepts referenced

- [[hermes-agent]]
- [[polymarket]]
- [[prediction-markets]]
- [[crypto-trading-bots]]
- [[atomic-mac-agent]]
- [[self-learning-agents]]
- [[bittensor]]

## Original excerpts

> *"All these factors together make Hermes the brain (not just the hands) of your trading setup - letting it adapt to market conditions rather than blindly following instructions you set once."*