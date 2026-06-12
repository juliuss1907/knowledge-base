# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-06-12 — Julius approved selected validation fixes; Summary 1-dòng explicitly ignored.

---

## Summary

**Pending approved fixes:** 3 groups

**Status:**
- ✅ Format Validator — latest run: **APPROVED** (8 files with invalid sub_tag `system`)
- ✅ Output Validator — latest run: **APPROVED PARTIAL**
  - ✅ Sources trống: **2 concepts approved for fix**
  - ✅ Key ideas <3: **18 concepts approved for fix**
  - ⏭️ Summary 1 dòng: **IGNORED by Julius**
  - ⏸️ Status draft: **not approved in this pass**
- ✅ Hygiene Inspector — latest run: **PROMOTE** (0 issues)
- ✅ Format Validator — 2026-06-06: APPLIED (6 files)
- ✅ Output Validator — 2026-06-06: APPROVED
- ✅ Hygiene Inspector — 2026-06-06: PROMOTE
- ✅ Format Validator — 2026-06-03: APPLIED (5 files)
- ✅ Output Validator — 2026-06-03: APPROVED
- ✅ Hygiene Inspector — 2026-06-03: PROMOTE

---

## Approved Fixes

### ✅ Format Validator — latest run (8 files)

**Issue:** invalid sub_tag `system` — `system` is Pool A main_tag, not Pool B sub_tag.

**Approved fix:** replace `system` with `research`.

| File | Fix |
|---|---|
| bottlenecks-mental-model.md | `system` → `research` |
| diminishing-returns-mental-model.md | `system` → `research` |
| ecosystems-mental-model.md | `system` → `research` |
| equilibrium-mental-model.md | `system` → `research` |
| feedback-loops.md | `system` → `research` |
| margin-of-safety-mental-model.md | `system` → `research` |
| src_farnam-street-mental-models-systems-thinking.md | `system` → `research` |
| src_feedback-loops-mental-model.md | `system` → `research` |

---

### ✅ Output Validator — Sources trống (2 concepts)

**Approved fix:** add correct source backlink into `## Sources` section and ensure frontmatter `sources:` matches.

| File | Issue |
|---|---|
| ai-powered-discovery.md | `## Sources` empty |
| second-order-effects.md | `## Sources` empty |

---

### ✅ Output Validator — Key ideas <3 (18 concepts)

**Approved fix:** expand `## Key ideas` to at least 3 bullets per concept. Keep existing meaning. Do not invent unsupported claims. Prefer sourcing from linked source notes.

**Count:** 18 concepts.

---

## Explicitly Ignored

### ⏭️ Summary 1 dòng

Julius explicitly chose to ignore this issue for now.

**Do not fix in this pass:**
- Summary 1 dòng across 359 files
- No re-compile required solely for Summary length

---

## Not Approved In This Pass

### ⏸️ Status draft

Latest validation found **109 draft files**. Julius did not approve this item in the current instruction. Leave unchanged unless separately approved.

---

## Commands

**To apply approved fixes:**
```
openclaw fix apply
```
