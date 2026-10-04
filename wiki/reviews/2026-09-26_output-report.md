# Output Validation — 2026-09-26
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 4 (1 ERROR, 3 WARNING, 0 INFO)
**Created:** 2026-09-26 23:12:57 +0700
**Validator:** output-validator
**Files checked:** 817 (212 sources + 605 concepts)
**New files:** 6 (1 source + 5 concepts) — batch "do-less" (Finlay, X 2026-09-24)

---

## Issue 1: Study misattribution — "time alone" experiment credited to Baird et al. 2012

**File:** `wiki/concepts/creative-incubation.md` (lines 20, 36) + `wiki/sources/src_do-less.md` (line 31)
**Severity:** ERROR
**Dimension:** Factual
**Issue:** The "people don't enjoy sitting alone 6–15 minutes with nothing to do" finding is attributed to Baird et al. (2012) in three places. That experiment is Wilson et al., "Just think: the challenges of the disengaged mind," *Science* 345(6192):75-7, 2014 (11 studies, PMID 24994650 / PMCID PMC4330241). Baird et al. 2012 (UC Santa Barbara) is a *different* study — "Inspired by Distraction" — about undemanding tasks improving creative insight. The raw source (`raw/posts/2026-09-24_do-less.md` line 28) correctly links PMC4330241; the Compile Agent merged two distinct experiments and misattributed the 6–15 minute finding to Baird. `src_do-less.md:31` is also wrong: it labels the 6–15 minute "prefer mundane activities" result as "Thí nghiệm incubation (Baird et al. 2012)", when that result belongs to Wilson et al. 2014, and it omits the genuinely-Baird experiment that the raw post cites separately at line 38.

**Evidence:**
```
wiki/concepts/creative-incubation.md:36
- [[src_do-less]] — Baird et al. 2012 (UCSB), thí nghiệm "time alone" 6–15 phút, giả thuyết tắm/máy bay/giường

wiki/sources/src_do-less.md:31
- **Thí nghiệm incubation (Baird et al. 2012):** sau một nhiệm vụ nhẹ nhàng, người ta quay lại bài toán sáng tạo với *nhiều ý tưởng hơn* so với sau nhiệm vụ nặng nhọc hoặc sau khi không nghỉ.
```
Verified against the cited source: PMC4330241 = Wilson et al. 2014, *Science*, "In 11 studies, we found that participants typically did not enjoy spending 6 to 15 minutes in a room by themselves with nothing to do but think, that they enjoyed doing mundane external activities much more…" The raw post links PMC4330241 for the 6–15 minute result (line 28) and a separate UCSB/Baird PDF for the incubation result (line 38) — the compile conflated them.

**Suggested fix:** In all three locations, attribute the 6–15 minute "prefer mundane activities / electric shock" finding to Wilson et al. 2014 (*Science*, PMCID PMC4330241), and keep Baird et al. 2012 (UCSB) only for the undemanding-task → more-creative-ideas result. `src_do-less.md` should carry **two** distinct key points (Baird 2012 incubation, Wilson 2014 time-alone), not one merged bullet. `creative-incubation.md:36` annotation should cite both. The two claims propagate to `boredom-as-dopamine-reset.md:28` and `busywork-vs-deep-work.md` (Key ideas) — check that "thí nghiệm cho thấy người ta không thích ngồi yên 6–15 phút" carries no Baird attribution after the fix.

---

## Issue 2: Mid-list blank lines split Key ideas into disconnected fragments

**File:** `wiki/concepts/busywork-vs-deep-work.md` (line 30), `wiki/concepts/one-thing-daily-priority.md` (line 28)
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** A blank line between two `- ` bullets breaks the Key ideas list into two separate markdown lists. In `busywork-vs-deep-work.md` the blank splits two content groups (the aggregated-source insights vs. the src_do-less insights); in `one-thing-daily-priority.md` it separates the Dickie Bush "ONE THING" rules from the Finlay "3 things" counterpoints. Visually they read as distinct lists with no signal that they belong together, and the split happens exactly at the source boundary — which reads as an unfinished paste rather than a deliberate grouping. This is a **new** defect: KB-wide scan of all 605 concepts + 212 sources found exactly **3** files with a mid-list blank split — 2 of them in today's batch, 1 carry-over (`meaning-through-work.md`, last_updated 2026-06-22, 6 occurrences). No other file in the KB has this shape, so it is not an established convention.

**Evidence:**
```
wiki/concepts/one-thing-daily-priority.md:27-29
- **Momentum compounding:** thắng 1 ngày nuôi thắng ngày kế tiếp ("momentum of one day feeds the next")
                                                          ← blank line
- **Ba thay vì một:** Finlay chọn **3 việc/ngày** từ sổ tuần (không phải 1 việc duy nhất như Dickie Bush…)
```
**Suggested fix:** Remove the blank line at `busywork-vs-deep-work.md:30` and `one-thing-daily-priority.md:28` so each Key ideas section is one continuous list. If the source-boundary grouping is intentional and worth keeping, signal it explicitly instead (e.g. a `**Từ src_do-less:**` sub-heading) rather than a bare blank line. `meaning-through-work.md` (6 occurrences) is carry-over — same fix, separate approval.

---

## Issue 3: Untranslated English term in Definition — "progress"

**File:** `wiki/concepts/busywork-vs-deep-work.md` (line 18)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** The Definition opens in Vietnamese and glosses the first technical term ("Busywork (công việc giả năng suất)") but then leaves "progress" untranslated mid-sentence: "…tạo ra ít hoặc không có **progress** thực sự". KB has both patterns in use but Vietnamese is dominant for common nouns: `tiến bộ` 18 occurrences vs `progress` 34 KB-wide, and in this same file line 23 already writes "zero progress" as an intentional English phrase inside a bolded lead-in, so the Definition is the inconsistent one. The term is not a technical term that needs preservation — it is ordinary vocabulary.

**Evidence:**
```
wiki/concepts/busywork-vs-deep-work.md:18
Busywork (công việc giả năng suất) là những hoạt động tiêu tốn nhiều thời gian và nỗ lực nhưng tạo ra ít hoặc không có progress thực sự — chiếm 80% nỗ lực nhưng chỉ tạo 20% kết quả.
```
**Suggested fix:** "…tạo ra ít hoặc không có tiến bộ thực sự". Line 23's "high effort, zero progress" is inside an English-led bullet and reads intentionally — leave it, or change both together if the file is being edited anyway.

---

## Issue 4: Source annotation in `## Sources` carries a PMC ID not present in the compiled source

**File:** `wiki/concepts/stress-habituation.md` (line 36)
**Severity:** INFO
**Dimension:** Factual
**Issue:** The Sources bullet annotates `[[src_do-less]]` with "stress habituation (PMC9797525) + allostatic load, khám bác sĩ giấc ngủ phát hiện gốc rễ stress". The PMC ID is accurate — PMC9797525 is indeed the soldiers/deployment stress-habituation study, and the raw post links it — but the ID appears **nowhere** in `src_do-less.md`, so the concept cites a source identifier the source file itself does not carry. A reader following the backlink cannot verify the study from the wiki. This is the only concept in the KB whose body contains a PMC ID (1/605), so it is not an established annotation convention either way.

**Evidence:**
```
wiki/concepts/stress-habituation.md:36
- [[src_do-less]] — stress habituation (PMC9797525) + allostatic load, khám bác sĩ giấc ngủ phát hiện gốc rễ stress
```
`grep -c 'PMC' wiki/sources/src_do-less.md` → 0. The raw post (`raw/posts/2026-09-24_do-less.md:26`) links both PMC9797525 (habituation) and PubMed 10681886 (allostatic load, McEwen 1998) — neither ID reached the compiled source.

**Suggested fix:** Either add the two study links to the `## Key points` bullets in `src_do-less.md` where the claims are made (line 30 covers both concepts and currently has no citation), or drop the PMC ID from the concept's Sources annotation. Prefer the former: the concept makes a research-backed claim and the source should carry the citation.

---

## Checks performed — all PASS

**Typo variants (all 5 Compile Agent tokenization defects): 0 instances**
- `ngưởi` hook-above: 0 files
- `ngườii/đờii/lờii` double-i: 0 files, 0 instances
- `người` spacing merge: 0 files, 0 instances
- `ngườI` / `[vowel+diacritic]I` capital-I: 0 files, 0 instances
- **Variant 5 dropped-i (mandatory manual grep, all 4 sub-patterns): 0 matches.** Clean streak spans 08-23 → 09-26 — **20 run-days with output reports**, every logged grep 0. (Historical streak *labels* drifted non-monotonically: 09-18 logged "16 consecutive", 09-25 logged "15" — the count was never reliably derived from report files. Counted from report files today: 19 prior run-days 08-23→09-25 + today = 20. Use the date range, not the number.)

**CJK contamination: 0 in today's batch.** All 6 new files clean.

KB-wide carry-over inventory (recounted 2026-09-27, superseding the figures in the original 09-26 entry — see Corrections section): **14 CJK-bearing lines / 33 CJK chars across 12 content files** (10 concepts + 2 sources) in `wiki/sources/` + `wiki/concepts/`. Separately, 60 CJK-bearing lines across 10 report files in `wiki/reviews/` — legitimate, since reports quote the Chinese strings they flag.

Legitimate Chinese content (do not fix) — **3 files**:
- `byte-level-bpe.md:26` — 中 (Chinese script byte count)
- `chinese-culture-confucianism.md:22` — 国家 (gloss for "quốc gia")
- `hundred-years-humiliation.md:16` — 百年国耻 (the standard Chinese name of the Century of Humiliation; the concept is explicitly about this term)

**Unremediated Compile Agent injections: 9 files** (7 concepts + 2 sources), 11 lines — batches **09-18 → 09-21**:
- 09-18: `src_50-system-design-concepts-explained-simply.md:24` (trade-off在哪里), `src_how-ai-labs-eventually-make-money.md:24` (builder几乎), `ai-lab-business-model.md:16` (companies面临)
- 09-20: `ai-chip-design.md:22,24` (颠覆, 密度), `financial-discipline.md:21,23` (浪费, 看起来), `life-planning-20s.md:17` (巨大)
- 09-21: `amygdala-vs-prefrontal-cortex.md:24` (沙发), `consumption-vs-action.md:25` (一年), `low-entry-principle.md:21` (让它阻止)

**Correction to the original 09-26 claim:** this report originally stated "73 CJK-bearing lines across 12 content files (8 concepts + 2 sources)" and dated the streak from 09-12. Both were wrong:
1. Content files carry **14** CJK-bearing lines (33 chars), not 73. The figure 73/74 corresponds to CJK lines across the whole `wiki/` tree including `wiki/reviews/` (60) — content and report files were conflated.
2. The streak does **not** start 09-12. The 09-12 CJK finding (`既是` in `src_harness-engineering-ai-coding.md` + `harness-engineering.md`) has been **resolved** — both files now return 0 CJK matches. The unremediated streak starts **09-18** and spans 3 flagged batches, surviving 6 validator runs (09-18, 09-20, 09-21, 09-24, 09-25, 09-26).
3. The original "8 concepts + 2 sources" miscounted the split — the real unremediated set is **7 concepts + 2 sources**, because `hundred-years-humiliation.md` is legitimate Chinese content (it was counted as an injection in the original entry).

**Structural integrity: 0 violations**
- Truncated concepts (missing sections): 0
- Truncated sources (missing Concepts referenced): 0
- Empty Key ideas: 0 · Empty Sources: 0
- `src_do-less.md` uses `## Key points` (correct for sources — no Defect C section-name drift)

**Multi-source invariants (Defect A/B/C) — all pass on the 3 multi-source concepts**
| Concept | Frontmatter sources | Body `## Sources` | Verdict |
|---|---|---|---|
| `boredom-as-dopamine-reset` | 2 | 2 | pass |
| `busywork-vs-deep-work` | 3 | 3 | pass |
| `one-thing-daily-priority` | 2 | 2 | pass |

- Defect A (backlink gap): none
- Defect B (duplicate key idea): none found on full read
- Defect C (section-name drift): none

**Completeness: all 6 new files meet depth thresholds**
- Definitions: 2–3 sentences each (2 concepts at exactly 2, 3 at 3) — all ≥2 ✅
- Key ideas / Key points: 6, 6, 9, 9, 12 concepts + 10 source points — all ≥5 ✅
- Summary: 4 sentences (KB norm 4–6) ✅

**Backlinks: 22/22 resolve.** All 4 source links, all 13 related-concept targets, all 5 `Concepts referenced` entries verified to exist. Zero broken, zero forward-references. `original:` → `raw/posts/2026-09-24_do-less.md` exists with `compiled_to: "[[src_do-less]]"` correctly set. Topic indexes regenerated by Index Agent — all 6 new files present in their 4 topic pages.

**Vietnamese quality:** Grammar and phrasing correct throughout. 8 English-bolded lead-ins in Key ideas (a deliberate, readable pattern). One questionable idiom at `one-thing-daily-priority.md:22` — `não đang "ngứa" muốn ghi ra` — the raw source says "I'm itching to write down the ideas"; `ngứa` (a horse's mane, not a verb) reads as a machine-translation artifact of "itching". Only occurrence of `ngứa` in the KB. Fold into the Issue 3 fix pass — low severity, no separate issue.

---

## Recommendations

1. **Fix Agent (blocking on Issue 1):** correct the Wilson et al. 2014 / Baird et al. 2012 split in 3 locations. This is a factual error that will propagate to every future concept compiled from `src_do-less`.
2. **Compile Agent prompt:** Issue 1 is a **study-attribution merge** — a new defect class, not one of the 5 known tokenization variants. The compile step collapsed two separately-linked experiments in the raw post into one mislabeled bullet. Add an instruction to keep one key point per distinct cited study and carry the citation identifier through to the compiled source.
3. **Fix Agent (non-blocking):** Issues 2 and 3 — two blank lines and one untranslated word. Batch them with any future fix pass.
4. **Julius decision:** the unremediated CJK injections are now **9 files / 11 lines** spanning batches **09-18 → 09-21**, surviving 6 validator runs without action. Either approve a CJK cleanup pass or accept them as a standing baseline. This has been re-escalated in each report since 09-18 without action. (Scope corrected 2026-09-27: the earlier "10 injections from 09-12→09-21" figure was wrong on both count and start date — see Corrections.)

---

## Corrections (2026-09-27, 23:00 validation run)

No new files were compiled on 2026-09-27, so this run produced no new issues. It did, however, audit the 09-26 report's carry-over claims and found **one of them factually wrong**. Corrected in place above; the corrections are recorded here so the change is auditable.

**Wrong claim:** *"KB-wide carry-over inventory: 73 CJK-bearing lines across 12 content files (8 concepts + 2 sources) + 9 report files… Remaining 10 are unremediated Compile Agent injections from 09-12→09-21 batches."*

**Verified replacement:**
| Figure | Claimed 09-26 | Verified 09-27 | Basis |
|---|---|---|---|
| CJK-bearing lines in content | 73 | **14** (33 chars) | `grep -rP '[\x{4e00}-\x{9fff}]' wiki/sources/ wiki/concepts/ \| wc -l` |
| CJK-bearing lines in reports | 9 files | **10 files / 60 lines** | same grep scoped to `wiki/reviews/` |
| Total across `wiki/` | (implied 73) | **74** | content 14 + reviews 60 |
| Unremediated injections | 10 files, 09-12 start | **9 files / 11 lines, 09-18 start** | per-file CJK grep + `date_compiled`/`last_updated` |

**Root cause of the error:** the 73/74 figure was taken across the whole `wiki/` tree, which folds `wiki/reviews/` into a number labelled "content files". The two populations are semantically different — reports legitimately quote the Chinese strings they flag, so counting them as contamination inflates the backlog roughly 5×. The start date was wrong in the other direction: the 09-12 CJK finding had in fact been fixed, and the report kept carrying it forward as unresolved.

**Note on `hundred-years-humiliation.md`:** the original entry listed 2 legitimate-Chinese files; there are **3**. `百年国耻` (Century of Humiliation) is the standard Chinese term and the concept is explicitly about that term — not an injection. It was miscounted as part of the injection backlog, which is why the concept-side split read 8 instead of 7.

**Carried forward unchanged:** Issue 1 (Baird/Wilson misattribution), Issue 2 (mid-list blank lines), Issue 3 (untranslated "progress"), Issue 4 (PMC ID not in source) — all re-verified present on disk today, none fixed since 09-26.

---

## Previous run context

**2026-09-25 (18:14):** 814 files, 0 new files, 0 issues, [SILENT]. Quick-scan clean, dropped-i streak 15. Nothing from that run overlaps with today's batch.

**2026-09-24 (08:50):** 6 files touched, 2 issues — 1 ERROR (`multi-agent-risk-review.md` Definition 1 câu), 1 WARNING (`ai-trading-agent.md` lặp `mua/bán/bán`). Still pending, unfixed. Also carries forward 3 CJK chars + 1 tokenization merge from 09-21.
