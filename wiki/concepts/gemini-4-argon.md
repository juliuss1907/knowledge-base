---
type: concept
status: draft
main_tag: ai
sub_tags: [news, research, strategy]
topic: gemini-4-argon
sources:
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# Gemini 4 Argon

## Definition

Gemini 4 Argon là flagship model tiếp theo của Google, được tung ra sau khoảng 7 tháng kể từ lần công bố, nối tiếp một chuỗi model dạng flash không giành được thị phần. Điểm nhấn được công bố là kết quả coding benchmark 77,9% trên Deep SWE — cao hơn mọi model hiện có — cùng mức cost of intelligence thấp hơn cả Anthropic lẫn OpenAI. Tuy nhiên model vẫn nằm dưới Pareto Frontier trong cuộc đua thị trường, vì cả model adoption và harness adoption đều chưa bắt kịp.

## Key ideas

- **Vị trí trong chuỗi sản phẩm:** ra mắt sau 7 tháng chờ đợi, kế tiếp nhiều model dạng flash trước đó — các flash model "struggle to get market adoption" vì cạnh tranh với flagship model khác và open model giá rẻ từ Trung Quốc
- **Benchmark nổi bật:** 77,9% trên Deep SWE, đứng trên mọi model hiện có tại thời điểm công bố
- **Cảnh báo về độ tin cậy số liệu:** toàn bộ 113 task và lời giải của Deep SWE công khai từ tháng 5, nên lab có thể nghiên cứu chúng trong post-training và nhắm benchmark — xem [[benchmark-contamination]]
- **Điểm yếu đã được ghi nhận:** Epoch phát hiện 23 task bị lỗi trong bộ benchmark
- **Harness adoption vẫn yếu:** anti-gravity chưa trở thành lựa chọn cạnh tranh cho developer; phần lớn người dùng vẫn ở Claude Code, Codex hoặc open harness — xem [[model-vs-harness-adoption]]
- **Model không nằm trên Pareto Frontier:** dù rẻ hơn, Anthropic và OpenAI vẫn dẫn đầu ở cả hai trục adoption
- **Chiến lược rollout theo doanh thu:** ưu tiên Ultra subscription users và paid API users — nơi doanh thu đã được thu — thay vì đốt compute để đua subscription như OpenAI và Anthropic
- **Ràng buộc công ty đại chúng:** Google phải cẩn thận phân bổ compute để tạo giá trị trong ecosystem (vì doanh thu phải báo cáo ra công), khác với OpenAI/Anthropic được tự do trợ giá subscription để săn user trước khi IPO
- **Quy mô API đủ lớn để thay đổi bài toán:** 22 tỷ token/phút, tăng 6 tỷ so với quý trước (call Q2 earnings), hơn 11 quadrillion token/năm chỉ riêng kênh API
- **Bước nhảy kỹ thuật đáng chú ý nhất:** output token tăng từ 64.000 lên **1 triệu token** — mở đường cho long-horizon task
- **Vì sao 1 triệu token là cam kết lớn:** duy trì coherence khi autoregressive generation kéo dài càng khó, nên việc đưa vào sản phẩm thương mại đòi hỏi mức tin cậy cao — xem [[autoregressive-error-compounding]]
- **Use case mở khóa:** code migration và research task chạy dài, nơi giá trị nằm ở khả năng giữ nhất quán xuyên suốt quỹ đạo dài
- **Chi phí có thời hạn:** lợi thế giá chỉ tồn tại cho tới khi discount tạm thời kết thúc và giá tăng gấp đôi

## Related concepts

- [[benchmark-contamination]]
- [[model-vs-harness-adoption]]
- [[autoregressive-error-compounding]]
- [[ai-evals]]
- [[ai-lab-business-model]]
- [[long-context-models]]

## Sources

- [[src_gemini-4-argon-explained-in-5min]]

## Notes
