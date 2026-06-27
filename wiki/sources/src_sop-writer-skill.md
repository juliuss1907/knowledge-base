---
type: source
original: "[[2026-06-27_sop-writer-skill]]"
main_tag: productivity
sub_tags: [tools, automation]
topic: sop-writer
date_compiled: 2026-06-27
url: https://github.com/aiskilloftheweek/claude-ai-skill-of-the-week/blob/main/skills/008-sop-writer/SKILL.md
author: aiskilloftheweek
---

# SOP Writer — Claude AI Skill

## Metadata

- **Author:** aiskilloftheweek
- **Source:** GitHub (claude-ai-skill-of-the-week #008)
- **URL:** https://github.com/aiskilloftheweek/claude-ai-skill-of-the-week/blob/main/skills/008-sop-writer/SKILL.md
- **Type:** repo / AI skill definition

## Summary

Một Claude AI skill giúp chuyển đổi bất kỳ mô tả quy trình nào — dù thô, không đầy đủ, hoặc lộn xộn — thành một Standard Operating Procedure (SOP) rõ ràng, có thể ủy thác. Skill phân loại input thành 4 kiểu (verbal, bullets rời rạc, mô tả bán cấu trúc, transcript), phân loại quy trình thành 5 type (delegation, editorial, onboarding, recurring operational, crisis), và tạo SOP với cấu trúc chuẩn gồm process overview, tools, steps, edge cases, completion checklist, FAQs, và delegability test. Điểm khác biệt: skill này chủ động elicit thông tin còn thiếu thay vì chỉ format lại input có sẵn.

## Key points

- 4 kiểu input: verbal/stream of consciousness, disorganized bullets, semi-structured, transcript. Mỗi kiểu có action khác nhau (full elicitation, partial elicitation, fill gaps, extract + confirm).
- 5 process types: Delegation (VA/contractor), Editorial, Onboarding, Recurring Operational, Crisis/Exception. Mỗi type có biến thể template riêng.
- Elicitation rule: 3+ fields missing → hỏi max 3 câu. 1-2 missing → hỏi 1 câu. 0 missing → produce ngay. Không bao giờ chạy questionnaire.
- Universal SOP template: Process overview → Tools required → Steps → Edge cases → Completion checklist → FAQs → Delegability test.
- Delegability test: 4 câu hỏi xác minh SOP có thể giao cho người zero context thực hiện được không.
- Output format thích ứng với destination (Notion/Obsidian, Google Docs, ClickUp, Email) và executor level (expanded cho VA, compact cho founder).
- Chất lượng: mọi step dùng active verb, edge case bắt buộc, không bịa steps không được mô tả.

## Concepts referenced

- [[standard-operating-procedure]]

## Original excerpts

> "Turns any process description — bullet points, voice transcripts, half-explained workflows, or detailed outlines — into a structured, delegatable Standard Operating Procedure."
