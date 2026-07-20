# Format Validation — 2026-07-15

**Status:** approved
**Issues found:** 313
**Created:** 2026-07-15 23:15
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** format-validator

> **Context:** Evening run. Previous approved baseline: 2026-07-14 (approved, 306 WARNINGs, 0 ERRORs). KB continues to grow with clean format health.
> **Delta from 07-14:** +7 WARNINGs, +5 files checked (+3 concepts, +1 source, +1 topic). All issues remain broken wikilinks — forward-references to uncompiled concepts. Zero structural format violations.

---

## Summary

| Metric | Value | Δ from 07-14 |
|---|---|---|
| Files checked | 774 | +5 |
| Concepts | 430 | +3 |
| Sources | 144 | +1 |
| Indexes | 33 | — |
| Topics | 167 | +1 |
| **Total issues** | **313** | +7 |
| **ERRORs** | **0** | — |
| **WARNINGS** | **313** | +7 |
| **INFOs** | **0** | — |

---

## Positive Delta

### ✅ Zero ERRORs maintained

The clean streak continues — 0 ERRORs for the third consecutive day (07-14: 0, 07-13: 0, today: 0). All structural issues from June (108 topic-file frontmatter ERRORs, 8 code-block language-tag ERRORs, ~10 misc edge cases) remain resolved.

### ✅ Topic files clean

All 167 topic files pass validation with no issues — Index Agent maintains correct frontmatter.

### ✅ Tag files clean

All 33 tag index files pass validation — no unquoted wikilink warnings, no field-order issues.

---

## WARNING Categories (313)

### 1. Broken wikilinks (forward-references) — 313

**Severity:** WARNING
**Category:** Markdown

**Issue:** Concepts and sources link to target concepts that have not yet been compiled. This is **expected forward-referencing behavior** in a growing KB — not a format error.

**Breakdown:**
- Individual broken wikilinks: 291
- Forward-reference summary groups: 21 (compressed from ~90 individual links)
- Other: 1 (raw-file wikilink pointing to non-existent raw file: `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` → `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]`)

**Most-referenced missing targets (top 10):**

| Target | Ref count |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |
| `[[naval-ravikant]]` | 3 |

**Top files by warning count:**

| File | Warnings |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/systematic-trading.md` | 4 |
| `wiki/concepts/vibe-coding.md` | 4 |
| `wiki/concepts/activation-energy.md` | 3 |

**Raw-file wikilink issue:** `wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md` references `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` in its `original` frontmatter field, but no such raw file exists. The actual raw file may have a different date prefix.

**Note:** Forward-references are expected and healthy in a growing KB. These resolve naturally as the referenced concepts are compiled. No action needed for 312 of 313 issues. The single raw-file resolution issue may need investigation if the source's `original` field is incorrect.

**Status:** 🔁 ONGOING — expected to persist as KB grows; resolves as targets are compiled

---

## Files Checked

| Zone | Count |
|---|---|
| `wiki/concepts/` | 430 |
| `wiki/sources/` | 144 |
| `wiki/tag/` | 33 |
| `wiki/topic/` | 167 |
| **Total** | **774** |

Errors reading files: 0

---

## Escalations

None. No ERRORs, no systemic violations, no spec conflicts. The single raw-file wikilink in `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` may be a manual data-entry issue — Julius can verify.

---

## Verification

```bash
test -f "wiki/reviews/2026-07-15_format-report.md" && echo "✅ Report written"
```
