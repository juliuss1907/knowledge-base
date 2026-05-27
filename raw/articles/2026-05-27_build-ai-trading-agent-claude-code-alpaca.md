---
type: raw
source_type: article
source_url: https://www.mindstudio.ai/blog/build-ai-trading-agent-claude-code-alpaca
date_ingested: 2026-05-27
tags: [ai, agents, tools, economic]
status: unprocessed
---

# How to Build a 24/7 AI Trading Agent with Claude Code and Alpaca

**Source:** MindStudio Blog  
**URL:** https://www.mindstudio.ai/blog/build-ai-trading-agent-claude-code-alpaca  
**Ingested:** 2026-05-27

---

## Original Content

## What This Agent Actually Does

Most people who want an AI trading agent end up with one of two things: a rigid rule-based bot that can't adapt, or a one-shot Claude session that fires off a few trades and then goes quiet. Neither is what you actually want.

What you want is a Claude Code trading agent that wakes up on a schedule, scans the market, reasons about what to do, places trades through the Alpaca API, and logs everything to a structured journal — all without you touching it. That's what this guide builds.

The agent has three main jobs:

- **Research** — Pull market data, news, and technical signals for a defined watchlist.
- **Trade** — Evaluate what the research says and place buy/sell/hold orders through Alpaca.
- **Journal** — Write a structured log entry explaining every decision, including the ones where it did nothing.

This is a paper trading setup by default. You can flip it to live trading once you're confident in the agent's behavior, but starting on paper is the only sensible approach.

## Prerequisites

Before writing a single line of code, you need three things in place.

### An Alpaca Account

[Alpaca](https://alpaca.markets) offers commission-free stock and crypto trading with a proper REST API. Sign up for a free account and generate both a paper trading API key and a live trading API key. Keep them separate. You'll use paper keys throughout development.

Your .env file will look like this:

```
APCA_API_KEY_ID=your_paper_key_id
APCA_API_SECRET_KEY=your_paper_secret_key
APCA_BASE_URL=https://paper-api.alpaca.markets
```

### Claude Code Installed and Configured

You need Claude Code running locally. If you haven't set up [Claude Code with scheduled routines](https://www.mindstudio.ai/blog/claude-code-routines-24-7-agents) yet, do that first. The scheduling layer is what makes this agent genuinely autonomous rather than a script you run manually.

### A Basic File Structure

```
/trading-agent
  CLAUDE.md              # Agent instructions and persona
  watchlist.json         # Stocks/ETFs to monitor
  journal/               # Trade logs stored here
  scripts/
    research.py          # Data fetching helpers
    trade.py             # Order placement helpers
  .env                   # API credentials (never commit this)
```

You don't need everything built before you start. You'll build these out in sequence.

## Step 1: Define the Agent's Persona in CLAUDE.md

The CLAUDE.md file is the agent's operating manual. Claude Code reads it at the start of every session. This is where you set the rules of engagement.

Here's a solid starting template:

```markdown
# Trading Agent Instructions

You are an autonomous trading agent managing a paper portfolio.

## Your Core Responsibilities
- Every market day at 9:45 AM ET: Run the research routine
- Every market day at 10:00 AM ET: Evaluate research and place trades
- Every market day at 4:15 PM ET: Write a journal entry covering the day

## Rules You Must Always Follow
- Never invest more than 5% of total portfolio value in a single position
- Never place a market order — always use limit orders within 0.2% of ask
- If a position drops 8% from your entry, close it without waiting
- Always write a journal entry, even on days you make no trades
- Never place trades when market status is "closed"

## Decision Framework
Before placing any trade, answer these questions:
1. What is the current portfolio cash balance?
2. What positions are already open?
3. What does recent news say about this ticker?
4. What do the 20-day and 50-day moving averages tell you?
5. What is the risk if this trade goes wrong?

## Output Format
Every action must be logged to journal/YYYY-MM-DD.md in structured format.
```

The more specific you are here, the more predictable the agent's behavior. Vague instructions produce vague behavior.

## Step 2: Build the Research Skill

The agent needs to pull real market data before it can make decisions. This is a Python helper script that the agent calls as a tool.

```python
# scripts/research.py

import os
import requests
from datetime import datetime, timedelta
import json

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_BASE_URL")

def get_bars(symbol, timeframe="1Day", limit=60):
    """Fetch historical price bars for a symbol."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"https://data.alpaca.markets/v2/stocks/{symbol}/bars"
    params = {
        "timeframe": timeframe,
        "limit": limit,
        "adjustment": "raw"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_account():
    """Get current portfolio status."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"{BASE_URL}/v2/account"
    response = requests.get(url, headers=headers)
    return response.json()

def get_positions():
    """Get all open positions."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"{BASE_URL}/v2/positions"
    response = requests.get(url, headers=headers)
    return response.json()

def get_news(symbol):
    """Get recent news for a symbol."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"https://data.alpaca.markets/v1beta1/news"
    params = {
        "symbols": symbol,
        "limit": 5,
        "sort": "desc"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "account"
    symbol = sys.argv[2] if len(sys.argv) > 2 else None

    if action == "bars" and symbol:
        print(json.dumps(get_bars(symbol)))
    elif action == "news" and symbol:
        print(json.dumps(get_news(symbol)))
    elif action == "positions":
        print(json.dumps(get_positions()))
    else:
        print(json.dumps(get_account()))
```

The agent can call this script directly from a bash tool: `python scripts/research.py bars AAPL` returns 60 days of price bars as JSON. Claude can then calculate moving averages, identify trends, and factor in the news before making a decision.

## Step 3: Build the Trade Execution Skill

Placing trades through Alpaca's API is straightforward. The tricky part is building in the guard rails your agent needs before it can touch real money.

```python
# scripts/trade.py

import os
import requests
import json
import sys

ALPACA_KEY = os.getenv("APCA_API_KEY_ID")
ALPACA_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_BASE_URL")

def place_order(symbol, qty, side, limit_price=None):
    """Place a buy or sell order."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
        "Content-Type": "application/json"
    }

    order_data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,  # "buy" or "sell"
        "type": "limit" if limit_price else "market",
        "time_in_force": "day",
    }

    if limit_price:
        order_data["limit_price"] = str(limit_price)

    url = f"{BASE_URL}/v2/orders"
    response = requests.post(url, headers=headers, json=order_data)
    return response.json()

def cancel_all_orders():
    """Cancel all open orders."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"{BASE_URL}/v2/orders"
    response = requests.delete(url, headers=headers)
    return response.status_code

def get_market_status():
    """Check if the market is open."""
    headers = {
        "APCA-API-KEY-ID": ALPACA_KEY,
        "APCA-API-SECRET-KEY": ALPACA_SECRET,
    }
    url = f"{BASE_URL}/v2/clock"
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    action = sys.argv[1]

    if action == "status":
        print(json.dumps(get_market_status()))
    elif action == "order":
        symbol = sys.argv[2]
        qty = sys.argv[3]
        side = sys.argv[4]
        limit_price = sys.argv[5] if len(sys.argv) > 5 else None
        print(json.dumps(place_order(symbol, qty, side, limit_price)))
    elif action == "cancel":
        print(cancel_all_orders())
```

Notice that market orders are technically available in this script but the agent's CLAUDE.md instructs it to never use them. This is an important pattern: the safety rules live in the agent's instructions, not just in the code.

## Step 4: Set Up the Trade Journal

Every decision the agent makes gets logged. This is non-negotiable. If you don't know why the agent did something, you can't improve it and you can't catch it making mistakes.

The journal format is simple markdown:

```markdown
# Trade Journal — 2026-04-18

## Portfolio Status
- Cash: $12,450.00
- Positions: NVDA (42 shares @ $845.20), SPY (15 shares @ $521.00)
- Total Value: $23,891.80

## Market Research
### NVDA
- 20-day MA: $838.50 | 50-day MA: $812.00 — bullish trend intact
- News: Positive analyst upgrade from Morgan Stanley, +8% PT increase
- Earnings: 3 weeks out — potential catalyst

### AAPL
- 20-day MA: $195.20 | 50-day MA: $198.80 — short-term weakness
- News: Supply chain concerns in Taiwan Strait reporting
- Decision: No action, watch for stabilization

## Trades Executed
| Time | Symbol | Action | Qty | Price | Reasoning |
|------|--------|--------|-----|-------|-----------|
| 10:03 | NVDA | BUY | 5 | $847.50 | MA trend + analyst upgrade = entry |

## Positions Closed
None today.

## End-of-Day Reflection
NVDA trade aligned with thesis. Held off on AAPL given macro uncertainty in news.
Tomorrow: Watch SPY for any trend break below 50-day MA.
```

## Step 5: Schedule the Routines

The agent needs three scheduled routines:

1. **Research routine** — Runs at 9:45 AM ET, pulls data for all watchlist symbols
2. **Trade routine** — Runs at 10:00 AM ET, evaluates research and places orders
3. **Journal routine** — Runs at 4:15 PM ET, writes the day's summary

Use Claude Code's scheduling feature to set these up. Each routine is a separate session that reads the CLAUDE.md file and executes the appropriate sequence.

## Key Safety Patterns

- **Never invest more than 5% per position** — Prevents catastrophic losses from any single bad trade
- **Always use limit orders** — Prevents slippage during volatile periods
- **8% stop-loss rule** — Automatic position closure if trade goes wrong
- **Market status check** — Never trade when markets are closed
- **Always journal** — Even on no-trade days, document why

## Going Live: The Flip Switch

Once you're confident in the agent's behavior on paper trading:

1. Generate live API keys from Alpaca
2. Update your .env file with live credentials
3. Keep the paper trading setup as a staging environment
4. Start with smaller position sizes (2% instead of 5%)
5. Monitor the first week closely before scaling up

## Multi-Agent Setup (Optional)

Once the single-agent setup is stable, you can add a second agent that acts as a critic:

- **Agent A (Trader)** — Makes decisions and proposes trades
- **Agent B (Risk Reviewer)** — Reads Agent A's proposals and approves or rejects them

Agent B runs 15 minutes after Agent A and reads the journal file. If it finds a proposed trade it disagrees with, it flags it and sets a `review_required` field in the journal.

## Managing Token Costs

A trading agent running three times a day, five days a week will accumulate meaningful token usage:

- **Truncate historical data** — Pull 60 bars by default, not 500
- **Summarize the journal** — Pass summaries rather than full 30-day history
- **Set explicit tool budgets** — Cap the number of tool calls per session
- **Define "done" clearly** — Prevent runaway research loops

## Monitoring Without Babysitting

Two things make monitoring easy:

1. **Daily email digest** — Add a final step to the end-of-day routine that sends a summary email
2. **Exception-only alerts** — Only notify when something unexpected happens (failed API calls, orders rejected, etc.)

## Summary

This setup gives you a genuinely autonomous trading agent that:

- Runs on a schedule without manual intervention
- Pulls real market data and news
- Makes reasoned decisions based on technical and fundamental signals
- Places trades through a proper brokerage API
- Documents every decision in a structured journal
- Has multiple layers of safety checks
- Can be monitored without constant babysitting

Start with paper trading. Prove the agent works. Then flip to live trading when you're confident in its behavior.
