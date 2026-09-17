# Output Validation — 2026-09-14

**Status:** approved
**Approved by:** Julius
**Approved at:** 2026-09-17 08:57 +0700
**Ghi chú duyệt:** Đã duyệt; chưa xác minh áp dụng sửa lỗi. Connor chỉ cập nhật báo cáo. Fix Agent xử lý ký tự lẫn ngôn ngữ và lỗi dính chữ theo danh sách. Chưa tự chọn xóa các liên kết goal-setting. Số mức độ ở đầu báo cáo không khớp từng mục (mục 1: ERROR; mục 2 và 3: WARNING); không dùng tổng 2E+1W làm bằng chứng đã xác minh.
**Issues found:** 4 (2 ERROR, 1 WARNING, 1 INFO)
**Created:** 2026-09-14 23:00:54
**Validator:** output-validator

---

## Files checked

**New files (compiled 09-14):** 7 (2 sources + 5 concepts)
**Carry-over from 09-12 (new since last output report):** 2 (1 source + 1 concept)
**Total new:** 9
**Existing KB:** 782 (200 sources + 582 concepts)

**Dropped-i variant 5 grep:** 0 matches (all 4 sub-patterns). Streak: 15 consecutive clean runs (08-23 → 09-14).

---

## Issue 1: Chinese characters "注意力" in Vietnamese text

**Files:**
- `wiki/sources/src_delusional-goals-drive-success.md` (line 31)
- `wiki/concepts/reality-distortion-field.md` (lines 16, 24)
- `wiki/concepts/goal-as-filter.md` (line 24)

**Severity:** ERROR
**Dimension:** Vietnamese quality / Factual
**Issue:** Chinese character "注意力" (zhùyìlì, meaning "attention") appears 4 times across 3 files, injected by Compile Agent instead of Vietnamese equivalent.
**Evidence:**
- `src_delusional-goals-drive-success.md:31`: "định hướng注意力 của cả nhóm kỹ sư"
- `reality-distortion-field.md:16`: "định hướng注意力 của nhóm kỹ sư"
- `reality-distortion-field.md:24`: "phân tán注意力"
- `goal-as-filter.md:24`: "định hướng注意力 của cả nhóm kỹ sư"
**Suggested fix:** Replace all instances of "注意力" with "sự chú ý" (or "focus" in English context). This is a Compile Agent tokenization defect — the LLM output Chinese instead of Vietnamese/English. Fix Agent can apply inline sed.

**Root cause note:** Same root cause as the 09-12 batch's "既是" Chinese character injection (reported in previous output report). This is now the 2nd occurrence of Chinese character injection in Compile Agent output. Recommend review of Compile Agent prompt or model routing.

---

## Issue 2: Spacing merge "tham chiếuvừa" in harness-engineering files

**Files:**
- `wiki/sources/src_harness-engineering-ai-coding.md` (line 24)
- `wiki/concepts/harness-engineering.md` (line 26)

**Severity:** WARNING
**Dimension:** Vietnamese quality
**Issue:** Missing space: "tự tham chiếuvừa" should be "tự tham chiếu, vừa" (or "tự tham chiếu. Vừa"). Same defect propagated from source to concept.
**Evidence:**
- `src_harness-engineering-ai-coding.md:24`: "tài liệu tự tham chiếuvừa là specification vừa là health record"
- `harness-engineering.md:26`: "Document tự tham chiếuvừa là specification vừa là health record"
**Suggested fix:** Insert space and comma: "tự tham chiếu, vừa là". Fix Agent inline.

---

## Issue 3: Forward-reference without raw source [[goal-setting]]

**Files:**
- `wiki/sources/src_delusional-goals-drive-success.md` (line 41: `[[goal-setting]]`)
- `wiki/concepts/delusional-goals.md` (line 31: `[[goal-setting]]`)
- `wiki/concepts/reality-distortion-field.md` (line 30: `[[goal-setting]]`)

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** `[[goal-setting]]` referenced in 3 files but no concept file, no source file, and NO raw material exists anywhere in `raw/`. No natural resolution path.
**Evidence:** `find raw/ -iname '*goal-setting*'` → 0 hits. `find wiki/ -iname '*goal-setting*'` → 0 hits.
**Suggested fix:** Two options: (a) Compile `goal-setting` concept when suitable source material arrives, or (b) Fix Agent drops the `[[goal-setting]]` wikilinks from all 3 files. Format Validator will track target in broken-targets backlog.

---

## Issue 4: Source file uses "## Key points" instead of "## Key points" — NOT an issue (verified)

**File:** `wiki/sources/src_harness-engineering-ai-coding.md`
**Severity:** N/A (checked, not an issue)
**Note:** Verified line 25 uses `## Key points` — correct per format-spec §3.3 for sources. No defect.

---

## Issue 5: harness-engineering.md has empty "## Notes" section

**File:** `wiki/concepts/harness-engineering.md`
**Severity:** INFO (not an issue)
**Note:** Empty `## Notes` is intentional per Compile Agent template. Not flagged per standing convention.

---

## Issue 6: All 7 new concept files have status: draft

**Files:** All 5 concepts compiled 09-14 + harness-engineering.md (09-12)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** All new concept files have `status: draft` in frontmatter. This is the expected default from Compile Agent. No action needed — status changes when concepts are promoted.
**Note:** Not an actionable issue; logged for awareness.

---

## Issue 7: Forward-references in harness-engineering (5 targets — 1 without raw)

**File:** `wiki/concepts/harness-engineering.md` (line 31-36)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** 5 concept references in Related: [[context-engineering]], [[progressive-hardening]], [[three-enforcement-loops]], [[agent-harness]], [[vibe-coding]], [[agentic-coding]]. Of these, 5 exist as concepts and 1 (`[[context-engineering]]`) also has a concept file. All targets have existing concept files. No missing targets.
**Note:** Verified all targets exist. No action needed.

---

## Summary

| Severity | Count | Description |
|---|---|---|
| ERROR | 2 | Chinese characters "注意力" (4 instances, 3 files); root cause = same as 09-12 "既是" injection |
| WARNING | 1 | Spacing merge "tham chiếuvừa" (2 files, same root); Forward-ref [[goal-setting]] without raw |
| INFO | 1 | All new concepts status:draft (expected default) |

**Systemic pattern:** Chinese character injection into Vietnamese text is now 2nd occurrence (09-12: "既是", 09-14: "注意力"). Both in Dan Koe / Substack content compiled by same pipeline. Recommend Compile Agent prompt review to prevent LLM fallback to CJK characters when generating Vietnamese text.

**Dropped-i streak:** 15 consecutive clean (08-23 → 09-14). Demotion to weekly recommended (threshold reached at streak 10, 09-01).

**Action items for Fix Agent:**
1. Replace "注意力" → "sự chú ý" in 3 files (4 instances)
2. Fix spacing "tham chiếuvừa" → "tham chiếu, vừa" in 2 files
3. Decide on `[[goal-setting]]`: compile or drop links (3 files)
