---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation, news]
topic: hermes-xai-grok-integration
sources:
  - [[wiki/sources/src_hermes-as-a-real-time-analyst]]
last_updated: 2026-05-19
---

# Grok-Hermes Integration

## Definition

Tích hợp giữa Nous Research (Hermes) và xAI cho phép X Premium/Premium+ users plug Grok subscription vào Hermes, mở rộng khả năng real-time research trên X và tiết kiệm chi phí đáng kể.

## Key ideas

- **Direct Grok subscription**: X Premium/Premium+ users có Grok subs có thể plug vào Hermes
- **x_search tool**: Cho phép Hermes search X natively
- **Cost optimization**: Từ X API ($0.5/ngày) xuống x_search ($0.1/ngày)
- **Grok subscription hack**: $30/3 tháng thay vì $30/tháng (cancel sau đăng ký để nhận offer)
- **Setup**: Authenticate với `hermes model` command, dùng `xai-oauth`
- **Real-time capability**: Access real-time X data cho research

## Cost Comparison

| Method | Cost/ngày | Notes |
|--------|-----------|-------|
| X API | ~$0.5 | Fetch smart accounts |
| x_search | ~$0.1 | Chỉ dùng cho X bookmark cron job |

## Related concepts

- [[x-search-tool]]
- [[ai-research-workflow]]

## Sources

- [[wiki/sources/src_hermes-as-a-real-time-analyst]]

## Notes
