---
type: concept
status: draft
main_tag: tech
sub_tags: [tools, coding, vibecode]
topic: ai-frontend-design-guidance
sources:
  - "[[src_impeccable]]"
last_updated: 2026-08-31
---

# Frontend Design Agent

## Definition

Frontend design agent là pattern dùng AI coding agent làm công cụ thiết kế frontend — agent viết code, tạo components, và iterate dựa trên design feedback. Impeccable mở rộng pattern này từ Anthropic's frontend-design skill ban đầu thành hệ thống hoàn chỉnh: 23 commands cho design vocabulary, 59 deterministic detector rules, live browser iteration, và context setup giúp agent biết audience, brand, voice. Khác với vibe coding thuần túy, frontend design agent có design vocabulary để critique, audit, polish một cách có chủ đích.

## Key ideas

- **Từ frontend-design skill đến Impeccable:** Anthropic's frontend-design là skill đầu tiên, Impeccable mở rộng thành hệ thống đầy đủ
- **Design commands:** critique (UX review), audit (technical checks), polish (final pass), distill (strip to essence), bolder/quieter
- **Deterministic + LLM rules:** 59 rules chạy không cần LLM cho technical checks, LLM-only critique cho UX
- **Live browser mode:** Visual variant iteration không cần reload
- **Anti-patterns:** Explicit guidance chống design tells phổ biến của AI-generated frontend
- **Context system:** PRODUCT.md + DESIGN.md giúp agent hiểu brand, audience, voice, colors

## Related concepts

- [[ai-frontend-design-guidance]]
- [[design-systems]]
- [[vibe-coding]]
- [[ai-assisted-development]]

## Sources

- [[src_impeccable]]

## Notes