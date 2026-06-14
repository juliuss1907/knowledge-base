# Action Required — Pending Reports

> Consolidated list of pending Hermes validation reports
> Updated automatically after each validation run
> Julius reviews this file to approve/reject fixes

**Last updated:** 2026-06-14 — Validation complete, pending Julius approval.

---

## Summary

**Pending approved fixes:** 0

**Status:**
- ⏳ Format Validator — 2026-06-14: **PENDING APPROVAL** (18 issues: 6 YAML parse errors, 5 invalid main_tag=psychology, 1 missing topic, 4 original wikilink with .md extension)
- ⏳ Output Validator — 2026-06-14: **PENDING APPROVAL** (16 issues: 14 missing Key ideas sections, 1 empty Sources, 1 short Summary)
- ✅ Hygiene Inspector — 2026-06-14: **PROMOTE** (2 orphan sources, non-critical)
- ✅ Format Validator — 2026-06-12: **APPLIED + VERIFIED** (0 invalid sub_tags remaining)
- ✅ Output Validator — 2026-06-12: **APPLIED PARTIAL + VERIFIED**
  - ✅ Sources trống: **2 concepts fixed; 0 empty Sources remaining**
  - ✅ Key ideas <3: **reviewed; only `retail-trading-fantasy.md` required expansion and was fixed**
  - ⏭️ Summary 1 dòng: **IGNORED by Julius**
  - ⏸️ Status draft: **not approved in this pass**
- ✅ Hygiene Inspector — 2026-06-12: **PROMOTE** (0 issues)
- ✅ Format Validator — 2026-06-06: APPLIED (6 files)
- ✅ Output Validator — 2026-06-06: APPROVED
- ✅ Hygiene Inspector — 2026-06-06: PROMOTE
- ✅ Format Validator — 2026-06-03: APPLIED (5 files)
- ✅ Output Validator — 2026-06-03: APPROVED
- ✅ Hygiene Inspector — 2026-06-03: PROMOTE

---

## Verification — 2026-06-12

### ✅ Format Validator

Scan result:
- Invalid sub_tags: **0**
- Empty sub_tags: **0**

The previously approved `system` → `research` fixes are complete.

---

### ✅ Sources trống

Scan result:
- Concepts with empty `## Sources`: **0**

The previously empty sources in:
- `ai-powered-discovery.md`
- `second-order-effects.md`

are now fixed.

---

### ✅ Key ideas <3

Fix Agent review result accepted:
- Most flagged files were false positives because they use structured subsections (`###`) instead of bullet-only `## Key ideas` lists.
- Only `retail-trading-fantasy.md` was genuinely underdeveloped.
- `retail-trading-fantasy.md` was expanded from 2 to 5 bullet points using source notes.

Validator note: bullet-count-only detection still flags some subsection-style files, but this is not treated as an actionable issue in this pass.

---

## Explicitly Ignored

### ⏭️ Summary 1 dòng

Julius explicitly chose to ignore this issue for now.

**Do not fix in this pass:**
- Summary 1 dòng across the wiki
- No re-compile required solely for Summary length

---

## Not Approved In This Pass

### ⏸️ Status draft

Latest validation found draft files. Julius did not approve this item in the current instruction. Leave unchanged unless separately approved.

---

## Critical Issues (Fix Immediately) — 2026-06-14

### ⏳ Format Validator — 2026-06-14 (18 issues)

**YAML parse errors — 6 files:**
`agent-harness.md`, `code-as-substrate.md`, `evolutionary-mismatch.md`, `factory-missions.md`, `multi-agent-taxonomy.md`, `plan-execute-verify-loop.md`
- Issue: `sub_tags` defined twice (inline array + block list)
- Fix: Remove duplicate block list, keep inline array only

**Invalid main_tag = `psychology` — 5 files:**
- Concepts: `activation-energy.md`, `hypergamy.md`, `relationship-dynamics.md`
- Sources: `src_activation-energy.md`, `src_hypergamy.md`
- Issue: `psychology` is Pool B (sub-tag), not Pool A (main-tag)
- Fix: Change main_tag to `productivity` (behavioral/mental-model content)

**Missing `topic` field — 1 file:**
- `active-thinking.md`
- Fix: Add `topic` field to frontmatter

**Original wikilink has `.md` extension — 4 source files:**
- `src_code-as-agent-harness-arxiv-2605-18747.md`
- `src_how-to-read-cash-flow-statement.md`
- `src_japanese-evening-routine-fix-sleep.md`
- `src_luke-alvoeiro-multi-agent-architecture-factory.md`
- Fix: Remove `.md` from `original` wikilink

### ⏳ Output Validator — 2026-06-14 (16 issues)

**Missing `## Key ideas` section — 14 concepts:**
`csa-hca-attention.md`, `deepseek-v4-flash-vs-pro.md`, `dollar-as-rent-payment.md`, `existential-vacuum.md`, `false-reinforcement-loop.md`, `fp4-lightning-indexer.md`, `kissinger-deal-1974.md`, `long-context-models.md`, `mixture-of-experts-moe.md`, `petrodollar-system.md`, `policy-review-framework.md`, `saudi-pakistan-defense-agreement.md`, `tragic-optimism.md`, `us-security-umbrella.md`
- Fix: Add `## Key ideas` with 2+ bullet points

**Sources section nearly empty — 1 concept:**
- `inversion.md`
- Fix: Add context to Sources section

**Summary too short — 1 source:**
- `src_viktor-frankl-meaning-video.md`
- Fix: Expand Summary to 2+ sentences

---

## Commands

**To apply approved fixes:**
```bash
openclaw fix apply
```
