# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-05-31 — Connor validation: 16 format issues + 18 output issues + 2 hygiene issues

---

## Summary
**Pending reports:** 3 (awaiting Kara fix)

**Status:**
- ⏳ Format Validator — 2026-05-30: **PENDING APPROVAL** (16 issues: 6 empty sub_tags, 8 invalid tags, 2 field order)
- ⏳ Output Validator — 2026-05-30: **PENDING APPROVAL** (18 issues: 1 empty sources + 17 invalid status:stub)
- ⏳ Hygiene Inspector — 2026-05-30: **PENDING APPROVAL** (2 unauthorized folders: memory/, search/)
- ✅ Format Validator — 2026-05-29: APPLIED (55/60 files fixed)
- ✅ Format Validator — 2026-05-28: RESOLVED
- ✅ Output Validator — 2026-05-29: RESOLVED
- ✅ Hygiene Inspector — 2026-05-29: RESOLVED

**Resolved reports:**
- [x] Format Validator — 2026-05-14 (3 issues)
- [x] Output Validator — 2026-05-14 (4 issues)
- [x] Hygiene Inspector — 2026-05-14 (14 issues)
- [x] Format Validator — 2026-05-17 (5 issues)
- [x] Hygiene Inspector — 2026-05-17 (20 issues)
- [x] Hygiene Inspector — 2026-05-20 (6 issues)
- [x] Output Validator — 2026-05-21 (11 issues)
- [x] Format Validator — 2026-05-21 (20 issues)
- [x] Hygiene Inspector — 2026-05-21 (9 issues)
- [x] Format Validator — 2026-05-22 (11 WARNING)
- [x] Hygiene Inspector — 2026-05-22 (3 ERROR + 2 issues)
- [x] Output Validator — 2026-05-22 (16 issues)
- [x] Format Validator — 2026-05-24 (2 ERROR + 5 WARNING)
- [x] Hygiene Inspector — 2026-05-24 (1 ERROR + 1 INFO)
- [x] Output Validator — 2026-05-24 (all 20 issues)
- [x] Format Validator — 2026-05-26 (17 ERROR + 3 WARNING)
- [x] Hygiene Inspector — 2026-05-26 (2 ERROR + 2 WARNING)
- [x] Output Validator — 2026-05-26 (2 ERROR + 4 WARNING)
- [x] Output Validator — 2026-05-27 (11 issues)
- [x] Format Validator — 2026-05-27 (20 issues)
- [x] Format Validator — 2026-05-28 (7 ERROR + 14 WARNING — all fixed)
- [x] Output Validator — 2026-05-28 (1 ERROR + 3 WARNING — all fixed)
- [x] Hygiene Inspector — 2026-05-28 (32 missing concepts — by design, no fix needed)

---

---

## Critical Issues (Fix Immediately)

### ⏳ Format Validator — 2026-05-30 (16 issues)

**6 files empty `sub_tags: []`** — need 1–3 tags:
agent-harness, code-as-substrate, evolutionary-mismatch, factory-missions, multi-agent-taxonomy, plan-execute-verify-loop

**8 files invalid tag `tech`** (not in Pool B — use `tools`):
Concepts: ai-infrastructure-bubble, csa-hca-attention, deepseek-v4-architecture, fp4-lightning-indexer, manifold-constrained-hyper-connections, mixture-of-experts-moe
Sources: src_ai-reflexivity-loop-is-same

**1 file invalid tag `observation`** (not in Pool B):
src_ai-trillion-dollar-blind-spot

**2 files frontmatter field order wrong** (`url`/`author` before `date_compiled`):
src_setup-is-not-an-edge, src_no-system-will-make-you-profitable

---

### ⏳ Output Validator — 2026-05-30 (18 issues)

**1 file empty `sources: []`**:
second-order-effects.md

**17 files invalid `status: stub`** (spec requires: draft|reviewed|needs-revision):
agent-handoff, orchestrator-worker-validator, fast-weights, strait-of-hormuz-geopolitics, american-security-guarantee, hippocampal-replay, agent-journal-pattern, uae-saudi-rivalry, spare-production-capacity, gated-delta-networks, multi-agent-risk-review, state-space-models-ssm, alpaca-api, kv-cache-eviction, kinked-demand-curve, claude-code-routines, paper-trading

---

### ⏳ Hygiene Inspector — 2026-05-30 (2 issues)

**2 unauthorized folders at root level — OUTSIDE Kara's scope** (per SKILL.md: root-level items belong to Julius):
- `memory/` — legacy folder, belongs to Julius
- `search/` — not in allowed list, belongs to Julius

---

## Warnings (Can Fix Later)

*None currently pending*

---

## Systematic Issues (No File-Level Fix — SKIP)

*None*

---

## Commands

**To approve a report:**
approve output
approve format
approve hygiene

**To view full report:**
show output
show format
show hygiene

**To apply approved fixes:**
openclaw fix apply
