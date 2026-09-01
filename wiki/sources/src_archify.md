---
type: source
original: "[[2026-08-30_tt-a1i_archify]]"
main_tag: tech
sub_tags: [tools, coding, automation]
topic: architecture-as-code
date_compiled: 2026-08-31
url: https://github.com/tt-a1i/archify
author: tt-a1i
---

# Archify

## Metadata

- **Author:** tt-a1i
- **Published:** [unknown]
- **Source:** github.com
- **URL:** https://github.com/tt-a1i/archify
- **Type:** repo

## Summary

Archify là hệ thống rendering và validation bằng Node.js dành cho Cursor, Claude Code, Codex CLI và OpenCode — biến codebase hoặc mô tả hệ thống thành system map tương tác, đẹp ngay trong chat. Agent sản xuất typed JSON IR, Archify deterministically compile thành HTML/SVG. Nó hỗ trợ 5 loại diagram, 4 presets, dark/light themes, và cho phép so sánh kiến trúc Before/Delta/After với validation receipt. Điểm mạnh cốt lõi: agent có layout judgment thay vì generic auto-layout, atomic validation trước khi deliver, và mọi tương tác đều grounded trong authored nodes (không tự bịa topology).

## Key points

- **Typed JSON IR:** Agent tạo JSON IR có schema; Archify deterministically compile thành HTML/SVG
- **5 loại diagram:** Architecture · Workflow · Sequence · Data Flow · Lifecycle
- **Atomic validation trước khi deliver:** Schema, layout, HTML/SVG, route, label clearance đều phải pass trước khi thay thế artifact tốt nhất trước đó
- **Layout judgment thay generic auto-layout:** Agent chọn hierarchy, spacing, routes, emphasis — endpoints tự dàn deterministic
- **Before/Delta/After compare:** So sánh hai validated snapshots với receipt, hiện added/removed/changed/moved/rerouted
- **Truthful interaction:** Upstream/downstream reach, routes, role comparison, stories đều reuse authored nodes — không bịa topology
- **Evidence-backed:** Kiến trúc có thể đánh dấu `SRC n` mở Git-verified files và line ranges pinned commit
- **Failure repair receipt:** `validate --json` trả rule codes, subject, evidence, supported fixes — không phải Node stack
- **Portable output:** Kết quả là 1 HTML file; exports PNG, SVG, WebM, 1200×630 share cards
- **Cài đặt đa nền tảng:** npx skills, ZIP manual, plugin — hỗ trợ Raven, Claude Code, Codex, opencode, DeepSeek Harness
- **Mermaid parsing ngoài scope:** Không phải Mermaid theme, không general-purpose drawing editor

## Concepts referenced

- [[architecture-as-code]]
- [[code-visualization]]
- [[system-map]]

## Original excerpts

> "Layout judgment over generic auto-layout — the agent chooses hierarchy, spacing, routes, and emphasis; shared automatic endpoints spread deterministically instead of piling arrows on one midpoint."

> "Failures come with a repair receipt — `validate --json` and `deliver --json` return stable rule codes, the exact subject, measured evidence, and only supported repair controls instead of a Node stack or an unstructured retry guess."
