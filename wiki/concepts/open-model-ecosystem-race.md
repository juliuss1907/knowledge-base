---
type: concept
status: draft
main_tag: ai
sub_tags: [geopolitics, research, opinion]
topic: open-models-us-china
sources:
  - "[[src_atom-project-american-truly-open-models]]"
  - "[[src_interconnects-ai]]"
last_updated: 2026-09-30
---

# Open Model Ecosystem Race

## Definition

Cuộc đua giành thế chủ động trong hệ sinh thái open AI models, hiện đang nghiêng về Trung Quốc. Điểm mấu chốt không phải số model hay chất lượng từng model, mà là **hệ sinh thái**: nhiều lab có hỗ trợ, tập trung compute, và phát hành đều đặn đủ rộng để chiếm đa số derivative, download và token share.

## Key ideas

- **Bất đối xứng hiện tại:** Mỹ có số lượng lab tương đương Trung Quốc (~20 lab), nhưng phần lớn phát hành model *nhỏ hơn* với *license hạn chế hơn* — nên tác động nhỏ hơn nhiều
- **Đảo ngược adoption qua các mốc:** mùa hè 2023 Llama 2 ~500% download của Qwen 1.5 → 2024 Qwen 2.5 chỉ còn thua ~20M download (cả hai >120M) → sau DeepSeek V3/R1, **top 10 open model trên LMArena đều từ tổ chức Trung Quốc**, top 3 ArtificialAnalysis là Trung Quốc
- **Derivative là metric quyết định hơn benchmark:** đầu 2024 model Trung Quốc chiếm 10–30% finetune mới; nay derivative của Qwen >40% model ngôn ngữ mới mỗi tháng. Share derivative của Llama rơi từ đỉnh ~50% (cuối 2024) còn 15%
- **Inference share đi cùng:** sau DeepSeek, Trung Quốc dẫn đầu token share trên OpenRouter và dẫn đầu user share theo quốc gia
- **Vũ khí thật của Trung Quốc là license, không chỉ model:** Qwen/DeepSeek dùng license đơn giản rút gọn từ thực hành open-source, gỡ rào cản pháp lý mà Llama vẫn phải chịu
- **Meta từng thắng nhờ distribution channel có sẵn, không nhờ openness:** Llama dẫn đầu 2023–2024 *bất chấp* license hạn chế. Nay đối thủ có cả kích thước lẫn license
- **Cú sốc làm lộ mô hình "một con ngựa":** giai đoạn 2023–2024 Meta gần như độc quyền open model; giữa Llama 3 và Llama 4, DeepSeek phát hành frontier permissive → "chạy một vận động viên đơn độc chống lại một đội có hệ sinh thái"
- **Cá nhân hóa vấn đề:** vấn đề không phải "Llama 4 không state-of-the-art", mà là mô hình một-nhà-hãy-duy-nhất đã hết hiệu lực khi có đối thủ theo cả hai trục
- **Hai trục Trung Quốc chơi, phải phản công cả hai:** Qwen phát hành *family* mạnh ở mọi kích thước (chiếm lĩnh phân khúc phổ biến); DeepSeek phát hành *open frontier* (chiếm lĩnh benchmark). Cả hai đều cần thiết cho sức khoẻ hệ sinh thái
- **Mỹ đang cố phục hồi:** OpenAI gpt-oss-120b là open weights đầu tiên kể từ GPT-2 (Apache 2.0); Nvidia Nemotron Nano 9B v2 ngang/vượt model Trung Quốc ở phân khúc 9B; IBM Granite, Microsoft Phi (thường MIT), Stanford Marin đều đáng kể; nhóm mới (Arcee/Trinity, Reflection) chưa đạt quy mô
- **Chính sách:** White House AI Action Plan được coi là inflection point nhận thức — innovation và adoption toàn cầu lợi ích vượt rủi ro — nhưng vẫn thiếu artifact và hành động
- **Công thức được kết luận:** "với compute và talent đúng, model mạnh sẽ nối theo. Công thức là đưa nguồn lực đó tới nơi với chỉ thị phát hành model mở"
- **Lịch sử hiện tại (2026):** cuộc đua đã đi từ giai đoạn kỹ thuật sang giai đoạn chính sách. Nathan Lambert viết **lời kêu gọi bằng chứng cho Quốc hội Mỹ** về balance of power open models (09/2026), đồng thời viết op-ed "Banning Open Source AI Would Be A Mistake" cùng Kevin Xu cho công chúng phi kỹ thuật — hai văn bản từ cùng một tác giả, cùng một vấn đề, hai đối tượng thuyết phục khác nhau
- **Đà leo frontier của Trung Quốc là liên tục, không phải một lần vượt:** GLM-5.2 được mô tả là "step change for open agents", GLM-5.3 tiếp tục giữ nhịp frontier, Kimi K3 được gọi là "open-weights escalation", Qwen 3.8 vẫn mở rộng phân khúc phổ biến
- **Vấn đề cạnh tranh đã được tách bạch khỏi câu hỏi "có distill không":** GLM-5.3 bị chú thích rõ "It's really not a distillation story" — tức năng lực được giữ bằng nghiên cứu và training trực tiếp, không phải bằng cách sao chép model của phương Tây
- **Cảnh báo khả thi nghiêm trọng nhất:** bài tiêu đề "6 months to live for open models" (07/2026) được chính tác giả gọi là "nguyên cơ khả thi nghiêm trọng nhất cho open source AI đang diễn ra ngay lúc này" — cho thấy ngay cả bên theo thế chủ động cũng đang lo ngại mô hình có thể tự vỡ
- **Đã có hạ tầng đo lường:** Artifacts Hub và Adoption Dashboard (08/2026) mở rộng việc curation và đo adoption — phản ứng trực tiếp với nhận định trong ATOM Project rằng thiếu adoption gần như không tạo tín hiệu vì nó nằm trong hành vi riêng tư
- **Chiến lược phân phối mới của Nvidia:** "Teaching Everyone to Fish for Tokens" — thay vì bán compute cho khách, đẩy khách tự build model. Đây là biến thể khác của cùng một cuộc đua: mở rộng thành viên hệ sinh thái thay vì thu tiền usage

## Related concepts

- [[open-weight-vs-open-source]]
- [[compute-concentration-frontier]]
- [[structural-competition]]
- [[ecosystems-mental-model]]
- [[category-kings-dynamics]]
- [[mixture-of-experts-moe]]

## Sources

- [[src_atom-project-american-truly-open-models]] — Nathan Lambert, The ATOM Project
- [[src_interconnects-ai]]

## Notes
