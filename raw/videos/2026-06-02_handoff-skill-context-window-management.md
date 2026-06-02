---
type: raw
source_type: video
source_url: https://www.youtube.com/watch?v=dtAJ2dOd3ko
date_ingested: 2026-06-02
tags: [ai, tools, productivity]
status: unprocessed
---

# Handoff Skill — Context Window Management for AI Coding Agents

**Channel:** YouTube  
**URL:** https://www.youtube.com/watch?v=dtAJ2dOd3ko  
**Date:** 2026-06-02  
**Type:** video

---

## Summary

A video explaining the Handoff Skill — a custom-built skill to manage context window when working with AI coding agents. As coding sessions drag on, the context window fills up and output quality degrades dramatically (the "dumb zone"). Even though Claude Code has 1M tokens of context, in reality only ~120K tokens remain "smart." The solution: instead of compacting summaries, hand off specific pieces of context to separate, focused sessions.

---

## The Problem

- Long coding sessions fill up context window → output quality drops severely ("dumb zone")
- Claude Code has 1M token context, but ~120K tokens is the practical limit for "smart" responses
- The longer the session, the more "confused" the agent becomes

## Old Solution — Compact

- Summarize current conversation → reset context
- Still 1 single session, accumulates "sediment" (residue from previous compacts)

## New Solution — Handoff Skill ✨

- Take a specific part of context (e.g., 1 bug fix, 1 feature) → transfer to a separate session
- Original session stays clean and focused

---

## 3 Usage Patterns

### 🔀 Handoff when grilled

**Pattern:** During planning, discover out-of-scope task → handoff to another session, keep main flow clean.

### 🧪 Handoff for prototyping

**Pattern:** Complex UI/experimentation needed → push to separate prototype session (~169K tokens!), handoff back when done.

### 🔄 Cross-agent handoff

**Pattern:** Since it's markdown, can pass from Claude Code → Codex → Copilot CLI, enabling adversarial review across different agents.

---

## Skill Principles

1. **Store handoff file in temp directory** — delete when done, don't stink up the codebase
2. **Include suggested skills for new session**
3. **Don't duplicate content from other artifacts** — use pointers only
4. **Redact sensitive info** (API keys, passwords)
5. **Always write clear purpose for next session**

---

## Key Concepts

- [[context-window-management]] — Context Window Management
- [[handoff-skill]] — Handoff Skill
- [[ai-coding-agents]] — AI Coding Agents
- [[session-separation]] — Session Separation
- [[cross-agent-workflow]] — Cross-Agent Workflow
- [[compact-vs-handoff]] — Compact vs Handoff

---

*A great video about context management techniques for AI coding agents — instead of stuffing everything into one session until it gets confused, split into multiple focused sessions using markdown files as bridges.*
