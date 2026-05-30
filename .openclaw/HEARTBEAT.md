# HEARTBEAT.md — OpenClaw System Health

> Last updated: 2026-05-30 14:02 (Asia/Saigon)
> Next check: 2026-05-30 14:30

---

## ⚠️ CRITICAL: Cron Jobs Overdue — 17 Days

Tất cả cron jobs đã overdue kể từ **2026-05-12**. Gateway vẫn chạy (PID 858811) nhưng automation đã dừng.

**Overdue jobs (10/10):**

| Job | Last Run | Next Scheduled | Status |
|-----|----------|----------------|--------|
| Compile Daily | 2026-05-12 08:48 | 2026-05-13 08:00 | ❌ error (1) |
| Index Update | 2026-05-12 08:56 | 2026-05-12 21:00 | ✅ ok |
| Git Auto-commit | 2026-05-12 08:57 | 2026-05-12 22:00 | ✅ ok |
| Weekly Health Check | 2026-05-12 08:48 | 2026-05-15 17:00 | ✅ ok |
| Horizon Morning Brief | 2026-05-12 08:57 | 2026-05-13 06:50 | ✅ ok |
| Horizon Crypto Brief | 2026-05-12 08:58 | 2026-05-13 08:50 | ✅ ok |
| Horizon Tech Brief | 2026-05-12 08:47 | 2026-05-12 12:50 | ✅ ok |
| Horizon F1 Brief | 2026-05-12 16:50 | 2026-05-12 16:50 | ✅ ok |
| Horizon Evening Reads | 2026-05-12 08:48 | 2026-05-12 20:50 | ✅ ok |
| Market Prices Update | 2026-05-12 08:46 | 2026-05-12 12:00 | ✅ ok |

**Compile Daily error:** `Edit: in raw/articles/2026-04-23_where did the kelp...md failed`

---

## System Status

| Zone | Status | Notes |
|------|--------|-------|
| raw/ | ✅ clean | 44 files, 0 unprocessed |
| wiki/sources/ | ✅ 38 files | |
| wiki/concepts/ | ✅ 172 files | |
| wiki/reviews/ | ✅ clean | 0 pending reports |
| Gateway process | ✅ running | PID 858811 |

---

## Action Required

1. **Julius cần restart cron/scheduler** — tất cả jobs overdue nhưng gateway vẫn chạy
2. **Compile Daily job** — cần check file `raw/articles/2026-04-23_where did the kelp...md`

---

*OpenClaw Heartbeat — AX400 — 2026-05-30 14:02*