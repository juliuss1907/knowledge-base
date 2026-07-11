# Output Validator Report — 2026-07-09

**Status: applied
**Approved by:** Julius
**Issues found:** 1
**Created:** 2026-07-09 22:00:00
**Validator:** output-validator (Hermes-VPS)

---

## Quick-scan results

| Metric | Value |
|---|---|
| New files today | 11 (3 sources + 8 concepts) |
| Typo "ngưởi" | 0 files (new: 0) |
| Typo double-i | 0 files, 0 instances (new: 0) |
| Typo "người" spacing merge | 4 files, 11 instances (new: 0 — carry-over) |
| 1-sentence definitions | 407 concepts (existing, carry-over) |
| Too few key points (<5) | 78 concepts (existing, carry-over) |
| Empty Key ideas | 9 concepts (existing, carry-over) |
| Truncated concepts | 0 |
| Truncated sources | 0 |
| Total sources | 135 |
| Total concepts | 409 |
| Draft concepts | 239 |

## New file deep validation: 1 WARNING

### 11 files validated — detailed results

| # | File | Definition | Key ideas | Backlinks | Vietnamese | Verdict |
|---|---|---|---|---|---|---|
| 1 | src_our-first-heartbreaks... | N/A (source) | 9 items | 2 refs, all resolve | Clean | ALL CLEAN |
| 2 | src_thiet-ke-quy-tac-bao-ve... | N/A (source) | 8 items | 3 refs, all resolve | Clean | ALL CLEAN |
| 3 | src_why-people-fail-at-learning... | N/A (source) | 9 items | 3 refs, all resolve | Clean | ALL CLEAN |
| 4 | boredom-as-dopamine-reset | 2 câu | 6 items | 4 refs, all resolve | Clean | ALL CLEAN |
| 5 | childhood-abandonment-patterns | 2 câu | 7 items | 2 refs, all resolve | Clean | ALL CLEAN |
| 6 | comprehensible-input | 2 câu | 8 items | 3 refs, all resolve | Clean | ALL CLEAN |
| 7 | decoding-messages-language | 2 câu | 7 items | 4 refs, all resolve | Clean | ALL CLEAN |
| 8 | dopamine-wanting-vs-liking | 2 câu | 7 items | 6 refs, all resolve | Clean | ALL CLEAN |
| 9 | emotional-inheritance | 2 câu | 5 items | 2 refs, all resolve | Clean | ALL CLEAN |
| 10 | environment-design-for-habits | 1 câu ⚠️ | 8 items | 5 refs, all resolve | Clean | WARNING |
| 11 | mental-representation-language | 2 câu | 5 items | 4 refs, all resolve | Clean | ALL CLEAN |

---

## Issue 1: environment-design-for-habits — Definition quá ngắn

**File:** wiki/concepts/environment-design-for-habits.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition chỉ có 1 câu (yêu cầu 2-3 câu trong format spec). Các concept khác trong batch hôm nay đều có 2 câu đầy đủ. File này được update hôm nay (thêm source `src_thiet-ke-quy-tac-bao-ve-su-chu-y`) nhưng definition không được mở rộng để phản ánh nội dung mới.

**Evidence:**
> "Chiến lược thay đổi bối cảnh xung quanh (vật lý, số và xã hội) để làm cho những thói quen tốt trở nên dễ dàng hơn và những thói quen xấu trở nên khó khăn hơn, thay vì dựa dẫm vào ý chí cá nhân."

**Suggested fix:** Mở rộng definition lên 2-3 câu, bổ sung thêm khía cạnh attention protection (từ source mới `src_thiet-ke-quy-tac-bao-ve-su-chu-y`) — cụ thể là vai trò của environment design trong việc chống lại dopamine hijacking của social media, không chỉ dừng ở thói quen chung.

---

## Systemic patterns (INFO — carry-over, không phải issues mới)

Các vấn đề dưới đây tồn tại trong các file cũ, không phải từ batch hôm nay. Được ghi nhận để tracking, không cần action từ Fix Agent.

- **"người" spacing merge:** 4 files, 11 instances — toàn bộ trong file cũ, 0 instance mới hôm nay. Pattern này đã được Fix Agent xử lý trong các batch trước, các instances còn lại là carry-over từ các file chưa được sửa.
- **78 concepts có <5 key ideas:** File cũ, cần review dần qua các đợt Fix Agent.
- **9 concepts có Key ideas trống:** Cần được compile lại hoặc xóa.
- **407 concepts có definition 1 câu:** Đây là technical debt toàn hệ thống, cần chiến dịch mở rộng definition qua thời gian.
