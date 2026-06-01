---
type: concept
status: draft
main_tag: economic
sub_tags: [research, tools]
topic: trading-risk-management
sources:
  - "[[src_no-system-will-make-you-profitable]]"
last_updated: 2026-05-29
---

# Sizing Policy (Trading)

## Definition

Kích thước vị thế (sizing) là biểu hiện của việc hiểu trade đến mức nào. Công thức trực giác: size ∝ edge / variance. Không phải "long" hay "short" — mà là bao nhiêu, từ đâu, với stop nào, trong volatility nào.

## Key ideas

- **Các yếu tố giảm size:** vol cao, cost cao, liquidity thấp, drawdown sâu, correlation cao, độ tin cậy của edge thấp
- **Kelly criterion:** Full Kelly là theoretically optimal nhưng trong trading "dirty game" — thường scale xuống half Kelly, quarter Kelly, volatility targeting
- **Oversize risk:** Một trade oversize có thể giết chết cả 3 trade sạch tiếp theo vì drawdown và mất risk budget

## Related concepts

- [[trading-policy-pi]]
- [[state-conditioned-decisions]]

## Sources

- [[src_no-system-will-make-you-profitable]]

## Notes

