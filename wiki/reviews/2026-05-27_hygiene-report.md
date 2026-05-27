# Hygiene Inspection — 2026-05-27

**Status:** pending
**Issues found:** 4
**Created:** 2026-05-27 07:54:00
**Validator:** hygiene-inspector

**Paths checked:** 6,082 (excluding .git, node_modules, .obsidian, venv site-packages, __pycache__)

---

## Issue 1: Forbidden folder at root level

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder `memory/` exists at root level but is not in the root whitelist.
**Current:** `memory/` contains `2026-05-25.md` and `2026-05-26.md` (daily memory logs).
**Expected:** Spec v1.2 (2026-05-17) migrated `memory/` from root to `.openclaw/memory/`. Root whitelist only allows: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`.
**Suggested fix:** Move `memory/` contents to `.openclaw/memory/` and delete `memory/` from root.

---

## Issue 2: HEARTBEAT.md at root is not a symlink

**Path:** `HEARTBEAT.md`
**Severity:** WARNING
**Category:** Naming / Path
**Issue:** `HEARTBEAT.md` at root is a regular UTF-8 text file, not a symlink to `.openclaw/HEARTBEAT.md`.
**Current:** Regular file (same content as `.openclaw/HEARTBEAT.md`).
**Expected:** Spec §2 requires `HEARTBEAT.md ✓ (symlink to .openclaw/HEARTBEAT.md)`. Other root symlinks (IDENTITY.md, SOUL.md, TOOLS.md, USER.md) are correctly symlinked — HEARTBEAT.md is the outlier.
**Suggested fix:** Replace with symlink: `ln -sf .openclaw/HEARTBEAT.md HEARTBEAT.md` after backing up if needed.

---

## Issue 3: Virtualenv folders in skill directory

**Path:** `.openclaw/skills/news-brief-skill/venv-3.11/`, `.openclaw/skills/news-brief-skill/venv-3.12/`
**Severity:** WARNING
**Category:** Path
**Issue:** Two Python virtualenv folders (`venv-3.11`, `venv-3.12`) containing 2,778 files are inside a skill directory.
**Current:** `venv-3.11/` and `venv-3.12/` directories with full Python packages (site-packages, lib, etc.)
**Expected:** Spec §4: Skill folders should only contain `.md` files and `.gitkeep`. No subfolders, no non-markdown files except `.gitkeep`.
**Suggested fix:** Move venvs outside the skills directory (e.g., to `.openclaw/venvs/`) or add them to `.gitignore` if they're ephemeral. These large dependency trees bloat the KB and may cause git issues.

---

## Issue 4: Backup and temp files in devices directory

**Path:** `.openclaw/devices/paired.json.bak`, `.openclaw/devices/paired.json.80f096b3-1f67-4a08-891c-25398297ceca.tmp`, `.openclaw/devices/pending.json.bak`, `.openclaw/openclaw.json.bak`
**Severity:** INFO
**Category:** Orphan
**Issue:** Backup (`.bak`) and temporary (`.tmp`) files found outside of gitignored paths.
**Current:** 4 files — 3 `.bak` and 1 `.tmp`.
**Expected:** OS artifacts and temporary files should be gitignored or cleaned up. They indicate previous operations (likely OpenClaw config changes) left behind stale files.
**Suggested fix:** Delete `.bak` and `.tmp` files or ensure they're covered by `.gitignore`. These appear safe to remove — they're device pairing/configuration backups.
