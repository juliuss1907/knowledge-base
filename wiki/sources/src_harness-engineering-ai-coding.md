---
type: source
original: "[[2026-09-12_harness-engineering-ai-coding]]"
main_tag: ai
sub_tags: [coding, tools]
topic: harness-engineering-ai-coding
date_compiled: 2026-09-12
url: https://habitat-thinking.github.io/ai-literacy-superpowers/plugins/ai-literacy-superpowers/explanation/harness-engineering/
author: Birgitta Boeckeler (original), Habitat-Thinking (plugin adaptation)
---

# Harness Engineering

## Metadata

- **Author:** Birgitta Boeckeler (original), Habitat-Thinking (plugin adaptation)
- **Published:** 2026-09-12
- **Source:** habitat-thinking.github.io
- **URL:** https://habitat-thinking.github.io/ai-literacy-superpowers/plugins/ai-literacy-superpowers/explanation/harness-engineering/
- **Type:** article

## Summary

Harness engineering là thực hành bao quanh code generation hỗ trợ bởi AI bằng các deterministic tooling, agent-based review, và periodic entropy checks để giữ cho AI-generated code luôn chính xác và nhất quán theo thời gian. Thuật ngữ này bắt nguồn từ bài viết của Birgitta Boeckeler trên martinfowler.com, so sánh vấn đề AI drift với test harness truyền thống — thay vì kiểm tra functional correctness, harness cho AI coding kiểm tra architectural decisions, naming conventions, security constraints, và structural rules. Khung làm việc gồm ba thành phần chính: context engineering (đảm bảo AI biết đủ thông tin), architectural constraints (enforcement mechanisms thông qua deterministic tools hoặc agent-based review), và garbage collection (quá trình periodic chống entropy tích tụ). Một harness tốt không tĩnh mà là "living harness" — tài liệu tự tham chiếu既是 specification vừa là health record, với feedback loop liên tục giữa document và enforcement mechanisms.

## Key points

- AI assistants tạo ra code trông hợp lý nhưng nếu không có constraint sẽ drift — quên conventions, lặp lại sai lầm, xói mòn internal consistency của codebase
- Test harness truyền thống kiểm tra functional correctness; harness cho AI coding cần kiểm tra broader scope — architectural decisions, naming conventions, security constraints, structural rules
- **Context engineering:** maintaining document (HARNESS.md) capture stack, architectural decisions, constraints, rationale — khác với README (giải thích project làm gì vs context doc nói AI phải/không được làm gì)
- **Architectural constraints:** deterministic tools (linters, scripts, regex) nhanh, rẻ, reliable vs agent-based review (LLM judgment) cho semantically complex constraints
- **Progressive hardening principle:** migrate constraints từ agent-based sang deterministic khi understanding đủ sâu để express precisely
- **Garbage collection:** periodic schedule (không triggered by coding event) — dead code, stale TODOs, abandoned conventions, outdated abstractions
- **Living harness:** self-referential document tracks constraint status (unverified → agent → deterministic), neglect becomes visible rather than invisible
- **Three enforcement loops:** inner (advisory, edit-time), middle (strict, PR-time, có quyền block merge), outer (investigative, scheduled, reports)
- **Self-improving dimension:** /reflect command captures session learnings → accumulate in learnings log → agents read from this log → patterns of past mistakes inform current review
- Agents operate with bounded trust — review, suggest, report, flag; humans decide. Không agent nào có unilateral authority modify production code

## Concepts referenced

- [[harness-engineering]]
- [[context-engineering]]
- [[progressive-hardening]]
- [[three-enforcement-loops]]
- [[agent-harness]]
