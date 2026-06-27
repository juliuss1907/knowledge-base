# Output Validation — 2026-05-29

**Status:** pending
**Issues found:** 4
**Created:** 2026-05-29 11:20:00
**Validator:** output-validator

**Files checked:** 199 (86 sources + 113 concepts)
**New/modified since last validation:** 0 files (no new files compiled since 2026-05-28)

---

## Issue 1: Softbank Carry Trade — Sources body empty despite frontmatter

**File:** wiki/concepts/softbank-carry-trade.md
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** The `## Sources` section body is empty — no wikilinks listed. The frontmatter correctly has `sources: - "[[src_ai-reflexivity-loop-is-same]]"`, but the body section has no source listing.
**Evidence:**
```yaml
# Frontmatter (correct):
sources:
  - "[[src_ai-reflexivity-loop-is-same]]"

# Body section (empty):
## Sources

## Notes
```
**Suggested fix:** Add `- [[src_ai-reflexivity-loop-is-same]]` to the `## Sources` body section.

---

## Issue 2: 2 source files still have 1-sentence summaries (repeated from 2026-05-27/28 reports)

**File:** wiki/sources/src_ai-trillion-dollar-blind-spot.md, wiki/sources/src_will-ai-replace-systems-thinking.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Summaries remain at 1 substantive sentence each (requirement: 3–5 sentences). This has been flagged in the 2026-05-26, 2026-05-27, and 2026-05-28 reports. The Fix Agent has not expanded the summaries.
**Evidence:**
- `src_ai-trillion-dollar-blind-spot.md` line 27: "Companies are racing to embed AI into their products while ignoring the most critical customer touchpoint: the static landing page..."
- `src_will-ai-replace-systems-thinking.md` line 27: "AI will not replace systems thinking, but it will fundamentally change how systems thinking is practiced..."
**Suggested fix:** Expand each summary to 3–5 sentences. Include the main argument, key conclusion, and why the topic matters.

---

## Issue 3: src_llm-need-sleep-consolidation — OPEC cross-contamination issue remains unresolved

**File:** wiki/sources/src_llm-need-sleep-consolidation.md
**Severity:** WARNING
**Dimension:** Factual accuracy
**Issue:** The 2026-05-28 report flagged cross-contamination: the `## Original excerpts` section showed OPEC text ("The spare capacity that Saudi Arabia and the UAE held was the enforcement mechanism...") that doesn't belong in a paper about LLM memory consolidation. The current file (lines 47-53) shows correct excerpts from the Lee/McLeish/Goldstein/Fanti paper, suggesting the contamination may have been cleaned OR the report was in error about the file state. Full verification needed.
**Evidence:** Current file lines 49-53 show correct paper excerpts about "novel contribution" and "hippocampal replay." No OPEC text visible in current version.
**Suggested fix:** Confirm whether this issue was already fixed or if the contamination exists in a different section/file.

---

## Issue 4: 146 of 199 files (73%) still in draft status

**File:** All wiki/concepts/*.md, wiki/sources/*.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Most files in the knowledge base have `status: draft` — only ~53 files (27%) have been promoted to `status: reviewed`. This is not a quality error per se, but indicates the knowledge base is in an early stage of curation.
**Evidence:** `grep -c "status: draft\|status: reviewed" concepts/*.md sources/*.md` — 146 draft vs ~53 reviewed
**Suggested fix:** Consider scheduling review sessions to promote stable, well-formed files to `reviewed` status.

---

## Summary

| Severity | Count | Notes |
|----------|-------|-------|
| ERROR | 1 | softbank-carry-trade empty Sources body |
| WARNING | 2 | 2 short summaries (persistent issue), LLM sleep cross-contamination needs verification |
| INFO | 1 | Most files still in draft status |

**Key observations:**
1. **No new files** — the knowledge base had no new compilations since yesterday's report. This is normal if no new sources were ingested.
2. **Persistent summary issue** — `src_ai-trillion-dollar-blind-spot` and `src_will-ai-replace-systems-thinking` summaries have been flagged 3 times but remain at 1 sentence. Recommend escalating to Julius for manual review.
3. **Empty Sources body pattern** — softbank-carry-trade is the latest concept with this issue. Previously ai-productivity, human-judgment-ai, and generative-ai-seo had the same issue (reported 2026-05-28). Pattern suggests systematic compilation gap.
4. **Status distribution** — 73% draft indicates early-stage KB. Not a blocking issue but worth tracking for curation roadmap.

**Files with no issues found (sample):**
- concepts/logotherapy-frankl.md — well-structured, Vietnamese quality good
- concepts/meaning-through-suffering.md — well-structured
- concepts/tragic-optimism.md — well-structured
- concepts/existential-vacuum.md — well-structured
- sources/src_viktor-frankl-meaning-video.md — complete, coherent
- concepts/petrodollar-system.md — coherent, factual
- concepts/ai-infrastructure-bubble.md — coherent, substantial

**Recommendation:** Address the empty Sources body pattern systematically — check Compile Agent's generation of `## Sources` section body.