# Format Validation — 2026-07-14

**Status:** pending
**Issues found:** 306
**Created:** 2026-07-14 23:16
**Validator:** format-validator

> **Context:** Evening run. Previous approved baseline: 2026-06-23 (APPLIED with 463 issues: 126 ERROR, 337 WARNING). 21-day gap since last format run — KB has grown significantly (+182 files, +182 concepts, +41 sources, +58 topics).
> **Delta from 06-23:** -126 ERROR (all gone!), -31 WARNING, +182 files checked. The 108 topic-file frontmatter ERRORs and 8 code-block-language-tag ERRORs from 06-23 are all resolved. Cleanest format report ever: **zero ERRORs across 769 files.**

---

## Summary

| Metric | Value | Δ from 06-23 |
|---|---|---|
| Files checked | 769 | +182 |
| Concepts | 427 | +93 |
| Sources | 143 | +41 |
| Indexes | 33 | — |
| Topics | 166 | +58 |
| **Total issues** | **306** | -157 |
| **ERRORs** | **0** | -126 |
| **WARNINGS** | **306** | -31 |
| **INFOs** | **0** | — |

---

## Positive Delta

### ✅ All ERROR categories from 06-23 resolved

The 126 ERRORs from June are completely gone:

1. **Topic files missing YAML frontmatter (~108 files)** — Index Agent now generates proper frontmatter for all `wiki/topic/*.md` files
2. **Code blocks missing language tags (8 files)** — All bare code blocks now have language identifiers
3. **Misc frontmatter/markdown edge cases (~10)** — All resolved

### ✅ Unquoted wikilink WARNINGs reduced

The 22 tag-file `parent: [[tag]]` unquoted wikilink WARNINGs from 06-23 are no longer flagged (either fixed or properly handled by updated validator).

### ✅ Field order + broken original wikilink WARNINGs resolved

The 2 field-order WARNINGs and 1 broken-original WARNING from 06-23 are gone.

**Net result: KB format health is excellent. All structural issues have been addressed.**

---

## WARNING Categories (306)

### 1. Broken wikilinks (forward-references) — 306

**Severity:** WARNING
**Category:** Markdown

**Issue:** Concepts and sources link to target concepts that have not yet been compiled. This is **expected forward-referencing behavior** in a growing KB — not a format error.

**Breakdown:**
- Individual broken wikilinks: 285
- Forward-reference summary groups: 21 (compressed from ~90 individual links)

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

**Note:** Forward-references are expected and healthy in a growing KB. These resolve naturally as the referenced concepts are compiled. No action needed.

**Status:** 🔁 ONGOING — expected to persist as KB grows; resolves as targets are compiled

---

## Files Checked

| Zone | Count |
|---|---|
| `wiki/concepts/` | 427 |
| `wiki/sources/` | 143 |
| `wiki/tag/` | 33 |
| `wiki/topic/` | 166 |
| **Total** | **769** |

Errors reading files: 0

---

## Escalations

None. No ERRORs, no systemic violations, no spec conflicts.

---

## Verification

```bash
test -f "wiki/reviews/2026-07-14_format-report.md" && echo "✅ Report written"
```
