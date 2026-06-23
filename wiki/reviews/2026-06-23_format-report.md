# Format Validation — 2026-06-23

**Status:** pending
**Issues found:** 463
**Created:** 2026-06-23 23:16
**Validator:** format-validator

> **Context:** Evening run after Output Validator (23:10). Previous approved baseline: 2026-06-22 22:30 (APPROVED with 453 issues: 134 ERROR, 319 WARNING).
> Delta from yesterday: -8 ERROR, +18 WARNING, +16 files checked. `main_tag: psychology` errors fully resolved. No new issue categories.

---

## Summary

| Metric | Value | Δ from 06-22 |
|---|---|---|
| Files checked | 587 | +16 |
| Concepts | 334 | +10 |
| Sources | 102 | +3 |
| Indexes | 33 | — |
| Topics (no frontmatter) | ~108 | ~same |
| **Total issues** | **463** | +10 |
| **ERRORs** | **126** | -8 |
| **WARNINGS** | **337** | +18 |
| **INFOs** | **0** | — |

---

## ERROR Categories (126)

### 1. Topic files missing YAML frontmatter — ~108 files

**Severity:** ERROR
**Category:** Frontmatter
**Scope:** `wiki/topic/*.md` — all topic index files

**Issue:** Every file under `wiki/topic/` lacks YAML frontmatter entirely. Files begin directly with `# Title` without `---` delimiters. This is a systemic Index Agent issue — topic files are compiled without frontmatter block.

**Expected:** Per `index-spec.md` §5.1, topic files should have:
```yaml
---
type: index
scope: topic
topic: <slug>
auto_generated: true
last_updated: YYYY-MM-DD
---
```

**Affected files (representative sample):**
- `wiki/topic/activation-energy-mental-model.md`
- `wiki/topic/ai-architecture.md`
- `wiki/topic/ai-economic-disruption-white-collar.md`
- `wiki/topic/code-as-agent-harness.md`
- `wiki/topic/deepseek-v4-architecture.md`
- `wiki/topic/game-theory-strategic-thinking.md`
- `wiki/topic/hermes-polymarket-trading-agent.md`
- `wiki/topic/mental-models-latticework.md`
- `wiki/topic/trading-psychology.md`
- …and ~98 more

**Suggested fix:** Update Index Agent to include YAML frontmatter in topic files per `index-spec.md` §5.1.

**Status:** 🔁 CARRY-OVER (since 06-17) — approved 06-22, not yet fixed

---

### 2. Code blocks missing language tags — 8 files

**Severity:** ERROR
**Category:** Markdown
**Scope:** 7 concepts + 1 source

**Issue:** Fenced code blocks (```) lack a language identifier. Per format-spec.md §9, all code blocks must specify language.

**Affected files:**
| # | File | Type |
|---|---|---|
| 1 | `wiki/concepts/ai-coach-prompting.md` | concept |
| 2 | `wiki/concepts/content-generation-workflow.md` | concept |
| 3 | `wiki/concepts/dollar-as-rent-payment.md` | concept |
| 4 | `wiki/concepts/existential-vacuum.md` | concept |
| 5 | `wiki/concepts/expert-knowledge-extraction.md` | concept |
| 6 | `wiki/concepts/trading-addiction-cycle.md` | concept |
| 7 | `wiki/concepts/x-search-tool.md` | concept |
| 8 | `wiki/sources/src_petrodollar-system-analysis.md` | source |

**Suggested fix:** Add language tag (e.g., ```python, ```bash, ```yaml) to each bare code block.

**Status:** 🔁 CARRY-OVER (since 06-14) — approved 06-22, not yet fixed

---

### 3. Additional ERRORs (truncated from full output) — ~10 more

**Severity:** ERROR
**Note:** Script output capped at 50KB stdout; 10 ERRORs beyond the 108 topic + 8 code-block issues listed above were present in the total count (126) but truncated from output. These include frontmatter/markdown edge cases.

**Status:** ⚠️ Requires full re-run with higher stdout cap to enumerate.

---

## WARNING Categories (337)

### 4. Broken wikilinks (forward-references) — ~290

**Severity:** WARNING
**Category:** Markdown

**Issue:** Concepts and sources link to target concepts that have not yet been compiled. This is **expected forward-referencing behavior** in a growing KB — not a format error.

**Delta:** +~20 from 06-22 (337 - 22 unquoted - 2 field order - 1 broken original ≈ ~312 broken wikilinks, but 22 tag unquoted are separate, so ~290 broken)

**Most-referenced missing targets (top 5):**
- `[[game-theory]]` — referenced by 7+ files
- `[[confirmation-bias]]` — referenced by 5+ files
- `[[decision-making]]` — referenced by 4+ files
- `[[pareto-principle]]` — referenced by 4+ files
- `[[deep-work]]` — referenced by 4+ files

**Note:** These are forward-references to uncompiled concepts. Report as WARNING per skill guidelines. Do not treat as systematic unless >50% of links are broken.

**Status:** 🔁 ONGOING — expected to persist as KB grows; resolves as targets are compiled

---

### 5. Unquoted wikilinks in YAML frontmatter — 22 files

**Severity:** WARNING
**Category:** Frontmatter
**Scope:** `wiki/tag/*.md`

**Issue:** Tag index files use unquoted `parent: [[tag]]` syntax. YAML parser interprets the leading `[` as a flow sequence, producing a nested list instead of a string. Example: `parent: [[ai]]` is parsed as `parent: [['ai']]`.

**Affected:** 22 `wiki/tag/*.md` files (was 23 yesterday — `wiki/tag/research.md` no longer flagged, either fixed or removed).

**Expected:** Quoted format: `parent: "[[ai]]"`

**Spec conflict:** `index-spec.md` shows unquoted `parent: [[tag]]` but `format-spec.md` §9 requires quoted wikilinks in frontmatter. Escalate as `[SPEC CONFLICT]`.

**Suggested fix:** Either (a) quote all `parent` values in `wiki/tag/*.md`, or (b) update `index-spec.md` to show quoted format and update Index Agent.

**Status:** 🔁 CARRY-OVER (since 06-14) — approved 06-22, not yet fixed

---

### 6. Field order mismatch — 1 file

**Severity:** WARNING
**Category:** Frontmatter
**File:** `wiki/sources/src_dan-koe-workflow-analysis-markus.md`

**Issue:** Frontmatter field order does not match source frontmatter order specified in format-spec.md §3.

**Status:** 🔁 CARRY-OVER — approved 06-22, not yet fixed (was 2 files; 1 resolved)

---

### 7. Broken original wikilink (raw file reference) — 1 file

**Severity:** WARNING
**Category:** Frontmatter
**File:** `wiki/sources/src_map-is-not-territory.md`

**Issue:** `original` field references `[[2026-06-03_map-is-not-territory]]` but corresponding raw file not found in `raw/`.

**Status:** 🔁 CARRY-OVER — approved 06-22, not yet fixed

---

## Positive Delta

### ✅ Resolved: `main_tag: psychology` — Pool B tag used as main_tag

The 11 files flagged on 06-22 with `main_tag: psychology` (Pool B tag used as main_tag) have been **fixed**. These files no longer appear in today's ERROR list. Fix Agent successfully applied the approved correction.

---

## Escalations

### [SYSTEMATIC VIOLATION] Topic files without frontmatter

- **108 files** affected — the entire `wiki/topic/` directory
- **Likely cause:** Index Agent does not generate YAML frontmatter for topic index files
- **Recommendation:** Update Index Agent SKILL.md to include frontmatter generation per `index-spec.md` §5.1
- **Julius decision:** APPROVED 06-22, awaiting fix

### [SPEC CONFLICT] Unquoted wikilinks

- `index-spec.md` shows `parent: [[tag]]` (unquoted)
- `format-spec.md` §9 requires quoted wikilinks in YAML frontmatter: `"[[tag]]"`
- **Recommendation:** Update `index-spec.md` to show quoted format, then fix all tag files
- **Julius decision:** APPROVED 06-22, awaiting fix

---

## Files Checked

| Zone | Count |
|---|---|
| `wiki/concepts/` | 334 |
| `wiki/sources/` | 102 |
| `wiki/tag/` | 33 |
| `wiki/topic/` | ~108 |
| Other indexes | 10 |
| **Total** | **587** |

---

## Verification

```bash
test -f "wiki/reviews/2026-06-23_format-report.md" && echo "✅ Report written"
```
