---
type: source
original: "[[2026-07-27_agent-memory-7-types-substack.md]]"
main_tag: ai
sub_tags: [tools, research]
topic: agent-memory-systems
date_compiled: 2026-07-30
url: https://jamwithai.substack.com/p/agent-memory-the-7-types-you-should
author: jamwithai (Substack)
---

# Agent Memory — the 7 types you should know before you ship to production

## Metadata

- **Author:** jamwithai (Substack)
- **Published:** 2026-07-27
- **Source:** jamwithai.substack.com
- **URL:** https://jamwithai.substack.com/p/agent-memory-the-7-types-you-should
- **Type:** article

## Summary

Bài viết trình bày framework phân loại 7 loại memory khác nhau trong AI agent systems, dựa trên nghiên cứu cognitive science và paper CoALA (2023). Mỗi loại memory phục vụ mục đích khác nhau: working memory cho context hiện tại, semantic memory cho facts, episodic memory cho experiences, procedural memory cho skills, external memory cho retrieval, parametric memory cho model weights, và prospective memory cho future tasks. Điểm then chốt là không phải agent nào cũng cần cả 7 loại — việc chọn đúng loại memory phù hợp với use case quan trọng hơn việc thêm càng nhiều càng tốt. Bài viết cũng chỉ ra các điểm fail phổ biến trong production và cách implement từng loại.

## Key points

- Memory trong AI agents không phải một khái niệm đơn nhất mà gồm 7 loại riêng biệt với cách lưu trữ, retrieve và failure modes khác nhau
- Working memory (in-context) là loại duy nhất model có thể sử dụng trực tiếp — storage chỉ là potential, working memory mới là active
- Semantic memory lưu facts và knowledge, thường implement bằng vector databases nhưng cần careful chunking và retrieval strategy
- Episodic memory lưu experiences và interactions cụ thể, giúp agent học từ quá khứ với cùng một user
- Procedural memory chứa skills và workflows, có thể được "compiled" từ nhiều lần thực hiện tương tự
- External/retrieval memory là pattern lấy thông tin từ outside sources (APIs, databases, search) đưa vào context
- Parametric memory là kiến thức đã được encode trong model weights thông qua fine-tuning
- Prospective memory giúp agent nhớ các tasks cần thực hiện trong tương lai (scheduling, follow-ups)
- "More memory is not a better agent" — agent tốt hơn là agent biết forget có chủ đích
- Framework này dựa trên CoALA paper (Sumers et al., 2023) mapping cognitive architectures sang LLM agents

## Concepts referenced

- [[in-context-memory]]
- [[semantic-memory]]
- [[episodic-memory]]
- [[procedural-memory]]
- [[external-retrieval-memory]]
- [[parametric-memory]]
- [[prospective-memory]]
- [[coal-framework]]

## Original excerpts

> "More memory is not a better agent. A better agent forgets on purpose."

> "Storage is potential. Working memory is what the model can actually use right now."

> "The useful design question is not 'how do we add memory to the agent?' It is: what should the agent remember, for how long, and under what conditions should that information come back?"
