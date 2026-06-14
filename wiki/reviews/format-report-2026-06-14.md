# Format Validator Report — 2026-06-14

**Validator:** Connor (Hermes-RK800)
**Scope:** wiki/concepts/ + wiki/sources/
**Total files reviewed:** 364 (282 concepts + 82 sources)

## Issues Found: 18

### CRITICAL — Invalid YAML frontmatter

**6 concept files affected:**
- `agent-harness.md`
- `code-as-substrate.md`
- `evolutionary-mismatch.md`
- `factory-missions.md`
- `multi-agent-taxonomy.md`
- `plan-execute-verify-loop.md`

**Root cause:** `sub_tags` defined twice — once as inline array `[research, ...]` and once as block list with `-` items. YAML parser fails.

**Fix:** Remove duplicate block list, keep inline array only.

### CRITICAL — Invalid main_tag (not in Pool A)

**3 concept files + 2 source files affected:**
- `activation-energy.md` → main_tag: `psychology` (Pool B, not Pool A)
- `hypergamy.md` → main_tag: `psychology`
- `relationship-dynamics.md` → main_tag: `psychology`
- `src_activation-energy.md` → main_tag: `psychology`
- `src_hypergamy.md` → main_tag: `psychology`

**Root cause:** Compile Agent used Pool B tag as main_tag. Pool A only allows: `ai`, `crypto`, `tech`, `productivity`, `system`, `economic`, `politic`.

**Fix:** Change main_tag to appropriate Pool A tag. Suggested: `productivity` for psychology-related content (as mental models / behavioral frameworks).

### CRITICAL — Missing required field

**1 concept file affected:**
- `active-thinking.md` → missing `topic` field

### CRITICAL — Invalid main_tag: psychology (source files)

(See above, counted in same group)

### WARNING — Field order wrong

**1 concept file affected:**
- `active-thinking.md` → field order: `type`, `status`, `main_tag`, `sub_tags`, `sources`, `last_updated` — missing `topic` caused order shift

### WARNING — Original wikilink format issue (source files)

**4 source files affected:**
- `src_code-as-agent-harness-arxiv-2605-18747.md` → `[[2026-05-22_code-as-agent-harness-arxiv-2605-18747.md]]` (has `.md` extension)
- `src_how-to-read-cash-flow-statement.md` → `[[2026-05-29_how-to-read-cash-flow-statement.md]]`
- `src_japanese-evening-routine-fix-sleep.md` → `[[2026-05-29_japanese-evening-routine-fix-sleep.md]]`
- `src_luke-alvoeiro-multi-agent-architecture-factory.md` → `[[2026-05-22_luke-alvoeiro-multi-agent-architecture-factory.md]]`

**Fix:** Remove `.md` extension from wikilink.

---

## ✅ Passing

- 272/282 concepts have valid frontmatter
- 76/82 sources have valid frontmatter
- All `last_updated` fields are valid ISO dates
- All `sub_tags` counts are within 1–3 range
- No main_tag masquerading as sub_tag detected in this run
- No `status: stub` detected

---

## Verdict

**REVISE** — 18 issues across 16 files. Most are Compile Agent structural errors (duplicate YAML + wrong main_tag pool). Fixable by Fix Agent.
