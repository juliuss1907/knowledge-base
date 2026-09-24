---
type: concept
status: draft
main_tag: ai
sub_tags: [automation, tools, hack]
topic: ai-trading-agent-safety
sources:
  - "[[src_alex-saint-ai-trading-bot-jev-solana]]"
last_updated: 2026-09-24
---

# Mô Hình Quyết Định Được Hiệu Chỉnh

## Definition

Mô hình quyết định được hiệu chỉnh là mô hình xuất probability có ý nghĩa đáng tin cậy, sao cho confidence `0.8` gần với tần suất đúng khoảng 80%. Loại output này biến mức chắc chắn thành tín hiệu vận hành có thể dùng cho threshold, veto và risk review.

## Key ideas

- Structured output như `choice`, `score` và `noul` phù hợp hơn với quyết định tự động vì có outcome rời rạc và dễ audit.
- `noul` cho phép hệ thống từ chối hành động thay vì bắt buộc chọn một hành động không phù hợp.
- Log phải lưu confidence cùng outcome thực tế; nếu không có outcome, calibration và quy trình cải thiện rules không thể được kiểm chứng.
- Rule “high confidence thì act, low confidence thì hold” đơn giản nhưng chỉ an toàn khi calibration thực sự đúng với workload đang chạy.
- Fail-closed behavior phải được cài trước các tính năng khác: API lỗi hoặc confidence không hợp lệ phải dẫn tới `hold`, không dẫn tới phỏng đoán.
- Calibration cần được audit theo thời gian vì drift của market có thể làm confidence cũ không còn phản ánh xác suất thực.

## Related concepts

- [[two-speed-agent-loop]]
- [[wallet-isolation-for-ai-agents]]
- [[ai-trading-agent]]
- [[multi-agent-risk-review]]

## Sources

- [[src_alex-saint-ai-trading-bot-jev-solana]]
