# HEARTBEAT.md — OpenClaw System Status

**Last check:** 2026-05-29 12:30 Asia/Saigon (05:30 UTC)
**Status:** ATTENTION REQUIRED

---

## System Health

| Check | Result |
|---|---|
| Raw backlog | 7 files unprocessed (36 processed / 43 total) |
| Pending reviews | 3 reports pending Julius approval |
| Tag index | 19 tag indexes |
| Topic index | 39 topic indexes |
| Concept files | 163 files |
| Inbox | Empty |

---

## Pending Hermes Reviews (3)

| Report | Date | Issues |
|---|---|---|
| Output Validator | 2026-05-29 | 1 ERROR + 2 WARNING + 1 INFO |
| Hygiene Inspector | 2026-05-29 | 32 missing concept files → compile needed |
| Format Validator | 2026-05-28 | 7 ERROR + 14 WARNING |

**Details:** `wiki/reviews/_action-required.md`

---

## Raw Backlog

7 files in `raw/` cần compile. Logged — Julius có thể nói "compile all" để xử lý ngay hoặc đợi CompileAgent chạy sáng mai 08:00.

---

## Notes

- Format Validator scan 2026-05-29: 7 ERROR + 14 WARNING — field order, YAML syntax, section headers
- Hygiene Inspector scan 2026-05-29: 32 missing concept files — OpenClaw compile needed
- Output Validator scan 2026-05-29: 4 issues (1 ERROR + 2 WARNING + 1 INFO)