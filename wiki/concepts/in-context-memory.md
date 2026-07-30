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

# In-context / Working Memory

## Definition

Working memory (hay in-context memory) là toàn bộ nội dung text được gửi vào model trong một API call — bao gồm instructions, conversation history, tool results, và retrieved information. Đây là loại memory duy nhất mà language model có thể "nhìn thấy" và sử dụng để generate response. Một khi API call kết thúc, model quên hoàn toàn nội dung đó trừ khi được re-send trong lần call tiếp theo.

## Key ideas

- Model chỉ có thể reason over những gì nằm trong current prompt — không có implicit memory giữa các calls
- Working memory có giới hạn cứng gọi là context window (số tokens tối đa model có thể xử lý)
- Khi conversation dài hơn context window, cần chọn lọc what to keep, what to drop, what to summarize
- Các messages cũ trong conversation vẫn "ảnh hưởng" đến model không phải vì model "nhớ" mà vì chúng được re-send mỗi turn
- Cắt bỏ old messages khỏi working memory = "forget" hoàn toàn thông tin đó

## Related concepts

- [[semantic-memory]]
- [[external-retrieval-memory]]
- [[context-window-management]]

## Sources

- [[src_agent-memory-7-types-substack.md]]

## Notes
