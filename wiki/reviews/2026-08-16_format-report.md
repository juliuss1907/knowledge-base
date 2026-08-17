# Format Validation — 2026-08-16

**Status:** approved
**Approved by:** Julius
**Approved date:** 2026-08-16
**Issues found:** 393
**Created:** 2026-08-16 23:15
**Validator:** format-validator
**Files checked:** 923 (525 concepts + 169 sources + 34 indexes + 195 topics)
**ERRORs**: 0
**WARNINGS**: 393
**INFOS:** 0
**Total issues**: 393
Files checked: 923
Total issues: 393

Δ from 2026-08-15 (pending, same validator methodology): **+2 total issues** (391→393), **+2 unique broken targets** (268→270). Both increases are genuine — the KB grew by 2 valid files (525 vs 524 concepts, 169 vs 168 sources) whose forward-references added 2 net target entries to the broken-wikilink pool. No regressions, no new structural/format violations. The 391-issue baseline from 08-15 already reflected the validator `.md.md`-strip correction, so this +2 is real growth, not methodology noise.

---

## Issue Summary

All 393 issues are **WARNING** severity — broken wikilinks (forward-references to uncompiled concepts):

| Category | Count | Description |
|---|---|---|
| Individual broken wikilinks | 373 | Links to concepts/sources that don't exist yet |
| Forward-reference groups | 20 | Files with 4-9 broken links each, summarized as single entries |
| Unique broken targets | 270 | Distinct concept/source slugs referenced but not compiled |

**No ERRORs, no INFOS.** Fourth consecutive clean ERROR run (08-13, 08-14, 08-15, 08-16; the 50 ERRORs from 08-11/08-12 were resolved by Fix Agent on 08-13 and have stayed resolved).

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 923 | 525 | 169 | 34 | 195 |

---

## Top 20 Broken Targets

These are the most frequently referenced concepts/sources that don't exist yet:

| # | Target | Count |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[ai-coding-agents]]` | 5 |
| 4 | `[[career-design]]` | 5 |
| 5 | `[[decision-making]]` | 5 |
| 6 | `[[deep-work]]` | 4 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-hype-vs-reality]]` | 3 |
| 9 | `[[economic-inequality]]` | 3 |
| 10 | `[[critical-thinking]]` | 3 |
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

All 270 unique broken targets are forward-references to concepts not yet compiled. These resolve naturally as the Compile Agent processes more raw sources.

## Verification

- [x] Read `wiki/meta/format-spec.md` (ground truth) — present, valid YAML
- [x] Scanned all 923 wiki files (concepts + sources + indexes + topics) in one pass
- [x] Dispatched each file to correct spec via `type` field (concept/source → format-spec, index → index-spec)
- [x] Validated 5 dimensions: frontmatter, sections, naming, markdown, wikilinks
- [x] Skipped `context/USER.md` (read-only, no frontmatter expected)
- [x] Confirmed no `wiki/drafts/` files were validated (already flagged)
- [x] Read-only run — no wiki content files modified

## Escalations

None. No ambiguous rules, no spec conflicts, no systematic violations. The 393 WARNINGs are all forward-reference broken wikilinks — a known, self-resolving condition, not a compliance failure.