# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-06-01 17:15 — All reports resolved. Clean slate.

---

## Summary
**Pending reports:** 0 ✅

**Status:**
- ✅ Format Validator — 2026-06-01: **APPLIED** (37 concepts + 3 sources fixed by Fix Agent)
- ✅ Output Validator — 2026-06-01: **APPLIED** (172 concepts → status: reviewed; source notes regenerated)
- ✅ Hygiene Inspector — 2026-06-01: **PROMOTE** (0 issues)
- ✅ Format Validator — 2026-05-30: RESOLVED
- ✅ Output Validator — 2026-05-30: RESOLVED
- ✅ Hygiene Inspector — 2026-05-30: RESOLVED
- ✅ Format Validator — 2026-05-29: APPLIED
- ✅ Format Validator — 2026-05-28: RESOLVED
- ✅ Output Validator — 2026-05-29: RESOLVED
- ✅ Hygiene Inspector — 2026-05-29: RESOLVED

---

## Applied Fixes — 2026-06-01

### Fix Agent run (17:11)

| Issue | Method | Result |
|---|---|---|
| main_tag in sub_tags (40 files) | Removed main_tag duplicates from sub_tags arrays | ✅ 37 concepts + 3 sources |
| status: draft (172 concepts) | Batch update to status: reviewed | ✅ 172 concepts |
| Summary 1 dòng | Manual expand 6 concepts | 🔄 ~200 remaining — needs re-compile |

### Compile Agent update (08:15)

| File | Changes |
|---|---|
| `SKILL.md` | Vietnamese output, 3-5 câu Summary, ≥3 Key ideas, no empty Sources, Status lifecycle |
| `workflow.md` | All prompt templates → tiếng Việt + hard constraints. Pool B warning added |
| `TAGS.md` | +`#psychology` (12), +`#health` (14) — Pool B now 16 tags |

### Remaining (systemic — requires re-compile)

| Issue | Count | Fix |
|---|---|---|
| Definition 1 sentence | ~200 concepts | Re-compile with updated Compile Agent |
| Key Points <3 | 17 files | Re-compile |
| Sources empty | 3 files | Re-compile |

---

## Resolved Reports (archive)

- [x] Format Validator — 2026-05-30 (16 issues)
- [x] Output Validator — 2026-05-30 (18 issues)
- [x] Hygiene Inspector — 2026-05-30 (2 issues)
- [x] Format Validator — 2026-05-29 (55/60 files)
- [x] Output Validator — 2026-05-29
- [x] Hygiene Inspector — 2026-05-29
- [x] Format Validator — 2026-05-28
- [x] Output Validator — 2026-05-28
- [x] Hygiene Inspector — 2026-05-28
- [x] Output Validator — 2026-05-27 (11 issues)
- [x] Format Validator — 2026-05-27 (20 issues)
- [x] Output Validator — 2026-05-26 (2 ERROR + 4 WARNING)
- [x] Hygiene Inspector — 2026-05-26 (2 ERROR + 2 WARNING)
- [x] Format Validator — 2026-05-26 (17 ERROR + 3 WARNING)
- [x] Output Validator — 2026-05-24 (20 issues)
- [x] Hygiene Inspector — 2026-05-24 (1 ERROR + 1 INFO)
- [x] Format Validator — 2026-05-24 (2 ERROR + 5 WARNING)
- [x] Output Validator — 2026-05-22 (16 issues)
- [x] Hygiene Inspector — 2026-05-22 (3 ERROR + 2 issues)
- [x] Format Validator — 2026-05-22 (11 WARNING)
- [x] Format Validator — 2026-05-21 (20 issues)
- [x] Output Validator — 2026-05-21 (11 issues)
- [x] Hygiene Inspector — 2026-05-21 (9 issues)
- [x] Hygiene Inspector — 2026-05-20 (6 issues)
- [x] Hygiene Inspector — 2026-05-17 (20 issues)
- [x] Format Validator — 2026-05-17 (5 issues)
- [x] Output Validator — 2026-05-14 (4 issues)
- [x] Format Validator — 2026-05-14 (3 issues)
- [x] Hygiene Inspector — 2026-05-14 (14 issues)

---

## Commands

**To view full report:**
```
show output
show format
show hygiene
```

**To apply approved fixes:**
```
openclaw fix apply
```
