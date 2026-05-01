---
type: concept
status: draft
tags: [#ai, #coding, #productivity]
---
# Hệ thống phát triển đa tác nhân (Multi-Agent Development System)

## Mô tả
Hệ thống phát triển đa tác nhân là một kiến trúc điều phối nhiều AI agent chuyên biệt để thực hiện các tác vụ phát triển phần mềm phức tạp, nhằm giảm thiểu vấn đề mất ngữ cảnh (context leak) và tăng tốc độ nghiên cứu thông qua xử lý song song.

### Kiến trúc cốt lõi
- **Coordinator Agent:** Đóng vai trò điều phối, không thực thi trực tiếp. Quản lý việc khởi tạo sub-agents, phân phối nhiệm vụ nghiên cứu, thu thập kết quả và định tuyến ngữ cảnh qua các giai đoạn.
- **Sub-agents:** Các tác nhân độc lập, thực hiện các câu hỏi nghiên cứu cụ thể và ghi kết quả ra file.
- **Memory Layer (File-based):** Sử dụng hệ thống file phẳng trên đĩa để lưu trữ kết quả nghiên cứu, bản phác thảo kiến trúc và kế hoạch. Điều này giúp dữ liệu bền vững, có thể kiểm tra và khôi phục sau khi khởi động lại session.

### Quy trình lập kế hoạch (Planning Workflow)
1. **Discovery:** Triển khai song song các agent nghiên cứu về bài học quá khứ (Lesson), trạng thái hiện tại (Current State) và các ràng buộc (Constraints). Thực hiện Gap Analysis để phân loại câu hỏi thành: có thể nghiên cứu (Researchable), cần người dùng quyết định (User Input), hoặc có thể trì hoãn (Deferrable).
2. **Feature Research:** Nghiên cứu sâu vào các khía cạnh cụ thể như tích hợp, bảo mật, hiệu năng.
3. **Planning:** Agent kiến trúc tạo tài liệu tổng thể, sau đó các Phase Planners tạo kế hoạch chi tiết cho từng giai đoạn, bao gồm danh sách task, file cần chỉnh sửa và lệnh xác thực (verification commands).

## Liên quan
- [[AI Agent Coordination]]
- [[Context Management in AI]]

## Nguồn tham khảo
- [How I Built a Multi-Agent Development System That Plans, Executes, and Remembers](https://hackernoon.com/how-i-built-a-multi-agent-development-system-that-plans-executes-and-remembers)
