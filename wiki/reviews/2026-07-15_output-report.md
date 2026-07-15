# Output Validation — 2026-07-15

**Status:** pending
**Issues found:** 4
**Created:** 2026-07-15 23:10:33
**Validator:** output-validator

---

## Issue 1: Systemic double-i typo (ngườii/lờii/thờii/tớii) — tất cả 4 file mới

**File:** wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md, wiki/concepts/math-mafia.md, wiki/concepts/olympiad-to-founder-pipeline.md, wiki/concepts/quant-finance-culture.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** 11 instances của lỗi double-i (ngườii→người, lờii→lời, thờii→thời, tớii→tới) trên cả 4 file được compile hôm nay. Đây là lỗi hệ thống từ Compile Agent đã được ghi nhận từ 2026-06-23 — prompt của Compile Agent vẫn sinh ra lỗi này sau khi "ngưởi" được sửa.

**Evidence:**
- `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` (7 instances): "ngườii" (dòng 24, 28, 30, 35×2), "lờii" (dòng 24), "thờii" (dòng 29), "tớii" (dòng 35)
- `math-mafia.md` (2 instances): "ngườii" (dòng 20, 22)
- `olympiad-to-founder-pipeline.md` (1 instance): "ngườii" (dòng 23)
- `quant-finance-culture.md` (1 instance): "ngườii" (dòng 21)

**Suggested fix:** Chạy sed trên cả 4 file:
```bash
sed -i 's/ngườii/người/g; s/lờii/lời/g; s/thờii/thời/g; s/tớii/tới/g' \
  wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md \
  wiki/concepts/math-mafia.md \
  wiki/concepts/olympiad-to-founder-pipeline.md \
  wiki/concepts/quant-finance-culture.md
```

---

## Issue 2: Hook-above typo "đồng thởi" → "đồng thời"

**File:** wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** "đồng thởi" (dòng 24, xuất hiện 2 lần) — đây là biến thể của lỗi hook-above, cùng root cause với "ngưởi". Ký tự "ở" (hook-above) thay vì "ờ" (grave).

**Evidence:** Dòng 24: "...Tác giả Jesse Zhang đồng thởi là thành viên..." và "...đồng thởi lưu ý rằng..."

**Suggested fix:**
```bash
sed -i 's/đồng thởi/đồng thời/g' wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md
```

---

## Issue 3: Broken forward-reference wikilinks — 3 concepts chưa được compile

**File:** wiki/concepts/math-mafia.md, wiki/concepts/olympiad-to-founder-pipeline.md, wiki/concepts/quant-finance-culture.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 3 wikilink trỏ đến concepts chưa tồn tại (forward-references). Đây là pattern quen thuộc khi Compile Agent reference concepts chưa được compile.

**Evidence:**
- `math-mafia.md` dòng 29: `[[paypal-mafia]]` → file không tồn tại
- `olympiad-to-founder-pipeline.md` dòng 30: `[[competitive-programming]]` → file không tồn tại
- `quant-finance-culture.md` dòng 30: `[[high-frequency-trading]]` → file không tồn tại

**Suggested fix:** Các link này sẽ tự resolve khi concepts tương ứng được compile trong tương lai. Nếu không có kế hoạch compile, cân nhắc remove link.

---

## Issue 4: math-mafia.md chỉ có 4 key ideas

**File:** wiki/concepts/math-mafia.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Section Key ideas chỉ có 4 mục, thấp hơn ngưỡng khuyến nghị 5-10. Nội dung hiện có chất lượng tốt nhưng thiếu chiều sâu so với các concept cùng batch.

**Evidence:** Dòng 19-23 chỉ liệt kê 4 bullet points, trong khi olympiad-to-founder-pipeline.md có 5 và quant-finance-culture.md có 5.

**Suggested fix:** Cân nhắc bổ sung thêm 1-2 key ideas, ví dụ: so sánh với các "mafia" khác (Paypal Mafia, Tesla Mafia), hoặc phân tích yếu tố tuyển chọn (selection bias vs causation).

---

## Summary

| Metric | Count |
|---|---|
| Files checked | 4 (1 source + 3 concepts) |
| New files today | 4 |
| Issues found | 4 (0 ERROR, 3 WARNING, 1 INFO) |
| Double-i typos | 11 instances across 4 files |
| Hook-above typos | 2 instances in 1 file |
| Broken wikilinks | 3 forward-references |

**Quick-scan context (toàn bộ KB):**
- Tổng số file: 144 sources + 430 concepts
- Double-i tồn đọng: 4 files, 10 instances (tất cả đều từ batch hôm nay)
- Spacing merge tồn đọng: 8 files, 19 instances (4 từ hôm nay — overlap với double-i)
- 1-sentence definitions: 428 concepts
- Key points <5: 79 concepts
- Empty Key ideas: 9 concepts
- Draft concepts: 260
