# OpenClaw (Kara) Troubleshooting

> How to diagnose and fix OpenClaw pipeline agent failures.
> Kara = Compile Agent + Index Agent + Fix Agent + Heartbeat, all running on OpenClaw runtime.

## Config Location

OpenClaw config: `~/.openclaw/openclaw.json`

Key sections:
- `agents.defaults.model.primary` — the model Kara uses for all agents
- `agents.defaults.model.fallbacks` — fallback models if primary fails
- `models.providers` — all available model providers with contextWindow/maxTokens

## Common Failure: "Context limit exceeded"

### Symptoms
- Ingest Agent works (simple task, short context)
- Compile Agent fails (reads raw files → writes sources + concepts, large context)
- Index Agent fails (scans all wiki files, very large context)
- Fix Agent fails (processes multiple files)
- Heartbeat fails (moderate context)

### Root Cause
Kara's primary model has too small a context window. Observed 2026-08-10: `api-box/deepseek-v4-flash[1m]` had `contextWindow: 16000` and `maxTokens: 4096` — 16K is insufficient for compile/index tasks that process 10+ files.

### Fix: Switch to larger context model

In `~/.openclaw/openclaw.json`, change `agents.defaults.model.primary`:

| Model | Context | Max Output | Suitable for |
|---|---|---|---|
| `api-box/deepseek-v4-flash[1m]` | 16K | 4K | Simple tasks only |
| `custom-api-ai-box-vn/deepseek-v4-pro` | 256K | 32K | Compile, Fix |
| `custom-api-ai-box-vn-2/deepseek-v4-pro[1m]` | 1M | 32K | All agents |

**Recommended:** `custom-api-ai-box-vn-2/deepseek-v4-pro[1m]` — 1M context handles all pipeline stages.

### Alternative: Add `reserveTokensFloor` equivalent

If OpenClaw supports compaction settings (similar to Hermes), add under `agents.defaults`:
```json
"compaction": {
  "reserveTokensFloor": 20000
}
```

## Pipeline Agent Health Check

When Kara's agents stop producing output, check in this order:

```bash
# 1. Check cron jobs (Hermes validators)
cronjob(action='list')  # via Hermes

# 2. Check last heartbeat
cat ~/knowledge-base/.openclaw/HEARTBEAT.md

# 3. Check last index success
cat ~/knowledge-base/.openclaw/last-index-success.txt

# 4. Check raw backlog
cat ~/knowledge-base/.openclaw/RAW_BACKLOG.md

# 5. Check OpenClaw memory for recent ingest activity
head -50 ~/knowledge-base/.openclaw/MEMORY.md

# 6. Check OpenClaw config for model/context issues
cat ~/.openclaw/openclaw.json | python3 -c "import json,sys; d=json.load(sys.stdin); print('Primary:', d['agents']['defaults']['model']['primary']); [print(f'{p}: {m.get(\"contextWindow\",\"?\")} ctx') for p,m in d['models']['providers'].items() for m2 in m.get('models',[]) if (m2.get('id','')==d['agents']['defaults']['model']['primary'].split('/')[-1])]"
```

## Agent State Indicators

| Agent | Health Check | Stale If |
|---|---|---|
| Ingest | `.openclaw/MEMORY.md` — latest entries | No new entries > 24h |
| Compile | New files in `wiki/sources/` and `wiki/concepts/` | No new files while `raw/` has unprocessed |
| Index | `.openclaw/last-index-success.txt` | Date > 2 days old |
| Fix | Status changes in `_action-required.md` | APPROVED reports not moving to APPLIED |
| Heartbeat | `.openclaw/HEARTBEAT.md` | Last updated > 24h |

## Pattern (2026-08-10)

Kara's agents stalled for 4 days (08-06 to 08-10). Only Ingest continued working. Root cause: `api-box/deepseek-v4-flash[1m]` with 16K context window couldn't handle compile/index/fix tasks. Fix: switch primary model to one with ≥256K context.