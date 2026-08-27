---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, automation]
topic: batch-vs-live-inference
sources:
  - "[[src_10-questions-for-your-startup-developers]]"
last_updated: 2026-08-27
---

# Batch vs Live Inference

## Definition

Phân loại workload AI thành live inference (người dùng phải thấy kết quả ngay lập tức) và batch prediction (có thể chờ, gửi khi xong). Đa số workload của startup thực chất là batch giả danh real-time — chuyển chúng khỏi interactive path là đòn bẩy cao nhất để tăng throughput mà không tốn DSQ.

## Key ideas

- **Ba câu hỏi phân loại traffic:**
  - Người dùng phải thấy kết quả trong một giây? → Live inference
  - Chờ vài giây + spinner OK? → Live, nhưng ứng viên cho streaming
  - Chấp nhận "email khi xong"? → Batch prediction
- **Batch prediction chạy trong queue riêng** — không tiêu thụ interactive DSQ, giá ~50% of on-demand inference
- **Ứng viên batch điển hình:** nightly document summarization, background classification signup mới, bulk translation, embedding backfills, evaluation runs trên test set
- **Đòn bẩy ngay lập tức:** đây thường là thay đổi value cao nhất có thể làm trong tuần

## Related concepts

- [[dynamic-shared-quota]]
- [[llm-consumption-modes]]

## Sources

- [[src_10-questions-for-your-startup-developers]]

