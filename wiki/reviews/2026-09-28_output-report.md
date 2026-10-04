# Output Validation — 2026-09-28
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 3 (0 ERROR, 3 WARNING, 0 INFO)
**Created:** 2026-09-28 23:00:42 +0700
**Validator:** output-validator
**Files checked:** 817 (212 sources + 605 concepts)
**New files (wiki layer):** 0 — `grep 'date_compiled: 2026-09-28'` → 0 sources; `grep 'last_updated: 2026-09-28'` → 0 concepts
**New files (raw layer):** 4 — ingested today, all `status: unprocessed`, none compiled

---

## Issue 1: `compiled_to` backlink missing in 3 processed raw files — one is a misspelled key

**File:** `raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md`, `raw/posts/2026-05-25_suyash-karn-ai-trillion-dollar-blind-spot-static-website.md`, `raw/articles/2026-05-25_will-ai-replace-systems-thinking.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Three raw files carry `status: processed` and have a compiled `src_*.md` whose frontmatter points back at them via `original: "[[...]]"` — but the forward `compiled_to` backlink is missing, so the raw→source direction is broken in all three. The third file has a **misspelled key**: `compile_to:` (missing the `d`), which means it is invisible to any consumer — including my own KB-scan procedure, which greps `compiled_to` — grepping for it returns nothing. The other two have no backlink key of any kind. This is a defect class that has never been reported before: prior runs treat "no `compiled_to`" as synonymous with "not yet compiled", which silently misreads these three as pending backlog.

**Evidence:**
```yaml
# raw/articles/2026-05-25_will-ai-replace-systems-thinking.md:11  — typo key
compile_to: "[[src_will-ai-replace-systems-thinking]]"

# raw/posts/2026-05-25_suyash-karn-...-static-website.md — no backlink key at all
status: processed          # ← line 9

# raw/posts/2026-09-01_google-cloud-agent-sandbox-runtimes.md — no backlink key at all
status: processed          # ← line 9
```
Verified: `grep -c '^compiled_to:'` = 0 on all three. Reverse links intact — `src_will-ai-replace-systems-thinking.md:3`, `src_ai-trillion-dollar-blind-spot.md:3`, and `src_google-cloud-agent-sandbox-runtimes.md:3` all carry `original: "[[<raw-slug>]]"`. KB-wide scale: 209 raws have `compiled_to`, 3 processed raws do not (1.4%).

**Suggested fix:** Fix Agent adds `compiled_to:` to the two files that lack it, and corrects `compile_to:` → `compiled_to:` on the third. Add the key-spelling check to the raw-layer scan so a typo'd key cannot masquerade as an uncompiled file. Do **not** treat these three as backlog.

---

## Issue 2: 4 raw files ingested today — the pipeline moved, at the raw layer only

**File:** `raw/websites/2026-09-28_interconnects-ai.md`, `raw/posts/2026-02-03_why-you-waste-your-evenings-neuroscience.md`, `raw/articles/2026-07-02_the-second-derivative-why-no-one.md`, `raw/websites/2025-08-04_atom-project-american-truly-open-models.md`
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Two consecutive validator runs (09-27, 09-28) reported the KB as idle. That is accurate for the wiki layer but not for the raw layer: four new raw files were ingested today between 19:53 and 20:43, all with `status: unprocessed`. The 09-27 format report's `no-compilation-happened` variant ("0 wiki files added, **0 raw ingested**, 0 commits") is therefore correct as of its own run but no longer describes the current state. **All four are untracked by git** — the backup cron has not committed them, which is consistent with the 5 `??` untracked entries noted on 09-27 (that count has since grown).

**Evidence:**
```
raw/websites/2026-09-28_interconnects-ai.md                       mtime 2026-09-28 20:43  status: unprocessed
raw/posts/2026-02-03_why-you-waste-your-evenings-neuroscience.md  mtime 2026-09-28 19:53  status: unprocessed
raw/articles/2026-07-02_the-second-derivative-why-no-one.md        date_ingested: 2026-09-28  status: unprocessed
raw/websites/2025-08-04_atom-project-american-truly-open-models.md date_ingested: 2026-09-28  status: unprocessed
```
`git status --porcelain raw/` → all four are `??`, plus `M` on the three index files (`articles.md`, `posts.md`, `websites.md`).

**Suggested fix:** No validator action. Flagged so the next Compile Agent run has a visible queue (4 files) and so the Format/Hygiene delta on 09-29 is not misread as idle. If the backup cron has not run since 09-24 20:51 (`e05f00ab` is still HEAD), that is a separate pipeline problem worth checking — it now covers 4 untracked raw files plus whatever else has accumulated.

---

## Issue 3: `_action-required.md` pending count is unverifiable — 9 entries use a Vietnamese status key

**File:** `wiki/reviews/_action-required.md`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** The file's stated count (`**Pending reports awaiting review:** 27`) matches the number of `###` entries in the Pending Reports section (27), but only **18** of those entries carry the machine-readable `- **Status:** pending` line. The other 9 use the Vietnamese key `- **Trạng thái:** chờ duyệt.` — same meaning, different key name, invisible to any grep for `Status`. This is a second, independent bookkeeping defect layered on the 16 stale history-section status lines flagged yesterday: a validator that recomputes the pending count the documented way (`grep -c '\*\*Status:\*\* pending'` scoped to the section) gets **18**, not 27, and would undercount by 9.

**Evidence:**
```
Section entry count (###):                     27   ← matches header
Entries with "**Status:** pending":            18   ← what the documented grep returns
Entries with "**Trạng thái:** chờ duyệt.":      9   ← invisible to that grep
Naive whole-file "**Status:** pending":        34   ← 18 pending + 16 stale history lines
```
The 9 bilingual entries: Hygiene 09-17 through 09-22 (6) and Format 09-17, 09-18, 09-19 (3).

**Suggested fix:** Normalize the 9 entries to `- **Status:** pending` so the documented counting procedure is correct. The 16 stale history-section status lines (`— APPLIED` in the heading, still `pending` in the body) remain outstanding from the 09-27 flag — recommend doing both in one pass, since the naive whole-file grep overcounts by 16 until the second half is cleaned.

---

## Checks performed — all PASS

**Typo variants (all 5 Compile Agent tokenization defects): 0 instances**
- `ngưởi` hook-above: 0 files
- `ngườii/đờii/lờii` double-i: 0 files, 0 instances
- `người` spacing merge: 0 files, 0 instances
- `ngườI` / `[vowel+diacritic]I` capital-I: 0 files, 0 instances
- **Variant 5 dropped-i (mandatory manual grep, all 4 sub-patterns): 0 matches.** Clean span **08-23 → 09-28**. Cite the date range, not the count — past entries' streak numbers drifted non-monotonically (09-18 logged 16, 09-25 logged 15). Demotion to weekly has been recommended since 09-30/08-31/09-01 and remains unconfirmed; the daily grep continues because it is the one check that would catch a catastrophic deletion typo.

**Structural integrity: 0 violations**
- Truncated concepts (missing sections): 0
- Truncated sources (missing Concepts referenced): 0
- Empty Key ideas: 0 · Empty Sources: 0
- Draft concepts: 436 (excluded from validation by design)

**Depth-debt legacy inventory: stable, spot-verified genuine**
- 116 concepts with 1-sentence Definition; 83 concepts with <5 key points. Sampled the flagged set: `amygdala-vs-prefrontal-cortex` (1 def sentence), `low-entry-principle` (1), `financial-discipline` (2) — real. Sampled the not-flagged set to confirm no false positives: `five-big-forces`, `power-law`, `mental-models` all score 2 and are correctly excluded. Unchanged from 09-26/09-27; pre-existing, not introduced by any recent batch.

**CJK contamination: 0 new. Carry-over figures re-verified.**
- Content scope (`wiki/sources/` + `wiki/concepts/`): **14 CJK-bearing lines / 33 CJK chars / 12 files** — matches the 09-27 correction exactly.
- Legitimate Chinese content (do not fix) — 3 files, each re-read today: `byte-level-bpe.md:26` (中, script byte count), `chinese-culture-confucianism.md:22` (国家, gloss for "quốc gia"), `hundred-years-humiliation.md:16` (百年国耻, the standard name of the Century of Humiliation — the concept is about this term).
- Unremediated Compile Agent injections: **9 files / 11 lines**, unchanged — 09-18: `src_50-system-design-concepts-explained-simply.md:24`, `src_how-ai-labs-eventually-make-money.md:24`, `ai-lab-business-model.md:16`; 09-20: `ai-chip-design.md:22,24`, `financial-discipline.md:21,23`, `life-planning-20s.md:17`; 09-21: `amygdala-vs-prefrontal-cortex.md:24`, `consumption-vs-action.md:25`, `low-entry-principle.md:21`.
- Review scope (`wiki/reviews/`): 67 CJK-bearing lines / 9 files excluding `archive/`, 68 / 10 including it. The 09-27 entry logged "60 lines / 10 files" — that figure is everything except the 09-26 report itself, which contributes 8 lines by quoting the strings it flags. Both numbers are legitimate: reports must quote what they report. Excluding the 09-26 report returns exactly 60, confirming the 09-27 methodology.

**Carry-over from the 09-26 report — all 4 still on disk, none fixed**
| Sev | Issue | Verified location today |
|---|---|---|
| ERROR | Baird et al. 2012 / Wilson et al. 2014 study misattribution | `creative-incubation.md:20,:36` + `src_do-less.md:31` — all 3 confirmed |
| WARNING | Mid-list blank line splitting Key ideas | `busywork-vs-deep-work.md:30`, `one-thing-daily-priority.md:28` — both confirmed |
| WARNING | Untranslated "progress" in Definition | `busywork-vs-deep-work.md:18` — confirmed |
| INFO | PMC9797525 annotated in concept, absent from source | `stress-habituation.md:36`; `grep -c PMC wiki/sources/src_do-less.md` = 0 — confirmed |

Note on the carry-over blank-line finding: `meaning-through-work.md` (last_updated 2026-06-22) has **6** such splits, not 6 scattered ones — every one of its 7 Key-ideas bullets is separated by a blank line, i.e. a consistent paragraph-style list, versus the single mid-list splits in the two 09-26 files. Same count as reported on 09-26 (6, verified correct), but the two shapes are not the same defect and Fix Agent may reasonably keep the file as-is while removing the two stray splits. Total KB-wide: 3 files, 8 splits.

---

## Recommendations

1. **Fix Agent — Issue 1 is new and unreported:** three processed raw files have no usable `compiled_to` backlink, one because the key is misspelled `compile_to`. This is invisible to the standard backlog scan and will keep recurring until the key spelling is checked.
2. **Fix Agent — Issue 3:** normalize 9 `**Trạng thái:**` entries to `**Status:** pending`; fold in the 16 stale history-section status lines still outstanding from 09-27.
3. **Fix Agent — still blocking from 09-26:** the Baird/Wilson misattribution (1 ERROR). It propagates to every future concept compiled from `src_do-less`.
4. **Julius decision:** the 9 CJK injections have now survived 7 validator runs (09-18, 09-20, 09-21, 09-24, 09-25, 09-26, 09-28) without action. Either approve a cleanup pass or accept them as a standing baseline.
5. **Pipeline check:** HEAD is still `e05f00ab` (2026-09-24 20:51) and the vault backup has not run in 4 days, with untracked files accumulating in `raw/` and `.hermes/.curator_backups/`. Outside validator scope — raising it because it affects evidence integrity for every validator that relies on `git log`.

---

## Corrections (2026-09-28, 23:00 validation run)

No numeric claim in the 09-26/09-27 reports required correction this run. The CJK figures the 09-27 run established were independently re-derived today and matched (14 lines / 33 chars / 12 files in content scope; 9 unremediated injection files; 3 legitimate-Chinese files). The one apparent discrepancy — the review-scope CJK count moving 60 → 67 — resolves to the 09-26 report itself contributing 8 lines by quoting the flagged strings; excluding it returns exactly 60, so the 09-27 methodology holds.

Carried forward unchanged, all re-verified present on disk today: the Baird/Wilson misattribution, the blank-line list splits, the untranslated "progress", and the PMC ID with no counterpart in the compiled source. None fixed since 09-26.
