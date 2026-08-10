# Format Validation — 2026-08-10

**Status:** pending
**Issues found:** 432
**Created:** 2026-08-10 23:15
**Validator:** format-validator
**Files checked:** 894 (508 concepts + 162 sources + 36 indexes + 188 topics)
**ERRORs**: 2
**WARNINGS**: 430
**INFOS:** 0
**Total issues**: 432
Files checked: 894
Total issues: 432

Δ from 2026-07-30 (approved): +27 files (+13 concepts, +3 sources, +2 indexes, +1 topic, +8 topics wait — topics grew by 1), +21 total issues (411→432)
Δ from 2026-08-09 (previous): +3 files (+2 indexes, +1 topic), +2 ERRORs (0→2), +0 WARNINGs (430→430)

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 894 | 508 | 162 | 36 | 188 |

## Issues Found: 432

| Severity | Count | Category |
|---|---|---|
| ERROR | **2** | Missing `## Co-occurring tags` section in tag index files |
| WARNING | **430** | Broken wikilinks (forward-references) |
| INFO | 0 | — |

**ERROR streak broken.** After 3 consecutive clean runs (08-07 through 08-09), 2 new ERRORs appeared: newly created tag indexes `layer2.md` and `perpdex.md` are missing the required `## Co-occurring tags` section. This is the same class of error Fix Agent resolved on 2026-08-06 for `opinion.md` and `research.md`.

### ERROR Details

| # | File | Issue |
|---|---|---|
| 1 | `wiki/tag/layer2.md` | Missing required section: `## Co-occurring tags` |
| 2 | `wiki/tag/perpdex.md` | Missing required section: `## Co-occurring tags` |

**Suggested fix:** Add `## Co-occurring tags` section header to both files. This is a known Index Agent omission — same pattern as opinion.md and research.md fixed on 2026-08-06.

### WARNING Details

**All 430 WARNINGs are broken wikilinks** — forward-references to concepts not yet compiled. These are expected in a growing KB where concepts link to each other and some targets haven't been written yet.

**Breakdown:**
- 410 individual broken wikilink targets
- 20 forward-reference groups (summarized by the validator for files with 4+ broken links)
- 278 unique broken target slugs

### Top 10 Broken Targets

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

### Top 10 Files by Warning Count

| File | Count |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/parametric-memory.md` | 4 |
| `wiki/concepts/pay-per-call-pricing.md` | 4 |
| `wiki/concepts/prospective-memory.md` | 4 |

### Forward-Reference Groups (20 files)

The validator grouped 20 files with 4+ broken wikilinks each into summary entries. Most notable:
- `wiki/sources/src_fs-blog-mental-models.md` — 7 broken wikilinks
- `wiki/sources/src_mental-models-of-art.md` — 9 broken wikilinks
- `wiki/sources/src_mental-models-of-economics.md` — 9 broken wikilinks
- `wiki/sources/src_thought-experiment.md` — 9 broken wikilinks
- `wiki/concepts/third-order-thinking.md` — 6 broken wikilinks
- `wiki/concepts/thought-experiment.md` — 6 broken wikilinks
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 broken wikilinks

---

## Verification

- [x] Validation script ran successfully (validate.py + parse_issues.py)
- [x] 894 files checked (508 concepts, 162 sources, 36 indexes, 188 topics)
- [x] 0 files failed to read (ERRORS_READING=0)
- [x] 2 ERRORs — both missing `## Co-occurring tags` in new tag index files (layer2.md, perpdex.md)
- [x] 430 WARNINGs — all broken wikilinks (forward-references)
- [x] +3 files vs yesterday: 2 new tag indexes (layer2, perpdex) + 1 new topic index
- [x] Report written to wiki/reviews/2026-08-10_format-report.md

## Escalations

**[SYSTEMATIC VIOLATION]**
Pattern: 2 new tag index files (layer2.md, perpdex.md) missing `## Co-occurring tags` section. Same issue previously fixed in opinion.md and research.md on 2026-08-06.
Likely cause: Index Agent not including `## Co-occurring tags` section when creating new tag index files.
Recommendation: Update index-agent/SKILL.md to ensure `## Co-occurring tags` section is always included in tag index files.