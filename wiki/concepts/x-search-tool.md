---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: hermes-xai-grok-integration
sources:
  - [[wiki/sources/src_hermes-as-a-real-time-analyst]]
last_updated: 2026-05-19
---

# x_search Tool

## Definition

Tool của Hermes cho phép search X (Twitter) natively như SuperGrok, tích hợp với Grok subscription để fetch real-time content và articles từ X — không cần X API.

## Key ideas

- **Native X search**: Search X trực tiếp như SuperGrok
- **X article analysis**: Có thể đọc và summarize X article content (trước đây X API chỉ đọc headline)
- **Grok 4.3 fetch content**: Dùng Grok để extract content từ X
- **DeepSeek analyze**: Base model (DeepSeek-v4-flash) analyze và summarize
- **No X API needed**: Không cần X API subscription, tiết kiệm chi phí (~$0.1/ngày vs $0.5/ngày)
- **Real-time data**: Access "town square" cho macro, geopolitics, tech, AI, crypto

## Setup

```yaml
x_search:
  timeout_seconds: 240 # hoặc 300 để tránh timeout
  retries: 2
  model: grok-4.3
```

**Lưu ý**: Dùng `xai-oauth` thay vì `xai` để đi qua Grok subscription thay vì xAI API.

## Related concepts

- [[grok-hermes-integration]]
- [[six-stage-research-pipeline]]

## Sources

- [[wiki/sources/src_hermes-as-a-real-time-analyst]]

## Notes
