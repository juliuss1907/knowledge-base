# Output Validation — 2026-05-28

**Status:** pending
**Issues found:** 7
**Created:** 2026-05-28 08:26:30
**Validator:** output-validator

**Files checked:** 149 (30 sources + 119 concepts)
**New/modified since last validation:** 38 files (8 today + 30 yesterday)

---

## Issue 1: Cross-contaminated excerpt — OPEC text in LLM Sleep source

**File:** wiki/sources/src_llm-need-sleep-consolidation.md
**Severity:** ERROR
**Dimension:** Factual accuracy
**Issue:** The `## Original excerpts` section contains an excerpt about Saudi Arabia and OPEC oil pricing that is completely unrelated to the LLM Sleep paper. This appears to be a cross-contamination error from the OPEC source file during compilation.
**Evidence:**
```
51|> "The spare capacity that Saudi Arabia and the UAE held was the enforcement
   |  mechanism. It was the threat that made the kink real — if anyone defected
   |  from the agreed price, the Saudis could flood the market and destroy the
   |  price-cutter's revenue."
```
The paper is about recurrent consolidation passes in SSM-attention hybrid LLMs (authors: Lee, McLeish, Goldstein, Fanti — CMU/UMD). Saudi Arabian oil policy does not appear in the paper. This excerpt belongs in `src_uae-opec-exit-end-of-era.md`.
**Suggested fix:** Remove the OPEC excerpt (lines 51-52). Replace with an actual excerpt from the paper about the consolidation mechanism, e.g., from the abstract or results section.

---

## Issue 2: 15 dangling wikilinks referencing non-existent concepts

**File:** 8 files (all 8 new files compiled today)
**Severity:** ERROR
**Dimension:** Completeness / Coherence
**Issue:** All 8 files compiled today reference wikilinks to 15 concepts that do not exist in `wiki/concepts/`. The wikilinks appear in `## Concepts referenced` (source files) and `## Related concepts` (concept files). Clicking any of these in Obsidian leads to a dead page.

**Missing concepts and which files reference them:**

| Missing concept | Referenced by |
|---|---|
| `claude-code-routines` | src_build-ai-trading-agent, ai-trading-agent |
| `alpaca-api` | src_build-ai-trading-agent, ai-trading-agent |
| `paper-trading` | src_build-ai-trading-agent, ai-trading-agent |
| `agent-journal-pattern` | src_build-ai-trading-agent, ai-trading-agent |
| `multi-agent-risk-review` | src_build-ai-trading-agent, ai-trading-agent |
| `state-space-models-ssm` | src_llm-need-sleep, llm-sleep, memory-consolidation-offline |
| `fast-weights` | src_llm-need-sleep, llm-sleep, memory-consolidation-offline |
| `gated-delta-networks` | src_llm-need-sleep, llm-sleep |
| `kv-cache-eviction` | src_llm-need-sleep, llm-sleep, memory-consolidation-offline |
| `hippocampal-replay` | src_llm-need-sleep, llm-sleep |
| `kinked-demand-curve` | src_uae-opec-exit, opec-cartel-structure |
| `spare-production-capacity` | src_uae-opec-exit, opec-cartel-structure |
| `strait-of-hormuz-geopolitics` | src_uae-opec-exit |
| `uae-saudi-rivalry` | src_uae-opec-exit, opec-cartel-structure, petrodollar-system |
| `american-security-guarantee` | src_uae-opec-exit, petrodollar-system |

**Evidence:** `test -f wiki/concepts/<slug>.md` returns MISSING for all 15.
**Suggested fix:** Either create stub concept files for all 15 missing concepts, or replace wikilinks with plain text references. This is a systematic compilation issue — the Compile Agent referenced sub-concepts without creating them.

---

## Issue 3: Empty `## Sources` body in 3 concept files (from 2026-05-27)

**File:** wiki/concepts/ai-productivity.md, wiki/concepts/human-judgment-ai.md, wiki/concepts/generative-ai-seo.md
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** Three concept files have valid `sources:` in frontmatter but the `## Sources` section body is empty — no wikilinks listed. All other concept files list their source wikilinks in the body (e.g., `- [[src_how-ai-productivity-fails]]`).
**Evidence:**
```
// ai-productivity.md lines 32-33, human-judgment-ai.md lines 31-33, generative-ai-seo.md lines 31-33:
## Sources

## Backlinks
```
**Suggested fix:** Add the source wikilinks to the `## Sources` section body, matching what's in frontmatter:
- ai-productivity.md → add `- [[src_how-ai-productivity-fails]]`
- human-judgment-ai.md → add `- [[src_will-ai-replace-systems-thinking]]`
- generative-ai-seo.md → add `- [[src_what-comes-after-systems-thinking]]`

---

## Issue 4: Short summaries still unfixed from 2026-05-26/27 reports (2 source files)

**File:** wiki/sources/src_ai-trillion-dollar-blind-spot.md, wiki/sources/src_will-ai-replace-systems-thinking.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Summaries remain at 1 substantive sentence each (requirement: 3–5 sentences). These were flagged as Issues 3 and 4 in the 2026-05-26 report and Issue 4 in the 2026-05-27 report. The Fix Agent added `## Original excerpts` (good) but did not expand the summaries.
**Evidence:**
- `src_ai-trillion-dollar-blind-spot.md` Summary lines 26-27: 1 sentence spanning 2 lines about companies ignoring landing pages
- `src_will-ai-replace-systems-thinking.md` Summary lines 25-27: 1 sentence about AI not replacing systems thinking
**Suggested fix:** Expand each summary to 3–5 sentences. Add key conclusions, implications, or call to action from the full source content.

---

## Issue 5: 8 new files all link to non-existent concepts — systematic compilation pattern

**File:** All 8 files compiled 2026-05-28
**Severity:** WARNING
**Dimension:** Completeness (systematic)
**Issue:** All 8 new files compiled today contain wikilinks to concepts that don't exist. This suggests the Compile Agent is referencing sub-concepts in the `## Concepts referenced` / `## Related concepts` sections without creating corresponding concept files. The 15 missing concepts are evenly distributed across 3 topic clusters:
- AI Trading: 5 missing (claude-code-routines, alpaca-api, paper-trading, agent-journal-pattern, multi-agent-risk-review)
- LLM Architecture: 5 missing (state-space-models-ssm, fast-weights, gated-delta-networks, kv-cache-eviction, hippocampal-replay)
- Oil Geopolitics: 5 missing (kinked-demand-curve, spare-production-capacity, strait-of-hormuz-geopolitics, uae-saudi-rivalry, american-security-guarantee)

**Pattern:** Same as Issue 3 from 2026-05-27 report — Compile Agent creates wikilinks to sub-concepts it doesn't create. The 2026-05-27 issue was resolved by creating `systems-thinking.md` and `second-order-effects.md` stubs.
**Suggested fix:** Either update Compile Agent to create stub concept files for all referenced sub-concepts, or limit `## Concepts referenced` to only existing concepts.

---

## Issue 6: Two older dangling wikilinks across existing files

**File:** wiki/sources/src_luke-alvoeiro-multi-agent-architecture-factory.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** Two dangling wikilinks in the `## Concepts referenced` section:
- `[[orchestrator-worker-validator]]` — MISSING
- `[[agent-handoff]]` — MISSING
These link to concepts that don't exist. `factory-missions`, `multi-agent-taxonomy`, and `validation-contract` (the other 3 referenced) DO exist.
**Evidence:**
```
41|- [[orchestrator-worker-validator]]
42|- [[agent-handoff]]
```
**Suggested fix:** Create stub concept files or replace with plain text references.

---

## Issue 7: 3 concept files (ai-productivity, human-judgment-ai, generative-ai-seo) have mismatched Sources section

**File:** wiki/concepts/ai-productivity.md, wiki/concepts/human-judgment-ai.md, wiki/concepts/generative-ai-seo.md
**Severity:** INFO
**Dimension:** Coherence
**Issue:** These 3 concept files have `sources:` in YAML frontmatter (e.g., `sources:\n  - [[src_how-ai-productivity-fails]]`) but the `## Sources` body section is empty. Contrast with `ai-augmented-systems-thinking.md` which properly lists sources both in frontmatter AND in the body section. This creates an inconsistent pattern where frontmatter claims sources exist but body doesn't reflect them.
**Evidence:** `## Sources` section body is empty in all 3 files.
**Suggested fix:** (Covered by Issue 3 — same fix)

---

## Summary

| Severity | Count | Notes |
|----------|-------|-------|
| ERROR | 3 | Cross-contaminated excerpt, 15 dangling wikilinks across 8 files, empty Sources section in 3 files |
| WARNING | 2 | Short summaries unfixed (x2), systematic dangling wikilinks pattern |
| INFO | 2 | 2 older dangling wikilinks, Sources frontmatter/body mismatch |

**Key observations:**
1. **Cross-contamination bug:** An OPEC excerpt leaked into the LLM Sleep source file — this suggests a compilation tool issue where excerpt buffers are not being cleared between files.
2. **Systematic dangling wikilinks:** All 8 new files today (100%) reference concepts that don't exist. The 2026-05-27 report had a similar issue (Issue 3: dangling `systems-thinking` and `second-order-effects`) which was later fixed by creating stubs. The same pattern now repeats on a larger scale (15 missing concepts vs 2 last time).
3. **4 of 6 unfixed issues from 2026-05-26 are now resolved** (duplicate Notes, missing Original excerpts, section name case, non-standard section) — the Fix Agent caught up on these. Only the summary length issue remains unfixed across 3 consecutive reports.
4. **Yesterday's 2026-05-27 report got fully approved** — `_action-required.md` shows all issues applied, system was clean as of yesterday.

**Recommendation:** Flag the cross-contamination and systematic dangling wikilinks issues for Compile Agent prompt review.
