---
type: source
original: "[[2026-06-16_loop-native-factory]]"
main_tag: ai
sub_tags: [tools, vibecode, research]
topic: loop-native-factory
date_compiled: 2026-06-17
url: https://bitsquarks.substack.com/p/loop-native-factory
author: bitsquarks
---

# Loop Native Factory

## Metadata

- **Author:** bitsquarks
- **Published:** June 16, 2026
- **Source:** Substack
- **URL:** https://bitsquarks.substack.com/p/loop-native-factory
- **Type:** Article

## Summary

Bài viết phân tích sự chuyển dịch cơ bản trong sản xuất phần mềm: từ "keystroke" sang "loop" là đơn vị nguyên tử của công việc. Tác giả truy nguyên lịch sử từ software factory thập niên 1970 qua Agile, DevOps, SRE đến platform engineering, và chỉ ra rằng đơn vị sản xuất cuối cùng đã thay đổi. Loop được định nghĩa là: model chạy trong harness, với tools, trong context, dưới policy, cho đến khi verifier kết thúc công việc. Bài viết phân tích 3 planes của loop-native factory (inner loop, outer loop, governance plane) và 8 modules cấu thành, đồng thời chỉ ra alignment là bottleneck mới thay vì viết code.

## Key points

- Software factory 1970s (Hitachi, Toshiba) chuẩn hóa process. Loop-native factory 2026 chuẩn hóa loop
- Đơn vị sản xuất đã thay đổi: từ developer viết code → loop là đơn vị nguyên tử
- Loop = model + harness + tools + context + policy + verifier. 6 primitives: spec, context, tools, verifier, memory, policy
- 3 planes: inner loop (IDE, local sandbox), outer loop (PR queue, CI/CD, multi-agent review), governance plane (policy, evals, telemetry)
- 8 modules: Spec, Loop Runtime, Context Plane, Verifier Bank, Policy Plane, Memory Layer, Delivery Loop, Governance Graph
- Cognition's pattern: single-threaded writes, multi-agent intelligence around the writer
- Claude Code: ~1.6% codebase là AI decision logic, 98.4% là operational infrastructure (sandboxing, hooks, permission classifiers)
- Alignment = sự hội tụ của systems, people, documents, code vào cùng understanding của "what should happen and why"
- 5 layers of alignment: ontological, teleological, behavioral, temporal, reflexive
- Các hệ thống AI trong production 95% không có ROI đo được sau 12 tháng vì thiếu governance plane

## Concepts referenced

- [[loop-native-factory]]
- [[alignment-engineering]]
- [[agent-harness]]
- [[cognition-multi-agent-pattern]]
- [[three-plane-architecture]]

## Original excerpts

> "The 1970s software factory standardized the process. The 2026 factory standardizes the loop."

> "The gap, between generation and rightness, is the most expensive gap in software."

> "When the loop becomes the atomic unit, three things change at once: (1) The unit of production stops being deterministic, (2) The marginal cost of generation collapses, (3) The scaffolding gets absorbed by the model on every release."

> "The bottleneck has shifted. It is no longer writing code. It is knowing what code to write, and why."

> "Alignment is the convergence of multiple systems, people, documents, and code, onto the same understanding of what should happen and why."
