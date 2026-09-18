# Output Validation — 2026-09-18

**Status:** pending
**Issues found:** 4 (3 ERROR, 1 WARNING, 0 INFO)
**Created:** 2026-09-18 23:02:00
**Validator:** output-validator

---

## Batch summary

- **Files checked:** 594 (204 sources + 586 concepts)
- **New files today:** 8 (3 sources + 5 concepts)
- **Dropped-i variant-5 grep:** 0 matches (all 4 sub-patterns clean)
- **Typo variants 1-4:** 0
- **Defect A/B/C (multi-source):** 1 DEFECT (Issue 2)
- **Truncated files:** 0
- **Empty sections:** 0

---

## Issue 1: Chinese characters `在哪里` in Vietnamese source summary

**File:** wiki/sources/src_50-system-design-concepts-explained-simply.md
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters `在哪里` injected into Vietnamese summary text (line 24). Compile Agent LLM output mixed Chinese into Vietnamese prose.
**Evidence:** `...giải quyết vấn đề gì, và trade-off在哪里. 2026 edition bổ sung...`
**Suggested fix:** Replace `在哪里` with Vietnamese equivalent (e.g. `ở đâu` or rewrite phrase). Same defect pattern as 09-12 `既是` and 09-14 `注意力`.

---

## Issue 2: Chinese characters `几乎` in Vietnamese source summary

**File:** wiki/sources/src_how-ai-labs-eventually-make-money.md
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters `几乎` injected into Vietnamese summary text (line 24). Same Compile Agent defect as Issue 1.
**Evidence:** `...giá trị tạo ra cho users nhưng builder几乎 không capture được.`
**Suggested fix:** Replace `几乎` with Vietnamese equivalent (e.g. `gần như`).

---

## Issue 3: Chinese characters `面临` in Vietnamese concept definition

**File:** wiki/concepts/ai-lab-business-model.md
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters `面临` injected into Vietnamese definition (line 16). Same Compile Agent defect as Issues 1-2. Third occurrence of Chinese contamination in this batch.
**Evidence:** `...các AI foundation model companies面临cấu trúc kinh tế đặc biệt...`
**Suggested fix:** Replace `面临` with Vietnamese equivalent (e.g. `đối mặt với` or `có`).

---

## Issue 4: Self-referencing wikilink in Related concepts

**File:** wiki/concepts/rag-retrieval-augmented-generation.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** `[[rag-retrieval-augmented-generation]]` in Related concepts (line 35) is a self-reference — the concept links to itself. Likely Compile Agent error when aggregating related concepts.
**Evidence:** `- [[rag-retrieval-augmented-generation]]` (line 35 in `## Related concepts`)
**Suggested fix:** Remove self-reference line.

---

## Summary

| Severity | Count | Details |
|---|---|---|
| ERROR | 3 | Chinese character contamination (3 files, same defect pattern as 09-12/09-14) |
| WARNING | 1 | Self-referencing wikilink in rag-retrieval-augmented-generation.md |
| INFO | 0 | — |

**Systemic pattern:** Chinese character injection is now the 3rd batch-level recurrence of this Compile Agent defect (09-12: `既是` ×2, 09-14: `注意力` ×4, 09-18: `在哪里`+`几乎`+`面临` ×3). Recommend reviewing Compile Agent prompt for Chinese token contamination.

**Dropped-i streak:** 16 consecutive clean runs (08-23 → 09-18). Demotion to weekly recommended (threshold reached 08-30; 3 prior recommendations unconfirmed).
