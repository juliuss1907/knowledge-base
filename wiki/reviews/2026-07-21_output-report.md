# Output Validation — 2026-07-21

**Status:** approved
**Approved by:** Julius
**Issues found:** 5 (1 ERROR, 2 WARNING, 2 INFO)
**Created:** 2026-07-21 23:06:27
**Validator:** output-validator

---

## Issue 1: [SYSTEMATIC ISSUE] Fifth variant typo — dropped trailing 'i' after 'ờ'

**Severity:** ERROR
**Dimension:** Vietnamese
**Issue:** Compile Agent is dropping the trailing 'i' from Vietnamese words that should end in "ời". This is the fifth manifestation of the same root cause (LLM mishandling characters after Vietnamese diacritics). Three sub-patterns detected:

| Pattern | Should be | Instances | Files affected |
|---|---|---|---|
| `ngườ` (e.g. "ngườ ta", "ngườ gác cửa") | `người` | ~22 | 13/16 |
| `thờ` (e.g. "thờ đại", "thờ gian", "đồng thờ") | `thời` | ~8 | 3/16 |
| `lờ` (e.g. "chính lờ") | `lời` | ~5 | 3/16 |

**Total: ~35 instances across 13/16 new files (81%).**

**Evidence — representative samples:**

- `src_ill-make-you-believe-you-can-achieve.md:24`: "phần lớn **ngườ** ta đã chấp nhận" → người ta
- `src_ill-make-you-believe-you-can-achieve.md:24`: "trong **thờ** đại hiện tại" → thời đại
- `src_ill-make-you-believe-you-can-achieve.md:24`: "**đồng thờ** chỉ ra" → đồng thời
- `src_the-art-of-elaboration.md:30`: "Viết bằng chính **lờ** buộc" → chính lời
- `src_the-art-of-elaboration.md:32`: "như **ngườ** gác cửa" → người gác cửa
- `concepts/internal-locus-of-control.md:16`: "**Ngườ** có internal locus" → Người
- `concepts/learned-helplessness.md:16`: "khi một **ngườ** liên tục" → người
- `concepts/new-leverage-digital-assets.md:16`: "Trong **thờ** đại AI" → thời đại
- `concepts/protoge-effect.md:17`: "cho **ngườ** khác ghi nhớ" → người khác

**Affected files (13/16):**
`src_ill-make-you-believe-you-can-achieve.md` (6 ngườ + 5 thờ), `src_the-art-of-elaboration.md` (1 ngườ + 2 lờ), `src_the-writing-habit-that-saved-my-brain.md` (1 ngườ + 2 thờ), `cheap-dopamine.md` (1 ngườ), `content-repurposing-system.md` (1 ngườ), `delusional-optimism.md` (1 ngườ), `elaboration-learning-technique.md` (1 ngườ + 2 lờ), `internal-locus-of-control.md` (2 ngườ), `learned-helplessness.md` (2 ngườ), `new-leverage-digital-assets.md` (1 ngườ + 1 thờ), `note-taking-systems.md` (1 ngườ), `protoge-effect.md` (2 ngườ + 1 lờ), `psycho-cybernetics.md` (1 ngườ)

**Clean files (3/16):** `forced-linearity-writing.md`, `law-of-assumption.md`, `learning-through-retrieval.md`

**Suggested fix:**
```bash
for f in <affected-files>; do
  sed -i 's/ngườ /người /g; s/ngườ,/người,/g; s/ngườ\./người./g
          s/thờ đại/thời đại/g; s/thờ gian/thời gian/g; s/đồng thờ/đồng thời/g
          s/chính lờ /chính lời /g; s/chính lờ\./chính lời./g' "$f"
done
```

**Root cause context:** This is the fifth variant from the same Compile Agent prompt defect:
1. "ngưởi" (hook-above 'ỉ' instead of grave 'ời') — original
2. "ngườii" (doubled 'i') — 2026-06-23
3. "ngườitrong" (spacing merge) — 2026-07-02
4. "ngườI" (capital-I) — 2026-07-16
5. **"ngườ" (dropped 'i') — 2026-07-21 (NEW)**

**Escalation:** This batch crosses the systematic threshold (>50% of new files affected, >30 total instances). Recommend reviewing Compile Agent's LLM prompt/tokenization settings to address the root cause rather than patching each new variant individually.

**Detection gap:** The `quick-scan.sh` script does NOT currently detect this variant. The existing checks cover 'ngưởi', 'ngườii', spacing merge, and 'ngườI', but not bare 'ngườ' followed by a space/punctuation. Recommend adding to quick-scan.sh:
```bash
grep -rPn 'ngườ[ ,.\t]|thờ (đại|gian)|đồng thờ|chính lờ[ ,.]' wiki/sources/ wiki/concepts/
```

---

## Issue 2: 3 concepts have fewer than 5 key ideas

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Three new concepts have only 4 key ideas each, below the 5-10 minimum threshold from the format spec.

**Files and counts:**
- `wiki/concepts/learned-helplessness.md` — 4 key ideas
- `wiki/concepts/learning-through-retrieval.md` — 4 key ideas
- `wiki/concepts/protoge-effect.md` — 4 key ideas

**Evidence:**
- `learned-helplessness.md`: 4 bullets (Vòng lặp, Dẫn đến việc lý luận, Trở thành cái bẫy, Giải pháp)
- `learning-through-retrieval.md`: 4 bullets (Học sinh thường nghĩ, Gọi lại từ trí nhớ, Elaboration là hình thức, Kết hợp với viết)
- `protoge-effect.md`: 4 bullets (Cognitive load, Viết vừa là hình thức dạy, Kết hợp với elaboration, Dan Koe quote)

**Suggested fix:** Each concept needs at least 1 more key idea. The source material provides additional depth — extract one more distinct point per concept from the original source.

---

## Issue 3: protoge-effect — non-standard concept name spelling

**Severity:** WARNING
**Dimension:** Factual
**Issue:** The concept is named "protoge-effect" but the correct French/English term is "protégé effect" (with accent on both 'e' letters). The filename `protoge-effect.md` and all wikilinks use the unaccented form.

**Evidence:**
- `wiki/concepts/protoge-effect.md` — filename omits accent
- All `[[protoge-effect]]` wikilinks across 3 files use the unaccented form
- The correct term "protégé effect" is widely documented in cognitive science literature

**Suggested fix:** This may be intentional (avoiding special characters in filenames). If so, add a note to the concept's Notes section acknowledging the simplified spelling. If not, rename to `protege-effect.md` (standard ASCII fallback) or consider whether the accent is necessary for searchability.

---

## Issue 4: All 13 new concepts are in draft status

**Severity:** INFO
**Dimension:** Completeness
**Issue:** All 13 concepts compiled today have `status: draft` in their frontmatter. This is consistent with the pipeline (Concepts promote from draft after review), but the batch-wide draft status means no concepts from today are currently referenceable as stable knowledge.

**Files:** All 13 concepts under `wiki/concepts/` compiled 2026-07-21.

**Suggested action:** After typo fixes are applied and key ideas expanded, promote suitable concepts by changing `status: draft` to `status: done`.

---

## Issue 5: Empty Notes sections across all concepts

**Severity:** INFO
**Dimension:** Completeness
**Issue:** All 13 concepts have empty `## Notes` sections. While this is not a format violation (Notes are optional), these sections could carry compilation notes, cross-reference context, or clarification about the concept's boundaries.

**Evidence:** Every concept ends with:
```markdown
## Notes

```

**Suggested action:** Consider having Compile Agent populate Notes with 1-2 sentences about compilation decisions (e.g., "Compiled from single source only — may need expansion", "Concept boundaries overlap with X — see also Y").

---

## Summary

| Dimension | ERROR | WARNING | INFO |
|---|---|---|---|
| Factual accuracy | 0 | 1 (protoge naming) | 0 |
| Completeness | 0 | 1 (too few key ideas) | 2 (draft status, empty notes) |
| Coherence | 0 | 0 | 0 |
| Vietnamese quality | 1 (dropped-i typo) | 0 | 0 |
| **Total** | **1** | **2** | **2** |

**Files checked:** 16 (3 sources + 13 concepts)
**Files with issues:** 13/16 (81%)
**Clean files:** forced-linearity-writing.md, law-of-assumption.md, learning-through-retrieval.md

**Priority action:** Fix the dropped-i typo across 13 files (Issue 1) — this is the blocker.
**Secondary:** Add 1+ key idea to the 3 under-threshold concepts (Issue 2).
