# Output Validation — 2026-06-26

**Status:** approved
**Approved by:** Julius — 2026-06-26 07:12 +07
**Issues found:** 4 (0 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-06-26 07:01:00 +07
**Validator:** output-validator

**Files checked:** 436 (102 sources + 334 concepts)
**New files today:** 0

> **Context:** Đây là re-run toàn bộ validator. Không có file mới trong ngày, nên findings phản ánh backlog/systemic content quality hiện tại.

---

## Delta vs most recent approved output report

Reference baseline: approved/applied Output Validator run dated `2026-06-25 15:53`.

| Metric | Current run | Previous approved | Delta |
|---|---:|---:|---:|
| New files today | 0 | 0 | 0 |
| Total issues | 4 | 4 | 0 |
| WARNING | 3 | 3 | 0 |
| INFO | 1 | 1 | 0 |
| 1-sentence definitions | 332 | 332 | 0 |
| Concepts with <5 key points | 81 | 81 | 0 |
| Empty `## Key ideas` | 9 | 9 | 0 |
| Draft concepts | 164 | 164 | 0 |

**Assessment:** Không có content-quality drift mới. Backlog systemic vẫn giữ nguyên.

---

## Issue 1: 1-sentence definitions remain systemic across the wiki

**Severity:** WARNING
**Dimension:** Completeness

**Count:** 332 concepts

**Issue:** Definition sections vẫn bị nén còn 1 câu ở phần lớn concept files.

**Assessment:** Systemic compile-template limitation. Không phải regression cùng ngày.

---

## Issue 2: Too few key points (<5) — 81 concepts

**Severity:** WARNING
**Dimension:** Completeness

**Count:** 81 concepts

**Issue:** `## Key ideas` có ít hơn 5 items trong 81 concepts.

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

**Issue:** Quick scan vẫn detect 9 concept files có `## Key ideas` rỗng.

---

## Issue 4: Draft concepts remain high

**Severity:** INFO
**Dimension:** Status audit

**Count:** 164 concepts

**Issue:** `status: draft` vẫn xuất hiện ở 164/334 concepts.

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

**REVISE** — không có batch-specific failure mới, nhưng backlog content-depth issues vẫn đứng yên.

## Verification

```bash
test -f "wiki/reviews/2026-06-26_output-report.md" && echo "✅ Report written"
```
