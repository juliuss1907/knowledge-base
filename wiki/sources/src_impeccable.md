---
type: source
original: "[[2026-08-30_juliuss1907_impeccable]]"
main_tag: tech
sub_tags: [tools, coding, vibecode]
topic: ai-frontend-design-guidance
date_compiled: 2026-08-31
url: https://github.com/juliuss1907/impeccable
author: juliuss1907
---

# Impeccable

## Metadata

- **Author:** juliuss1907
- **Published:** [unknown]
- **Source:** github.com
- **URL:** https://github.com/juliuss1907/impeccable
- **Type:** repo

## Summary

Impeccable là design guidance dành cho AI coding agents — 1 skill, 23 commands, live browser iteration, và 59 deterministic detector rules để cải thiện thiết kế frontend do AI tạo ra. Khởi đầu từ Anthropic's frontend-design skill, Impeccable giải quyết vấn đề "mọi model trained trên cùng SaaS templates" dẫn đến cùng những dấu hiệu nhận diện (Inter cho mọi thứ, gradient tím-xanh, cards lồng cards, text xám trên nền màu). Nó thêm một setup flow (`/impeccable init` viết PRODUCT.md và DESIGN.md), 23 commands chia sẻ design vocabulary với AI, và 59 deterministic detector rules chạy không cần LLM hay API key. Hỗ trợ nhiều nền tảng: Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, Grok Build.

## Key points

- **23 commands:** craft, init, document, extract, shape, critique, audit, polish, bolder, quieter, distill, harden, onboard, animate, colorize, typeset, layout, delight, overdrive, clarify, adapt, optimize, live
- **59 deterministic detector rules:** CLI + browser extension chạy rules không cần LLM và không cần API key; LLM-only critique checks bổ sung
- **Setup flow:** `/impeccable init` viết PRODUCT.md và DESIGN.md để mọi command sau đọc context về audience, brand, voice, colors, type
- **Anti-patterns:** Không dùng overused fonts (Inter), không gray text trên colored background, không pure black/gray (luôn tint), không wrap mọi thứ trong cards, không bounce/elastic easing
- **Live browser iteration:** Visual variant mode `/impeccable live` iterate elements trực tiếp trong browser
- **Pin shortcuts:** `/impeccable pin audit` tạo `/audit` standalone
- **Cài đặt đa nền tảng:** CLI installer, git submodule, plugin, download ZIP, copy repo — hỗ trợ nhiều harness folders
- **Provider hooks:** Install provider-native hook manifest cho Claude Code, Cursor, Codex, Copilot, Grok Build
- **Codex trust:** Codex tracks trust theo hook definition — update `.codex/hooks.json` cần re-approve
- **Anti-patterns & anti-references:** Bộ quy tắc rõ ràng chống lại design tells phổ biến của AI

## Concepts referenced

- [[ai-frontend-design-guidance]]
- [[frontend-design-agent]]
- [[design-systems]]
- [[vibe-coding]]

## Original excerpts

> "Skip the guidance and you get the same handful of tells on every project: Inter for everything, purple-to-blue gradients, cards nested in cards, gray text on colored backgrounds, the rounded-square icon tile above every heading."

> "23 commands. A shared design vocabulary with your AI: `polish`, `audit`, `critique`, `distill`, `animate`, `bolder`, `quieter`, and more."