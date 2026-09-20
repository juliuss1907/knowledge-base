# Output Validator Report — 2026-09-20

**Status:** pending
**Issues found:** 4 (2 ERROR, 2 WARNING, 0 INFO)
**Created:** 2026-09-20 23:02:00
**Validator:** output-validator
**Files checked:** 800 (592 concepts + 208 sources)
**New files:** 12 (4 sources + 8 concepts)

---

## Issue 1: Chinese characters in Vietnamese text — SYSTEMIC

**Files:** wiki/concepts/ai-chip-design.md, wiki/concepts/financial-discipline.md, wiki/concepts/life-planning-20s.md
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters (CJK Unified Ideographs) injected into Vietnamese body text — 5 instances across 3 new concept files. This is the same Compile Agent defect observed on 09-12 (`既是`) and 09-14 (`注意力`) and 09-18 (`在哪里`, `几乎`, `面临`).
**Evidence:**
- `ai-chip-design.md:22` — "...khi có AI assist —**颠覆** traditional chip design workflow..."
- `ai-chip-design.md:24` — "...so với human baseline — circuits**密度** hơn trong cùng diện tích silicon"
- `financial-discipline.md:21` — "Không trả full =**浪费** money và hurt credit score"
- `financial-discipline.md:23` — "8%/year**看起来** ít nhưng big picture hơn nhiều"
- `life-planning-20s.md:17` — "...compound thành**巨大** differences ở tuổi 30..."
**Suggested fix:** Fix Agent replace Chinese chars: `颠覆`→`thay đổi`, `密度`→`đậm đặc`, `浪费`→`lãng phí`, `看起来`→`có vẻ`, `巨大`→`to lớn`. Compile Agent prompt review recommended — 4th recurrence in 9 days.

---

## Issue 2: "người" spacing merge — variant 3

**File:** wiki/concepts/vibe-coding.md
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** "Người" merges with following word — space dropped. Same root cause as variants 1-5 (Compile Agent LLM mishandles Vietnamese diacritics).
**Evidence:**
- `vibe-coding.md:21` — "**Ngườikhông** biết code hoặc công nghệ..." → should be "**Người không** biết code..."
**Suggested fix:** Fix Agent: `sed -i 's/Ngườikhông/Người không/g' wiki/concepts/vibe-coding.md`

---

## Issue 3: Missing closing parenthesis

**File:** wiki/concepts/vibe-coding.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Opening parenthesis `(` on line 27 has no matching closing `)` — breaks sentence structure.
**Evidence:**
- `vibe-coding.md:27` — "**Kỹ năng quý giá hơn:** Marketing (**đưa sản phẩm đến với mọi người trở nên quan trọng hơn khả năng viết code**" — missing `)` before newline
**Suggested fix:** Fix Agent: add closing `)` after "viết code" on line 27.

---

## Issue 4: Forward-references without raw material — 5 unique targets

**Files:** wiki/concepts/ai-frontend-design-guidance.md, wiki/concepts/life-planning-20s.md, wiki/concepts/vibe-coding.md, wiki/sources/src_if-i-had-to-start-over-at-20-heres-what-id-do.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 5 unique wikilink targets referenced across 4 new files have no concept, no source, and no raw material anywhere in the KB — no natural resolution path. These are forward-refs that cannot self-resolve when Compile Agent processes pending raw.
**Evidence:**
- `[[ai-assisted-development]]` — referenced in ai-frontend-design-guidance.md (Related) + vibe-coding.md (Related)
- `[[distraction-management]]` — referenced in life-planning-20s.md (Related) + src_if-i-had-to-start-over... (Concepts)
- `[[natural-language-programming]]` — referenced in vibe-coding.md (Related)
- `[[no-code-movement]]` — referenced in vibe-coding.md (Related)
- `[[one-person-business]]` — referenced in vibe-coding.md (Related)
**Suggested fix:** Two options: (a) compile concepts when suitable sources arrive, or (b) Fix Agent drops the links. No raw material exists for any of the 5 targets.

---

## Summary

| Severity | Count | Details |
|----------|-------|---------|
| ERROR | 2 | Chinese chars (5 instances, 3 files) + spacing merge (1 instance, 1 file) |
| WARNING | 2 | Missing paren (1 instance) + forward-refs without raw (5 targets) |
| INFO | 0 | — |

**Total:** 4 issues across 5 files (3 concepts with errors, 1 concept with warning, 1 source with warning).

**Typo variants 1-5:** All clean in new files. Dropped-i variant-5 streak: **11 consecutive** (08-23 → 09-20, including all 4 sub-patterns).

**Systemic defect:** Chinese character injection recurs for the 4th time in 9 days (09-12, 09-14, 09-18, 09-20). Recommend Compile Agent prompt review to prevent CJK characters in Vietnamese output.
