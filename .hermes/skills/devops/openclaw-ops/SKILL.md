---
name: openclaw-ops
description: Operate OpenClaw gateway, cron jobs, and LLM model routing (Kara agents). Covers config schema, contextWindow tuning, auth/rate-limit debugging, and cron failure recovery.
---

# OpenClaw Ops

Class-level skill for running and debugging OpenClaw (Kara) on this host. Use when touching `~/.openclaw/openclaw.json`, `~/.openclaw/cron/jobs.json`, cron runs, model selection, auth, or gateway lifecycle.

## When to Use

- `KB Compile Daily` / `KB Index Daily` fail with `Context overflow`, `FallbackSummaryError`, 401/403/410/429
- Need to change cron primary/fallback models, timeouts, or compaction floor
- `openclaw configure` wizard overwrote manual edits
- Gateway shows `invalid config: Unrecognized keys` or `gateway closed (1006)`
- Probing which `ollama`/`9router`/`api-box` models are alive, free, or subscription-gated

## Architecture (this host)

- Gateway binary: `/home/julius/.nvm/versions/node/v24.15.0/lib/node_modules/openclaw/dist/index.js` (`openclaw-gateway` via `systemctl --user`)
- Config: `~/.openclaw/openclaw.json` — hot-reloaded; invalid keys cause `config reload skipped`
- Cron: `~/.openclaw/cron/jobs.json` + `~/.openclaw/cron/runs` (JSONL) — query via `openclaw cron runs --id <id>`
- Auth: `~/.openclaw/agents/main/agent/auth-profiles.json` (google, ollama, opencode, openai-codex)
- Model catalogs: `models.providers.<provider>.models[]` (correct place for `contextWindow`); plugin models (e.g. `opencode`) are dynamic and not in `models.providers`

## Workflow 1 — Diagnose a Cron Failure

1. List: `openclaw cron list` → note `Name`, `Model`, `Status`, `ID`
2. History: `openclaw cron runs --id <id> > /tmp/runs.json` → `entries[]` (not `runs`), field `error`/`lastError` + `summary`
3. Classify error (see Reference: `references/model-failures.md`):
   - `Context overflow: prompt too large` → `contextWindow` too small or `reserveTokensFloor` too low
   - `401 Model not supported` / `410 retired` → model ID removed upstream
   - `403 insufficient quota` / `403 no quyền` → token lacks scope or quota 0
   - `403 requires subscription` → Ollama free vs paid tier
   - `429 rate_limit` → transient cooldown (retry after minutes)
   - `OAuth token refresh failed` → Codex token expired, needs re-auth
4. Verify liveness before patching (see Workflow 3)

## Workflow 2 — Patch Cron Models Safely

1. Edit `~/.openclaw/cron/jobs.json`: set `payload.model` (primary) + `payload.fallbacks[]` + `payload.timeoutSeconds: 600`. Keep at least 2 free fallbacks.
2. If touching `openclaw.json`, edit the **correct schema**:
   - ✅ `models.providers.<provider>.models[].contextWindow` / `maxTokens` — per-provider, per-model
   - ✅ `agents.defaults.compaction.reserveTokensFloor` — e.g. `50000` for Compile scanning `raw/`
   - ❌ `agents.defaults.models.<model>: {contextWindow}` — **invalid**, gateway rejects with `Unrecognized keys`
3. Backup first: `cp openclaw.json openclaw.json.bak-$(date +%Y%m%d)`
4. Restart gateway: `systemctl --user restart openclaw-gateway` → `systemctl --user is-active openclaw-gateway` → wait 6–8s before `openclaw cron run <id>` (avoids `1006 abnormal closure`)
5. Trigger: `openclaw cron run <id>` → wait for Telegram delivery or re-query `cron runs`

## Workflow 3 — Probe Model Liveness (don't guess)

```bash
KEY=$(python3 -c "import json; print(json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))['profiles']['ollama:default']['key'])")
for m in "nemotron-3-nano:30b" "nemotron-3-super" "gpt-oss:120b" "qwen3.5:397b"; do
  curl -s https://ollama.com/v1/chat/completions \
    -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
    -d "{\"model\":\"$m\",\"messages\":[{\"role\":\"user\",\"content\":\"hi\"}],\"max_tokens\":5}" | head -c 400
  echo " — $m"
done
curl -s http://localhost:20128/v1/models | python3 -m json.tool | head -n 40
```

- Success → `chatcmpl-*` with usage; Failure → `requires subscription`, `retired`, `not found`
- Known free (2026-08-21): `ollama/nemotron-3-nano:30b`, `ollama/nemotron-3-super`, `ollama/gpt-oss:120b`
- Known dead/gated: `opencode/minimax-m2.5-free` (401), `ollama/kimi-k2.5:cloud` (410 retired 2026-07-31), `ollama/minimax-m2.7:cloud`/`kimi-k2.6:cloud` (403 subscription), `api-box/deepseek-v4-flash[1m]` (403 no quyền with current token), `ai-box-vn/deepseek-v4-pro` (quota 0)

## Workflow 4 — Fix Context Overflow

- Symptom: `estimatedPromptTokens=14226 promptBudgetBeforeReserve=8000 overflowTokens=6226`
- Root cause check: `[1m]` in id means 1M upstream but config still `16000` → mismatch
- Fix: bump `models.providers.<prov>.models[].contextWindow` to real value (128k–1M) + `reserveTokensFloor` to 50000; verify no `agents.defaults.models` remains; restart gateway
- **Never** run `openclaw configure` after manual tuning — wizard resets floor to 20000 and drops custom windows

## Workflow 5 — Node Runtime Mismatch (update breaks gateway)

`openclaw update` upgrades the package in the nvm prefix, but the systemd unit's `ExecStart` may still point at the system Node (`/usr/bin/node`) — if that Node is older than the new package's `engines.node` requirement, the gateway crash-loops (5 restarts → systemd gives up silently). Sequence observed 2026-08-22: update to 2026.7.1-2 (requires ≥24.15.0) → `/usr/bin/node` is 24.14.1 → exit status 1 ×5 → gateway dead from 14:05 with no obvious alert.

1. Detect: `systemctl --user status openclaw-gateway` — `failed`, `Start request repeated too quickly`; test `node <dist>/index.js --version` with each Node runtime
2. Fix: edit `~/.config/systemd/user/openclaw-gateway.service` — change `ExecStart=/usr/bin/node` to the nvm Node that satisfies engines (`/home/julius/.nvm/versions/node/v24.15.0/bin/node`)
3. `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway`
4. Verify: `is-active` + port LISTEN (`ss -tlnp | grep 18789`) + HTTP probe `curl -s -m 5 http://127.0.0.1:18789`
5. Cleanup (Julius runs, needs sudo): `sudo npm rm -g openclaw` (removes root-owned duplicate in `/usr/lib` that causes EACCES on future updates) + `nvm alias default <version>`
6. Note: updater auto-selects "managed service Node" when runnables differ; after step 2 the service and nvm agree, so updates land cleanly

## Pitfalls

- `cron runs` JSON shape is `{entries:[], total, hasMore}`, not `{runs:[]}` — parsing `runs` yields 0.
- `openclaw cron run --id` is wrong; correct is `openclaw cron run <id>` (positional).
- Gateway `1006` right after restart is normal race — sleep before triggering.
- `google/gemma-4-31b-it` and `9router/oc/mimo-v2.5-free` rate-limit is transient — keep them as primary/candidate but ensure free ollama fallbacks behind them.
- OpenCode Zen models are plugin-supplied — their `contextWindow` is not in `openclaw.json` at all.
- Two openclaw installs can coexist: root-owned `/usr/lib/node_modules/openclaw` (from a past `sudo npm -g`) and the user's nvm copy. Shell PATH may resolve the system one; `openclaw update` then tries to write `/usr/lib` → EACCES. Remove the system copy rather than updating it with sudo.
- OpenClaw treats any directory containing `AGENTS.md` as a workspace and writes `openclaw-workspace-state.json` into CWD — KB root will keep regenerating this file. Fix at the git layer (`.gitignore`), not by deleting the file; see knowledge-base-validation hygiene table.

## Verification

- After patch: `python3 -c "import json,pathlib; d=json.loads(pathlib.Path('~/.openclaw/openclaw.json').expanduser().read_text()); print(d['agents']['defaults']['compaction']); print([(m['id'],m['contextWindow']) for m in d['models']['providers']['9router']['models']])"`
- After restart: `systemctl --user status openclaw-gateway | head` shows no `invalid config` line
- After run: `openclaw cron runs --id <id>` latest `status: ok` with `model/provider` populated (not `None/None`)

## References

- `references/model-failures.md` — error transcript catalog + liveness matrix from 2026-08-21 session
- `references/gateway-schema.md` — valid vs invalid config paths (with rejected-keys example)
