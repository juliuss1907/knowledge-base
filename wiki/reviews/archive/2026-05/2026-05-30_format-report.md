# Format Validator Report — 2026-05-30

**Validator:** Connor (Hermes-RK800)
**Scope:** Full KB scan post-Fix-Agent (55/60 sub_tags fixed)
**Total files reviewed:** ~120 concepts + sources

## Issues Found: 16

### CRITICAL — sub_tags

**6 files empty `sub_tags: []`**:
- agent-harness.md
- code-as-substrate.md
- evolutionary-mismatch.md
- factory-missions.md
- multi-agent-taxonomy.md
- plan-execute-verify-loop.md

**7 files invalid tag `tech`** (not in Pool B — use `tools`):
Concepts: ai-infrastructure-bubble, csa-hca-attention, deepseek-v4-architecture, fp4-lightning-indexer, manifold-constrained-hyper-connections, mixture-of-experts-moe
Sources: src_ai-reflexivity-loop-is-same

**1 file invalid tag `observation`** (not in Pool B):
- src_ai-trillion-dollar-blind-spot

### WARNING — Frontmatter Field Order

**2 files wrong order** (url/author before date_compiled):
- src_setup-is-not-an-edge.md
- src_no-system-will-make-you-profitable.md

Spec order: `type, original, main_tag, sub_tags, topic, date_compiled, url, author`

---

## Verdict

**REVISE** — 16 issues across format, sub_tags, and field order.

Fix list ready for Kara. Approved by Julius (via _action-required.md).