# Format Validation — 2026-06-27

**Status:** pending
**Issues found:** 339 (24 ERROR, 315 WARNING, 0 INFO)
**Created:** 2026-06-27 23:16:45 +0700
**Validator:** format-validator
**Scope:** Full KB (concepts + sources + indexes + topics)

---

## Delta from last approved (2026-06-26 23:15)

| Metric | 2026-06-26 (APPROVED) | 2026-06-27 | Delta |
|---|---|---|---|
| Scope | concepts + sources only | Full KB (623 files) | Expanded |
| Files checked | 436 | 623 | +187 |
| ERROR | 4 | 24 | +20 |
| WARNING | 310 (in scope) | 315 | +5 |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ 8 code-block language-tag ERRORs → **GONE** (all 8 from 06-26 resolved by Fix Agent)

**Negative delta (new issues):**
- 🔴 23 new ERROR: `wiki/tag/*.md` — Missing `level` field (previously excluded from scoped runs)
- 🔴 1 new ERROR: Slug exceeds 50 chars in source filename
- ⚠️ +5 WARNING (broken wikilinks — net change in expanded scope)

---

## ERRORs (24)

### Issue 1: Slug exceeds 50-character limit

**File:** wiki/sources/src_give-me-14-minutes-and-ill-destroy-your-procrastination-forever.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Source slug body exceeds 50 chars (63 chars)
**Current:** `give-me-14-minutes-and-ill-destroy-your-procrastination-forever`
**Expected:** Slug body ≤ 50 chars (lowercase-hyphen)
**Suggested fix:** Shorten to e.g. `give-me-14-minutes-destroy-procrastination` (42 chars) and rename file → `src_give-me-14-minutes-destroy-procrastination.md`

---

### Issue 2–24: Tag index files missing `level` field

**Files:** 23 files under `wiki/tag/`
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** All 23 tag index files have `type: index` but are missing the required `level` field
**Current:** Frontmatter has `type: index` without `level: 3`
**Expected:** Per index-spec.md §5, level-3 tag indexes require `level: 3`
**Affected tags:** ai, automation, coding, crypto, defi, economic, geopolitics, hack, health, investment, law, layer1, news, opinion, politic, productivity, psychology, research, system, tech, tools, tutorial, vibecode

**Suggested fix:** Add `level: 3` to all 23 tag index frontmatters. Previously these were excluded from scoped runs (concepts + sources only). Now visible in full KB validation.

---

## WARNINGs (315)

### Broken wikilinks / forward references (~290 WARNINGs)

**Category:** Markdown
**Severity:** WARNING
**Issue:** Forward-references to concepts not yet compiled. Expected in growing KB — not actionable individually.

**Top clusters (files with 5+ broken links):**
- `wiki/concepts/third-order-thinking.md` — 6 broken wikilinks
- `wiki/concepts/thought-experiment.md` — 6 broken wikilinks
- `wiki/sources/src_fs-blog-mental-models.md` — 7 broken wikilinks
- `wiki/sources/src_mental-models-of-art.md` — 9 broken wikilinks
- `wiki/sources/src_mental-models-of-economics.md` — 9 broken wikilinks
- `wiki/sources/src_thought-experiment.md` — 9 broken wikilinks
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 broken wikilinks
- `wiki/sources/src_incentives-hidden-forces.md` — 6 broken wikilinks
- `wiki/sources/src_probabilistic-thinking.md` — 6 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-biology-series.md` — 6 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` — 6 broken wikilinks

---

### Original wikilink raw-file not found (4 WARNINGs)

| File | Target raw file | Status |
|---|---|---|
| `src_code-as-agent-harness-arxiv-2605-18747.md` | `2026-05-22_code-as-agent-harness-arxiv-2605-18747` | Not found in raw/ |
| `src_llm-need-sleep-consolidation.md` | `2026-05-27_llm-need-sleep-consolidation` | Not found in raw/ |
| `src_petrodollar-system-analysis.md` | `2026-05-28_petrodollar-system-analysis` | Not found in raw/ |
| `src_thermodynamics.md` | `2026-06-04_thermodynamics` | Not found in raw/ |

**Note:** All 4 carry over from 06-26. Raw files may be missing or the original link format is wrong.

---

### Other warnings (~21)

- Field order mismatches in concepts and sources (cosmetic, no functional impact)
- Unquoted `parent: [[tag]]` wikilinks parsed as nested YAML list in tag indexes (SPEC CONFLICT — index-spec.md shows unquoted format)

---

## Summary

| Category | ERROR | WARNING | INFO |
|---|---|---|---|
| Frontmatter | 23 | 4 | 0 |
| Naming | 1 | 0 | 0 |
| Markdown | 0 | ~310 | 0 |
| Sections | 0 | ~1 | 0 |

**Files checked:**
- 354 concepts
- 110 sources
- 33 indexes (tag + root)
- 126 topics
- **623 total** — 0 read errors

**Key takeaway:**
- 8 code-block ERRORs from 06-26 → fully resolved ✅
- 23 tag-file ERRORs surfaced (missing `level`) — previously hidden by scoped validation
- 1 naming ERROR (slug too long) — new, requires file rename
- Broken wikilink backlog stable (~310 WARNINGs) — forward references expected in growing KB
- Topic files (126) passed light validation — no new issues

---

## Escalations

### [SYSTEMATIC VIOLATION]
**Pattern:** All 23 tag index files (`wiki/tag/*.md`) missing `level: 3` field
**Likely cause:** Index Agent not including `level` in generated tag indexes
**Recommendation:** Update index-agent/SKILL.md to include `level: 3` in all tag index frontmatters; run Index Agent to regenerate all 23 tag files.

### [SPEC CONFLICT]
**Issue:** Unquoted `parent: [[tag]]` in tag index frontmatters parsed as nested YAML list
**Status:** Carry-over from 06-22. index-spec.md shows unquoted format; format-spec.md §9 requires quoted format.
**Recommendation:** Update index-spec.md to show quoted `parent: "[[tag]]"` format.
