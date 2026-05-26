# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-27 — 2026-05-26 reports: Output approved, Format partial approved, Hygiene partial approved

---

## Summary

**Pending reports:** 0

**Status:**
- ✅ Output Validator — 2026-05-26: **approved** (2 ERROR + 4 WARNING → Kara fix)
- 🔶 Format Validator — 2026-05-26: **partial approved** — individual file fixes only (4 new files with source_type/source_url), SKIP compile-agent/SKILL.md
- 🔶 Hygiene Inspector — 2026-05-26: **partial approved** — .gitkeep fixes only, KEEP RAW_BACKLOG.md + HEARTBEAT.md
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

---

## Critical Issues (Fix Immediately)

- **Format 2026-05-26 — FILE FIXES ONLY:** 4 new files (src_ai-trillion-dollar-blind-spot, src_will-ai-replace-systems-thinking, static-website-blind-spot, ai-augmented-systems-thinking) use wrong fields (`source_type`/`source_url`) — Fix Agent to replace with correct `original` field per format-spec. Also fix section names (`Key Points`→`Key points`, `Related Concepts`→`Concepts referenced`), remove extra sections (`Opportunity`, `Backlinks`, `Notes`), fix `marketing` and `system` sub-tags. Compile Agent SKILL.md template is CORRECT as-is.
- **Output 2026-05-24:** 11 broken wikilinks → systematic, requires Compile Agent re-run

---

## Warnings (Can Fix Later)

- Hygiene 2026-05-26: 2 WARNING — `.gitkeep` in `wiki/topic/` + `wiki/drafts/`
- Hygiene 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`
- Hygiene 2026-05-22: 1 INFO — `raw/raw.md` spec gap

---

## Pending Reports

*None — all reports processed*

---

## Recently Applied

- [x] **Output Validator — 2026-05-26**: 2 ERROR (definition too short) + 4 WARNING → Kara fix
- [x] **Format Validator — 2026-05-26**: COMPILE AGENT TEMPLATE FIX ONLY — update compile-agent/SKILL.md to match format-spec.md v2.0. Specific file fixes SKIPPED.
- [x] **Hygiene Inspector — 2026-05-26**: .gitkeep cleanup only. **KEEP** `raw/RAW_BACKLOG.md` and `wiki/reviews/HEARTBEAT.md** — Julius decision to retain these files.
- [x] Hygiene Inspector — 2026-05-22: memory/ → .openclaw/memory/, RAW_BACKLOG.md deleted (now re-created — intentional)
- [x] Format Validator — 2026-05-22: extra sections ×3, YAML syntax ×3, legacy fields ×2, field order ×2
- [x] Output Validator — 2026-05-22: Empty Original excerpts, Empty Notes systematic, Too many key points ×6, Broken wikilinks ×17

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