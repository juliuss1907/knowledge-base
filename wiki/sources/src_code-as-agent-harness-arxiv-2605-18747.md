---
type: source
original: [[2026-05-22_code-as-agent-harness-arxiv-2605-18747.md]]
main_tag: ai
sub_tags: [research, coding]
topic: code-as-agent-harness
date_compiled: 2026-05-23
url: https://www.alphaxiv.org/abs/2605.18747
author: "Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei"
---

# Code as Agent Harness

## Metadata

- **Author:** Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei
- **Institutions:** University of Illinois Urbana-Champaign, Meta, Stanford University
- **Published:** arXiv 2605.18747
- **Source:** alphaXiv / arXiv
- **URL:** https://www.alphaxiv.org/abs/2605.18747
- **Type:** paper

## Summary

Paper này tái định nghĩa vai trò của code trong các hệ thống agent dựa trên LLM — từ một sản phẩm đầu ra thuần túy thành nền tảng vận hành (operational substrate) cho trí tuệ agent. Code không chỉ là kết quả của khả năng coding của LLM, mà trở thành phương tiện kết nối reasoning, action, environment modeling và execution-based verification trong vòng lặp tác vụ dài hạn.

## Key points

- **Code as Agent Harness:** Code là operational substrate cho agent intelligence — executable, inspectable, stateful, verifiable
- **Agent-Initiated Code Artifacts:** Code objects do agent tạo ra, thực thi, quan sát, chỉnh sửa và chia sẻ trong vòng lặp tác vụ
- **Ba tầng kiến trúc:** Harness Interface (kết nối), Harness Mechanisms (độ tin cậy), Scaling the Harness (multi-agent)
- **Code for Reasoning:** Externalize internal logic thành verifiable computation — Program-of-Thoughts, PAL, DeepSeek-Prover
- **Code for Action:** Generated programs như executable policies — Code as Policies, RoboCodeX, Voyager
- **Code for Environment Modeling:** World state, dynamics, feedback signals được biểu diễn qua code — ViStruct, WorldCoder
- **Memory types cho agent:** Working, Semantic, Experiential, Long-term, Multi-Agent — quản lý tension giữa context window và task state
- **Plan-Execute-Verify loop:** Transform debugging thành control process cho state transitions — contract formation, sandboxed execution, deterministic verification
- **Multi-Agent coordination:** Functional role specialization (Programmer, Tester, Reviewer, Architect) và shared code-centric substrate
- **Harness engineering challenges:** Evaluation, Semantic verification, Self-evolving harnesses, Transactional state, Human oversight, Multimodal integration

## Concepts referenced

- [[agent-harness]]
- [[code-as-substrate]]
- [[agent-initiated-code-artifacts]]
- [[program-of-thoughts]]
- [[multi-agent-systems]]
- [[plan-execute-verify-loop]]
- [[code-for-reasoning]]
- [[code-for-action]]
- [[code-for-environment-modeling]]

## Original excerpts

> "Code is no longer just an output target for LLMs (demonstrating coding capability), but becomes the **medium for agent intelligence** itself — spanning reasoning, action, environment modeling, and execution-based verification."

> "Pure text reasoning: unreliable for symbolic computation, hard to verify, no persistence. Code: executable, inspectable, stateful — enabling reliable closed-loop behavior."

> "Old View: Code = output of LLM coding capability. New View: Code = executable, inspectable, stateful operational substrate."
