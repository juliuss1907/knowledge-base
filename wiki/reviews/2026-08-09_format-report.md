# Format Validation — 2026-08-09

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-10
**Issues found:** 430
**Created:** 2026-08-09 23:15
**Validator:** format-validator
**Files checked:** 891 (508 concepts + 162 sources + 34 indexes + 187 topics)
**ERRORs**: 0
**WARNINGS**: 430
**INFOS:** 0
**Total issues**: 430
Files checked: 891
Total issues: 430

Δ from 2026-07-30 (approved): +24 files (+13 concepts, +3 sources, +8 topics), +19 WARNINGs (411→430)
Δ from 2026-08-08 (previous): 0 files, 0 ERRORs, 0 WARNINGs — identical run (3rd consecutive)

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 891 | 508 | 162 | 34 | 187 |

## Issues Found: 430

| Severity | Count | Category |
|---|---|---|
| ERROR | **0** | — |
| WARNING | **430** | Broken wikilinks (forward-references) |
| INFO | 0 | — |

**0 ERROR streak:** 3rd consecutive clean run (08-07, 08-08, 08-09). No new structural issues. KB format compliance is stable.

**All 430 WARNINGs are broken wikilinks** — these are forward-references to concepts not yet compiled. Broken wikilink references are expected in a growing KB where concepts link to each other and some targets haven't been written yet.

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
- `wiki/concepts/third-order-thinking.md` — 6 broken wikilinks
- `wiki/concepts/thought-experiment.md` — 6 broken wikilinks
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 broken wikilinks
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` — 6 broken wikilinks
- `wiki/sources/src_fs-blog-mental-models.md` — 7 broken wikilinks

---

## Verification

- [x] Validation script ran successfully (validate.py + parse_issues.py)
- [x] 891 files checked (508 concepts, 162 sources, 34 indexes, 187 topics)
- [x] 0 files failed to read (ERR_READ=0)
- [x] 0 ERRORs — all frontmatter, sections, naming, markdown syntax pass
- [x] 430 WARNINGs — all broken wikilinks (forward-references)
- [x] Results identical to 2026-08-08 and 2026-08-07 (3rd consecutive identical run)
- [x] Report written to wiki/reviews/2026-08-09_format-report.md

## Escalations

No escalations needed. All 430 WARNINGs are expected forward-references — these resolve when Compile Agent creates the missing concept files. No format-spec violations, no structural errors, no regressions. 3rd consecutive clean run — KB format compliance is stable.