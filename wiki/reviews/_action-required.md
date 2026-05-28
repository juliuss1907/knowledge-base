# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-28 08:26 — Output Validator complete, 3 reports pending

---

## Summary

**Pending reports:** 3

**Status:**
- ⏳ **Output Validator — 2026-05-28:** pending (3 ERROR + 2 WARNING + 2 INFO)
- ⏳ **Format Validator — 2026-05-28:** pending (22 ERROR + 2 WARNING)
- ⏳ **Hygiene Inspector — 2026-05-28:** pending (2 ERROR + 1 WARNING)
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

- **Output 2026-05-28 — ERROR:** Cross-contaminated excerpt in src_llm-need-sleep-consolidation.md — OPEC oil pricing excerpt leaked into LLM Sleep paper
- **Output 2026-05-28 — ERROR:** 15 dangling wikilinks across 8 new files — concepts referenced but never created
- **Output 2026-05-28 — ERROR:** Empty `## Sources` body in 3 concept files (ai-productivity, human-judgment-ai, generative-ai-seo)
- **Format 2026-05-28 — 21 ERRORs:** `original:` field in source files uses path/URL instead of wikilink format
- **Format 2026-05-28 — 1 ERROR:** systems-thinking.md sources array malformed (trailing `[]`)

---

## Warnings (Can Fix Later)

- **Output 2026-05-28 — WARNING:** Short summaries still unfixed in 2 source files (src_ai-trillion-dollar-blind-spot, src_will-ai-replace-systems-thinking — flagged 3 reports in a row)
- **Output 2026-05-28 — WARNING:** Systematic dangling wikilinks — Compile Agent may need prompt fix
- **Output 2026-05-28 — INFO:** 2 older dangling wikilinks in src_luke-alvoeiro-multi-agent-architecture-factory.md (orchestrator-worker-validator, agent-handoff)
- **Output 2026-05-28 — INFO:** Sources frontmatter/body mismatch in 3 concept files
- **Hygiene 2026-05-28 — 2 ERRORs:** `memory/` folder at root, `RAW_BACKLOG.md` stray file

---

## Systematic Issues (No File-Level Fix — SKIP)

- **Output 2026-05-28:** Dangling wikilinks systematic — 15 missing concepts from today + 2 from older files. Likely Compile Agent prompt issue: agent references sub-concepts without creating them.

---

## Pending Reports

- [ ] **Output Validator — 2026-05-28** (3 ERROR + 2 WARNING + 2 INFO, 7 issues)
- [ ] **Format Validator — 2026-05-28** (pending)
- [ ] **Hygiene Inspector — 2026-05-28** (pending)

---

## Recently Applied

- [x] **Output Validator — 2026-05-28**: Report generated — 7 issues (3 ERROR: cross-contaminated excerpt, 15 dangling wikilinks, empty Sources body; 2 WARNING; 2 INFO)
- [x] **Hygiene Inspector — 2026-05-27**: memory/ migrated, HEARTBEAT.md symlink, venvs deleted, .bak/.tmp cleaned (4 issues)
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