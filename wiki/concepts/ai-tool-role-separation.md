---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, opinion]
topic: hermes-operator-builder-pattern
sources:
  - [[wiki/sources/src_1-month-with-hermes-ive-been-using-wrong]]
last_updated: 2026-05-19
---

# AI Tool Role Separation

## Definition

Nguyên tắc phân chia vai trò rõ ràng giữa các AI tools: một số tool phù hợp làm **Builder** (xây dựng), một số phù hợp làm **Operator** (vận hành). Không cố gắng ép một tool làm cả hai vai trò.

## Key ideas

- **Builder = One-time building tasks**: Dashboard, websites, slides, excel, UI/UX changes
- **Operator = Ongoing tasks**: Deliver reports, analyze data, pull & learn, recurring jobs
- **Claude/Code assistant = Builder**: Nhanh, aesthetics tốt, built-in features
- **AI Agent/Hermes = Operator**: Persistent memory, self-learning, automation
- **Linh hoạt theo nhu cầu**: Một số chỉ cần daily briefing, một số chỉ cần dashboard
- **"You have to steer the AI. Not let it steer you"**: Human ownership quan trọng

## Related concepts

- [[hermes-operator-role]]
- [[claude-builder-role]]

## Sources

- [[wiki/sources/src_1-month-with-hermes-ive-been-using-wrong]]

## Notes
