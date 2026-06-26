# Hygiene Inspection — 2026-06-26

**Status:** pending
**Issues found:** 1 actionable (1 ERROR, 0 WARNING)
**Created:** 2026-06-26 07:01:00 +07
**Validator:** hygiene-inspector

**Paths checked:** 30

> **Scope note:** Raw script reported 2 findings. `memory/` at repo root is excluded from Kara scope and is not counted as an actionable hygiene issue in this report.

---

## Delta vs most recent approved hygiene report

Reference baseline: approved/applied Hygiene Inspector run dated `2026-06-25 15:53`.

| Metric | Current run | Previous approved | Delta |
|---|---:|---:|---:|
| Raw script findings | 2 | 4 | -2 |
| Actionable issues | 1 | 3 | -2 |
| ERROR | 1 | 2 | -1 |
| WARNING | 0 | 1 | -1 |
| Excluded false positives | 1 | 1 | 0 |

**Positive delta:** `state/` đã biến mất. `.last-heartbeat` cũng đã được dọn.
**Remaining issue:** `wiki/reviews/HEARTBEAT.md` vẫn nằm sai zone.

---

## Issue 1: `wiki/reviews/HEARTBEAT.md` leaked into review zone

**Path:** `wiki/reviews/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Path

**Issue:** Heartbeat artifact đang nằm trong `wiki/reviews/`, nơi chỉ nên chứa validator reports.

---

## Excluded by Scope

### `memory/` at repo root

**Raw script severity:** ERROR
**Reason excluded:** Root-level `memory/` thuộc Julius-side environment, không phải Kara cleanup scope.

---

## Summary

| Category | Count |
|---|---:|
| ERROR | 1 |
| WARNING | 0 |
| INFO | 0 |
| Excluded false positives | 1 |

## Verdict

**REVISE** — 1 hygiene error thực còn lại. Hai issue từ baseline trước đã được resolve.

## Verification

```bash
test -f "wiki/reviews/2026-06-26_hygiene-report.md" && echo "✅ Report written"
```
