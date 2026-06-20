# Format Validation — 2026-06-01 (post-fix)

**Status:** pending
**Issues found:** 57 files affected
**Created:** 2026-06-01 17:21
**Validator:** Connor (Hermes-RK800) — format-validator
**Previous run:** 2026-06-01 08:16 (86 issues)

---

## Summary

**Scope:** 186 concepts + 41 sources = 227 files
**Ground truth:** TAGS.md Pool B (16 tags: hack, tools, automation, vibecode, research, tutorial, opinion, news, defi, perpdex, layer1, layer2, law, coding, psychology, health)
**Result: REVISE** — 57 files affected (25%). Cải thiện từ 86 (41%).

---

## Issue 1: Invalid sub_tags — 51 files (IMPROVED: 80 → 51)

**Severity:** ERROR
**Category:** Frontmatter

### Invalid tag breakdown

| Tag | Count | Thực chất |
|---|---|---|
| `systems` | 21 | main_tag Pool A |
| `economic` | 15 | main_tag Pool A |
| `politic` | 7 | main_tag Pool A |
| `tech` | 2 | main_tag Pool A |
| `productivity` | 1 | main_tag Pool A |
| `ai` | 1 | main_tag Pool A |
| `crypto` | 1 | main_tag Pool A |
| `memory` | 1 | Không có trong Pool B |
| `frontend` | 1 | Không có trong Pool B |
| `economics` | 1 | Typo — `economic` là main_tag |
| `blindspots`, `behavior`, `analysis` | mỗi cái 1 | Không có trong Pool B |

**Root cause:** Compile Agent cũ. Fix Agent đã strip được ~29 files (từ 80 → 51). Còn 51 files vẫn còn main_tags trong sub_tags.

---

## Issue 2: Empty sub_tags — 6 files (UNCHANGED)

**Severity:** ERROR
**Category:** Frontmatter

**Files:**
- agent-harness.md
- code-as-substrate.md
- evolutionary-mismatch.md
- factory-missions.md
- multi-agent-taxonomy.md
- plan-execute-verify-loop.md

**Issue:** `sub_tags: []` — spec yêu cầu 1-3.

---

## ✅ Passing

- Field order: 100% correct ✓
- Wikilink format: 100% ✓
- No >3 sub_tags ✓
- Sub_tags distribution: 0 tags (6), 1 tag (10), 2 tags (179), 3 tags (32) ✓ — 211/227 files in 1-3 range
- No invalid status values ✓
- Filename conventions ✓

---

## Verdict

**REVISE** — 51 invalid sub_tags + 6 empty. 

Fix Agent đã strip được ~36% invalid tags. 51 còn lại cần re-compile hoặc Fix Agent pass thứ hai.
