# Hygiene Inspection — 2026-05-26

**Status:** pending
**Issues found:** 4 (2 ERROR, 2 WARNING)
**Created:** 2026-05-26 08:00:54
**Validator:** hygiene-inspector

**Paths checked:** ~24,452 (full KB scan excluding .git, node_modules, .obsidian)

---

## Issue 1: File at raw/ root level

**Path:** `raw/RAW_BACKLOG.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File exists at `raw/` root level, violating the rule "No files at `raw/` root level" (folder-structure.md §6).
**Current:** `raw/RAW_BACKLOG.md` exists alongside the allowed `raw/raw.md`
**Expected:** Only `raw/raw.md` (index file) at raw/ root. All other content must be in type subfolders (articles/, posts/, etc.).
**Suggested fix:** Move `RAW_BACKLOG.md` into an appropriate `raw/` subfolder, or into `wiki/drafts/`, or delete if obsolete.

---

## Issue 2: Unexpected file in reviews/

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path
**Issue:** `HEARTBEAT.md` found in `wiki/reviews/`, which only allows `_action-required.md` and `YYYY-MM-DD_<type>-report.md` files (folder-structure.md §7).
**Current:** `wiki/reviews/HEARTBEAT.md`
**Expected:** Only `_action-required.md` and dated report files (`output-report.md`, `format-report.md`, `hygiene-report.md`)
**Suggested fix:** Remove or relocate `HEARTBEAT.md`. If an agent mistakenly created this, it belongs in `.openclaw/` or `.hermes/` agent home instead.

---

## Issue 3: Git placeholder in topic/ folder

**Path:** `wiki/topic/.gitkeep`
**Severity:** WARNING
**Category:** Naming
**Issue:** `.gitkeep` found in `wiki/topic/`, but this folder is designated for `<topic>.md` files only (folder-structure.md §7). `.gitkeep` is a non-markdown placeholder.
**Current:** `wiki/topic/.gitkeep`
**Expected:** All files in `wiki/topic/` should be topic index files (`.md` with lowercase-hyphen slugs)
**Suggested fix:** `.gitkeep` can be removed since `wiki/topic/` already has content files; the directory won't disappear from git.

---

## Issue 4: Git placeholder in drafts/ folder

**Path:** `wiki/drafts/.gitkeep`
**Severity:** WARNING
**Category:** Naming
**Issue:** `.gitkeep` found in `wiki/drafts/`, but this folder is designated for `<slug>.md` files only (folder-structure.md §7).
**Current:** `wiki/drafts/.gitkeep`
**Expected:** All files in `wiki/drafts/` should be `<slug>.md` content files awaiting review.
**Suggested fix:** `.gitkeep` can be removed since `wiki/drafts/` is tracked even without a placeholder when git tracks other path content. Alternatively, leave it if intentionally keeping the directory empty-trackable.

---

## Validation summary

| Check | Result |
|---|---|
| Root level files/folders | ✅ OK — all 9 root-level items match whitelist |
| `context/` (exactly 2 files) | ✅ OK — context.md + USER.md |
| `raw/` subfolders (exactly 6) | ✅ OK — articles, posts, websites, videos, papers, repos |
| `raw/` content naming (YYYY-MM-DD_) | ✅ OK — all content files follow convention |
| `wiki/meta/` (exactly 3 files) | ✅ OK — format-spec.md, folder-structure.md, index-spec.md |
| `wiki/sources/` naming (src_) | ✅ OK — all files start with `src_` |
| `wiki/concepts/` naming (lowercase-hyphen) | ✅ OK — all slugs valid |
| `wiki/tag/` index (tag.md) | ✅ OK — required index present |
| Nesting in raw/<type>/ | ✅ OK — no nested subfolders |
| Uppercase folder names | ✅ OK — none found |
| OS artifacts (.DS_Store, Thumbs.db) | ✅ OK — none found |
| `.tmp` / `.bak` files | ✅ OK — only runtime artifacts in agent homes |
| Agent homes (.openclaw/, .hermes/) | ✅ OK — runtime content only |
| Empty folders | ✅ OK — only runtime cache/skill dirs |

---

## No changes from previous run

The last hygiene report (`2026-05-24_hygiene-report.md`) identified different issues. Today's findings are new or persistent.

**Persistent:**
- `raw/RAW_BACKLOG.md` has been flagged in prior reports and remains unfixed.
- `wiki/reviews/HEARTBEAT.md` is a new finding (not in previous reports).
