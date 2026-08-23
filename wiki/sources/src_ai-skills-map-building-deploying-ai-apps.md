---
type: source
original: "[[2026-08-21_ai-skills-map-building-deploying-ai-apps]]"
main_tag: ai
sub_tags: [coding, research]
topic: ai-engineering-skills
date_compiled: 2026-08-23
url: https://x.com/AndrewYNg/status/2090840747738374568
author: AndrewYNg
---

# AI Engineering Skills Map: Building and Deploying AI Applications

## Metadata

- **Author:** Andrew Ng (@AndrewYNg)
- **Platform:** X (post)
- **Published:** 2026-08-21
- **Ingested:** 2026-08-22
- **URL:** https://x.com/AndrewYNg/status/2090840747738374568
- **Type:** post
- **Series:** AI Engineering Skills Map (part 2)

## Summary

Ở phần 2 của AI Engineering Skills Map, Andrew Ng đi sâu vào kỹ năng thứ nhất — building and deploying AI applications — và chia nó thành 6 mảng con: LLM foundations, grounding models with data, building agentic systems, evaluation-driven development, operating in production, và machine learning foundations. Ông nhấn mạnh điểm khác biệt căn bản giữa AI software và traditional software là output khó đoán, khiến việc build AI mang tính iterative cao hơn: engineer giỏi liên tục build → examine → quyết định bước tiếp theo dựa trên intermediate results. Trong 6 mảng, Ng đánh giá evaluation-driven development — driving disciplined evals/error analysis loop — là trait quan trọng nhất phân biệt người xây AI hệ thống giỏi. Bài viết cũng liệt kê kỹ năng production cụ thể: observability, drift detection, regression testing với statistical evaluations, tối ưu cost/latency qua distillation và fine-tuning.

## Key points

- Build AI khác traditional software ở output bất định → quá trình iterative, khó plan trước; kỹ năng then chốt là quyết định "làm gì tiếp theo" từ intermediate results để tạo reliable system trên unreliable components
- LLM foundations: hiểu tokenization, generation, khi nào tin model/khi nào fail; tradeoffs context window, cache hits, knowledge cutoff, reasoning effort, sampling parameters, tool calling; chọn model/mix models, fine-tuning hay self-hosting
- Grounding models with data: RAG vector search chỉ là khởi đầu — menu kỹ thuật gồm vector index, knowledge graph, semantic layer over structured data; quyết định gì đưa vào prompt vs cho model retrieve on demand bằng tools; pipeline biến documents thành LLM-ready inputs sạch và tươi
- Building agentic systems: phổ trải từ fixed workflow (chuỗi LLM calls định sẵn) đến agent harness (LLM tự quyết step tiếp); chọn architecture, fallbacks, tools (MCP, CLI, sandbox), memory architecture, quản lý context session dài, multi-agent orchestration; production hóa cần guardrails, adversarial inputs, chống data exfiltration, governance
- Evaluation-driven development — trait quan trọng nhất: disciplined evals/error analysis loop định hướng effort; building evals là deep technical skill (đọc traces, EDA + product insight); biết chọn deterministic code-based evals vs LLM-as-a-judge vs human-in-the-loop, và evaluate chính evals
- Operating in production: observability trên real usage, track drift, phản ứng nhanh với model failures và security incidents (adversarial prompt injection); regression testing + CI/CD dùng statistical evaluations nhiều hơn truyền thống, calibrate theo risk; tối ưu cost/latency bằng model choice optimization, distillation, fine-tuning, workflow simplification
- Machine learning foundations: supervised learning + reinforcement learning là nền của modern LLMs; bias/variance, error analysis, data engineering vẫn là mental frameworks trung tâm cho mọi quyết định trong hệ thống có uncertain output

## Concepts referenced

- [[ai-engineering-skills]]
- [[ai-evals]]
- [[rag-retrieval-augmented-generation]]
- [[agent-harness]]
- [[context-window-management]]

## Original excerpts

> In my experience, the most important trait that distinguishes someone great at building AI systems is whether you can drive a disciplined evals/error analysis loop to drive development.
