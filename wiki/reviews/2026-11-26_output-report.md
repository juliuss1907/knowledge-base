# Output Validation — 2026-11-26

**Status:** pending
**Issues found:** 2 (0 ERROR, 2 WARNING, 0 INFO)
**Created:** 2026-11-26 23:00 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Quét cơ học 881 tệp: 233 nguồn và 648 khái niệm. Đọc và đánh giá chi tiết 6 khái niệm cập nhật ngày 2026-11-26; đây là các tệp đã tồn tại, không phải 6 tệp mới.
- Đối chiếu hai khái niệm về học tập với `wiki/sources/src_cognitive-offloading-learning-ai.md` và bản raw Stanford; đối chiếu `internal-locus-of-control.md` với nguồn được dẫn. Không kiểm chứng độc lập các nghiên cứu gốc hoặc toàn bộ nội dung 881 tệp theo bốn chiều.
- Các thay đổi được đối chiếu với nội dung trước đó: những câu cụ thể bị nêu trong báo cáo 2026-11-22 và 2026-11-25 đã được điều chỉnh theo hướng thận trọng hơn; lỗi `Ngườ` trong báo cáo 2026-11-23 đã được sửa. Đây là xác nhận đối với các đoạn nêu cụ thể, không phải xác nhận mọi vấn đề liên quan đã được giải quyết.
- Các wikilink trong 6 tệp có đích đúng tên. Không phát hiện mẫu mất chữ i trong bốn nhóm kiểm tra bổ sung, không phân biệt hoa thường. Quick-scan báo 117 định nghĩa một câu và 77 khái niệm ít ý theo heuristic; chưa xác minh từng trường hợp, không tính là lỗi mới.
- Không sửa, di chuyển hoặc xóa tệp nội dung. Hai vấn đề dưới đây là phát hiện trong các tệp cập nhật, không khẳng định chúng mới phát sinh ngày 2026-11-26.

---

## Issue 1: Đồng nhất locus of control với niềm tin mọi việc đều thuận lợi

**File:** `wiki/concepts/internal-locus-of-control.md:16,21,24`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Tệp trình bày niềm tin rằng vận mệnh luôn thuận lợi như một ý chính của locus of control nội tại, trong khi đó là khái niệm khác với niềm tin kết quả chịu ảnh hưởng của hành động bản thân. Tệp còn khẳng định bốn nhân vật lịch sử đều có đặc điểm tâm lý này mà không đưa bằng chứng cho từng người; nguồn được dẫn không cung cấp bằng chứng đó.
**Evidence:** “Tin rằng vận mệnh hoàn toàn thuận lợi cho mình”; “Những người vĩ đại trong lịch sử (Alexander Đại đế, Julius Caesar, Napoleon, Thành Cát Tư Hãn) đều có locus of control nội tại mạnh mẽ”.
**Suggested fix:** Định nghĩa theo mức độ một người tin kết quả chịu ảnh hưởng từ hành động của họ, không đồng nhất với lạc quan tuyệt đối hay quyền kiểm soát mọi kết quả. Bỏ khẳng định về từng nhân vật hoặc bổ sung nguồn đáng tin cậy và quy thuộc cụ thể.

---

## Issue 2: Khái quát tác động lên tự đánh giá thành kết luận tất yếu

**File:** `wiki/concepts/cognitive-offloading.md:25`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Câu này khẳng định offloading làm giảm tự đánh giá của người học như hệ quả chung. Raw Stanford dòng 32 nói các đánh giá này *có thể* giảm khi offload các nhiệm vụ học tập; bài không cung cấp tại đoạn đó bằng chứng cho mọi hình thức offloading hoặc mọi người học.
**Evidence:** “Offloading còn bào mòn self-perception: người học tự đánh giá thấp khả năng sáng tạo và mức độ kiên cường học tập của mình.” Raw: “a student’s self-perceptions of creative ability and learning resilience can be reduced by offloading learning tasks.”
**Suggested fix:** Quy thuộc nhận định cho nguồn và dùng “có thể giảm” trong bối cảnh offload nhiệm vụ học tập; bổ sung nghiên cứu gốc nếu muốn mô tả điều kiện và mức tác động cụ thể.
