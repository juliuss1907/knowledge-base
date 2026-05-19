---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, research]
topic: hermes-top-skills-analysis
sources:
  - [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]
last_updated: 2026-05-19
---

# External Memory Providers

## Definition

Các service cung cấp external memory cho AI agents như Hermes — lưu trữ và recall thông tin qua các sessions với high accuracy, đặc biệt cho long-horizon và multi-session contexts.

## Key ideas

- **Hindsight:** #1 recall accuracy — especially long-horizon, multi-session, large-scale
- **Memory config + external memory:** Giúp retain context và search knowledge base
- **Cảnh báo cost:** Link Hindsight to OpenRouter + Claude Sonnet 4.6 → Burn $50+ tokens trong 1 ngày
- **Alternative:** Explore other memory providers nếu cost prohibitive
- **Use case:** Reflect skill, pattern detection, historical analysis

## Related concepts

- [[reflect-skill-hindsight]]
- [[hermes-token-management]]

## Sources

- [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]

## Notes
