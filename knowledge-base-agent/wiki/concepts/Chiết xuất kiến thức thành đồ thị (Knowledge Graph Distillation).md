---
type: concept
status: draft
tags: [#ai, #coding, #productivity]
---
# Chiết xuất kiến thức thành đồ thị (Knowledge Graph Distillation)

## Mô tả
Chiết xuất kiến thức thành đồ thị là quá trình chuyển đổi các tài liệu dài (như sách, báo cáo) thành một cấu trúc đồ thị (knowledge graph) thay vì tóm tắt văn bản phẳng. Phương pháp này giúp bảo toàn mối quan hệ giữa các khái niệm, cho phép người dùng thấy được sự kết nối và trọng tâm của nội dung mà không bị giới hạn bởi cửa sổ ngữ cảnh (context window) của LLM.

### Quy trình thực hiện (ví dụ từ SpineDigest)
- **Trích xuất Chunk (Chunk Extraction):** Chia nhỏ tài liệu và trích xuất các đơn vị kiến thức độc lập (facts, arguments, concepts) từ từng phần.
- **Xây dựng đồ thị (Knowledge Graph Construction):** Sử dụng thuật toán phân cụm dựa trên độ tương đồng ngữ nghĩa để kết nối các chunk liên quan thành các "chuỗi" (snakes) ý tưởng.
- **Tóm tắt đối kháng (Adversarial Summarization):** Sử dụng cơ chế đa tác nhân (multi-agent) trong đó một agent viết tóm tắt và các agent khác đóng vai trò "giáo sư" phản biện dựa trên tài liệu gốc để tinh chỉnh kết quả.

### Lợi ích so với tóm tắt truyền thống
- **Vượt qua giới hạn Token:** Xử lý được tài liệu cực dài bằng cách chia nhỏ.
- **Bảo toàn cấu trúc:** Thấy được các ý tưởng nào được tác giả lặp lại nhiều lần hoặc các khái niệm phụ thuộc lẫn nhau.
- **Khả năng tái xuất (Re-exportability):** Lưu trữ cấu trúc đồ thị thô, cho phép tạo ra nhiều bản tóm tắt khác nhau với các góc nhìn (focus) khác nhau mà không cần chạy lại LLM từ đầu.

## Liên quan
- [[Knowledge Management]]
- [[LLM-based Research]]
- [[Hệ thống phát triển đa tác nhân (Multi-Agent Development System)]]

## Nguồn tham khảo
- [I built an open-source tool to distill books into knowledge graphs](https://dev.to/cookcoco/i-built-an-open-source-tool-to-distill-books-into-knowledge-graphs-fbo)
