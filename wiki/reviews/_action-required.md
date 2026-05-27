# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-27 — Output + Format Validator reports pending review

---

## Summary

**Pending reports:** 2

**Status:**
- 🔴 Output Validator — 2026-05-27: pending (3 ERROR + 5 WARNING + 3 INFO)
- 🔴 Format Validator — 2026-05-27: pending (14 ERROR + 6 WARNING)
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

---

## Critical Issues (Fix Immediately)

- **Format 2026-05-27 — 5 STUB FILES:** ai-powered-discovery, ai-productivity, conversational-website, generative-ai-seo, human-judgment-ai — `status: stub` → `status: draft`, add `## Key ideas` section, fill `sources` array
- **Format 2026-05-27 — 2 INVALID SUB-TAGS:** ai-productivity (sub_tag 'productivity' → replace with Pool B tag), generative-ai-seo (sub_tag 'marketing' → replace or propose new tag)
- **Format 2026-05-27 — 2 FIELD ORDER:** src_ai-trillion-dollar-blind-spot, src_will-ai-replace-systems-thinking — reorder: main_tag, sub_tags, topic, date_compiled, author

---

## Warnings (Can Fix Later)

- Hygiene 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`
- raw/raw.md spec gap — folder-structure.md §6 now updated (FIXED)

---

## Systematic Issues (No File-Level Fix — SKIP)

*None — all issues now approved*

---

## Pending Reports

- 🔴 **Output Validator — 2026-05-27**: 3 ERROR + 5 WARNING + 3 INFO — [Report](2026-05-27_output-report.md)
- 🔴 **Format Validator — 2026-05-27**: 14 ERROR + 6 WARNING — [Report](2026-05-27_format-report.md)

---

## Recently Applied

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