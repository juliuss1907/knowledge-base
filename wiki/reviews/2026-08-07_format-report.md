# Format Validation — 2026-08-07

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-10
**Issues found:** 430
**Created:** 2026-08-07 23:15
**Validator:** format-validator
**Files checked:** 891 (508 concepts + 162 sources + 34 indexes + 187 topics)
**ERRORs**: 0
**WARNINGS**: 430
**INFOS:** 0
**Total issues**: 430
Files checked: 891
Total issues: 430

Δ from 2026-07-30 (approved): +24 files (+13 concepts, +3 sources, +8 topics), +19 WARNINGs (411→430)
Δ from 2026-08-05 (last run): +5 files (+4 concepts, +1 source), -3 ERRORs (fixed by Fix Agent 08-06), WARNINGs unchanged (430→430)

---

## Issues Found: 430

| Severity | Count | Category |
|---|---|---|
| ERROR | **0** | — |
| WARNING | **430** | Broken wikilinks (forward-references) |
| INFO | 0 | — |

**0 ERROR streak:** Restored — 08-06 Fix Agent resolved the 3 ERRORs (career→strategy sub_tag, Co-occurring tags sections). 1st consecutive clean run.

**3 ERRORs resolved by Fix Agent (2026-08-06):**
- `wiki/concepts/optionality-principle.md` — sub_tag `career` → `strategy` (career not in TAGS.md Pool B)
- `wiki/tag/opinion.md` — added `## Co-occurring tags` section header
- `wiki/tag/research.md` — added `## Co-occurring tags` section header

---

## All Issues — WARNING Level Only

**430 WARNINGs** — all are **broken wikilinks** (forward-references to uncompiled concepts). No structural format errors (frontmatter, sections, naming, code blocks all clean).

### Summary

| Category | Count |
|---|---|
| Individual broken wikilinks | 410 |
| Forward-reference summary groups | 20 |
| Unique broken targets | 278 |

### Top 20 Broken Link Targets

| Target | Count |
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

### Forward-Reference Summary Groups (20)

| File | Count | Notes |
|---|---|---|
| `wiki/sources/src_mental-models-of-art.md` | 9 | Forward-references |
| `wiki/sources/src_mental-models-of-economics.md` | 9 | Forward-references |
| `wiki/sources/src_thought-experiment.md` | 9 | Forward-references |
| `wiki/sources/src_fs-blog-mental-models.md` | 7 | Forward-references |
| `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 | Forward-references |
| `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 | Forward-references |
| `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 | Forward-references |
| `wiki/sources/src_incentives-hidden-forces.md` | 6 | Forward-references |
| `wiki/sources/src_probabilistic-thinking.md` | 6 | Forward-references |
| `wiki/concepts/third-order-thinking.md` | 6 | Forward-references |
| `wiki/concepts/thought-experiment.md` | 6 | Forward-references |
| `wiki/sources/src_11-minutes-hack-github.md` | 4 | Forward-references |
| `wiki/sources/src_ai-future-skills.md` | 4 | Forward-references |
| `wiki/sources/src_critical-thinking-dennett.md` | 4 | Forward-references |
| `wiki/sources/src_feedback-loops-mental-model.md` | 4 | Forward-references |
| `wiki/sources/src_global-macro-investing.md` | 4 | Forward-references |
| `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 | Forward-references |
| `wiki/sources/src_the-cost-of-discretion.md` | 4 | Forward-references |
| `wiki/sources/src_the-seed-and-the-machine.md` | 4 | Forward-references |
| `wiki/sources/src_tribute-system-new-world-order.md` | 4 | Forward-references |

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

---

## Files checked

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 891 | 508 | 162 | 34 | 187 |

---

## Verification

- [x] Validation script `validate.py` ran successfully (exit 0)
- [x] All 891 files read without errors (ERRORS_READING=0)
- [x] 0 format-spec violations (ERRORs)
- [x] 430 broken wikilink WARNINGs (all forward-references)
- [x] Top 20 targets, forward-reference summary groups, and top-10 files tabulated
- [x] Delta computed against 2026-07-30 (approved) and 2026-08-05 (last run)
- [x] Fix Agent batch (08-06) resolved 3 ERRORs from 08-01 through 08-05
- [x] Report written to `wiki/reviews/2026-08-07_format-report.md`

---

## Escalations

None. 0 ERRORs — all WARNINGs are forward-reference broken wikilinks, which are expected in a growing KB and resolve automatically when referenced concepts are compiled.