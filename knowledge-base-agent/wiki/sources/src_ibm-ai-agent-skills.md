---
type: source
source_url: https://www.youtube.com/watch?v=Lg-meK5IU8Q
date_ingested: 2026-05-03
tags: [#ai]
---

# Kỹ năng của Đại lý AI (AI Agent Skills) — IBM Technology

Nguồn: YouTube (IBM Technology)

Nội dung chính:
- Khái niệm: Skills cung cấp "kiến thức thủ tục" (procedural knowledge) cho AI agents, lấp đầy khoảng trống mà các LLM (với kiến thức sự thật) không có.
- Cấu trúc Skill: Thư mục chứa `skill.md` (YAML Front Matter với Name/Description), `scripts/`, `references/`, `assets/`.
- Cơ chế Tiết lộ Dần dần (Progressive Disclosure) 3 cấp độ:
    1. Metadata (Tên/Mô tả) $\rightarrow$ Tải lúc khởi động.
    2. Instructions (Body `skill.md`) $\rightarrow$ Tải khi khớp mô tả.
    3. Resources (Scripts/Files) $\rightarrow$ Tải khi thực sự cần thực hiện.
- So sánh:
    - MCP: Cung cấp công cụ, nhưng không dạy cách/khi nào dùng.
    - RAG: Cung cấp dữ kiện/sự thật, không cung cấp cách làm.
    - Fine-tuning: Tốn kém, khó thay đổi.
- Tiêu chuẩn mở: định dạng `skill.md` (agentskills.io) cho phép chia sẻ kỹ năng giữa các nền tảng AI khác nhau.
- Cảnh báo bảo mật: Cần kiểm tra mã nguồn của scripts trong skills để tránh mã độc.
