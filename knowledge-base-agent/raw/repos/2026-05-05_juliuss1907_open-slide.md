---
type: raw
source_type: repo
source_url: https://github.com/juliuss1907/open-slide
date_ingested: 2026-05-05
tags: [#ai, #coding]
status: unprocessed
---

# Open Slide — A Slide Framework Built for Agents

**Owner:** juliuss1907 (Julius)  
**Repo:** open-slide  
**Forked from:** 1weiho/open-slide  
**License:** MIT  
**Link:** https://github.com/juliuss1907/open-slide

---

## Tóm tắt

**Open Slide** là một slide framework được xây dựng cho agents — tạo presentation bằng AI agents.

---

## Kiến trúc

**Monorepo structure:**
- `apps/playground/` — Framework source và dev environment
- `packages/cli/` — CLI tool published as `openslide`
- `.agents/skills/` — Shared skills cho agents
- `.claude/skills/` — Claude-specific skills

---

## CLI Usage

```bash
npx openslide init [dir]
```

Scaffold một deck workspace từ template được sync.

---

## Key Features

- **Agent-native:** Built from ground up cho AI agents
- **Monorepo:** Turborepo + pnpm workspace
- **CLI tooling:** `openslide` npm package
- **Skills system:** Modular agent skills
- **Theme support:** Customizable themes

---

## Tech Stack

- TypeScript
- pnpm workspace
- Turborepo
- Changesets for versioning

---

## Recent Commits (bởi Julius)

- Restructure into monorepo with openslide CLI
- Decouple scaffolding template from playground
- Rename CLAUDE.md to AGENTS.md (cross-agent convention)
- Release packages workflow
