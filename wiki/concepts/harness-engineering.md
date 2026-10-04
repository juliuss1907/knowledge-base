---
type: concept
status: draft
main_tag: ai
sub_tags: [coding, tools]
topic: harness-engineering-ai-coding
sources:
  - "[[src_harness-engineering-ai-coding]]"
  - "[[src_googletech-behavioral-evals-harness-engineering]]"
  - "[[src_gemini-4-argon-explained-in-5min]]"
  - "[[src_how-to-make-infinite-ads-with-claude-code]]"
  - "[[src_motion-design-studio-with-opus-5-5]]"
last_updated: 2026-10-04
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
- **Living harness:** Document tự tham chiếu, vừa là specification vừa là health record — tracks constraint status và được chính enforcement mechanisms audit. Neglect becomes visible rather than invisible.
- **Bounded trust:** No agent có unilateral authority modify production code. Agents review, suggest, report, flag — humans decide.
- **Bốn thành phần tối thiểu của một harness hoạt động:** knowledge (agent hiểu domain của bạn), skill (biết *cách* làm việc), tools (thực sự làm được), và loop (tốt hơn sau mỗi lần dùng). Thiếu bất kỳ thành phần nào thì output AI vẫn chạy nhưng lệch — ví dụ quảng cáo AI "đúng kỹ thuật, sai giọng thương hiệu".
- **Harness quyết định cả output creative lẫn output video:** cùng một công thức "không có model nào đủ, cái thiếu là hệ thống" lặp lại ở quảng cáo tĩnh (brand brain + judge, [[brand-brain]] + [[llm-judge-loop]]) và ở video (render engine + critique loop, [[code2video-render-loop]] + [[critique-loop-self-scoring]])
- **"Prompt là 10% — 90% còn lại là harness":** một prompt một dòng tạo ra clip trông giống mọi clip khác; khác biệt thật nằm ở render engine, thư viện chuyển động, beat grid, và vòng tự soi frame — cùng một model, khác context đầu vào
- **Loop đóng bằng rule, không đóng bằng cảm xúc:** mỗi lỗi người dùng chỉ ra phải được ghi thành rule trong file cấu hình mà harness đọc mỗi run; sửa cùng một lỗi ở hai batch liên tiếp là dấu hiệu harness chưa đóng vòng lặp, xem [[llm-judge-loop]]
- **Adoption là phép đo cuối cùng:** harness không tự chứng minh giá trị — Codex đạt 5 triệu weekly active users so với 2,4 triệu của anti-gravity, dù model phía sau có thể mạnh và rẻ hơn. Chất lượng harness chuyển thành weekly active users, xem [[model-vs-harness-adoption]]

## Related concepts

- [[context-engineering]]
- [[progressive-hardening]]
- [[three-enforcement-loops]]
- [[agent-harness]]
- [[vibe-coding]]
- [[agentic-coding]]
- [[model-vs-harness-adoption]]
- [[brand-brain]]
- [[llm-judge-loop]]
- [[code2video-render-loop]]
- [[critique-loop-self-scoring]]
- [[directors-brief]]

## Sources

- [[src_harness-engineering-ai-coding]]
- [[src_googletech-behavioral-evals-harness-engineering]]
- [[src_gemini-4-argon-explained-in-5min]]
- [[src_how-to-make-infinite-ads-with-claude-code]]
- [[src_motion-design-studio-with-opus-5-5]]

## Notes
