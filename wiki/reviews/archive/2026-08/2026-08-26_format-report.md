# Format Validation — 2026-08-26

**Status:** approved
**Issues found:** 391
**Created:** 2026-08-26 23:16
**Validator:** format-validator
**Files checked:** 966 (540 concepts + 184 sources + 34 indexes + 208 topics)
**ERRORs**: 0
**WARNINGS**: 391
**INFOS:** 0
**Total issues**: 391
Files checked: 966
Total issues: 391

Δ from 2026-08-25 (pending — prior day's run): **0 net change** (391→391), **0 ERRORs** (flat at 0 — clean streak holds, tenth consecutive day), **391 WARNINGs (flat)**, **+16 files** (950→966: +8 concepts, +4 sources, +4 topics via git reconciliation, 0 merges/deletes), **268 unique broken targets (−1 from 269)**, **Top-20 list shifted** (critical-thinking resolved at 3 refs — compiled today; deep-work 4→5; intellectual-humility entered at 3). Composition churned, not flat: individual broken wikilinks 371→372 (+1), forward-reference groups 20→19 (−1). `critical-thinking` concept compiled today resolved 3 of its forward-references; new file `attention-management.md` added 1 new `[[deep-work]]` ref. Net: KB grows (+16), backlog flat, composition slowly shifting.

---

## Issue Summary

All 391 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 372 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 19 | Files with 4-6 broken links each, summarized as single entries |
| Unique broken targets | 268 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Frontmatter, sections, naming, markdown syntax all compliant across 966 files.

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 966 | 540 | 184 | 34 | 208 |

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

Standing note (one line, not an escalation): 268 unique broken targets — back down from the 269 plateau that held 08-22 through 08-25. First day of forward-reference resolution in the Count since the plateau formed: `critical-thinking` compiled today resolved 3 refs. Compile Agent's raw backlog is slowly draining; forward-references resolve only when those concepts get compiled.

---

## Verification

Checklist of steps taken this run:

- [x] validate.py run from KB root (exit 0) — 966 files scanned in one pass
- [x] parse_issues.py statistics extracted (391W, 0E, 0I, 268 unique targets)
- [x] Git reconciliation vs 2026-08-25 23:15 baseline: +16 added (8 concepts + 4 sources + 4 topics), 0 deleted, 0 merges
- [x] New-file link check: new concepts/sources contribute 1 broken wikilink (attention-management.md → [[deep-work]])
- [x] Top-20 comparison vs archived 08-25 report: critical-thinking (3) dropped out, deep-work 4→5, intellectual-humility entered — composition churned, not flat
- [x] Previous report Status header checked: 08-25 format report shows `pending` → still pending in _action-required.md, no reconcile needed
