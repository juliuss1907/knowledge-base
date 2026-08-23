---
type: concept
status: draft
main_tag: ai
sub_tags: [research]
topic: ai-reward-hacking-alignment
sources:
  - "[[src_reward-hacking-writeup]]"
last_updated: 2026-07-27
---

# AI Alignment

## Definition

AI alignment là lĩnh vực nghiên cứu và kỹ thuật nhằm đảm bảo AI systems hoạt động theo đúng ý định và values của con người. Mục tiêu là tạo ra AI mà behavior của chúng phù hợp với human intent, ngay cả khi systems trở nên more capable.

## Key ideas

- Core problem: specification problem - làm sao để định nghĩa objective mô tả đúng điều con người thực sự muốn
- Reward hacking là một dạng của alignment failure - model optimize sai objective
- Outer alignment: đảm bảo objective/reward function đúng đắn
- Inner alignment: đảm bảo model thực sự pursue objective đã cho thay vì pursue proxy goals
- Deceptive alignment: model appear aligned trong training nhưng pursue different goals khi deployed
- Các giải pháp: RLHF, constitutional AI, interpretability, adversarial training

## Related concepts

- [[reward-hacking]]
- [[ai-safety-monitoring]]
- [[reinforcement-learning]]
- [[rlhf]]
- [[interpretability]]

## Sources

- [[src_reward-hacking-writeup]] — rewardhacking.org analysis (2026-07-21)

## Notes

