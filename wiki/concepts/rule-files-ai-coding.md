---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tutorial, tools]
topic: rule-files-ai-coding
sources: ["[[src_ultimate-guide-rule-files-ai-coding]]"]
last_updated: 2026-11-22
---

# Rule Files for AI Coding

## Definition

Rule files for AI coding là các tài liệu hướng dẫn coding agent theo conventions và giới hạn thực tế của dự án, được nạp theo cơ chế và phạm vi của từng công cụ. Tài liệu trong repository thường nên được quản lý phiên bản; hướng dẫn ở thư mục người dùng hoặc theo module có thể có phạm vi và cách nạp khác. Chúng biến kiến thức vận hành lặp lại thành context có thể tái sử dụng giữa các phiên làm việc.

## Key ideas

- Nội dung cốt lõi gồm commands, cấu trúc dự án, stack có phiên bản, code examples, Git workflow và boundaries.
- Ví dụ đúng và các lệnh có thể chạy được giảm suy đoán hiệu quả hơn chỉ dẫn chung chung.
- Quy tắc nên được thêm sau các sự cố hoặc friction thật để tạo institutional knowledge có ích.
- Tài liệu phải ngắn gọn vì mọi token persistent đều cạnh tranh với context của tác vụ hiện tại.
- Phân tầng rules theo global, repository và module giúp giữ hướng dẫn cục bộ mà không làm file gốc phình to.

## Related concepts

- [[context-engineering]]
- [[agentic-coding]]
- [[agent-skill-management]]

## Sources

- [[src_ultimate-guide-rule-files-ai-coding]]
