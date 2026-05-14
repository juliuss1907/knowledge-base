---
name: obsidian-git-no-conflict
description: Prevent Obsidian Git plugin merge conflicts on multi-machine setups (VPS + main machine). Covers comprehensive .gitignore, git rm --cached for tracked state files, and the 3 plugin settings that eliminate race conditions.
category: devops
---

# Obsidian Git — Zero Conflict Setup

When two machines (VPS + máy chính) both run Obsidian Git plugin with auto-sync, merge conflicts are inevitable. This skill eliminates them permanently through Git hygiene + plugin configuration.

## Root causes (3 simultaneous problems)

| # | Cause | Effect |
|---|---|---|
| 1 | Machine-specific UI state files tracked by Git | `.obsidian/graph.json`, `workspace.json`, `app.json` change every session → perpetual conflicts |
| 2 | `mergeStrategy: "none"` | Plugin refuses to auto-merge, so ANY simultaneous change becomes a conflict |
| 3 | Auto-push on both machines (interval 10 min) | Race condition when both push new commits simultaneously |

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

## Fix 2: Change 3 plugin settings

Open Obsidian → Settings → Community plugins → Obsidian Git → settings gear:

| Setting | Wrong value | Correct value | Why |
|---|---|---|---|
| **Auto push interval** | `10` (minutes) | `0` (disabled) | Eliminates race condition — only one machine ever pushes at a time |
| **Merge strategy** | `none` | **để trống** | Enables automatic merge resolution instead of failing on every parallel change. NOTE: "ort" is a Git engine strategy, NOT an option in the plugin UI. The UI shows \"Other sync service\" for `none`. Leave this field empty for normal merge. |
| **Pull before push** | `true` | `true` (keep) | Ensures local is always up to date before pushing |

### The push policy

- **Auto-pull stays ON** → each machine auto-fetches latest within 30 seconds
- **Auto-push turned OFF** → Julius pushes manually from whichever machine he's actively working on
- Result: Machine A manually pushes → Machine B auto-pulls → never a conflict

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
- **Obsidian Git plugin auto-stages files** — even with `.gitignore`, the plugin may detect changes and stage them. The `.gitignore` prevents them from being committed, but you'll still see them as modified. This is safe — they won't actually be pushed.
- **Plugin data.json is regenerated on restart** — after `git rm --cached`, the file still exists on disk (just untracked). The plugin will keep updating it locally, but Git will ignore it.
- **Other plugin conflicts** — any Obsidian plugin that stores machine-specific state in `data.json` is a conflict vector. The `plugins/*/data.json` pattern covers them all.
- **micro editor backup on merge** — when `git pull` triggers a merge commit and `EDITOR=micro`, micro may detect a stale backup file. Press `i` to ignore it, then `Ctrl+S`, `Ctrl+Q` to complete the merge.
- **Obsidian Git on VPS** — VPS typically doesn't run Obsidian (no GUI). If Obsidian Git plugin is installed but Obsidian isn't running, it won't cause problems. The plugin only operates when Obsidian is open.
