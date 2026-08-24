# Output Validation — 2026-08-23

**Status:** applied
**Approved by:** Julius
**Issues found:** 4
**Created:** 2026-08-23 23:05:00
**Validator:** output-validator

---

## Scope

- **Files checked:** 705 (178 sources + 527 concepts) + 8 drafts skipped
- **New files today:** 8 (4 sources + 4 concepts) — all read in full:
  - Sources: `src_ai-engineering-skills-map.md`, `src_ai-skills-map-building-deploying-ai-apps.md`, `src_schedule-maxxing.md`, `src_strategy-vs-tactics-dan-koe.md`
  - Concepts: `agentic-coding.md`, `ai-engineering-skills.md`, `schedule-maxxing.md`, `strategic-thinking.md`
- **Method:** quick-scan.sh + mandatory dropped-i grep variant 5 (3 sub-patterns, MANUAL) + full read of new files + wikilink resolution check (23/23 targets OK) + cross-check concept claims against parent sources

---

## Issue 1: Carry-over typo "ngưởi" — 10 instances in 5 files

**File:** wiki/sources/src_the-let-them-theory-gabriel-reality.md; wiki/concepts/intolerance-of-uncertainty.md; wiki/concepts/let-them-theory.md; wiki/concepts/control-trap.md; wiki/concepts/anterior-cingulate-cortex.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Variant-1 typo persists in 5 older files. NOT introduced today — all 5 predate 08-23 (new-file count = 0). Same carry-over class as the double-i/capital-I batch flagged 08-22 and applied inline.
**Evidence:** instance counts per file: src_the-let-them-theory-gabriel-reality.md ×4, control-trap.md ×3, intolerance-of-uncertainty.md ×1, let-them-theory.md ×1, anterior-cingulate-cortex.md ×1.
**Suggested fix:** `sed -i 's/ngưởi/người/g'` on the 5 files listed above.

---

## Issue 2: Carry-over typo "người" spacing merge — 11 instances in 4 files

**File:** wiki/sources/src_ai-future-skills.md; wiki/sources/src_critical-thinking-dennett.md; wiki/sources/src_tribute-system-new-world-order.md; wiki/concepts/occams-broom.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Variant-3 spacing merge ("người" fuses with next word). NOT introduced today (new = 0). Verified real merges, not regex overlap with double-i (0 double-i matches in these files): ngườilãnh đạo, ngườikhác, ngườithường, ngườicần, ngườiphụ thuộc, ngườitrị giá, ngườita.
**Evidence:** `src_ai-future-skills.md`: "mọi ngườithường bỏ qua", "làm việc cùng ngườikhác"; `src_critical-thinking-dennett.md`: "con ngườicần phát triển", "ngườiphụ thuộc"; `src_tribute-system-new-world-order.md`: "giữa ngườilãnh đạo và"; `occams-broom.md`: "ngườita thường từ chối".
**Suggested fix:** sed longest-match-first per Production Lessons (`s/ngườilãnh đạo/người lãnh đạo/g` etc. for each observed collocation), then re-read surrounding sentences for concealed missing periods.

---

## Issue 3: Concept `agentic-coding.md` mixes two distinct source contexts without separation

**File:** wiki/concepts/agentic-coding.md
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Definition and Key ideas 1–8 describe Thariq's Fable/unknowns framework; Key ideas 9–10 and frontmatter source #2 introduce Andrew Ng's coding-agent skill from a different series (different author, different model context — Ng's post does not mention Fable). The merge is legitimate (both concern agentic coding) but the two framings are interleaved without signaling the switch: Key idea 1 states "Fable là model đầu tiên mà chất lượng work bị giới hạn bởi..." as a general claim while it is a product-specific claim by Thariq.
**Evidence:** line 21: "Bottleneck chính trong agentic coding không phải là model — Fable là model đầu tiên mà chất lượng work bị giới hạn bởi khả năng của người dùng..."; lines 29–30 attribute to "(Andrew Ng)" mid-list. Source list correctly includes both sources.
**Suggested fix:** Either split key ideas into two labeled groups (Fable framework / Andrew Ng skills map), or reword Key idea 1 to scope the claim to Thariq's argument ("Theo Thariq, Fable là model đầu tiên mà..."). No factual error — presentation only.

---

## Issue 4: Musashi attribution unverifiable against live source

**File:** wiki/sources/src_strategy-vs-tactics-dan-koe.md; wiki/concepts/strategic-thinking.md
**Severity:** INFO
**Dimension:** Factual
**Issue:** Both files cite "Musashi's 9 precepts (Book of 5 Rings)". The Koe article is crawler-walled (fetch returned no body text), so the exact list could not be verified against the primary post. Cross-check against the published Go Rin No Shō ground truth chapter list (Earth: ground/strategy framing; Water: "do not think dishonestly"; Fire: timing/attention to small things; Wind; Void) is consistent with the 9 items as summarized — no contradiction found. Flagged for transparency only.
**Evidence:** source line 33: "Musashi's 9 precepts (Book of 5 Rings): từ 'don't think dishonestly' đến 'do nothing useless'". Live fetch of `https://thedankoe.com/p/strategy-vs-tactics-how-to-actually/` returned 74 KB shell, 1.7 KB text, zero keyword hits (crawler wall).
**Suggested fix:** None required if Julius confirms content matches the original article read at ingest time. Optional: note in source Metadata that verification was done offline.

---

## Checks passed (new files)

1. **Dropped-i variant 5 grep (MANDATORY manual):** 0 matches on entire KB for all 3 sub-patterns (`ngườ[ ,.\t;:!?)]|ngườ$`, `thờ (đại|gian|hiện|điểm|kỳ|buổi|trẻ)|đồng thờ[^i]`, `thay v `). Clean.
2. **Double-i / capital-I variants:** 0 instances anywhere (08-22 inline fix held).
3. **Wikilink resolution:** all 23 unique `[[...]]` targets from the 8 new files resolve to existing files (concepts primary, sources fallback).
4. **Frontmatter:** all 8 new files have valid frontmatter, correct main_tag/sub_tags, `date_compiled`/`last_updated: 2026-08-23`.
5. **Completeness:** all 4 concepts have Definition (2+ câu), Key ideas ≥9, Related concepts, Sources, Notes. All 4 sources have Summary (4+ câu), Key points ≥7, Concepts referenced, Original excerpts. No truncation signals.
6. **Cross-source consistency:** `ai-engineering-skills.md` figures match both Ng sources (10.000+ job postings, 4 skills, 6 sub-areas); part-1/part-2 relationship stated correctly in both directions.
7. **Topic pages exist:** schedule-maxxing, strategic-thinking, ai-engineering-skills, fable-finding-unknowns all present under `wiki/topic/`.
8. **Drafts:** 8 files in `wiki/drafts/` skipped per spec.

## Systemic issues

None new this run. The two carry-over typos (Issues 1–2) are residue of the known Compile Agent tokenization defect family (5 documented variants); total open inventory is now small (~21 instances / 9 files, down from ~45 instances / 32 files before the 08-22 inline apply). Not escalating — below threshold (>50% new files affected AND >30 instances). Recommend Fix Agent sweep these 9 files in the next approved batch.

## Summary

| Severity | Count |
|---|---|
| ERROR | 0 |
| WARNING | 2 |
| INFO | 2 |

Batch quality cao. 8 file mới sạch: 0 typo mới, full structure, mọi wikilink resolve, số liệu nhất quán với sources. Còn lại chỉ carry-over inventory (9 file cũ) và 1 khuyến nghị trình bày cho agentic-coding.md.

**Applied:** 2026-08-24 09:58 by Fix Agent (Kara) — fixes verified in place (applied inline by Connor 09:48); report archived.
