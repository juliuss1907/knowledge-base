---
type: concept
status: draft
tags: [#ai, #coding]
---

# Phần mềm hướng Agent (Agent-native Software)

## Mô tả
Một triết lý thiết kế phần mềm trong đó ứng dụng không chỉ tập trung vào trải nghiệm người dùng (UX) mà còn tập trung vào trải nghiệm của AI Agent (AX - Agent Experience), cho phép AI dễ dàng hiểu, vận hành và tương tác với hệ thống.

## Nội dung chính
- **Đặc điểm của phần mềm Agent-native**:
    - **Skills-first**: Cung cấp các bộ kỹ năng (Skills) dưới dạng tài liệu hoặc code mà AI có thể tự đọc và áp dụng.
    - **Chuẩn hóa Context**: Sử dụng các file như `AGENTS.md` hoặc `SYSTEM_RULES.md` để cung cấp ngữ cảnh và quy tắc vận hành cho AI.
    - **CLI-centric**: Ưu tiên các công cụ dòng lệnh (CLI) vì AI tương tác với terminal hiệu quả hơn giao diện đồ họa (GUI).
    - **Structured Outputs**: Ưu tiên các định dạng dữ liệu mà AI dễ xử lý (Markdown, JSON, YAML) thay vì các định dạng đóng.
- **Ví dụ điển hình**:
    - **Open Slide**: Framework tạo slide cung cấp sẵn skills cho agent và CLI để scaffold project.
    - **OpenClaw**: Hệ thống vận hành agent với các skills chuyên biệt và quản lý memory.

## Liên quan
- [[Open-Slide]]
- [[AI-Workflow-Automation]]

## Nguồn tham khảo
- [[src_open-slide]]
