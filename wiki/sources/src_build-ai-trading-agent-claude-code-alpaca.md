---
type: source
original: [[2026-05-27_build-ai-trading-agent-claude-code-alpaca]]
main_tag: tech
sub_tags: [tutorial, automation, tools]
topic: ai-trading-agent-claude-code
date_compiled: 2026-05-28
url: https://www.mindstudio.ai/blog/build-ai-trading-agent-claude-code-alpaca
author: MindStudio
---

# How to Build a 24/7 AI Trading Agent with Claude Code and Alpaca

## Metadata

- **Source:** MindStudio Blog
- **URL:** https://www.mindstudio.ai/blog/build-ai-trading-agent-claude-code-alpaca
- **Date compiled:** 2026-05-28
- **Original:** [[2026-05-27_build-ai-trading-agent-claude-code-alpaca]]

## Summary

Tutorial xây dựng agent tự động giao dịch qua Alpaca API sử dụng Claude Code. Agent chạy 24/7 với 3 thành phần: Research (pull market data/news), Trade (đặt lệnh), Journal (ghi log). Sử dụng CLAUDE.md làm operating manual, kết hợp Python scripts (research.py, trade.py) gọi Alpaca API. Safety rules: max 5% per position, limit orders only, 8% stop-loss. Bắt đầu với paper trading trước khi chuyển live.

## Key points

- **3 routines:** Research (9:45 AM), Trade (10:00 AM), Journal (4:15 PM)
- **CLAUDE.md:** Agent instructions, rules of engagement, decision framework
- **Safety rules:** Max 5% per position, limit orders (0.2% of ask), 8% stop-loss, no market orders
- **Scripts:** research.py (get_bars, get_news, get_account), trade.py (place_order, get_market_status)
- **Paper trading default:** Sử dụng paper-api.alpaca.markets, flip to live khi confident
- **Journal format:** Markdown với portfolio status, market research, trades executed, end-of-day reflection
- **Multi-agent option:** Agent B (Risk Reviewer) review proposals của Agent A (Trader)
- **Token management:** Truncate historical data (60 bars), summarize journal, set tool budgets

## Concepts referenced

- [[ai-trading-agent]]
- [[claude-code-routines]]
- [[alpaca-api]]
- [[paper-trading]]
- [[agent-journal-pattern]]
- [[multi-agent-risk-review]]

## Original excerpts

> "What you want is a Claude Code trading agent that wakes up on a schedule, scans the market, reasons about what to do, places trades through the Alpaca API, and logs everything to a structured journal — all without you touching it."

> "The safety rules live in the agent's instructions, not just in the code. That way Claude reasons about them rather than blindly bypassing them."

> "Never invest more than 5% of total portfolio value in a single position. Never place a market order — always use limit orders within 0.2% of ask."
