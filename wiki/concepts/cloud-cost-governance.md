---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, hack, system]
topic: cloud-cost-governance
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# Cloud Cost Governance

## Definition

Hệ thống các lớp kiểm soát chi phí cloud để ngăn không cho hóa đơn chạy khỏi tầm tay — đặc biệt trong bối cảnh AI, nơi key bị lộ có thể tích lũy hàng chục nghìn đô trong 48 giờ. Nguyên lý cốt lõi: budgets chỉ thông báo, bạn phải tự xây phanh.

## Key ideas

- **Ba lớp spend control (nên dùng như các lớp xếp tầng):**
  1. **Spend cap budget (Preview)** — Cloud Billing budget thực thi thay vì chỉ email. Chạm 100% budget → Google tạm dừng service tới khi lift thủ công. Alert vẫn bắn ở 50%/80%. Một cap cover một project + một eligible service; enforcement dựa trên ước tính, không tức thì — nên đặt dưới ceiling thật; đang Preview, danh sách service tăng dần
  2. **Billing budget + Pub/Sub trigger tắt billing** — khi budget chạm ngưỡng, Pub/Sub bắn Cloud Function detach billing account. Mạnh hơn nhưng nguy hiểm hơn — có thể để lại resource unrecoverable — nên dùng thứ hai. Giới hạn scope bằng `--filter-projects` (nếu không áp dụng cả billing account), deploy function trong cùng project cần bảo vệ
  3. **Quota overrides** — cap cơ học cost tích lũy bằng cách đặt per-model, per-region quota dưới default. Key lộ không thể burn thứ quota từ chối phục vụ
- **Hai cách hiểu hệ quả tài chính:** Shared Responsibility Model của Google — khách hàng chịu trách nhiệm chi phí phát sinh từ credential hợp lệ của họ
- **Traffic shape quan trọng:** thứ tự dùng đúng các consumption mode (xem [[llm-consumption-modes]]) là nền của govern — đo p50/p99 TPM trước khi cam kết capacity

## Related concepts

- [[llm-consumption-modes]]
- [[dynamic-shared-quota]]
- [[secrets-management]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

## Notes

