---
type: repo
title: SOP Writer — Claude AI Skill
url: https://github.com/aiskilloftheweek/claude-ai-skill-of-the-week/blob/main/skills/008-sop-writer/SKILL.md
author: aiskilloftheweek
date_ingested: 2026-06-27
status: unprocessed
source: github.com
---

# SOP Writer — Claude AI Skill

**Source:** aiskilloftheweek/claude-ai-skill-of-the-week — Skill #008

## Overview

A Claude AI skill that transforms any process description — however rough, incomplete, or disorganized — into a clear, delegatable Standard Operating Procedure (SOP). Works for solopreneurs, ops managers, and founders alike.

**When to trigger:** User wants to document a process, create a procedure for a team member or VA, build an operations manual, standardize a workflow, or says phrases like "write an SOP for this", "help me document this process", "I need to delegate this", "create a procedure for my VA", "turn this into a checklist someone else can follow".

## Input Classification

| Type | Signals | Action |
|---|---|---|
| Verbal / stream of consciousness | Informal, jumps around, missing sequence | Run full elicitation |
| Disorganized bullets | Has structure but missing tool/trigger/output details | Run partial elicitation |
| Semi-structured description | Steps in order, some tools mentioned | Fill gaps only, then produce |
| Loom transcript / audio dump | Long, repetitive, with digressions | Extract, then confirm before producing |

If input too vague: ask "Can you describe what happens from start to finish when you run this process — even roughly?"

## Process Type Classification

- **Type A — Delegation to VA/contractor:** process executed by someone external
- **Type B — Editorial / content process:** publishing, writing, content workflows
- **Type C — Onboarding:** new client, new hire, new tool rollout
- **Type D — Recurring operational:** daily/weekly/monthly repeating tasks
- **Type E — Crisis / exception handling:** non-standard situations, escalations

If unclear: ask "Who will be running this process?" and "Is this something that happens on a schedule, or when something specific occurs?"

## Mandatory Fields to Elicit

- Process name, Executor (role), Trigger, Expected output, Tools involved, Frequency

**Elicitation rule:** If 3+ missing → ask in one block (max 3 questions). If 1-2 missing → ask 1 question then proceed. If 0 missing → produce SOP directly. Never run a questionnaire.

**Key elicitation questions:**
- "What kicks this process off?"
- "When this process is finished correctly, what's different in the world?"
- "Has this process ever gone wrong? What happened?"
- "Is there any step where the person has to make a judgment call?"

## Output Format by Destination

| Destination | Format |
|---|---|
| Notion / Obsidian | Markdown with section emoji |
| Google Docs / Word | Clean Markdown, no emoji |
| ClickUp / Asana | Flat numbered steps, no nesting |
| Email to VA | Flowing text, steps in bold |
| Not specified | Default: Markdown with emoji |

**Detail level:** VA/external → expanded (where to click, what to type). Founder/self → compact (one line per step).

## Universal SOP Template

```markdown
# [PROCESS NAME]

**Version:** 1.0 | **Created:** [date] | **Review by:** [date + 6 months]

---

## 📋 Process overview
- **Executed by:** [role]
- **Trigger:** [what starts this process]
- **Frequency:** [how often]
- **Estimated time:** [X minutes / hours]
- **Expected output:** [what is objectively true when done]

---

## 🛠️ Tools required
- [Tool name] — [what it's used for]

---

## 📝 Steps
1. **[Action verb] [what]** — [where / in which tool]
2. ...

---

## ⚠️ Edge cases & exceptions
- If [situation X occurs] → [do Y instead]
- If [something is missing] → [escalate to / default to]
- If unsure → [decision rule or who to contact]

---

## ✅ Completion checklist
- [ ] [Verifiable output 1]

---

## ❓ FAQs
**Q:** [First-timer question]
**A:** [Answer]

---

## 🧪 Delegability test
- [ ] Someone with zero context could complete it using only this document
- [ ] Every tool mentioned is accessible to the executor
- [ ] Edge cases cover situations that have actually occurred
- [ ] Expected output is verifiable — not subjective
```

## Type-Specific Variants

### Type A — Delegation to VA
- Expand FAQs to 5-7 questions
- Add "If unclear, [specific action]" under each complex step
- Add escalation path (who to contact, how, response time)
- Expanded step format: 3a, 3b, 3c sub-steps

### Type B — Editorial / Content
- Add "Quality criteria" (objective standards, e.g., "Title under 60 chars")
- Add "Common mistakes" — 3-5 things that go wrong

### Type C — Onboarding
- Replace "Frequency" with "Timeline"
- Steps by time: Day 1 / Week 1 / Month 1
- Add "Milestones" and "Success criteria at 30 days"

### Type D — Recurring Operational
- Estimated time per step alongside each step
- Add "Anomaly signals" — early warning signs
- Compress FAQs; expand Completion checklist

### Type E — Crisis / Exception Handling
- Lead with decision matrix: IF [A] → Step 3, IF [B] → Step 7, IF [C] → Escalate
- Label every step: [CRITICAL] / [STANDARD] / [OPTIONAL]
- Add "Post-resolution checklist"

## Quality Verification (Pre-Delivery)

- Every step uses active verb ("Open", "Click", "Send", "Copy")
- Every tool mentioned is confirmed to exist
- At least one edge case included
- Delegability Test block present
- No invented steps
- Format matches destination
- Detail level matches executor

## Rules

- Always produce SOP in the same language the user writes in
- Even simple processes (<5 steps) get full structure — value is in format, not just steps
- If user says "just give me the steps, no template", respect that but always append Delegability Test
- Never fabricate specific steps, tool names, or criteria not described by user
- Mark unresolvable gaps with [TO COMPLETE]

## Example

**User input:** "When I get a new client inquiry from the contact form, I check if they fit, schedule a call, and send them the onboarding doc after."

**Skill response:**
- Classifies as Type C (onboarding), asks who runs it
- Identifies missing: tools, trigger specifics, expected output, edge cases
- Asks (max 3): "Which tools for scheduling and onboarding doc?" + "What makes someone a 'fit'?"
- Produces SOP with decision criteria for fit/no-fit as edge case
