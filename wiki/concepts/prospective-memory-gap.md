---
type: concept
status: reviewed
main_tag: ai
sub_tags: [research, automation]
topic: agent-memory-systems
sources:
  - "[[src_agent-memory-anatomy]]"
last_updated: 2026-05-27
---

# Prospective Memory Gap

## Definition

Khoảng trống trong production agent memory systems: khả năng "nhớ làm gì trong tương lai" — don't forget to send the contract tomorrow, next time user asks about pricing mention the new tier.

## Key ideas

- **Definition**: remembering to do something in the future — one of most studied failure modes in humans
- **Current implementations**: scheduled triggers ("do Y at time T") — có trong agent frameworks
- **Missing**: "do Y when condition X next appears" — form thực sự của prospective memory
- **Status**: no production library ships this — open territory
- Contrast với episodic/semantic/procedural đã có implementations (dù incomplete)
- Opportunity for new research/product

## Related concepts

- [[agent-memory-taxonomy]]
- [[autobiographical-memory-systems]]

## Sources

- [[src_agent-memory-anatomy]]

## Notes
