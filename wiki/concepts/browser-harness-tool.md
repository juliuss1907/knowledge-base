---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: hermes-workflow-optimization
sources:
  - [[wiki/sources/src_hermes-analyst-workflow-essentials]]
  - [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]
last_updated: 2026-05-19
---

# Browser Harness Tool

## Definition

Tool @browser_use trong Hermes cho phép agent surf web như human — flexible nhất nhưng chậm hơn direct tools cho task cụ thể. Dùng cho X article extraction và general web browsing.

## Key ideas

- **@browser_use:** Flexible web browsing tool
- **Surf như human:** Không bị block như automated scraping
- **Chậm hơn direct tools:** Trade-off flexibility vs speed
- **X Bookmark Workflow:** X API v2 pull bookmarks → Browser Harness extract X articles content nếu cần summarize
- **Cảnh báo:** Practice extreme caution — dùng isolated/fresh browser, không share sensitive credentials

**Workflow:**
1. X API → fetch bookmarks list
2. Browser → navigate to article URL → extract full text
3. LLM → summarize mỗi article
4. Output → daily report

## Related concepts

- [[agent-skill-management]]
- [[x-bookmark-prioritization]]

## Sources

- [[wiki/sources/src_hermes-analyst-workflow-essentials]]
- [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]

## Notes
