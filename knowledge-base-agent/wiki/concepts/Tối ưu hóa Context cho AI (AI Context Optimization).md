---
type: concept
status: draft
tags: [#ai, #productivity]
updated: 2026-05-04
---

# Tối ưu hóa Context cho AI (AI Context Optimization)

## Mô tả
Kỹ thuật quản lý luồng thông tin đầu vào (context) cho LLM nhằm tối đa hóa chất lượng output trong khi tối thiểu hóa việc tiêu tốn token và tránh hiện tượng suy giảm trí tuệ do quá tải thông tin (context stuffing).

### 1. Vấn đề của "Context Stuffing"
Nhiều người dùng có xu hướng đưa toàn bộ hướng dẫn, quy tắc và tài liệu vào một file duy nhất (như `agent.md` hoặc `claude.md`) và nạp vào mỗi cuộc hội thoại. Điều này dẫn đến:
- **Lãng phí Token:** Tiêu tốn chi phí và giới hạn context window một cách không cần thiết.
- **Suy giảm độ nhạy:** Khi context quá lớn, AI dễ bị nhiễu, bỏ sót các chi tiết quan trọng hoặc trở nên kém linh hoạt.

### 2. Chiến lược Progressive Disclosure (Tiết lộ dần dần)
Thay vì nạp toàn bộ, hãy sử dụng kiến trúc **Skills** với 3 cấp độ truy xuất:
- **Level 1 (Metadata):** Chỉ tải Tên và Mô tả của tất cả skills khi khởi động. Đóng vai trò như một "Mục lục".
- **Level 2 (Instructions):** Tải toàn bộ nội dung Body của `skill.md` khi yêu cầu của người dùng khớp với mô tả của skill đó.
- **Level 3 (Resources):** Chỉ tải các script, file tham khảo hoặc assets khi tác vụ thực sự đi vào giai đoạn thực thi.
- **Kết quả:** Tiết kiệm token, giữ cho "tư duy" của AI nhạy bén hơn vì chỉ tập trung vào thông tin liên quan.

### 3. Xây dựng Kỹ năng Đệ quy (Recursive Skill Building)
Một quy trình tối ưu hóa context liên tục thông qua 3 bước:
1. **Walkthrough:** Thực hiện tác vụ cùng AI từng bước, chỉnh sửa sai sót và dạy AI cách tư duy đúng cho task đó.
2. **Codification:** Yêu cầu AI xem lại lịch sử hội thoại thành công và tự viết ra file `skill.md` để lưu trữ quy trình.
3. **Recursive Update:** Mỗi khi AI gặp lỗi hoặc tìm ra cách làm tốt hơn $\rightarrow$ cập nhật ngay vào `skill.md`. Điều này biến AI thành một hệ thống tự cải thiện.

### 4. Tư duy Đào tạo "Bottom-up"
Thay vì cài đặt các agent phức tạp có sẵn, hãy:
- Coi AI như một nhân viên mới.
- Đào tạo theo quy trình, "khẩu vị" và chiến lược độc nhất của bạn.
- Xây dựng kỹ năng từ những tác vụ nhỏ nhất, sau đó mở rộng dần.

## Liên quan
- [[Kiến trúc Skills và Agents (Skills vs Agents Architecture)]] — Cách triển khai Progressive Disclosure thông qua thư viện Skills.
- [[Sử dụng AI đúng cách (Using AI Correctly)]] — Việc xây dựng context file là một phần của workflow chuyên gia.

## Nguồn tham khảo
- [[src_gisenberg-ross-ai-agents-skills]] — Tối ưu hóa AI Agents — Greg Isenberg x Ross Mike.
