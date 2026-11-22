---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools, automation]
topic: pstack-agent-workflow
sources: ["[[src_pstack-cursor-engineer-ships-code-with-ai]]"]
last_updated: 2026-11-21
---

# Pstack Agent Workflow

## Definition

Pstack agent workflow là cách tổ chức skills cho toàn bộ vòng đời phát triển phần mềm với AI, từ hiểu codebase, thiết kế, xây dựng và verification đến giao PR. Workflow coi skills là các năng lực chuyên biệt được gọi theo ngữ cảnh thay vì gom mọi quy tắc vào một prompt thường trực.

## Key ideas

- Học “how” và “why” của codebase trước khi lập kế hoạch làm giảm quyết định dựa trên giả định.
- Thiết kế có thể fan-out sang nhiều model, rồi dùng một bước phản biện để tổng hợp ưu điểm của từng phương án.
- TDD, lint và cleanup diff biến tiêu chuẩn chất lượng thành các bước lặp lại được.
- Verification end-to-end phải bao gồm môi trường, thao tác người dùng, bằng chứng và cleanup.
- Skills nhỏ, có index kích hoạt, tránh làm system prompt phình to và tiêu tốn context cho quy tắc không liên quan.

## Related concepts

- [[agentic-coding]]
- [[agent-skill-management]]
- [[plan-execute-verify-loop]]

## Sources

- [[src_pstack-cursor-engineer-ships-code-with-ai]]

