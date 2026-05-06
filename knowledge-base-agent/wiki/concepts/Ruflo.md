---
type: concept
status: draft
tags: [#ai, #coding]
---

# Ruflo

## Mô tả
Một nền tảng orchestration (điều phối) dành cho các AI Agent, đặc biệt tối ưu cho hệ sinh thái Claude. Ruflo cho phép xây dựng các hệ thống đa tác nhân (multi-agent swarms) để thực hiện các luồng công việc phức tạp và tự trị.

## Nội dung chính
- **Agent Swarms**: Thay vì dùng một agent đơn lẻ, Ruflo cho phép triển khai một "đàn" agent, trong đó mỗi agent có vai trò chuyên biệt và phối hợp với nhau để hoàn thành mục tiêu.
- **Autonomous Workflows**: Khả năng tự thiết lập và điều phối pipeline công việc mà không cần sự can thiệp chi tiết của con người.
- **Khả năng tích hợp**: Tương thích hoàn toàn với Claude Code, Codex và giao thức MCP (Model Context Protocol), tạo ra một hệ sinh thái mở cho các plugin.
- **Kiến trúc nâng cao**: 
    - Sử dụng **Graph-node records** để quản lý mối quan hệ giữa các agent và các cạnh nhân quả (causal edges).
    - Hệ thống routing **SONA** với fallback 5 tầng đảm bảo độ tin cậy cao trong việc điều phối tác vụ.
- **Hệ thống tự học**: Tích hợp khả năng tự cải thiện (self-improving) cho các agent thông qua vòng lặp feedback.

## Liên quan
- [[Agent Orchestration]]
- [[Agent-native Software]]

## Nguồn tham khảo
- [[src_ruflo]]
