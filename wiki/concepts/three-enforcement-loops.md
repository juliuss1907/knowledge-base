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

# Three Enforcement Loops

## Definition

Ba enforcement loops là khung phân loại các cơ chế kiểm soát trong harness engineering, phân chia theo thời điểm và mức độ nghiêm trọng trong development workflow. Mỗi loop phục vụ mục đích riêng: inner loop optimize cho low friction, middle loop có quyền block merge, outer loop producing reports thay vì blocks.

## Key ideas

- **Inner loop (advisory, edit-time):** Lightweight checks chạy trên file save hoặc session completion. Optimized cho low friction — làm problems visible early mà không stop work. Mục đích: early warning system.
- **Middle loop (strict, PR-time):** Full suite deterministic và agent-based checks chạy trên pull request. Có quyền block merge — đây là main enforcement point cho architectural constraints. Level of authority cao nhất trong ba loops.
- **Outer loop (investigative, scheduled):** Garbage collection rules, fitness functions, harness audits chạy theo schedule (daily/weekly). Produces reports thay vì blocks. Findings feed back vào harness như potential new constraints — không block immediate work nhưng phát hiện accumulating problems trước khi serious.
- **Bounded trust principle:** Agent operates trong ba loops đều với bounded trust — không có unilateral authority modify production code hay merge changes. Agents review, suggest, report, flag; humans decide.
- **Feedback loop giữa loops:** Outer loop findings → new constraints → middle loop enforcement → inner loop visibility. Tạo hệ thống self-reinforcing where early detection feeds stronger enforcement.

## Related concepts

- [[harness-engineering]]
- [[progressive-hardening]]
- [[context-engineering]]

## Sources

- "[[src_harness-engineering-ai-coding]]"

## Notes
