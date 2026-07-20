# Format Validation — 2026-07-17

**Status:** applied
**Issues found:** 324
**ERRORs:** 5
**WARNINGS**: 319
**INFOS:** 0
**Created:** 2026-07-17 23:16
**Approved by:** Julius
**Approved on:** 2026-07-20
**Validator:** format-validator
**Files checked:** 796
**Total issues**: 324
Files checked: 796
Total issues: 324

> **Δ from 07-14 (approved):** 306 WARNINGs, 0 ERRORs → 324 issues, 5 ERRORs, 319 WARNINGs across 796 files. The three-day clean streak (0 ERRORs: 07-14, 07-15, 07-16) is broken today — 5 structural/naming ERRORs detected. Source: 3 concept files missing required sections, 2 source files exceeding slug length limit.

---

## Delta from 07-14 (approved)

| Metric | 07-14 | 07-17 | Δ |
|---|---|---|---|
| Files checked | 769 | 796 | +27 |
| Concepts | 427 | 444 | +17 |
| Sources | 143 | 148 | +5 |
| Indexes | 33 | 33 | 0 |
| Topics | 166 | 171 | +5 |
| **Total issues** | **306** | **324** | **+18** |
| **ERRORs** | **0** | **5** | **+5** 🔴 |
| **WARNINGs** | **306** | **319** | **+13** |
| **INFOs** | **0** | **0** | 0 |

---

## Positive Delta (resolved from 07-14)

No issues resolved — 07-14 had zero ERRORs and 306 WARNINGs (all forward-reference wikilinks). Today's WARNING count is +13 larger due to KB growth.

## Negative Delta (new in 07-17)

| # | Severity | Category | File | Issue |
|---|---|---|---|---|
| 1 | ERROR | Sections | `wiki/concepts/destination-vs-vehicle.md` | Missing required section: ## Key ideas |
| 2 | ERROR | Sections | `wiki/concepts/psychic-energy.md` | Missing required section: ## Sources |
| 3 | ERROR | Sections | `wiki/concepts/social-attraction.md` | Missing required section: ## Key ideas |
| 4 | ERROR | Naming | `wiki/sources/src_is-there-anything-left-to-build-in-crypto-wintermute.md` | Slug exceeds 50 chars (52 chars) |
| 5 | ERROR | Naming | `wiki/sources/src_the-5-laws-of-people-who-never-chase-gabriel-reality.md` | Slug exceeds 50 chars (52 chars) |

Plus +13 WARNINGs from new files referencing yet-uncompiled concepts (forward-references — expected, no action needed).

---

## Summary

| Metric | Value |
|---|---|
| Files checked | 796 |
| Concepts (validated) | 444 |
| Sources (validated) | 148 |
| Indexes (validated) | 33 |
| Topics (validated) | 171 |
| Errors reading | 0 |
| **Total issues** | **324** |
| **ERRORs** | **5** |
| **WARNINGs** | **319** |
| **INFOs** | **0** |

---

## ERROR Breakdown (5)

### Issue 1–3: Missing required sections (3 concept files)

Three concepts are missing required sections per format-spec.md §2:

**1. `wiki/concepts/destination-vs-vehicle.md`**
- **Severity:** ERROR
- **Category:** Sections
- **Issue:** Missing required section `## Key ideas`
- **Expected:** `## Key ideas` appears after `## Definition`, before `## Related concepts`

**2. `wiki/concepts/social-attraction.md`**
- **Severity:** ERROR
- **Category:** Sections
- **Issue:** Missing required section `## Key ideas`
- **Expected:** `## Key ideas` appears after `## Definition`, before `## Related concepts`

**3. `wiki/concepts/psychic-energy.md`**
- **Severity:** ERROR
- **Category:** Sections
- **Issue:** Missing required section `## Sources`
- **Expected:** `## Sources` as last section, with wikilinks to source files

**Root cause:** Likely Compile Agent skipping these sections during compilation. These 3 concepts were compiled without the required section structure.

**Suggested fix:** Recompile or manually add missing sections: `destination-vs-vehicle.md` + `social-attraction.md` need `## Key ideas`; `psychic-energy.md` needs `## Sources`.

### Issue 4–5: Slug exceeds 50-character limit (2 source files)

Two source files have slugs exceeding the 50-character limit per format-spec.md §2.1 (also applied to sources by convention):

**4. `wiki/sources/src_is-there-anything-left-to-build-in-crypto-wintermute.md`**
- **Severity:** ERROR
- **Category:** Naming
- **Issue:** Slug body `is-there-anything-left-to-build-in-crypto-wintermute` is 52 characters
- **Expected:** ≤ 50 characters
- **Suggested fix:** Rename to shorter slug, e.g., `src_is-there-anything-left-to-build-in-crypto.md` (48 chars)

**5. `wiki/sources/src_the-5-laws-of-people-who-never-chase-gabriel-reality.md`**
- **Severity:** ERROR
- **Category:** Naming
- **Issue:** Slug body `the-5-laws-of-people-who-never-chase-gabriel-reality` is 52 characters
- **Expected:** ≤ 50 characters
- **Suggested fix:** Rename to shorter slug, e.g., `src_the-5-laws-of-people-who-never-chase.md` (44 chars)

**Root cause:** Long source titles producing slugs that exceed the length limit. Compile Agent should truncate slugs to ≤ 50 chars.

---

## WARNING Summary (319)

All 319 WARNINGs are broken wikilinks (forward-references to unconcompiled concepts). None are structural or syntactic issues.

- **296** individual broken wikilinks (199 unique targets)
- **21** forward-reference summary groups (files with 4+ broken links, grouped to stay under report limit)
- **2** raw-file `original` wikilink issues (files not found in `raw/` subdirectories)

### Top 10 most-referenced missing targets

| Target | Refs |
|---|---|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[src_you-just-hired-a-million-bad-employees-a16z.md]]` | 5 |
| `[[deep-work]]` | 4 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[critical-thinking]]` | 3 |

### Raw-file original link issues (2)

| File | Issue |
|---|---|
| `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` | `[[2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md]]` — raw file not found |
| `src_you-just-hired-a-million-bad-employees-a16z.md` | `[[2026-07-15_you-just-hired-a-million-bad-employees-a16z.md]]` — raw file not found |

Both are timing issues (source compiled before raw file indexed) — may self-resolve or need manual correction.

---

## Topic files: Clean

171 topic files (`wiki/topic/*.md`) — all passed light validation: `topic` matches filename, `auto_generated: true`, valid `last_updated`, H1 present. No issues.

## Tag files: Clean

33 index files (Tầng 1–3 + tag indexes) — all passed index-spec.md validation. No format violations. The 2026-07-03 `level` field / path contradiction fix is holding.

---

## Systemic issues

### 1. Broken wikilinks remain the dominant pattern

319/324 issues (98.5%) are forward-reference wikilinks. This is the natural byproduct of an actively growing KB — concepts reference each other, and not all are compiled yet. **Not a quality concern** at this scale.

### 2. Clean streak broken — structural gaps in 3 new concepts

After three consecutive days of 0 ERRORs (07-14 through 07-16), 5 new ERRORs appear today. Three are missing sections in concept files — Compile Agent may not be enforcing the full section checklist. Two are slug-length violations in source files.

**Recommendation:** Review Compile Agent's section-requirement enforcement. The fact that most concepts (441/444 = 99.3%) have correct sections suggests this is an intermittent edge case, not a systematic regression.

### 3. Slug length limit regularly violated for long titles

Two source slugs exceed 50 chars today. Previous reports have flagged similar naming issues. The Compile Agent should auto-truncate slugs during compilation.

---

## Actions needed

| Priority | Action | Owner |
|---|---|---|
| 🔴 HIGH | Add `## Key ideas` to `destination-vs-vehicle.md` and `social-attraction.md` | Fix Agent |
| 🔴 HIGH | Add `## Sources` to `psychic-energy.md` | Fix Agent |
| 🟡 MEDIUM | Shorten slugs of 2 source files to ≤ 50 chars | Fix Agent / Manual rename |
| 🟢 LOW | 319 forward-ref wikilinks — no action (expected in growing KB) | — |
| 🟢 LOW | 2 raw-file original wikilink issues — transient timing, may self-resolve | — |

---

## Escalations

### [SYSTEMATIC VIOLATION — Slug Length]

```
Pattern: 2 source files have slugs exceeding 50-char limit
Likely cause: Compile Agent does not truncate slugs during compilation
Recommendation: Update compile-agent SKILL.md to enforce slug ≤ 50 chars (truncate at 50 if needed)
```

### [SYSTEMATIC VIOLATION — Missing Sections]

```
Pattern: 3 concept files missing required sections (2x Key ideas, 1x Sources)
Likely cause: Compile Agent skipping sections for certain concept types or source materials
Recommendation: Review compile-agent SKILL.md section requirements — ensure ## Key ideas and ## Sources are mandatory
```

---

## Verification

- [x] validate.py ran successfully on 796 files
- [x] 5 ERRORs confirmed (3 missing sections + 2 slug > 50)
- [x] 319 WARNINGs confirmed (all forward-reference broken wikilinks)
- [x] _action-required.md updated with today's entry
- [x] Report written to `wiki/reviews/2026-07-17_format-report.md`
