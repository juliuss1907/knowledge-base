# Output Validation — 2026-07-07

**Status:** pending
**Issues found:** 8 (0 ERROR, 3 WARNING, 5 INFO)
**Created:** 2026-07-07 23:08:18 +0700
**Validator:** output-validator

---

## Summary

- ⚠️ 3 WARNING trên `human-premium.md`: definition 1 câu (cần 2-3), key ideas chỉ có 4 (cần 5-10), Sources section thiếu `src_career-advice-age-of-ai-phil-chen`
- ℹ️ 1 INFO: `map-is-not-territory.md` — definition có redundancy "các mô hình mental models"
- ℹ️ 3 INFO: forward-reference wikilinks → 3 missing targets (`cognitive-biases`, `confirmation-bias`, `maslow-hierarchy`) trong Related concepts của 2 concept mới
- ℹ️ 1 INFO systemic: 400 one-sentence definitions, 79 few key points, 9 empty Key ideas, 232 drafts — carry-over
- ✅ 9/10 files mới PASS hoàn toàn trên 4 dimensions (factual, completeness, coherence, Vietnamese)
- ✅ 3 sources sạch: đầy đủ sections, key points 9-10, Vietnamese tự nhiên, original excerpts đầy đủ
- 🔤 Quick-scan sạch: 0 typo "ngưởi", 0 typo "ngườii/đờii...", 0 spacing merge, 0 truncated trong 10 file mới
- 🔗 Cross-linking chặt chẽ: 3 cluster — `fable-finding-unknowns` (2 files), `human-nature-meta-skill` (2 files), `career-advice-ai-age` (3 files)

---

## New file deep validation: 10 files (3 sources + 7 concepts)

### Sources — ALL CLEAN ✅

| File | Key points | Definition | Issues |
|---|---|---|---|
| `src_field-guide-to-fable-finding-unknowns.md` | 9 | N/A | 0 |
| `src_most-profitable-skill-human-nature-dan-koe.md` | 9 | N/A | 0 |
| `src_career-advice-age-of-ai-phil-chen.md` | 10 | N/A | 0 |

Tất cả 3 sources có đầy đủ sections (Summary, Key points, Concepts referenced, Original excerpts), key points 9-10 (trong range 5-10), Vietnamese tự nhiên không có dấu hiệu MT artifacts.

### Concepts — 5/7 PASS ✅, 2 có issues

| File | Key ideas | Definition | Issues |
|---|---|---|---|
| `agentic-coding.md` | 8 | 2 câu ✅ | 0 |
| `persuasion-psychology.md` | 8 | 2 câu ✅ | 0 |
| `levels-of-awareness.md` | 8 | 2 câu ✅ | 0 |
| `problem-selection.md` | 7 | 2 câu ✅ | 0 |
| `last-mile-execution.md` | 6 | 2 câu ✅ | 0 |
| `map-is-not-territory.md` | 15 | 2 câu ✅ | 1 INFO |
| `human-premium.md` | 4 ⚠️ | 1 câu ⚠️ | 3 WARNING |

---

## Issue 1: Definition quá ngắn

**File:** wiki/concepts/human-premium.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition chỉ có 1 câu. Format spec yêu cầu 2-3 câu.
**Evidence:**
> "Giá trị gia tăng của con người trong các dịch vụ hoặc tương tác mà máy móc không thể thay thế, dựa trên khả năng kết nối cảm xúc, sự thú vị trong tính cách và kỹ năng xã hội (being a \"good hang\")."

**Suggested fix:** Mở rộng definition thành 2-3 câu. Thêm câu về ứng dụng thực tế hoặc phân biệt với AI capability. Có thể bổ sung perspective từ `src_career-advice-age-of-ai-phil-chen` về unique perspective và attention to detail ở last mile.

---

## Issue 2: Key ideas không đủ số lượng

**File:** wiki/concepts/human-premium.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Chỉ có 4 key ideas. Format spec yêu cầu 5-10.
**Evidence:** File có 4 bullet points trong section ## Key ideas. Quick-scan xác nhận `human-premium.md:4`.

**Suggested fix:** Thêm ít nhất 1 key idea. Source `src_career-advice-age-of-ai-phil-chen` có nội dung phong phú về human premium (unique perspective, attention to detail, differentiation from AI's median output). Có thể extract thêm 1-2 key ideas từ source này.

---

## Issue 3: Sources section không đồng bộ với frontmatter

**File:** wiki/concepts/human-premium.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Frontmatter liệt kê 2 sources (`src_2026-advice` + `src_career-advice-age-of-ai-phil-chen`), nhưng `## Sources` section chỉ có `src_2026-advice`. Thiếu `src_career-advice-age-of-ai-phil-chen`.

**Evidence:**
Frontmatter: `sources: ["[[src_2026-advice]]", "[[src_career-advice-age-of-ai-phil-chen]]"]`
Sources section: chỉ có `- [[src_2026-advice]]`

**Suggested fix:** Thêm `- [[src_career-advice-age-of-ai-phil-chen]]` vào `## Sources` section. Source này đã được compiled cùng ngày (2026-07-07) và reference đến human-premium — nên được include.

---

## Issue 4: Redundancy trong definition

**File:** wiki/concepts/map-is-not-territory.md
**Severity:** INFO
**Dimension:** Vietnamese quality
**Issue:** Definition có cụm "các mô hình mental models" — redundancy giữa tiếng Việt và tiếng Anh. "Mental models" đã là "mô hình tư duy" trong tiếng Việt, không cần prefix "các mô hình."

**Evidence:**
> "...các mô hình mental models, bản đồ, và sự trừu tượng hóa của thế giới..."

**Suggested fix:** Đổi thành một trong các lựa chọn: (a) "các mental model" (b) "các mô hình tư duy" (c) "mental models" — tùy theo phong cách nhất quán của file.

---

## Issue 5-7: Forward-reference wikilinks (3 targets)

**Severity:** INFO
**Dimension:** Factual accuracy
**Issue:** 3 wikilinks trong `## Related concepts` trỏ đến concepts chưa tồn tại. Đây là forward-references sẽ tự resolve khi concepts được compiled. Không phải broken links — chỉ là references đến nội dung chưa được tạo.

| Missing target | Referenced from |
|---|---|
| `cognitive-biases` | `map-is-not-territory.md` |
| `confirmation-bias` | `map-is-not-territory.md` |
| `maslow-hierarchy` | `persuasion-psychology.md` |

**Suggested fix:** Không cần action gấp. Tự resolve khi concepts tương ứng được compiled. Nếu muốn ưu tiên, 3 targets này đều là foundational concepts có thể cần compile sớm.

---

## Issue 8: Systemic patterns — carry-over

**Severity:** INFO
**Dimension:** Completeness (systemic)
**Issue:** Các systemic patterns từ các lần validation trước vẫn tồn tại. Không có thay đổi đáng kể so với run 2026-07-06.

| Pattern | Count | Delta từ 07-06 |
|---|---|---|
| One-sentence definitions | 400 | +0 (ổn định) |
| Too few key points (<5) | 79 | +0 (ổn định, human-premium mới đã được flag riêng) |
| Empty Key ideas | 9 | +0 |
| Draft concepts | 232 | +0 |
| Người spacing merge | 4 files / 11 instances | +0 (0 new, all carry-over) |

**Evidence (quick-scan output):**
```
📝 1-sentence definitions: 400 concepts
📊 Too few key points (<5): 79
📭 Empty Key ideas: 9
🏷️  Draft concepts: 232
🔤 Typo 'người' spacing merge: 4 files, 11 instances (new: 0)
```

Tất cả mechanical checks trên 10 file mới đều clean: 0 typo "ngưởi", 0 typo "ngườii/đờii...", 0 spacing merge, 0 truncated files.

**Suggested fix:** Không cần action trong run này. Carry-over patterns không có thay đổi. Spacing merge vẫn ở 4 file cũ (không file mới nào bị ảnh hưởng).

---

## Actions

- Review `wiki/reviews/2026-07-07_output-report.md`
- Nếu approve: giao Fix Agent sửa `human-premium.md` (definition + key ideas + missing source)
- `map-is-not-territory.md` redundancy: low priority, có thể defer
- Forward-reference wikilinks: tự resolve, không cần action
- Systemic carry-over: không cần action (ổn định từ 07-06)
- 9/10 file mới clean — batch chất lượng cao

---

**Report:** `wiki/reviews/2026-07-07_output-report.md`
