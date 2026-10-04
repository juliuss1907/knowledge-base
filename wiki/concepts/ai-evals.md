---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, system]
topic: ai-token-workforce
sources:
  - "[[src_you-just-hired-a-million-bad-employees-a16z]]"
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# AI Evals

## Definition

AI evals (evaluations) là hệ thống đo lường objective để xác định AI output có đúng hay không - tương đương với OKRs cho human workforce. Coding là use case AI duy nhất "breakout" vì có evals built-in (code chạy hoặc không). Evals chuyển đổi fuzzy human processes thành quantitative metrics, cho phép firms leverage infinitely scalable token workforce một cách reliable.

## Key ideas

- 99% AI revenue hiện nay đến từ coding vì coding có built-in evals
- Evals là breakout mechanism cho cross-domain AI use cases
- Firms sẽ có proprietary eval suites khác nhau - đây là competitive advantage
- Generic evals hoặc agents không tạo ra edge cho organizations
- Eval suite sẽ trở thành tài nguyên quý giá nhất của một firm
- Real work của management là express qualitative processes dưới dạng quantitative
- Specific evals quan trọng hơn teaching employees prompting
- Evals là path để chạy 100X tokens hiệu quả
- **Public benchmark mất dần giá trị phân biệt:** toàn bộ 113 task và lời giải của Deep SWE được công khai từ tháng 5, nên lab có thể học chúng trong post-training và nhắm điểm số — benchmark công khai bị nhiễm rất nhanh
- **Chất lượng eval cũng suy giảm:** Epoch phát hiện 23 task lỗi trong bộ benchmark đó; số liệu do lab tự báo cáo cần "healthy skepticism"
- **Benchmark saturate nhanh hơn trước**, buộc refresh thường xuyên hơn → gánh nặng đánh giá tiến bộ thật chuyển sang người dùng
- **Hệ quả chiến lược:** khoảng cách giữa model đang đua benchmark và model thực sự được dùng phải đo bằng adoption (harness + model adoption), xem [[model-vs-harness-adoption]]

## Related concepts

- [[100x-token]]
- [[ai-transformation]]
- [[benchmark-contamination]]
- [[model-vs-harness-adoption]]

## Sources

- [[src_you-just-hired-a-million-bad-employees-a16z]]
- [[src_gemini-4-argon-explained-in-5min]]

## Notes

