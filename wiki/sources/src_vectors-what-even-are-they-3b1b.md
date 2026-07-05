---
type: source
original: "[[2026-07-04_vectors-what-even-are-they-3b1b]]"
main_tag: ai
sub_tags: [tutorial, research, coding]
topic: vectors-fundamentals
date_compiled: 2026-07-05
url: https://www.3blue1brown.com/lessons/vectors
author: Grant Sanderson (3Blue1Brown)
---

# Vectors, what even are they? — Linear Algebra Chapter 1

## Metadata

- **Author:** Grant Sanderson (3Blue1Brown)
- **Published:** 2016-08-06
- **Source:** 3Blue1Brown
- **URL:** https://www.3blue1brown.com/lessons/vectors
- **Type:** article

## Summary

Bài viết là chương đầu tiên trong series Linear Algebra của 3Blue1Brown, giới thiệu khái niệm vector qua ba góc nhìn: vật lý (mũi tên trong không gian có độ dài và hướng), khoa học máy tính (danh sách số có thứ tự), và toán học (bất kỳ đối tượng nào có phép cộng và nhân vô hướng được định nghĩa hợp lý). Grant Sanderson giải thích cách hệ tọa độ tạo ra cầu nối giữa hai cách hiểu trực quan (mũi tên) và tính toán (danh sách số), thông qua phép cộng vector và phép nhân vô hướng. Sức mạnh của đại số tuyến tính đến từ khả năng chuyển đổi qua lại giữa hai biểu diễn này — người phân tích dữ liệu có thể hình dung danh sách số dưới dạng hình học, trong khi lập trình viên đồ họa có thể thao tác không gian bằng các con số.

## Key points

- Vector có thể được hiểu theo 3 cách: mũi tên trong không gian (vật lý), danh sách số có thứ tự (CS), và bất kỳ thứ gì có phép cộng + nhân vô hướng (toán học)
- Trong vật lý, vector được định nghĩa bởi độ dài và hướng, có thể di chuyển tự do mà vẫn là cùng một vector
- Trong CS, vector là ordered list — thứ tự các phần tử quan trọng, mỗi chiều là một feature riêng
- Hệ tọa độ tạo ra song ánh (bijection) giữa mỗi cặp/bộ số và một vector duy nhất: tọa độ là chỉ dẫn đi từ gốc đến đầu mũi tên
- Phép cộng vector: đặt đuôi vector thứ hai vào đầu vector thứ nhất, tổng là vector từ đuôi đầu tiên đến đầu thứ hai — tương đương `[x₁+x₂, y₁+y₂]`
- Phép nhân vô hướng (scalar multiplication): nhân với 2 → kéo dài gấp đôi, nhân với ⅓ → co lại ⅓, nhân với số âm → đảo hướng
- Hai phép toán cơ bản nhất của đại số tuyến tính là vector addition và scalar multiplication — mọi chủ đề nâng cao đều xoay quanh chúng
- Sức mạnh thực sự nằm ở khả năng dịch chuyển giữa biểu diễn hình học và biểu diễn số học
- Trích dẫn Hermann Weyl: "The introduction of numbers as coordinates is an act of violence" — gợi ý rằng việc gán số cho không gian là một sự áp đặt, nhưng cũng là công cụ mạnh mẽ

## Concepts referenced

- [[vectors]]
- [[vector-addition]]
- [[scalar-multiplication]]
- [[coordinate-systems]]

## Original excerpts

> "The introduction of numbers as coordinates is an act of violence." — Hermann Weyl

> Every linear algebra topic revolves around vector addition and scalar multiplication.
