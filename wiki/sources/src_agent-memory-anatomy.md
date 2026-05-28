---
type: source
original: "[[2026-05-27_agent-memory-anatomy]]"
main_tag: ai
sub_tags:
  - research
  - tools
topic: agent-memory-systems
date_compiled: 2026-05-27
url: https://brgsk.xyz/agent-memory-anatomy/
author: brgsk
---

# Agent Memory: An Anatomy

## Metadata

- **Author:** brgsk
- **Published:** 2026 (mid-2026)
- **Source:** brgsk.xyz
- **URL:** https://brgsk.xyz/agent-memory-anatomy/
- **Type:** article

## Summary

Bài phân tích chi tiết về kiến trúc bộ nhớ agent, chỉ ra rằng hầu hết thư viện "agent memory" hiện nay chỉ thực hiện một phần rất hẹp của khái niệm "memory" trong khoa học nhận thức. Tác giả đồng hóa bộ nhớ agent thành ba thành phần: extractor (trích xuất thông tin), store (lưu trữ), và retriever (truy xuất). Phân tích chỉ ra rằng thực tế các thư viện chủ yếu xử lý "autobiographical memory" (thông tin về người dùng) thay vì đầy đủ các loại bộ nhớ: episodic (sự kiện), semantic (kiến thức), procedural (kỹ năng), và prospective (kế hoạch tương lai).

## Key points

- Thuật ngữ episodic/semantic bắt nguồn từ Tulving (1972), nhưng triển khai kỹ thuật thường chỉ là "nhãn" chứ không phải hệ thống riêng biệt
- Ba thành phần cốt lõi: extractor (quyết định giữ gì), store (xử lý mâu thuẫn), retriever (tìm kiếm liên quan)
- Thời điểm extraction quan trọng: eager (tốn token) vs lazy (mất ngữ cảnh)
- Xử lý mâu thuẫn trong store: overwrite, append, hay mark superseded — quyết định có thể audit "đã tin gì tháng trước"
- Episodic memory bị nén thành semantic tại extraction — mất ngữ cảnh thời gian/địa điểm
- Procedural memory là thước đo chênh lệch giữa claim và implementation (LangMem vs Mem0)
- Prospective memory (nhớ làm gì tương lai) gần như không tồn tại trong production
- Thực chất: autobiographical memory — agent giữ thông tin về người dùng thay cho họ
- Consolidation (Anthropic Dreams, Letta sleep-time): offline rewrite, dedupe, resolve contradictions
- Biological forgetting không phải feature — agent có thể keep everything và giải quyết retrieval problem

## Concepts referenced

- [[agent-memory-taxonomy]]
- [[memory-extraction-timing]]
- [[consolidation-offline-processing]]
- [[autobiographical-memory-systems]]
- [[prospective-memory-gap]]

## Original excerpts

> "the most consequential choice an extractor makes is timing. extract eagerly, after every message, and you spend tokens on small talk that goes nowhere. extract lazily, at the end of a session, and the context you needed to resolve a pronoun is already gone."

> "a store that can't answer what did I believe last month? isn't a memory system. it's a snapshot with a timestamp on it."

> "what these libraries actually are: semantic memory, and within semantic, one specific subset: autobiographical memory — the facts a person knows about their own life."

> "biological-style forgetting belongs in the third category — shouldn't. whether some other forgetting rule belongs anywhere is a separate question."
