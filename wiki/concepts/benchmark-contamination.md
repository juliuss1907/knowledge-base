---
type: concept
status: draft
main_tag: ai
sub_tags: [research, opinion]
topic: benchmark-contamination
sources:
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# Benchmark Contamination

## Definition

Benchmark contamination là hiện tượng benchmark AI bị "nhiễm" khi toàn bộ task và lời giải được công khai, cho phép các lab nghiên cứu chúng trong post-training và nhắm vào điểm số thay vì cải thiện năng lực thật. Kết hợp với tốc độ bão hoà benchmark nhanh hơn trước, nó khiến con số do lab tự công bố ngày càng khó dùng để đo tiến bộ khoa học.

## Key ideas

- **Cơ chế nhiễm:** toàn bộ **113 task và lời giải của Deep SWE được công khai từ tháng 5** → lab có thể study chúng trong post-training rồi benchmark model quanh public benchmark
- **Chênh lệch lợi thế theo thời gian:** lab phát hành model càng muộn càng có lợi thế nhẹ, vì có thể kịp đưa benchmark vào post-training — đây là hiệu ứng cấu trúc của toàn ngành, không phải lỗi cá biệt của lab nào
- **Đa số benchmark Google báo cáo đều là public** → phần lớn số liệu công bố rơi vào vùng rủi ro này
- **Chất lượng benchmark cũng là vấn đề:** Epoch phát hiện **23 task bị lỗi** trong bộ benchmark này, một lý do để giữ "healthy skepticism" ngay cả với số liệu từ lab uy tín
- **Saturation tăng tốc:** benchmark saturate nhanh hơn nhiều so với trước, buộc phải refresh thường xuyên hơn — vòng đời benchmark ngày càng ngắn
- **Gánh nặng chuyển sang người dùng:** người tiêu dùng phải tự gánh phần lớn gánh nặng theo dõi tiến bộ khoa học thật của AI, vì báo cáo benchmark không còn đáng tin
- **Post-training là kênh nhiễm chính:** mọi benchmark đã public đều có thể bị "học thuộc" qua post-training trước khi công bố kết quả
- **Hệ quả với evals:** nhấn mạnh giá trị của proprietary eval suite — benchmark công khai nhanh chóng mất khả năng phân biệt model, xem [[ai-evals]]

## Related concepts

- [[ai-evals]]
- [[gemini-4-argon]]
- [[error-signal-learning]]
- [[long-context-models]]

## Sources

- [[src_gemini-4-argon-explained-in-5min]]

## Notes
