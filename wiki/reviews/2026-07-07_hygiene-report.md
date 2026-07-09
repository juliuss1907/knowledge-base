# Hygiene Inspection — 2026-07-07

**Status:** approved
**Issues found:** 2 (1 ERROR, 1 WARNING)
**Created:** 2026-07-07 23:30:00 +0700
**Validator:** hygiene-inspector

**Paths checked:** 51,715

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 |
| WARNING | 1 |
| INFO | 0 |

### Đánh giá tổng quan

- 🔴 1 ERROR: `memory/` folder at root level — recurring orphan (lần 4 trong 5 ngày: 07-03, 07-04, 07-06, 07-07)
- ⚠️ 1 WARNING: `memory/compilation-log.md` — file bên trong folder `memory/` orphaned, chưa được move
- ✅ Tất cả active content zones (context/, raw/, wiki/) 100% compliant
- ✅ HEARTBEAT.md leak resolved — 9 ngày ổn định (từ 06-28)
- ✅ `state/` resolved — không còn xuất hiện (đã fix từ 07-05)
- ✅ Root symlinks all valid (HEARTBEAT, IDENTITY, SOUL, TOOLS, USER)

### Delta from 2026-07-06 (PENDING: 2 issues — same pattern)

- 🔴 SAME: `memory/` folder — unchanged from yesterday. Folder vẫn chưa được move/rmdir. PENDING report từ 07-06 chưa được Julius review.
- ⚠️ SAME: `memory/compilation-log.md` — same file as 07-06 (last modified Jul 6 08:16), no new content added today
- +14 paths (51,715 vs 51,701 — growth từ file mới trong KB)

### KB structure health

- **Active zone health:** 100% (context/, raw/, wiki/ — không có issue nào)
- **Root zone health:** 99.996% (2/51,715 paths with issues)
- **Trend:** Ổn định — không có issue mới, 2 issue carry-over từ 07-06 chưa được resolve

---

## Issue 1: Root folder orphan — memory/

**Path:** `memory/`
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist — recurring orphan

**Current:** `memory/` folder at knowledge base root (last modified Jul 6 08:16)
**Expected:** Root folders chỉ được phép: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`
**History:** 
- 2026-07-03: Flagged (chứa `2026-07-03.md`)
- 2026-07-04: Flagged again (chứa `2026-07-03.md`)
- 2026-07-05: Resolved — KB 100% clean
- 2026-07-06: Tái xuất hiện với file mới `compilation-log.md`
- 2026-07-07: **Vẫn tồn tại** — chưa được move/rmdir, PENDING report 07-06 chưa reviewed

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

**Current:** `memory/compilation-log.md` (1059 bytes, last modified Jul 6 08:16)
**Expected:** Compilation logs should be in `.openclaw/memory/` or `.hermes/` (agent runtime workspace)
**Note:** File này là compilation log từ compile process ngày 07-06 (processed 2 articles: rag-is-dead-kuba-turbopuffer, steve-jobs-stanford-2005-commencement). Path gốc `memory/` đã migrate vào `.openclaw/memory/` từ folder-structure.md v1.2 (2026-05-17) nhưng process vẫn ghi vào path cũ.

**Suggested fix:**
```
mv memory/compilation-log.md .openclaw/memory/compilation-log.md
```

---

## Systemic note

### memory/ recurrence pattern (4 lần trong 5 ngày)

| Date | Contents | Status |
|---|---|---|
| 07-03 | `2026-07-03.md` (memory file) | Flagged, later resolved |
| 07-04 | `2026-07-03.md` (same file, not yet moved) | Flagged, resolved by Fix Agent 07-05 |
| 07-05 | — | Clean (0 issues) |
| 07-06 | `compilation-log.md` (new file) | Flagged — PENDING, not yet reviewed |
| 07-07 | `compilation-log.md` (same file, unchanged) | Flagged — carry-over, still PENDING |

**Root cause:** Compile process (OpenClaw compile-agent) đang ghi compilation log vào `memory/` thay vì `.openclaw/memory/`. Folder-structure.md v1.2 đã migrate memory vào `.openclaw/` từ 2026-05-17.

**Khuyến nghị:** 
- 🚨 [ESCALATION — 4th occurrence] Cần process-level fix trong `compile-agent/SKILL.md` hoặc script compile — sửa output path từ `memory/` thành `.openclaw/memory/`
- File deletion/rmdir chỉ là temporary fix — folder sẽ tái xuất hiện mỗi khi compile process chạy
- Nếu quyết định giữ `memory/` ở root: cần update `folder-structure.md` để whitelist (có chủ đích, không phải workaround)

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

1. Review `wiki/reviews/2026-07-07_hygiene-report.md`
2. Nếu approve: `mv memory/compilation-log.md .openclaw/memory/` → `rmdir memory/`
3. 🚨 [ESCALATION — 4th occurrence] `memory/` recurrence (4 lần trong 5 ngày): tìm và sửa compile-agent output path từ `memory/` thành `.openclaw/memory/`
4. KB structure health: 99.996% (2/51,715 paths with issues)

**Report:** `wiki/reviews/2026-07-07_hygiene-report.md`
