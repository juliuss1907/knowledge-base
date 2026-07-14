# Output Validator Report — 2026-07-12

**Status: applied
**Approved by:** Julius
**Issues found:** 4 (1 ERROR, 2 WARNING, 1 INFO)
**Created:** 2026-07-12 23:10:48
**Validator:** output-validator

---

## Summary

- **Files checked:** 563 (140 sources + 422 concepts + 1 action file)
- **New files validated (deep):** 10 (3 sources + 7 concepts)
- **Previous validation:** 2026-07-10 (archived). 2026-07-11 was silent (0 new files).
- **07-12 batch:** Two thematic clusters — crypto communications (a16z, 1 source + 3 concepts) and Charlie Munger learning method (2 sources + 4 concepts). All 10 files are well-structured with complete sections, coherent arguments, and clean Vietnamese.

---

## New file deep validation: ALL CLEAN

| File | Definition | Key ideas | Sections | Typos | Verdict |
|---|---|---|---|---|---|
| `src_the-new-comms-playbook-show-dont.md` | N/A (source) | 8 | Complete | None | PROMOTE |
| `src_giai-thich-sau-phuong-phap-hoc-charlie-munger.md` | N/A (source) | 10 | Complete | None | PROMOTE |
| `src_learn-anything-like-charlie-munger.md` | N/A (source) | 8 | Complete | None | PROMOTE |
| `concepts/show-me-era.md` | Substantial | 7 | Complete | None | PROMOTE |
| `concepts/proof-stack.md` | Substantial | 6 | Complete | None | PROMOTE |
| `concepts/two-track-communications.md` | Substantial | 6 | Complete | None | PROMOTE |
| `concepts/fluency-illusion.md` | Substantial | 6 | Complete | None | PROMOTE |
| `concepts/retrieval-practice.md` | Substantial | 7 | Complete | None | PROMOTE |
| `concepts/spacing-effect.md` | Substantial | 6 | Complete | None | PROMOTE |
| `concepts/chauffeur-knowledge.md` | Substantial | 5 | Complete | None | PROMOTE |

**No mechanical issues detected in new files:**
- Zero "ngưởi" typos
- Zero "ngườii/đờii" double-i typos
- Zero "người" spacing merge issues
- Zero truncated files
- Zero empty Key ideas sections
- Vietnamese diacritics: all correct, natural phrasing

---

## Issue 1: Missing concept file (forward-reference)

**File:** `wiki/concepts/spacing-effect.md` (line 33)
**Severity:** ERROR
**Dimension:** Factual accuracy
**Issue:** Concept references `[[forgetting-curve]]` in Related concepts section, but `wiki/concepts/forgetting-curve.md` does not exist. This causes a broken wikilink in Obsidian.
**Evidence:**
```
## Related concepts
- [[forgetting-curve]]          ← file does not exist
- [[memory-consolidation-offline]]
```
**Suggested fix:** Either create `concepts/forgetting-curve.md` (recommended — it's a well-known Ebbinghaus concept directly relevant to spacing effect), or remove the wikilink.

---

## Issue 2-15: Forward-reference wikilinks — pre-existing concepts missing backlinks to new sources

**Files affected:** 7 new concepts referencing 14 pre-existing concepts
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** New concepts reference 14 pre-existing concepts that do not have reciprocal backlinks to the new source files. This is a systemic consequence of the Compile Agent's one-directional workflow — pre-existing concepts are not re-opened when new sources arrive.

**Representative examples (3 of 14):**

| New concept | References | Pre-existing concept | Missing backlink to |
|---|---|---|---|
| `show-me-era.md` | `[[tokenization]]` | `tokenization.md` | `src_the-new-comms-playbook-show-dont` |
| `fluency-illusion.md` | `[[cognitive-load-theory]]` | `cognitive-load-theory.md` | `src_giai-thich-sau-phuong-phap-hoc-charlie-munger` |
| `chauffeur-knowledge.md` | `[[circle-of-competence]]` | `circle-of-competence.md` | `src_giai-thich-sau-phuong-phap-hoc-charlie-munger` |

**Full list of pre-existing concepts needing backlink updates:**
`tokenization`, `compounding-effect`, `mental-models`, `category-kings-dynamics`, `leading-indicators`, `positioning-before-price`, `narrative-certainty-trap`, `cognitive-load-theory`, `meta-learning`, `deliberate-practice`, `feedback-loop`, `memory-consolidation-offline`, `tacit-knowledge`, `circle-of-competence`

**Suggested fix:** Fix Agent should add the respective source backlinks to each pre-existing concept's `## Sources` section. A batch operation: for each (concept, source) pair above, append to the concept's frontmatter `sources:` list and `## Sources` section.

---

## Issue 16: Single-sentence definitions (all 7 new concepts)

**Files:** All 7 new concepts (`show-me-era`, `proof-stack`, `two-track-communications`, `fluency-illusion`, `retrieval-practice`, `spacing-effect`, `chauffeur-knowledge`)
**Severity:** INFO
**Dimension:** Completeness
**Issue:** The format spec recommends 2-3 sentence definitions. All 7 new concepts have single-sentence definitions — though each sentence is substantial (compound, multi-clause, conveying full semantic meaning). This is a known Compile Agent output style (compact paragraphs as single sentences with semicolons and colons).
**Evidence:** All definitions are long compound sentences with semicolons/colons — e.g., proof-stack definition is 55 words in one sentence.
**Evaluation:** These are NOT inadequate — they convey complete meaning. Pattern is systemic (quick-scan reports 420 concepts with 1-sentence definitions). Recommend reviewing the Compile Agent prompt to encourage 2-3 sentence definitions rather than one compound sentence, but do not block these files for this alone.
**Suggested fix:** Low priority. If Fix Agent is touching these files for other reasons, split definitions into 2-3 simpler sentences. Otherwise, accept as-is.

---

## Systemic patterns (INFO — carry-over, không phải issues mới)

The quick-scan identified the following systemic patterns across the entire wiki — these are NOT new issues introduced today:

| Pattern | Count | Notes |
|---|---|---|
| 1-sentence definitions | 420 concepts | Compile Agent style: one compound sentence instead of 2-3 simple ones |
| Too few key points (<5) | 78 concepts | Most have 3-4 key ideas vs 5-10 spec |
| Empty Key ideas | 9 concepts | Needs re-compilation |
| Draft concepts | 252 | Normal — review pipeline backlog |
| "người" spacing merge | 4 files / 11 instances | All in pre-existing files (new: 0) |

---

## Actions

1. **[P1 — Fix Agent]** Create `wiki/concepts/forgetting-curve.md` or remove the broken wikilink from `spacing-effect.md`
2. **[P2 — Fix Agent]** Add source backlinks to 14 pre-existing concepts (see Issue 2-15 table)
3. **[P3 — Compile Agent review]** Single-sentence definition style — review prompt to encourage 2-3 simple sentences instead of one compound sentence
