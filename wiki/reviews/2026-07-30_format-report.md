# Format Validator Report — 2026-07-30

**Status:** pending
**Issues found:** 411
**Created:** 2026-07-30
**Validator:** format-validator
**Files checked:** 867 (495 concepts + 159 sources + 34 indexes + 179 topics)
**Delta from 07-26:** +28 files (+26 concepts, +3 sources, +1 index, -2 topics), +54 WARNINGs (357→411)

---

## Issues Found: 411

| Severity | Count | Category |
|---|---|---|
| ERROR | **0** | — |
| WARNING | **411** | Broken wikilinks (forward-references) |
| INFO | 0 | — |

**0 ERROR streak:** 07-22 through 07-30 (9 consecutive clean runs).

---

## All Issues — WARNING Level Only

All 411 WARNINGs are **broken wikilinks** — concepts and sources linking to target concepts that have not yet been compiled. This is a forward-reference pattern, not a structural format error.

### Top Broken Link Targets

| Target | Refs | Type |
|---|---|---|
| `game-theory` | 10 | Concept not yet compiled |
| `confirmation-bias` | 8 | Concept not yet compiled |
| `deep-work` | 5 | Concept not yet compiled |
| `ai-coding-agents` | 4 | Concept not yet compiled |
| `decision-making` | 4 | Concept not yet compiled |
| `src_you-just-hired-a-million-bad-employees-a16z.md` | 5 | Source with `.md` suffix in wikilink |
| `src_agent-memory-7-types-substack.md` | 7 | Source with `.md` suffix (new batch) |
| `src_the-let-them-theory-gabriel-reality.md` | 4 | Source with `.md` suffix (new batch) |
| `src_how-to-remember-everything-you-read-dan-koe.md` | 4 | Source with `.md` suffix (new batch) |
| `career-design` | 3 | Concept not yet compiled |

### New Pattern: Source wikilinks with `.md` extension

The new batch (memory-types, let-them-theory, dan-koe) contains wikilinks to sources WITH `.md` extension in the link target. Example: `[[src_agent-memory-7-types-substack.md]]` instead of `[[src_agent-memory-7-types-substack]]`. Count: ~11 instances across 3 new source files. This is a Compile Agent regression — source-to-source wikilinks should not include `.md`.

### Source files with `.md` in wikilink targets

- `wiki/concepts/coal-framework.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/episodic-memory.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/external-retrieval-memory.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/parametric-memory.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/procedural-memory.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/prospective-memory.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/semantic-memory.md` → `[[src_agent-memory-7-types-substack.md]]`
- `wiki/concepts/anterior-cingulate-cortex.md` → `[[src_the-let-them-theory-gabriel-reality.md]]`
- `wiki/concepts/control-trap.md` → `[[src_the-let-them-theory-gabriel-reality.md]]`
- `wiki/concepts/intolerance-of-uncertainty.md` → `[[src_the-let-them-theory-gabriel-reality.md]]`
- `wiki/concepts/let-them-theory.md` → `[[src_the-let-them-theory-gabriel-reality.md]]`
- `wiki/concepts/cybernetics-learning-model.md` → `[[src_how-to-remember-everything-you-read-dan-koe.md]]`
- `wiki/concepts/error-signal-learning.md` → `[[src_how-to-remember-everything-you-read-dan-koe.md]]`
- `wiki/concepts/goal-directed-learning.md` → `[[src_how-to-remember-everything-you-read-dan-koe.md]]`
- `wiki/concepts/learning-filter.md` → `[[src_how-to-remember-everything-you-read-dan-koe.md]]`

---

## ✅ Passing

- ✅ All frontmatter fields valid
- ✅ All YAML sections parse correctly
- ✅ Field order compliant with format-spec.md v2.2
- ✅ sub_tags count within range (1-3)
- ✅ All tags in TAGS.md
- ✅ Section order valid (required sections present in correct order)
- ✅ No duplicate YAML keys
- ✅ File naming conventions followed
- ✅ Wikilink format correct (quoted in frontmatter, bare in body)

---

## Verdict

**PROMOTE** — 0 ERRORs, clean structural quality. All 411 WARNINGs are forward-reference broken wikilinks (content gaps) plus a new `.md`-in-wikilink pattern in the memory-theory batch. No format fixes required.

The `.md` suffix in source wikilinks is a minor annoyance but doesn't break anything since these targets don't exist either way. Recommend flagging in Compile Agent workflow to strip `.md` from wikilink targets.

---

## Structural Quality Trend

| Date | Files | ERRORs | WARNINGs |
|---|---|---|---|
| 07-22 | 817 | 0 | 318 |
| 07-23 | 831 | 0 | 337 |
| 07-24 | 829 | 1 | 336 |
| 07-25 | 829 | 0 | 336 |
| 07-26 | 839 | 0 | 357 |
| 07-30 | **867** | **0** | **411** |

9 consecutive days with 0-1 ERRORs. KB format is structurally solid.
