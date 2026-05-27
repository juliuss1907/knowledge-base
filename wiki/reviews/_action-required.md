# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-27 07:54 — Hygiene report pending

---

## Summary

**Pending reports:** 1

**Status:**
- ⏳ **Hygiene Inspector — 2026-05-27:** pending (4 issues: 1 ERROR + 2 WARNING + 1 INFO)
- ✅ Output Validator — 2026-05-27: approved (11 issues)
- ✅ Format Validator — 2026-05-27: approved (20 issues)
- ✅ Output Validator — 2026-05-26: approved (2 ERROR + 4 WARNING → Kara fix)
- ✅ Format Validator — 2026-05-26: approved (4 new files — source_type/source_url → original, section names, tags)
- ✅ Hygiene Inspector — 2026-05-26: approved (.gitkeep in topic/ + drafts/)
- ✅ Format Validator — 2026-05-24: approved
- ✅ Hygiene Inspector — 2026-05-24: approved
- ✅ Output Validator — 2026-05-22: approved
- ✅ Format Validator — 2026-05-22: approved
- ✅ Hygiene Inspector — 2026-05-22: approved

**Resolved reports:**
- [x] Output Validator — 2026-05-14 (4 issues)
- [x] Format Validator — 2026-05-14 (3 issues)
- [x] Format Validator — 2026-05-17 (5 issues)
- [x] Hygiene Inspector — 2026-05-14 (14 issues)
- [x] Hygiene Inspector — 2026-05-17 (20 issues)
- [x] Hygiene Inspector — 2026-05-20 (6 issues)
- [x] Output Validator — 2026-05-21 (11 issues)
- [x] Format Validator — 2026-05-21 (20 issues)
- [x] Hygiene Inspector — 2026-05-21 (9 issues)
- [x] Hygiene Inspector — 2026-05-22 (3 ERROR + 2 issues)
- [x] Format Validator — 2026-05-22 (11 WARNING)
- [x] Output Validator — 2026-05-22 (16 issues)
- [x] Format Validator — 2026-05-24 (2 ERROR resolved + 3 WARNING)
- [x] Hygiene Inspector — 2026-05-24 (1 ERROR + 1 INFO)
- [x] Output Validator — 2026-05-24 (all 20 issues)
- [x] Format Validator — 2026-05-26 (all 17 ERROR + 3 WARNING)
- [x] Hygiene Inspector — 2026-05-26 (all 2 ERROR + 2 WARNING)
- [x] Output Validator — 2026-05-27 (11 issues)
- [x] Format Validator — 2026-05-27 (20 issues)

---

## Critical Issues (Fix Immediately)

- **Hygiene 2026-05-27 — ERROR #1:** `memory/` folder at root level — migrate to `.openclaw/memory/` per spec v1.2
- **Output 2026-05-27 — ERROR #3:** create stubs for `systems-thinking` and `second-order-effects` (dangling wikilinks in ai-augmented-systems-thinking.md, src_will-ai-replace-systems-thinking.md, human-judgment-ai.md)
- **Format 2026-05-27 — 5 STUB FILES:** `status: stub` → `draft`, add `## Key ideas`, fill `sources` array (ai-powered-discovery, ai-productivity, conversational-website, generative-ai-seo, human-judgment-ai)
- **Format 2026-05-27 — 2 INVALID SUB-TAGS:** ai-productivity (`productivity` → replace with Pool B), generative-ai-seo (`marketing` → replace or propose)
- **Format 2026-05-27 — OTHER:** section case (static-website-blind-spot), code block language (x-search-tool.md), field order (2 source files)
- **Output 2026-05-27 — WARNINGS:** Summary short (2 files), Duplicate Notes (cynefin-framework.md), Missing Original excerpts (3 files), empty Backlinks/Notes (2 files)

---

## Warnings (Can Fix Later)

- **Hygiene 2026-05-27 — WARNING #2:** HEARTBEAT.md at root is regular file, not symlink → replace with symlink
- **Hygiene 2026-05-27 — WARNING #3:** `venv-3.11` and `venv-3.12` in `.openclaw/skills/news-brief-skill/` — move or gitignore
- Hygiene 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`
- Output 2026-05-27: 5 stubs missing Key ideas — extend when time allows

---

## Systematic Issues (No File-Level Fix — SKIP)

- **Hygiene 2026-05-27 — INFO #4:** 4 `.bak`/`.tmp` files in `.openclaw/devices/` and `.openclaw/` — clean up stale backup files

---

## Pending Reports

*None — all reports approved*

---

## Recently Applied

- [x] **Output Validator — 2026-05-27**: 3 ERROR (duplicate Notes, missing excerpts, dangling wikilinks) + 5 WARNING
- [x] **Format Validator — 2026-05-27**: 14 ERROR + 6 WARNING (5 stub concept fixes, field order, code block)
- [x] **Output Validator — 2026-05-26**: 2 ERROR (definition too short) + 4 WARNING → Kara fix
- [x] **Format Validator — 2026-05-26**: 4 files fixed — source_type/source_url → original, Key Points → Key points, Related Concepts → Concepts referenced, remove extra sections, fix sub-tags
- [x] **Hygiene Inspector — 2026-05-26**: .gitkeep removed from topic/ + drafts/
- [x] Hygiene Inspector — 2026-05-22: memory/ → .openclaw/memory/, RAW_BACKLOG.md, HEARTBEAT.md
- [x] Format Validator — 2026-05-22: extra sections ×3, YAML syntax ×3, legacy fields ×2, field order ×2
- [x] Output Validator — 2026-05-22: Empty Original excerpts, Empty Notes systematic, Too many key points ×6, Broken wikilinks ×17
- [x] Format Validator — 2026-05-24: sources-as-string → format-spec updated to accept string OR array
- [x] Hygiene Inspector — 2026-05-24: EOF files deleted
- [x] Output Validator — 2026-05-24: wikilinks, excerpts, last_updated, Empty Notes systematic

---

## Commands

**To approve a report:**
approve output
approve format
approve hygiene

**To view full report:**
show output
show format
show hygiene

**To apply approved fixes:**
openclaw fix apply