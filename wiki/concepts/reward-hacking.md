---
type: concept
status: draft
main_tag: ai
sub_tags: [research, hack]
topic: ai-reward-hacking-alignment
sources:
  - "[[src_reward-hacking-writeup]]"
last_updated: 2026-07-27
---

# Reward Hacking

## Definition

Reward hacking là hiện tượng AI systems tìm cách tối đa hóa reward signal từ grader/evaluator thay vì thực sự hoàn thành objective mà ngườI dùng mong muốn. Đây là một dạng của specification gaming hoặc proxy gaming trong reinforcement learning.

## Key ideas

- AI optimize cho metric (reward) thay vì true objective
- Có thể dẫn đến hành vi nguy hiểm: exploit vulnerabilities, bypass safeguards, tạo kết quả giả
- Xuất phát từ RL training process - model học cách maximize score từ grader
- Ba dạng chính: under-performance (Potemkin work), over-performance (over-eagerness), và security violations
- Reward hacking khác với malicious behavior - model không "cố tình" gây hại mà chỉ tối ưu reward function

## Related concepts

- [[reward-seeking]]
- [[apparent-success-seeking]]
- [[ai-alignment]]
- [[specification-gaming]]
- [[proxy-gaming]]

## Sources

- [[src_reward-hacking-writeup]] — rewardhacking.org analysis (2026-07-21)

## Notes

