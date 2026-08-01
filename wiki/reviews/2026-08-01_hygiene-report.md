# Hygiene Inspector Report — 2026-08-01

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-01
**Issues found:** 5
**Created:** 2026-08-01
**Validator:** hygiene-inspector
**Paths checked:** 53,461
**Delta from 07-30:** +25 paths

---

## Issues Found

| # | Severity | Category | Path | Issue |
|---|---|---|---|---|
| 1 | **ERROR** | Orphan | `memory/` | Recurring root folder — **đã quay lại** sau 3 run sạch |
| 2 | **ERROR** | Path | `raw/tools/` | Unknown raw subfolder 'tools' |
| 3 | **ERROR** | Path | `raw/tools/2026-07-25_introducing-backsearch-gr-inc.md` | File in unknown subfolder |
| 4 | **ERROR** | Path | `raw/tools/2026-07-25_monid-ai-agent-tool-platform.md` | File in unknown subfolder |
| 5 | **WARNING** | Path | `memory/2026-07-31.md` | Orphan file in wrong location |

---

## Detail

### 1. ERROR — `memory/` quay lại (lần thứ 8)

Sau 3 run sạch liên tiếp (07-24, 07-25, 07-26), `memory/` đã tái xuất với file `memory/2026-07-31.md`. OpenClaw agent vẫn ghi memory logs vào `memory/` thay vì `.openclaw/memory/`.

**Suggested fix:** Move `memory/2026-07-31.md` → `.openclaw/memory/`, rmdir `memory/`. Root cause: cần update AGENTS.md §4.4 hoặc fix process-level.

### 2-4. ERROR — `raw/tools/` subfolder mới

Thư mục `raw/tools/` không nằm trong whitelist (`articles, papers, posts, repos, videos, websites`).

Chứa 2 file:
- `raw/tools/2026-07-25_introducing-backsearch-gr-inc.md`
- `raw/tools/2026-07-25_monid-ai-agent-tool-platform.md`
- `raw/tools/tools.md` (sub-index)

**Suggested fix:** Nếu Julius muốn thêm `tools` vào raw subfolders → cần update `wiki/meta/folder-structure.md` và `raw/raw.md`. Nếu không → move files vào `raw/articles/` hoặc subfolder phù hợp.

---

## ✅ Passing

- ✅ No `state/` — đã xóa 07-30, không tái tạo
- ✅ All wiki/ paths compliant
- ✅ No .bak/.tmp/.swp files
- ✅ No leaked agent artifacts at root
- ✅ `.openclaw/`, `.hermes/` clean

---

## Recurring Issues Tracker

| Issue | First Seen | Last Clean | Status |
|---|---|---|---|
| `memory/` at root | 06-19 | 07-26 (3 runs) | ❌ **Quay lại 01/08** |
| `state/` at root | Pre-06-27 | 07-30 | ✅ Resolved |
| `raw/tools/` | 01/08 | — | 🆕 New |

---

## Verdict

**REVISE** — 4 ERRORs (memory/ tái diễn + raw/tools/ mới).

### Action items:
1. **Julius:** Quyết định về `raw/tools/` — thêm vào whitelist hay move files?
2. **Connor/Julis:** `rmdir memory/` sau khi move file → `.openclaw/memory/`
3. **Root cause:** Trace process tạo `memory/` — đây là lần thứ 8
