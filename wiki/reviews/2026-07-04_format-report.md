# Format Validation — 2026-07-04

**Status:** pending
**Issues found:** 331 (3 ERROR, 328 WARNING, 0 INFO)
**Created:** 2026-07-04 23:16:16 +0700
**Validator:** format-validator
**Scope:** Full KB — 694 files (388 concepts + 126 sources + 33 indexes + 147 topics)

---

## Delta from last approved (2026-07-01 23:15)

| Metric | 2026-07-01 (APPROVED) | 2026-07-04 | Delta |
|---|---|---|---|
| Scope | 665 files | 694 files | **+29** |
| ERROR | 1 | 3 | **+2** |
| WARNING | 311 | 328 | **+17** |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ **7 individual broken wikilinks resolved** — 283 individual broken wikilinks (down from 290). Targets như `pareto-principle`, `sunk-cost-fallacy`, `anchoring` giờ đã có concept.
- ✅ **tag/tag.md frontmatter errors resolved** — `level`, `auto_generated`, `items_managed_by`, và `parent` đã được sửa (3 trong 5 ERROR từ 07-02/07-03 đã resolve). Còn lại 2 section ERROR (Overview, Parent).
- ✅ **Topic files clean** — 147 topic files pass light validation, stable since 07-01.
- ✅ **Code-block language tags resolved** — confirmed still resolved (stable since 06-26).

**Negative delta (new/regression):**
- 🔴 **+2 ERROR trên `wiki/tag/tag.md`** — 2 section vẫn thiếu: `## Overview` và `## Parent`. Từ 5 ERROR (07-02/07-03) → còn 2 ERROR. 3 ERROR kia (level, auto_generated, items_managed_by, parent) đã được fix.
- 🔴 **24 unquoted wikilink WARNINGs REAPPEARED** — Regression. Đã resolve 07-03 (Index Agent regenerated với quoted format), nhưng hôm nay (07-04) Index Agent regenerate lại với format cũ. 24 file `wiki/tag/*.md` hiện có `parent: [[tag]]` (unquoted).
- 🔴 **Pre-approved exception**: `src_youre-being-trained-for-a-world-that-no-longer-exists.md` — slug 53 chars. Julius approved exception on 2026-07-02. Carried over.

**WARNING delta (07-01 → 07-04):**
- ⚠️ **+17 WARNING**: Net increase = 24 unquoted wikilink (regression) − 7 broken wikilinks resolved = +17
- 283 individual broken wikilinks + 21 forward-reference summary groups + 24 unquoted wikilink = 328
- 192 unique broken targets (down from 194)

**Note:** 2026-07-02 (340 issues, still PENDING) và 2026-07-03 (317 issues, still PENDING) là các báo cáo trung gian chưa được Julius approve. Delta tracking dùng baseline 07-01 (APPROVED).

---

## Summary

2 vấn đề tồn đọng:

1. **tag/tag.md còn thiếu 2 section** — `## Overview` và `## Parent`. Đây là carry-over từ 07-02 (5 ERROR → giờ còn 2). Fix Agent chưa chạy vì báo cáo 07-02 + 07-03 vẫn PENDING.

2. **24 unquoted wikilink regression** — Index Agent regenerate tag files hôm nay (07-04) dùng format `parent: [[tag]]` (unquoted) thay vì `parent: "[[tag]]"` (quoted). Đây là format cũ đã resolve 07-03 nay quay lại.

1 ERROR slug-too-long vẫn là pre-approved exception — không cần action.

Broken wikilinks giảm nhẹ: 283 individual (từ 290) + 21 groups. 192 unique targets (từ 194).

---

## Issue 1: tag/tag.md — Missing required section: Overview

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Sections
**Issue:** Thiếu `## Overview` — Tầng 2 index yêu cầu section này để mô tả index
**Current:** Không có section `## Overview`
**Expected:** `## Overview` với mô tả ngắn gọn về tag index system
**Suggested fix:** Thêm `## Overview` trước `## Stats`

---

## Issue 2: tag/tag.md — Missing required section: Parent

**File:** `wiki/tag/tag.md`
**Severity:** ERROR
**Category:** Sections
**Issue:** Thiếu `## Parent` — Tầng 2 index yêu cầu link lên Tầng 1
**Current:** Không có section `## Parent`
**Expected:** `## Parent` với wikilink `[[wiki]]`
**Suggested fix:** Thêm `## Parent` với nội dung `- [[wiki]]`

---

## Issue 3: Slug exceeds 50-character limit (PRE-APPROVED EXCEPTION)

**File:** `wiki/sources/src_youre-being-trained-for-a-world-that-no-longer-exists.md`
**Severity:** ~~ERROR~~ → **APPROVED EXCEPTION**
**Category:** Naming
**Issue:** Source file slug is 53 characters, exceeding the 50-character limit
**Current:** `src_youre-being-trained-for-a-world-that-no-longer-exists` (53 chars)
**Expected:** Slug ≤ 50 characters
**Status:** Julius approved exception on 2026-07-02. No action needed.
**Suggested fix:** None — exception approved

---

## Issue 4: Unquoted wikilink in tag file frontmatter — REGRESSION (×24 files)

**Files:** 24 files under `wiki/tag/*.md` (all except `tag.md`)
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `parent` field uses unquoted `[[tag]]` format, parsed as YAML list instead of string
**Current:** `parent: [[<parent-tag>]]` (unquoted)
**Expected:** `parent: "[[<parent-tag>]]"` (quoted, per format-spec.md §9)
**Root cause:** Index Agent regenerate tag files today (07-04) with old template using unquoted format. This was resolved 07-03 and has now regressed.
**Suggested fix:**
1. Update `index-agent/SKILL.md` template to use `parent: "[[tag]]"` (quoted)
2. Fix Agent wrap quotes on all 24 tag files
3. Monitor: đảm bảo Index Agent không overwrite với format cũ sau khi fix

**Affected files:** `wiki/tag/ai.md`, `wiki/tag/automation.md`, `wiki/tag/coding.md`, `wiki/tag/crypto.md`, `wiki/tag/defi.md`, `wiki/tag/economic.md`, `wiki/tag/geopolitics.md`, `wiki/tag/hack.md`, `wiki/tag/health.md`, `wiki/tag/investment.md`, `wiki/tag/law.md`, `wiki/tag/layer1.md`, `wiki/tag/news.md`, `wiki/tag/opinion.md`, `wiki/tag/politic.md`, `wiki/tag/productivity.md`, `wiki/tag/psychology.md`, `wiki/tag/research.md`, `wiki/tag/system.md`, `wiki/tag/tech.md`, `wiki/tag/tools.md`, `wiki/tag/tutorial.md`, `wiki/tag/vibecode.md`, `wiki/tag/tag.md`

---

## Issue 5: Broken wikilink backlog — 283 individual + 21 groups

**Severity:** WARNING
**Category:** Markdown
**Issue:** 283 individual broken wikilinks + 21 forward-reference summary groups across concepts and sources
**Unique broken targets:** 192
**Nature:** Forward-references to uncompiled concepts — expected in a growing KB
**Top 5 broken targets:**
| Target | Count |
|---|---|
| `[[game-theory]]` | 10× |
| `[[confirmation-bias]]` | 8× |
| `[[ai-coding-agents]]` | 5× |
| `[[career-design]]` | 5× |
| `[[decision-making]]` | 5× |

**Top files by warning count:**
| File | Broken wikilinks |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |

**Suggested fix:** No action needed — forward-references tự resolve khi concepts được compile. Prioritize compiling top targets nếu muốn giảm backlog.

---

## Escalations

### [SYSTEMATIC VIOLATION] Unquoted wikilink regression

```
[SYSTEMATIC VIOLATION]
Pattern: 24 tag files have parent: [[tag]] (unquoted) — same format as 07-02
Resolution 07-03: Index Agent regenerated with quoted format → 0 warnings
Regression 07-04: Index Agent regenerated again with UNQUOTED format → 24 warnings back
Likely cause: Index Agent SKILL.md template still uses unquoted format.
              Resolution on 07-03 was a one-time generate, not a template fix.
Recommendation: Update index-agent/SKILL.md tag file template to use parent: "[[tag]]" (quoted).
               Without template fix, every Index Agent run will reintroduce this warning.
```

### [SPEC CONFLICT] index-spec.md shows unquoted wikilinks

```
[SPEC CONFLICT]
Issue: index-spec.md examples show parent: [[tag]] (unquoted)
format-spec.md §9 note: wikilinks in frontmatter must be quoted ("[[...]]")
Status: Known conflict — carried over from 07-02, 07-03
Recommendation: Update index-spec.md to show quoted format for consistency
```

---

## KB Format Health

- **Files with ERROR:** 2 / 694 (0.29%)
- **Files with WARNING:** ~160 / 694 (23%) — mostly forward-reference wikilinks
- **Clean files:** ~532 / 694 (77%)
- **Overall health:** 99.71% ERROR-free
