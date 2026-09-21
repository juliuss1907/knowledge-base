# Output Validation — 2026-09-21

**Status:** pending
**Issues found:** 5 (3 ERROR, 2 WARNING, 0 INFO)
**Created:** 2026-09-21 23:01:11 +0700
**Validator:** output-validator
**Files checked:** 10 (2 sources + 8 concepts)
**New files:** 10 (compiled 2026-09-21)
**Previous run:** 2026-09-20 (4 issues: 2E+2W+0I, pending)

---

## Issue 1: [SYSTEMATIC] Chinese characters in Vietnamese text — 4th recurrence (9 days)

**File:** `wiki/concepts/low-entry-principle.md`
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters `让它阻止` injected into Vietnamese sentence. Line 21: `"Bad hair day" không phải lý do bỏ cuộc — bạn không mention thì không ai biết, vậy tại sao让它阻止 bạn?`
**Evidence:** `vậy tại sao让它阻止 bạn?` — mixed Chinese (让它阻止 = "let it stop you") in Vietnamese body
**Suggested fix:** Replace with Vietnamese: `"vậy tại sao lại để nó ngăn cản bạn?"`

---

## Issue 2: [SYSTEMATIC] Chinese characters in Vietnamese text — 4th recurrence (9 days)

**File:** `wiki/concepts/amygdala-vs-prefrontal-cortex.md`
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters `沙发` (sofa) injected into Vietnamese sentence. Line 24: `Đây là lý do gym analogy works: cơ thể nói "no" khi nằm trên沙发, nhưng 20 phút vào workout thì lại yêu thích — amygdala đã sai`
**Evidence:** `nằm trên沙发` — Chinese word for "sofa" in Vietnamese body
**Suggested fix:** Replace with Vietnamese: `"nằm trên ghế sô pha"` or `"nằm ủ rũ"`

---

## Issue 3: [SYSTEMATIC] Chinese characters in Vietnamese text — 4th recurrence (9 days)

**File:** `wiki/concepts/consumption-vs-action.md`
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters `一年` (one year) injected into Vietnamese sentence. Line 25: `-一年 2019-2020: tiêu thụ content YouTube thay vì tạo content — cảm giác gần goal hơn nhưng thực tế đang comfortable hơn với việc không làm`
**Evidence:** `-一年 2019-2020` — Chinese "one year" prefix before date range
**Suggested fix:** Remove Chinese characters: `"Giai đoạn 2019-2020: tiêu thụ content YouTube..."` or `"Trong năm 2019-2020:..."`

---

## Issue 4: Tokenization merge — words concatenated without space

**File:** `wiki/concepts/curiosity-hijacking.md`
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Definition line 16 has two words merged: `thông tininterest` — Vietnamese and English concatenated without space
**Evidence:** `não vẫn đang "săn" thông tininterest như designed` — should be separated or rewritten
**Suggested fix:** Separate: `"săn thông tin interest"` or rewrite as `"săn thông tin mà não quan tâm"`

---

## Issue 5: Missing closing parenthesis

**File:** `wiki/concepts/curiosity-hijacking.md`
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Line 26: `"Dopamine overload thường bị nhầm với personality flaw: "lazy, unmotivated, can't focus, not curious" — fixed mindset gây hại vì nghĩ mình unchangeable"` — the quoted phrase has no closing punctuation/parenthesis before the em dash
**Evidence:** `not curious" — fixed mindset` — missing `)` or period after the closing quote
**Suggested fix:** Add closing punctuation: `...not curious" — fixed mindset gây hại vì nghĩ mình không thể thay đổi`

---

## Summary

| Severity | Count | Files affected |
|---|---|---|
| ERROR | 3 | 3 (low-entry-principle, amygdala-vs-prefrontal-cortex, consumption-vs-action) |
| WARNING | 2 | 1 (curiosity-hijacking ×2) |
| INFO | 0 | 0 |
| **Total** | **5** | **4** |

**Pattern:** Chinese character injection continues as SYSTEMATIC issue — 3 ERRORs across 3 files in this batch, same root cause as 09-20 (5 instances in 3 files). This is the 5th+ recurrence since 09-12. Compile Agent prompt has unresolved CJK injection defect. Recommend prompt review.

**Batch quality:** 6/10 files clean (no issues). 4/10 have issues, all from same root cause (CJK injection ×3, tokenization merge ×1).

**Dropped-i streak:** 12 consecutive days (08-23 → 09-21). All 3 sub-patterns = 0 matches.

**Backlinks:** All `## Sources` sections match frontmatter `sources:` count. All `## Related concepts` targets exist. No truncated files. All concept definitions ≥2 sentences. All key ideas ≥5 items (84 legacy concepts with <5 are pre-existing depth-debt, not from this batch).
