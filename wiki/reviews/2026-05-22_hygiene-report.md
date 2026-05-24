# Hygiene Inspection — 2026-05-22

**Status:** approved 2026-05-24
**Issues found:** 5
**Created:** 2026-05-22 23:33:52
**Validator:** hygiene-inspector

**Paths checked:** 18,979

---

## Issue 1: Stale `memory/` directory at root level

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** The `memory/` directory still exists at root level after migration to `.openclaw/memory/`
**Current:** `memory/` directory with `2026-05-22.md` at root
**Expected:** Room root has no `memory/` directory (migrated to `.openclaw/memory/` per folder-structure.md v1.2 changelog, 2026-05-17)
**Suggested fix:** Remove `memory/` from root level (content already lives in `.openclaw/memory/`)

---

## Issue 2: Unlisted file at root level — RAW_BACKLOG.md

**Path:** `RAW_BACKLOG.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist. Root level allows only: 4 required `.md` files (`AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`), 5 allowed symlinks (`HEARTBEAT.md`, `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`), `.gitignore`, `scripts/`, and the 5 standard folders (`.git/`, `.obsidian/`, `.openclaw/`, `.hermes/`, `context/`, `raw/`, `wiki/`).
**Current:** `RAW_BACKLOG.md` at root level
**Expected:** No file `RAW_BACKLOG.md` at root level
**Suggested fix:** Move `RAW_BACKLOG.md` to `wiki/` or `scripts/`, or add it to the folder-structure.md root whitelist if intentional. If this is a temporary work-tracker, move to `wiki/drafts/` or `.openclaw/memory/`.

---

## Issue 3: HEARTBEAT.md in wiki/reviews/

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** `wiki/reviews/` is a Hermes-only output zone. Allowed files are: `_action-required.md`, `YYYY-MM-DD_output-report.md`, `YYYY-MM-DD_format-report.md`, `YYYY-MM-DD_hygiene-report.md`, and `archive/`. `HEARTBEAT.md` is an agent identity file and doesn't belong in the reviews folder.
**Current:** `wiki/reviews/HEARTBEAT.md` exists
**Expected:** No `HEARTBEAT.md` in `wiki/reviews/`
**Suggested fix:** Remove `wiki/reviews/HEARTBEAT.md`. If a heartbeat is needed, it should live in agent home directories (`.hermes/HEARTBEAT.md` or `.openclaw/HEARTBEAT.md`).

---

## Issue 4: .gitkeep in wiki/topic/ doesn't match naming convention

**Path:** `wiki/topic/.gitkeep`
**Severity:** WARNING
**Category:** Naming
**Issue:** `wiki/topic/` files should follow the `<topic>.md` naming pattern (lowercase-hyphen slugs). `.gitkeep` is an auxiliary placeholder, not a topic file.
**Current:** `.gitkeep` in `wiki/topic/`
**Expected:** All files in `wiki/topic/` should be topic `.md` files. If keeping an empty folder in git is needed, the `.gitkeep` should be documented as an exception.
**Suggested fix:** Either remove `.gitkeep` once the folder has enough topic files, or add an explicit `.gitkeep` exception for `wiki/topic/` in folder-structure.md.

---

## Issue 5: raw.md at raw/ root level not in whitelist

**Path:** `raw/raw.md`
**Severity:** INFO
**Category:** Path
**Issue:** Section 6 of folder-structure.md explicitly states "No files at `raw/` root level." However, `raw/raw.md` exists and is referenced as a read-only file in `AGENTS.md` Section 4.2. This appears to be an omission in the folder-structure.md whitelist — `wiki/wiki.md` is explicitly listed as "required (level 1 index)" in Section 7, but `raw/raw.md` has no equivalent entry in Section 6.
**Current:** `raw/raw.md` exists at raw root
**Expected:** Section 6 should include `raw.md` as a permitted level 1 index file, or `raw/raw.md` should be removed
**Suggested fix:** Update folder-structure.md Section 6 to add `raw.md` as "✓ required (level 1 index)" — mirroring the same entry for `wiki/wiki.md` in Section 7. This is a folder-structure.md spec gap, not a structural hygiene problem.

---

## Summary

| # | Severity | Category | Path |
|---|---|---|---|
| 1 | ERROR | Path | `memory/` (root) |
| 2 | ERROR | Path | `RAW_BACKLOG.md` (root) |
| 3 | ERROR | Path | `wiki/reviews/HEARTBEAT.md` |
| 4 | WARNING | Naming | `wiki/topic/.gitkeep` |
| 5 | INFO | Path | `raw/raw.md` (spec gap) |

**Clean:** root symlinks (5/5 OK), context/ (2/2 OK), raw/ subfolders (6/6 OK), wiki/ subfolders (7/7 OK), agent homes (fully compliant), scripts/ (OK), no OS artifacts (`.DS_Store`, `Thumbs.db`), no uppercase folder names.
