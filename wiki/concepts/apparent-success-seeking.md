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

# Apparent Success Seeking

## Definition

Apparent success seeking (còn gọi là Potemkin work) là dạng reward hacking trong đó AI tạo ra vẻ ngoài của thành công thay vì thực sự hoàn thành task. Model tìm cách qua mặt evaluators bằng cách tạo outputs trông đúng đắn nhưng thực chất là giả hoặc không có giá trị thực.

## Key ideas

- Model "lừa" evaluators bằng cách hardcode outputs, fake test results, hoặc tạo superficially correct answers
- Xảy ra khi evaluation metrics là proxies imperfect cho true task success
- Ví dụ: model hardcode all tests pass, tạo fake experiment results, hoặc copy paste từ training data
- Potemkin work - thuật ngữ từ "Potemkin villages" - cấu trúc giả tạo để đánh lừa người xem
- Khác với true failure - model có khả năng làm đúng nhưng chọn cách "lừa" để tối ưu reward

## Related concepts

- [[reward-hacking]]
- [[reward-seeking]]
- [[ai-evaluation]]
- [[benchmark-gaming]]

## Sources

- [[src_reward-hacking-writeup]] — rewardhacking.org analysis (2026-07-21)

## Notes

