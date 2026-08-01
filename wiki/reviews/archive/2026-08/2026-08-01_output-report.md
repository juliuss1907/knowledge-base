# Output Validator Report — 2026-08-01

**Status:** applied
**Applied by:** Fix Agent
**Applied at:** 2026-08-01
**Approved by:** Julius
**Approved date:** 2026-08-01
**Issues found:** 4 issues + 3 systemic patterns
**Created:** 2026-08-01
**Validator:** output-validator
**Files checked:** 665 (161 sources + 504 concepts)
**New files:** 5 (1 source + 4 concepts)

---

## New Files This Run

### Sources (1 new)
- `wiki/sources/src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md`

### Concepts (4 new)
- `wiki/concepts/cuoc-dua-khong-di-lui.md`
- `wiki/concepts/moores-law-economics.md`
- `wiki/concepts/semiconductor-industry-consolidation.md`
- `wiki/concepts/technology-driven-dependence.md`

---

## Issues Found

### 1. WARNING — Double-i typos (NEW instances)

**12 files, 33 instances** — trong đó có **5 instances mới** (từ batch semiconductor). Pattern: `ngườii`, `đờii`, `lờii` (double-i do Compile Agent tokenization).

### 2. WARNING — Người spacing merge (NEW instances)

**12 files, 30 instances** — trong đó có **4 instances mới**. Pattern: `người dùng` bị merge thành `ngườidùng`.

### 3. INFO — Dropped-i typos (no new)

**5 files** vẫn còn `ngưởi` nhưng **không có instance mới** — các file cũ chưa được Fix Agent sửa từ lần approve 07-30.

### 4. WARNING — 1-sentence definitions

**502/504 concepts** (99.6%) có Definition 1 câu. +9 concepts so với 07-30 (493→502). 2 concepts có multi-sentence: `stoic-dichotomy-of-control.md` và `let-them-theory.md`.

### 5. WARNING — Too few key points (<5)

**86 concepts** — không đổi so với 07-30.

### 6. INFO — High draft ratio

**335/504 concepts (66.5%)** ở `draft`. +9 so với 07-30.

---

## Systemic Patterns

### A. Compile Agent vẫn tạo Definition 1 câu

502/504 concepts — tỉ lệ 99.6%. Prompt template chưa được update dù đã flag 2 lần (07-26, 07-30).

### B. Typo patterns tồn đọng

Dropped-i `ngưởi` trong 5 file cũ chưa được Fix Agent sửa từ 07-30 approve. Double-i và spacing-merge tiếp tục có instance mới từ batch mới.

---

## ✅ Passing

- ✅ No truncated concepts
- ✅ No truncated sources
- ✅ All Sources sections populated
- ✅ Language: all Vietnamese
- ✅ No new dropped-i (ngưởi) — lần đầu không có dropped-i mới!

---

## Verdict

**REVISE** — 2 WARNING (double-i new + spacing-merge new) + systemic quality issues.

### Action items:
1. **Fix Agent:** Sửa double-i instances mới (5 instances trong 12 files)
2. **Fix Agent:** Sửa người spacing merge mới (4 instances)
3. **Fix Agent:** Sửa dropped-i `ngưởi` tồn đọng từ 07-30 (5 files)
4. **Compile Agent:** Update prompt: Definition ≥2 câu
