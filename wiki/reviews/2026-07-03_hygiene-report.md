# Hygiene Inspection — 2026-07-03

**Status:** pending
**Issues found:** 4
**Created:** 2026-07-03 23:31:41 +0700
**Validator:** hygiene-inspector

**Paths checked:** 51,630

---

## Summary

- 🔴 2 ERROR: `memory/` folder not in root whitelist + `state/` recurring root folder
- ⚠️ 1 WARNING: file inside orphaned `memory/` folder (`memory/2026-07-03.md`)
- ℹ️ 1 INFO: `state/` empty directory (same path as ERROR, separate issue category)
- ✅ Tất cả active content zones (context/, raw/, wiki/meta/, wiki/sources/, wiki/concepts/, wiki/tag/, wiki/topic/, wiki/drafts/, wiki/reviews/) 100% compliant
- ✅ HEARTBEAT.md leak vẫn resolved — ổn định 5 ngày từ 06-28
- ✅ Tất cả naming conventions tuân thủ đúng spec
- KB structure health: 99.992% (4/51,630 paths with issues)

---

## Issue 1: `memory/` folder not in root whitelist

**Path:** memory/
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** `memory/` directory at root level (contains 1 file: `2026-07-03.md`)
**Expected:** Root folders allowed: context, raw, wiki, scripts (per folder-structure.md §2)
**Suggested fix:** `memory/` was migrated to `.openclaw/memory/` in v1.2 (folder-structure.md changelog). This root-level folder has re-appeared with content — move `memory/2026-07-03.md` to `.openclaw/memory/` and delete `memory/`.

---

## Issue 2: `state/` recurring root folder

**Path:** state/
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: `state/`
**Current:** `state/` empty directory at root level (recreated 2026-07-02 10:28, previously resolved 2026-06-27)
**Expected:** Recurring empty directory — previously resolved 2026-06-27, recreated 2026-07-02. Move inside `.hermes/` or `.openclaw/` if needed; otherwise rmdir.
**Suggested fix:** Remove directory: `rmdir state/`. Investigate which process recreates this directory.

---

## Issue 3: `memory/2026-07-03.md` — file inside orphaned folder

**Path:** memory/2026-07-03.md
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule
**Current:** `memory/2026-07-03.md` — file exists inside the orphaned `memory/` root folder
**Expected:** Should be in a known location or whitelisted (`.openclaw/memory/` is the correct destination)
**Suggested fix:** Move to `.openclaw/memory/2026-07-03.md`, then delete the `memory/` folder.

---

## Issue 4: `state/` empty directory

**Path:** state/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory
**Current:** `state/` directory exists but contains no files
**Expected:** Non-empty directory or removed
**Suggested fix:** Remove empty directory: `rmdir state/`

---

## Delta from 2026-07-02 (PENDING)

| Change | Detail |
|---|---|
| 🔴 NEW | `memory/` folder reappeared at root — last seen pre-migration to `.openclaw/memory/` in v1.2 |
| 🔴 SAME | `state/` vẫn là recurring root orphan (cả ERROR path + INFO empty dir) |
| ⚠️ NEW | `memory/2026-07-03.md` — file content inside orphaned folder |
| ✅ STABLE | HEARTBEAT.md leak resolved (5 ngày ổn định) |
| +12 paths | 51,630 vs 51,618 |

---

## Actions

- Review `wiki/reviews/2026-07-03_hygiene-report.md`
- Nếu approve ERRORs: di chuyển `memory/2026-07-03.md` → `.openclaw/memory/`, xóa `memory/`, `rmdir state/`
- Điều tra: process nào tạo `memory/` folder mới (file dated today 07-03) — có thể là cron job hoặc agent đang ghi sai output path
- `state/` recurrence: 3 lần trong 7 ngày — cần process-level fix cho output path của process tạo nó
