---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, productivity]
topic: ai-coding-context-handoff
sources:
  - "[[src_handoff-skill-context-window-management]]"
last_updated: 2026-06-03
---

# Compact vs Handoff

## Definition

So sánh hai chiến lược quản lý context window trong AI coding agents: **Compact** (tóm tắt toàn bộ conversation hiện tại rồi reset) và **Handoff** (tách một phần context cụ thể sang session riêng). Handoff được đánh giá cao hơn cho việc duy trì chất lượng và tổ chức công việc.

## Key ideas

**Compact:**
- Tóm tắt conversation → reset context
- Vẫn là 1 session, tích lũy "sediment" (dư thừa từ các lần compact trước)
- Dễ bị "dumb zone" khi session dài

**Handoff:**
- Tách specific context (1 bug, 1 feature) sang session riêng
- Session gốc giữ sạch, không bị nhiễu
- Nhiều session tập trung thay vì 1 session dài bloat
- Cho phép cross-agent workflow

**Ưu điểm của Handoff:**
- Giữ main flow clean
- Scope rõ ràng cho từng session
- Dễ dàng handoff giữa các agents khác nhau
- Tránh accumulation của "sediment"

## Related concepts

- [[handoff-skill]]
- [[context-window-management]]
- [[session-separation]]

## Sources

- [[src_handoff-skill-context-window-management]]

## Notes
