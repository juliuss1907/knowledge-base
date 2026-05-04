---
type: concept
status: draft
tags: [#ai]
updated: 2026-05-04
---

# Kiến trúc Skills và Agents (Skills vs Agents Architecture)

## Mô tả
Một mô hình kiến trúc mới trong phát triển AI, chuyển dịch từ việc tạo ra nhiều tác nhân (agents) chuyên biệt sang việc sử dụng một tác nhân nền tảng (Foundational Agent) kết hợp với một thư viện các kỹ năng (Skills Library) có thể nạp vào linh hoạt.

### 1. Vấn đề của Cách tiếp cận Multi-Agent truyền thống
Việc xây dựng một agent riêng cho mỗi nhiệm vụ gây ra các vấn đề:
- **Lãng phí nguồn lực:** Mỗi agent cần được thiết lập và quản lý riêng.
- **Khó bảo trì:** Thay đổi quy trình yêu cầu cập nhật nhiều agent khác nhau.
- **Thiếu nhất quán:** Khó đồng bộ hóa tri thức giữa các agent.

### 2. Định nghĩa và Đặc điểm của "Skills"
Một **Skill** không phải là một prompt đơn lẻ, mà là một "gói chuyên môn" (expertise package). Nó cung cấp **Kiến thức thủ tục (Procedural Knowledge)** — tức là hướng dẫn chi tiết về *cách thực hiện* một quy trình cụ thể, điều mà các LLM thường thiếu dù có nhiều kiến thức sự thật.

**Cấu trúc một Skill:**
- **Định dạng:** Là một thư mục (folder) chứa:
    - `skill.md`: Tệp trung tâm với YAML frontmatter (Name, Description) và Body (hướng dẫn chi tiết).
    - `scripts/`: Mã thực thi (JS, Python, Bash) để tự động hóa tác vụ.
    - `references/`: Tài liệu tham khảo bổ sung.
    - `assets/`: Các tệp tĩnh, templates.
- **Progressive Disclosure:** AI chỉ đọc metadata của skill khi khởi động; chỉ khi nhiệm vụ yêu cầu, nó mới truy xuất sâu vào nội dung chi tiết để tiết kiệm token và tránh nhiễu.
- **Quy trình xây dựng (Walkthrough $\rightarrow$ Codify):** Skills hiệu quả nhất không phải do viết sẵn mà được tạo ra bằng cách hướng dẫn AI làm từng bước $\rightarrow$ sửa lỗi $\rightarrow$ yêu cầu AI tự viết lại quy trình thành file `skill.md`.

### 3. Kiến trúc 3 Lớp (The 3-Layer Architecture)
Để vận hành hiệu quả, hệ thống AI được chia thành 3 lớp:
1. **Agent Loop (Lớp Tư duy):** Vòng lặp suy luận cốt lõi, chịu trách nhiệm lập kế hoạch và ra quyết định.
2. **MCP - Model Context Protocol (Lớp Kết nối):** Giao thức tiêu chuẩn để kết nối AI với dữ liệu và công cụ thế giới thực (ví dụ: DB, Browser, API).
3. **Skills Library (Lớp Chuyên môn):** Kho lưu trữ các gói kỹ năng giúp AI thực hiện các tác vụ phức tạp một cách nhất quán và chính xác.

### 4. Phân loại Skills
- **Foundational Skills:** Mở rộng khả năng cơ bản (ví dụ: phân tích dữ liệu sinh học, tạo báo cáo tài chính).
- **Integration Skills:** Tối ưu hóa việc sử dụng công cụ bên thứ ba (ví dụ: Notion, GitHub).
- **Enterprise Skills:** Mã hóa quy trình vận hành nội bộ (SOP) của một tổ chức vào AI.

### 5. Tầm nhìn về AI Tự học (Self-Evolving AI)
Trong tương lai, AI có thể tự động hóa việc tạo skill: khi phát hiện một mẫu công việc lặp lại, AI sẽ tự viết hướng dẫn và lưu lại thành một Skill mới trong thư viện, biến kinh nghiệm thành tài sản tri thức vĩnh viễn của tổ chức.

### 6. So sánh với các phương pháp khác

| Công nghệ | Chức năng chính | Điểm yếu so với Skills |
|---|---|---|
| **MCP** | Kết nối API/Công cụ | Cung cấp "tay" nhưng không dạy "cách/khi nào" dùng |
| **RAG** | Truy xuất dữ kiện/sự thật | Cung cấp "kiến thức" nhưng không cung cấp "quy trình" |
| **Fine-tuning** | Tích hợp vào trọng số model | Chi phí cao, khó cập nhật nhanh |
| **Skills** | Cung cấp kiến thức thủ tục | Linh hoạt, dễ cập nhật, có thể chia sẻ |

### 7. Tiêu chuẩn mở và Bảo mật
- **Tiêu chuẩn:** Định dạng `skill.md` (theo agentskills.io) hướng tới việc trở thành tiêu chuẩn mở, cho phép một skill tạo cho nền tảng này (vd: Claude Code) có thể hoạt động trên nền tảng khác.
- **Bảo mật:** Do skills có thể chứa mã thực thi (`scripts/`), người dùng cần kiểm tra mã nguồn trước khi cài đặt để tránh mã độc hoặc prompt injection.

## Liên quan
- [[mcp-vs-skills]] — So sánh giữa giao thức kết nối MCP và các gói kỹ năng Skills.
- [[Tối ưu hóa Claude (Claude Optimization)]] — Việc sử dụng `skill-creator` là một phần của tối ưu hóa Claude.

## Nguồn tham khảo
- [[src_anthropic-skills-vs-agents]] — Skills vs Agents — Tư duy mới trong phát triển AI.
- [[src_ibm-ai-agent-skills]] — Kỹ năng của Đại lý AI (AI Agent Skills) — IBM Technology.
