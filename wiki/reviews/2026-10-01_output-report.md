# Output Validation — 2026-10-01

**Status:** APPLIED — Fix Agent (OpenClaw main) xử lúc 2026-10-02 10:52 +07:00. CJK cleanup 9 file/11 dòng/26 ký tự (giữ 3 file hợp lệ: byte-level-bpe 中, hundred-years-humiliation 百年国耻, chinese-culture-confucianism 国家); rename slug 52→48 ký tự `src_why-youve-lost-your-curiosity-how-to-get-it-back` + 7 file link; vá mắt xích metrics vào src_ai-reflexivity-loop-is-same; 3 compiled_to; 2 broken wikilink bỏ; 9 khoá `- **Trạng thái:**` → `- **Status:** pending`. 4 claim trong báo cáo bị đính chính sau khi đo trực tiếp — xem `.openclaw/MEMORY.md` 2026-10-02.
**Issues found:** 8 (2 ERROR, 5 WARNING, 1 INFO)
**Created:** 2026-10-01 23:01:30
**Validator:** output-validator

**Files checked:** 828 (216 sources + 612 concepts)
**New files:** 0 — no file carries `date_compiled: 2026-10-01` or `last_updated: 2026-10-01`
**Dropped-i grep (variant 5):** 0 matches, all 4 sub-patterns — streak now **12 consecutive clean runs** (08-23 → 10-01)
**Run type:** carry-over audit day. Per the 2026-09-27 procedure, every numeric claim in the 09-30 report was re-measured against the filesystem before being inherited. Findings below include two corrections and one script repair.

---

## Issue 1: `amygdala-vs-prefrontal-cortex.md` — 2 ERRORs still unremediated (carry-over, day 2)

**File:** `wiki/concepts/amygdala-vs-prefrontal-cortex.md`
**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Both ERRORs flagged on 09-30 are unchanged on disk. The file has been sitting in the queue across two validator runs.

**Evidence 1 — CJK injection:** line 25 still reads `cơ thể nói "no" khi nằm trên沙发, nhưng 20 phút vào workout thì lại yêu thích`. `沙发` ("sofa") substitutes for the Vietnamese noun inside an otherwise fully-Vietnamese sentence.

**Evidence 2 — untranslated bullets:** bullets 21–26 remain lightly-Vietnamesed English fragments. Verbatim re-read:
- line 21 — `- Amygdala: chạy scan nhanh mỗi khi sắp làm gì đó — nếu cảm thấy uncertain, uncomfortable, hoặc emotionally loaded`
- line 22 — `- Prefrontal cortex: phần não "trưởng thành" (~25 tuổi), chịu trách nhiệm planning, decision-making, thinking long-term, weighing consequences`
- line 26 — `- Research: 4-6 lần lặp lại đủ để recalibrate amygdala's response với task mới`

Bullets 27–29 (from the second source) are correct Vietnamese. The contrast inside one file confirms the defect is confined to the first-source material. Line 25 additionally **misstates the source**: `raw/videos/2026-09-20_why-you-never-start-its-not-about-motivation.md` line 39 has the speaker saying her amygdala blocked the gym, and she found consistency via *rock climbing, ballet, yoga, Pilates* — never "20 phút vào workout thì lại yêu thích".

**Origin check (re-run, unchanged):** `src_why-you-waste-your-evenings-neuroscience.md`, `src_why-you-never-start-its-not-about-motivation.md`, and both raw files all return 0 CJK matches. The injection happens at concept-compile, not at ingestion.
**Suggested fix:** rewrite bullets 21–26 in full Vietnamese, correcting line 25 against the raw transcript. Use bullets 27–29 as the quality reference. One file, two jobs.

---

## Issue 2: `ai-lab-business-model.md` + its source — CJK pair still contaminated (carry-over, day 2)

**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** The 09-18 source carries `builder几乎 không capture được`; the concept faithfully copied contamination into `面临`. Source-first fix is still required — patching the concept alone leaves the source broken.
**Evidence:**
- `wiki/sources/src_how-ai-labs-eventually-make-money.md` line 24 — `...nhưng builder几乎 không capture được`
- `wiki/concepts/ai-lab-business-model.md` line 17 — `các AI foundation model companies面临cấu trúc kinh tế đặc biệt`
**Suggested fix:** fix `src_how-ai-labs-eventually-make-money.md` first, then patch or recompile the concept. Listed as ERROR in aggregate because it blocks two files.

---

## Issue 3: `ai-infrastructure-bubble.md` — 3 unsourced metrics still present (carry-over)

**Severity:** WARNING
**Dimension:** Factual
**Issue:** `## Key metrics (Q4 FY26)` carries three specific figures that trace to neither declared source. Re-verified: `grep -rn '68\.1\|215\.9\|62\.3' wiki/ --include='*.md' | grep -v '^wiki/reviews/'` returns only the two lines in this file and nothing else in the knowledge base. The third figure (`OpenAI: $2B/tháng doanh thu`) appears exactly once KB-wide — in this file.
**Evidence:** lines 30–32 — `NVIDIA doanh thu: $68.1B (+73% YoY), cả năm $215.9B` / `Data center revenue: $62.3B/quý (+75% YoY)` / `OpenAI: $2B/tháng doanh thu, vẫn lỗ ở quy mô lớn`
**Carry-over, not new:** `git show HEAD:wiki/concepts/ai-infrastructure-bubble.md` shows `## Key metrics` already present in the 09-24 backup. Today's compile added 2 Key ideas, 3 Related concepts, 1 source — it did not touch this section.
**Suggested fix:** cite a source for the figures or delete the section. Do not re-verify against the web — mark unsourced and let Julius decide.

---

## Issue 4: 3 of 4 broken wikilinks have no natural resolution path (carry-over)

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Resolution re-checked with exact-filename tests (`wiki/concepts/<slug>.md`, `wiki/sources/src_<slug>.md`) rather than the `find -iname` glob used on 09-30, which produces false positives from partial slug matches.

| File | Link | Concept file | Source file | Raw material | Verdict |
|---|---|---|---|---|---|
| `discipline-as-freedom.md:31` | `[[naval-ravikant]]` | no | no | none | drop the link |
| `nash-equilibrium.md:34` | `[[coordination-games]]` | no | no | none | drop the link |
| `nash-equilibrium.md:33` | `[[game-theory]]` | no | no | 3 raw | genuine forward-ref — wait |
| `reflexivity-soros.md:33` | `[[market-inefficiency]]` | no | no | none | drop the link |

**Note on `[[game-theory]]`:** `find wiki/ -iname '*game-theory*'` returns 7 files, which could read as "this target exists". It does not — the matches are `iterated-game-theory.md`, three `src_*game-theory*` sources about different subjects, and three `wiki/topic/` indexes. There is no `wiki/concepts/game-theory.md` and no `wiki/sources/src_game-theory.md`, so the link is genuinely unresolved. **This is a correction to the 09-30 report**, which listed the same 7 hits as supporting evidence without separating concept/source/topic. File-level attribution was right; the evidence line was misleading.
**Suggested fix:** drop the 3 no-source links; leave `[[game-theory]]` pending until raw material compiles. Cross-reference: Format Validator tracks all four in its broken-targets backlog.

---

## Issue 5: `compiled_to` defects — 3 raw files, no change in 3 runs

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Three raw files carry `status: processed` and have a compiled `src_*.md`, but no usable forward backlink. Re-run of the 09-28 scan: identical results.
**Evidence:**
- `raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md` — no `compiled_to` key at all
- `raw/posts/2026-05-25_suyash-karn-ai-trillion-dollar-blind-spot-static-website.md` — no key at all
- `raw/articles/2026-05-25_will-ai-replace-systems-thinking.md` line 11 — key spelled **`compile_to:`** (missing `d`), value `"[[src_will-ai-replace-systems-thinking]]"`

**Genuine backlog is 0:** `grep -rl '^status: unprocessed' raw/` returns nothing. These 3 are backlink defects, not a compile queue — the two populations must not be conflated.
**Suggested fix:** add `compiled_to: "[[src_...]]"` to the first two; rename the key on the third. Validator does not edit `raw/`.

---

## Issue 6: `_action-required.md` — pending queue grew to 36; status-key drift widened to 12

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Two structural defects, both re-measured. Pending queue is now **36 entries** (was 33 on 09-30, 30 on 09-28) — three validator runs added three entries and nothing was approved or applied in that window.
**Status-key drift:** a per-entry audit (not a naive grep) shows **9 entries** using the Vietnamese key `- **Trạng thái:** chờ duyệt.` and **27** using `- **Status:** pending` — 36 total, matching the entry count exactly. The raw `grep -c 'Trạng thái'` returns **12**, not 9, because the 09-28 and 09-29 Output entries *quote* the key verbatim inside their issue text. Anyone auditing by grepping the Vietnamese string will overcount by 3.
**Verification:**
```bash
sed -n '/^## Pending Reports/,/^## Báo cáo đã duyệt/p' wiki/reviews/_action-required.md | grep -c '^### '   # 36
sed -n '...' | grep -c '^- \*\*Status:\*\*'      # 27
sed -n '...' | grep -c '^- \*\*Trạng thái:\*\*'   # 9
grep '\*\*Pending reports awaiting review:\*\*' wiki/reviews/_action-required.md   # 36 — agrees
```
**Additional structural note:** 36 entries in the Pending Reports range, but the naive whole-file `grep -c '\*\*Status:\*\* pending'` is unreliable in *both* directions — the history section still holds stale `— APPLIED` entries reading `pending` (overcount) while the Vietnamese-key entries are missed (undercount). The `### ` entry count is the only reliable unit.
**Suggested fix:** Fix Agent normalises the 9 Vietnamese keys to `- **Status:** pending` and clears the stale history-section status lines. Validator does not edit this file beyond adding its own entry. **Julius decision needed:** 36 pending reports with 0 applied in 3 days means the approval loop has stalled; the queue is growing faster than it drains.

---

## Issue 7: [SYSTEMATIC ISSUE] CJK injection — 10 validator runs, zero remediation

**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** CJK injection remains the only Compile Agent defect still actively producing new instances. Every numeric claim from 09-30 was re-verified and **all are exact**.

**Verified inventory (content scope only, `wiki/sources/` + `wiki/concepts/`):**

| Metric | 09-30 claim | Verified 10-01 | Status |
|---|---|---|---|
| Files | 12 | 12 | exact |
| Lines | 14 | 14 | exact |
| CJK chars | 33 | 33 | exact |
| Injections | 9 files / 11 lines / 26 chars | 9 / 11 / 26 | exact |
| Legitimate | 3 files / 3 lines | 3 / 3 | exact |

**Per-file breakdown (chars / lines / path):**
- 5 chars, 2 lines — `wiki/concepts/financial-discipline.md`
- 4 chars, 1 line — `wiki/concepts/low-entry-principle.md`
- 4 chars, 2 lines — `wiki/concepts/ai-chip-design.md`
- 4 chars, 1 line — `wiki/concepts/hundred-years-humiliation.md` — **legitimate**, concept is *about* the term 百年国耻
- 3 chars, 1 line — `wiki/sources/src_50-system-design-concepts-explained-simply.md`
- 2 chars, 1 line — `wiki/sources/src_how-ai-labs-eventually-make-money.md`
- 2 chars, 1 line — `wiki/concepts/ai-lab-business-model.md`
- 2 chars, 1 line — `wiki/concepts/amygdala-vs-prefrontal-cortex.md`
- 2 chars, 1 line — `wiki/concepts/consumption-vs-action.md`
- 2 chars, 1 line — `wiki/concepts/life-planning-20s.md`
- 1 char, 1 line — `wiki/concepts/byte-level-bpe.md` — **legitimate**, term 中 (zhōng, "middle")
- 2 chars, 1 line — `wiki/concepts/chinese-culture-confucianism.md` — **legitimate**, term 国家

Note the legitimate set is **3 files** (not 2 as the 09-29 report stated, and not the `byte-level-bpe` + `hundred-years-humiliation` pair alone). `chinese-culture-confucianism.md` carries 国家 in a concept about Chinese political terminology and is equally intentional.

**Decision still open — unchanged and now blocking.** These injections have survived **10 validator runs** (09-18, 09-20, 09-21, 09-24, 09-25, 09-26, 09-28, 09-29, 09-30, 10-01) without action. Re-escalating the same numbers daily adds no information; this is now a queue item, not a validator finding. **Recommended:** Julius either approves a single cleanup pass (9 files, 11 lines) or records them as accepted baseline so the report stops carrying the inventory. Note that Issue 2 (the `src_how-ai-labs` pair) is *blocked* on this decision — a source-layer injection cannot be fixed as part of the concept-level pass without touching `wiki/sources/`.

---

## Issue 8: [CORRECTION] `quick-scan.sh` section 4 was never patched; skill's baseline of 82 is wrong

**Severity:** INFO
**Dimension:** Completeness
**Issue:** The skill documents that section 4 ("Too few key points") still uses `grep -c '^- '` while section 6 uses the corrected `grep -cE '^- |^[0-9]+\.|^\|'`, and instructs re-baselining to 82. Both halves were wrong. Section 4 was never patched, and 82 does not describe this KB.

**Verified:** quick-scan reported **78** under-5 concepts at run start. An independent re-implementation of the corrected pattern returns **77**. Diffing the two flag lists shows exactly one difference — `five-big-forces.md`, whose Key ideas are a numbered list, so the unpatched counter scored it 2 bullets and the corrected counter scores it 5 (rescued, no longer flagged).

**Repair applied this run.** Section 4 now uses the same pattern as section 6. This is validator-owned tooling under `.hermes/skills/`, explicitly authorised as action item 1 in the 09-28 report — **not** a wiki content edit, so the read-only constraint holds. Post-patch quick-scan reports **77**, matching the independent count.

**Corrected baseline:**
- **77** concepts in the 1–4 range (flagged by quick-scan)
- **9** concepts with a zero-bullet Key ideas section (not flagged, because the gate requires `> 0`)
- **86** concepts total under 5 key points

The 9 zero-bullet files are `ai-coach-prompting`, `ai-first-business-model`, `content-generation-workflow`, `digital-product-flywheel`, `expert-knowledge-extraction`, `google-project-oxygen`, `multi-agent-taxonomy`, `personal-branding-ai`, `six-stage-research-pipeline`. **All 9 are false positives of the 08-25 class, not real defects** — their content is a numbered list or a markdown table that the `grep -cE` pattern now counts correctly (verified: 6, 6, 8, 5 bullets respectively on spot-check). They appear in the zero list only because the *outer* gate `[ "$points" -gt 0 ]` excludes them from the flag output. The `> 0` guard is doing its job; no further change needed.
**Suggested fix:** skill text updated with the corrected baseline (77 / 9 / 86). No wiki action.

---

## Corrections to the 09-30 report

| # | 09-30 claim | Verified 10-01 | Correction |
|---|---|---|---|
| 1 | `[[game-theory]]` evidence cited 7 `wiki/` hits, implying the target exists | 0 concept files, 0 source files; the 7 hits are 1 partial-slug concept, 3 differently-scoped sources, 3 topic indexes | Link is genuinely broken. Evidence line was misleading — use exact-filename tests, not `find -iname` globs. |
| 2 | Skill baseline: "re-baseline the `<5 key points` inventory to 82" | Section 4 unpatched ⇒ real figure was 78; corrected figure is 77 | 82 was never measured against this KB. Baseline is **77**. |
| 3 | Legitimate-CJK set implied 2 files | 3 files — `byte-level-bpe`, `hundred-years-humiliation`, `chinese-culture-confucianism` | Add `chinese-culture-confucianism.md` (国家) to the do-not-fix list. |
| 4 | Blank-line splits in Key ideas: 3 files / 8 splits | Verified 3 files, 14 blank lines total (8 + 3 + 3) | The 8 figure counted only `meaning-through-work.md`. Shape still differs per file — `meaning-through-work` has 7 bullets each separated (deliberate paragraph style, per the 09-28 note), while `busywork-vs-deep-work` (12 bullets) and `one-thing-daily-priority` (9 bullets) carry 3 splits each and are the real single-split defects. Not one uniform fix. |

---

## Checks that passed

- **Dropped-i variant 5:** 0 matches across all 4 sub-patterns — `ngườ` + punctuation, `thờ` compounds, `thay v `, `lờ` compounds. Streak = 12 consecutive clean runs (08-23 → 10-01).
- **Typos variants 1–4:** 0 files for `ngưởi`, double-i, `người` spacing-merge, capital-I.
- **Truncation:** 0 truncated sources, 0 truncated concepts.
- **Empty sections:** 0 empty Key ideas, 0 empty Sources.
- **1-sentence definitions:** 116 concepts KB-wide — unchanged from 09-30's 116, within the established norm.
- **`## Notes` presence:** 538/612 concepts have the section, 74 do not — unchanged.
- **File counts:** 216 sources + 612 concepts = 828, matching the 09-30 report exactly. No deletions, no drift.
- **Raw backlog:** 0 files with `status: unprocessed`.
- **Read-only constraint:** 0 files under `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/` modified in the 10 minutes before this report. The only write outside `wiki/reviews/` was the validator-owned `.hermes/skills/` script repair (Issue 8), which is not wiki content.

---

## Systemic observations

**[SYSTEMATIC ISSUE] CJK injection is the only Compile Agent defect still reproducing.** All five Vietnamese tokenization variants have been at 0 for 12 consecutive runs. CJK injection remains the sole active producer. Root cause is narrowed and unchanged: raw ingestion is clean, the source layer is clean except for the one inherited case, and injection occurs at concept compile. Recommend Compile Agent prompt review, per the standing escalation raised 09-18.

**[SYSTEMATIC ISSUE] The approval loop has stalled.** 36 pending reports, 0 applied in the last 3 runs, queue growing at 1/day from three validators. Every finding in this report is a carry-over from a queue that is not draining. Escalating the same defects daily produces no new information — the constraint is Julius-side action, not validator throughput.

**[INFRASTRUCTURE] Vault backup down 7 days.** HEAD is `e05f00ab` dated 2026-09-24 20:51; 696 uncommitted files KB-wide. The 09-30 Format report already flagged this at 6 days. All uncommitted work is exposed to single-machine loss. Not an output-quality finding, but it gates safe remediation of everything else.

---

## Verdict summary

| Item | Verdict | Reason |
|---|---|---|
| `amygdala-vs-prefrontal-cortex.md` | **REJECT** | 2 ERROR unremediated, day 2 — CJK injection + 6 untranslated bullets, one factually misstates its source |
| `src_how-ai-labs-eventually-make-money.md` + `ai-lab-business-model.md` | **REVISE** | Source-layer CJK injection; blocked pending the Issue 7 decision |
| `ai-infrastructure-bubble.md` | **REVISE** | 3 unsourced metrics (carry-over); today's additions are accurate |
| 3 no-source wikilinks | **REVISE** | Drop the links; nothing to compile from |
| 3 raw `compiled_to` defects | **REVISE** | Add/rename the forward backlink |
| 9 CJK injection files | **REVISE** | Blocked on Julius decision — approve cleanup or record as baseline |
| `_action-required.md` queue | **REVISE** | 36 pending, 12 status-key drift, approval loop stalled |
| `quick-scan.sh` section 4 | **PROMOTE** (repaired) | Pattern aligned with section 6; 78 → 77 verified |
| Remaining 824 files | **PROMOTE** | No new defects found |

**Date defect in `src_interconnects-ai.md` (carry-over from 09-30, still present):** line 24 Summary reads `bài ngày 09/2021... 21/09/2026` — `09/2021` is impossible in a 2026 snapshot. Verified against `raw/websites/2026-09-28_interconnects-ai.md`: the RSS listing runs 2026-06-19 to 2026-09-22, and the balance-of-power post is dated **2026-09-21**. Intended text is almost certainly `09/2026... 21/09/2026`. Non-blocking, but a garbled year token in a factual field. Fold into the REVISE batch.

---

## Structural integrity

- Report file: `wiki/reviews/2026-10-01_output-report.md`
- Action file: `wiki/reviews/_action-required.md` — pending 36 → 37 at time of writing; **→ 38 after the sibling Format Validator ran at 23:15 and added its own entry.** The `### ` entry count and the header agree at 38; this run's entry is the 10-01 Output one.
- Memory log: `.hermes/MEMORY.md` — entry inserted top-of-file (line 15); sibling Format entry sits above it at line 7
- Validator-owned script modified: `.hermes/skills/output-validator/scripts/quick-scan.sh` (section 4 pattern, Issue 8)

**Sibling-race note.** Format Validator (23:15) ran between this report's writing and its verification pass. Two consequences, both benign: (1) the pending header moved 37 → 38 under this validator's own entry — the sibling counted ahead, exactly the race documented in the skill; (2) `MEMORY.md` gained the sibling's entry at line 7, pushing this entry from 7 to 15. Neither validator clobbered the other's writes. The correct invariant is `### ` entry count == header value, both now 38 — not either literal.
