---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, research]
topic: ai-engineering-skills
sources:
  - "[[src_ai-engineering-skills-map]]"
  - "[[src_ai-skills-map-building-deploying-ai-apps]]"
last_updated: 2026-08-23
---

# AI Engineering Skills

## Definition

AI Engineering Skills là bộ 4 kỹ năng cốt lõi Andrew Ng xác định qua phân tích hơn 10.000 job postings + phỏng vấn chuyên gia: (1) building and deploying AI applications, (2) software engineering fundamentals, (3) using coding agents, (4) shaping the build. Đây là kỹ năng cho mọi developer chứ không riêng role "AI Engineer" — tương tự cách cloud skills trở thành bắt buộc cho tất cả. Điểm khác biệt nền tảng của AI software là output không đoán trước được, nên kỹ năng trung tâm là dùng statistical techniques (evals, error analysis) để biến hệ thống unreliable thành reliable.

## Key ideas

- **4 kỹ năng chính:** Building & deploying AI apps (LLM, context engineering, RAG, agentic workflows + evals/error analysis) · Software engineering fundamentals (nhận ra tradeoffs cost/scale/reliability/speed) · Using coding agents (steer, context management, verifiers) · Shaping the build (product sense, quyết định spec)
- **AI engineering ≠ AI Engineer role:** toàn bộ developer — full-stack, data, DevOps, ML — đều cần, như cloud skills ngày nay
- **Output bất định là gốc của mọi kỹ năng:** không đoán trước LLM trả gì → build AI là quá trình iterative, kỹ năng quyết định "làm gì tiếp theo" dựa trên intermediate results
- **Vibe coding thiếu fundamentals = poor tradeoffs:** developer không biết tradeoff nào tồn tại sẽ không biết cung cấp context gì cho coding agent → agent ra quyết định kém; fundamentals cho phép steer agent bằng "precise language of software engineering"
- **Coding agent skill:** mental model về agent, biết khi nào can thiệp/khi nào buông, quản lý context, cân bằng planning vs execution, cung cấp verifiers/evals để agent tự close loop, orchestrate multi-agent, tránh pitfall (agent hỏng production DB)
- **Shaping the build:** agent giỏi deliver theo spec → giá trị engineer dịch chuyển sang định hình spec: product sense, business context, customer goals; biết khi nào MVP nhanh khi nào build chậm cho chắc
- **Ownership & agency:** AI mở cơ hội tự nhận diện problem đáng làm và tự drive project — không chờ được giao design pixel-perfect để implement
- **Continuous learning mindset:** best practices đổi liên tục, cần routines thử tool mới và evolve workflow
- **Skill #1 tách thành 6 mảng (part 2):** LLM foundations · grounding models with data · building agentic systems · evaluation-driven development · operating in production · machine learning foundations
- **Build AI = iterative process:** output model không đoán trước → không plan trọn gói được; engineer giỏi loop build → examine → decide next step từ intermediate results, tạo reliable systems trên unreliable components
- **Evaluation-driven development quan trọng nhất:** disciplined evals/error analysis loop là trait phân biệt người giỏi nhất; chọn giữa deterministic code-based evals / LLM-as-a-judge / human-in-the-loop theo project + stage; phải evaluate chính evals
- **Grounding vượt xa RAG vector search:** menu gồm vector index, knowledge graph, semantic layer over structured data; quyết định prompt-time context vs on-demand retrieval bằng tools; pipeline documents → LLM-ready inputs
- **Agentic spectrum:** fixed workflow (chain LLM calls) ↔ agent harness (LLM tự quyết next step); quyết định tools (MCP/CLI/sandbox), memory architecture, context management session dài, single vs multi-agent; production cần guardrails + adversarial defense (prompt injection, data exfiltration) + governance
- **Production ops:** observability, drift detection, statistical regression testing calibrate theo risk, tối ưu cost/latency bằng distillation/fine-tuning/workflow simplification
- **ML foundations vẫn bắt buộc:** supervised + reinforcement learning là nền của LLM; bias/variance, error analysis, data engineering là frameworks điều hướng uncertainty

## Related concepts

- [[agentic-coding]]
- [[vibe-coding]]
- [[ai-evals]]
- [[context-window-management]]

## Sources

- [[src_ai-engineering-skills-map]] — Andrew Ng, X 2026-08-14 (part 1: 4 kỹ năng tổng quan)
- [[src_ai-skills-map-building-deploying-ai-apps]] — Andrew Ng, X 2026-08-21 (part 2: chi tiết 6 mảng của skill #1)

## Notes
