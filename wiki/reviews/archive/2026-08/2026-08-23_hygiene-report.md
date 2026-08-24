# Hygiene Inspection — 2026-08-23

**Status:** applied
**Approved by:** Julius
**Issues found:** 1
**Created:** 2026-08-23 23:32:08
**Validator:** hygiene-inspector

**Paths checked:** 55832

---

## Issue 1: File not in root whitelist

**Path:** `openclaw-workspace-state.json`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** `openclaw-workspace-state.json` tại KB root (69 bytes, JSON runtime state: `version 1, setupCompletedAt 2026-05-12`)
**Expected:** Chỉ AGENTS.md, TAGS.md, README.md, knowledge-base.md, 5 symlinks, .gitignore được phép ở root
**Suggested fix:** Root-cause: redirect OpenClaw session runtime state output về `.openclaw/` (hoặc ~/.openclaw/), sau đó `git rm openclaw-workspace-state.json` + commit

---

## Escalation

```
[SYSTEMATIC VIOLATION]
Path: openclaw-workspace-state.json
Pattern: LẦN 2 LIÊN TIẾP xuất hiện ở KB root (08-22, 08-23).
  08-22: flagged ERROR — approved + applied inline 2026-08-23 sáng nay
         (git rm → ~/.openclaw/) bởi Connor.
  08-23: OpenClaw runtime RECREATE file lúc 12:25 cùng ngày;
         git auto-commit (~10-min vault backup) re-track file vào repo.
Likely cause: Một tiến trình OpenClaw session ghi workspace state trực tiếp
  vào KB root thay vì agent home (.openclaw/ hoặc ~/.openclaw/).
  File là git-tracked → filesystem deletion chỉ xóa working copy;
  committed copy sống sót và tái xuất hiện ở lần checkout/sync kế tiếp.
Recommendation: Root-cause fix BẮT BUỘC — xác định process ghi file
  (session bootstrap/runtime state writer) và redirect output path về
  agent home. Sau đó `git rm openclaw-workspace-state.json` + commit.
  Deletion đơn thuần ĐÃ CHỨNG MINH VÔ HIỆU (recycle < 12 giờ).
```

---

## Ghi chú chạy

- **55832 paths checked** (+23 so với 08-22: 55809) — tăng trưởng bình thường từ ingest pipeline.
- **`memory/` và `state/`: VẮNG MẶT** — chạy sạch thứ 2 liên tiếp sau khi Fix Agent dọn batch 08-22. Streak tiếp tục.
- **Không HEARTBEAT leak** — `wiki/HEARTBEAT.md`, `wiki/reviews/HEARTBEAT.md`, `raw/.last_heartbeat` đều vắng mặt.
- **Không naming violation** — raw/concepts/sources/tag/topic/drafts/reviews đều đạt chuẩn. Không `.bak`/`.tmp` sót lại.
- **WARNING 08-22 đã resolved:** `wiki/drafts/fixagent-regen-tags.py` không còn trong drafts/.
- **Khuyến nghị script:** thêm `openclaw-workspace-state.json` vào `ROOT_ORPHAN_MAP` trong scan-script để theo dõi recurrence có cấu trúc (cần patch khi không phải cron mode).

---

*Validator: hygiene-inspector v1.20 — read-only. Không file/folder nào bị sửa đổi ngoài wiki/reviews/.*

**Applied:** 2026-08-24 09:58 by Fix Agent (Kara) — fixes verified in place (applied inline by Connor 09:48); report archived.
