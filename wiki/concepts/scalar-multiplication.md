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

# Scalar Multiplication

## Definition

Phép nhân vô hướng (scalar multiplication) là phép toán nhân một vector với một số thực (scalar), làm thay đổi độ dài và/hoặc hướng của vector. Nhân với số >1 kéo dài vector, nhân với số trong khoảng (0,1) co ngắn vector, và nhân với số âm vừa đảo hướng vừa thay đổi độ dài. Về mặt số học: `c * [x, y] = [c*x, c*y]`.

## Key ideas

- **Scaling trực quan:** Nhân với 2 → dài gấp đôi; nhân với ⅓ → co lại còn ⅓; nhân với -1.5 → đảo hướng + dài gấp 1.5 lần
- **Công thức số học:** `c * [x, y] = [c*x, c*y]` — nhân từng thành phần với cùng một hằng số, mở rộng trực tiếp lên không gian n chiều
- **Scalar là số thực:** Trong ngữ cảnh đại số tuyến tính cơ bản, scalar luôn là số thực — chúng "scale" (co giãn) vector
- **Không thay đổi đường thẳng chứa vector:** Khi nhân với scalar dương, vector nằm trên cùng một đường thẳng qua gốc tọa độ — chỉ độ dài thay đổi
- **Vai trò nền tảng:** Cùng với vector addition, scalar multiplication định nghĩa không gian vector — mọi khái niệm nâng cao (linear combination, span, basis, linear transformation) đều bắt nguồn từ đây
- **Ứng dụng trong ML:** Scalar multiplication là nền tảng của các phép biến đổi như scaling features, gradient descent (step size × gradient), và regularization

## Related concepts

- [[vectors]]
- [[vector-addition]]
- [[coordinate-systems]]

## Sources

- [[src_vectors-what-even-are-they-3b1b]]

## Notes

