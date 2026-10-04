---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, coding, strategy]
topic: ai-ad-creative-system
sources:
  - "[[src_how-to-make-infinite-ads-with-claude-code]]"
last_updated: 2026-10-04
---

# LLM Judge Loop

## Definition

LLM judge loop là kiểm soát chất lượng bằng cách cho một model khác chấm điểm output của model tạo sinh theo một rubric viết trước, rồi dùng phán quyết đó quyết định giữ hay sửa — trước khi con người kịp nhìn. Vòng lặp đóng lại khi phần feedback của con người được ghi thành rule vĩnh viễn trong file cấu hình.

## Key ideas

- **Thứ tự là toàn bộ ý tưởng:** "khi ảnh quay về, đừng nhìn nó vội, hãy để judge nhìn trước" — con người bị loại khỏi vòng lặp sàng lọc ban đầu vì mắt người dễ tha thứ cho output kém
- **Rubric phải viết trước, cụ thể, kiểm chứng được:** các tiêu chí mẫu gồm hallucinations (có bịa thứ không có trong brief/catalog/template không), product accuracy (sản phẩm có khớp ảnh catalog), logo fidelity (đúng hình, không méo, đúng vị trí theo rules), brand identity (có giống ta không)
- **Phán quyết là nhị phân trước, điểm số sau:** pass/fail theo chiều đánh giá, không phải thang điểm tổng — điểm tổng che mất việc một chiều hỏng là fail
- **Sửa cục bộ chứ không làm lại:** ảnh fail đưa sang model edit mạnh hơn với prompt chỉ sửa đúng vấn đề, thay vì regenerate từ đầu — giữ nguyên phần đã đúng, tiết kiệm compute
- **Chặn trên số vòng lặp:** mặc định thử 1–2 lần rồi bỏ ảnh đó; vòng lặp vô hạn là lãng phí token và sinh output tệ hơn
- **Điều kiện dừng sớm quan trọng hơn số vòng:** nếu judge fail trên quá nhiều chiều cùng lúc, báo hiệu ý tưởng gốc không đáng sửa — dừng loop, thay ý tưởng
- **Vòng đóng chỉ hoàn tất ở bước cuối:** phản hồi của người dùng phải được chuyển thành rule trong `rules.md`, nếu không sẽ phải sửa đi sửa lại cùng một lỗi ở các batch sau
- **Sửa cùng lỗi hai lần là bug trong hệ thống, không phải trong ảnh:** mỗi lỗi lặp lại một lần nữa là dấu hiệu thiếu rule, xem [[codified-taste]]
- **Phù hợp với workflow ở đầu ra:** judge hoạt động tốt nhất khi output có thể mô tả bằng tiêu chí quan sát được (ảnh, code, tài liệu) chứ không với output mở nghĩa

## Related concepts

- [[brand-brain]]
- [[behavioral-evals]]
- [[ai-evals]]
- [[harness-engineering]]
- [[plan-execute-verify-loop]]

## Sources

- [[src_how-to-make-infinite-ads-with-claude-code]]

## Notes
