# Action Required — Pending Reviews

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-14 23:34:24

---

## Summary

**Pending reports:** 3

**Status:**
- Output Validator: 1 pending report (4 issues)
- Format Validator: 1 pending report (3 issues)
- Hygiene Inspector: 1 pending report (14 issues — 8 ERROR, 2 WARNING, 4 INFO)

---

## 🔴 Critical Issues (Fix Immediately)

### Output Validator — 2026-05-14

**1. Incorrect wikilink format in frontmatter `sources` field** — ERROR
- 7 concept files use `[[wiki/sources/src_active-vs-lazy-thinking]]` instead of `[[src_active-vs-lazy-thinking]]`
- Affects: `philosopher-syndrome`, `information-compression`, `abstraction-layer-fallacy`, `organizational-incrementalism`, `nice-syndrome`, `lazy-thinking`, `active-thinking`

### Hygiene Inspector — 2026-05-14

**⚠️ SPEC vs REALITY CONFLICT** — folder-structure.md v1.0 is outdated
- `.hermes/` and `.openclaw/` have 30+ runtime files (databases, caches, logs, sessions, deployed skills) — spec only allows 5 items
- `.hermes/skills/` has 29 folders vs 3 spec'd (26 extra deployed skills)
- `.openclaw/skills/` has 5 folders vs 4 spec'd (1 extra: agent-reach)
- 5 root-level symlinks not in whitelist
- **Recommendation:** Update folder-structure.md to v1.1

---

## 🟡 Warnings (Can Fix Later)

### Output Validator — 2026-05-14

**1. Empty `## Notes` sections in all 12 concept files** — WARNING
- All concept files have empty Notes section headers
- Either remove or add annotations

### Hygiene Inspector — 2026-05-14

**1. Non-standard file in skill folder** — WARNING
- `.hermes/skills/output-validator/validation-criteria.md` not in allowed file list (expected: SKILL.md, workflow.md, examples.md, reference.md)

---

## 🟢 Info & Suggestions

### Output Validator — 2026-05-14

**1. Source summaries at minimum boundary (3 sentences)** — INFO
- Both source files (`src_what-comes-after-systems-thinking`, `src_active-vs-lazy-thinking`) at exactly 3 sentences

**2. Key points above recommended range** — INFO
- 3 files (2 sources + 1 concept) have 10-11 items vs 5-10 target

### Hygiene Inspector — 2026-05-14

**1-4. Expected subfolders not yet created** — INFO
- `wiki/tag/`, `wiki/topic/`, `wiki/drafts/`, `wiki/reviews/archive/` — create as needed

---

## Pending Reports

### 1. Output Validation — 2026-05-14

**File:** [2026-05-14_output-report.md](2026-05-14_output-report.md)
**Status:** pending
**Created:** 2026-05-14 23:00:00
**Issues:** 4 (1 ERROR, 1 WARNING, 2 INFO)
**Files affected:** 14

**Summary:**
- 1 critical quality issue (wrong wikilink format in 7 files)
- 1 improvement needed (empty Notes sections in 12 files)
- 2 suggestions (summary length, key points count)

**Actions:**
- `approve output` — approve this report
- `reject output` — reject this report
- `show output` — show full report details

---

### 2. Format Validation — 2026-05-14

**File:** [2026-05-14_format-report.md](2026-05-14_format-report.md)
**Status:** pending
**Created:** 2026-05-14 23:18:48
**Issues:** 3 (0 ERROR, 2 WARNING, 1 INFO)
**Files affected:** 4

**Summary:**
- 2 source files have legacy `date_ingested` field + disrupted field order
- 1 ambiguity flag: conflicting wikilink conventions (bare slug vs full path)
- Clean on sections, naming, YAML syntax, list/emphasis/code styling

**Actions:**
- `approve format` — approve this report
- `reject format` — reject this report
- `show format` — show full report details

---

### 3. Hygiene Inspection — 2026-05-14

**File:** [2026-05-14_hygiene-report.md](2026-05-14_hygiene-report.md)
**Status:** pending
**Created:** 2026-05-14 23:34:24
**Issues:** 14 (8 ERROR, 2 WARNING, 4 INFO)
**Files affected:** N/A (folder structure only)

**Summary:**
- ⚠️ Critical SPEC vs REALITY conflict: folder-structure.md defines idealized agent homes (5 items each), real agents have 30+ runtime files
- 5 root-level symlinks (HEARTBEAT.md, IDENTITY.md, SOUL.md, TOOLS.md, USER.md) not in whitelist
- .hermes/skills/ has 29 folders vs 3 spec'd — 26 extra deployed skills
- .openclaw/skills/ has 5 folders vs 4 spec'd — 1 extra (agent-reach)
- 4 expected folders not yet created: wiki/tag/, wiki/topic/, wiki/drafts/, wiki/reviews/archive/
- 1 non-standard file in skill folder: validation-criteria.md

**Recommendation:** Update folder-structure.md to v1.1 with runtime artifact whitelists

**Actions:**
- `approve hygiene` — approve this report
- `reject hygiene` — reject this report
- `show hygiene` — show full report details

---

## Recently Applied

<!-- Reports applied in last 7 days appear here -->
<!-- Auto-cleaned after 7 days -->

*No recently applied reports.*

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

**To reject a report:**
reject output
reject format
reject hygiene

**To apply approved fixes:**
openclaw fix apply
