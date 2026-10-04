---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, vibecode]
topic: ai-design-workflow
sources:
  - "[[src_how-i-design-with-ai]]"
  - "[[src_unreasonable-effectiveness-of-html]]"
last_updated: 2026-10-03
---

# Design Process

## Definition

Design process là phương pháp có cấu trúc để thiết kế sản phẩm, được Christopher Alexander mô tả trong "Notes on the Synthesis of Form" và được Matt Dailey áp dụng cho việc dùng AI. Quy trình gồm 3 bước: (1) liệt kê tất cả constraints bạn đang thiết kế cho, (2) xem xét một loạt solutions thỏa mãn các constraints đó, (3) nếu nhận ra một constraint cần thêm hoặc có thể bỏ, quay lại bước 1. Điểm cốt lõi là quyết định constraints trước, không nhảy thẳng vào giải pháp.

## Key ideas

- **3 bước lặp:** constraints → array of solutions → feedback loop, quay lại bước 1 khi phát hiện constraint mới
- **Constraints đa dạng:** font và sizing rules, workflows phải hỗ trợ, business-logic states — bạn quyết định chúng
- **Lỗi phổ biến — skip bước 3:** chơi "design wackamole" — nhảy vào fix từng phần khi user confused, dẫn đến patchwork disjoint
- **AI làm trầm trọng wackamole:** prompting "Make X more prominent" hoặc "Add an affordance" tạo ra design ngẫu nhiên ưu tiên một số interactions, làm user càng confused
- **Feedback nên thay đổi constraints, không chỉ solutions:** khi feedback đến, đánh giá xem nó có thay đổi design constraints không trước khi nhảy vào giải pháp
- **Xử lý papercuts:** giữ document tracking minor annoyances, move fast trên obvious fixes nhưng gom minor ones để xử lý cohesively khi redesign
- **Bước "xem xét một loạt solutions" chạy song song thay vì tuần tự:** dàn nhiều hướng khác biệt rõ (layout, tone, density) cạnh nhau trong một trang, mỗi hướng gắn nhãn trade-off, để so sánh trực tiếp thay vì đánh giá tuần tự từng phương án
- **Trình duyệt là công cụ chẩn đoán cho constraint chưa rõ:** bản HTML cho phép thấy ngay hậu quả của một thay đổi trước khi chốt — phản hồi trả về dạng constraint, đúng với vòng lặp bước 3

## Related concepts

- [[product-vs-prototype]]
- [[codified-taste]]
- [[problem-statement-redesign]]
- [[taste-judgment]]
- [[multi-file-artifact-workflow]]
- [[html-as-agent-output-format]]

## Sources

- [[src_how-i-design-with-ai]]
- [[src_unreasonable-effectiveness-of-html]] — Thariq Shihipar, Anthropic (2026-05-20)

## Notes
