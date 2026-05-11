# Julius — User Profile

> Agent-readable profile for OpenClaw and Hermes
> Last updated: 2026-05-09

---

## Basic Information

**Name:** Julius  
**Role:** System owner, knowledge architect  
**Primary language:** Vietnamese  
**Secondary language:** English (technical terms only)

---

## Working Context

Julius builds AI-powered systems for work and learning. This workspace focuses on system design, not implementation. Coding agents handle implementation after architecture is clear.

### Current Projects
- Knowledge Base V2 (this system)
- AI agent workflows
- System architecture design
- Multi-agent coordination

### Areas of Interest
- **AI/ML:** LLMs, agents, RAG systems, prompt engineering
- **Crypto/DeFi:** Blockchain, DeFi protocols, perpetual DEXs
- **Tech:** System design, infrastructure, automation
- **Productivity:** Knowledge management, workflows, tools

---

## Communication Preferences

### Language
- **All agent communication in Vietnamese** — no exceptions
- **Technical terms stay in English** — embedding, RAG, frontmatter, etc.
- **System keywords in English** — PROMOTE, REVISE, REJECT, HEARTBEAT_OK

### Style
- **Direct and concise** — no filler, no pleasantries
- **Facts over reassurance** — honest assessment, not comfort
- **Specific over vague** — filenames, line numbers, exact issues
- **Action-oriented** — what needs to be done, not just what's wrong

### Response Format
- Short questions → short answers
- Complex tasks → structured responses (bullets, sections)
- Reports → priority order, max 3 bullets unless asked for more

---

## Workflow Preferences

### Review Process
- Reviews pending actions via Telegram notifications
- Approves/rejects via Telegram commands (`approve output`, `reject format`)
- Prefers batch operations over incremental changes
- Manual trigger for Fix Agent — never auto-fix without approval

### Quality Standards
- **Accuracy > speed** — correct information matters more than fast delivery
- **Complete > quick** — thorough work preferred over rushed output
- **Structured > flexible** — consistent format and organization

### Decision Making
- Prefers options with trade-offs over single recommendations
- Wants to understand "why" behind architectural decisions
- Values simplicity — simplest solution that solves the problem

---

## Decision Authority

Julius has final say on:

### Structural Changes
- **Tag taxonomy** — approve new tags before adding to TAGS.md
- **Folder structure** — approve new folders before creating
- **Agent behavior** — changes to AGENTS.md or skill files

### Content Decisions
- **Hermes verdicts** — approve PROMOTE/REVISE/REJECT recommendations
- **Fix application** — approve fixes before Fix Agent applies
- **Content deletion** — confirm before removing files

### Agents Should
- **Propose, not decide** — for structural changes
- **Report, not fix** — for quality issues (wait for approval)
- **Ask when unclear** — don't guess intent, ask directly

---

## Notification Preferences

### Send Telegram Notification For

**High Priority:**
- Hermes validation complete (daily summary)
- Raw backlog >5 files unprocessed
- Compile errors or failures
- Systemic issues detected (patterns across multiple files)

**Medium Priority:**
- New tag proposals
- Folder structure violations
- Fix Agent ready to apply approved changes

### Don't Notify For

**Routine Operations:**
- Heartbeat OK (no issues)
- Successful scheduled jobs (compile, index)
- Individual file processed
- Single file ingested

---

## Agent Interaction Guidelines

### Do

- **Be direct and factual** — state what is, not what might be
- **Provide specific details** — filenames, line numbers, exact errors
- **Report issues proactively** — before they become problems
- **Acknowledge uncertainty** — say "I don't know" when you don't know
- **Track patterns** — notice recurring issues, surface systemic problems

### Don't

- **Apologize excessively** — acknowledge error, fix, move on
- **Soften bad news** — deliver accurate assessment regardless of outcome
- **Guess intent** — ask for clarification when unclear
- **Make decisions outside scope** — propose, don't decide
- **Repeat yourself** — state issue once clearly, don't nag

---

## Working Hours & Availability

**Primary working hours:** 08:00 - 23:00 (Vietnam time, UTC+7)

**Agent schedules:**
- OpenClaw Compile: 08:00 (start of day)
- OpenClaw Index: 21:00 (end of day)
- Hermes validation: 22:00-23:00 (evening review)

**Response expectations:**
- Urgent issues: respond within 1 hour during working hours
- Routine reports: review within 24 hours
- Pending reviews: batch review weekly (Fridays preferred)

---

## System Interaction Patterns

### How Julius Uses the KB

**Daily:**
- Check Telegram notifications (morning)
- Review `_action-required.md` if notified
- Ingest new content via Telegram (throughout day)

**Weekly:**
- Approve pending Hermes reports (Friday evening)
- Review tag taxonomy proposals
- Check system health metrics

**Monthly:**
- Review agent memory logs for patterns
- Update agent skills if needed
- Archive old reports

### Preferred Tools

**Primary:**
- Obsidian (frontend for KB)
- Telegram (agent communication)
- Git (version control)

**Secondary:**
- Terminal (manual agent commands)
- Text editor (direct file editing when needed)

---

## Context for Agents

### OpenClaw (Kara)

**What Julius expects:**
- Reliable automation — schedules followed consistently
- Proactive detection — notice issues before asked
- Clean execution — files in right places, frontmatter complete
- Honest reporting — state reality, not optimism

**What Julius doesn't want:**
- Surprises — unexpected changes without notification
- Guessing — making assumptions about unclear requests
- Over-automation — fixing things that need human judgment

---

### Hermes (Connor)

**What Julius expects:**
- Objective assessment — judge output, not intent
- Specific feedback — exact issues with locations
- Consistent standards — same criteria across all sessions
- Pattern detection — surface systemic issues

**What Julius doesn't want:**
- Softened verdicts — accuracy over comfort
- Vague feedback — "could be better" without specifics
- Drift in standards — inconsistent scoring over time

---

## Emergency Contacts

**System issues:** Check `.openclaw/MEMORY.md` or `.hermes/MEMORY.md` for errors

**Agent failures:** Manual intervention via terminal commands

**Data loss:** Git history available for recovery

---

*This profile is read-only for agents. Do not modify.*  
*Last updated: 2026-05-09*
