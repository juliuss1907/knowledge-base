---
type: source
original: "[[2026-08-30_ai-engineering-skills-map-building-deploying-ai-applications]]"
main_tag: ai
sub_tags: [coding, research]
topic: ai-engineering-skills
date_compiled: 2026-08-31
url: https://www.deeplearning.ai/the-batch/he-ai-engineering-skills-map-in-detail-building-and-deploying-ai-applications
author: Andrew Ng
---

# The AI Engineering Skills Map In Detail — Building and Deploying AI Applications

## Metadata

- **Author:** Andrew Ng (The Batch — deeplearning.ai)
- **Published:** [unknown]
- **Source:** deeplearning.ai
- **URL:** https://www.deeplearning.ai/the-batch/he-ai-engineering-skills-map-in-detail-building-and-deploying-ai-applications
- **Type:** article

## Summary

Đây là phần chi tiết của AI Engineering Skills Map về kỹ năng thứ nhất — building and deploying AI applications — chia thành 6 mảng: LLM foundations, grounding models with data, building agentic systems, evaluation-driven development, operating in production, machine learning foundations. Andrew Ng nhấn mạnh điểm khác biệt căn bản: output của AI software không đoán trước được, nên build AI là quá trình iterative hơn hẳn traditional software — engineer giỏi liên tục build → examine → quyết định bước tiếp theo dựa trên intermediate results. Ông đánh giá evaluation-driven development (disciplined evals/error analysis loop) là trait quan trọng nhất phân biệt người xây hệ thống AI giỏi. Bản này là The Batch letter mở rộng, chi tiết hơn bản X post trước đó về cùng chủ đề.

## Key points

- **6 mảng của skill #1:** LLM foundations · grounding models with data · building agentic systems · evaluation-driven development · operating in production · machine learning foundations
- **Output bất định là gốc:** Không biết trước LLM output hay supervised learning prediction → build AI iterative hơn, khó plan trọn gói; kỹ năng then chốt là quyết định bước tiếp theo từ intermediate results
- **LLM foundations:** Hiểu tokenization, generation, khi nào tin model/khi nào fail; multimodal tradeoffs, context window, cache hits, knowledge cutoff, reasoning effort, sampling parameters, tool calling
- **Grounding models with data:** Menu vượt xa RAG vector search — vector index, knowledge graph, semantic layer over structured data; quyết định prompt-time context vs on-demand retrieval bằng tools; pipeline documents → LLM-ready inputs sạch và tươi
- **Building agentic systems:** Spectrum từ fixed workflow đến agent harness (LLM tự quyết next step); chọn tools (MCP, CLI, sandbox), memory architecture, context management, multi-agent vs single-agent; production cần guardrails, adversarial defense (data exfiltration), governance
- **Evaluation-driven development — quan trọng nhất:** Disciplined evals/error analysis loop định hướng effort; building evals là deep skill — đọc traces, EDA, product insight; chọn deterministic code-based vs LLM-as-a-judge vs human-in-the-loop; phải evaluate chính evals
- **Operating in production:** Observability trên real usage, drift detection, phản ứng nhanh model failures + security incidents; regression testing/CI/CD dùng statistical evaluations, calibrate theo risk; tối ưu cost/latency bằng model choice, distillation, fine-tuning, workflow simplification
- **ML foundations bắt buộc:** Supervised + reinforcement learning là nền của LLM; bias/variance, error analysis, data engineering là frameworks điều hướng uncertainty

## Concepts referenced

- [[ai-engineering-skills]]
- [[ai-evals]]
- [[rag-retrieval-augmented-generation]]
- [[agent-harness]]
- [[context-window-management]]
- [[ai-observability]]

## Original excerpts

> "The key difference between AI applications and non-AI software is that the former's output is less predictable."

> "In my experience, the most important trait that distinguishes someone great at building AI systems is whether you can drive a disciplined evals/error analysis loop to drive development."