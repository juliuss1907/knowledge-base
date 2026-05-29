# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-29 11:20 — Output Validator scan complete (4 issues: 1 ERROR + 2 WARNING + 1 INFO)

---

## Summary

**Pending reports:** 3

**Status:**
- ⏳ Output Validator — 2026-05-29: PENDING (1 ERROR: softbank-carry-trade empty Sources body)
- ⏳ Hygiene Inspector — 2026-05-29: PENDING (32 missing concept files → OpenClaw compile needed)
- ⏳ Format Validator — 2026-05-28: PENDING (80 ERROR — wikilinks not quoted)
- ✅ Output Validator — 2026-05-28: PENDING (7 issues from yesterday — carried forward)
- ✅ Hygiene Inspector — 2026-05-28: approved (memory/ merged, RAW_BACKLOG.md deleted, venv kept)
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

**33 ERRORs found (32 Hygiene + 1 Output):**
- 32 wikilinks in source files point to concept files that don't exist yet → see: `wiki/reviews/2026-05-28_hygiene-report.md`
- 1 Output Validator: softbank-carry-trade.md has empty `## Sources` section body despite frontmatter having sources listed

---

## Warnings (Can Fix Later)

*None*

---

## Systematic Issues (No File-Level Fix — SKIP)

*None*

---

## Pending Reports

*None — all reports approved*

---

## Recently Applied

- [x] **Output + Format + Hygiene — 2026-05-28**: All 3 reports fixed (Kara + Julius manual: HTTP→HTTPS, hygiene cleanup)
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