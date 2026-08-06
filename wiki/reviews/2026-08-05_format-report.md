# Format Validation — 2026-08-05

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-05
**Issues found:** 433
**Created:** 2026-08-05 23:15
**Validator:** format-validator
**ERRORs**: 3
**WARNINGS**: 430
**INFOS:** 0
**Files checked:** 886 (504 concepts + 161 sources + 34 indexes + 187 topics)
**Total issues**: 433
Files checked: 886
Total issues: 433
Δ from 08-04: **no change** — 4th consecutive identical run (08-01 → 08-03 → 08-04 → 08-05). KB static since 08-01. Same 3 ERRORs, same 430 WARNINGs, same 278 unique broken targets. Pending fixes unapplied for 4 days.
Δ from 07-30 (approved): +19 files (+9 concepts, +2 sources, +0 indexes, +8 topics), +22 issues (0→3 ERRORs, +19 WARNINGs).

---

## Issues Found: 433

| Severity | Count | Category |
|---|---|---|
| ERROR | **3** | Frontmatter (1) + Sections (2) |
| WARNING | **430** | Broken wikilinks (410 individual + 20 forward-reference groups) |
| INFO | 0 | — |

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 886 | 504 | 161 | 34 | 187 |

**Unique broken wikilink targets:** 278

⚠️ 0-ERROR streak BROKEN since 08-01 (was 9 days: 07-22 → 07-30). KB static — 4th consecutive run with identical results. Pending fixes have not been applied.

---

## ERRORs — 3

### Issue 1: Invalid sub_tag — "career" not in TAGS.md

**File:** wiki/concepts/optionality-principle.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` field contains `"career"` which is not in TAGS.md Pool B
**Current:** `sub_tags: [career]`
**Expected:** Valid Pool B tag (e.g., `skill`, `practice`, `strategy`) or proposed addition to TAGS.md
**Suggested fix:** Replace `career` with valid Pool B tag OR propose adding `career` to TAGS.md

---

### Issue 2: Missing `## Co-occurring tags` section

**File:** wiki/tag/opinion.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Tầng 3 tag index missing required `## Co-occurring tags` section
**Current:** Section absent
**Expected:** `## Co-occurring tags` with list of tags that appear alongside `opinion`
**Suggested fix:** Index Agent regenerate `wiki/tag/opinion.md` with co-occurring tags section

---

### Issue 3: Missing `## Co-occurring tags` section

**File:** wiki/tag/research.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Tầng 3 tag index missing required `## Co-occurring tags` section
**Current:** Section absent
**Expected:** `## Co-occurring tags` with list of tags that appear alongside `research`
**Suggested fix:** Index Agent regenerate `wiki/tag/research.md` with co-occurring tags section

---

## WARNINGs — 430

All 430 WARNINGs are **broken wikilinks** — concepts and sources linking to target concepts/sources that have not yet been compiled. This is a forward-reference pattern, not a structural format error.

### Top 20 Broken Link Targets

| Target | Occurrences |
|---|---|
| `[[game-theory]]` | 10 |
| `[[src_agent-memory-7-types-substack.md]]` | 8 |
| `[[confirmation-bias]]` | 8 |
| `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 |
| `[[src_the-let-them-theory-gabriel-reality.md]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
| `[[src_how-to-remember-everything-you-read-dan-koe.md]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[src_cuoc-ua-xem-ai-khong-i-lui-curiositypocket.md]]` | 4 |
| `[[src_introducing-backsearch-gr-inc.md]]` | 3 |
| `[[src_monid-ai-agent-tool-platform.md]]` | 3 |
| `[[attention-economy]]` | 3 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |

### Top 10 Files by WARNING Count

| File | WARNINGs |
|---|---|
| wiki/concepts/collaborative-thinking.md | 5 |
| wiki/concepts/probabilistic-thinking.md | 5 |
| wiki/concepts/feedback-loops.md | 4 |
| wiki/concepts/hanlons-razor.md | 4 |
| wiki/concepts/meaning-through-work.md | 4 |
| wiki/concepts/occams-broom.md | 4 |
| wiki/concepts/occams-razor.md | 4 |
| wiki/concepts/parametric-memory.md | 4 |
| wiki/concepts/pay-per-call-pricing.md | 4 |
| wiki/concepts/prospective-memory.md | 4 |

### Forward-Reference Summary Groups (20)

20 files have 4+ broken wikilinks reported as grouped summaries:

- `wiki/concepts/third-order-thinking.md` — 6 broken wikilinks (forward-references)
- `wiki/concepts/thought-experiment.md` — 6 broken wikilinks (forward-references)
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 broken wikilinks (forward-references)
- `wiki/sources/src_farnam-street-mental-models-biology-series.md` — 6 broken wikilinks (forward-references)
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` — 6 broken wikilinks (forward-references)
- `wiki/sources/src_incentives-hidden-forces.md` — 6 broken wikilinks (forward-references)
- `wiki/sources/src_mental-models-of-art.md` — 9 broken wikilinks (forward-references)
- `wiki/sources/src_mental-models-of-economics.md` — 9 broken wikilinks (forward-references)
- `wiki/sources/src_thought-experiment.md` — 9 broken wikilinks (forward-references)
- `wiki/sources/src_fs-blog-mental-models.md` — 7 broken wikilinks (forward-references)
- Plus 10 additional grouped files with 4 broken wikilinks each

---

## Verification

- [x] Validation script (`validate.py`) executed successfully — 0 ERRORS_READING
- [x] All 886 files parsed without YAML/read errors
- [x] Spec dispatch: 504 concepts, 161 sources → format-spec.md; 34 indexes → index-spec.md; 187 topics → topic validation; context/USER.md skipped
- [x] ERRORs verified: 3 (1 invalid sub_tag + 2 missing Co-occurring tags)
- [x] WARNINGs verified: 410 individual broken wikilinks + 20 forward-reference groups = 430 total
- [x] Delta from 08-04: no change — 4th consecutive identical run
- [x] Delta from 07-30 (approved): +19 files, +22 issues

---

## Escalations

### [SYSTEMATIC VIOLATION]
Pattern: 430 broken wikilinks across 278 unique targets — 4th consecutive identical run (08-01, 08-03, 08-04, 08-05). KB static since 08-01. These are all forward-reference content gaps — no structural format errors in the WARNINGs. The 3 ERRORs are the only actionable format violations.

### [SYSTEMATIC VIOLATION]
Pattern: 2 tag indexes (opinion.md, research.md) consistently missing `## Co-occurring tags`. 4th consecutive flag. Likely cause: Index Agent not generating this section for these specific Tầng 3 files.

Recommendation: Review index-agent SKILL.md — ensure `## Co-occurring tags` is generated for every Tầng 3 tag file.
