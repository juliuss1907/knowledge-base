---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: harness-engineering-ai-coding
sources:
  - "[[src_harness-engineering-ai-coding]]"
last_updated: 2026-09-12
---

# Context Engineering

## Definition

Context engineering là discipline đảm bảo AI coding assistant biết đủ thông tin cần thiết để tạo code chính xác — bao gồm stack, architectural decisions, naming conventions, constraints, và rationale đằng sau mỗi quyết định. Đây là thành phần đầu tiên và quan trọng nhất của harness engineering: AI chỉ có thể làm tốt trong phạm vi những gì nó biết.

## Key ideas

- **Context document ≠ README:** HARNESS.md là knowledge base cho AI, không phải README cho humans. README explains what project does; context doc tells AI what it must/must not do and why. Hai tài liệu này có audiences và update rhythms khác nhau.
- **Nội dung cần capture:** tech stack (libraries, frameworks, tools), architectural decisions và rationale, naming conventions, security constraints, structural rules, patterns cần follow.
- **Consequence of missing context:** Nếu AI không biết project dùng logging library nào, nó sẽ tự invent approach riêng. Nếu không biết team never use mutable global state, nó sẽ dùng khi convenient. Nếu không biết DB writes phải qua abstraction layer, nó sẽ bypass.
- **Giảm vi phạm nhưng không eliminate:** Context engineering giảm architectural constraint violations vì AI có thêm thông tin. Tuy nhiên, AI là probabilistic system optimising cho plausibility, không phải rule-following machine — vi phạm vẫn xảy ra và cần enforcement mechanisms bổ sung.
- **Accuracy và currency requirements:** Document cần accurate, specific, và được keep current. Nếu outdated thì worse than nothing — AI sẽ follow stale rules.

## Related concepts

- [[harness-engineering]]
- [[progressive-hardening]]
- [[agentic-coding]]
- [[agent-skill-management]]

## Sources

- "[[src_harness-engineering-ai-coding]]"

## Notes
