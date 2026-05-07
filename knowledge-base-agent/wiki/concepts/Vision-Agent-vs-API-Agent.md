---
type: concept
status: draft
tags: [#ai, #coding]
related_concepts: ["Hạ tầng cho Computer-Use Agents (Infrastructure for Computer-Use Agents)"]
sources: ["src_computer-use-45x-expensive"]
compiled_date: 2026-05-07
---

# Vision Agent vs API Agent — Cost Comparison

## Mô tả

Benchmark so sánh **vision agent** (browser-use, computer-use) với **API agent** (structured HTTP endpoints). Vision agent đắt hơn ~45x về tokens, ~50x về thời gian trên cùng task.

## Kết quả Benchmark

| Metric | Vision agent | API agent |
|---|---|---|
| Steps/calls | 53 ± 13 | 8 ± 0 |
| Wall-clock time | ~17 min (1003s) | 7.7-19.7s |
| Input tokens | 550,976 | 9,478 |

## Key Insight

> "Better models will narrow the cost per step. They will not narrow the step count, because the step count is set by the interface."

Vision agent phải **pay for the seeing** — mỗi render = screenshot = thousands of tokens.

## When to use what?

| Use case | Recommendation |
|---|---|
| Third-party SaaS, legacy systems | Vision agent |
| Internal tools bạn tự build | **API agent** |

## Liên quan

- [[Hạ tầng cho Computer-Use Agents (Infrastructure for Computer-Use Agents)]]

## Nguồn tham khảo

- Reflex (https://reflex.dev)