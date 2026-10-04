---
type: concept
status: draft
main_tag: ai
sub_tags: [research, opinion]
topic: open-models-us-china
sources:
  - "[[src_atom-project-american-truly-open-models]]"
last_updated: 2026-09-30
---

# Open Weight vs Open Source

## Definition

Hai mức độ mở của một AI model, phân biệt bằng những gì được phát hành. **Open-weight** chỉ công bố weights để inference hoặc fine-tune. **Open source** công bố đầy đủ weights *cùng* training data và training code. "Truly open" trong hội thoại open-AI luôn ám chỉ mức thứ hai.

## Key ideas

- Open-weight vẫn là **black box về quy trình**: bạn có được thành phẩm nhưng không có data hay code để tái tạo hay kiểm chứng nó
- Open source mở thêm ba nhóm artifact: training data, intermediate checkpoints, training code — cho phép **tái lập kết quả**, debug, và hiểu *tại sao* model hoạt động
- **Mô hình fully open còn hiếm trong ngành**, dù các bản open-weight đã trở thành chuẩn mực thực tế
- **License là biến cạnh tranh độc lập với openness:** model có thể open-weight nhưng license hạn chế, hoặc license permissive mà model nhỏ. License permissive chính là thứ đã giúp Qwen/DeepSeek bắt kịp và vượt Llama
- **Ai2 Olmo** là reference case: full stack mở (weights + data + checkpoints + code) + Apache 2.0 không ràng buộc; Olmo 3 32B Think được đánh giá là reasoning model fully open tốt nhất
- **Ranh giới đang mờ dần:** Nvidia Nemotron đã bắt đầu phát hành thêm data release, license mở dần; IBM Granite và OpenAI gpt-oss dùng Apache 2.0; nhưng Liquid AI vẫn chặn doanh thu ≥$10M/năm dù "gần như Apache"
- Lợi ích không dừng ở kỹ thuật: **mindshare và soft power** — lợi ích của việc chia sẻ công nghệ rơi về người xây, đúng như lịch sử open source software
- Với các bên build sản phẩm, thiếu adoption gần như **không tạo tín hiệu đo được** vì nó nằm trong hành vi riêng tư — sentiment này lặp lại trong các cuộc trao đổi thực tế với doanh nghiệp

## Related concepts

- [[open-model-ecosystem-race]]
- [[compute-concentration-frontier]]
- [[mixture-of-experts-moe]]
- [[responsible-ai-security-research]]
- [[ecosystems-mental-model]]

## Sources

- [[src_atom-project-american-truly-open-models]] — Nathan Lambert, The ATOM Project

## Notes
