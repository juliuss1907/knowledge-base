# Output Validation — 2026-07-16

**Status:** pending
**Issues found:** 1
**Created:** 2026-07-16 23:10:53
**Validator:** output-validator

---

## Issue 1: New typo variant — "ngườI" (capital I thay vì lowercase i sau "ờ")

**File:** wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md (4 instances), wiki/concepts/100x-token.md (1 instance)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Biến thể mới của lỗi systematic diacritic từ Compile Agent: ký tự capital I (U+0049) được dùng thay cho lowercase i (U+0069) sau "ờ" trong từ "người". Kết quả là "ngườI" thay vì "người". Đây là dạng thứ ba của cùng root cause — sau double-i ("ngườii") và spacing merge ("ngườitrong"). 5 instances trên 2 trong số 6 file mới hôm nay.

**Evidence:**
- `src_you-just-hired-a-million-bad-employees-a16z.md` (4 instances):
  - Dòng 24: "...\"Con ngườI hiện đã rẻ hơn phần mềm\"..." và "...workforce con ngườI và quản lý AI tokens..."
  - Dòng 28: "...con ngườI rẻ hơn software..."
  - Dòng 30: "...vì ngườI dùng không biết cách sử dụng tokens..."
- `100x-token.md` (1 instance):
  - Dòng 22: "- NgườI nắm giữ 100X tokens có động lực thấp nhất..."

**Suggested fix:**
```bash
sed -i 's/ngườI/người/g' \
  wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md \
  wiki/concepts/100x-token.md
```

**Root cause note:** Đây là biến thể thứ ba của lỗi systematic trong Compile Agent sau double-i ("ngườii", tháng 6) và spacing merge ("ngườitrong", tháng 7). Cả ba đều bắt nguồn từ cách tokenizer hoặc prompt của Compile Agent xử lý không chính xác ký tự sau "ờ". Capital I (U+0049) về mặt visual gần giống lowercase i (U+0069) trong một số font, có thể khiến model chọn sai. Recommend review Compile Agent prompt để sửa root cause thay vì tiếp tục patch từng biến thể.

---

## Summary

| Metric | Count |
|---|---|
| Files checked | 579 (145 sources + 434 concepts) |
| New files today | 6 (1 source + 5 concepts) |
| Issues found | 1 (0 ERROR, 1 WARNING, 0 INFO) |
| Capital-I typos | 5 instances across 2 files |

**New files validated in detail:**
- ✅ `wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md` — đầy đủ sections, 11 key points, summary 5 câu. 4 lỗi "ngườI".
- ✅ `wiki/concepts/100x-token.md` — definition 3 câu, 6 key ideas, đầy đủ sections. 1 lỗi "ngườI".
- ✅ `wiki/concepts/ai-evals.md` — definition 3 câu, 8 key ideas, sạch.
- ✅ `wiki/concepts/ai-transformation.md` — definition 3 câu, 8 key ideas, sạch.
- ✅ `wiki/concepts/token-looping.md` — definition 3 câu, 7 key ideas, sạch.
- ✅ `wiki/concepts/tokenmaxxing.md` — definition 3 câu, 6 key ideas, sạch.

**Quick-scan context (toàn bộ KB):**
- Tổng số file: 145 sources + 434 concepts = 579
- Double-i tồn đọng (từ batch trước): 4 files, 10 instances — không file nào từ hôm nay
- Spacing merge tồn đọng (từ batch trước): 8 files, 19 instances — không file nào từ hôm nay
- "ngườI" capital-I: CHỈ trong 2 file mới hôm nay (5 instances) — chưa tồn tại trong KB cũ
- 1-sentence definitions: 432 concepts (systemic, carry-over)
- Key points <5: 78 concepts (systemic, carry-over)
- Empty Key ideas: 9 concepts (systemic, carry-over)
- Draft concepts: 264

**Assessment:** Batch hôm nay chất lượng tốt. Tất cả 6 file đều có cấu trúc hoàn chỉnh, definition đủ 3 câu, key ideas đủ 5-8 mục. Lỗi duy nhất là biến thể "ngườI" (capital I) — một dạng mới của lỗi systematic đã biết, dễ sửa bằng sed. Không có ERROR, không có file truncated, không có broken wikilinks.
