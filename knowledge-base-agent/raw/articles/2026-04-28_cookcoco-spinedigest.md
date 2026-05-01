---
type: raw
source_type: article
source_url: https://dev.to/cookcoco/i-built-an-open-source-tool-to-distill-books-into-knowledge-graphs-fbo
date_ingested: 2026-04-28
batch: tech
tags: [#ai, #coding, #productivity]
status: processed
processed_date: 2026-05-01
approved_by: julius
---
# I built an open-source tool to distill books into knowledge graphs
## Cookcoco

**Link gốc:** https://dev.to/cookcoco/i-built-an-open-source-tool-to-distill-books-into-knowledge-graphs-fbo
**Published:** 2026-04-28
**Tags:** #opensource #llm #cli #productivity

---

## Tóm tắt

Cookcoco xây dựng **SpineDigest**, một open-source CLI tool biến sách (EPUB, Markdown, plain text) thành structured knowledge graph thay vì flat summary. Pipeline 3 giai đoạn: chunk extraction → knowledge graph construction → adversarial summarization. Có desktop app **Inkora** để visualize kết quả.

---

## Vấn đề

Tác giả có thói quen mua sách nhanh hơn đọc. Lý do: đến chapter 3 thì quên chapter 1, không biết concepts kết nối thế nào, xong không nhớ structure. "Just take better notes" không giải quyết được vì không biết **which parts matter** cho đến khi đọc xong.

---

## Tại sao không dùng ChatGPT để summarize?

1. **Context window limits** — sách thường 80k–200k tokens
2. **No structure** — flat summary loses relationships giữa ideas
3. **No re-exportability** — muốn format/focus khác phải rerun lại từ đầu

---

## Cách hoạt động

### Stage 1: Chunk extraction
Book được split thành sections và feed vào LLM từng section một — simulate how a person reads. Mỗi section, model extracts discrete knowledge units ("chunks"): self-contained facts, arguments, or concepts worth preserving.

→ Giải quyết context window problem, produce cleaner output.

### Stage 2: Knowledge graph construction
Classical graph algorithm (không phải LLM) clusters chunks by semantic similarity và builds graph of how concepts relate across the book. Related chunks grouped into "snakes" — chains of connected ideas.

→ Useful nhất: thấy được ideas nào author returns to repeatedly, which concepts depend on each other, where real weight of the book sits.

### Stage 3: Adversarial summarization
Multi-agent pass: một LLM writes summary, others ("professors") challenge nó against source material và stated extraction goal. Summary revised đến khi withstand scrutiny.

→ Overkill cho some books, nhưng making real difference cho dense technical/academic material.

---

## Usage

```bash
npm install -g spinedigest
spinedigest --input ./book.epub --output ./digest.md
```

With specific focus:
```bash
spinedigest --input ./book.epub --output ./digest.md \
  --prompt "Focus on system design tradeoffs and architectural patterns"
```

**Requires:** Node.js ≥ 22.12.0 + credentials cho supported LLM provider.

---

## .sdpub format

Processing takes time và API calls. SpineDigest saves full knowledge structure (chunks, graph, topology) vào `.sdpub` archive file.

Re-export later without rerunning LLM:
```bash
spinedigest --input ./digest.sdpub --output ./digest-v2.md \
  --prompt "Now focus on the historical context instead"
```

---

## Desktop app: Inkora

Free desktop app để visualize `.sdpub` files với topology và graph views. Hữu ích hơn stare at raw Markdown.

---

## Điểm yếu

Tác giả tự nhận: **chunking quality** là phần ít tự tin nhất. Current approach works well on well-structured non-fiction, nhưng gets messier với academic papers hoặc books có nhiều repetition.

---

## Liên quan

- Knowledge management tools (tương tự Obsidian, Notion)
- LLM-based research tools (tương tự Condup's approach)
- Knowledge graph concept (liên quan đến bài viết về Niri bookmark và graph view)