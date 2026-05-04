---
type: raw
source_type: repo
source_url: https://github.com/aattaran/deepclaude
date_ingested: 2026-05-04
tags: [#ai, #coding]
status: unprocessed
---

# deepclaude — Use Claude Code with DeepSeek V4 Pro

**Owner:** aattaran  
**Repo:** deepclaude  
**License:** MIT  
**Stars:** 321  
**Forks:** 16  

---

## What it does

Use Claude Code's autonomous agent loop with **DeepSeek V4 Pro**, **OpenRouter**, or any Anthropic-compatible backend. Same UX, **17x cheaper**.

Claude Code costs $200/month with usage caps. DeepSeek V4 Pro scores 96.4% on LiveCodeBench and costs $0.87/M output tokens.

**Architecture:**
```
Your terminal
  +-- Claude Code CLI (tool loop, file editing, bash, git - unchanged)
        +-- API calls -> DeepSeek V4 Pro ($0.87/M) instead of Anthropic ($15/M)
```

---

## Quick start

### 1. Get API key
Sign up at platform.deepseek.com, add $5 credit, copy API key.

### 2. Set environment variables
```shell
# Windows (PowerShell)
setx DEEPSEEK_API_KEY "sk-your-key-here"

# macOS/Linux
echo 'export DEEPSEEK_API_KEY="sk-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Install
```shell
# macOS/Linux
chmod +x deepclaude.sh
sudo ln -s "$(pwd)/deepclaude.sh" /usr/local/bin/deepclaude
```

### 4. Use
```shell
deepclaude                  # Launch with DeepSeek V4 Pro
deepclaude --status         # Show available backends
deepclaude --backend or     # Use OpenRouter ($0.44/M input)
deepclaude --backend fw     # Use Fireworks AI (fastest)
deepclaude --backend anthropic  # Normal Claude Code
deepclaude --cost           # Pricing comparison
deepclaude --benchmark      # Latency test
```

---

## Supported backends

| Backend | Flag | Input/M | Output/M | Servers | Notes |
|---|---|---|---|---|---|
| **DeepSeek** (default) | `--backend ds` | $0.44 | $0.87 | China | Auto context caching (120x cheaper on repeat turns) |
| **OpenRouter** | `--backend or` | $0.44 | $0.87 | US | Cheapest, lowest latency from US/EU |
| **Fireworks AI** | `--backend fw` | $1.74 | $3.48 | US | Fastest inference |
| **Anthropic** | `--backend anthropic` | $3.00 | $15.00 | US | Original Claude Opus |

---

## Cost comparison

| Usage level | Anthropic Max | deepclaude (DeepSeek) | Savings |
|---|---|---|---|
| Light (10 days/mo) | $200/mo (capped) | ~$20/mo | 90% |
| Heavy (25 days/mo) | $200/mo (capped) | ~$50/mo | 75% |
| With auto loops | $200/mo (capped) | ~$80/mo | 60% |

---

## What works / What doesn't

### Works
- File reading, writing, editing
- Bash/PowerShell execution
- Glob and Grep search
- Multi-step autonomous tool loops
- Subagent spawning
- Git operations
- Project initialization (`/init`)
- Thinking mode

### Doesn't work
- Image/vision input (DeepSeek's endpoint doesn't support)
- Parallel tool use (Claude Code sends sequentially by default)
- MCP server tools (not supported through compatibility layer)
- Anthropic's `cache_control` (DeepSeek has its own automatic caching)

---

## Intelligence difference

- **Routine tasks** (80% of work): DeepSeek V4 Pro is comparable to Claude Opus
- **Complex reasoning** (20%): Claude Opus is stronger

---

## Live switching (no restart)

Switch between backends **mid-session** using slash commands:

Add to `~/.claude/commands/`:
- `deepseek.md` → type `/deepseek` to switch
- `anthropic.md` → type `/anthropic` to switch
- `openrouter.md` → type `/openrouter` to switch

Proxy runs on `localhost:3200` and intercepts API calls.

---

## Key insight

DeepSeek V4 Pro offers comparable performance to Claude Opus for routine coding tasks at a fraction of the cost, making it a viable alternative for developers looking to reduce AI tooling expenses while maintaining productivity.
