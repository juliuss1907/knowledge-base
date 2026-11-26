# Output Validation — 2026-11-22

**Status:** approved
**Approved by:** Julius
**Issues found:** 2 (0 ERROR, 2 WARNING, 0 INFO)
**Created:** 2026-11-22 23:00:36 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Quét cơ học 880 tệp: 232 sources và 648 concepts. Đọc chi tiết 11 tệp mang ngày biên soạn hoặc cập nhật 2026-11-22: 1 source và 10 concepts; ngày cập nhật không đồng nghĩa tất cả đều là tệp mới.
- Đối chiếu source mới và bốn concept ASI với bản raw DeepMind; đối chiếu ba concept về học tập với source Stanford và bản raw tương ứng. Ba concept còn lại được kiểm tra so với nội dung và báo cáo ngày 2026-11-21; chưa đối chiếu lại đầy đủ với raw của chúng.
- Không xác minh độc lập các nghiên cứu gốc, tuyên bố của nhà sản xuất hoặc toàn bộ nội dung 880 tệp theo bốn chiều chất lượng. Không suy ra độ chính xác thực tế chỉ từ sự nhất quán với raw.
- Bốn nhóm mẫu mất chữ i: không có kết quả trong sources và concepts. Các đích wikilink trong thân 11 tệp tồn tại theo tên tệp chính xác. Quick-scan báo 117 định nghĩa một câu và 77 concepts ít ý theo heuristic; chưa xác minh từng trường hợp và không tính chúng là lỗi mới.
- Các concept trong lô đều có `status: draft`. Không thay đổi nội dung hoặc trạng thái.

## Issue 1: Khái quát quan hệ nhân quả từ bằng chứng theo bối cảnh

**File:** wiki/concepts/cognitive-offloading.md:16,23–25; wiki/concepts/transfer-of-learning.md:22–24
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Các câu mô tả tác hại của offloading và mức độ tổn hại như kết luận chung hoặc tỷ lệ xác định. Bản raw Stanford nói việc giao các quá trình nhận thức sâu *có thể* làm giảm khả năng, và kết quả Brazil tập trung ở nhóm dùng AI nhiều hơn; đây không đủ để xác lập quan hệ tỷ lệ chung giữa mức offload và tác hại.
**Evidence:** `cognitive-offloading.md:23`: “Offload các quá trình nhận thức sâu … làm giảm khả năng”; `transfer-of-learning.md:24`: “Mức độ tổn hại tỉ lệ với mức độ offload”. Raw `raw/articles/2026-11-04_cognitive-offloading-learning-ai.md:32,74–82` dùng “can reduce” và “suggests”.
**Suggested fix:** Đổi sang “có thể làm giảm”; quy thuộc kết quả và mối liên hệ với mức dùng AI cho nghiên cứu học sinh Brazil; không khẳng định tỷ lệ hoặc quan hệ nhân quả phổ quát khi chưa có nghiên cứu gốc hỗ trợ.

## Issue 2: Định nghĩa transfer dùng tiêu chuẩn loại trừ tuyệt đối

**File:** wiki/concepts/transfer-of-learning.md:16
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Câu định nghĩa đồng nhất năng lực chỉ thể hiện khi có công cụ với năng lực hoàn toàn thuộc về công cụ. Điều này bỏ qua khả năng người học có kỹ năng sử dụng công cụ; nó cũng căng với dòng 25, nơi tệp thừa nhận phải nêu điều kiện dùng công cụ khi đánh giá transfer.
**Evidence:** “nếu năng lực chỉ tồn tại khi có công cụ hỗ trợ thì đó là năng lực của công cụ, không phải của người học.” Raw Stanford dòng 42 chỉ định nghĩa transfer là áp dụng kiến thức, kỹ năng và chiến lược sang ngữ cảnh mới.
**Suggested fix:** Phân biệt năng lực thực hiện có hỗ trợ và năng lực độc lập; đánh giá transfer theo nhiệm vụ mới và điều kiện sử dụng công cụ, không phủ nhận toàn bộ năng lực của người học.
