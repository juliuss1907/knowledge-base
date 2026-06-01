---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, tools]
topic: llm-memory-consolidation
sources:
  - "[[src_llm-need-sleep-consolidation]]"
last_updated: 2026-05-28
---

# Gated Delta Networks

## Definition

Loại State Space Model sử dụng delta-rule correction cho weight updates — được dùng trong experiments của LLM Sleep paper.

## Key ideas

- Incorporates delta-rule correction: ΔS = learning_signal
- Cho phép selective writing, overwriting, forgetting
- Dùng trong 4-layer GDN-attention hybrid model
- Hebbian-like update rules from Mamba2-style SSMs

## Related concepts

- [[llm-sleep]]
- [[state-space-models-ssm]]

## Sources

- [[src_llm-need-sleep-consolidation]]

## Notes
