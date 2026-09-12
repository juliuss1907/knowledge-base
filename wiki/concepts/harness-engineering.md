---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: harness-engineering-ai-coding
sources:
  - "[[src_harness-engineering-ai-coding]]"
last_updated: 2026-09-12
---

# Harness Engineering

## Definition

Harness engineering là thực hành bao quanh AI-assisted code generation bằng deterministic tooling, agent-based review, và periodic entropy checks để giữ cho AI-generated code luôn chính xác và nhất quán theo thời gian. Khác với test harness truyền thống kiểm tra functional correctness, harness engineering kiểm tra broader scope — architectural decisions, naming conventions, security constraints, và structural rules mà team đã agreed upon.

## Key ideas

- **Vấn đề AI drift:** AI assistants tạo code trông hợp lý nhưng nếu không có constraint sẽ dần xói mòn internal consistency — quên conventions, lặp sai lầm, bypass abstractions. Code vẫn compile và pass tests nhưng degradation là quiet.
- **Ba thành phần cốt lõi:** (1) Context engineering — đảm bảo AI biết đủ thông tin cần thiết; (2) Architectural constraints — enforcement mechanisms bắt violations; (3) Garbage collection — periodic fights entropy tích tụ.
- **Test harness analogy:** Test harness không make code correct by construction mà detect khi code stops being correct. Harness engineering áp dụng logic tương tự nhưng kiểm tra architectural và structural integrity thay vì functional correctness.
- **Context vs README:** HARNESS.md là knowledge base cho AI, không phải README cho humans — capture stack, architectural decisions, constraints, rationale. README explains what project does; context doc tells AI what it must/must not do and why.
- **Deterministic vs agent-based verification:** Deterministic tools (linters, scripts, regex) nhanh, rẻ, reliable cho constraints express precisely. Agent-based review (LLM judgment) cần thiết cho semantically complex constraints involving intent và patterns.
- **Progressive hardening:** Migrate constraints từ unverified → agent → deterministic khi understanding đủ sâu. Direction is always toward deterministic.
- **Living harness:** Document tự tham chiếu既是 specification vừa là health record — tracks constraint status và được chính enforcement mechanisms audit. Neglect becomes visible rather than invisible.
- **Bounded trust:** No agent có unilateral authority modify production code. Agents review, suggest, report, flag — humans decide.

## Related concepts

- [[context-engineering]]
- [[progressive-hardening]]
- [[three-enforcement-loops]]
- [[agent-harness]]
- [[vibe-coding]]
- [[agentic-coding]]

## Sources

- "[[src_harness-engineering-ai-coding]]"

## Notes
