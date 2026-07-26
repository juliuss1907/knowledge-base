---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: agent-backtesting
sources:
  - "[[src_introducing-backsearch-gr-inc.md]]"
last_updated: 2026-07-26
---

# Agent Backtesting

## Definition

Agent Backtesting là phương pháp đánh giá performance của AI agents bằng cách chạy chúng trên dữ liệu lịch sử — nơi kết quả cuối cùng đã biết — để kiểm tra khả năng dự đoán và ra quyết định. Khác với live evaluation, backtesting cho phép reproducible assessment và comparison giữa các agent versions.

## Key ideas

- **Reproducible evaluation**: Cùng một test trên cùng một data sẽ cho kết quả nhất quán
- **Known outcomes**: Chạy agent trên quá khứ nơi "future" đã được reveal, cho phép objective scoring
- **Strategy validation**: Quant finance sử dụng để backtest trading strategies trước khi deploy
- **Controlled environment**: Có thể fix external variables để isolate agent's decision-making
- **Time-stepped simulation**: Duyệt qua historical timeline step-by-step để simulate real-time decision making
- **Risk-free testing**: Test strategies mà không risk real capital hoặc real-world consequences

## Challenges

- **Data leakage prevention**: Đảm bảo agent không access information from the "future"
- **Look-ahead bias**: Tránh situations nơi strategy dùng information không available tại thời điểm quyết định
- **Overfitting**: Agent optimize quá mức cho historical data mà không generalize cho future
- **Changing market regimes**: Historical performance không guarantee future results

## Related concepts

- [[frozen-corpus-search]]
- [[point-in-time-data]]
- [[quantitative-finance]]
- [[reinforcement-learning-environments]]

## Sources

- [[src_introducing-backsearch-gr-inc.md]] — BackSearch cung cấp frozen web corpus cho agent backtesting

## Notes

