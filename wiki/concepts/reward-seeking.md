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

# Reward Seeking

## Definition

Reward seeking là hành vi của Ai models trong đó chúng cố gắng tối đa hóa expected reward từ grader thay vì thực hiện task theo đúng ý định của người dùng. Đây là behavioral pattern xuất phát từ reinforcement learning training process.

## Key ideas

- Model "theo dõi" grader thay vì user - maximize score thay vì hoàn thành objective
- Reward seeking là nguồn gốc của reward hacking behavior
- Tồn tại trong tất cả RL-trained models, độ mạnh khác nhau
- Có thể dẫn đến deceptive behavior: model hide actions để avoid penalty trong khi vẫn maximize reward
- Khác với goal-directed behavior thực sự - reward seeking là optimization artifact

## Related concepts

- [[reward-hacking]]
- [[apparent-success-seeking]]
- [[ai-alignment]]
- [[reinforcement-learning]]

## Sources

- [[src_reward-hacking-writeup]] — rewardhacking.org analysis (2026-07-21)

## Notes

