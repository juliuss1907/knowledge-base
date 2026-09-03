# Format Validation — 2026-09-01

**Status:** approved
**Issues found:** 396
**Created:** 2026-09-01 23:15:37
**Validator:** format-validator
**Files checked:** 1027 (567 concepts + 195 sources + 34 indexes + 231 topics)
**ERRORs**: 0
**WARNINGS**: 396
**INFOS:** 0
**Total issues**: 396
Files checked: 1027
Total issues: 396

Δ from 2026-08-31 23:15 run (approved): **−3 net** (399→396), **0 ERRORs** (3→0 — ALL THREE 08-31 ERRORs RESOLVED by Fix Agent: 2 slug renames `src_ai-engineering-skills-map-building-deploying-ai-applications`→`src_ai-eng-skills-map-building-deploying` (60→41 chars) + `src_ai-engineering-skills-map-software-engineering-fundamentals`→`src_ai-eng-skills-map-se-fundamentals` (59→38 chars), + `src_impeccable.md` missing `## Key points` added — verified via git log R100 renames at 2026-09-01 10:02 + live file grep), **396 WARNINGs (0 — exact flat)**, **0 new wiki files** (1027→1027 — no compilation today, variant no-compilation-happened), **270 unique broken targets (0 — flat day 2 at 270)**, **Top-20 identical** (same slugs, same counts, same order — all 20 rows match 08-31 exactly). Composition: individual broken 377→377 (flat), forward-ref groups 19→19 (flat), other warnings 0→0 (flat). 1 new raw file (`raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md` at 17:13) ingested but NOT yet compiled — 0 wiki-layer growth. Net: the only change is the ERROR backlog clearing; the broken-wikilink backlog is byte-identical to yesterday.

| Metric | 08-31 | 09-01 | Delta |
|---|---|---|---|
| Files checked | 1027 | 1027 | 0 |
| Total issues | 399 | 396 | −3 |
| ERRORs | 3 | 0 | −3 |
| WARNINGs | 396 | 396 | 0 |
| Unique broken targets | 270 | 270 | 0 |
| Individual broken | 377 | 377 | 0 |
| Forward-ref groups | 19 | 19 | 0 |
| Other warnings | 0 | 0 | 0 |

---

## Issue Summary

**Clean ERROR streak RESTORED (day 1 at 0 ERRORs).** The 3 ERRORs that broke the 14-day clean streak on 08-31 have all been resolved by Fix Agent this morning (verified 10:02 commit):

1. `src_ai-engineering-skills-map-building-deploying-ai-applications.md` — slug 60 chars → **renamed** to `src_ai-eng-skills-map-building-deploying.md` (41 chars, under 50 limit)
2. `src_ai-engineering-skills-map-software-engineering-fundamentals.md` — slug 59 chars → **renamed** to `src_ai-eng-skills-map-se-fundamentals.md` (38 chars, under 50 limit)
3. `src_impeccable.md` — missing `## Key points` → **section added** (now present, live grep confirms)

Backlink integrity verified: `ai-engineering-skills.md` frontmatter + body now reference the renamed slugs (`[[src_ai-eng-skills-map-se-fundamentals]]`, `[[src_ai-eng-skills-map-building-deploying]]`) and all resolve. No broken backlinks introduced by the renames.

The 396 WARNINGs are all broken wikilinks (forward-references to uncompiled concepts/sources):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 377 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-9 broken links each, summarized as single entries |
| Other warnings | 0 | No other warning categories |
| Unique broken targets | 270 | Distinct concept/source slugs referenced but not compiled |

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1027 | 567 | 195 | 34 | 231 |

---

## Top 20 Broken Targets

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[deep-work]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-assisted-development]]` | 3 |
| 9 | `[[ai-hype-vs-reality]]` | 3 |
| 10 | `[[economic-inequality]]` | 3 |
| 11 | `[[intellectual-humility]]` | 3 |
| 12 | `[[naval-ravikant]]` | 3 |
| 13 | `[[risk-parity]]` | 3 |
| 14 | `[[second-law-of-thermodynamics]]` | 3 |
| 15 | `[[homeostasis]]` | 3 |
| 16 | `[[saying-no]]` | 3 |
| 17 | `[[cognitive-dissonance]]` | 3 |
| 18 | `[[power-imbalance]]` | 3 |
| 19 | `[[stoicism]]` | 3 |
| 20 | `[[first-order-thinking]]` | 3 |

**Top-20 identical to 08-31** — same slugs, same counts, same order. No targets entered, none fell off. The forward-reference pool is frozen because no new content files were compiled today.

---

## Forward-Reference Groups (19)

Files carrying 4-9 forward-references each (summarized as single WARNING entries):

- wiki/concepts/third-order-thinking.md: 6
- wiki/concepts/thought-experiment.md: 6
- wiki/sources/src_11-minutes-hack-github.md: 4
- wiki/sources/src_ai-future-skills.md: 4
- wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md: 6
- wiki/sources/src_farnam-street-mental-models-biology-series.md: 6
- wiki/sources/src_farnam-street-mental-models-systems-thinking.md: 6
- wiki/sources/src_feedback-loops-mental-model.md: 4
- wiki/sources/src_fs-blog-mental-models.md: 7
- wiki/sources/src_global-macro-investing.md: 4
- wiki/sources/src_hermes-polymarket-btc-trading-agent.md: 4
- wiki/sources/src_incentives-hidden-forces.md: 6
- wiki/sources/src_mental-models-of-art.md: 9
- wiki/sources/src_mental-models-of-economics.md: 9
- wiki/sources/src_probabilistic-thinking.md: 6
- wiki/sources/src_the-cost-of-discretion.md: 4
- wiki/sources/src_the-seed-and-the-machine.md: 4
- wiki/sources/src_thought-experiment.md: 9
- wiki/sources/src_tribute-system-new-world-order.md: 4

Identical set to 08-31 — no new forward-reference groups formed, none resolved.

---

## New Files This Run

**Zero new wiki files** since 08-31 23:15. Git reconciliation (`git log --since=2026-08-31 --diff-filter=A -- wiki/concepts wiki/sources wiki/tag wiki/topic`) returns 0 additions. The wiki layer is byte-identical to the 08-31 run.

**Raw layer grew +1** (not compiled):
- `raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md` (ingested 17:13)

**3 source files modified** by Fix Agent (the 08-31 ERROR fixes — 2 renames + 1 section). **Zero deletions** (no merges).

---

## Escalations

No new escalations this run. The 08-31 Compile Agent quality issue (3 ERRORs: 2 slug-length + 1 missing section) has been **RESOLVED** — all three fixed by Fix Agent and verified this run. No fix needed for the 396 forward-ref WARNINGs (they resolve naturally as Compile Agent processes raw files).

Standing note (one line, not an escalation): 270 unique broken targets — day 2 at 270 (was 268 for 6 days, 269 for 4 days before that). The broken-wikilink backlog is neither draining nor accumulating right now because no compilation happened today. Compile Agent's next target priority: `[[game-theory]]` (10 refs) and `[[confirmation-bias]]` (8 refs). 1 raw file sitting uncompiled as of 17:13 (`raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md`).

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 1027 files scanned in one pass
- [x] parse_issues.py statistics extracted (0E + 396W + 0I, 270 unique targets)
- [x] Git reconciliation vs 2026-08-31 23:15 baseline: +0 wiki files added (0 concepts + 0 sources + 0 topics), 0 deleted, 0 merges; +1 raw file (uncompiled); 3 source files modified by Fix Agent
- [x] All 3 ERRORs from 08-31 verified resolved: 2 slug renames confirmed via git log R100 (10:02) + `ls` (41/38 chars, under 50); `src_impeccable.md` `## Key points` confirmed via live grep
- [x] Backlink integrity after renames: `ai-engineering-skills.md` references resolve to renamed slugs — no new broken links introduced
- [x] Top-20 comparison vs 2026-08-31 report: identical (all 20 rows match)
- [x] Forward-ref groups vs 08-31: identical 19 groups
- [x] Previous report Status header checked: 08-31 format report shows `approved` + already ✅ APPLIED in _action-required → no reconcile needed
- [x] Output Validator 09-01 run (23:03) confirms 0 new source/concept files — corroborates no-compilation
- [x] YAML edge cases handled (datetime.date, unquoted [[wikilinks]])
- [x] File-count delta reconciled via git log --diff-filter=A/D (not mtime)
- [x] context/USER.md skipped (read-only, no frontmatter expected)
- [x] Topics dispatched by scope:topic (not index-spec.md)
- [x] Tag files cross-checked: 0 unquoted-parent false positives (24→0 stays resolved)
