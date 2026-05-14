# Output Validation — 2026-05-14

**Status:** pending
**Issues found:** 4
**Created:** 2026-05-14 23:00:00
**Validator:** output-validator

**Files checked:** 14 (6 new, 8 existing)

---

## Issue 1: Incorrect wikilink format in frontmatter `sources` field

**File:** 7 concept files:
- `wiki/concepts/philosopher-syndrome.md`
- `wiki/concepts/information-compression.md`
- `wiki/concepts/abstraction-layer-fallacy.md`
- `wiki/concepts/organizational-incrementalism.md`
- `wiki/concepts/nice-syndrome.md`
- `wiki/concepts/lazy-thinking.md`
- `wiki/concepts/active-thinking.md`

**Severity:** ERROR
**Dimension:** Factual
**Issue:** All 7 concept files use full-path wikilink `[[wiki/sources/src_active-vs-lazy-thinking]]` in the frontmatter `sources` field. The correct format is the bare slug `[[src_active-vs-lazy-thinking]]`, consistent with all other wikilinks used throughout the wiki (e.g., `## Concepts referenced`, `## Sources` sections all use bare slugs like `[[lazy-thinking]]`).

**Evidence:**
```yaml
sources:
  - [[wiki/sources/src_active-vs-lazy-thinking]]
```

**Suggested fix:** Replace `[[wiki/sources/src_active-vs-lazy-thinking]]` with `[[src_active-vs-lazy-thinking]]` in all 7 files. The bare slug format `[[src_<slug>]]` is the established convention (used consistently by the 5 system-topic concepts referencing `[[src_what-comes-after-systems-thinking]]`).

---

## Issue 2: Empty `## Notes` sections in all 12 concept files

**File:** 12 concept files:
- `wiki/concepts/systems-thinking-limitations.md`
- `wiki/concepts/complex-adaptive-systems.md`
- `wiki/concepts/cynefin-framework.md`
- `wiki/concepts/complicated-vs-complex.md`
- `wiki/concepts/ashbys-law.md`
- `wiki/concepts/philosopher-syndrome.md`
- `wiki/concepts/information-compression.md`
- `wiki/concepts/abstraction-layer-fallacy.md`
- `wiki/concepts/organizational-incrementalism.md`
- `wiki/concepts/nice-syndrome.md`
- `wiki/concepts/lazy-thinking.md`
- `wiki/concepts/active-thinking.md`

**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Every concept file has `## Notes` as a section header with no content following it. The Notes section is documented as "optional" (for Julius's annotations), but having it present and empty across all 12 files is a systematic pattern. An empty section header provides no value and introduces visual clutter.

**Evidence:**
```
## Notes

```
(empty — no content follows the section header)

**Suggested fix:** Either (a) remove the empty `## Notes` section from all 12 files, or (b) add brief Julius annotations/reflections where applicable. Option (a) is simpler and appropriate since these are freshly compiled concepts with no annotations yet.

---

## Issue 3: Source summaries at minimum boundary (exactly 3 sentences)

**File:** 2 source files:
- `wiki/sources/src_what-comes-after-systems-thinking.md`
- `wiki/sources/src_active-vs-lazy-thinking.md`

**Severity:** INFO
**Dimension:** Completeness
**Issue:** Both source file summaries are exactly 3 sentences — the bare minimum of the 3-5 sentence target range. While technically compliant, borderline compliance across all source files suggests the Compile Agent may default to minimum-length summaries.

**Evidence:**
Both summaries are 3 sentences each, covering the source topic and key frameworks but lacking a concluding sentence or additional context.

**Suggested fix:** Consider expanding to 4-5 sentences for richer context. This is a suggestion for Compile Agent tuning, not an immediate fix.

---

## Issue 4: Key points count slightly above target range

**File:** 3 files:
- `wiki/sources/src_what-comes-after-systems-thinking.md` (11 items)
- `wiki/sources/src_active-vs-lazy-thinking.md` (11 items)
- `wiki/concepts/active-thinking.md` (10 items)

**Severity:** INFO
**Dimension:** Completeness
**Issue:** Key points/ideas lists exceed the recommended 5-10 range. Two source files have 11 points, and one concept has 10 (at boundary). The content is substantive, but slightly over the target.

**Evidence:**
- `src_what-comes-after-systems-thinking.md`: 11 key points
- `src_active-vs-lazy-thinking.md`: 11 key points
- `active-thinking.md`: 10 key ideas

**Suggested fix:** Consolidate or trim to 5-10 most impactful points. Not urgent — content quality is good, just slightly over target.

---

## Systemic Observation

**Pattern:** All 7 concept files compiled from the same ingest batch (`src_active-vs-lazy-thinking`, date_compiled: 2026-05-13) share identical formatting issues:
- Same incorrect wikilink format (`[[wiki/sources/...]]`)
- Same empty Notes sections
- Same `status: draft` frontmatter

This suggests Compile Agent may have an issue in its wikilink generation logic — it's prepending path prefixes to source wikilinks. The newer batch (2026-05-14, system topic) uses correct bare-slug format, so the fix may apply only to the batch compiled on 2026-05-13.

**Recommendation:** Review Compile Agent's source wikilink generation and ensure consistent bare-slug format.
