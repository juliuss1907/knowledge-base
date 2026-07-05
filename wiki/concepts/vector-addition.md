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

# Vector Addition

## Definition

Phép cộng vector (vector addition) là một trong hai phép toán nền tảng của đại số tuyến tính. Về mặt hình học, cộng hai vector được thực hiện bằng cách đặt đuôi (tail) của vector thứ hai vào đầu (tip) của vector thứ nhất — vector tổng là mũi tên nối từ đuôi vector thứ nhất đến đầu vector thứ hai. Về mặt số học, phép cộng vector được tính bằng cách cộng từng thành phần tương ứng: `[x₁, y₁] + [x₂, y₂] = [x₁+x₂, y₁+y₂]`.

## Key ideas

- **Trực quan hình học:** Đặt đuôi vector thứ hai vào đầu vector thứ nhất, tổng là vector từ điểm bắt đầu đến điểm kết thúc — giống như bước đi hai bước liên tiếp
- **Công thức số học:** `[x₁, y₁] + [x₂, y₂] = [x₁+x₂, y₁+y₂]` — cộng từng thành phần tương ứng, mở rộng tự nhiên lên không gian n chiều
- **Phép cộng là phép hợp thành chuyển động:** Mỗi vector biểu diễn một bước di chuyển, cộng hai vector tương đương thực hiện lần lượt hai bước đó — cùng đích đến với một bước tổng hợp
- **Mở rộng từ phép cộng số thực:** Trên trục số, `2+5` nghĩa là di chuyển 2 bước phải rồi 5 bước phải = 7 bước phải — phép cộng vector tổng quát hóa ý tưởng này lên không gian nhiều chiều
- **Vai trò nền tảng:** Cùng với scalar multiplication, vector addition là phép toán cốt lõi — mọi chủ đề trong đại số tuyến tính (linear combinations, span, linear transformations) đều xây dựng từ hai phép toán này

## Related concepts

- [[vectors]]
- [[scalar-multiplication]]
- [[coordinate-systems]]

## Sources

- [[src_vectors-what-even-are-they-3b1b]]

## Notes

