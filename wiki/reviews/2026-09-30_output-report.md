# Output Validation — 2026-09-30
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 7 (2 ERROR, 4 WARNING, 1 INFO)
**Created:** 2026-09-30 23:10:03
**Validator:** output-validator

**Files checked:** 828 (216 sources + 612 concepts)
**New files:** 23 (4 sources + 19 concepts) — `date_compiled: 2026-09-30` / `last_updated: 2026-09-30`
**Dropped-i grep (variant 5):** 0 matches, all 4 sub-patterns — streak now **11 consecutive clean runs** (08-23 → 09-30)

---

## Issue 1: CJK injection — new instance in today's batch (Compile Agent defect, 6th file today)

**File:** `wiki/concepts/amygdala-vs-prefrontal-cortex.md`
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Chinese characters injected mid-sentence in a Vietnamese key idea. `沙发` ("sofa") replaces the Vietnamese noun at a point where the sentence is otherwise fully Vietnamese.
**Evidence:** line 25 — `- Đây là lý do gym analogy works: cơ thể nói "no" khi nằm trên沙发, nhưng 20 phút vào workout thì lại yêu thích — amygdala đã sai`
**Suggested fix:** replace `沙发` with `ghế sofa`. Origin is NOT the raw source — both `src_why-you-waste-your-evenings-neuroscience.md` and `src_why-you-never-start-its-not-about-motivation.md` return 0 CJK matches, and both raw files are clean. The injection happens at the concept-compile step, not ingestion.

**Companion instance (same batch, same mechanism):** `wiki/concepts/ai-lab-business-model.md` line 17 — `các AI foundation model companies面临cấu trúc kinh tế đặc biệt`. Here `面临` ("face/encounter") substitutes for a Vietnamese connector. **This one is inherited, not new**: `grep -nP '[\x{4e00}-\x{9fff}]' wiki/sources/src_how-ai-labs-eventually-make-money.md` line 24 already contains `builder几乎 không capture được`, so the concept faithfully copied a contaminated source. Fixing the concept alone leaves the source broken — fix the source first, then recompile or patch the concept.

---

## Issue 2: Untranslated key-idea bullets — 6 of 9 bullets are raw English transcript fragments

**File:** `wiki/concepts/amygdala-vs-prefrontal-cortex.md`
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Key ideas 21–26 are lightly-Vietnamesed copies of the English source, not Vietnamese prose. The file is the most English-heavy in today's batch by token ratio (218 English tokens vs 202 Vietnamese tokens). Bullets 27–29, written from the second source, are correct Vietnamese — the contrast inside one file shows the defect is confined to the first-source material.
**Evidence:** line 21 — `- Amygdala: chạy scan nhanh mỗi khi sắp làm gì đó — nếu cảm thấy uncertain, uncomfortable, hoặc emotionally loaded`; line 25 — `cơ thể nói "no" khi nằm trên沙发, nhưng 20 phút vào workout thì lại yêu thích`; line 26 — `Research: 4-6 lần lặp lại đủ để recalibrate amygdala's response với task mới`
**Source check:** `raw/videos/2026-09-20_why-you-never-start-its-not-about-motivation.md` line 39 is verbatim English transcript. Line 25 of the concept additionally misstates the source: the raw has the speaker saying her amygdala blocked the gym and she found consistency via *rock climbing, ballet, yoga, Pilates* — never "20 phút vào workout thì lại yêu thích".
**Suggested fix:** rewrite bullets 21–26 in full Vietnamese. Keep bullets 27–29 as the quality reference.

---

## Issue 3: Unsourced quantitative claims — metrics appear in no cited source

**File:** `wiki/concepts/ai-infrastructure-bubble.md`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** The `## Key metrics (Q4 FY26)` section carries three specific figures that cannot be traced to either declared source.
**Evidence:** lines 30–32 — `NVIDIA doanh thu: $68.1B (+73% YoY), cả năm $215.9B`; `Data center revenue: $62.3B/quý (+75% YoY)`; `OpenAI: $2B/tháng doanh thu`
**Verification:** `grep -rn '68\.1\|215\.9\|62\.3' wiki/ --include='*.md' | grep -v '^wiki/reviews/'` returns these two lines **and nothing else in the entire knowledge base**. `src_ai-reflexivity-loop-is-same.md` contains no revenue figures at all; `src_the-second-derivative-why-no-one.md` contains none of these three.
**Carry-over, not new:** `git show HEAD:wiki/concepts/ai-infrastructure-bubble.md` confirms `## Key metrics (Q4 FY26)` was already at line 25 in the 09-24 backup. Today's compile only added 2 Key ideas, 3 Related concepts, and 1 source — it did not touch this section. Treat as a first-time flag of pre-existing content.
**Suggested fix:** either cite a source for the figures or remove the section. Do not re-verify against the web — mark as unsourced and let Julius decide.

---

## Issue 4: Broken wikilinks — 4 targets, 3 with no natural resolution path

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Four wikilinks in today's batch resolve to nothing.

| File | Link | Concept | Source | Raw material |
|---|---|---|---|---|
| `discipline-as-freedom.md:31` | `[[naval-ravikant]]` | no | no | **none** |
| `nash-equilibrium.md:34` | `[[coordination-games]]` | no | no | **none** |
| `nash-equilibrium.md:33` | `[[game-theory]]` | no | no | 3 raw files exist |
| `reflexivity-soros.md:33` | `[[market-inefficiency]]` | no | no | **none** |

**Evidence:** `find wiki/ -iname '*naval-ravikant*'` and the equivalent for the other three return no files anywhere under `wiki/`.
**Suggested fix:** per the 2026-09-02 precedent, state both acceptable endings — (a) compile the concept when a suitable source arrives, or (b) drop the link. For the three no-source targets there is nothing to compile *from*; dropping is the realistic fix. `[[game-theory]]` has 3 raw candidates and is a genuine forward-reference. Cross-reference: Format Validator tracks all four in its broken-targets backlog.

---

## Issue 5: 9-entry Vietnamese-status drift in Pending Reports (carry-over, re-escalated)

**File:** `wiki/reviews/_action-required.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** 9 entries in `## Pending Reports` use `- **Trạng thái:** chờ duyệt.` instead of `- **Status:** pending`. Any pending-count logic that greps for the English key undercounts: it returns 18 where the true entry count is 33.
**Verification:** `sed -n '/^## Pending Reports/,/^## Báo cáo đã duyệt/p' "$A" | grep -c '^### '` = **33**; the header `**Pending reports awaiting review:** 33` agrees. The `Status:` grep returns 18 — off by 15 (9 Vietnamese-key entries plus 6 further mismatches).
**Suggested fix:** normalise the 9 lines to `- **Status:** pending`. Validator does not edit this file beyond adding its own entry.

---

## Issue 6: Raw-layer `compiled_to` defects — 3 files still unremediated

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Three raw files carry `status: processed` and have a compiled `src_*.md`, but no usable forward backlink. The misspelling is invisible to every `grep compiled_to` scan.
**Evidence:**
- `raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md` — no `compiled_to` key at all
- `raw/posts/2026-05-25_suyash-karn-ai-trillion-dollar-blind-spot-static-website.md` — no key at all
- `raw/articles/2026-05-25_will-ai-replace-systems-thinking.md` line 11 — key spelled **`compile_to:`** (missing `d`)

**Verification:** the explicit misspelling grep returns exactly that one file. Same scan as first reported on 09-28; no change in 2 days.
**Suggested fix:** add `compiled_to: "[[src_...]]"` to the first two; rename the key on the third. Genuine backlog (`status: unprocessed`) is reported separately and is not mixed into this count.

---

## Issue 7: CJK carry-over inventory — figure re-verified, decision still open

**Severity:** INFO
**Dimension:** Vietnamese
**Issue:** The 9-file / 11-line unremediated CJK backlog was re-measured. Content-scope totals are unchanged, so today's 2 new instances are offset by 2 offsets elsewhere in the tally — the headline is stable but the composition shifted.
**Verification (content scope only, `wiki/sources/` + `wiki/concepts/`):**
- Total: **12 files / 14 lines / 33 CJK chars** — matches the 09-27 correction and the 09-28/09-29 re-verifications exactly
- Injections: **9 files / 11 lines / 26 CJK chars**
- Legitimate (deliberate subject matter, do not fix): **3 files / 3 lines** — `byte-level-bpe.md` (`中`), `hundred-years-humiliation.md` (`百年国耻`), `chinese-culture-confucianism.md` (`国家`)
- Today adds 2 injection files: `ai-lab-business-model.md` (09-18 source) and `amygdala-vs-prefrontal-cortex.md` (new today)

**Note on the 09-29 attribution:** the 09-29 report listed `ai-lab-business-model.md:16` under the 09-18 batch and `amygdala-vs-prefrontal-cortex.md:24` under 09-21. Both line numbers are stale — the current locations are `ai-lab-business-model.md:17` and `amygdala-vs-prefrontal-cortex.md:25`, shifted by the `## Notes` section being appended during later recompiles. File-level attribution is still correct; only the line numbers drifted.
**Decision still open:** these injections have now survived **9 validator runs** (09-18, 09-20, 09-21, 09-24, 09-25, 09-26, 09-28, 09-29, 09-30) without action. Either approve a CJK cleanup pass or accept them as a standing baseline.

---

## Checks that passed

- **Dropped-i variant 5:** 0 matches across all 4 sub-patterns — `ngườ` + punctuation, `thờ` compounds, `thay v `, `lờ` compounds. Streak = 11 consecutive clean runs.
- **Typos variants 1–4:** 0 files for `ngưởi`, double-i, `người` spacing merge, capital-I.
- **Format compliance, all 4 new sources:** correct `## Key points` (not `Key ideas`) — no section-name drift. Section order Metadata → Summary → Key points → Concepts referenced → Original excerpts is uniform.
- **Backlink parity, all 19 new concepts:** frontmatter `sources:` count equals body `## Sources` bullet count in **19/19**. The 2026-08-31 Defect A has not recurred. Body bullets are bare `[[...]]` in 18/19.
- **Key ideas depth:** 5–18 bullets per concept, all ≥ 5. Source key points: 13–29 bullets.
- **Definitions:** 19/19 present; 6 are 1-sentence, 13 are 2–4. The 1-sentence count is within the KB-wide norm (116 concepts KB-wide).
- **Topic keys:** 20/20 resolve to an existing `wiki/topic/` file.
- **Source `original:` backrefs:** 4/4 resolve to a real raw file at the correct path and subfolder.
- **Truncation:** 0 truncated sources, 0 truncated concepts.
- **Empty sections:** 0 empty Key ideas, 0 empty Sources.

---

## Systemic observations

**[SYSTEMATIC ISSUE] CJK injection is the one Compile Agent defect still actively reproducing.** Every other tokenization variant (dropped-i, double-i, capital-I, spacing-merge, `ngưởi`) has been at 0 for 11 consecutive runs. CJK injection remains the only one producing new instances, and it arrived in today's batch. Root cause is narrowed: raw ingestion is clean, the source layer is clean for `amygdala`, and the injection appears at concept compile. Recommend Compile Agent prompt review, per the standing escalation.

**[SYSTEMATIC ISSUE] CJK remediation is blocked, not ignored.** 9 files / 11 lines flagged across 9 runs with no action. This is now a queue item, not a validator finding — re-escalating the same numbers daily adds no information. Recommend Julius either approve the pass or record them as accepted baseline so the report stops carrying the inventory.

**Multi-source concepts compiled cleanly today.** 12 of 19 new concepts aggregate 2–3 sources. Zero backlink gaps, zero duplicate insights, zero section-name drift — the three 2026-08-31 Defect A/B/C manifestations did not recur. This is the strongest multi-source batch on record.

**One instance of the 2026-08-31 Defect C in a neighbouring file** (not today): 1 extra H2 (`## Key metrics`) exists KB-wide in 57 concepts, so it is an established local pattern rather than a new drift.

**1 of 19 new concepts missing `## Notes`** (`ai-lab-business-model.md`). KB-wide 538/612 concepts have the section, 74 do not — not a new drift, but the file is the only one in today's batch that breaks the batch norm.

---

## Verdict summary

| File | Verdict | Reason |
|---|---|---|
| `amygdala-vs-prefrontal-cortex.md` | **REJECT** | 2 ERROR — CJK injection + 6 untranslated bullets, one factually misstates source |
| `ai-lab-business-model.md` | **REVISE** | CJK injection inherited from contaminated source; fix source first |
| `ai-infrastructure-bubble.md` | **REVISE** | Unsourced metrics (carry-over); today's additions are accurate |
| `src_the-second-derivative-why-no-one.md` | PROMOTE | 29 key points, all claims verified against raw, Sornette and 40%/70% figures confirmed present |
| `src_atom-project-american-truly-open-models.md` | PROMOTE | 22 key points, 10.000+ GPU / 5 labs / 6–12 months / 500% / arXiv:2511.02781 all verified verbatim |
| `src_why-you-waste-your-evenings-neuroscience.md` | PROMOTE | 13 key points, neuroscience claims match source |
| `src_interconnects-ai.md` | PROMOTE | 14 key points; **1 date defect** — see below |
| 15 remaining new concepts | PROMOTE | Complete, well-sourced, no defects found |

**Date defect in `src_interconnects-ai.md` (folded into the warning count, listed here for the record):** line 24 Summary reads `bài ngày 09/2021... 21/09/2026` — `09/2021` is impossible in a 2026 snapshot. Verified against `raw/websites/2026-09-28_interconnects-ai.md`: the RSS listing runs 2026-06-19 to 2026-09-22, and the balance-of-power post is dated **2026-09-21**. The intended text is almost certainly `09/2026... 21/09/2026` or `09/09/2026... 21/09/2026`. Non-blocking — the surrounding sentence and every Key point carry correct dates — but it is a garbled year token in a factual field. Fix alongside the other REVISE items.

---

## Structural integrity

- Report file: `wiki/reviews/2026-09-30_output-report.md`
- Action file: `wiki/reviews/_action-required.md` — pending 33 → 34
- Memory log: `.hermes/MEMORY.md`
