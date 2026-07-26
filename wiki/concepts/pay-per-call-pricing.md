---
type: concept
status: draft
main_tag: economic
sub_tags: [tools, automation]
topic: ai-agent-tool-platform
sources:
  - "[[src_monid-ai-agent-tool-platform.md]]"
last_updated: 2026-07-26
---

# Pay-per-call Pricing

## Definition

Pay-per-call Pricing là mô hình định giá dịch vụ theo đó ngườ dùng chỉ trả tiền cho mỗi lần thực sự gọi API hoặc sử dụng service, thay v thanh toán subscription fee cố định hàng tháng. Mô hình này đặc biệt phù hợp cho AI agents và automated workflows có usage pattern thất thường.

## Key ideas

- **Usage-based billing**: Chi phí tỷ lệ thuận với số lượng calls thực tế, không có flat fees
- **No minimum commitments**: Không yêu cầu cam kết sử dụng tối thiểu
- **Cost predictability**: Dễ dàng tính toán cost per operation cho budgeting
- **Scalability**: Tự động scale theo demand mà không cần upgrade/downgrade plans
- **Reduced waste**: Không trả tiền cho capacity không sử dụng trong tháng
- **Per-call granularity**: Định giá chi tiết đến từng API call ($0.0013/call trong ví dụ Monid)

## Trade-offs

| Pros | Cons |
|------|------|
| Chi phí thấp cho low-volume usage | Có thể expensive hơn subscription cho high-volume |
| Không cần quản lý nhiều subscriptions | Harder to predict monthly bills |
| Perfect cho sporadic agent workflows | No volume discounts tự động |

## Related concepts

- [[usage-based-pricing]]
- [[api-economics]]
- [[serverless-pricing]]

## Sources

- [[src_monid-ai-agent-tool-platform.md]] — Monid sử dụng mô hình $0.0013 per call, balance-based billing

## Notes

