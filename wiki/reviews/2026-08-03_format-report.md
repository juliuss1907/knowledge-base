# Format Validation — 2026-08-03

**Status:** pending
**Issues found:** 433
**Created:** 2026-08-03 23:15
**Validator:** format-validator
**ERRORs**: 3
**WARNINGS**: 430
**INFOS:** 0
**Files checked:** 886 (504 concepts + 161 sources + 34 indexes + 187 topics)
**Total issues**: 433

**Δ from 2026-08-01 (last report):** No change — identical results. +0 files, +0 issues. Same 3 ERRORs and 430 WARNINGs carried forward. KB is static since 08-01; pending fixes from that report have not been applied yet.

Files checked: 886
Total issues: 433

---

## Issues Found: 433

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 886 | 504 | 161 | 34 | 187 |

### ERRORs: 3

---

## Issue 1: Invalid sub_tag — not in TAGS.md

**File:** wiki/concepts/optionality-principle.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags` contains `career` — not in TAGS.md Pool B
**Current:** `sub_tags: [career]`
**Expected:** Valid Pool B tag from TAGS.md (e.g., `psychology`, `strategy`, `systems`)
**Suggested fix:** Replace `career` with a valid Pool B tag, or propose adding `career` to TAGS.md tag taxonomy

---

## Issue 2: Missing required section — ## Co-occurring tags

**File:** wiki/tag/opinion.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Tầng 3 tag index missing required `## Co-occurring tags` section (per index-spec.md §5)
**Current:** Section absent
**Expected:** `## Co-occurring tags` section listing related tags
**Suggested fix:** Regenerate via Index Agent with co-occurring tags section

---

## Issue 3: Missing required section — ## Co-occurring tags

**File:** wiki/tag/research.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Tầng 3 tag index missing required `## Co-occurring tags` section (per index-spec.md §5)
**Current:** Section absent
**Expected:** `## Co-occurring tags` section listing related tags
**Suggested fix:** Regenerate via Index Agent with co-occurring tags section

---

### WARNINGs: 430

All 430 WARNINGs are broken wikilinks — forward-references to concepts or sources not yet compiled into the wiki. Breakdown:

- **Individual broken wikilinks:** 410 (278 unique targets)
- **Forward-reference groups:** 20 (summarized per file)

#### Top 20 most-cited broken targets

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

#### Forward-reference groups (20)

| File | Count | Notes |
|---|---|---|
| wiki/concepts/third-order-thinking.md | 6 | Forward-references to uncompiled concepts |
| wiki/concepts/thought-experiment.md | 6 | Forward-references to uncompiled concepts |
| wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md | 6 | Forward-references |
| wiki/sources/src_farnam-street-mental-models-biology-series.md | 6 | Forward-references |
| wiki/sources/src_farnam-street-mental-models-systems-thinking.md | 6 | Forward-references |
| wiki/sources/src_incentives-hidden-forces.md | 6 | Forward-references |
| wiki/sources/src_probabilistic-thinking.md | 6 | Forward-references |
| wiki/sources/src_mental-models-of-art.md | 9 | Forward-references |
| wiki/sources/src_mental-models-of-economics.md | 9 | Forward-references |
| wiki/sources/src_thought-experiment.md | 9 | Forward-references |
| wiki/sources/src_fs-blog-mental-models.md | 7 | Forward-references |
| wiki/sources/src_11-minutes-hack-github.md | 4 | Forward-references |
| wiki/sources/src_ai-future-skills.md | 4 | Forward-references |
| wiki/sources/src_critical-thinking-dennett.md | 4 | Forward-references |
| wiki/sources/src_feedback-loops-mental-model.md | 4 | Forward-references |
| wiki/sources/src_global-macro-investing.md | 4 | Forward-references |
| wiki/sources/src_hermes-polymarket-btc-trading-agent.md | 4 | Forward-references |
| wiki/sources/src_the-cost-of-discretion.md | 4 | Forward-references |
| wiki/sources/src_the-seed-and-the-machine.md | 4 | Forward-references |
| wiki/sources/src_tribute-system-new-world-order.md | 4 | Forward-references |

#### Top 10 files by broken wikilink count

| File | Count |
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

---

## Verification

- [x] Validation script (`validate.py`) completed: 886 files scanned, 0 read errors
- [x] Issue parsing (`parse_issues.py`) completed: 433 issues classified
- [x] Previous report (2026-08-01) checked: still `pending`, no reconciliation needed
- [x] Delta computed: 0 change vs 2026-08-01 — identical results
- [x] 3 ERRORs confirmed: 1 invalid sub_tag + 2 missing Co-occurring tags sections (carried from 08-01)
- [x] 430 WARNINGs confirmed: all broken wikilinks (278 unique targets)
- [x] All ERRORs are attributable — no unexplained failures

---

## Escalations

No new escalations. The 3 ERRORs have been pending since 08-01 (previous report). Recommend priority: Index Agent regenerate opinion.md and research.md with `## Co-occurring tags` section + investigate whether this is a systemic Index Agent bug. The `career` sub_tag in optionality-principle.md needs either tag taxonomy update or field correction.

---

*Validation completed 2026-08-03 23:15. Report identical to 2026-08-01 — KB unchanged. Fixes pending Julius review.*
