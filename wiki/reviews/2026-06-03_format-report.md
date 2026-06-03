# Format Validation — 2026-06-03

**Status:** applied
**Issues found:** 5 files
**Created:** 2026-06-03 08:16
**Validator:** Connor (Hermes-RK800) — format-validator
**Previous run:** 2026-06-01-v2 (16 issues → Connor tự fix → 0)

---

## Summary

**Scope:** 199 concepts + 44 sources = 243 files
**Ground truth:** TAGS.md Pool B (16 tags)
**Result: REVISE** — 5 files. Các file này được compile SAU khi Connor đã fix 16 files lần trước.

---

## Issue: Invalid sub_tags — 5 files (NEW)

**Severity:** ERROR
**Category:** Frontmatter

| File | Invalid tag | Suggested |
|---|---|---|
| compact-vs-handoff.md | `productivity` | automation |
| context-window-management.md | `productivity` | automation |
| handoff-skill.md | `productivity` | automation |
| session-separation.md | `productivity` | automation |
| src_handoff-skill-context-window-management.md | `productivity` | automation |

**Root cause:** 5 files mới được compile gần đây — Compile Agent cũ vẫn dùng `productivity` làm sub_tag.

---

## ✅ Passing

- Sub_tags count: 1-3 range — 100% ✓
- Empty sub_tags: 0 ✓
- >3 sub_tags: 0 ✓
- Field order: 100% correct ✓
- Wikilink format: 100% ✓
- No invalid status values ✓
- Filename conventions ✓

---

## Verdict

**REVISE** — 5 files, minor. Tất cả đều là `productivity` trong sub_tags — dễ fix.

Đây là các file mới được compile sau lần fix trước, Compile Agent chưa áp dụng constraint mới.
