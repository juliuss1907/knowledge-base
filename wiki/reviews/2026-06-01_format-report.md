# Format Validation — 2026-06-01

**Status:** pending
**Issues found:** 2 systemic issues + 6 individual issues
**Created:** 2026-06-01 08:16
**Validator:** Connor (Hermes-RK800) — format-validator

---

## Summary

**Scope:** 172 concepts + 38 sources = 210 files
**Ground truth:** `wiki/meta/format-spec.md` (found), `TAGS.md` Pool B (14 tags: hack, tools, automation, vibecode, research, tutorial, opinion, news, defi, perpdex, layer1, layer2, law, coding)
**Result: REVISE** — 86 files affected (41%). Đa số là systemic sub_tag errors.

---

## Issue 1: Invalid sub_tags — 80 files

**Severity:** ERROR
**Category:** Frontmatter
**Files affected:** 80/210
**Issue:** 80 files chứa sub_tags không có trong TAGS.md Pool B. Các tag không hợp lệ phổ biến nhất:

| Invalid tag | Count | Pool B alternative? |
|---|---|---|
| `economic` | 23 | Dùng `main_tag: economic` |
| `productivity` | 22 | Dùng `main_tag: productivity` |
| `systems` | 21 | Dùng `main_tag: system` |
| `psychology` | 13 | Không có — cần đề xuất thêm |
| `ai` | 10 | Dùng `main_tag: ai` |
| `politic` | 9 | Dùng `main_tag: politic` |
| `health` | 9 | Không có — cần đề xuất thêm |
| `tech` | 2 | Dùng `main_tag: tech` |
| `crypto` | 1 | Dùng `main_tag: crypto` |
| `memory`, `frontend`, `blindspots`, `behavior`, `analysis`, `economics` | mỗi cái 1 | Mixed |

**Root cause:** Nhiều main_tags đang bị dùng làm sub_tags (`economic`, `productivity`, `systems`, `ai`, `politic`). Đây là confusion giữa Pool A và Pool B.

**Suggested fix:** 
1. Xác định rõ: main_tags (Pool A) ≠ sub_tags (Pool B). Mỗi file đã có main_tag — không cần lặp lại làm sub_tag.
2. Giữ lại sub_tags hợp lệ (ví dụ: `automation`, `tools`, `research`, `tutorial`, `hack`, `opinion`, `news`, `law`, `coding`, `vibecode`)
3. Với `psychology` và `health`: hoặc đề xuất Julius thêm vào Pool B, hoặc dùng tag hiện có gần nhất.

---

## Issue 2: 0 sub_tags — 6 files

**Severity:** ERROR
**Category:** Frontmatter
**Files affected:**
- agent-harness.md
- code-as-substrate.md
- evolutionary-mismatch.md
- factory-missions.md
- multi-agent-taxonomy.md
- plan-execute-verify-loop.md

**Issue:** 6 files có `sub_tags: []` (trống). Spec yêu cầu 1-3 sub_tags.

**Suggested fix:** Thêm ít nhất 1 sub_tag từ Pool B cho mỗi file.

---

## ✅ Passing

- **Field order:** 100% correct (main_tag trước sub_tags) ✓
- **Wikilink format:** 100% quoted trong frontmatter ✓
- **Status values:** 100% `draft` (valid) — không còn `stub` ✓
- **Type field:** 100% correct (`concept` trong concepts/, `source` trong sources/) ✓
- **No >3 sub_tags:** 0 files vượt quá limit ✓
- **Sub_tags count 2-3:** 128 files (2 tags) + 76 files (3 tags) = 204/210 files in valid range ✓
- **Filename conventions:** Tất cả files theo đúng format (`*.md` trong đúng folder) ✓

---

## Verdict

**REVISE** — 86 files affected: 80 invalid sub_tags + 6 thiếu sub_tags.

Đây là systemic issue: Compile Agent đang dùng main_tags làm sub_tags. Cần cập nhật compile prompt để phân biệt rõ Pool A (main_tag) và Pool B (sub_tags). Sau khi Julius quyết định có thêm `psychology`, `health` vào Pool B không, số lượng invalid sẽ giảm đáng kể.
