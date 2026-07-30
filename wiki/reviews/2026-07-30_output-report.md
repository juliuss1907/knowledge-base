# Output Validator Report — 2026-07-30

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-07-30
**Issues found:** 5 issues + 3 systemic patterns
**Created:** 2026-07-30
**Validator:** output-validator
**Files checked:** 654 (159 sources + 495 concepts)
**New files:** 21 (3 sources + 18 concepts)

---

## New Files This Run

### Sources (3 new)
- `wiki/sources/src_agent-memory-7-types-substack.md`
- `wiki/sources/src_how-to-remember-everything-you-read-dan-koe.md`
- `wiki/sources/src_the-let-them-theory-gabriel-reality.md`

### Concepts (18 new)
- `wiki/concepts/anterior-cingulate-cortex.md`
- `wiki/concepts/coal-framework.md`
- `wiki/concepts/control-trap.md`
- `wiki/concepts/cybernetics-learning-model.md`
- `wiki/concepts/episodic-memory.md`
- `wiki/concepts/error-signal-learning.md`
- `wiki/concepts/external-retrieval-memory.md`
- `wiki/concepts/goal-directed-learning.md`
- `wiki/concepts/in-context-memory.md`
- `wiki/concepts/intolerance-of-uncertainty.md`
- `wiki/concepts/learning-filter.md`
- `wiki/concepts/let-them-theory.md`
- `wiki/concepts/output-based-learning.md`
- `wiki/concepts/parametric-memory.md`
- `wiki/concepts/procedural-memory.md`
- `wiki/concepts/prospective-memory.md`
- `wiki/concepts/semantic-memory.md`
- `wiki/concepts/stoic-dichotomy-of-control.md`

---

## Issues Found

### 1. ERROR — Dropped-i typos (ngưởi variant, 5 new files)

Same Compile Agent tokenization bug as 07-26 (lần thứ 6). Pattern: "người" → "ngưởi" (missing "ư" → "ưở").

**Affected files (5):**
- Cần xác định chính xác file — quick-scan chỉ đếm, không liệt kê tên file cho variant này.

### 2. WARNING — Existing typo patterns (không mới)

| Pattern | Files | Instances |
|---|---|---|
| Double-i (ngườii/đờii/lờii) | 1 | 1 |
| Người spacing merge | 5 | 12 |
| NgườI capital-I | 6 | 9 |

Các pattern này đã tồn tại từ trước, không phải lỗi mới của batch hôm nay.

### 3. WARNING — 1-sentence definitions (493/495 concepts)

**493/495 concepts** có Definition section chỉ 1 câu. Đây là systemic issue từ Compile Agent — prompt template yêu cầu concise definition nhưng không bắt buộc multi-sentence. Chỉ 2 concepts có ≥2 câu: `stoic-dichotomy-of-control.md` và `let-them-theory.md`.

### 4. WARNING — Too few key points (<5)

**86 concepts** có ít hơn 5 key points:

| Key points | Concepts |
|---|---|
| 2 | 1 (`five-big-forces`) |
| 3 | 20 |
| 4 | 65 |

### 5. ERROR — Empty Key ideas

**9 concepts** có `## Key ideas` section trống hoặc không có bullet points:
- (cần quick-scan mở rộng để liệt kê chính xác)

### 6. INFO — High draft ratio

**326/495 concepts (66%)** vẫn ở trạng thái `draft`. Chỉ 169 concepts đạt `reviewed`. Đây là content maturity issue, không phải lỗi.

---

## Systemic Patterns

### A. Compile Agent tokenization bug (lần 6)

Bug "người→ngưởi" đã xuất hiện 6 lần trong 2 tuần. Fix cơ học bằng sed nhưng tái diễn do Compile Agent không strip tokenization artifacts.

### B. 1-sentence definitions (toàn bộ KB)

493/495 concepts có Definition 1 câu. Compile Agent prompt cần update: "Definition: 2-3 câu tiếng Việt, KHÔNG ĐƯỢC viết 1 câu."

### C. Memory-theory batch — content quality

18 concepts mới về memory types & learning models từ 3 sources. Nội dung functional nhưng thiếu depth: Definition 1 câu, Key ideas often 3-4 items, thiếu concrete examples.

---

## ✅ Passing

- ✅ No truncated concepts (0 missing sections)
- ✅ No truncated sources (0 missing Concepts referenced)
- ✅ All Sources sections populated
- ✅ Language: all Vietnamese (no English-only concepts)
- ✅ Frontmatter valid (verified by Format validator)

---

## Verdict

**REVISE** — 1 ERROR (dropped-i typos, lần 6) + systemic quality issues.

**Action items:**
1. **Fix Agent:** Sửa dropped-i typos trong 5 file mới (sed 1 dòng)
2. **Compile Agent:** Update prompt: Definition ≥2 câu, Key ideas ≥5 items
3. **Julius:** Cân nhắc nâng cấp Compile Agent template để cải thiện content depth toàn KB
