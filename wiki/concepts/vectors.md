---
type: concept
status: draft
main_tag: ai
sub_tags: [tutorial, research, coding]
topic: vectors-fundamentals
sources:
  - "[[src_vectors-what-even-are-they-3b1b]]"
last_updated: 2026-07-05
---

# Vectors

## Definition

Vector là một đối tượng toán học có thể được hiểu qua ba góc nhìn bổ sung cho nhau: trong vật lý, vector là mũi tên trong không gian có độ dài và hướng; trong khoa học máy tính, vector là danh sách số có thứ tự (ordered list); trong toán học thuần túy, vector là bất kỳ đối tượng nào có phép cộng và phép nhân vô hướng được định nghĩa một cách hợp lý. Ba định nghĩa này không mâu thuẫn mà bổ trợ cho nhau — tùy ngữ cảnh, ta chọn cách hiểu phù hợp nhất.

## Key ideas

- **Ba góc nhìn tương đương:** Vật lý (mũi tên), CS (danh sách số), Toán học (đại số trừu tượng) — mỗi góc nhìn hữu ích trong ngữ cảnh riêng
- **Tính chất vật lý:** Vector được xác định bởi độ dài và hướng, không phụ thuộc vào vị trí — có thể tịnh tiến tự do mà vẫn là cùng một vector
- **Tính chất CS:** Vector là ordered list, thứ tự phần tử có ý nghĩa — mỗi vị trí đại diện cho một feature/chiều khác nhau (ví dụ: `[diện_tích, giá]` cho nhà)
- **Tính chất toán học:** Định nghĩa trừu tượng nhất — bất kỳ tập hợp nào có phép cộng và nhân vô hướng thỏa mãn các tiên đề đều là không gian vector
- **Cầu nối tọa độ:** Hệ tọa độ tạo ra song ánh giữa hình học (điểm/mũi tên) và đại số (bộ số) — đây là nền tảng cho mọi ứng dụng của đại số tuyến tính
- **Vai trò trong AI/ML:** Vector là cấu trúc dữ liệu nền tảng — embeddings, feature vectors, weights đều được biểu diễn dưới dạng vector
- **Câu nói của Weyl:** "The introduction of numbers as coordinates is an act of violence" — gán số cho không gian là một sự áp đặt trừu tượng, nhưng chính sự áp đặt này mở ra khả năng tính toán mạnh mẽ

## Related concepts

- [[vector-addition]]
- [[scalar-multiplication]]
- [[coordinate-systems]]

## Sources

- [[src_vectors-what-even-are-they-3b1b]]

## Notes

