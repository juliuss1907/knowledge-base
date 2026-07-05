# Output Validation — 2026-07-02

**Status:** approved
**Approved by:** Julius — 2026-07-05
**Issues found:** 4
**Created:** 2026-07-02 23:05:00 +0700
**Validator:** output-validator

---

## Overview

**Files checked:** 497 (121 sources + 376 concepts)
**New files since last output validation (2026-06-30):** 28
- 07-01 batch: 8 sources + 17 concepts
- 07-02 batch: 1 source + 2 concepts

**Quick-scan results (mechanical checks):**
- 🔤 Typo "ngưởi": 0 files
- 🔤 Typo "ngườii/đờii..." (double-i): 0 files, 0 instances
- ✂️ Truncated concepts: 0
- ✂️ Truncated sources: 0
- 📭 Empty Key ideas: 9 (unchanged)
- 🏷️ Draft concepts: 206

---

## Issue 1: Vietnamese spacing — "người" merge

**File:** wiki/concepts/high-agency.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** 7 instances of "người" merging with the following word without a space, plus a run-on sentence in the Definition section.

**Evidence (line 17):**
> khi các kỹ năng kỹ thuật có thể được AI thực hiện tốt hơn con ngườitrong kỹ năng này giúp con ngườitrở thành ngườichỉ đạo AI giải quyết các vấn đề họ quan tâm.

The line contains 3 merged words ("ngườitrong", "ngườitrở thành", "ngườichỉ đạo") and is structured as a run-on sentence. After fixing spacing: the clause boundary between "con người" and "Kỹ năng này" is still missing.

**Other instances:**
- Line 22: `ngườicó agency` → `người có agency`
- Line 25: `ngườilên sao Hỏa` → `người lên sao Hỏa`
- Line 32: `ngườicó agency` → `người có agency`

**Suggested fix:**
```bash
sed -i 's/ngườitrong/người. Trong/g; s/ngườitrở thành/người trở thành/g; s/ngườichỉ đạo/người chỉ đạo/g; s/ngườicó/người có/g; s/ngườilên/người lên/g' wiki/concepts/high-agency.md
```
Then manually restructure the Definition sentence (line 17) to break the run-on into 2 sentences.

---

## Issue 2: Vietnamese quality — Definition run-on

**File:** wiki/concepts/high-agency.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Definition sentence (line 17) is a single 3-clause run-on. After fixing spacing, the sentence still runs: "con người trong kỹ năng này giúp con người trở thành người chỉ đạo AI" — the transition from "con người" to "Kỹ năng này" lacks a sentence boundary.

**Evidence:**
> Đây là kỹ năng được dự đoán sẽ trở nên vô cùng quan trọng trong kỷ nguyên AI, khi các kỹ năng kỹ thuật có thể được AI thực hiện tốt hơn con người. Kỹ năng này giúp con người trở thành người chỉ đạo AI giải quyết các vấn đề họ quan tâm.

**Suggested fix:** Break the Definition into 2 sentences at the natural boundary after "con người."

---

## Issue 3: English/Vietnamese mixing

**File:** wiki/sources/src_money-is-the-easiest-way-to-measure-your-life.md
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** Line 34 uses "trust cao" — a hybrid English-Vietnamese phrase.

**Evidence:**
> sống trong xã hội trust cao với tự do và ổn định

**Suggested fix:** "xã hội có độ tin cậy cao" hoặc "xã hội có mức trust cao"

---

## Issue 4: Forward-reference backlinks

**File:** wiki/concepts/high-agency.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** 4 of 5 backlinks in `## Related concepts` reference concepts that do not exist yet in the wiki.

**Evidence:**
- `[[sovereign-individual]]` — MISSING
- `[[ai-future-skills]]` — MISSING
- `[[self-directed-learning]]` — MISSING
- `[[growth-mindset]]` — MISSING

**Note:** `[[vibe-coding]]` resolves correctly. These are forward-references — not blocking but means the concept references ideas that aren't yet in the KB.

---

## Systemic patterns (carry-over, unchanged)

| Pattern | Count | Delta from 06-30 |
|---|---|---|
| One-sentence definitions | 374 | +15 (from expanded scope) |
| Too few key points (<5) | 79 | 0 |
| Empty Key ideas | 9 | 0 |
| Draft concepts | 206 | +15 (from expanded scope) |

---

## Cluster quality assessment

### 07-02 cluster: five-types-of-wealth (3 files)
- **Source:** `src_money-is-the-easiest-way-to-measure-your-life.md` — URL verified (HTTP 200), 9 key points, good excerpts
- **Concepts:** `erg-theory.md` (5 key ideas), `five-types-of-wealth.md` (7 key ideas)
- Cross-linking: tight — source → both concepts, concepts ↔ each other
- ✅ Clean except 1 INFO (trust cao)

### 07-01 batch: productivity/laws-of-the-world cluster (25 files)
- **8 sources:** URLs verified where present (2 × HTTP 200/103, 6 missing frontmatter URL — format concern, not output)
- **17 concepts:** All structurally complete (Definition ≥2 câu, Key ideas 5-10 ý)
- **Cross-linking:** Strong internal network (laws-of-the-world ↔ costly-signal ↔ output-vs-outcome ↔ right-problem-framework ↔ deliberate-practice ↔ leverage ↔ prices-law)
- **Quality:** High — 1 WARNING (high-agency spacing), otherwise clean
- Concepts like `brain-coupling.md`, `extroversion-as-skill.md` show excellent Vietnamese quality with natural mixing of English terminology

---

## Actions

- Review `wiki/reviews/2026-07-02_output-report.md`
- Nếu approve: giao Fix Agent sửa spacing issues trong `high-agency.md` (7 instances + run-on sentence)
- 1 INFO về "trust cao" trong source — không bắt buộc
- 4 forward-reference backlinks sẽ tự resolve khi concepts được tạo sau
- Systemic patterns unchanged — không cần action
