---
type: raw
source_type: article
source_url: https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/
date_ingested: 2026-05-06
tags: [#ai, #coding]
status: processed
processed_date: 2026-05-07
---
# Computer Use is 45x More Expensive Than Structured APIs
**Author:** Reflex  
**Link:** https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/  
**Date:** April 27, 2026
---
## Tóm tắt
Benchmark so sánh **vision agent** (browser-use, computer-use) vs **API agent** (structured HTTP endpoints) trên cùng một admin panel task.
---
## Task
Tìm customer "Smith" có nhiều orders nhất → locate pending order gần nhất → accept tất cả pending reviews → mark order as delivered.
---
## Kết quả
| Metric | Vision agent (Sonnet) | API (Sonnet) | API (Haiku) |
|---|---|---|---|
| **Steps/calls** | 53 ± 13 | 8 ± 0 | 8 ± 0 |
| **Wall-clock time** | ~17 min (1003s) | 19.7s | 7.7s |
| **Input tokens** | 550,976 | 12,151 | 9,478 |
| **Output tokens** | 37,962 | 934 | 819 |
**→ Vision agent đắt hơn ~45x về tokens, ~50x về thờI gian**
---
## Vấn đề với Vision Agent
- **Không hoàn thành task** với prompt đơn giản (6 câu)
- Miss 3/4 pending reviews vì không scroll — không có signal là còn data below fold
- **Cần 14-step walkthrough** chi tiết mới chạy được
- Variance cao: 14-22 min, 400-750k tokens mỗi run
---
## API Agent
- Hoàn thành trong **8 calls** liên tục
- Không variance — same 8 calls mỗi lần
- Đọc structured response trực tiếp từ handlers, không cần interpret pixels
---
## Key Insight
> "Better models will narrow the cost per step. They will not narrow the step count, because the step count is set by the interface."
Vision agent phải **pay for the seeing** — mỗi render = screenshot = thousands of tokens. Better vision models giảm error rate nhưng không giảm số screenshots cần thiết.
---
## When to use what?
| Use case | Recommendation |
|---|---|
| Third-party SaaS, legacy systems | Vision agent |
| Internal tools bạn tự build | **API agent** — math points the other way |
---
## Reflex 0.9
Auto-generates HTTP endpoints từ event handlers → API surface engineering cost ≈ 0.
