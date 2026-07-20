# Output Validation — 2026-07-18

**Status:** approved
**Issues found:** 3
**Created:** 2026-07-18 23:09:43
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** output-validator

---

## Issue 1: Truncated concept — `psychic-energy.md` thiếu `## Sources` và `## Notes`

**File:** wiki/concepts/psychic-energy.md
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File bị cắt ngang giữa chừng tại dòng 47 — kết thúc bằng `- [[flow-state]] — yêu cầu psychic` (chưa hoàn chỉnh). Thiếu phần còn lại của `## Related concepts` và toàn bộ `## Sources` section. Quick-scan xác nhận: `psychic-energy.md(rel=1 src=00)` — 1 related concept, 0 sources.

**Evidence:**
```
47|- [[flow-state]] — yêu cầu psychic
```
File kết thúc tại đây. Không có `## Sources` section, không có `## Notes`.

**Suggested fix:** Re-compile `psychic-energy.md` từ source `src_happiness-is-a-skill-hussain-ibarra.md`. Concept này cần ít nhất: hoàn thiện Related concepts (flow-state, psychic-entropy, hedonic-adaptation), thêm Sources section, thêm Notes. Chặn file này khỏi việc được reference cho đến khi fix.

---

## Issue 2: Broken wikilink — `[[crypto-ai-stacking]]` không tồn tại

**File:** wiki/sources/src_is-there-anything-left-to-build-in-crypto-wintermute.md
**Severity:** WARNING
**Dimension:** Factual accuracy
**Issue:** File reference `[[crypto-ai-stacking]]` trong `## Concepts referenced` nhưng `wiki/concepts/crypto-ai-stacking.md` không tồn tại và không có fallback tại `wiki/sources/src_crypto-ai-stacking.md`.

**Evidence:**
```
48|## Concepts referenced
49|
50|- [[machine-economy]]
51|- [[agentic-commerce]]
52|- [[autonomous-agents]]
53|- [[crypto-ai-stacking]]
```

**Suggested fix:** Một trong hai hướng:
1. Compile concept `crypto-ai-stacking.md` từ source gốc (nếu có trong raw/)
2. Hoặc xóa dòng reference `[[crypto-ai-stacking]]` khỏi file source nếu concept này không có kế hoạch compile

---

## Issue 3–5: Systemic — Capital-I typo mở rộng (237+ instances trên 14 file)

**Files:** Toàn bộ 14 file mới từ 2026-07-17
**Severity:** WARNING
**Dimension:** Vietnamese

### Issue 3: Capital-I thay thế lowercase-i sau nguyên âm tiếng Việt

**Pattern gốc (từ 07-16):** Chỉ ghi nhận "ngườI" → "người". **Batch này mở rộng đáng kể** — lỗi ảnh hưởng đến MỌI từ tiếng Việt kết thúc bằng lowercase-i sau một nguyên âm. Các pattern phát hiện mới:

| Pattern | Fix | Ví dụ |
|---|---|---|
| BàI | Bài | "BàI viết" |
| mớI | mới | "mớI đây" |
| hỏI | hỏi | "câu hỏI" |
| giớI | giới | "thế giớI" |
| lờI | lời | "câu trả lờI" |
| nơI | nơi | "nơI chốn" |
| tàI | tài | "tàI chính" |
| VớI | Với | "VớI sự phát triển" |
| tạI | tại | "hiện tạI" |
| phảI | phải | "không phảI" |
| đuổI | đuổi | "theo đuổI" |
| MốI | Mối | "MốI quan hệ" |
| hộI | hội | "xã hộI" |
| ngoạI | ngoại | "bên ngoạI" |
| thờI | thời | "thờI gian" |
| GiảI | Giải | "GiảI pháp" |
| đổI | đổi | "thay đổI" |
| mọI | mọi | "mọI người" |
| lạI | lại | "trở lạI" |
| cuốI | cuối | "cuốI cùng" |
| đI | đi | "đI bộ" |

**Phân bố theo file (instances):**

| File | Count |
|---|---|
| `hedonic-adaptation.md` | 27 |
| `psychic-entropy.md` | 24 |
| `destination-vs-vehicle.md` | 23 |
| `src_the-5-laws-of-people-who-never-chase-gabriel-reality.md` | 21 |
| `flow-state.md` | 20 |
| `social-attraction.md` | 19 |
| `dopamine-prediction-gap.md` | 19 |
| `psychic-energy.md` | 18 |
| `outcome-independence.md` | 16 |
| `machine-economy.md` | 15 |
| `autonomous-agents.md` | 12 |
| `src_is-there-anything-left-to-build-in-crypto-wintermute.md` | 11 |
| `agentic-commerce.md` | 7 |
| `src_happiness-is-a-skill-hussain-ibarra.md` | 5 |
| **TOTAL** | **237** |

**Evidence (mẫu từ `src_the-5-laws-of-people-who-never-chase-gabriel-reality.md`, 21 instances):**
- Dòng 24: "BàI viết... ngườI thu hút... theo đuổI... MốI quan hệ... vớI họ... lõI... phảI"
- Dòng 28: "tạI và tương laI... phảI reward"
- Dòng 30: "NgườI thu hút có life vớI actual substance"

**Suggested fix:** Sử dụng sed script mở rộng cho toàn bộ 14 file:
```bash
# Fix tất cả capital-I instances (U+0049 → U+0069) trong các file bị ảnh hưởng
for f in \
  wiki/sources/src_happiness-is-a-skill-hussain-ibarra.md \
  wiki/sources/src_is-there-anything-left-to-build-in-crypto-wintermute.md \
  wiki/sources/src_the-5-laws-of-people-who-never-chase-gabriel-reality.md \
  wiki/concepts/social-attraction.md \
  wiki/concepts/destination-vs-vehicle.md \
  wiki/concepts/dopamine-prediction-gap.md \
  wiki/concepts/psychic-energy.md \
  wiki/concepts/psychic-entropy.md \
  wiki/concepts/flow-state.md \
  wiki/concepts/hedonic-adaptation.md \
  wiki/concepts/machine-economy.md \
  wiki/concepts/agentic-commerce.md \
  wiki/concepts/autonomous-agents.md \
  wiki/concepts/outcome-independence.md; do
  sed -i 's/àI/ài/g; s/áI/ái/g; s/ảI/ải/g; s/ãI/ãi/g; s/ạI/ại/g; s/èI/èi/g; s/éI/éi/g; s/ẻI/ẻi/g; s/ẽI/ẽi/g; s/ẹI/ẹi/g; s/ềI/ềi/g; s/ếI/ếi/g; s/ểI/ểi/g; s/ễI/ễi/g; s/ệI/ệi/g; s/ìI/ìi/g; s/íI/íi/g; s/ỉI/ỉi/g; s/ĩI/ĩi/g; s/ịI/ịi/g; s/òI/òi/g; s/óI/ói/g; s/ỏI/ỏi/g; s/õI/õi/g; s/ọI/ọi/g; s/ồI/ồi/g; s/ốI/ối/g; s/ổI/ổi/g; s/ỗI/ỗi/g; s/ộI/ội/g; s/ờI/ời/g; s/ớI/ới/g; s/ởI/ởi/g; s/ỡI/ỡi/g; s/ợI/ợi/g; s/ùI/ùi/g; s/úI/úi/g; s/ủI/ủi/g; s/ũI/ũi/g; s/ụI/ụi/g; s/ừI/ừi/g; s/ứI/ứi/g; s/ửI/ửi/g; s/ữI/ữi/g; s/ựI/ựi/g; s/ỳI/ỳi/g; s/ýI/ýi/g; s/ỷI/ỷi/g; s/ỹI/ỹi/g; s/đI/đi/g' "$f"
done
```

**Root cause escalation:** Production lesson từ 07-16 ghi nhận "ngườI" là biến thể thứ ba. Batch này chứng minh lỗi rộng hơn nhiều — KHÔNG chỉ giới hạn ở "ngườI" mà là toàn bộ Vietnamese lowercase-i sau nguyên âm. Compile Agent đang dùng capital I (U+0049) thay vì lowercase i (U+0069) ở vị trí sau tất cả các nguyên âm có dấu tiếng Việt. Recommend review khẩn cấp Compile Agent prompt — nếu không sửa root cause, mỗi batch mới sẽ tiếp tục tạo ra hàng trăm instances cần fix thủ công.

---

## Summary

| Metric | Count |
|---|---|
| Files checked | 592 (148 sources + 444 concepts) |
| New files since last run | 14 (3 sources + 11 concepts, all from 2026-07-17) |
| Issues found | 5 (1 ERROR, 4 WARNING, 0 INFO) |
| Capital-I instances | 237+ across all 14 new files |

**New files validated in detail — 2026-07-17 batch:**

Sources:
- ✅ `src_happiness-is-a-skill-hussain-ibarra.md` — cấu trúc tốt, 10 key points, 6 quotes. 5 capital-I instances.
- ✅ `src_is-there-anything-left-to-build-in-crypto-wintermute.md` — cấu trúc tốt, 11 key points, 7 quotes. 11 capital-I instances + 1 broken wikilink `[[crypto-ai-stacking]]`.
- ✅ `src_the-5-laws-of-people-who-never-chase-gabriel-reality.md` — cấu trúc tốt, 7 key points, 9 quotes. 21 capital-I instances.

Concepts:
- ✅ `social-attraction.md` — definition 3 câu, sections đầy đủ. 19 capital-I instances.
- ✅ `destination-vs-vehicle.md` — definition 3 câu, sections đầy đủ. 23 capital-I instances.
- ✅ `dopamine-prediction-gap.md` — definition 2 câu, 3 key ideas (dưới minimum 5). 19 capital-I instances.
- ❌ `psychic-energy.md` — **ERROR: truncated**. Thiếu Sources section. 18 capital-I instances.
- ✅ `psychic-entropy.md` — definition 3 câu, 4 key ideas. 24 capital-I instances.
- ✅ `flow-state.md` — definition 4 câu, 5 key ideas. 20 capital-I instances.
- ✅ `hedonic-adaptation.md` — definition 3 câu, 4 key ideas. 27 capital-I instances.
- ✅ `machine-economy.md` — definition 3 câu, 4 key ideas. 15 capital-I instances.
- ✅ `agentic-commerce.md` — definition 2 câu, 3 key ideas. 7 capital-I instances.
- ✅ `autonomous-agents.md` — definition 2 câu, 4 key ideas. 12 capital-I instances.
- ✅ `outcome-independence.md` — definition 3 câu, 4 key ideas. 16 capital-I instances.

**Quick-scan context (toàn bộ KB):**
- Tổng số file: 148 sources + 444 concepts = 592
- Double-i tồn đọng: 4 files, 10 instances (carry-over, không từ batch mới)
- Spacing merge tồn đọng: 8 files, 19 instances (carry-over, không từ batch mới)
- Capital-I tồn đọng (từ batch trước): 13 files, 31 instances — **chưa fix từ 07-16**
- Capital-I MỚI (batch 07-17): 237+ instances trên 14 file — **nghiêm trọng hơn dự đoán**
- 1-sentence definitions: 442 concepts (systemic, carry-over)
- Key points <5: 86 concepts (systemic, carry-over)
- Truncated concepts: 2 (psychic-energy + carry-over)
- Empty Key ideas: 11 concepts
- Empty Sources: 1 concept
- Draft concepts: 275

**Assessment:** Batch 07-17 có chất lượng cấu trúc tốt — tất cả file đều có sections đầy đủ, definition rõ ràng, summaries mạch lạc. Tuy nhiên bị ảnh hưởng nặng bởi lỗi capital-I systematic (237+ instances). Ngoài ra có 1 ERROR (psychic-energy.md truncated) và 1 broken wikilink (crypto-ai-stacking). Lỗi capital-I đã lan rộng hơn nhiều so với dự đoán từ 07-16 (chỉ 5 instances, giới hạn ở "ngườI") — cần escalation khẩn cấp đến Compile Agent prompt để chặn root cause.
