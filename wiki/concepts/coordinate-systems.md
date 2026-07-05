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

# Coordinate Systems

## Definition

Hệ tọa độ (coordinate system) là một hệ quy chiếu dùng để gán mỗi điểm trong không gian với một bộ số duy nhất. Trong không gian 2D, hệ tọa độ Descartes gồm trục x (ngang) và trục y (dọc) giao nhau tại gốc tọa độ (origin) — gốc này vừa là trung tâm của không gian, vừa là gốc của mọi vector. Tọa độ của một điểm chính là chỉ dẫn cách đi từ gốc đến điểm đó: di chuyển theo trục x trước, rồi song song với trục y.

## Key ideas

- **Song ánh (bijection):** Mỗi cặp số (2D) hoặc bộ ba số (3D) tương ứng với chính xác một điểm/vector duy nhất trong không gian — không có sự mơ hồ
- **Gốc tọa độ (origin):** Điểm giao của tất cả các trục, vừa là tâm không gian vừa là điểm bắt đầu của mọi vector — mọi tọa độ đều được đo từ đây
- **Quy ước dấu:** Trục x: dương = phải, âm = trái; trục y: dương = lên, âm = xuống; trục z (3D): vuông góc với mặt phẳng xy
- **Cầu nối hình học - đại số:** Hệ tọa độ cho phép chuyển đổi hai chiều giữa trực quan hình học (mũi tên) và tính toán số học (danh sách số) — đây là insight cốt lõi của đại số tuyến tính
- **Trích dẫn Weyl:** "The introduction of numbers as coordinates is an act of violence" — việc áp đặt hệ tọa độ là một hành động trừu tượng hóa không tự nhiên, nhưng chính nó mở ra toàn bộ sức mạnh tính toán của đại số tuyến tính
- **Mở rộng lên n chiều:** Dù không thể hình dung trực quan trên 3 chiều, hệ tọa độ mở rộng tự nhiên lên không gian n chiều bằng cách thêm trục mới vuông góc với tất cả trục hiện có

## Related concepts

- [[vectors]]
- [[vector-addition]]
- [[scalar-multiplication]]

## Sources

- [[src_vectors-what-even-are-they-3b1b]]

## Notes

