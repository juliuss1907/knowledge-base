# Format Validation — 2026-07-03

**Status:** approved
**Approved by:** Julius — 2026-07-05
**Issues found:** 317 (6 ERROR, 311 WARNING, 0 INFO)
**Created:** 2026-07-03 23:17:01 +0700
**Validator:** format-validator
**Scope:** Full KB — 670 files (376 concepts + 121 sources + 33 indexes + 140 topics)

---

## Delta from last approved (2026-07-01 23:15)

| Metric | 2026-07-01 (APPROVED) | 2026-07-03 | Delta |
|---|---|---|---|
| Scope | 665 files | 670 files | **+5** |
| ERROR | 1 | 6 | **+5** |
| WARNING | 311 | 311 | **0** |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ **23 unquoted wikilink WARNINGs resolved** — Tất cả 23 `wiki/tag/*.md` files giờ có `parent: "[[tag]]"` (quoted). Index Agent đã regenerate với format đúng. Spec conflict index-spec.md vs format-spec.md §9 đã được xử lý thực tế.
- ✅ **Topic files clean** — 140 topic files pass light validation, no regression (ổn định từ 07-01)
- ✅ **Tag file sections resolved** — 69 tag-file section ERRORs từ 06-29 remain resolved (confirmed stable through 4 consecutive runs)
- ✅ **Code-block language tags resolved** — confirmed still resolved (stable since 06-26)

**Negative delta (new/regression):**
- 🔴 **+5 ERRORs trên `wiki/tag/tag.md`** — surfaced 07-02, still present 07-03. File có `level: 1` nhưng filesystem path yêu cầu `level: 2`. Ngoài ra thiếu 4 section và sai `auto_generated`. Không phải regression từ Index Agent hôm nay — tag/tag.md không được regenerate (giữ nguyên từ 07-02).
- 🔴 **Pre-approved exception**: `src_youre-trained-for-world-that-no-longer-exists.md` — slug 53 chars. Julius approved exception on 2026-07-02. Carried over.

**WARNING delta (07-02 → 07-03):**
- ⚠️ **−23 WARNING**: Unquoted wikilink warnings → resolved (see positive delta)
- ⚠️ **Broken wikilinks stable**: 290 individual + 21 forward-reference groups. 194 unique targets unchanged.

**Note:** 2026-07-02 report (340 issues, still PENDING) had 23 more WARNINGs than today. Today's count matches 07-01 baseline (311) because the 23 unquoted wikilink WARNINGs surfaced 07-02 and resolved 07-03.

---

## Summary

Chỉ 1 vấn đề mới tồn đọng: **5 ERROR trên `wiki/tag/tag.md`** — file index gốc của tag system có `level: 1` sai với filesystem path (phải là 2). Các expected values trong báo cáo hôm qua (07-02) và script hôm nay bị sai một phần vì validator dispatch theo trường `level` thay vì path-derived tier.

1 ERROR slug-too-long vẫn là pre-approved exception — không cần action.

Broken wikilinks stable ở 290 + 21 groups / 194 unique targets — không thay đổi từ 07-01.

**Correction:** Báo cáo này sửa expected values cho tag/tag.md — dùng Tầng 2 rules (path-derived) thay vì Tầng 1 (level field).

---

## Issue 1: tag/tag.md — level field contradicts filesystem path

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter — Cross-validation
**Issue:** `level: 1` nhưng filesystem path `wiki/tag/tag.md` → Tầng 2 theo index-spec.md §4.1
**Current:** `level: 1`
**Expected:** `level: 2`
**Impact:** Validator dispatch sai spec → 4/5 ERROR có expected values sai trong báo cáo 07-02. Các issue bên dưới được đánh giá lại theo Tầng 2 rules.
**Suggested fix:** Đổi `level: 1` → `level: 2`

---

## Issue 2: tag/tag.md — auto_generated flag

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `auto_generated: true` — Tầng 2 index yêu cầu `auto_generated: false` (file được maintain thủ công bởi Index Agent)
**Current:** `auto_generated: true`
**Expected:** `auto_generated: false`
**Suggested fix:** Đổi `auto_generated` → `false`

---

## Issue 3: tag/tag.md — Missing required field items_managed_by

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** Thiếu trường `items_managed_by` — Tầng 2 index yêu cầu field này (giá trị: `ingest-agent` hoặc `index-agent`)
**Current:** Không có field `items_managed_by`
**Expected:** `items_managed_by: index-agent`
**Suggested fix:** Thêm `items_managed_by: index-agent` vào frontmatter

---

## Issue 4: tag/tag.md — parent field is null

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `parent: null` — Tầng 2 index yêu cầu parent là wikilink đến Tầng 1
**Current:** `parent: null`
**Expected:** `parent: "[[wiki]]"` (trỏ đến `wiki/wiki.md`)
**Suggested fix:** Đổi `parent` → `"[[wiki]]"`

---

## Issue 5: tag/tag.md — Missing required sections

**File:** `wiki/tag/tag.md`
**Severity:** ERROR (×4)
**Category:** Sections
**Issue:** Thiếu 4 section bắt buộc cho Tầng 2 index per index-spec.md §4

**Hiện có:** `## Stats`, `## Main Tags (Pool A)`, `## Sub Tags (Pool B)`
**Còn thiếu:**
- `## Overview` — mô tả index này là gì
- `## Parent` — link lên Tầng 1 (`wiki/wiki.md`)
- `## Items` — danh sách sub-index pages (23 tag files). Hai section `## Main Tags` và `## Sub Tags` hiện tại có thể serve như Items.
- `## Notes` — curator annotations

**Suggested fix:**
1. Thêm `## Overview` ngắn gọn
2. Thêm `## Parent` với link `[[wiki]]`
3. Đổi tên `## Main Tags (Pool A)` → `## Items` (hoặc gộp 2 section Pool A + Pool B dưới `## Items`)
4. Thêm `## Notes`

**Note:** Các expected values trong báo cáo 07-02 (`## Sub-indexes` thay vì `## Parent` + `## Items`) là sai vì validator dispatch theo `level: 1` (Tầng 1 rules). Báo cáo này dùng đúng Tầng 2 rules.

---

## Issue 6: Slug exceeds 50-character limit (PRE-APPROVED EXCEPTION)

**File:** `wiki/sources/src_youre-trained-for-world-that-no-longer-exists.md`
**Severity:** ~~ERROR~~ → **APPROVED EXCEPTION**
**Category:** Naming
**Issue:** Source file slug is 53 characters, exceeding the 50-character limit
**Current:** `src_youre-trained-for-world-that-no-longer-exists` (53 chars)
**Expected:** Slug ≤ 50 characters
**Status:** Julius approved exception on 2026-07-02 — no action needed. Carried over from 07-01 and 07-02 reports.

---

## Issue 7: Broken wikilinks — Stable backlog (290 individual + 21 groups)

**Severity:** WARNING (311 total, stable from 07-01)
**Category:** Markdown
**Issue:** 290 individual broken wikilinks + 21 forward-reference summary groups across concepts and sources. These are forward-references to concepts not yet compiled — expected in a growing KB.

**Top 10 broken targets:**
| Target | Occurrences |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[pareto-principle]]` | 6 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |

**194 unique broken targets total** — unchanged from 07-01, 07-02, and 06-30. Stable backlog.

**Top 5 files by warning count:**
| File | Warnings |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |

These will auto-resolve when target concepts are compiled. No action needed.

---

## KB Format Health

| Metric | Value |
|---|---|
| Files checked | 670 |
| ERROR rate | 0.90% (6/670) — 5 on 1 index file + 1 pre-approved |
| ERROR rate (excluding pre-approved) | 0.75% (5/670) |
| WARNING rate | 46.4% (311/670) — nearly all are forward-reference broken wikilinks |
| Actual structural issues | 5 (5 ERRORs on tag/tag.md) |
| KB format health score | **99.3%** (excl. forward-ref broken wikilinks) |
| Health trend | ↑ from 99.1% (07-02) — 23 unquoted wikilink WARNINGs resolved |

---

## Escalation

### [LEVEL-PATH CONTRADICTION] tag/tag.md level field

```
File: wiki/tag/tag.md
Issue: level: 1 contradicts filesystem path (wiki/tag/ → Tầng 2)
Impact: Validator dispatched to wrong spec tier, producing incorrect expected values
Resolution: This report uses path-derived tier (Tầng 2) for correct expected values
Recommendation: Fix Agent should update level: 1 → level: 2 along with other fixes
Validator fix: validate.py should cross-check level field against path before dispatching
```

---

**Report complete.** Review at `wiki/reviews/_action-required.md`
**Commands:** `approve format` hoặc `show format`
