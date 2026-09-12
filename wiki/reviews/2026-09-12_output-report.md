# Output Validation — 2026-09-12

**Status:** pending
**Issues found:** 2
**Created:** 2026-09-12 23:00:46
**Validator:** output-validator

---

## Issue 1: Chinese characters in Vietnamese content

**File:** `wiki/sources/src_harness-engineering-ai-coding.md`
**Severity:** ERROR
**Dimension:** Vietnamese quality
**Issue:** Chinese characters "既是" appear mid-sentence in Vietnamese summary text, breaking readability and introducing non-Vietnamese content without justification.
**Evidence:** Line 24: `...tài liệu tự tham chiếu既是 specification vừa là health record...`
**Suggested fix:** Replace "既是" with appropriate Vietnamese. Should read: `...tài liệu tự tham chiếu vừa là specification vừa là health record...`

---

## Issue 2: Chinese characters in Vietnamese content (same root cause)

**File:** `wiki/concepts/harness-engineering.md`
**Severity:** ERROR
**Dimension:** Vietnamese quality
**Issue:** Same Chinese characters "既是" from source propagated into concept compilation.
**Evidence:** Line 26: `- **Living harness:** Document tự tham chiếu既是 specification vừa là health record...`
**Suggested fix:** Replace "既是" with "vừa là" — source and concept should both read `...vừa là specification vừa là health record...`

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 2 |
| WARNING | 0 |
| INFO | 0 |

**Files checked:** 775 (198 sources + 577 concepts)
**New files today:** 5 (1 source + 4 concepts)
**Dropped-i streak:** 14 consecutive (08-23 → 09-12), variant 5 grep clean

**Notes:**
- Both ERRORs are the same defect (Compile Agent injected Chinese characters "既是" into Vietnamese text). Present in source file and propagated to concept.
- All forward references in new files resolve (`[[agentic-coding]]`, `[[agent-skill-management]]`, `[[vibe-coding]]`, `[[agent-harness]]` all exist).
- No duplicate key ideas, no backlink gaps, no truncated files.
- Chinese characters in `byte-level-bpe.md`, `hundred-years-humiliation.md`, `chinese-culture-confucianism.md` are INTENTIONAL (factual references to Chinese language/history) — not flagged.
