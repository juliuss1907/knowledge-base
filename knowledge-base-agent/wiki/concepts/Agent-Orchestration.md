---
type: concept
status: draft
tags: [#ai, #coding]
---

# Điều phối Agent (Agent Orchestration)

## Mô tả
Quá trình quản lý, điều phối và phối hợp hoạt động của một hoặc nhiều AI Agent để thực hiện các tác vụ phức tạp mà một agent đơn lẻ không thể hoàn thành một cách hiệu quả.

## Nội dung chính
- **Multi-Agent Swarms (Đàn Agent)**: Chiến lược triển khai nhiều agent với các vai trò chuyên biệt (ví dụ: một agent nghiên cứu, một agent viết lách, một agent kiểm tra). Các agent tương tác với nhau để cùng đạt được mục tiêu.
- **Autonomous Workflows (Luồng công việc tự trị)**: Xây dựng các pipeline mà trong đó AI tự quyết định bước tiếp theo cần làm, tự phân phối tác vụ cho agent phù hợp và tự kiểm tra kết quả.
- **Cơ chế điều phối (Orchestration Mechanisms)**:
    - **Routing**: Định tuyến task đến agent có kỹ năng phù hợp nhất (ví dụ: SONA routing).
    - **Fallback**: Hệ thống dự phòng khi một agent thất bại trong việc thực hiện task.
    - **Graph-based Management**: Quản lý mối quan hệ và luồng công việc dưới dạng đồ thị (Graph) để theo dõi các cạnh nhân quả (causal edges).
- **Lợi ích**: Tăng độ chính xác, giảm sai sót (do có agent review) và cho phép xử lý các bài toán quy mô lớn hơn.

## Liên quan
- [[Ruflo]]
- [[Agent-native Software]]

## Nguồn tham khảo
- [[src_ruflo]]
