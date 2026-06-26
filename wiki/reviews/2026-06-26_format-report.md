# Format Validation — 2026-06-26

**Status:** pending
**Issues found:** 314 in requested scope (`455` raw script findings minus `23` out-of-scope tag warnings and `118` out-of-scope topic-file errors)
**Created:** 2026-06-26 23:15:57 +07
**Validator:** format-validator

> **Ground truth:** `wiki/meta/format-spec.md`
> **Requested scope:** `wiki/concepts/*.md` + `wiki/sources/*.md`
> **Scope note:** Reusable validator script still scans `wiki/tag/*.md` and `wiki/topic/*.md`. Report này chỉ tính actionable findings trong requested scope.

---

## Delta vs most recent approved format report

Reference baseline: approved Format Validator run dated `2026-06-26 07:01 +07`.

| Metric | Current run | Previous approved | Delta |
|---|---:|---:|---:|
| Files checked in requested scope | 436 | 436 | 0 |
| In-scope issues | 314 | 322 | -8 |
| In-scope ERROR | 4 | 8 | -4 |
| In-scope WARNING | 310 | 314 | -4 |
| In-scope INFO | 0 | 0 | 0 |

**Positive delta:**
- 8 `Code block missing language tag` ERROR ở run approved buổi sáng đã biến mất.
- 1 frontmatter field-order WARNING trong `wiki/sources/src_dan-koe-workflow-analysis-markus.md` đã biến mất.
- 1 broken `original` WARNING trong `wiki/sources/src_map-is-not-territory.md` đã biến mất.
- Broken wikilink warnings giảm nhẹ từ 312 xuống 310.

**Negative delta:**
- Xuất hiện 4 ERROR mới: toàn bộ là YAML frontmatter parse failures trong batch `everything-is-a-win-when-the-goal`.

**Assessment:** Requested scope sạch hơn về tổng số issue, nhưng batch mới đã đưa vào 4 file không parse được frontmatter. Đây là regression mới. Không thể PROMOTE run này.

---

## Summary

| Metric | Value |
|---|---:|
| Concepts checked | 334 |
| Sources checked | 102 |
| Requested-scope files checked | 436 |
| Raw script findings | 455 |
| Excluded `wiki/tag/*.md` warnings | 23 |
| Excluded `wiki/topic/*.md` errors | 118 |
| **In-scope ERRORs** | **4** |
| **In-scope WARNINGs** | **310** |
| **In-scope INFOs** | **0** |
| **In-scope total** | **314** |

---

## Issue 1: YAML frontmatter parse failures in new experience-over-achievement batch

**Severity:** ERROR
**Category:** Frontmatter
**Issue:** 4 file mới có YAML frontmatter không parse được. Parser dừng ở `sub_tags: [#psychology, #opinion]` vì `#` trong inline flow sequence bị hiểu như comment syntax, làm frontmatter vi phạm `format-spec.md` §2.2 / §3.2.
**Current:**
- `main_tag: #productivity`
- `sub_tags: [#psychology, #opinion]`
**Expected:**
- `main_tag: productivity`
- `sub_tags: [psychology, opinion]`
- YAML frontmatter phải parse được trước khi kiểm tra các rule còn lại.
**Suggested fix:** Bỏ toàn bộ prefix `#` trong frontmatter tags của batch này. Sau đó rerun validator để xác nhận các file pass đầy đủ.

**Affected files:**
1. `wiki/concepts/experience-over-achievement.md`
2. `wiki/concepts/performative-existence.md`
3. `wiki/concepts/presence.md`
4. `wiki/sources/src_everything-is-a-win-when-the-goal.md`

**Evidence:**
- Parser error anchor: `sub_tags: [#psychology, #opinion]`
- Cả 4 file cùng pattern. Đây không phải lỗi isolated. Đây là compile regression trong cùng một batch.

---

## Issue 2: Broken wikilinks / forward references

**Severity:** WARNING
**Category:** Markdown
**Issue:** 310 wikilink warnings trong concepts và sources trỏ tới target chưa tồn tại.
**Current:** Internal links resolve tới slug không có file tương ứng trong `wiki/` hoặc `raw/`.
**Expected:** Internal links nên trỏ tới file đã tồn tại, hoặc được giữ lại có chủ đích như forward references trong KB đang mở rộng.
**Suggested fix:** Tạo missing targets cho những concept trọng yếu, hoặc chấp nhận rõ ràng đây là forward-reference backlog.

**Most repeated missing targets:**
- `[[game-theory]]` — 10 references
- `[[confirmation-bias]]` — 8 references
- `[[pareto-principle]]` — 6 references
- `[[ai-coding-agents]]` — 5 references
- `[[career-design]]` — 5 references
- `[[decision-making]]` — 5 references
- `[[deep-work]]` — 4 references

**Assessment:** Đây vẫn là backlog kiểu forward-reference. Không phải blocker tức thời như YAML parse errors.

---

## Requested-scope clean areas

- Không còn `Code block missing language tag` ERROR trong requested scope.
- Không còn frontmatter field-order WARNING trong requested scope.
- Không còn broken `original` raw-reference WARNING trong requested scope.
- Không có lỗi naming convention trong `wiki/concepts/` hoặc `wiki/sources/`.
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

## Systematic note

[SYSTEMATIC VIOLATION]
Pattern: 4/4 file trong batch `everything-is-a-win-when-the-goal` dùng hashtag-style tags trong YAML frontmatter.
Likely cause: Compile Agent hoặc manual template cho batch mới không theo `format-spec.md` frontmatter schema.
Recommendation: Review compile path cho batch 2026-06-26 liên quan `experience-over-achievement` cluster.

---

## Verdict

**REVISE** — 4 ERROR mới là hard format break. Phần còn lại chủ yếu là forward-reference warnings backlog.

## Verification

```bash
test -f "wiki/reviews/2026-06-26_format-report.md" && echo "✅ Report written"
```