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

### Fix: Match configured contextWindow to the model's REAL window

⚠️ Config drift (found 2026-08-21): `[1m]`-suffix models were configured with `contextWindow: 16000` although their real windows are 256K–1M. The framework trusts the config value, compacts prematurely, and dies with `FallbackSummaryError: All models failed` even though providers had plenty of room. Always set contextWindow to the true size.

Model status (verified 2026-08-22):

| Model | Real context | Status |
|---|---|---|
| `9router/oc/mimo-v2.5-free` | 128K | ✅ working free primary (occasional rate-limit cooldowns) |
| `ollama/nemotron-3-nano:30b` | large | ✅ working free fallback |
| `ollama/nemotron-3-super` | large | ✅ working free fallback |
| `ollama/gpt-oss:120b` | large | ✅ working free |
| `google/gemma-4-31b-it` | 128K | ✅ works, sometimes rate-limited |
| `opencode/minimax-m2.5-free` | — | ❌ dead (HTTP 401 "model not supported") |
| `ollama/kimi-k2.5:cloud` | — | ❌ retired 2026-07-31 |
| `ollama/minimax-m2.7:cloud` / `kimi-k2.6:cloud` | — | ❌ 403 subscription required |
| `openai-codex/gpt-5.4` | — | ⚠️ OAuth refresh expires — re-auth or drop |
| `api-box/deepseek-v4-flash[1m]` / `-pro[1m]` | 256K / 1M | ⚠️ 403 "Token không có quyền truy cập" on current key |

**Recommended chain:** primary `9router/oc/mimo-v2.5-free` → fallbacks `ollama/nemotron-3-nano:30b` → `ollama/nemotron-3-super` → `google/gemma-4-31b-it`. Rate-limit cooldowns (1–15 min) are temporary — don't hammer retries during cooldown.

### Compaction settings — CONFIRMED working

`agents.defaults.compaction.reserveTokensFloor` exists and matters. Set **50000** (20000 is too low for raw/-scale scans):

```json
"compaction": { "reserveTokensFloor": 50000 }
```

⚠️ NEVER run `openclaw configure` — the wizard resets `reserveTokensFloor` to 20000 and strips custom `contextWindow` values. Edit `~/.openclaw/openclaw.json` by hand, then `systemctl --user restart openclaw-gateway.service`.

## Gateway won't start after `openclaw update` (2026-08-22)

The systemd unit `~/.config/systemd/user/openclaw-gateway.service` hardcodes an ExecStart node path. After an update, two failure modes appear:

1. **Unit runs system node** (`/usr/bin/node`) which is older than the nvm node the package was upgraded for → gateway exits instantly, systemd hits `StartLimitBurst=5` and gives up silently ("Start request repeated too quickly").
2. Unit runs nvm node but package now requires a newer node than installed.

Fix pattern:
```bash
systemctl --user status openclaw-gateway.service   # confirm crash-loop / failed
# point ExecStart at the nvm node matching the upgraded package:
sed -i 's|^ExecStart=/usr/bin/node |ExecStart=/home/julius/.nvm/versions/node/v24.15.0/bin/node |' \
  ~/.config/systemd/user/openclaw-gateway.service
systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service
ss -tlnp | grep 18789   # verify port listens; curl 127.0.0.1:18789
```

Related: `openclaw update` as user julius hits npm EACCES on `/usr/lib/node_modules/openclaw` (old root-owned global install). Fix: `sudo npm rm -g openclaw`, then update inside nvm prefix only.

## Runtime artifacts leak into KB root (recurring, systematic)

OpenClaw sessions write working files to CWD (= KB root) instead of agent home `.openclaw/`. Observed leaks: `memory/` (6+ times Jul–Aug), empty `state/` phantom dir, `openclaw-workspace-state.json`. All get git-tracked by the ~5-min `vault backup` auto-commit, so plain deletion resurrects them.

Durable fix per artifact: redirect the writer's output path → `.openclaw/`, then `git rm <artifact>` + commit, and add a `.gitignore` guard line. Root-level cleanup is Connor-approved inline work (see approval workflow in SKILL.md).

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