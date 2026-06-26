# HEARTBEAT.md — OpenClaw System Health

**Last check:** 2026-06-26 16:30 ICT
**Status:** `HEARTBEAT_ISSUES`

---

## System Status

| Check | Result |
|---|---|
| Raw backlog (unprocessed >24h) | 0 files |
| Raw unprocessed (today) | 2 files |
| Wiki concepts | 337 files |
| Wiki sources | 103 files |
| Total raw sources | 112 files (no change from 14:30) |
| Pending reviews | 0 — all approved/applied |

---

## Issues Found

### 1. Frontmatter Error (raw)
- ⚠️ `raw/articles/2026-06-26_give-me-14-minutes-and-ill-destroy-your-procrastination-forever.md` — dùng `type: article` thay vì `type: raw`. Sẽ khiến CompileAgent bỏ qua file này. Cần sửa trước 08:00 ngày mai.

### 2. Concept Missing Backlinks Section
- ⚠️ `wiki/concepts/impulse-response-gap.md` — thiếu `## Backlinks` section. Có `## Related concepts` và `## Sources` nhưng không có backlinks riêng.

### 3. Hygiene — Leaked File in Review Zone
- ⚠️ `wiki/reviews/HEARTBEAT.md` — vẫn tồn tại trong review zone (đã flag từ 06-25 hygiene report, chưa được xóa).

---

## Inbox

- Clean. No #agent/inbox items detected.

## Raw Backlog

- 2 files unprocessed, both from today (2026-06-26) — trong 24h window:
  - `raw/articles/2026-06-26_give-me-14-minutes-and-ill-destroy-your-procrastination-forever.md` (lỗi frontmatter)
  - `raw/articles/2026-06-26_why-china-got-rich-and-india-didnt.md` (OK)

## Concept Backlinks

- Random check: `conversational-website.md` — healthy (có Backlinks, Sources, Related concepts)
- Random check: `impulse-response-gap.md` — **thiếu `## Backlinks` section**

## Pending Reviews

- `_action-required.md`: 0 pending. Tất cả Hermes reports từ 06-25 và 06-26 đã approved/applied.

---

## Notes

- 2 file raw hôm nay chưa compile — CompileAgent sẽ xử lý 08:00 ngày mai, nhưng 1 file cần sửa frontmatter trước.
- `wiki/reviews/HEARTBEAT.md` nên được xóa — đã tồn tại qua 2 hygiene cycles.
