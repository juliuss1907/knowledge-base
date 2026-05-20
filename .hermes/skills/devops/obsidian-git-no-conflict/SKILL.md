---
name: obsidian-git-no-conflict
description: Prevent Obsidian Git plugin merge conflicts on multi-machine setups (VPS + main machine). Covers comprehensive .gitignore, git rm --cached for tracked state files, and the 3 plugin settings that eliminate race conditions.
category: devops
---

# Obsidian Git — Zero Conflict Setup

When two machines (VPS + máy chính) both run Obsidian Git plugin with auto-sync, merge conflicts are inevitable. This skill eliminates them permanently through Git hygiene + plugin configuration.

## Root causes (5 simultaneous problems)

| # | Cause | Effect |
|---|---|---|
| 1 | Machine-specific Obsidian UI state files tracked by Git | `.obsidian/graph.json`, `workspace.json`, `app.json` change every session → perpetual conflicts |
| 2 | Agent runtime state files tracked by Git | `.hermes/auth.json`, `memories/MEMORY.md`, `models_dev_cache.json`; `.openclaw/main.sqlite`, `device-auth.json` — change on every agent run → sync = conflict |
| 3 | `mergeStrategy: "none"` | Plugin refuses to auto-merge, so ANY simultaneous change becomes a conflict |
| 4 | Auto-push on both machines (interval 10 min) | Race condition when both push new commits simultaneously |
| 5 | `git rm --cached` only on one machine | File still exists on disk on the other → Obsidian Git re-stages it → "Not a file" conflict when the other machine's deletion arrives |

## Fix 1: Comprehensive .gitignore

The problem: `.gitignore` only works on files NEVER tracked. Obsidian Git plugin tracks UI state files by default. You need BOTH the ignore pattern AND `git rm --cached`.

### The complete ignore block

```gitignore
# Obsidian UI/state files (máy-specific — không sync)
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/graph.json
.obsidian/app.json
.obsidian/appearance.json
.obsidian/cache
.obsidian/hotkeys.json
.obsidian/text.json
.obsidian/bookmarks.json
.obsidian/snippets/

# Obsidian plugin data (máy-specific state)
.obsidian/plugins/*/data.json
```

### Untrack already-committed files

```bash
# Find ALL tracked files matching the patterns
git ls-files '.obsidian/graph.json' '.obsidian/app.json' '.obsidian/appearance.json' '.obsidian/hotkeys.json' '.obsidian/bookmarks.json' '.obsidian/text.json' '.obsidian/plugins/*/data.json'

# Untrack them all in one commit
git rm --cached .obsidian/graph.json .obsidian/app.json .obsidian/appearance.json .obsidian/hotkeys.json .obsidian/text.json .obsidian/bookmarks.json
git rm --cached .obsidian/plugins/*/data.json

git add .gitignore
git commit -m "fix: untrack all Obsidian UI state + plugin data from Git"
git push
```

## Fix 2: Agent runtime state (.hermes/ + .openclaw/)

Agent runtime creates files that change on every execution. These MUST be gitignored and untracked from BOTH machines, or they'll cause "Not a file" conflicts when one machine deletes and the other recreates.

### The complete runtime ignore block

```gitignore
# Hermes runtime state (máy-specific — không sync)
.hermes/auth/
.hermes/auth.json
.hermes/auth.lock
.hermes/channel_directory.json
.hermes/state.db*
.hermes/gateway.pid
.hermes/gateway_state.json
.hermes/logs/
.hermes/sessions/
.hermes/cron/
.hermes/cache/
.hermes/memories/MEMORY.md
.hermes/.skills_prompt_snapshot.json
.hermes/.update_check
.hermes/.restart_last_processed.json
.hermes/models_dev_cache.json
.hermes/ollama_cloud_models_cache.json
.hermes/bin/

# OpenClaw runtime state (máy-specific — không sync)
.openclaw/main.sqlite
.openclaw/device-auth.json
.openclaw/device.json
.openclaw/devices/
.openclaw/exec-approvals.json
.openclaw/update-check.json
.openclaw/workspace-state.json
.openclaw/logs/
.openclaw/completions/
.openclaw/flows/
.openclaw/subagents/
.openclaw/tasks/
.openclaw/media/
.openclaw/telegram/
.openclaw/canvas/
.openclaw/identity/
.openclaw/agents/
.openclaw/*.bak
```

### Untrack from BOTH machines

**Critical: both machines must untrack, or the conflict persists.** The "Not a file" error happens because machine A deleted the file from Git, but machine B still has it on disk → Obsidian Git sees the changed file and auto-stages it → pushes a re-creation → machine A sees "deleted by them."

```bash
# Run on BOTH VPS and máy chính
cd ~/knowledge-base
git pull --no-rebase origin master

# Untrack hermes runtime files that are still tracked
git rm --cached .hermes/memories/MEMORY.md \
  .hermes/.skills_prompt_snapshot.json \
  .hermes/.update_check .hermes/models_dev_cache.json \
  .hermes/auth.json .hermes/gateway.pid \
  .hermes/channel_directory.json \
  .openclaw/HEARTBEAT.md 2>/dev/null

git add .gitignore
git commit -m "fix: untrack all agent runtime state files" && git push origin master
```

## Fix 3: Change 3 plugin settings (Fix 2 renumbered to Fix 3 — Fix 2 is now "Agent runtime state")

Open Obsidian → Settings → Community plugins → Obsidian Git → settings gear:

| Setting | Wrong value | Correct value | Why |
|---|---|---|---|
| **Auto push interval** | `10` (minutes) | `0` (disabled) | Eliminates race condition — only one machine ever pushes at a time |
| **Merge strategy** | `none` | **để trống** | Enables automatic merge resolution instead of failing on every parallel change. NOTE: "ort" is a Git engine strategy, NOT an option in the plugin UI. The UI shows \"Other sync service\" for `none`. Leave this field empty for normal merge. |
| **Pull before push** | `true` | `true` (keep) | Ensures local is always up to date before pushing |

### The push policy

- **Auto-pull stays ON** on both machines → each auto-fetches latest within 30 seconds
- **Auto-push: VPS ON, main machine OFF** — VPS agents push on predictable schedules (08:00, 21:00, 23:00), main machine human editing is unpredictable. Only one machine ever pushes, eliminating race conditions
- Result: VPS auto-pushes agent output → main machine auto-pulls → Julius manually pushes human edits when ready → never a conflict

## Fix 3: Identity file symlinks (if applicable)

If OpenClaw runtime creates agent identity files at workspace root (IDENTITY.md, SOUL.md, HEARTBEAT.md, USER.md, TOOLS.md), these will cause conflicts when both machines regenerate them:

```bash
# Move real content to .openclaw/
mv IDENTITY.md .openclaw/IDENTITY.md
mv SOUL.md .openclaw/SOUL.md
# ... etc

# Create symlinks (runtime reads from root, Git tracks from .openclaw/)
ln -sf .openclaw/IDENTITY.md IDENTITY.md
ln -sf .openclaw/SOUL.md SOUL.md
ln -sf .openclaw/HEARTBEAT.md HEARTBEAT.md
ln -sf .openclaw/USER.md USER.md
ln -sf .openclaw/TOOLS.md TOOLS.md

# Add symlinks to .gitignore
echo "IDENTITY.md" >> .gitignore
echo "SOUL.md" >> .gitignore
echo "HEARTBEAT.md" >> .gitignore
echo "USER.md" >> .gitignore
echo "TOOLS.md" >> .gitignore
```

### Why symlinks instead of untracking

OpenClaw runtime checks for these files at workspace root on startup and **recreates them if missing**. A symlink satisfies the check (file exists) but Git only tracks the target. Without symlinks, the runtime would recreate the files, Git would track them, and they'd conflict again.

## Verification checklist

After applying all fixes, verify on BOTH machines:

```bash
# 1. No UI state files tracked
git ls-files '.obsidian/graph.json' '.obsidian/app.json'  # should be empty

# 2. No plugin data files tracked
git ls-files '.obsidian/plugins/*/data.json'  # should be empty

# 3. Clean working tree
git status  # "nothing to commit, working tree clean"

# 4. gitignore covers all patterns
grep "obsidian" .gitignore
```

## Pitfalls

- **`.gitignore` won't untrack already-committed files** — always run `git ls-files <pattern>` after adding to `.gitignore`, and `git rm --cached` any stragglers
- **"Not a file" conflicts are recursive** — this is the single hardest conflict pattern to break. Machine A deletes file from Git → Machine B's Obsidian Git auto-pushes a recreation before B pulls the deletion → Machine A pulls and sees "deleted by them" → Machine A resolves → Machine B's auto-push recreates AGAIN. This loop continues until auto-push is disabled on one machine OR both machines untrack simultaneously. **The fix is always: untrack on BOTH machines + disable auto-push on one.**
- **Agent runtime files regenerate** — `.hermes/auth.json`, `memories/MEMORY.md`, cache files are recreated on every agent run. They MUST be in `.gitignore` AND untracked from both machines, or they'll perpetually re-enter Git.
- **Obsidian Git plugin auto-stages files** — even with `.gitignore`, the plugin may detect changes. The `.gitignore` prevents them from being committed, but you'll still see them as modified. This is safe.
- **Plugin data.json is regenerated on restart** — after `git rm --cached`, the file still exists on disk (just untracked). The plugin will keep updating it locally, but Git will ignore it.
- **Other plugin conflicts** — any Obsidian plugin that stores machine-specific state in `data.json` is a conflict vector. The `plugins/*/data.json` pattern covers them all.
- **micro editor backup on merge** — when `git pull` triggers a merge commit and `EDITOR=micro`, micro may detect a stale backup file. Press `i` to ignore it, then `Ctrl+S`, `Ctrl+Q` to complete the merge.
- **Obsidian Git on VPS** — VPS typically doesn't run Obsidian (no GUI). If Obsidian Git plugin is installed but Obsidian isn't running, it won't cause problems. The plugin only operates when Obsidian is open.
