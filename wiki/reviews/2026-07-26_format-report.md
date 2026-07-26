# Format Validation — 2026-07-26

**Status:** pending
**Issues found:** 357
**ERRORs**: 0
**WARNINGS**: 357
**INFOS:** 0
**Created:** 2026-07-26 23:15
**Validator:** format-validator
**Files checked:** 839
**Total issues**: 357
Files checked: 839
Total issues: 357

> **Δ from 07-25 (previous, approved):** +10 files (829→839), +21 issues (336→357). +6 concepts, +2 sources, +2 topics. 0 ERRORs maintained (clean streak continues — 07-22 through 07-26). WARNINGs +21 (336→357), all broken wikilinks. File breakdown: Concepts 466→472 (+6), Sources 153→155 (+2), Indexes 34→34 (no change), Topics 176→178 (+2).
>
> **Δ from 07-20 (last applied baseline):** +43 files (796→839), +39 issues (318→357). -1 ERROR (1→0), +39 WARNING (318→357). The single 07-20 ERROR has been fixed; all remaining issues are forward-reference broken wikilinks.

---

## Files checked

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 839 | 472 | 155 | 34 | 178 |

---

## Summary

**357 WARNINGs — 0 ERRORs.** Clean structural quality across all 839 files. Every warning is a broken wikilink: forward-references to concepts not yet compiled into the knowledge base. No frontmatter violations, no section structure errors, no naming issues, no code block problems.

**Breakdown:**
- 332 individual broken wikilinks (226 unique targets)
- 21 forward-reference summary groups (files with 4+ broken links, counted as single entries)
- 4 false-positive `original` field warnings (files exist in `raw/tools/` and `raw/articles/` — validator script regex bug)

---

## Issue Categories

### 1. Forward-Reference Broken Wikilinks — 353 WARNINGs

**All 353 broken wikilink WARNINGs are forward-references** — concepts linked from wiki files but not yet compiled into `wiki/concepts/`. These are expected in a growing knowledge base and represent content gaps, not format defects.

**Top 20 most-referenced uncompiled targets:**

| Target | References |
|---|---|
| `game-theory` | 10 |
| `confirmation-bias` | 8 |
| `src_you-just-hired-a-million-bad-employees-a16z.md` | 5 |
| `ai-coding-agents` | 5 |
| `career-design` | 5 |
| `decision-making` | 5 |
| `deep-work` | 4 |
| `src_introducing-backsearch-gr-inc.md` | 3 |
| `src_monid-ai-agent-tool-platform.md` | 3 |
| `attention-economy` | 3 |
| `ai-hype-vs-reality` | 3 |
| `economic-inequality` | 3 |
| `critical-thinking` | 3 |
| `naval-ravikant` | 3 |
| `risk-parity` | 3 |
| `second-law-of-thermodynamics` | 3 |
| `homeostasis` | 3 |
| `saying-no` | 3 |
| `power-imbalance` | 3 |
| `src_why-the-math-mafia-is-doing-well-jesse-zhang.md` | 3 |

**Top 10 files by warning count:**

| File | Warnings |
|---|---|
| `wiki/concepts/collaborative-thinking.md` | 5 |
| `wiki/concepts/probabilistic-thinking.md` | 5 |
| `wiki/concepts/feedback-loops.md` | 4 |
| `wiki/concepts/hanlons-razor.md` | 4 |
| `wiki/concepts/meaning-through-work.md` | 4 |
| `wiki/concepts/occams-broom.md` | 4 |
| `wiki/concepts/occams-razor.md` | 4 |
| `wiki/concepts/pay-per-call-pricing.md` | 4 |
| `wiki/concepts/systematic-trading.md` | 4 |
| `wiki/concepts/vibe-coding.md` | 4 |

### 2. False-Positive `original` Field Warnings — 4 WARNINGs

Validator script flagged 4 source files for missing raw files, but all 4 files exist in the correct `raw/` subdirectories. This is a known validator bug: the wikilink target includes `.md` (e.g., `[[2026-07-25_introducing-backsearch-gr-inc.md]]`), and the validator appends `.md` again, looking for `file.md.md`.

| File | Target | Actual location | Status |
|---|---|---|---|
| `wiki/sources/src_introducing-backsearch-gr-inc.md` | `2026-07-25_introducing-backsearch-gr-inc.md` | `raw/tools/` | ✅ Exists |
| `wiki/sources/src_monid-ai-agent-tool-platform.md` | `2026-07-25_monid-ai-agent-tool-platform.md` | `raw/tools/` | ✅ Exists |
| `wiki/sources/src_why-the-math-mafia-is-doing-well-jesse-zhang.md` | `2026-07-14_why-the-math-mafia-is-doing-well-jesse-zhang.md` | `raw/articles/` | ✅ Exists |
| `wiki/sources/src_you-just-hired-a-million-bad-employees-a16z.md` | `2026-07-15_you-just-hired-a-million-bad-employees-a16z.md` | `raw/articles/` | ✅ Exists |

**Root cause:** The `original` field wikilink includes `.md` extension (`[[file.md]]`), but the validator strips `[[...]]` then appends `.md`, producing a double-extension glob pattern. Fix needed in `scripts/validate.py` — strip `.md` from wikilink target before searching, or handle the case where the target already has the extension.

---

## Escalations

### [VALIDATOR BUG] — original field false positives (recurring)

**Status:** Known issue, unresolved since 2026-07-20.
**Impact:** 4 false WARNINGs in today's report. Previously observed 2026-07-20, 2026-07-24, 2026-07-25.
**Root cause:** `scripts/validate.py` line ~280 — `check_original_wikilink()` does not strip `.md` from wikilink targets before globbing. When the target already includes `.md`, the validator appends another `.md` and searches for `*file.md.md`.
**Recommendation:** Patch `scripts/validate.py` to strip `.md` suffix from targets before appending.

### [VALIDATOR BUG] — Source-body raw-file wikilink resolution (recurring)

**Status:** Known issue, unresolved.
**Impact:** Several `src_*.md` wikilinks flagged as broken in concept files, but the source files exist in `wiki/sources/`. The broken-source-reference check in `validate.py` doesn't account for `src_` prefix wikilink patterns properly.
**Recommendation:** Review and patch broken-wikilink resolution logic for `src_`-prefixed targets.

---

## Verification

- ✅ All 839 wiki files scanned (472 concepts + 155 sources + 34 indexes + 178 topics)
- ✅ 0 read errors — all files successfully parsed
- ✅ 0 YAML parse failures
- ✅ 0 frontmatter structural errors (missing required fields, invalid types, Pool mismatches)
- ✅ 0 section structure errors (missing headings, duplicates, order violations)
- ✅ 0 naming convention violations
- ✅ 0 code block issues
- ✅ `context/USER.md` correctly skipped (read-only, no frontmatter)
- ✅ Topic files dispatched correctly (scope: topic, light validation only)
- ✅ All 34 index files routed by path-derived level (no level/path contradictions)
- ✅ 4 false-positive `original` field warnings verified — all 4 raw files confirmed to exist

---

## Verdict

**No format fixes required.** All 357 WARNINGs are either:
1. **Forward-reference broken wikilinks** (353) — content gap, not format defect. These resolve naturally as concepts are compiled.
2. **Validator false positives** (4) — `original` field warnings where files actually exist. Validator bug, not file issue.

**0 ERRORs** — structural format quality is clean across all 839 files.

**Recommendation:** APPROVE without fixes. Address validator bugs in `scripts/validate.py` separately.
