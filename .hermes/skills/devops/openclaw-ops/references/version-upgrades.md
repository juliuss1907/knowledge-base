# OpenClaw Version Upgrade Log + Retired-Key Archaeology

## 2026-09-08 — node v24.15.0 → v24.20.0, openclaw 2026.7.1-2 → 2026.9.3

### Engines floor check (step 0)

```
$ npm view openclaw version   → 2026.9.3
$ npm view openclaw engines   → { node: '>=24.16.0 <25 || >=26.1.0' }
```

The running node (v24.15.0) was BELOW the new floor — node bump is a hard prerequisite for the openclaw upgrade. The floor moves every release; always check before choosing the node version.

### Global package migration

npm ≥11 blocks install-scripts by default. The first `npm i -g` warned:

```
npm warn install-scripts   koffi@... (install: node-gyp-build)
npm warn install-scripts   tree-sitter-bash@0.25.1 (install: node-gyp-build)
npm warn install-scripts   protobufjs@7.6.6 (postinstall: node scripts/postinstall)
npm warn install-scripts Run `npm install -g --allow-scripts=openclaw,@google/genai,koffi,tree-sitter-bash,protobufjs` to allow these scripts
```

Re-ran with the allow-list → openclaw 2026.9.3, pm2 7.0.4, clawhub 0.23.3, mcporter 0.13.10. Without it, native deps (koffi, tree-sitter) ship unbuilt → runtime breakage.

### First gateway start failed: exit 78

```
Process: .../v24.20.0/bin/node .../openclaw/dist/index.js gateway --port 18789 (code=exited, status=78)
[gateway] requires state database schema migration. Stop the service ... run openclaw doctor --fix ...
Gateway failed to start: failed to acquire plugin lifecycle lease core:plugin-lifecycle/global |
OpenClaw state database schema migration required (audit-events-v2) at ~/.openclaw/state/openclaw.sqlite
```

Status 78 = CONFIG-class failure. Backup `openclaw.sqlite` (~23 MB) → `openclaw doctor --fix` → "Doctor complete". Restart → active, HTTP 200 (after ~13s warmup; HTTP 000 at 5s was just slow boot, not failure).

### Doctor --fix silently rewrote openclaw.json

Diff against pre-upgrade backup (2026-09-02):

REMOVED:
- `agents.defaults.compaction.reserveTokensFloor: 50000` ← the floor

ADDED (benign migrations):
- `agents.defaults.modelPolicy.allow: [...]` (from legacy `agents.defaults.models` restriction)
- `agents.entries.main: {}`
- `channels.telegram.groupAllowFrom`, discord/slack enabled entries
- ollama model `params.num_ctx: 128000`
- long list of `plugins.entries.<id>.enabled: false` normalizations
- `meta.lastRunCommand: "doctor"`, `meta.migrations.modelPolicyAllowlist: true`

**Key insight: `reserveTokensFloor` was not lost by accident — it is officially retired.** Evidence chain (dist of 2026.9.3):

1. `dist/legacy-*.mjs` → `RETIRED_AGENT_TUNING_PATHS = [["compaction","reserveTokens"],["compaction","reserveTokensFloor"],["compaction","maxHistoryShare"], ["contextPruning",...] ...]`
2. Migration id `runtime.tuning-knobs-purge` ("Remove retired runtime tuning knobs... built-in defaults now apply") calls `stripRetiredTuningKnobs()` which deletes these at every agent config scope
3. Replacement getter: `dist/resource-loader-*.mjs` → `getCompactionReserveTokens() { return this.settings.compaction?.reserveTokens ?? 16384; }` — reads from **per-agent settings**, not openclaw.json
4. New default floor: `dist/agent-settings-*.mjs` → `DEFAULT_AGENT_COMPACTION_RESERVE_TOKENS_FLOOR = 2e4` (=20000) — exactly the value the wizard used to force
5. Effective reserve = `min(max(reserveTokens, floor), floor(contextWindow * 0.25))` — `MAX_COMPACTION_RESERVE_RATIO = .25` in `dist/agent-compaction-constants-*.mjs`

### Fix: move the floor to per-agent settings

`~/.openclaw/agents/main/agent/settings.json` and `~/.openclaw/agents/kara/agent/settings.json` (neither existed before; created fresh):

```json
{
  "compaction": {
    "reserveTokens": 50000
  }
}
```

Settings file is safe to hand-write: `SettingsManager.migrateSettings()` only touches known legacy keys (`queueMode`, `websockets`, `skills`, `retry`), does not strip unknown keys. Storage backend (`FileSettingsStorage`) expects `{"compaction": {...}}` at top level of the global scope.

### Verification matrix (final)

- `systemctl --user is-active openclaw-gateway` → active; HTTP 200 on :18789 and :18789/healthz
- `bash -ic 'openclaw --version'` → OpenClaw 2026.9.3 (1391f7c)
- `openclaw doctor` → complete, only memory.search info block, no blockers
- `python3 -m json.tool ~/.openclaw/openclaw.json` → valid JSON
- `cat ~/.openclaw/agents/*/agent/settings.json` → `{"compaction":{"reserveTokens":50000}}` ×2
- `contextWindow` values of all 19 provider models: unchanged (verified via backup-diff find)

### Backups kept

- `~/.openclaw/openclaw.json.bak-20260902` (pre-upgrade, has the retired floor)
- `~/.openclaw/openclaw.json.bak` (doctor's own backup)
- `~/.config/systemd/user/openclaw-gateway.service.bak-20260902`
- `~/.openclaw/state/openclaw.sqlite.bak-20260902` (~23 MB)

## Dist-archaeology method (reusable)

When an openclaw upgrade silently drops a config key you tuned:

1. Confirm it's gone: `diff <(python3 -m json.tool <old-backup>) <(python3 -m json.tool ~/.openclaw/openclaw.json)`
2. Check if retired: `grep -rn "<keyName>" ~/.nvm/versions/node/v<ver>/lib/node_modules/openclaw/dist/legacy-*.mjs` — look for `RETIRED_TUNING_PATHS` / `RETIRED_AGENT_TUNING_PATHS`
3. Find the replacement: `grep -rn "<keyName>" dist/*.d.ts` (type defs prove the concept still exists) then `grep -rn "getCompaction\|<keyName>" dist/resource-loader-*.mjs dist/agent-settings-*.mjs` for the actual getter + default
4. Read the effective-value math (min/max clamps vs contextWindow) before choosing the replacement value
5. Write the replacement in the NEW location (per-agent settings.json), not the old one — re-adding a retired key to openclaw.json just guarantees the next doctor run strips it again

## Pre-2026-09-08 history

- 2026-08-22: gateway crash-loop after `openclaw update` — systemd unit still pointed at `/usr/bin/node` (24.14.1) below engines floor (≥24.15.0). Fix: re-point ExecStart to nvm node. See SKILL.md Workflow 5.
- 2026-09-02: CLI `command not found` — nvm default alias `24` resolved to v24.19.0 (no openclaw installed there) + `~/.bashrc` `export PATH=/usr/bin:$PATH` shadowing nvm with system node v24.14.1. Fix: alias → exact version, remove PATH prepend. See SKILL.md Workflow 6.
