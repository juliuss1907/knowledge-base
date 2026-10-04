---
type: concept
status: reviewed
main_tag: ai
sub_tags: [automation, tools, coding]
topic: code-as-agent-harness
sources:
  - "[[src_code-as-agent-harness-arxiv-2605-18747]]"
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# Agent Harness

## Definition

Agent harness là lớp phần mềm (software layer) bao quanh LLM, cung cấp cơ sở hạ tầng operational để kết nối đầu ra của model với hành động thực tế trong môi trường. Harness biến model "stateless" thành agent có khả năng thực thi lâu dài và đáng tin cậy.

## Key ideas

- **Operational substrate:** Code đóng vai trò nền tảng vận hành, không chỉ là sản phẩm đầu ra
- **Reliability bridge:** Kết nối model reasoning với persistent execution
- **System-level robustness:** Vượt qua giới hạn của base model capabilities
- **Harness engineering:** Ngành khoa học mới tập trung vào thiết kế, đo lường, tối ưu operational substrates
- **Harness là trục cạnh tranh độc lập với model:** Codex có 5 triệu weekly active users so với 2,4 triệu của anti-gravity, dù model của Google mạnh và rẻ hơn — người dùng sống trong harness chứ không sống trong model
- **Model tốt nhất vẫn thua nếu harness yếu:** Gemini 4 Argon undercut giá của Anthropic và OpenAI nhưng vẫn nằm dưới Pareto Frontier, vì cả hai đều dẫn đầu ở harness adoption lẫn model adoption
- **Sản phẩm thương mại mở đường cho long-horizon task:** harness phải chịu được quỹ đạo dài (code migration, research task) khi model có 1 triệu output token — xem [[autoregressive-error-compounding]]

## Related concepts

- [[code-as-substrate]]
- [[plan-execute-verify-loop]]
- [[model-vs-harness-adoption]]
- [[harness-engineering]]

## Sources

- [[src_code-as-agent-harness-arxiv-2605-18747]]
- [[src_gemini-4-argon-explained-in-5min]]

