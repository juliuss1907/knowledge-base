# Output Validation — 2026-10-13

**Status:** pending
**Issues found:** 1 (0 ERROR, 1 WARNING, 0 INFO)
**Created:** 2026-10-13 23:05:00
**Validator:** output-validator
**Files checked:** 851 (222 sources + 629 concepts)
**New files:** 5 (1 source + 4 concepts)

---

## Issue 1: Too few key points in concept

**File:** wiki/concepts/separation-of-creation-and-judgment.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Section `## Key ideas` chỉ có 4 ý (ngưỡng tối thiểu theo spec là 5-10 ý).
**Evidence:**
```markdown
## Key ideas

- Tự phê phán sớm dập tắt sáng tạo: việc biên tập và phán xét nhảy vào quá trình ngay từ những câu đầu tiên sẽ xem sự vụng về ban đầu như bằng chứng của sự thất bại, khiến nhiều dự án bị bỏ dở trước khi thành hình.
- Bản thảo thô là công cụ tư duy: trang nháp vụng về không phải là một sản phẩm hoàn thiện bị lỗi, mà là không gian để người viết phát hiện và làm rõ suy nghĩ của chính mình; biên tập không thể cải thiện câu văn mà cái tôi từ chối viết ra.
- Lịch trình riêng biệt: phân bổ các phiên làm việc độc lập—phiên thứ nhất dành hoàn toàn cho việc khám phá và xả ý tưởng thô; các phiên sau mới dành cho việc mài giũa cấu trúc và chọn lọc từ ngữ.
- Quyền được viết tệ trong thời gian ngắn: cho phép bản thân tạo ra những đoạn văn dở tệ trong 10-15 phút đầu phiên làm việc giúp triệt tiêu áp lực phải gây ấn tượng, mở đường cho những ý tưởng sâu sắc tự nhiên xuất hiện sau đó.
```
**Suggested fix:** Bổ sung ý thứ 5 từ nguồn `src_how-i-stopped-feeling-overwhelmed`, ví dụ: hoãn việc đòi hỏi bản thảo thô phải chứng minh giá trị ngay từ đầu, hoặc xem trang nháp là không gian thử nghiệm thay vì sản phẩm hoàn thiện bị lỗi.

---

## Summary

- **Files checked:** 851 (222 sources + 629 concepts)
- **New files validated:** 5 (1 source: `src_how-i-stopped-feeling-overwhelmed`, 2 new concepts: `creative-overwhelm`, `separation-of-creation-and-judgment`, 2 updated concepts: `attention-management`, `consumption-vs-action`)
- **Factual accuracy:** 100% claims định lượng và nội dung khớp raw source `raw/articles/2026-07-29_how-i-stopped-feeling-overwhelmed.md`.
- **Completeness:** 4/5 file đạt chuẩn cấu trúc; 1 concept (`separation-of-creation-and-judgment.md`) có 4/5 key ideas (WARNING).
- **Coherence:** Luồng lập luận mạch lạc, không mâu thuẫn nội tại hay nhân bản ý trùng (Defect B = 0).
- **Vietnamese quality:** Ngôn ngữ tự nhiên, không có hiện tượng dịch máy hay lỗi tokenization:
  - `ngưởi`: 0
  - `ngườii/đờii/lờii...` (double-i): 0
  - `người[a-z]` spacing merge: 0
  - `ngườI` capital-I: 0
  - dropped-i variant 5 (`ngườ`, `thờ`, `thay v`, `chính lờ`): 0 (chuỗi 18 lượt sạch liên tiếp)
  - CJK contamination: 0
- **Wikilinks & Backlinks:** 100% wikilink hợp lệ. Không có forward-ref mới nào ngoài `[[deep-work]]` đã có sẵn từ trước trong `attention-management.md`. Defect A = 0 (100% khớp giữa frontmatter và body `## Sources`). Source dùng `## Key points` chuẩn (Defect C = 0).
- **Raw layer:** `raw/articles/2026-07-29_how-i-stopped-feeling-overwhelmed.md` có `status: processed` và `compiled_to: "[[src_how-i-stopped-feeling-overwhelmed]]"`. Raw backlog: 0 unprocessed.
