# Hygiene Inspection — 2026-11-07

**Status:** pending
**Issues found:** **4 ERROR + 16 WARNING** (20 nhóm). Paths checked: 234,720.
**Created:** 2026-11-07 10:22:07 +0700
**Validator:** hygiene-inspector

## Summary

| Metric | Count |
|---|---|
| Paths checked | 234,720 |
| Total issues | 257 |
| Issues reported (unique) | 20 |
| ERRORs | 4 |
| WARNINGs | 16 |

## ERRORs (4)

### E1 — `DREAMS.md` at root (carry-forward)

File not in root whitelist. External writer process leak.

**Action:** Kara xóa hoặc di chuyển. Process ghi cần fix.

### E2 — `memory/` at root (carry-forward, recurring)

Recurring root folder `memory/` chứa `.dreams/session-corpus/` (16 file txt). Đã flag nhiều lần (07-03, 07-06, 07-07, 07-08, 07-11...).

**Action:** Move contents to `.openclaw/memory/`, rmdir. Fix writing process.

### E3 — `openclaw-workspace-state.json.migrated.*` at root (carry-forward)

Marker file từ migration cũ, vẫn tracked.

**Action:** `git rm --cached` + thêm ignore rule `*.migrated.*`.

### E4 — `wiki/HEARTBEAT.md` leaked (carry-forward)

HEARTBEAT.md trong `wiki/` root — process leak. Dangling symlink hoặc direct file.

**Action:** Xóa + fix process ghi.

## WARNINGs (16)

### W1 — `memory/.dreams/session-corpus/` — 16 unclassified files

16 file txt (2026-09-08 → 2026-09-24) trong `memory/.dreams/session-corpus/`. Không nằm trong whitelist.

**Action:** Covered by E2 (toàn bộ `memory/` cần di chuyển).

## Resolved Issues

- **E2 (vault backup):** ĐÃ PHỤC HỒI (commit tự động hoạt động bình thường)
- **E4 (credential tracking):** ĐÃ XỬ LÝ (untracked commit `380d3f74`, .gitignore updated)

## Notes

