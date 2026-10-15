---
type: concept
status: draft
main_tag: ai
sub_tags: [research]
topic: attention-mechanism-foundation
sources:
  - "[[src_is-attention-the-essence-of-intelligence]]"
last_updated: 2026-10-15
---

# Attention Mechanism

## Definition

Cơ chế attention là một toán tử toán học trong mạng neural nhân tạo cho phép mô hình tập trung động vào các phần khác nhau của chuỗi đầu vào khi tính toán biểu diễn của một từ hoặc phần tử cụ thể. Kỹ thuật này lần đầu được đề xuất bởi Dzmitry Bahdanau, Kyunghyun Cho và Yoshua Bengio vào năm 2014 nhằm giải quyết nút thắt cổ chai của vector ngữ cảnh có độ dài cố định trong dịch máy.

## Key ideas

- **Loại bỏ nút thắt bộ nhớ cố định:** Thay vì nén toàn bộ câu dài vào một vector ẩn duy nhất trước khi giải mã, attention cho phép bộ giải mã quét qua toàn bộ câu gốc để tìm thông tin liên quan nhất cho mỗi bước sinh từ tiếp theo.
- **Bộ ba vector Query - Key - Value:** Mỗi từ được chiếu tuyến tính thành ba vector: query đại diện cho thông tin từ đó đang tìm kiếm, key đại diện cho đặc trưng nhận diện của các từ khác, và value chứa nội dung thực tế đóng góp vào biểu diễn mới.
- **Biến ngữ cảnh thành toán học:** Mức độ phù hợp giữa query và key (thường đo bằng tích vô hướng) quyết định trọng số chú ý; các trọng số này nhân với value tương ứng để tạo ra một biểu diễn mới giàu ngữ cảnh cho từ hiện tại.
- **Khả năng mở rộng quy mô:** Phép tính ma trận song song của attention cho phép xử lý văn bản có độ dài lớn hiệu quả hơn rất nhiều so với các bước lặp tuần tự của mạng RNN truyền thống.
- **Học liên kết thống kê tự động:** Mô hình tự động khám phá và mã hóa các quan hệ ngữ nghĩa, ngữ pháp phức tạp (như đại từ thay thế cho danh từ xa) qua hàng tỷ trọng số mà không cần bất kỳ luật định trước nào từ con người.

## Related concepts

- [[transformer-architecture]]
- [[language-modeling-ai-complete]]
- [[csa-hca-attention]]

## Sources

- [[src_is-attention-the-essence-of-intelligence]]

## Notes
