# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-24 08:05 — Output Validator run complete (17 new files validated, 20 issues found)

---

## Summary

**Pending reports:** 4

**Status:**
- 🔴 Output Validator — 2026-05-24: 1 ERROR (broken wikilinks) + 11 WARNING + 8 INFO — requires Compile Agent re-run
- ⚠️ Output Validator — 2026-05-22: 7 issues remaining (7 WARNING, 0 INFO after fixes) — awaiting review
- ℹ️ Format Validator — 2026-05-22: 5 issues remaining (0 ERROR, 5 WARNING, 0 INFO after fixes) — awaiting review
- 🔴 Hygiene Inspector — 2026-05-22: 2 issues remaining (0 ERROR, 1 WARNING, 1 INFO after fixes) — awaiting review

**Resolved reports:**
- [x] Output Validator — 2026-05-14 (4 issues: wikilink + warnings + info)
- [x] Format Validator — 2026-05-14 (3 issues: date_ingested removal + warnings)
- [x] Format Validator — 2026-05-17 (5 issues: extra fields, bracket syntax, broken wikilink)
- [x] Hygiene Inspector — 2026-05-14 (14 issues: folder-structure.md v1.1 + missing folders)
- [x] Hygiene Inspector — 2026-05-17 (20 issues: memory/ folder, stale files, runtime whitelist)
- [x] Hygiene Inspector — 2026-05-20 (6 issues: EOF, memory/, state/, stale backups)
- [x] Output Validator — 2026-05-21 (11 issues: empty sections, key ideas, typo, broken wikilinks)
- [x] Format Validator — 2026-05-21 (20 issues: section case, original wikilink, date_ingested — Compile Agent fixed)
- [x] Hygiene Inspector — 2026-05-21 (9 issues: stale backup files)
- [x] Hygiene Inspector — 2026-05-22 (3 ERROR fixed: memory/ → .openclaw/memory/, RAW_BACKLOG.md deleted, wiki/reviews/HEARTBEAT.md removed)
- [x] Format Validator — 2026-05-22 (6 WARNING fixed: extra sections ×3, YAML syntax ×2, legacy fields ×2)
- [x] Output Validator — 2026-05-22 (1 WARNING fixed: Empty Original excerpts)

---

## Critical Issues (Fix Immediately)

- **Output 2026-05-24:** 1 ERROR — 11 broken wikilinks referencing missing concept pages. Compile Agent must create: `agent-initiated-code-artifacts`, `multi-agent-systems`, `code-for-reasoning`, `code-for-action`, `code-for-environment-modeling`, `orchestrator-worker-validator`, `agent-handoff`, `harness-control`, `program-of-thoughts`, `supergrok-subscription`, `nous-research`
- **Hygiene 2026-05-22:** 3 ERROR — `memory/` stale dir at root, `RAW_BACKLOG.md` at root (not in whitelist), `wiki/reviews/HEARTBEAT.md` in wrong location

---

## Warnings (Can Fix Later)

- Output Validator 2026-05-22: 7 WARNING remaining — Empty Notes (systematic), Too many key points (needs Julius decision), Broken wikilinks (needs concept compilation)
- Format Validator 2026-05-22: 5 WARNING remaining — Field order (minor)
- Hygiene Inspector 2026-05-22: 1 WARNING — `.gitkeep` naming in `wiki/topic/`

---

## Info & Suggestions

- Hygiene Inspector 2026-05-22: 1 INFO — `raw/raw.md` spec gap (missing from folder-structure.md Section 6)

---

## Pending Reports

- [ ] **Output Validator — 2026-05-22** (7 issues remaining: 7 WARNING after fixes applied by Kara)
  - WARNING: Empty Notes (systematic — needs Compile Agent template fix), key points overflow × 6 files (needs consolidation), broken wikilinks × 17 (needs concept compilation)
  - Report: wiki/reviews/2026-05-22_output-report.md

- [ ] **Format Validator — 2026-05-22** (5 issues remaining: 5 WARNING after fixes applied by Kara)
  - WARNING: Field order × 2 files (minor)
  - Report: wiki/reviews/2026-05-22_format-report.md

- [ ] **Hygiene Inspector — 2026-05-22** (2 issues remaining: 1 WARNING + 1 INFO after ERROR fixes applied by Kara)
  - WARNING: `.gitkeep` in `wiki/topic/` naming convention
  - INFO: `raw/raw.md` spec gap (missing from folder-structure.md Section 6)
  - Report: wiki/reviews/2026-05-22_hygiene-report.md

---

## Recently Applied

- [x] Output Validator — 2026-05-21 (approved 2026-05-22: empty sections, key ideas gaps, Vietnamese typo → Kara fix)
- [x] Format Validator — 2026-05-21 (approved 2026-05-22: section case / original wikilink / date_ingested — Compile Agent template fixed)
- [x] Hygiene Inspector — 2026-05-21 (approved 2026-05-22: stale backup files cleaned up)

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
