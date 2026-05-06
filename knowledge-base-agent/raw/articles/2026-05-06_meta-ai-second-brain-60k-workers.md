---
type: raw
source_type: article
source_url: https://medium.com/@AnalyticsAtMeta/how-we-built-an-ai-second-brain-for-60k-knowledge-workers-78c507dd795b
date_ingested: 2026-05-06
tags: [#ai, #productivity, #business]
status: unprocessed
---

# How We Built an AI Second Brain for 60K Knowledge Workers (Meta)

**Author:** Analytics at Meta  
**Link:** https://medium.com/@AnalyticsAtMeta/how-we-built-an-ai-second-brain-for-60k-knowledge-workers-78c507dd795b  
**Date:** April 29, 2026

---

## Tóm tắt

Meta xây dựng **AI Second Brain** — từ experiment trong analytics org đến **63,000+ users** across mọi function (engineers, PMs, designers, legal, finance, sales) chỉ trong 3 tháng.

---

## Vấn đề

Knowledge workers đối mặt với **workflow fragmentation** — thông tin (meeting notes, tasks, decisions, code context) nằm rải rác across platforms. Mỗi AI conversation bắt đầu "cold": phải giải thích lại context, mất 10 phút trước khi làm việc thực sự.

---

## 4 Components chính

**1. PARA Workspace**
- Dựa trên Tiago Forte's PARA method: **Projects, Areas, Resources, Archives**
- Agent hiểu được cấu trúc công việc — biết gì đang active, quan trọng, file mới đi đâu
- **Progressive disclosure:** root CLAUDE.md (identity + active portfolio) → project CLAUDE.md on demand
- Giải quyết context window limits — không load tất cả mọi thứ

**2. Infrastructure Layer (MCPs & CLIs)**
- Authenticated access vào internal tools: docs, messaging, task trackers, code reviews
- Agent có thể pull meeting transcripts, check tasks, read threads, write documents

**3. Agent (Claude Code + Harness)**
- Execution environment: filesystem access, tool calling, MCP integration, error recovery
- Agentic loop: reason → act → observe → repeat

**4. Skills (Markdown + Scripts)**
- Reusable workflows encoded as plain markdown
- Examples:
  - `/para-init` — bootstrap workspace từ recent activity
  - `/start-project` — create project từ brain dump
  - `/read-meeting-notes` — process transcripts, extract action items, route to projects
  - `/debrief:team` — generate manager-level team report

---

## Adoption: 0 → 63,000 in 3 Months

- **Inflection point:** Non-technical PM publish post "I finally built my second brain"
- Growth organic, viral — không có top-down directive
- **10,000 DAU**, 9 discipline-specific packages, team-level shared context system

---

## Key Learnings

1. **Infrastructure comes first** — authenticated access to internal tools separates useful agent from chatbot
2. **Progressive disclosure outperforms context dumping** — lean context up front, drill as needed
3. **Low-friction onboarding drives viral adoption** — `/para-init` removes biggest barrier
4. **Your users are your best builders** — community built most features after launch
5. **Composability creates more value than features** — skills là markdown files, anyone can extend

---

## What's Next

- **"Third Brain"** — team-level shared context system (piloting across dozens of teams)
- **Proactive agents** — run on schedules: morning briefings, automated meeting processing, end-of-day digests
