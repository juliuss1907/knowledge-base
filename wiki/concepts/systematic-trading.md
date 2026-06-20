---
type: concept
status: draft
main_tag: economic
sub_tags: [tutorial, automation]
topic: trading-methodology
sources:
  - "[[src_the-cost-of-discretion]]"
last_updated: 2026-06-17
---

# Systematic Trading

## Definition

Phương pháp giao dịch sử dụng rules-based systems để tạo tín hiệu vào lệnh, quản lý vị thế, và thoát lệnh mà không cần can thiệp discretionary của trader. Mục tiêu là loại bỏ con ngưởi khỏi execution loop để tránh cognitive biases.

## Key ideas

- Không phải systematic luôn lợi nhuận hơn discretionary về raw return
- Case cho systematic: capacity, reproducibility, ability to run multiple uncorrelated strategies simultaneously
- Discretionary trader profitable với 1 strategy sẽ struggle với 5. Systematic trader có thể chạy 25 strategies
- 4 cognitive holes không thể discipline ra khỏi: loss aversion, recency bias, confirmation bias, sunk cost
- "Good discretionary day" nguy hiểm nhất: dạy bạn phiên bản "tốt" của mình là thật, nhưng variance trong performance ngày-đêm lớn hơn variance của strategy
- Workflow xây dựng: backtest → walk-forward → Monte Carlo → paper/micro-live 3 tháng → scale
- Hardest part: trusting system through drawdown mà model nói là within tolerance
- Trade-off: engagement + agency + simplicity đổi lấy capacity

## Related concepts

- [[discretionary-vs-systematic-trading]]
- [[trading-cognitive-biases]]
- [[walk-forward-analysis]]
- [[monte-carlo-simulation]]

## Sources

- [[src_the-cost-of-discretion]]

## Notes
