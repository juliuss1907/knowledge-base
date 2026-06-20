# Output Validation — 2026-06-19

**Status:** pending
**Issues found:** 5
**Created:** 2026-06-19 22:00:00
**Validator:** output-validator

**Files checked:** 400 (93 sources + 307 concepts)
**New files:** 8 (1 source + 7 concepts, compiled today)
**Existing files quick-scanned:** 392

---

## Issue 1: 1-sentence definitions across all 7 new concepts (Systemic)

**File:** 7 concepts — see list below
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** All 7 new concepts compiled today have exactly 1-sentence definitions. Spec requires 2-3 sentences. This is the same systemic pattern flagged on 2026-06-18 (for `infrastructure-capex-cycle.md` and others).

**Evidence (representative — all 7 follow same pattern):**

`200-day-sma-risk-line.md`:
> "Đường trung bình động 200 ngày (200-day Simple Moving Average) được sử dụng như "risk line" để xác định khi nào nên tấn công (offense) và khi nào nên phòng thủ (defense)."

`climax-top.md`:
> "Một dạng đỉnh exhaustion được William O'Neil định nghĩa, xảy ra khi cổ phiếu dẫn đầu tăng parabolic sau chu kỳ dài, thường trên volume khổng lồ và price swings rộng."

**Affected files:**
- `wiki/concepts/200-day-sma-risk-line.md`
- `wiki/concepts/character-change-signal.md`
- `wiki/concepts/climax-top.md`
- `wiki/concepts/four-stages-market-cycle.md`
- `wiki/concepts/market-structure-blueprint.md`
- `wiki/concepts/relative-strength-leadership.md`
- `wiki/concepts/volume-confirmation.md`

**Suggested fix:** Expand each definition to 2-3 sentences — add context, scope, or relationship to other concepts. Likely root cause: Compile Agent prompt produces 1-sentence definitions by default. Review `compile-agent/SKILL.md` definition generation template.

---

## Issue 2: Too few key points — four-stages-market-cycle.md

**File:** wiki/concepts/four-stages-market-cycle.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Only 4 bullet points in `## Key ideas` section — minimum is 5, target range is 5-10.

**Evidence:**
```
- **Stage 1 (Accumulation):** Accumulation bắt đầu...
- **Stage 2 (Markup/Uptrend):** Price confirm strength...
- **Stage 3 (Distribution/Topping):** Momentum weaken...
- **Stage 4 (Markdown/Downtrend):** Trend broken...
```

**Suggested fix:** Add at least 1 more key idea — e.g., on transitions between stages, or on how to confirm which stage the market is currently in.

---

## Issue 3: "ngưởi" typo still in 10 existing files (Systemic, unfixed since 06-17)

**File:** 10 files (listed below)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** The Vietnamese typo "ngưởi" (should be "người") was flagged as systemic on 2026-06-17 with 9 affected files. After partial fix, 10 instances remain. None of today's new files are affected.

**Evidence (representative):**
- `wiki/sources/src_after-the-heater-rule-keeps-you-alive.md` — contains "ngưởi"
- `wiki/sources/src_tai-chinh-ca-nhan-9-ban-co-ang-thuc.md` — contains "ngưởi"
- `wiki/concepts/ai-coach-prompting.md` — contains "ngưởi"
- `wiki/concepts/systematic-trading.md` — contains "ngưởi"
- `wiki/concepts/lifestyle-inflation.md` — contains "ngưởi"
- `wiki/concepts/ai-first-business-model.md` — contains "ngưởi"
- `wiki/sources/src_the-cost-of-discretion.md` — contains "ngưởi"
- `wiki/sources/src_how-average-people-will-get-rich-with-ai.md` — contains "ngưởi"
- `wiki/sources/src_cach-nhanh-nhat-nop-ho-so-bao-hiem-that-nghiep.md` — contains "ngưởi"
- `wiki/sources/src_dan-koe-workflow-analysis-markus.md` — contains "ngưởi"

**Suggested fix:** Run `sed -i 's/ngưởi/người/g'` across all 10 files per list above.

---

## Issue 4: All 7 new concepts carry status: draft

**File:** 7 concepts (same files as Issue 1)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** All 7 new concepts are compiled with `status: draft`. This is the same pattern from 2026-06-17 (14 files). Julius explicitly chose not to change draft status in that pass.

**Suggested fix:** After spot-check review, promote to `status: reviewed` by updating frontmatter.

---

## Issue 5: Mixed Vietnamese-English in new files

**File:** All 8 new files (7 concepts + 1 source)
**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** All new files mix Vietnamese and English. Technical terms like "SMA", "accumulation", "distribution", "climax top" are correctly preserved in English within Vietnamese sentences. This is standard practice for technical content and not a quality defect — flagged for awareness.

**Evidence (representative, from `volume-confirmation.md`):**
> "Khối lượng giao dịch (volume) là 'truth teller' - xác nhận những gì giá cả không nói được, cho biết institutions đang tham gia hay thoát ra khỏi thị trường."

**Suggested fix:** None required. Mixed EN/VN with technical terms in English is the expected convention for this KB's domain (finance, trading, technology).

---

## Verified OK

- ✅ No truncated files — all 400 files have required sections (including `infrastructure-capex-cycle.md`, which was flagged 06-18 and is now fixed)
- ✅ No empty `## Sources` sections (0 out of 307 concepts)
- ✅ No empty `## Key ideas` sections (0 out of 307 concepts)
- ✅ No empty `## Key points` sections (0 out of 93 sources)
- ✅ No broken wikilinks in today's 8 new files — all 7 `[[src_how-the-market-warns-you-before-the-crash]]` references valid, all cross-concept links verified
- ✅ Source `src_how-the-market-warns-you-before-the-crash.md` — 4-5 sentence Summary ✓, 10 Key points ✓, Original excerpts present ✓, Concepts referenced section complete ✓
- ✅ No contradictions between concepts and source detected
- ✅ No date/number errors in new files
- ✅ Technical "ngưởi" typo NOT present in any of today's 8 new files
- ✅ Grammar and spelling correct in new files beyond the definition-length pattern
