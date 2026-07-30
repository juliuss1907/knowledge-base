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

# Parametric Memory

## Definition

Parametric memory là kiến thức đã được encoded trực tiếp vào model weights thông qua training hoặc fine-tuning. Đây là "implicit memory" của model — những gì model "biết" mà không cần retrieve từ external source.

## Key ideas

- Knowledge stored in model weights (parameters)
- Created qua pre-training (broad knowledge) hoặc fine-tuning (specialized knowledge)
- Pros: instant access, no retrieval cost, always available
- Cons: static (không update được mà không re-train), black-box (khó interpret), có thể outdated
- Distinct từ other memory types: parametric là internal, others là external augmentations
- Fine-tuning cho specific domain = "implanting" memory vào weights
- Trade-off: fine-tuning cost vs. retrieval flexibility

## Related concepts

- [[fine-tuning]]
- [[model-weights]]
- [[in-context-learning]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
