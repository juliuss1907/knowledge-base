# Format Validation — 2026-07-11

**Status: applied
**Approved by:** Julius
**Issues found:** 305
**Created:** 2026-07-11 23:15
**Validator:** format-validator

> **Context:** Evening run after Output Validator (22:00). Previous report: 2026-07-10 (APPLIED — 2 ERRORs fixed by Fix Agent on 07-11).
> **Delta vs 07-10:** 0 net file change, -2 ERRORs (both fixed), -1 WARNING.

---

## Delta Summary

| Metric | 2026-07-10 (previous) | 2026-07-11 (today) | Delta |
|---|---|---|---|
| Files checked | 719 | 719 | 0 |
| Concepts | 415 | 415 | 0 |
| Sources | 137 | 137 | 0 |
| Indexes | 10 | 10 | 0 |
| Topics | 157 | 157 | 0 |
| Total issues | 308 | 305 | -3 |
| ERROR | 2 | 0 | **-2** ✅ |
| WARNING | 306 | 305 | -1 |
| INFO | 0 | 0 | 0 |

**Key changes:**
- ✅ **Both long-standing ERRORs RESOLVED** — slug length (`src_youre-trained-for-world-that-no-longer-exists`) and missing `## Notes` in `tag.md` fixed by Fix Agent (07-11 batch)
- 📊 **No net file growth** — KB size stable at 719 files
- ⚠️ **-1 WARNING** — one less broken wikilink (marginal)

---

## Spec Compliance Summary

| Category | Files | ERROR | WARNING | Notes |
|---|---|---|---|---|
| **Concepts** (415) | `wiki/concepts/` | 0 | 284+21 groups | All clean — only forward-ref wikilinks |
| **Sources** (137) | `wiki/sources/` | 0 | 0 | 100% clean |
| **Indexes** (10) | `wiki/tag/` | 0 | 0 | 100% clean |
| **Topics** (157) | `wiki/topic/` | 0 | 0 | 100% clean |
| **Raw indexes** | `raw/*/` | 0 | 0 | 100% clean |
| **Root indexes** | `wiki/wiki.md`, etc. | 0 | 0 | 100% clean |

---

## WARNINGs (305) — Forward-reference wikilinks

All 305 WARNINGs are broken wikilinks pointing to concepts/sources that do not yet exist in the KB. This is a systemic pattern — the KB references concepts ahead of compilation.

- **284 individual broken references** + **21 forward-reference groups** (batched)
- **193 unique broken targets**

### Top 20 most-referenced missing targets

| Target | File count |
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

### Forward-reference groups (21)

Files where all broken wikilinks were batched:
- `wiki/concepts/third-order-thinking.md` — 6 links
- `wiki/concepts/thought-experiment.md` — 6 links
- `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` — 6 links
- `wiki/sources/src_farnam-street-mental-models-biology-series.md` — 6 links
- `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` — 6 links
- `wiki/sources/src_incentives-hidden-forces.md` — 6 links
- `wiki/sources/src_probabilistic-thinking.md` — 6 links
- `wiki/sources/src_mental-models-of-art.md` — 9 links
- `wiki/sources/src_mental-models-of-economics.md` — 9 links
- `wiki/sources/src_thought-experiment.md` — 9 links
- `wiki/sources/src_fs-blog-mental-models.md` — 7 links
- `wiki/sources/src_11-minutes-hack-github.md` — 4 links
- `wiki/sources/src_6-thoi-quen-binh-thuong-dang-huy-hoai-nao-bo.md` — 4 links
- `wiki/sources/src_ai-future-skills.md` — 4 links
- `wiki/sources/src_critical-thinking-dennett.md` — 4 links
- `wiki/sources/src_feedback-loops-mental-model.md` — 4 links
- `wiki/sources/src_global-macro-investing.md` — 4 links
- `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` — 4 links
- `wiki/sources/src_the-cost-of-discretion.md` — 4 links
- `wiki/sources/src_the-seed-and-the-machine.md` — 4 links
- `wiki/sources/src_tribute-system-new-world-order.md` — 4 links

### Files with most individual broken links (top 5)

| File | Broken count |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |

### Resolution path for forward-reference warnings

These WARNINGs will auto-resolve as referenced concepts are compiled. **No action needed** — this is expected behavior for a growing KB. Priority candidates for compilation (most-referenced):
1. `game-theory` (10 refs) — foundational concept, highest value
2. `confirmation-bias` (8 refs) — cognitive bias, widely referenced
3. `ai-coding-agents`, `career-design`, `decision-making` (5 refs each)

---

## Summary

| Severity | Count | Actionable |
|---|---|---|
| ERROR | 0 | ✅ Clean — no fixes needed |
| WARNING | 305 | ⏳ No — forward-refs auto-resolve |
| INFO | 0 | — |

🎉 **First clean run since 2026-07-02.** Format compliance across all 719 files is at 100% — zero frontmatter errors, zero section errors, zero naming violations, zero code-block issues. The 305 WARNINGs are all expected forward-reference wikilinks that auto-resolve with KB growth.

**Recommendation:** Approve as-is. No format fixes needed.
