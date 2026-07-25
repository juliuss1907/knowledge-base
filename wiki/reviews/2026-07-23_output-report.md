# Output Validation — 2026-07-23

**Status:** approved
**Approved by:** Julius
**Issues found:** 4
**Created:** 2026-07-23 23:13:01
**Validator:** output-validator

---

## Issue 1: [SYSTEMATIC ISSUE] Double-i typo (ngườii/đờii/lờii/rờii/thờii/giớii) across 11/13 new files

**File:** Multiple — 11 files in today's batch
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Compile Agent consistently doubles the final 'i' after grave-accented Vietnamese vowels. 66 instances across 11 of 13 new files (85% affected). This is the fifth documented variant of the same root cause: LLM mishandling of the 'i' character following Vietnamese characters with diacritics.

**Affected files (new today):**

| File | ngườii | thờii | Total |
|---|---|---|---|
| `wiki/concepts/comparison-trap.md` | 12 | 1 | 13 |
| `wiki/concepts/second-order-thinking.md` | 4 | 6 | 10 |
| `wiki/sources/src_never-enough-ronacher.md` | 8 | 1 | 9 |
| `wiki/concepts/ai-dependency.md` | 6 | 1 | 7 |
| `wiki/concepts/work-life-balance.md` | 4 | 3 | 7 |
| `wiki/concepts/never-enough-culture.md` | 3 | 2 | 5 |
| `wiki/concepts/iatrogenics.md` | 3 | 1 | 4 |
| `wiki/concepts/enough.md` | 3 | 0 | 3 |
| `wiki/concepts/naive-interventionism.md` | 3 | 0 | 3 |
| `wiki/concepts/skin-in-the-game.md` | 3 | 0 | 3 |
| `wiki/concepts/presence.md` | 2 | 0 | 2 |

**Clean files (no double-i):**
- `wiki/sources/src_iatrogenics-farnam-street.md`
- `wiki/concepts/primum-non-nocere.md`

**Evidence:** `ngườii` appears where `người` is correct; `thờii` where `thời` is correct. Pattern consistent across all affected files.

**Suggested fix:** Fix Agent to apply sed across all 11 files:
```bash
sed -i 's/ngườii/người/g; s/đờii/đời/g; s/lờii/lời/g; s/rờii/rời/g; s/thờii/thời/g; s/giớii/giới/g' <file>
```

**Root cause:** Compile Agent prompt defect — LLM tokenization boundary instability between Vietnamese diacritic characters and following 'i'. Five variants documented so far (ngưởi, ngườii, người-spacing-merge, ngườI, ngườ). Recommend reviewing compile-agent/SKILL.md to prevent recurrence.

---

## Issue 2: Missing forward-reference wikilinks across 10 new concepts

**File:** 10 concepts in today's batch
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Concepts reference ~20 wikilinks to other concepts that have not yet been compiled. These are intentional forward-references (placeholders for future compilation), but they create dead links in the current knowledge graph.

**Affected references (grouped by target concept):**

Shared (2 files each):
- `[[burnout]]` — `never-enough-culture.md`, `work-life-balance.md`
- `[[hustle-culture]]` — `never-enough-culture.md`, `work-life-balance.md`
- `[[homeostasis]]` — `src_iatrogenics-farnam-street.md`, `iatrogenics.md`

Single references:
- `[[digital-minimalism]]`, `[[attention-economy]]`, `[[automation-paradox]]` — `ai-dependency.md`
- `[[envy]]`, `[[status-anxiety]]` — `comparison-trap.md`
- `[[contentment]]`, `[[minimalism]]`, `[[satisfaction]]` — `enough.md`
- `[[bias-for-action]]` — `naive-interventionism.md`
- `[[via-negativa]]` — `primum-non-nocere.md`
- `[[first-order-thinking]]`, `[[decision-making]]` — `second-order-thinking.md`
- `[[incentive-alignment]]`, `[[principal-agent-problem]]` — `skin-in-the-game.md`

**Evidence:** `grep -oP '\[\[\K[^]]+'` on each file, checked against `wiki/concepts/` and `wiki/sources/` file existence.

**Suggested fix:** Compile these missing concepts. Until then, links remain dead but do not block use of existing concepts. Priority targets: `burnout` and `hustle-culture` (referenced by 2 concepts each, related to never-enough-culture cluster).

---

## Issue 3: second-order-thinking.md has 23 key ideas (exceeds recommended range)

**File:** `wiki/concepts/second-order-thinking.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** The `## Key ideas` section contains 23 items, significantly exceeding the recommended 5-10 range. While all items are substantive and well-written, this density reduces scanability and may indicate the concept should be split or the key ideas consolidated.

**Evidence:** Line count from `## Key ideas` to `## Related concepts` = 23 bullet points (lines 20-43). Covers: definition, examples (chocolate, geopolitics, exercise), time-horizon framework, application method, competitive advantage argument.

**Suggested fix:** Either (a) consolidate related points into 10-12 broader items, or (b) split into separate `## Key ideas` (core) and `## Extended examples` sections.

---

## Issue 4: presence.md has lowercase title

**File:** `wiki/concepts/presence.md`
**Severity:** INFO
**Dimension:** Coherence
**Issue:** The markdown title is `# presence` (lowercase) instead of `# Presence` (title case). All other 466 concepts use title case for the H1 heading.

**Evidence:** Line 13: `# presence`

**Suggested fix:** Change `# presence` to `# Presence` on line 13.

---

## Summary

| Dimension | ERROR | WARNING | INFO |
|---|---|---|---|
| Factual | 0 | 0 | 0 |
| Completeness | 0 | 2 | 0 |
| Coherence | 0 | 0 | 1 |
| Vietnamese | 1 | 0 | 0 |

**Overall:** Today's batch of 13 files (2 sources + 11 concepts) is structurally sound — all files have complete sections, natural Vietnamese phrasing, and coherent arguments. The primary quality issue is the double-i typo (66 instances, 11/13 files), a recurring Compile Agent prompt defect. Two secondary issues: excessive key ideas in one concept and a minor title casing inconsistency. Forward-reference wikilinks (~20) are noted as expected placeholders, not blocking issues.

**Note:** Quick-scan also detected 464 concepts with 1-sentence definitions and 89 with <5 key points — these are pre-existing structural issues across the broader wiki, not specific to today's batch.
