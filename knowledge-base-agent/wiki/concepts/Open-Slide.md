---
type: concept
status: draft
tags: [#ai, #coding]
---

# Open Slide

## Mô tả
Một framework xây dựng slide (presentation) được thiết kế hướng tới AI Agent (Agent-native), cho phép các agent tự động tạo ra nội dung và cấu trúc bài thuyết trình một cách hiệu quả.

## Nội dung chính
- **Agent-native Design**: Thay vì chỉ là công cụ cho con người, Open Slide cung cấp các điểm chạm cho AI như:
    - **Hệ thống Skills**: Các skill modular giúp agent hiểu cách tạo slide, chọn theme và sắp xếp nội dung.
    - **Chuẩn AGENTS.md**: Sử dụng một file hướng dẫn chung cho tất cả các agent tham gia vào project thay vì các file config riêng lẻ cho từng model.
- **Công cụ hỗ trợ**:
    - **CLI `openslide`**: Cho phép khởi tạo nhanh một deck workspace từ template.
    - **Monorepo Architecture**: Sử dụng Turborepo và pnpm để quản lý các package CLI và playground một cách tách biệt.
- **Giá trị**: Giảm thiểu rào cản giữa việc lên ý tưởng (prompting) và tạo ra kết quả cuối cùng (slide) bằng cách cung cấp một môi trường mà agent có thể tự vận hành.

## Liên quan
- [[Agent-native Software]]
- [[AI-Workflow-Automation]]

## Nguồn tham khảo
- [[src_open-slide]]
