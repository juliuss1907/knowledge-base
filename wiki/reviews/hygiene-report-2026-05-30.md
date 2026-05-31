# Hygiene Inspector Report — 2026-05-30

**Validator:** Connor (Hermes-RK800)
**Scope:** KB folder structure + file organization
**Total folders checked:** 7 (wiki/sources, wiki/concepts, wiki/tag, wiki/topic, wiki/meta, wiki/reviews, drafts)

## Issues Found: 2

### WARNING — Unauthorized folders at root level

**1. `memory/`** — legacy folder at root
- Location: `/home/julius/knowledge-base/memory/`
- Issue: Per folder-structure.md v1.2, this should be `.openclaw/memory/`
- Contains: `2026-05-28.md` + `.dreams/` subfolder (events.jsonl, short-term-recall.json)

**2. `search/`** — not in allowed folder whitelist
- Location: `/home/julius/knowledge-base/search/`
- Issue: Not in allowed list (allowed: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`)
- Contains: `docs/appearance/google-images.md`, `docs/fundamentals/get-started-developers.md`

### ✅ Passing

- Folder structure intact (all required folders present)
- No .bak/.tmp files
- No orphan files
- Reviews folder clean

---

## Verdict

**REVISE** — 2 unauthorized folders need removal or relocation.

Note: These are root-level hygiene issues, not KB content. Kara's scope is wiki/ files only — Julius needs to handle memory/ and search/ personally.

Approved by Julius (via _action-required.md).