# Output Validation — 2026-06-23

**Status:** approved
**Approved by:** Julius — 2026-06-24
**Issues found:** 5 (0 ERROR, 3 WARNING, 2 INFO)
**Created:** 2026-06-23 23:10:07
**Validator:** output-validator

**Files checked:** 436 (102 sources + 334 concepts)
**New files today:** 13 (3 sources + 10 concepts)
**Previous run:** N/A (first run of 2026-06-23)

---

## Issue 1: [SYSTEMIC] "ngườii/đờii/lờii/rờii/thờii" typo — double 'i' after 'ờ'

**File:** Multiple — all 13 new files (10 concepts + 3 sources)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Từ tiếng Việt kết thúc bằng "ời" bị viết sai thành "ờii" (thừa một chữ 'i'). Lỗi hệ thống xuất hiện trong 100% file mới hôm nay (13/13 file), tổng cộng 52 instances.

**Patterns identified:**
- `ngườii` → `người` (39 instances, 12 files)
- `đờii` → `đời` (3 instances: completion-motivation, increasing-surface-area-luck, src_this-will-help-you-figure-out-what-you-want)
- `lờii` → `lời` (4 instances: increasing-surface-area-luck, src_nha-bao-lam-gi, src_this-will-help-you-figure-out-what-you-want)
- `rờii` → `rời` (4 instances: journalism-social-institution, knowledge-builder-journalist, src_nha-bao-lam-gi)
- `thờii` → `thời` (1 instance: src_gamification-app-truth)
- `thế giớii` → `thế giới` (1 instance: src_nha-bao-lam-gi)

**Root cause:** Compile Agent (hoặc LLM sinh nội dung) thêm thừa một chữ 'i' sau các từ tiếng Việt có âm "ời". Đây là biến thể mới của lỗi "ngưởi" trước đây (đã được Fix Agent sửa còn 1 file trong batch 06-22).

**Evidence (3 representative files):**
```
File: wiki/concepts/attention-economy-vs-knowledge-economy.md (line 16)
"...đại diện bởi ngườii sáng tạo nội dung..."

File: wiki/concepts/completion-motivation.md (line 23)
"...Ngườii thường xuyên đóng kín các vòng tròn có tỷ lệ mất ngủ thấp hơn 48% — chứng minh tạo ra giá trị đờii thực..."

File: wiki/sources/src_nha-bao-lam-gi.md (line 32)
"...Con ngườii không phản ứng với thế giới như nó vốn có, mà với hình ảnh về thế giớii trong nhận thức của mình"
```

**Suggested fix:** `sed -i 's/ngườii/người/g; s/đờii/đời/g; s/lờii/lời/g; s/rờii/rời/g; s/thờii/thời/g; s/giớii/giới/g'` trên toàn bộ 13 file. Review Compile Agent prompt để tránh lặp lại.

---

## Issue 2: [SYSTEMIC] 1-sentence definitions across 10 new concepts

**File:** All 10 new concepts (attention-economy-vs-knowledge-economy, completion-motivation, gamification-design-patterns, increasing-surface-area-luck, journalism-social-institution, knowledge-builder-journalist, recognizing-life-signals, self-discovery-through-conversations, streak-psychology, variable-reward-systems)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Toàn bộ 10 concept mới hôm nay đều có Definition 1 câu (cần 2-3 câu theo spec). Đây là vấn đề hệ thống từ Compile Agent template.

**Context:** Julius đã ghi nhận và deprioritize vấn đề này từ 2026-06-12 ("Explicitly Ignored: Summary 1 dòng"). Tuy nhiên, 100% file mới vẫn bị ảnh hưởng — đưa vào report để tracking.

**Evidence (representative):**
```
File: wiki/concepts/streak-psychology.md (line 16)
"Hiện tượng tâm lý trong thiết kế sản phẩm khi chuỗi ngày liên tiếp hoàn thành một hành vi (streak) biến động lực nội tại thành áp lực ngoại tại và nghĩa vụ ép buộc."

File: wiki/concepts/variable-reward-systems.md (line 16)
"Hệ thống phần thưởng trong đó ngườii dùng biết chắc chắn sẽ nhận được phần thưởng nhưng không biết giá trị cụ thể của nó."
```

**Suggested fix:** Đã có trong backlog. Không cần action riêng cho batch này. Khi Compile Agent được cập nhật template, tái biên dịch toàn bộ.

---

## Issue 3: [SYSTEMIC] 17 broken wikilinks in new concepts

**File:** 10 new concepts
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 17 wikilinks trỏ đến concepts chưa được biên dịch (forward references). Điều này được kỳ vọng trong KB đang phát triển, nhưng cần được tracking.

**Broken links by concept:**

| Concept | Broken links |
|---|---|
| attention-economy-vs-knowledge-economy | information-overload, media-literacy |
| completion-motivation | zeigarnik-effect, progress-tracking |
| gamification-design-patterns | behavioral-design |
| increasing-surface-area-luck | serendipity-engineering, career-pivots |
| journalism-social-institution | public-reasoning, democratic-institutions |
| knowledge-builder-journalist | deep-reporting |
| recognizing-life-signals | career-pivots, decision-making |
| self-discovery-through-conversations | career-exploration, emotional-intelligence |
| streak-psychology | loss-aversion, fomo-psychology |
| variable-reward-systems | intermittent-reinforcement, behavioral-addiction |

**Evidence:**
```
File: wiki/concepts/attention-economy-vs-knowledge-economy.md (line 29-30)
"- [[information-overload]]"
"- [[media-literacy]]"
→ Cả hai file không tồn tại trong wiki/concepts/ hoặc wiki/sources/
```

**Suggested fix:** Các link này sẽ tự resolved khi Compile Agent biên dịch các concept tương ứng. Không cần sửa ngay. Tracking để đảm bảo các concept được biên dịch trong các batch sau.

---

## Issue 4: All 13 new files have draft status

**File:** All 13 new files
**Severity:** INFO
**Dimension:** Completeness
**Issue:** 13/13 file mới hôm nay mang `status: draft` — đây là trạng thái mặc định cho file mới biên dịch, không phải vấn đề chất lượng.

**Suggested fix:** Không cần action. Tracking qua quick-scan: tổng số draft concepts hiện tại là 164/334 (49%).

---

## Issue 5: 81 concepts with <5 key points (quick-scan background)

**File:** 81 concepts (xem danh sách đầy đủ trong quick-scan output)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Quick-scan phát hiện 81 concepts có <5 key points. Trong đó có những file dùng cấu trúc subsection (###) thay vì bullet points — đây là false positive đã biết (xác nhận từ 06-12). Số lượng không thay đổi so với batch 06-22 (vẫn 81).

**Suggested fix:** Đã có trong backlog. Không cần action cho batch này. Khi Compile Agent cập nhật template, các file sẽ được tái cấu trúc.

---

## Summary

| Dimension | ERROR | WARNING | INFO |
|---|---|---|---|
| Factual | 0 | 0 | 0 |
| Completeness | 0 | 2 | 2 |
| Coherence | 0 | 0 | 0 |
| Vietnamese | 0 | 1 | 0 |
| **Total** | **0** | **3** | **2** |

**Quick-scan statistics:**
- "ngưởi" typo: 0 (fixed! was 1 in 06-22 evening, now 0)
- 1-sentence definitions: 332 concepts (unchanged, systemic)
- <5 key points: 81 concepts (unchanged, mostly false positives)
- Draft concepts: 164 (unchanged)
- Empty Key ideas: 1 (false positive — subsection-style file)
- Empty Sources: 0
- Truncated files: 0

**Key takeaway:** Batch hôm nay sạch về mặt factual và coherence. Vấn đề chính là typo "ngườii/đờii/lờii..." (biến thể mới của lỗi "ngưởi" cũ) xuất hiện trên 100% file mới — cần Fix Agent xử lý và Compile Agent điều chỉnh prompt để tránh lặp lại.
