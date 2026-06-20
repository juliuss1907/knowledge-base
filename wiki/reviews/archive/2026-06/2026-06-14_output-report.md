# Output Validator Report — 2026-06-14

**Validator:** Connor (Hermes-RK800)
**Scope:** wiki/concepts/ + wiki/sources/
**Total files reviewed:** 364 (282 concepts + 82 sources)

## Issues Found: 16

### CRITICAL — Missing Key ideas section (concepts)

**14 concept files affected:**
- `csa-hca-attention.md`
- `deepseek-v4-flash-vs-pro.md`
- `dollar-as-rent-payment.md`
- `existential-vacuum.md`
- `false-reinforcement-loop.md`
- `fp4-lightning-indexer.md`
- `kissinger-deal-1974.md`
- `long-context-models.md`
- `mixture-of-experts-moe.md`
- `petrodollar-system.md`
- `policy-review-framework.md`
- `saudi-pakistan-defense-agreement.md`
- `tragic-optimism.md`
- `us-security-umbrella.md`

**Pattern:** All files have `## Definition` and `## Sources` but skip `## Key ideas`. This is a Compile Agent section omission.

**Fix:** Add `## Key ideas` section with 2+ bullet points extracted from source content.

### WARNING — Sources section nearly empty

**1 concept file affected:**
- `inversion.md` — `## Sources` section contains only a wikilink with no context

**Fix:** Ensure Sources section has meaningful content (not just a bare link).

### WARNING — Summary too short (source file)

**1 source file affected:**
- `src_viktor-frankl-meaning-video.md` — `## Summary` contains only 1 sentence

**Fix:** Expand Summary to 2+ sentences per format-spec.

---

## ✅ Passing

- 268/282 concepts have all required sections (Definition, Key ideas, Related concepts, Sources)
- 81/82 sources have all required sections (Metadata, Summary, Key points, Concepts referenced)
- All Definition sections have sufficient length (>30 chars)
- All Key ideas sections with bullets have ≥2 items (except the 14 missing ones)
- All Sources sections are populated (except 1 nearly empty)

---

## Verdict

**REVISE** — 16 issues across 15 files. 14 missing Key ideas sections are the bulk of the work. Fixable by Fix Agent.


---
**Status:** applied
**Applied at:** 2026-06-15 14:31
**Applied by:** fix-agent

