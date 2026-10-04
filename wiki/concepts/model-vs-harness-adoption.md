---
type: concept
status: draft
main_tag: ai
sub_tags: [strategy, tools]
topic: model-vs-harness-adoption
sources:
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# Model vs Harness Adoption

## Definition

Model vs harness adoption là việc phân biệt năng lực của một model với mức độ được thị trường thực sự sử dụng. Một model có thể dẫn đầu benchmark và rẻ hơn đối thủ, nhưng vẫn thua về adoption nếu lớp phần mềm đi kèm (agent harness) chưa đủ cạnh tranh — vì người dùng coding thực tế sống trong harness chứ không sống trong model.

## Key ideas

- **Harness là sản phẩm người dùng chạm vào:** developer dùng Claude Code, Codex hoặc open harness, không dùng model trực tiếp — nên model adoption phụ thuộc mạnh vào chất lượng harness, xem [[agent-harness]]
- **Số liệu cụ thể về khoảng cách adoption:** **Codex có 5 triệu weekly active users so với 2,4 triệu của anti-gravity** — Codex hơn gấp đôi dù model không mạnh hơn rõ rệt
- **Model mạnh chưa đủ:** Gemini 4 Argon mạnh và rẻ, nhưng Google vẫn chưa giải được bài toán làm anti-gravity trở thành lựa chọn cạnh tranh cho developer
- **Pareto Frontier nhìn nhận đúng bản chất cuộc đua:** Argon có giá rẻ hơn nhưng vẫn nằm dưới Pareto Frontier, vì Anthropic và OpenAI dẫn đầu ở **cả hai trục: harness adoption và model adoption**
- **Harness engineering là lợi thế cạnh tranh độc lập:** chất lượng lớp điều phối, context, verification quyết định adoption nhiều không kém benchmark, xem [[harness-engineering]]
- **Adoption là chỉ số bền vững hơn benchmark:** benchmark đo năng lực tại một thời điểm và dễ bị nhiễm, còn adoption đo giá trị thực tế người dùng ghi nhận, xem [[benchmark-contamination]]
- **Bài học cạnh tranh:** model mới tốt nhất chưa chắc chiếm được thị phần nếu lớp trải nghiệm người dùng và hệ sinh thái quanh nó còn yếu

## Related concepts

- [[agent-harness]]
- [[harness-engineering]]
- [[benchmark-contamination]]
- [[gemini-4-argon]]
- [[compute-concentration-frontier]]

## Sources

- [[src_gemini-4-argon-explained-in-5min]]

## Notes
