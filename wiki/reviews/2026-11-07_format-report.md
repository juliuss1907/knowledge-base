# Format Validation — 2026-11-07

**Status:** pending
**Issues found:** 396
**Created:** 2026-11-07 10:22:07 +0700
**Validator:** format-validator

## Summary

| Metric | Count |
|---|---|
| Files checked | 1172 |
| Concepts | 638 |
| Sources | 225 |
| Indexes | 34 |
| Topics (skipped) | 275 |
| Total issues | 396 |
| ERRORs | 2 |
| WARNINGs | 394 |

## ERRORs (2)

### E1 — sub_tags contains Pool A tag `productivity` (2 files)

1. `wiki/concepts/socratic-prompting.md` — sub_tags contains `productivity` (Pool A only)
2. `wiki/sources/src_claude-best-practices-power-user-guide.md` — sub_tags contains `productivity` (Pool A only)

**Action:** Kara (Fix Agent) cần thay thế `productivity` bằng Pool B tag hợp lệ.

## WARNINGs (394)

### W1 — Broken wikilinks (forward-references) — 394 instances

Systemic pattern: Compile Agent tạo wikilink đến concept chưa tồn tại. Đây là forward-references, không phải lỗi per-file. Carry-forward từ các report trước.

**Action:** Không cần sửa. Giảm dần khi Compile Agent tạo thêm concepts.

## Notes

