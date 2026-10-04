# Output Validation — 2026-09-29
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 4 (0 ERROR, 4 WARNING, 0 INFO)
**Created:** 2026-09-29 23:08:43 +0700
**Validator:** output-validator
**Files checked:** 817 (212 sources + 605 concepts)
**New files (wiki layer):** 0 — `grep 'date_compiled: 2026-09-29'` → 0 sources; `grep 'last_updated: 2026-09-29'` → 0 concepts
**New files (raw layer):** 0 — no raw file has `date_ingested: 2026-09-29`; `find raw/ -newermt '2026-09-29 00:00'` returns nothing. Unprocessed backlog is still the same **4 files** ingested 09-28.

---

## Issue 1: `quick-scan.sh` section 4 still counts only `- ` bullets — the 08-25 fix was never applied to it

**File:** `.hermes/skills/output-validator/scripts/quick-scan.sh` (line 110–111)
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** On 2026-08-25 the skill's "Empty Key ideas" counter was patched after it produced false positives on numbered lists and tables, changing the pattern to `grep -cE '^- |^[0-9]+\.|^\|'`. **Section 4 ("Too few key points") was not patched with it** — it still reads `grep -c '^- '` only. Any concept whose Key ideas are a numbered list is silently scored 0 bullets and drops out of the counter entirely (`points -gt 0` gate), so it is never flagged even when genuinely short. Running the corrected pattern across all 605 concepts changes the flagged set: **83 → 82**, and the difference is real, not cosmetic.

**Evidence:**
```bash
# quick-scan.sh:110-111 (current, unpatched)
points=$(sed -n '/^## Key ideas$/,/^## /p' "$f" 2>/dev/null \
    | sed '1d;/^## /,$d' | grep -c '^- ' 2>/dev/null || echo 0)

# python re-derivation with the 08-25 pattern (bullets + numbered + table rows)
OLD (bullet-only) flagged: 83
CORRECTED (bullets+numbered+table) flagged: 82
--- false positives eliminated: 1
```
The eliminated file is `five-big-forces.md`, whose Key ideas are a **numbered list 1–5** plus 2 bullets:
```
1. **Debt and Money (Nợ và Tiền tệ):** …
…
5. **New Technologies (Công nghệ Mới):** …
- **Tương tác:** …
- **Phân tích:** …
```
Old pattern scores it **2** (`- ` bullets only) → flagged as "too few key points" despite carrying 7 points. Corrected pattern scores **7** → correctly excluded. Note the 2026-08-25 lesson table names `google-project-oxygen.md` (8 ideas) and `six-stage-research-pipeline.md` (8 table rows) as the verified cases; the same defect simply had not been carried to section 4.

**Suggested fix:** Apply the 08-25 pattern to section 4 for consistency: `grep -cE '^- |^[0-9]+\.|^\|'`. Re-baseline the "<5 key points" legacy inventory to **82** (from 83) once patched, and correct the historical claim below. This is a script change, not a wiki change — validator scope, no approval needed beyond Julius's awareness.

---

## Issue 2: The 09-28 and 09-26 spot-check claims about "correctly not flagged" are wrong in both directions

**File:** `wiki/reviews/2026-09-28_output-report.md:93` (and inherited into `_action-required.md` 09-28 entry + `.hermes/MEMORY.md` 09-28 entry)
**Severity:** WARNING
**Dimension:** Factual
**Issue:** The 09-28 report states: *"Sampled the not-flagged set to confirm no false positives: `five-big-forces`, `power-law`, `mental-models` all score 2 and are correctly excluded."* **All three are factually wrong, in two different ways.** `five-big-forces` scores 7 bullets and is **flagged** by quick-scan right now (visible in today's scan output as `wiki/concepts/five-big-forces.md:2`) — so the claim "correctly excluded" is false. `power-law` and `mental-models` score **3**, not 2 — minor arithmetic, but the substance is right: they are genuinely short and *are* correctly flagged. So one of three sampled "not-flagged" files was actually flagged, and the other two were miscounted while being correctly classified for the wrong stated reason.

**Evidence:**
```
five-big-forces:  7 points  (5 numbered + 2 bullets) → quick-scan FLAGS it as ":2"
power-law:        3 points                              → quick-scan flags ":3" — report said "2"
mental-models:    3 points                              → quick-scan flags ":3" — report said "2"
```
Today's quick-scan output contains `wiki/concepts/five-big-forces.md:2` in the "Too few key points" list, which directly contradicts the 09-28 report's assertion.

**Suggested fix:** Treat this as the measurement half of Issue 1 — after the script fix, the "not-flagged" sample must be re-derived from the corrected counter. The `financial-discipline` sample claim (2 definition sentences) was spot-checked today and **is** correct. Amending the 09-28 report text is optional; what must not persist is the claim that `five-big-forces` is excluded.

---

## Issue 3: `_action-required.md` bilingual-key defect is unchanged, but the 09-28 count of "18" is now 21

**File:** `wiki/reviews/_action-required.md`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Carry-forward from 09-28 Issue 3, re-verified today with a parser instead of a bare grep (the 09-28 count was itself a grep artifact). The structure is unchanged: **30 entries** in Pending Reports, **21** carry a line-initial `- **Status:** pending`, and **9** use `- **Trạng thái:** chờ duyệt.`. The naive whole-file grep for `**Status:** pending` returns **41** (21 pending + 16 stale history-section lines + 4 from the new sibling runs since). The 9 bilingual entries are Hygiene 09-17→09-22 (6) and Format 09-17/09-18/09-19 (3) — identical list to 09-28. **The defect has not been fixed**, and it has now propagated: the 09-28 Output entry itself quotes the Vietnamese key inside its summary prose, so a naive `grep 'Trạng thái'` returns 10 matches (9 real + 1 quote), which would mislead anyone auditing the count from the report text.

**Evidence:**
```
Pending Reports entries (###):                      30   ← matches header "30"
Line-initial "- **Status:** pending":               21   ← what the documented grep sees
Line-initial "- **Trạng thái:**":                    9   ← invisible to that grep
Naive whole-file "**Status:** pending":             41   ← 21 + 16 stale history + 4 sibling
Entries with BOTH keys:                              1   ← the 09-28 Output entry (quotes the key in prose)
```
The 9 unfixed entries:
```
Hygiene  09-22 (23:31), 09-21 (23:31), 09-20 (23:30), 09-19 (23:30), 09-18 (23:33), 09-17
Format   09-17, 09-19 (23:15), 09-18 (23:16)
```

**Suggested fix:** Normalize the 9 entries to `- **Status:** pending`, and fold in the 16 stale history-section status lines still outstanding from 09-27 — one pass fixes both bookkeeping defects. Separately, avoid quoting raw `- **Trạng thái:**` inside a future entry's prose, since it pollutes the very grep used to audit the count. The `### ` entry count remains the only reliable unit until both halves are cleaned.

---

## Issue 4: `vault backup` still stopped — now 5 days, and today's report adds a 13th untracked report

**File:** `.git` state of the vault
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Hygiene 09-28 escalated this as a new ERROR (backup stopped since 09-24 20:51). Re-verified today: **still stopped, now 5 days**. Local `HEAD` = `e05f00ab`; `git ls-remote origin refs/heads/master` (read-only, no fetch) returns the **same** `e05f00ab` — so the main machine has not pushed either, which localizes the fault to the backup process itself rather than to a push failure. Untracked report files have grown from 11 to **12** before today's run (now 13 with this report): 09-25, 09-26, 09-27, 09-28 format/hygiene/output, plus today's three. Since `.gitignore` does not exclude `wiki/reviews/` (verified by the 09-28 hygiene run), all of them will land in the first commit when the backup resumes — no intervention needed, but 5 days of uncommitted work is accumulating on a single machine.

**Evidence:**
```
git log --oneline -1                 → e05f00ab vault backup: 2026-09-24 20:51:08
git ls-remote origin refs/heads/master → e05f00abf29e84c8ab9874aeab1850345115a37e
git status --porcelain wiki/reviews/  → 12 × ?? (11 from 09-25→09-28 + _action-required.md M)
```
Raw layer is also entirely untracked: 5 `??` raw files (`the-second-derivative`, `why-your-waste-your-evenings-neuroscience`, `do-less`, `atom-project`, `interconnects-ai`) + 3 `M` index files. The do-less batch (1 source + 5 concepts) is `??` in `wiki/` too — it has been output-validated (09-26) but never committed.

**Suggested fix:** Not a validator action — validator writes only `wiki/reviews/` and does not commit or push. **Julius:** check on the main machine whether Obsidian is still open, the Git plugin still enabled, and whether a merge conflict or an expired token is blocking commits. Raised because every validator's evidence chain depends on `git log`; with 5 days uncommitted, `find -newer` against any older baseline is the only trustworthy signal.

---

## Checks performed — all PASS

**Typo variants (all 5 Compile Agent tokenization defects): 0 instances**
- `ngưởi` hook-above: 0 files
- `ngườii/đờii/lờii` double-i: 0 files, 0 instances
- `người` spacing merge: 0 files, 0 instances
- `ngườI` / `[vowel+diacritic]I` capital-I: 0 files, 0 instances
- **Variant 5 dropped-i (mandatory manual grep, all 4 sub-patterns): 0 matches.** Clean span **08-23 → 09-29**. Cite the date range, not a streak counter — past entries' streak numbers drifted non-monotonically (09-18 logged 16, 09-25 logged 15). Demotion to weekly has been recommended repeatedly and remains unconfirmed; the daily grep continues because it is the one check that would catch a catastrophic deletion typo.

**Structural integrity: 0 violations**
- Truncated concepts (missing sections): 0
- Truncated sources (missing Concepts referenced): 0
- Empty Key ideas: 0 · Empty Sources: 0
- Draft concepts: 436 (excluded from validation by design)

**Multi-source backlink invariant (Defect A): 0 mismatches KB-wide**
With 0 new concepts there is no new batch to check, so the invariant was run across the whole KB instead — the cheapest way to catch a backlog. Frontmatter `sources:` count vs body `## Sources` bullet count, for every concept declaring ≥2 sources: **0 mismatches**. The 08-31 recurrence (`ai-engineering-skills.md`, 4 in frontmatter / 2 in body) is not present anywhere today.

**Depth-debt legacy inventory: stable, one measurement defect found**
- quick-scan reports **116** concepts with 1-sentence Definition and **83** concepts with <5 key points. The key-points figure is 83 under the unpatched counter and **82** under the corrected one (Issue 1).
- Spot-checked the flagged set — genuine: `amygdala-vs-prefrontal-cortex` (1 def sentence), `low-entry-principle` (1), `financial-discipline` (2 def sentences, 2 — matches the 09-28 claim).
- Spot-checked the claimed-not-flagged set — **2 of 3 claims wrong** (Issue 2).

**CJK contamination: 0 new. Carry-over figures re-verified.**
- Content scope (`wiki/sources/` + `wiki/concepts/`): **14 CJK-bearing lines / 33 CJK chars / 12 files** — matches the 09-27 correction and the 09-28 re-verification exactly.
- Legitimate Chinese content (do not fix) — 3 files, each re-read today: `byte-level-bpe.md:26` (中, script byte count), `chinese-culture-confucianism.md:22` (国家, gloss for "quốc gia"), `hundred-years-humiliation.md:16` (百年国耻, the standard name of the Century of Humiliation — the concept is about this term).
- Unremediated Compile Agent injections: **9 files / 11 lines**, unchanged — 09-18: `src_50-system-design-concepts-explained-simply.md:24`, `src_how-ai-labs-eventually-make-money.md:24`, `ai-lab-business-model.md:16`; 09-20: `ai-chip-design.md:22,24`, `financial-discipline.md:21,23`, `life-planning-20s.md:17`; 09-21: `amygdala-vs-prefrontal-cortex.md:24`, `consumption-vs-action.md:25`, `low-entry-principle.md:21`.
- Review scope (`wiki/reviews/`): **68 lines / 10 files** excluding `archive/`, **69 / 11** including it. 09-28 logged 67/9 and 68/10; the +1 is this report's own quoted strings plus the growing report set — expected, since every report contributes the strings it flags.

**Carry-over from 09-26 and 09-28 — all still on disk, none fixed**
| Sev | Issue | Verified today |
|---|---|---|
| ERROR | Baird et al. 2012 / Wilson et al. 2014 study misattribution | `creative-incubation.md:20,:36` + `src_do-less.md:31` — all 3 confirmed |
| WARNING | Mid-list blank line splitting Key ideas | `busywork-vs-deep-work.md:30`, `one-thing-daily-priority.md:28` — both confirmed |
| WARNING | Untranslated "progress" in Definition | `busywork-vs-deep-work.md:18` — confirmed |
| INFO | PMC9797525 annotated in concept, absent from source | `stress-habituation.md:36`; `grep -c PMC wiki/sources/src_do-less.md` = 0 — confirmed |
| WARNING | 3 processed raws missing `compiled_to` (1 misspelled `compile_to`) | All 3 confirmed unchanged; KB still 209 raws with `compiled_to` |

Carry-over blank-line note (kept from 09-28, re-verified): `meaning-through-work.md` splits at lines **21, 23, 25, 27, 29, 31** — 6 splits meaning **every one of its 7 Key-ideas bullets is separated**, i.e. a deliberate paragraph-style list, not the same defect as the single mid-list splits in the two 09-26 files. KB-wide: 3 files, 8 splits. Fix Agent may reasonably leave this file alone.

---

## Recommendations

1. **Output-validator script — Issue 1 (self-fix, no wiki change):** patch `quick-scan.sh` section 4 to the 08-25 pattern and re-baseline the legacy inventory to 82. This is a measurement defect that has been silently under-counting numbered-list concepts in every run since 08-25.
2. **Fix Agent — Issue 3:** normalize 9 `**Trạng thái:**` entries to `**Status:** pending`; fold in the 16 stale history-section status lines outstanding from 09-27. One pass clears both.
3. **Fix Agent — still blocking from 09-26:** the Baird/Wilson misattribution (1 ERROR). It propagates to every future concept compiled from `src_do-less`.
4. **Julius decision:** the 9 CJK injections have now survived 8 validator runs (09-18, 09-20, 09-21, 09-24, 09-25, 09-26, 09-28, 09-29) without action. Either approve a cleanup pass or accept them as a standing baseline.
5. **Pipeline — Issue 4 (escalating):** `vault backup` stopped 5 days; remote `master` also at `e05f00ab`, so the fault is the backup process, not the push. 13 reports + 5 raw files + the do-less wiki batch uncommitted.

---

## Corrections (2026-09-29, 23:00 validation run)

Self-audit of every numeric claim carried forward from the 09-28 and 09-26 reports, re-derived with explicitly scoped paths.

| Claimed (source) | Claimed value | Verified today | Verdict |
|---|---|---|---|
| 09-28 §"Depth-debt": `five-big-forces`, `power-law`, `mental-models` all score 2, correctly excluded | 2, not flagged | `five-big-forces` = **7, IS flagged**; `power-law` = 3; `mental-models` = 3 | **WRONG** — see Issue 2 |
| 09-28 Issue 1: 3 processed raws missing `compiled_to`, 1 with `compile_to:` typo; 209 raws have the key | 3 / 209 | identical | correct |
| 09-28 §CJK content: 14 lines / 33 chars / 12 files | 14/33/12 | 14/33/12 | correct |
| 09-28 §CJK review scope: 67 lines / 9 files excl. archive | 67/9 | 68/10 | drift (+1: this report) — expected, methodology sound |
| 09-28 Issue 3: 9 entries use `**Trạng thái:**` | 9 | 9 (list identical) | correct, unfixed |
| 09-28 §CJK injections: 9 files / 11 lines unremediated | 9/11 | 9 files, 11 lines | correct |
| 09-26/09-28 carry-over: Baird/Wilson 3 sites; blank splits at `:30`/`:28`; "progress" at `:18`; PMC gap | as listed | all confirmed at the same line numbers | correct |
| 09-26/09-28: `meaning-through-work.md` = 6 splits | 6 | 6 (lines 21,23,25,27,29,31) | correct |
| quick-scan "Too few key points" counter | 83 | 83 under unpatched pattern, **82** under the 08-25 pattern | **measurement defect** — see Issue 1 |

No claim about file counts required correction: 817 total (212 sources + 605 concepts) is reproduced by three independent methods (frontmatter dates, `ls | wc -l`, quick-scan totals).
