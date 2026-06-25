# Format Validation — 2026-06-25

**Status:** pending
**Issues found:** 322 in requested scope (`463` raw script findings minus `23` out-of-scope tag warnings and `118` out-of-scope topic-file errors)
**Created:** 2026-06-25 23:15:51 +07
**Validator:** format-validator

> **Ground truth:** `wiki/meta/format-spec.md`
> **Requested scope:** `wiki/concepts/*.md` + `wiki/sources/*.md`
> **Scope note:** The reusable validator script still scans `wiki/tag/*.md` and `wiki/topic/*.md`. This report excludes those findings because this cron instruction explicitly limited validation to concepts and sources.

---

## Delta vs most recent approved format report

Reference baseline: approved/applied Format Validator run dated `2026-06-25 15:53`.

| Metric | Current run | Previous approved | Delta |
|---|---:|---:|---:|
| Files checked in requested scope | 436 | 436 | 0 |
| In-scope issues | 322 | 322 | 0 |
| In-scope ERROR | 8 | 8 | 0 |
| In-scope WARNING | 314 | 314 | 0 |
| In-scope INFO | 0 | 0 | 0 |
|
**Positive delta:** None.
**Negative delta:** None.
**Assessment:** No format drift detected inside `wiki/concepts/` and `wiki/sources/` since the last approved run.

---

## Summary

| Metric | Value |
|---|---:|
| Concepts checked | 334 |
| Sources checked | 102 |
| Requested-scope files checked | 436 |
| Raw script findings | 463 |
| Excluded `wiki/tag/*.md` warnings | 23 |
| Excluded `wiki/topic/*.md` errors | 118 |
| **In-scope ERRORs** | **8** |
| **In-scope WARNINGs** | **314** |
| **In-scope INFOs** | **0** |
| **In-scope total** | **322** |

---

## Issue 1: Code blocks missing language tags

**Severity:** ERROR
**Category:** Markdown
**Issue:** Fenced code blocks use bare triple backticks without a language identifier.
**Current:** ```
**Expected:** ```bash, ```python, ```yaml, ```json, or another explicit language tag required by `format-spec.md` §4.
**Suggested fix:** Add the correct language tag to every fenced code block.

**Affected files:**
1. `wiki/concepts/ai-coach-prompting.md`
2. `wiki/concepts/content-generation-workflow.md`
3. `wiki/concepts/dollar-as-rent-payment.md`
4. `wiki/concepts/existential-vacuum.md`
5. `wiki/concepts/expert-knowledge-extraction.md`
6. `wiki/concepts/trading-addiction-cycle.md`
7. `wiki/concepts/x-search-tool.md`
8. `wiki/sources/src_petrodollar-system-analysis.md`

---

## Issue 2: Broken wikilinks / forward references

**Severity:** WARNING
**Category:** Markdown
**Issue:** 312 wikilinks inside concepts and sources point to targets that do not exist yet.
**Current:** Links resolve to non-existent concept/source slugs.
**Expected:** Internal links should point to existing wiki files, or be accepted as explicit forward references until the target exists.
**Suggested fix:** Create the missing target files, or defer if the links are intentional forward references in a growing KB.

**Most repeated missing targets:**
- `[[game-theory]]` — 9 references
- `[[confirmation-bias]]` — 8 references
- `[[pareto-principle]]` — 6 references
- `[[ai-coding-agents]]` — 5 references
- `[[career-design]]` — 5 references
- `[[decision-making]]` — 5 references
- `[[deep-work]]` — 4 references

**Assessment:** Đây vẫn là pattern forward-reference chiếm đa số warnings. Không có dấu hiệu regression mới trong requested scope.

---

## Issue 3: Frontmatter field order mismatch

**File:** `wiki/sources/src_dan-koe-workflow-analysis-markus.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** Thứ tự fields trong YAML frontmatter không khớp `format-spec.md` §3.2.
**Current:** Field order mismatch.
**Expected:** `type`, `original`, `main_tag`, `sub_tags`, `topic`, `date_compiled`, rồi optional `url`, `author`.
**Suggested fix:** Sắp xếp lại frontmatter theo đúng thứ tự spec.

---

## Issue 4: Broken `original` raw-file reference

**File:** `wiki/sources/src_map-is-not-territory.md`
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `original: "[[2026-06-03_map-is-not-territory]]"` trỏ tới raw file không tồn tại.
**Current:** Wikilink frontmatter không resolve được trong `raw/`.
**Expected:** `original` phải trỏ tới raw file hiện có.
**Suggested fix:** Khôi phục raw file đúng slug hoặc sửa `original` sang target tồn tại.

---

## Requested-scope clean areas

- Không có lỗi naming convention trong `wiki/concepts/` hoặc `wiki/sources/`.
- Không có lỗi YAML syntax trong requested scope.
- Không có lỗi thiếu section bắt buộc hoặc sai heading level trong requested scope.
- Không có INFO items trong requested scope.

---

## Excluded from actionable count

### Out-of-scope tag files — 23 WARNING

`wiki/tag/*.md` vẫn dùng `parent: [[tag]]` không có quotes. Đây là issue ngoài requested scope của run này.

### Out-of-scope topic files — 118 ERROR

Script hiện tại vẫn report `wiki/topic/*.md` là `No frontmatter: Missing opening ---`.
Theo current instruction của run này, topic files không nằm trong phạm vi actionable report.

---

## Verdict

**REVISE** — 8 direct Markdown format errors còn tồn tại. Phần còn lại chủ yếu là forward-reference warnings và 2 frontmatter warnings đơn lẻ trong requested scope.

## Verification

```bash
test -f "wiki/reviews/2026-06-25_format-report.md" && echo "✅ Report written"
```