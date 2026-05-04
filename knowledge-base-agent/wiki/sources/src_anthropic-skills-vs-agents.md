---
type: source
source_url: https://www.youtube.com/watch?v=???
date_ingested: 2026-05-03
tags: [#ai]
---

# Skills vs Agents — Tư duy mới trong phát triển AI

Tác giả: Barry Zhang và Mahesh Murag (Anthropic)
Nguồn: YouTube

Nội dung chính:
- Thay đổi tư duy: Từ việc xây dựng nhiều Agent riêng biệt cho từng task sang việc dùng một Agent nền tảng nạp thêm các "gói chuyên môn" (Skills).
- Định nghĩa Skill: Một thư mục chứa tệp tin, scripts và hướng dẫn, cung cấp kiến thức thủ tục (procedural knowledge) cho AI.
- Đặc điểm kỹ thuật: Định dạng thư mục, hỗ trợ scripts tự ghi chép, cơ chế Progressive Disclosure (chỉ đọc sâu khi cần).
- Phân loại Skills: Foundational (khả năng mới), Integration (kết nối công cụ), Enterprise (quy trình nội bộ).
- Kiến trúc 3 lớp:
    1. Agent Loop (Tư duy cốt lõi).
    2. MCP - Model Context Protocol (Kết nối dữ liệu/công cụ).
    3. Skills Library (Tri thức/Chuyên môn).
- Tầm nhìn: AI có khả năng tự tạo Skill từ các tác vụ lặp lại, tạo ra kho lưu trữ kiến thức phát triển không ngừng.
