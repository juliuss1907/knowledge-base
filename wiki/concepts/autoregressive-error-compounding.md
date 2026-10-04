---
type: concept
status: draft
main_tag: ai
sub_tags: [research, system]
topic: autoregressive-error-compounding
sources:
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# Autoregressive Error Compounding

## Definition

Autoregressive error compounding là hiện tượng sai sót tích luỹ dọc theo chuỗi sinh token của mô hình autoregressive: mỗi bước sinh token có một xác suất đúng nhỏ hơn 1, và các lỗi cộng dồn theo độ dài quỹ đạo. Hệ quả là độ tin cậy của chuỗi dài suy giảm theo hàm mũ, khiến việc duy trì coherence ở quy mô hàng triệu token trở thành thách thức kỹ thuật trung tâm.

## Key ideas

- **Ví dụ tính toán trong video:** nếu mỗi token đúng với xác suất 99%, thì chuỗi **100 bước độc lập chỉ còn khoảng 37% khả năng mọi bước đều đúng** (0.99^100 ≈ 0.366) — giảm theo hàm mũ chứ không phải tuyến tính
- **Điều kiện lý thuyết:** phép tính trên giả định lỗi ở các bước là độc lập; thực tế cơ chế attention có thể hỗ trợ hoặc làm trầm trọng thêm tùy cách huấn luyện
- **Chỉ trích của Yann LeCun:** ông chỉ trích mô hình autoregressive vì cơ chế sinh token liên tiếp làm lỗi tích luỹ trên quỹ đạo dài — đặc biệt nghiêm trọng khi độ dài quỹ đạo lớn
- **Quy mô làm thay đổi bản chất vấn đề:** khác biệt giữa 64.000 và 1 triệu token không phải chỉ là hệ số, mà là bước nhảy sang vùng mà error compounding trở nên quyết định
- **Cam kết thương mại như tín hiệu kỹ thuật:** việc Google dám mở rộng output lên 1 triệu token cho sản phẩm thương mại ngụ ý mức tin cậy đủ cao ở dài context — xem [[long-context-models]]
- **Use case được mở khóa:** code migration, research task chạy dài, và mọi workflow nhiều bước nơi chất lượng đầu ra cuối phụ thuộc tính đúng của toàn bộ chuỗi, không chỉ bước cuối
- **Hệ quả thiết kế:** muốn giảm rủi ro phải giảm xác suất lỗi mỗi bước, thêm verification ở từng giai đoạn, hoặc chấp nhận rằng độ dài quỹ đạo phải được giới hạn ở mức mà độ tin cậy chấp nhận được

## Related concepts

- [[long-context-models]]
- [[context-window-management]]
- [[tokenization]]
- [[error-signal-learning]]
- [[gemini-4-argon]]

## Sources

- [[src_gemini-4-argon-explained-in-5min]]

## Notes
