---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, research]
topic: agent-memory-systems
sources:
  - "[[src_agent-memory-7-types-substack.md]]"
last_updated: 2026-07-30
---

# Procedural Memory

## Definition

Procedural memory chứa skills, workflows, và sequences of actions — kiểu "how to" knowledge. Trong AI agents, đây có thể là learned tool usage patterns, optimized prompts, hoặc multi-step workflows được "compiled" từ nhiều lần thực hiện tương tự.

## Key ideas

- Lưu trữ dạng "how to" — skills và procedures thay vì facts
- Có thể được tạo thủ công (hardcoded workflows) hoặc learned (few-shot optimization)
- "Compilation" concept: nhiều lần thực hiện tương tự → generalized procedure
- Ví dụ: agent học cách phân tích một loại request cụ thể sau nhiều lần làm
- Different từ episodic: procedural lưu generalized skill, episodic lưu specific instances
- Implementation: prompt templates, workflow definitions, learned policies

## Related concepts

- [[episodic-memory]]
- [[few-shot-prompting]]
- [[workflow-automation]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
