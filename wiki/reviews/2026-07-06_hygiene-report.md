# Hygiene Inspection — 2026-07-06

**Status:** approved
**Issues found:** 2 (1 ERROR, 1 WARNING)
**Created:** 2026-07-06 23:30:00 +0700
**Validator:** hygiene-inspector

**Paths checked:** 51,701

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 |
| WARNING | 1 |
| INFO | 0 |

### Đánh giá tổng quan

- 🔴 1 ERROR: `memory/` folder at root level — recurring orphan (đã flagged 07-03, 07-04, resolved, nay tái xuất hiện với file mới)
- ⚠️ 1 WARNING: `memory/compilation-log.md` — file mới bên trong folder `memory/` orphaned, process đang ghi log compilation vào sai path
- ✅ Tất cả active content zones (context/, raw/, wiki/) 100% compliant
- ✅ HEARTBEAT.md leak resolved — 8 ngày ổn định (từ 06-28)
- ✅ `state/` resolved — không còn xuất hiện (đã fix từ 07-05)

### Delta from 2026-07-05 (APPROVED: 0 issues)

- 🔴 NEW: `memory/` folder reappeared at root — chứa file mới `compilation-log.md`
- ⚠️ NEW: `memory/compilation-log.md` — compilation log bị ghi sai path
- +80 paths (51,701 vs 51,621 — growth từ các file mới trong KB)

### KB structure health

- **Active zone health:** 100% (context/, raw/, wiki/ — không có issue nào)
- **Root zone health:** 99.996% (2/51,701 paths with issues)
- **Trend:** Tái phát — `memory/` folder từng resolved 07-05, nay quay lại với nội dung khác

---

## Issue 1: Root folder orphan — memory/

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist — recurring orphan

**Current:** `memory/` folder at knowledge base root
**Expected:** Root folders chỉ được phép: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`
**History:** 
- 2026-07-03: Flagged (chứa `2026-07-03.md`)
- 2026-07-04: Flagged again (chứa `2026-07-03.md`)
- 2026-07-05: Resolved — KB 100% clean
- 2026-07-06: **Tái xuất hiện** với file mới `compilation-log.md`

**Suggested fix:**
```
mv memory/compilation-log.md .openclaw/memory/
rmdir memory/
```
Hoặc nếu `memory/` được dùng bởi process compile: cập nhật `folder-structure.md` để whitelist, hoặc sửa process output path thành `.openclaw/memory/`.

---

## Issue 2: Orphaned file inside memory/

**Path:** `memory/compilation-log.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Path not classified by any rule — file inside orphaned root folder

**Current:** `memory/compilation-log.md`
**Expected:** Compilation logs should be in `.openclaw/memory/` or `.hermes/` (agent runtime workspace)
**Note:** File này là compilation log — likely được tạo bởi compile process. Path gốc `memory/` đã migrate vào `.openclaw/memory/` từ folder-structure.md v1.2 (2026-05-17) nhưng process vẫn ghi vào path cũ.

**Suggested fix:**
```
mv memory/compilation-log.md .openclaw/memory/compilation-log.md
```

---

## Systemic note

### memory/ recurrence pattern (3 lần trong 4 ngày)

| Date | Contents | Status |
|---|---|---|
| 07-03 | `2026-07-03.md` (memory file) | Flagged, later resolved |
| 07-04 | `2026-07-03.md` (same file, not yet moved) | Flagged, resolved by Fix Agent 07-05 |
| 07-05 | — | Clean (0 issues) |
| 07-06 | `compilation-log.md` (new file) | Flagged — process-level leak |

**Root cause:** Một process (likely compile agent) đang ghi output vào `memory/` thay vì `.openclaw/memory/`. Folder-structure.md v1.2 đã migrate memory vào `.openclaw/` từ 2026-05-17, nhưng ít nhất 2 process khác nhau vẫn dùng path cũ:
1. Process ghi file memory (`2026-07-03.md`)
2. Process ghi compilation log (`compilation-log.md`)

**Khuyến nghị:** 
- [ESCALATION] Cần process-level fix — sửa tất cả agent config/SKILL.md để dùng `.openclaw/memory/` thay vì `memory/`
- File deletion/rmdir chỉ là temporary fix — folder sẽ tái xuất hiện mỗi khi process chạy

---

## Verified clean zones

| Zone | Status | Details |
|---|---|---|
| `context/` | ✅ Clean | Exactly context.md + USER.md |
| `raw/` | ✅ Clean | All 6 type subfolders, no files at root, naming compliant |
| `wiki/meta/` | ✅ Clean | 3 files: format-spec, folder-structure, index-spec |
| `wiki/sources/` | ✅ Clean | All src_<slug>.md |
| `wiki/concepts/` | ✅ Clean | All lowercase-hyphen |
| `wiki/tag/` | ✅ Clean | Auto-generated, naming compliant |
| `wiki/topic/` | ✅ Clean | Auto-generated, naming compliant |
| `wiki/drafts/` | ✅ Clean | No .bak/.tmp leftovers, naming compliant |
| `wiki/reviews/` | ✅ Clean | No HEARTBEAT leak, reports properly named |
| `wiki/reviews/archive/` | ✅ Clean | YYYY-MM/YYYY-MM-DD_<type>-report.md |
| Agent homes | ✅ Clean | .hermes/, .openclaw/ — no misplaced user content |
| `scripts/` | ✅ Clean | Utility scripts only |
| Root symlinks | ✅ Clean | HEARTBEAT, IDENTITY, SOUL, TOOLS, USER — all valid |

---

## Actions

1. Review `wiki/reviews/2026-07-06_hygiene-report.md`
2. Nếu approve: `mv memory/compilation-log.md .openclaw/memory/` → `rmdir memory/`
3. 🚨 [ESCALATION] `memory/` recurrence (3 lần trong 4 ngày): tìm và sửa tất cả process/SKILL.md đang ghi vào `memory/` thay vì `.openclaw/memory/`
4. KB structure health: 99.996% (2/51,701 paths with issues)

**Report:** `wiki/reviews/2026-07-06_hygiene-report.md`
