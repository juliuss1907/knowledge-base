# Output Validation — 2026-08-16

**Status:** applied
**Approved by:** Julius
**Approved date:** 2026-08-16
**Issues found:** 3 (0 ERROR, 1 WARNING, 2 INFO)
**Created:** 2026-08-16 23:00:35
**Applied:** 2026-08-22 14:40 by fix-agent (OpenClaw)
**Validator:** output-validator

**Files checked:** 169 sources + 525 concepts
**New files:** 2 (1 source + 1 concept) — compiled today
**Overall:** Small, clean batch. No typos in the 5 known Compile Agent variants (dropped-i check via manual grep: 0 matches). No truncated files. Vietnamese quality is high. Both new files are well-structured, accurate, and coherent. A single genuine spelling typo plus two minor/pre-existing concerns.

---

## Issue 1: Vietnamese spelling typo — "lực chọn" → "lựa chọn"

**File:** wiki/concepts/ai-text-watermarking.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** In Key ideas bullet 1, the phrase `"lực chọn giữa các từ"` misspells `lựa chọn` (choice) as `lực chọn` (force-selection). This is a genuine spelling error — the same line correctly uses `lựa chọn từ` two clauses later, confirming the typo.
**Evidence:** Line 20: `Dấu nằm trong "lực chọn giữa các từ" (choices between words) — vì text không có pixels để giấu và metadata không sống sót qua copy-paste, mark phải nằm ở thứ tồn tại sau mọi thao tác: chính lựa chọn từ.`
**Suggested fix:** Change `"lực chọn giữa các từ"` to `"lựa chọn giữa các từ"`. Single-word replacement; the citation in parentheses confirms the intended meaning is "choices between words".

---

## Issue 2: Forward-reference backlinks to uncompiled concepts

**File:** wiki/concepts/ai-text-watermarking.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** `## Related concepts` links to `[[synthid]]` and `[[llm-output-detection]]`, neither of which exists in `wiki/concepts/` yet. These are legitimate forward-references that will resolve as Compile Agent processes the relevant raw sources — part of the existing 391-WARNING broken-wikilink pool already tracked by Format Validator.
**Evidence:** `## Related concepts` section (lines 29-32).
**Suggested fix:** None required now. Links resolve automatically once the target concepts are compiled. Optionally verify that raw sources for SynthID / LLM-output-detection are queued for compilation.

---

## Issue 3: Source metadata artifact + mangled English

**File:** wiki/sources/src_how-ai-text-watermarking-works.md
**Severity:** INFO
**Dimension:** Vietnamese / Completeness
**Issue:** Two minor artifacts: (a) Metadata line 16 reads `James Padolsey (NOPE, declaude)` — `NOPE` is a stray token, likely intended as "(author of declaude)"; (b) Key point 7 line 32 contains `replay key-l colouring`, where `key-l` is a mangled rendering (likely `key's`/`key` colouring).
**Evidence:** Line 16: `- **Tác giả:** James Padolsey (NOPE, declaude)`; Line 32: `Detection không đọc nội dung hay phán xét phong cách — chỉ replay key-l colouring và đếm tỷ lệ green`.
**Suggested fix:** Clean `(NOPE, declaude)` → `(tác giả declaude)`. Clarify `key-l colouring` → `key-là màu` / `key's colouring`. Cosmetic; no effect on factual accuracy.