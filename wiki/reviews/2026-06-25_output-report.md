# Output Validation — 2026-06-25

**Status:** pending
**Issues found:** 4 (0 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-06-25 15:53
**Validator:** output-validator

**Files checked:** 436 (102 sources + 334 concepts)
**New files today:** 0

> **Context:** This re-run found no new files for today's batch. Output findings therefore reflect current backlog/systemic content quality, not a newly ingested set.

---

## Issue 1: 1-sentence definitions remain systemic across the wiki

**Severity:** WARNING  
**Dimension:** Completeness

**Count:** 332 concepts

**Issue:** Definition sections remain compressed to a single sentence across most concepts.

**Assessment:** Systemic compile-template limitation. Not a same-day regression.

---

## Issue 2: Too few key points (<5) — 81 concepts

**Severity:** WARNING  
**Dimension:** Completeness

**Count:** 81 concepts

**Issue:** `## Key ideas` has fewer than 5 items in 81 concepts.

**Representative files:**
- `wiki/concepts/activation-energy.md` — 3
- `wiki/concepts/agent-harness.md` — 4
- `wiki/concepts/cash-flow-statement.md` — 3
- `wiki/concepts/five-big-forces.md` — 2
- `wiki/concepts/tokenmaxxing.md` — 4

---

## Issue 3: Empty `## Key ideas` — 9 concepts

**Severity:** WARNING  
**Dimension:** Completeness

**Count:** 9 concepts

**Issue:** Quick scan still detects 9 concept files with empty `## Key ideas` sections.

---

## Issue 4: Draft concepts remain high

**Severity:** INFO  
**Dimension:** Status audit

**Count:** 164 concepts

**Issue:** `status: draft` still appears on 164/334 concepts.

---

## Summary

| Metric | Value |
|---|---:|
| New files today | 0 |
| 1-sentence definitions | 332 |
| Concepts with <5 key points | 81 |
| Empty `## Key ideas` | 9 |
| Empty `## Sources` | 0 |
| Draft concepts | 164 |
| Truncated concepts | 0 |
| Truncated sources | 0 |

## Verdict

**REVISE** — no new batch-specific failures today, but the backlog-level content-depth issues remain unchanged.

## Verification

```bash
test -f "wiki/reviews/2026-06-25_output-report.md" && echo "✅ Report written"
```