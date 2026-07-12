# Format Validation — 2026-07-12

**Status:** pending
**Issues found:** 307
**Created:** 2026-07-12 23:15
**Validator:** format-validator

> **Context:** Evening run. Previous report: 2026-07-11 (APPLIED — 0 ERRORs, 305 WARNINGs forward-ref wikilinks). Third consecutive clean run with zero ERRORs.
> **Delta vs 07-11:** 0 net file change, +2 WARNINGs (new broken wikilinks from fresh compilations).

---

## Summary

| Metric | Value |
|---|---|
| Files checked | 758 |
| Concepts | 422 |
| Sources | 140 |
| Indexes | 33 |
| Topics | 163 |
| **ERRORs** | **0** |
| **WARNINGs** | **307** |
| **INFOs** | **0** |

## Delta Tracking (vs 2026-07-11 APPROVED)

| Metric | 07-11 | 07-12 | Δ |
|---|---|---|---|
| Files checked | 758 | 758 | 0 |
| ERRORs | 0 | 0 | 0 |
| WARNINGs | 305 | 307 | **+2** |
| INFOs | 0 | 0 | 0 |
| Files with issues | ~158 | 160 | +2 |

**Assessment:** Net +2 WARNINGs — minor organic growth from newly compiled files referencing not-yet-compiled concepts. No new error categories. Stable.

---

## All Issues: Broken Wikilinks (307 WARNINGs)

All 307 WARNINGs are **broken wikilinks** — forward references to concepts that have not yet been compiled. This is the expected, stable state for a growing knowledge base.

### Breakdown

| Type | Count |
|---|---|
| Individual broken wikilinks | 286 |
| Grouped forward-reference summaries | 21 |
| Unique broken targets | 195 |
| Files affected | 160 |

### Top 20 Most-Referenced Missing Concepts

| Target | Files referencing |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[power-imbalance]]` | 3 |
| `[[first-order-thinking]]` | 3 |
| `[[breaking-point]]` | 2 |
| `[[momentum]]` | 2 |
| `[[multi-agent-systems]]` | 2 |
| `[[dao-legal-structure]]` | 2 |
| `[[ubi-universal-basic-income]]` | 2 |

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
| `wiki/concepts/systematic-trading.md` | 4 |
| `wiki/concepts/vibe-coding.md` | 4 |
| `wiki/concepts/activation-energy.md` | 3 |

---

## Analysis

### Frontmatter Compliance: CLEAN ✅
0 ERRORs — all 758 files have valid YAML, correct field types, proper tag values, valid dates.

### Section Structure: CLEAN ✅
0 ERRORs — all required sections present and in correct order for concept and source files.

### Naming Conventions: CLEAN ✅
0 ERRORs — all filenames follow slug rules, correct prefixes, valid file paths.

### Markdown Syntax: CLEAN ✅
0 ERRORs — no code block issues, no header-level violations, no malformed wikilinks.

### Broken Wikilinks: 307 WARNINGs (SYSTEMIC — No Action Needed)

This is the third consecutive run with **zero ERRORs** across all categories. The 307 WARNINGs are entirely forward-reference wikilinks — concepts that mention other concepts not yet compiled. This is inherent to how the KB grows organically. As new sources are ingested and compiled, these forward references naturally resolve.

**Top targets like `game-theory` (10 refs) and `confirmation-bias` (8 refs)** are clear priorities for future compilation — they would resolve the most warnings at once.

**No action required from Fix Agent.** These are not format errors; they're references to future content.

---

## Escalation

None. No ambiguous rules, no spec conflicts, no systematic format violations.

---

## Verdict

**KB format health: EXCELLENT.** Zero structural violations for the third consecutive day. 307 forward-reference WARNINGs are organic KB growth artifacts, not quality issues. No Fix Agent action needed.
