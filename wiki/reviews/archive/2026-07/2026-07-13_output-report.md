# Output Validator Report — 2026-07-13

**Status: applied
**Approved by:** Julius
**Issues found:** 5 (1 ERROR, 2 WARNING, 2 INFO)
**Created:** 2026-07-13 23:08:54
**Validator:** output-validator

---

## Summary

- **Files checked:** 570 (143 sources + 427 concepts)
- **New files validated (deep):** 10 (3 sources + 7 concepts) — all compiled 2026-07-13
- **Previous validation:** 2026-07-12 (pending, not yet approved)
- **07-13 batch:** Two thematic clusters — investment psychology (1 source + 2 concepts) and self-improvement/productivity (2 sources + 5 concepts, spanning arcade tokens and deliberate practice topics)

**Quick-scan results (all files):**
| Check | Result |
|---|---|
| "ngưởi" typo | 0 (unchanged) |
| "ngườii/đờii" double-i | 0 (unchanged) |
| "người" spacing merge | 4 files / 11 instances (all pre-existing, new: 0) |
| 1-sentence definitions | 425 concepts (up from 420 on 07-12) |
| Too few key points (<5) | 78 concepts |
| Empty Key ideas | 9 |
| Truncated concepts | 0 |
| Truncated sources | 0 |
| Draft concepts | 257 |

---

## New file deep validation

| File | Definition | Key ideas | Sections | Typos | Verdict |
|---|---|---|---|---|---|
| `src_an-all-too-common-investment-story.md` | N/A (source) | 8 | Complete | None | PROMOTE |
| `src_the-art-of-being-overlooked-stay-silent.md` | N/A (source) | 10 | Complete | None | PROMOTE |
| `src_the-most-underrated-token-type.md` | N/A (source) | 10 | Complete | None | PROMOTE |
| `concepts/arcade-tokens.md` | 2 câu | 10 | Complete | None | PROMOTE |
| `concepts/deliberate-practice.md` | 2 câu | 9 | Complete | None | PROMOTE (see Issue 3) |
| `concepts/goal-announcement-trap.md` | 2 câu | 8 | Complete | None | PROMOTE |
| `concepts/intrinsic-motivation.md` | 2 câu | 9 | Complete | None | PROMOTE |
| `concepts/investment-conviction.md` | 2 câu | 6 | Complete | None | PROMOTE |
| `concepts/outsourced-thinking.md` | 2 câu | 8 | Complete | None | PROMOTE |
| `concepts/token-economic-mechanics.md` | 2 câu | 10 | Complete | None | PROMOTE |

**All 10 new files have complete sections, no truncation, clean Vietnamese (except Issue 3).** The quick-scan mechanical checks pass for all 10.

---

## Issue 1: 3 missing wikilink targets (forward-reference, aggregated)

**File:** Multiple (see below)
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** 3 unique wikilink targets referenced by today's files do not exist in `wiki/concepts/`. Users navigating from these files will hit dead links.

**Affected targets and files:**

| Missing target | Referenced by (files) | Count |
|---|---|---|
| `delayed-gratification` | `src_the-art-of-being-overlooked-stay-silent.md`, `goal-announcement-trap.md`, `intrinsic-motivation.md` | 3 |
| `onchain-loyalty-programs` | `src_the-most-underrated-token-type.md`, `arcade-tokens.md`, `token-economic-mechanics.md` | 3 |
| `utility-tokens` | `arcade-tokens.md`, `token-economic-mechanics.md` | 2 |

**Evidence:** All three terms appear as `[[...]]` wikilinks in the Sources and Related concepts sections of the listed files. File system check confirms no corresponding `.md` files exist at `wiki/concepts/<slug>.md`.

**Suggested fix:**
- [P1] Compile Agent: Create `delayed-gratification.md`, `onchain-loyalty-programs.md`, `utility-tokens.md` from the source material that references them, OR
- [P2] Fix Agent: Remove these wikilinks from the referencing files until the concepts are compiled

**Note:** This is the same forward-reference pattern flagged in the 2026-07-12 format report (307 WARNINGs for broken wikilinks across the entire KB). Today's 3 new missing targets extend this systemic issue.

---

## Issue 2: 6 pre-existing concepts missing backlinks to new sources (systemic)

**File:** Multiple (see below)
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 6 pre-existing concepts are referenced by today's new sources but do not list those sources in their `## Sources` section. This creates one-directional links — the source points to the concept, but the concept doesn't point back.

**Affected concepts and missing source backlinks:**

| Concept | Missing backlink to |
|---|---|
| `persuasion-psychology` | `src_an-all-too-common-investment-story` |
| `circle-of-competence` | `src_an-all-too-common-investment-story` |
| `lazy-thinking` | `src_an-all-too-common-investment-story` |
| `first-principles-thinking` | `src_an-all-too-common-investment-story` |
| `discipline-as-freedom` | `src_the-art-of-being-overlooked-stay-silent` |
| `dopamine-reward-loop` | `src_the-art-of-being-overlooked-stay-silent` |

**Evidence:** `grep` for each new source filename in each concept's `## Sources` section returned 0 matches. All 6 concepts pre-date today's compilation.

**Suggested fix:** Fix Agent: Add the missing source references to each concept's `## Sources` section and frontmatter `sources:` list.

**Note:** This is the same systemic pattern as 2026-07-12 (14 pre-existing concepts missing backlinks). Today adds 6 more. Root cause: Compile Agent only updates newly created concepts with source backlinks — it does not retroactively update existing concepts when a new source references them.

---

## Issue 3: Excessive English-Vietnamese mixing in deliberate-practice.md

**File:** `wiki/concepts/deliberate-practice.md`
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** The file contains multiple full English sentences embedded in Vietnamese prose without clear demarcation (quotes, italics, or citation markers). While some technical term mixing is acceptable, full sentences in English within Vietnamese paragraphs break reading flow and language consistency.

**Evidence (from the file):**
- Line 21: `- Undirected effort does not produce expertise — cần deliberate practice với feedback và problem selection`
- Line 22: `- Efficiency never mattered in the grander scheme — direction mới là thứ quyết định`
- Line 24: `- Mastering the wrong problem is worse than failure — nó rút cạn năng lượng như thể bạn đang làm việc quan trọng`
- Line 25: `- Đối với entrepreneur: không cạnh tranh trong không gian bão hòa với platitudes. Chọn 5 giá trị bạn actively wage war against`
- Line 27: `- "A river cuts through rock not because of its power but its persistence" — James Watkins. Slow, boring, consistent reps thắng trong dài hạn`

**Suggested fix:** Either (a) translate the English sentences to Vietnamese while preserving the quoted source attribution where applicable, or (b) format the English phrases as explicit inline quotes with quotation marks and attribution. The James Watkins quote (line 27) is properly attributed — the other English fragments lack similar treatment.

---

## Issue 4: All 7 new concepts have single-sentence definitions (systemic, continuing)

**File:** All 7 new concepts: `arcade-tokens.md`, `deliberate-practice.md`, `goal-announcement-trap.md`, `intrinsic-motivation.md`, `investment-conviction.md`, `outsourced-thinking.md`, `token-economic-mechanics.md`
**Severity:** INFO
**Dimension:** Completeness
**Issue:** All 7 concepts compiled today have single-sentence definitions (2 câu minimum technically met, but often one long run-on sentence split by a period). The validator's requirement is 2-3 distinct, well-formed sentences that clearly define the concept. Today's batch continues the systemic pattern — now 425 concepts (up from 420 on 07-12) have this single-sentence style.

**Evidence:** All 7 definitions are 2 sentences, each structured as "X là Y. Chi tiết bổ sung." — the second sentence is typically an elaboration clause rather than a standalone definitional sentence.

**Note:** This is a systemic Compile Agent output style issue. The 07-12 report flagged this at 420 concepts. Today extends to 425. Root cause is in the Compile Agent prompt, not individual file quality.

---

## Issue 5: All 7 new concepts have empty Notes sections

**File:** All 7 new concepts
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Every concept compiled today has an empty `## Notes` section. While Notes is optional, having it present but empty in every file suggests the Compile Agent template includes it by default without populating it.

**Evidence:** All 7 files end with:
```
## Notes
```
With no content following. Total: 7 empty Notes sections.

**Note:** This is consistent with the broader pattern — most concepts in the KB have empty Notes sections (257 draft concepts, most with empty Notes). Not a regression, just a continued template artifact.

---

## Cross-reference consistency

| Metric | 07-12 | 07-13 | Delta |
|---|---|---|---|
| Missing wikilink targets | 1 (`forgetting-curve`) | 3 | +2 |
| Pre-existing concepts missing backlinks | 14 | 6 | -8 |
| Single-sentence definitions | 420 | 425 | +5 (7 new, minus 2 promoted) |
| "người" spacing merge | 4 files / 11 instances | 4 files / 11 instances | 0 (unchanged) |
| "ngườii" double-i | 0 | 0 | 0 |
| "ngưởi" typo | 0 | 0 | 0 |

---

## Action items

- [P1] **Fix Agent: Create 3 missing concepts** — `delayed-gratification.md`, `onchain-loyalty-programs.md`, `utility-tokens.md` — or remove their wikilinks from referencing files
- [P2] **Fix Agent: Add backlinks** — Add `src_an-all-too-common-investment-story` and `src_the-art-of-being-overlooked-stay-silent` to the Sources sections of the 6 pre-existing concepts listed in Issue 2
- [P3] **Fix Agent: Clean deliberate-practice.md** — Translate or properly attribute the 5 English sentence fragments in the Key ideas section
- [P4] **Review: Compile Agent definition style** — 425 concepts now have single-sentence definitions. This is a prompt-level issue, not individual fixes

---

## Previous approved run context

The 2026-07-12 report (pending, not yet approved) covered 10 files from the Charlie Munger learning method and crypto communications clusters. Its key findings:

- 1 ERROR: Missing `forgetting-curve` concept (still unresolved)
- 2 WARNING: 14 pre-existing concepts missing backlinks (6 of which overlap with today's new sources? No — the 07-12 sources were `src_the-new-comms-playbook-show-dont`, `src_giai-thich-sau-phuong-phap-hoc-charlie-munger`, `src_learn-anything-like-charlie-munger`. No overlap with today's 3 sources.)
- 1 INFO: Single-sentence definition pattern (continuing)
- Mechanical: All clean on typos, truncation, sections

The 07-11 run was silent (0 new files), so today's report covers a 2-day gap since the last report with actual findings.
