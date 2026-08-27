# Format Validation — 2026-08-27

**Status:** approved
**Issues found:** 391
**Created:** 2026-08-27 19:15
**Validator:** format-validator
**Files checked:** 975 (548 concepts + 185 sources + 34 indexes + 208 topics)
**ERRORs**: 0
**WARNINGS**: 391
**INFOS:** 0
**Total issues**: 391
Files checked: 975
Total issues: 391

Δ from 2026-08-26 (pending — prior day's run): **0 net change** (391→391), **0 ERRORs** (flat at 0 — clean streak holds, eleventh consecutive day), **391 WARNINGs (flat)**, **+9 files** (966→975: +8 concepts, +1 source via git reconciliation, 0 merges/deletes), **268 unique broken targets (flat)**, **Top-20 list identical** (same slugs, same counts — deep-work 5, intellectual-humility 3, etc.). Composition exact-zero-flat, not churned: individual broken wikilinks 372→372 (flat), forward-reference groups 19→19 (flat). KB grew +9 (gcp-ai-startup-governance cluster), all 9 new files contributed **0 broken wikilinks** (all 10 targets trong Related concepts đã tồn tại). Net: KB grows (+9), backlog flat, composition frozen.

---

## Issue Summary

All 391 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 372 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-6 broken links each, summarized as single entries |
| Unique broken targets | 268 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Frontmatter, sections, naming, markdown syntax all compliant across 975 files.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 975 | 548 | 185 | 34 | 208 |

---

## Top 20 Broken Targets

These are the most frequently referenced concepts/sources that don't exist yet:

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[deep-work]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-hype-vs-reality]]` | 3 |
| 9 | `[[economic-inequality]]` | 3 |
| 10 | `[[intellectual-humility]]` | 3 |
| 11 | `[[naval-ravikant]]` | 3 |
| 12 | `[[risk-parity]]` | 3 |
| 13 | `[[second-law-of-thermodynamics]]` | 3 |
| 14 | `[[homeostasis]]` | 3 |
| 15 | `[[saying-no]]` | 3 |
| 16 | `[[cognitive-dissonance]]` | 3 |
| 17 | `[[power-imbalance]]` | 3 |
| 18 | `[[stoicism]]` | 3 |
| 19 | `[[first-order-thinking]]` | 3 |
| 20 | `[[breaking-point]]` | 2 |

---

## Forward-Reference Groups (19)

Files carrying 4-6 forward-references each (summarized as single WARNING entries):

- wiki/concepts/third-order-thinking.md: 6
- wiki/concepts/thought-experiment.md: 6
- wiki/sources/src_11-minutes-hack-github.md: 4
- wiki/sources/src_ai-future-skills.md: 4
- wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md: 6
- (14 more groups — full list in `/tmp/issues.txt`, parse via `parse_issues.py`)

---

## Escalations

None.

Standing note (one line, not an escalation): 268 unique broken targets — flat day 2 after exiting the 269 plateau (08-22→08-25). Composition frozen: exact-zero-flat with identical Top-20, same individual/forward/Files-checked splits. Backlog is neither draining nor accumulating; it's a steady state while KB grows. Compile Agent's next target priority: `[[game-theory]]` (10 refs) and `[[deep-work]]` (5 refs, most cited uncompiled concept).

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 975 files scanned in one pass
- [x] parse_issues.py statistics extracted (391W, 0E, 0I, 268 unique targets)
- [x] Git reconciliation vs 2026-08-26 23:16 baseline: +9 added (8 concepts + 1 source), 0 deleted, 0 merges
- [x] New-file link check: all 9 new files contribute **0 broken wikilinks** (verified by Output validator — all 10 targets in Related concepts exist)
- [x] Top-20 comparison vs 2026-08-26 report: identical — same slugs, same counts. Exact-zero-flat.
- [x] Previous report Status header checked: 08-26 format report shows `pending` → still pending in _action-required.md, no reconcile needed