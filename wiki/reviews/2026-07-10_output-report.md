# Output Validator Report — 2026-07-10

**Status:** approved
**Approved by:** Julius
**Issues found:** 3
**Created:** 2026-07-10 22:00:00
**Validator:** output-validator (Hermes-VPS)

---

## Quick-scan results

| Metric | Value |
|---|---|
| New files today | 8 (2 sources + 6 concepts) |
| Typo "ngưởi" | 0 files (new: 0) |
| Typo double-i | 0 files, 0 instances (new: 0) |
| Typo "người" spacing merge | 4 files, 11 instances (new: 0 — carry-over) |
| 1-sentence definitions | 413 concepts (carry-over) |
| Too few key points (<5) | 78 concepts (carry-over) |
| Empty Key ideas | 9 concepts (carry-over) |
| Truncated concepts | 0 |
| Truncated sources | 0 |
| Total sources | 137 |
| Total concepts | 415 |
| Draft concepts | 245 |

---

## New file deep validation: 1 ERROR + 2 WARNING

### 8 files validated — detailed results

| # | File | Definition | Key Ideas | Wikilinks | Verdict |
|---|---|---|---|---|---|
| 1 | src_living-beyond-the-labels.md | N/A (source) | 11 items | 3/3 resolve | **PASS** |
| 2 | src_you-escape-competition... | N/A (source) | 9 items | 3/3 resolve | **PASS** |
| 3 | authenticity-creative-expression.md | 2 câu | 6 items | 6/6 resolve | **PASS** |
| 4 | identity-threat-neuroscience.md | 2 câu | 7 items | 6/6 resolve | **PASS** |
| 5 | internal-foundation-identity.md | 2 câu | 6 items | 6/6 resolve | **PASS** |
| 6 | label-cognitive-shortcut.md | 2 câu | 7 items | 5/6 resolve | **1 ERROR** |
| 7 | self-knowledge-practice.md | 1 câu | 6 items | 6/6 resolve | **1 WARNING** |
| 8 | social-media-comparison-trap.md | 1 câu | 6 items | 6/6 resolve | **1 WARNING** |

---

## Issue 1: Broken wikilink — forward-reference

**File:** wiki/concepts/label-cognitive-shortcut.md
**Severity:** ERROR
**Dimension:** Factual
**Issue:** `[[confirmation-bias]]` trong `## Related concepts` không resolve — concept chưa được compile
**Evidence:** Line 30: `- [[confirmation-bias]]` — không tồn tại `wiki/concepts/confirmation-bias.md` hoặc `wiki/sources/src_confirmation-bias.md`
**Suggested fix:** Đây là forward-reference. Block concept này khỏi được reference bởi file khác cho đến khi `confirmation-bias` được compile, hoặc thay thế bằng concept đã tồn tại nếu có concept tương tự.

---

## Issue 2: Definition 1 câu — cần 2-3 câu

**File:** wiki/concepts/self-knowledge-practice.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition section chỉ có 1 câu. Concept definitions cần 2-3 câu để đảm bảo đầy đủ.
**Evidence:** Line 16: toàn bộ definition là 1 câu dài — `Self-knowledge practice là tập hợp các thực hành có chủ đích...`
**Suggested fix:** Tách thành 2 câu: (1) định nghĩa self-knowledge practice là gì, (2) mục đích của nó — phát triển authentic creative expression thông qua hiểu biết bản thân.

---

## Issue 3: Definition 1 câu — cần 2-3 câu

**File:** wiki/concepts/social-media-comparison-trap.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition section chỉ có 1 câu. Concept definitions cần 2-3 câu để đảm bảo đầy đủ.
**Evidence:** Line 16: toàn bộ definition là 1 câu dài — `Social media comparison trap là hiện tượng scrolling mạng xã hội...`
**Suggested fix:** Tách thành 2 câu: (1) định nghĩa hiện tượng comparison trap, (2) hệ quả — nó kéo con người ra khỏi bản thân và cản trở phát triển sự độc đáo.

---

## Systemic patterns (INFO — carry-over, không phải issues mới)

### Người spacing merge (carry-over)
4 files, 11 instances — tất cả trong file cũ, không có instance mới hôm nay. Các file bị ảnh hưởng chưa được Fix Agent xử lý từ các lần validation trước.

### <5 key ideas (carry-over)
78 concepts có <5 key ideas — toàn bộ là file cũ, không có file mới nào trong batch này.

### 1-sentence definitions (carry-over)
413 concepts có definition 1 câu — systemic issue từ lâu, 2 file mới hôm nay (`self-knowledge-practice.md`, `social-media-comparison-trap.md`) được flag riêng ở trên.

---

## Summary

| Severity | Count | Details |
|---|---|---|
| ERROR | 1 | Broken wikilink `[[confirmation-bias]]` trong `label-cognitive-shortcut.md` |
| WARNING | 2 | Definition 1 câu: `self-knowledge-practice.md`, `social-media-comparison-trap.md` |
| INFO | 0 | — |

**Batch chất lượng cao.** 5/8 files pass hoàn toàn (2 sources + 3 concepts). Các concept có nội dung sâu, faithful với source material, coherence tốt. Vietnamese tự nhiên, không có lỗi chính tả. 2 WARNINGs là issue nhẹ về formatting (tách definition thành 2 câu). 1 ERROR là forward-reference sẽ tự resolve khi `confirmation-bias` được compile.

**Actions cần Julius:**
- Fix `label-cognitive-shortcut.md`: compile `confirmation-bias` concept hoặc thay thế wikilink
- Fix `self-knowledge-practice.md`: tách definition thành 2 câu
- Fix `social-media-comparison-trap.md`: tách definition thành 2 câu
