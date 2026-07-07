---
type: raw
source_type: article
source_url: https://x.com/trq212/status/2073100352921215386
source_name: X (Twitter) — X Article
author: Thariq (@trq212)
title: "A Field Guide to Fable: Finding Your Unknowns"
date_ingested: 2026-07-06
date_published: 2026-07-03
tags: [ai, productivity, coding]
status: processed
compiled_at: 2026-07-07
compiled_to: "[[src_field-guide-to-fable-finding-unknowns]]"
---

# A Field Guide to Fable: Finding Your Unknowns

**Author:** Thariq (@trq212)
**Source:** X Article
**Published:** 2026-07-03
**Engagement:** 7,869 likes · 990 RT · 232 replies · 17,865 bookmarks

---

Working with Claude Fable 5 keeps re-teaching an old lesson: **the map is not the territory.**

The map = your prompts, skills, context — what you give Claude. The territory = the codebase, real world, its actual constraints. The gap between them = **unknowns**. Fable is the first model where the quality of work is bottlenecked by your ability to clarify its unknowns.

---

## Knowing Your Unknowns (Rumsfeld framework applied to coding)

| Category | Definition |
|---|---|
| **Known Knowns** | What's in your prompt. What you tell the agent you want. |
| **Known Unknowns** | What haven't you figured out yet, but you're aware of it? |
| **Unknown Knowns** | What's so obvious you'd never write it down, but would recognize if you saw it? |
| **Unknown Unknowns** | What haven't you considered at all? Do you know how good something can be? |

The best agentic coders (like Boris, Jarred) have relatively few unknowns. They're deeply in-sync with both the codebase and model behaviors. **Reducing and planning for your unknowns is the skill of agentic coding.**

---

## Pre-implementation Techniques

### 1. Blind Spot Pass
Ask Claude to find your unknown unknowns before you start.

> "I'm working on adding a new auth provider but I know nothing about the auth modules in this codebase. Can you do a blindspot pass to help me figure out my relevant unknown unknowns?"

### 2. Brainstorms and Prototypes
When involving criteria you only know to define when you see it (unknown knowns). Visual design is hard to articulate but you know it when you see it.

> "Make me an HTML page with 4 wildly different design directions so I can react to them."

### 3. Interviews
Ask Claude to interview you one question at a time about ambiguities, prioritizing questions where your answer would change the architecture.

### 4. References
The best reference is source code. Point Fable at a folder/library and tell it what to look for, even in a different language.

> "This Rust crate implements the exact backoff behavior I want. Read it and reimplement the same semantics in TypeScript."

### 5. Implementation Plans
Before coding, ask Claude for a plan that surfaces decisions you're most likely to change: data models, type interfaces, UX flows.

---

## During Implementation

### Implementation Notes
No matter how much planning, unknown unknowns always lurk. Ask Claude Code to keep a temporary `implementation-notes.md` tracking decisions made.

> "Keep an implementation-notes.md. If you hit an edge case that forces deviation, pick the conservative option, log it under 'Deviations', and keep going."

---

## Post-implementation

### Pitches and Explainers
Package prototype + spec + implementation notes into a single doc for buy-in.

### Quizzes
After a long session, ask Claude to quiz you on the changes. Only merge after passing perfectly.

> "Give me an HTML report on the changes with context, intuition, what was done, and a quiz at the bottom."

---

## How This Comes Together: Launching Fable

Thariq edited the Fable launch video entirely with Claude Code:
1. Known Knowns: Claude could edit videos + transcribe
2. Unknown Unknowns: Could ffmpeg accurately cut ums/pauses? → Claude explained Whisper
3. Unknown Knowns: Wanted timed UI with words → Claude prototyped with Remotion
4. Unknown Unknowns: Video looked muted → asked Claude to teach him color grading

---

## Bottom Line

> "Every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out what you didn't know before it gets expensive to fix. Start your next project by asking Claude to help you find your unknowns."
