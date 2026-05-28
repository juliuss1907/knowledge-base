# Hygiene Report — 2026-05-28

> Hygiene Inspector run: 2026-05-28 08:21 AM
> Ground truth: `wiki/meta/folder-structure.md` v1.2 (2026-05-17)
|> KB path: `/home/julius/knowledge-base/`
**Status:** APPROVED 2026-05-28

---

## 1. Summary

| Check | Result |
|---|---|
| Root level files | ⚠️ 2 issues |
| `.openclaw/` structure | ✅ PASS |
| `.hermes/` structure | ✅ PASS |
| `context/` structure | ✅ PASS |
| `raw/` structure | ✅ PASS |
| `wiki/` structure | ✅ PASS |
| Symlinks (root level) | ✅ PASS |
| venvs | ⚠️ 1 found |
| `.bak/.tmp` files | ✅ CLEAN |
| `.gitkeep` presence | ✅ PASS |

---

## 2. Root Level (depth 0) — Issues Found

### 2.1 ERROR: `memory/` — Orphaned Root Folder

**Path:** `/home/julius/knowledge-base/memory/`

**Expected:** Per folder-structure.md v1.2 changelog, `memory/` was migrated to `.openclaw/memory/`. This folder should not exist at root.

**Found:**
```
memory/
└── 2026-05-27.md
```

**Fix required:** This is a Julius-only folder (by convention, not an agent write zone). Recommend moving content to `.openclaw/memory/` and deleting the folder, OR moving to `julius-workspace` if it contains personal notes not meant for the KB pipeline.

---

### 2.2 ERROR: `RAW_BACKLOG.md` — Stray Root File

**Path:** `/home/julius/knowledge-base/RAW_BACKLOG.md`

**Expected:** Root level allows only: AGENTS.md, TAGS.md, README.md, knowledge-base.md + 5 symlinks (HEARTBEAT, IDENTITY, SOUL, TOOLS, USER) + system folders (.git, .obsidian, .openclaw, .hermes) + context/, raw/, wiki/, scripts/

**Fix required:** Either:
- Move content to relevant `raw/<type>/<type>.md` index files (append-only)
- Delete if redundant
- Move to `julius-workspace` if personal reference notes

---

## 3. venvs — Issue Found

### 3.1 WARNING: Python venv in `.hermes/hermes-agent/venv/`

**Path:** `/home/julius/knowledge-base/.hermes/hermes-agent/venv/`

**Found:** Standard Python virtual environment with `bin/python`, `lib64`, etc.

**Note:** The `setup-skeleton-kb-v2.sh` script at `scripts/setup-skeleton-kb-v2.sh` was the original venv creator for this project. The venv was supposed to be deleted per 2026-05-27 hygiene fixes. If this venv is no longer needed (OpenClaw/Hermes manage their own runtimes), it should be removed.

**Recommendation:** Verify if `venv/` is still in use by any Hermès subsystem before deletion. If not used, delete with `rm -rf venv/`.

---

## 4. Forbidden Pattern Scan — PASS

| Pattern | Found |
|---|---|
| `*.bak` files | None |
| `*.tmp` files (in user-visible paths) | None (`.hermes/.../node_modules/.tmp` is internal node.js build artifact — acceptable) |
| `.DS_Store` | None |
| `Thumbs.db` | None |
| Files at `wiki/` root | None ✅ |
| Files at `raw/` root | None ✅ |
| Uppercase folder names | None ✅ |

---

## 5. Structural Validation

### 5.1 `.openclaw/` — ✅ PASS

| Required | Status |
|---|---|
| `IDENTITY.md` | ✅ |
| `SOUL.md` | ✅ |
| `MEMORY.md` | ✅ |
| `HEARTBEAT.md` | ✅ |
| `skills/` | ✅ |

Runtime folders (agents/, canvas, completions/, cron/, devices/, flows/, identity/, logs/, media/, memory/, subagents/, tasks/, telegram/) are present and owned by OpenClaw runtime — acceptable per spec catch-all clause.

### 5.2 `.hermes/` — ✅ PASS

| Required | Status |
|---|---|
| `IDENTITY.md` | ✅ |
| `SOUL.md` | ✅ |
| `MEMORY.md` | ✅ |
| `HEARTBEAT.md` | ✅ |
| `skills/` | ✅ |

Runtime folders (audio_cache/, bin/, cache/, cron/, hooks/, image_cache/, logs/, memories/, pairing/, sandboxes/, sessions/, etc.) present — acceptable per spec catch-all clause.

### 5.3 `wiki/meta/` — ✅ PASS

Exactly 3 files: `folder-structure.md`, `format-spec.md`, `index-spec.md` — matches v1.2 spec.

### 5.4 `context/` — ✅ PASS

Exactly 2 files: `context.md`, `USER.md` — matches spec.

### 5.5 `raw/` — ✅ PASS

6 subfolders: `articles/`, `papers/`, `posts/`, `repos/`, `videos/`, `websites/` — matches spec.

### 5.6 `wiki/reviews/` — ✅ PASS

Correct structure with `_action-required.md`, dated reports, and `archive/` subfolder.

**Note:** `wiki/reviews/HEARTBEAT.md` presence is unusual but appears to be a work file created during the 2026-05-27 session. It should be moved to `.openclaw/` if it's an OpenClaw runtime artifact.

### 5.7 `wiki/drafts/` and `wiki/topic/` — ✅ PASS

Both contain `.gitkeep` as required placeholder when empty.

### 5.8 Root-level symlinks — ✅ PASS

All 5 required symlinks present and correctly pointing to `.openclaw/`:
- `HEARTBEAT.md → .openclaw/HEARTBEAT.md`
- `IDENTITY.md → .openclaw/IDENTITY.md`
- `SOUL.md → .openclaw/SOUL.md`
- `TOOLS.md → .openclaw/TOOLS.md`
- `USER.md → .openclaw/USER.md`

---

## 6. Skill Folders

The spec (section 12) lists 4 agent skill folders each for `.openclaw/` and `.hermes/`. The actual runtime contains many more skill folders as the agents own these spaces entirely and the catch-all clause applies. This is functioning as designed.

**OpenClaw skills found:** `agent-reach`, `compile-agent`, `fix-agent`, `index-agent`, `ingest-agent`, `news-brief-skill` + runtime folders (`agents/`, `subagents/`)

**Hermes skills found:** `format-validator`, `hygiene-inspector`, `output-validator`, `agent-reach` + 30+ additional skill modules

All acceptable as runtime workspace content.

---

## 7. Issues Summary

| # | Severity | Path | Issue |
|---|---|---|---|
| 1 | ERROR | `/memory/` | Orphaned root folder — should have migrated to `.openclaw/memory/` per v1.2 |
| 2 | ERROR | `/RAW_BACKLOG.md` | Stray file not in root whitelist |
| 3 | WARNING | `/.hermes/hermes-agent/venv/` | Python venv not deleted (supposed to be removed per 2026-05-27 fixes) |
| 4 | INFO | `/wiki/reviews/HEARTBEAT.md` | Unusual file in reviews folder — likely a session artifact, should be moved |

---

## 8. Resolution

| # | Action | Owner |
|---|---|---|
| 1 | Move `memory/2026-05-27.md` to `.openclaw/memory/`, then delete `memory/` | Julius |
| 2 | Audit `RAW_BACKLOG.md` — move content to relevant `raw/<type>/<type>.md` or delete | Julius |
| 3 | Verify and delete `venv/` if unused | Julius |
| 4 | Move `wiki/reviews/HEARTBEAT.md` to `.openclaw/` if it's an OpenClaw runtime artifact | OpenClaw (via fix-agent) |

---

*Report generated by Hygiene Inspector — Hermes subagent*
*Next scheduled run: 2026-05-29 (or on demand)*
