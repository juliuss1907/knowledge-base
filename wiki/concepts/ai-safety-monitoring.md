---
type: concept
status: draft
main_tag: ai
sub_tags: [research, tools]
topic: ai-reward-hacking-alignment
sources:
  - "[[src_reward-hacking-writeup]]"
last_updated: 2026-07-27
---

# Ai Safety Monitoring

## Definition

Ai safety monitoring là các hệ thống và quy trình để theo dõi, phát hiện, và ngăn chặn dangerous behaviors từ Ai systems trong quá trình training và deployment. Đây là một layer của defense-in-depth approach cho Ai safety.

## Key ideas

- Monitoring cần detect cả overt bad behaviors lẫn deceptive/cooperative behaviors
- Ai control: technical approaches để maintain effective oversight của con người trên Ai systems
- Sandboxing và isolation là biện pháp cơ bản nhưng có thể bị bypass (như vụ OpenAi 2026)
- Capability evaluations: đánh giá xem model có khả năng gây hại không
- Alignment evaluations: đánh giá xem model có pursue đúng objectives không
- Scalable oversight: làm sao để con người giám sát systems vượt quá human-level capability

## Related concepts

- [[ai-alignment]]
- [[reward-hacking]]
- [[ai-control]]
- [[capability-evaluation]]
- [[alignment-evaluation]]

## Sources

- [[src_reward-hacking-writeup]] — rewardhacking.org analysis (2026-07-21)

## Notes

