---
type: concept
status: draft
tags: [#ai, #research]
updated: 2026-05-04
---

# Phát hiện văn bản AI (AI Text Detection)

## Mô tả
Phân tích về khả năng và giới hạn của việc phát hiện văn bản do AI tạo ra. Kết luận chính là việc phát hiện văn bản AI thông qua phân tích thống kê là bất khả thi về mặt toán học khi các mô hình ngôn ngữ lớn (LLM) ngày càng hoàn thiện.

### 1. Sự thất bại của AI Detectors
- **Hiện trạng:** Các công cụ detector (như ZeroGPT) thường xuyên đưa ra kết quả sai (False Positive). Ví dụ: Hiến pháp Hoa Kỳ hoặc Kinh Thánh bị đánh giá là AI-generated với tỷ lệ trên 90%.
- **Nguyên nhân:** LLM được huấn luyện với mục tiêu tạo ra văn bản không thể phân biệt được với con người.

### 2. Ràng buộc Toán học (The Mathematical Constraint)
- **KL Divergence:** Quá trình training LLM tập trung vào việc giảm thiểu *Kullback-Leibler (KL) divergence* giữa phân phối xác suất của model và phân phối của dữ liệu thực (con người).
- **Chuỗi tác động:** $\text{Training giảm KL divergence} \rightarrow \text{Giảm Total Variation} \rightarrow \text{Giảm Detection Accuracy}$.
- **Kết quả:** Khi model càng tốt, độ chính xác của detector sẽ tiến dần về mức 50% (tương đương với việc tung đồng xu ngẫu nhiên).

### 3. Scaling Laws & Phong cách viết
- **Scaling Laws:** Khi kích thước model tăng, KL divergence giảm theo quy luật lũy thừa (power law), khiến khoảng cách giữa detector và sự ngẫu nhiên thu hẹp lại.
- **Phong cách (Style):** Phong cách viết thực chất là các đặc trưng thống kê (statistical features). Nếu phân phối của model khớp với con người, mọi phân tích phong cách (stylometric analysis) đều sẽ thất bại.

### 4. Giải pháp Watermarking
- **Định nghĩa:** Phương pháp nhúng các tín hiệu ẩn (cryptographic signals) vào quá trình chọn token của model.
- **Điều kiện:** Chỉ khả thi nếu công ty phát triển AI chủ động thực hiện từ đầu; không thể phát hiện bằng công cụ bên thứ ba sau khi văn bản đã được tạo ra.

## Liên quan
- [[tokenmaxxing]] — Cách tối ưu token có thể ảnh hưởng đến đặc trưng thống kê của văn bản.
- [[ai-editorial-policy.md]] — Chính sách biên tập AI trong bối cảnh không thể phát hiện AI text.

## Nguồn tham khảo
- [[src_ai-detection-impossible]] — AI Learned to Write Like You. Detection is Mathematically Impossible.
