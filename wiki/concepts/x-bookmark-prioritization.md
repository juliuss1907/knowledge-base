---
type: concept
status: draft
main_tag: ai
sub_tags: [tools, automation]
topic: hermes-top-skills-analysis
sources:
  - [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]
last_updated: 2026-05-19
---

# X Bookmark Prioritization Skill

## Definition

Skill của Hermes nhìn vào X bookmarks, pick và rank theo priority (preference/investments/interests), summarize và propose next steps — giải quyết vấn đề bookmarks stale.

## Key ideas

- **Vấn đề:** 10-20 bookmarks/ngày nhưng chỉ revisit 1-2, còn lại stale
- **Solution:** Auto-rank và summarize bookmarks
- **Pick 15 top:** Rank theo priority dựa trên user preferences
- **Summarize:** Tóm tắt nội dung mỗi bookmark
- **Propose next steps:** Đề xuất hành động
- **Workflow:** X API → fetch bookmarks list → Browser → navigate to article → LLM summarize

**Blocker:** X API v2 không đọc được X articles → dùng Browser Harness

## Related concepts

- [[x-account-tracking-skill]]
- [[reflect-skill-hindsight]]

## Sources

- [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]

## Notes
