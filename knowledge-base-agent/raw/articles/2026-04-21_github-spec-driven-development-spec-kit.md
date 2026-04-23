---
type: raw
source_type: article
source_url: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
date_ingested: 2026-04-21
tags: [#coding, #ai]
status: processed
processed_date: 2026-04-22
---
# Spec-Driven Development with AI: Get Started with a New Open Source Toolkit

## Tóm tắt

GitHub ra mắt Spec Kit — open source toolkit cho spec-driven development với AI coding agents như GitHub Copilot, Claude Code, Gemini CLI.

## Vấn đề với "vibe coding"

Code agents ngày càng mạnh nhưng approach của chúng ta có vấn đề: ta treat chúng như search engines thay vì pair programmers. Vibe coding OK cho prototypes, nhưng không reliable cho mission-critical apps.

Vấn đề không phải ở coding ability của agent mà ở cách chúng ta approach. Agents giỏi pattern recognition nhưng vẫn cần unambiguous instructions.

## Spec Kit — 4 phases

1. **Specify** — Cung cấp high-level description về what đang build và why. Agent generate detailed specification về user journeys, experiences, outcomes. Không phải về tech stack hay app design.
2. **Plan** — Cung cấp desired stack, architecture, constraints. Agent generate comprehensive technical plan. Có thể ask cho multiple plan variations để compare.
3. **Tasks** — Agent break spec và plan thành small, reviewable chunks. Mỗi task implementable và testable in isolation — gần như TDD cho AI agent.
4. **Implement** — Agent tackle tasks one by one. Developer review focused changes thay vì thousand-line code dumps.

**Key insight:** Mỗi phase có specific job, không move sang phase tiếp theo cho đến khi current task fully validated.

## Cách hoạt động

```bash
# Install
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>

# Commands trong coding agent
/specify  # Generate spec từ high-level prompt
/plan     # Create technical implementation plan  
/tasks    # Break down thành actionable tasks
```

## Tại sao approach này hoạt động

Language models giỏi pattern completion nhưng không giỏi mind reading. Vague prompt như "add photo sharing to my app" buộc model guess hàng nghìn unstated requirements.

Spec rõ ràng + plan + focused tasks = coding agent biết what to build, how to build, và in what sequence.

## 3 scenarios phù hợp nhất

1. **Greenfield (0→1):** Upfront spec đảm bảo AI build what you actually intend
2. **Feature work (N→N+1):** Phổ biến nhất — spec buộc clarity về cách feature interact với existing system
3. **Legacy modernization:** Capture essential business logic trong modern spec, redesign, để AI rebuild without inherited tech debt

## Hướng đi

Chuyển từ "code is source of truth" → "intent is source of truth." Spec trở thành executable artifact — khi spec tự động thành working code, nó quyết định what gets built.

## Links

- Spec Kit: https://github.com/github/spec-kit
- Post cũ của tác giả (heeki): https://heeki.medium.com/using-spec-driven-development-with-claude-code-4a1ebe5d9f29