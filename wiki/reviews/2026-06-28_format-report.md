# Format Validation — 2026-06-28

**Status:** pending
**Issues found:** 442 (127 ERROR, 315 WARNING, 0 INFO)
**Created:** 2026-06-28 23:15:44 +0700
**Validator:** format-validator
**Scope:** Full KB — 623 files (354 concepts + 110 sources + 33 indexes + 126 topics)

---

## Delta from last approved (2026-06-26 23:15)

| Metric | 2026-06-26 (APPROVED) | 2026-06-28 | Delta |
|---|---|---|---|
| Scope | concepts + sources only (436 files) | Full KB (623 files) | +187 |
| ERROR | 4 | 127 | **+123** |
| WARNING | 310 | 315 | +5 |
| INFO | 0 | 0 | 0 |

**Positive delta (issues resolved):**
- ✅ 8 code-block language-tag ERRORs → **GONE** (resolved by Fix Agent from 06-26 report)

**Negative delta (new issues):**
- 🔴 **126 new ERROR**: `wiki/topic/*.md` — all topic files missing YAML frontmatter (systematic Index Agent issue)
- 🔴 1 new ERROR: Slug exceeds 50 chars (returned from prior report, not yet fixed)
- ⚠️ +5 WARNING (net change in broken wikilinks across expanded scope)

---

## [SYSTEMATIC VIOLATION] Topic files missing frontmatter

**Pattern:** 126/126 topic files under `wiki/topic/` have no YAML frontmatter
**Likely cause:** Index Agent generates topic files starting with `# Topic: <slug>` H1 instead of `---` frontmatter block
**Recommendation:** Update `index-agent/SKILL.md` to include required frontmatter for topic files

**Required frontmatter for topic files:**
```yaml
---
type: index
scope: topic
auto_generated: true
last_updated: YYYY-MM-DD
---
```

**Affected files (all 126):**

| # | File |
|---|---|
| 1 | `wiki/topic/activation-energy-mental-model.md` |
| 2 | `wiki/topic/active-thinking-methodology.md` |
| 3 | `wiki/topic/active-thinking.md` |
| 4 | `wiki/topic/agent-memory-systems.md` |
| 5 | `wiki/topic/ai-architecture.md` |
| 6 | `wiki/topic/ai-business-criticism.md` |
| 7 | `wiki/topic/ai-coding-context-handoff.md` |
| 8 | `wiki/topic/ai-economic-disruption-white-collar.md` |
| 9 | `wiki/topic/ai-engineering.md` |
| 10 | `wiki/topic/ai-first-business.md` |
| 11 | `wiki/topic/ai-funding-dynamics.md` |
| 12 | `wiki/topic/ai-future-skills.md` |
| 13 | `wiki/topic/ai-lab-valuation-dynamics.md` |
| 14 | `wiki/topic/ai-landing-page-discovery.md` |
| 15 | `wiki/topic/ai-legal-personhood.md` |
| 16 | `wiki/topic/ai-overviews.md` |
| 17 | `wiki/topic/ai-productivity.md` |
| 18 | `wiki/topic/ai-reflexivity-2026.md` |
| 19 | `wiki/topic/ai-security-vulnerability-research.md` |
| 20 | `wiki/topic/ai-systems-thinking-augmentation.md` |
| 21 | `wiki/topic/ai-trading-agent-claude-code.md` |
| 22 | `wiki/topic/ai-vulnerability-discovery.md` |
| 23 | `wiki/topic/ai-workflow-methodology.md` |
| 24 | `wiki/topic/brain-health-habits.md` |
| 25 | `wiki/topic/brain-health.md` |
| 26 | `wiki/topic/career-advice-ai-age.md` |
| 27 | `wiki/topic/code-as-agent-harness.md` |
| 28 | `wiki/topic/compounding-growth.md` |
| 29 | `wiki/topic/coordinated-vulnerability-disclosure.md` |
| 30 | `wiki/topic/counterinsurgency-warfare.md` |
| 31 | `wiki/topic/critical-thinking-tools.md` |
| 32 | `wiki/topic/dan-koe-mind-game.md` |
| 33 | `wiki/topic/deepseek-v4-architecture.md` |
| 34 | `wiki/topic/discipline-and-spontaneity.md` |
| 35 | `wiki/topic/embodied-knowledge.md` |
| 36 | `wiki/topic/evolutionary-mismatch-modern-life.md` |
| 37 | `wiki/topic/experience-over-achievement.md` |
| 38 | `wiki/topic/factory-missions-architecture.md` |
| 39 | `wiki/topic/financial-statement-analysis.md` |
| 40 | `wiki/topic/game-theory-strategic-thinking.md` |
| 41 | `wiki/topic/gamification-design-patterns.md` |
| 42 | `wiki/topic/generative-ai-search-optimization.md` |
| 43 | `wiki/topic/generative-ai-seo.md` |
| 44 | `wiki/topic/generative-search-results.md` |
| 45 | `wiki/topic/geo-strategy.md` |
| 46 | `wiki/topic/github-supply-chain-attack-vs-code.md` |
| 47 | `wiki/topic/global-macro-investing.md` |
| 48 | `wiki/topic/google-ai-mode.md` |
| 49 | `wiki/topic/google-ai-search-optimization.md` |
| 50 | `wiki/topic/hermes-operator-builder-pattern.md` |
| 51 | `wiki/topic/hermes-personal-analyst-setup.md` |
| 52 | `wiki/topic/hermes-polymarket-trading-agent.md` |
| 53 | `wiki/topic/hermes-top-skills-analysis.md` |
| 54 | `wiki/topic/hermes-workflow-optimization.md` |
| 55 | `wiki/topic/hermes-xai-grok-integration.md` |
| 56 | `wiki/topic/hermes-xurl-x-api-integration.md` |
| 57 | `wiki/topic/hypergamy-relationships.md` |
| 58 | `wiki/topic/ikigai-unbundling.md` |
| 59 | `wiki/topic/incentives-psychology.md` |
| 60 | `wiki/topic/investment-principles.md` |
| 61 | `wiki/topic/job-evaluation-framework.md` |
| 62 | `wiki/topic/job-worth-doing.md` |
| 63 | `wiki/topic/journalism-ai-era.md` |
| 64 | `wiki/topic/leader-leader-leadership.md` |
| 65 | `wiki/topic/leverage-mental-model.md` |
| 66 | `wiki/topic/llm-capabilities.md` |
| 67 | `wiki/topic/llm-memory-consolidation.md` |
| 68 | `wiki/topic/long-term-thinking.md` |
| 69 | `wiki/topic/loop-native-factory.md` |
| 70 | `wiki/topic/market-cycles.md` |
| 71 | `wiki/topic/market-dynamics.md` |
| 72 | `wiki/topic/market-psychology.md` |
| 73 | `wiki/topic/market-structure-analysis.md` |
| 74 | `wiki/topic/market-structure.md` |
| 75 | `wiki/topic/meaning-life-purpose.md` |
| 76 | `wiki/topic/mental-models-art.md` |
| 77 | `wiki/topic/mental-models-biology.md` |
| 78 | `wiki/topic/mental-models-economics.md` |
| 79 | `wiki/topic/mental-models-feedback.md` |
| 80 | `wiki/topic/mental-models-latticework.md` |
| 81 | `wiki/topic/mental-models-systems.md` |
| 82 | `wiki/topic/mental-models.md` |
| 83 | `wiki/topic/multi-agent-architecture.md` |
| 84 | `wiki/topic/nuclear-deterrence.md` |
| 85 | `wiki/topic/personal-finance-saving-rate.md` |
| 86 | `wiki/topic/personal-finance.md` |
| 87 | `wiki/topic/personal-systems.md` |
| 88 | `wiki/topic/petrodollar-collapse.md` |
| 89 | `wiki/topic/post-systems-thinking.md` |
| 90 | `wiki/topic/prices-law.md` |
| 91 | `wiki/topic/procrastination-neuroscience.md` |
| 92 | `wiki/topic/responsible-ai-security-research.md` |
| 93 | `wiki/topic/retrieval-augmented-generation.md` |
| 94 | `wiki/topic/saudi-defense-diversification.md` |
| 95 | `wiki/topic/seed-vs-machine-architecture.md` |
| 96 | `wiki/topic/self-discovery-serendipity.md` |
| 97 | `wiki/topic/simplicity-psychology.md` |
| 98 | `wiki/topic/skill-acquisition.md` |
| 99 | `wiki/topic/sleep-hygiene.md` |
| 100 | `wiki/topic/sop-writer.md` |
| 101 | `wiki/topic/speed-vs-velocity-productivity.md` |
| 102 | `wiki/topic/sso-security-risks.md` |
| 103 | `wiki/topic/state-capacity-development.md` |
| 104 | `wiki/topic/structural-competition.md` |
| 105 | `wiki/topic/system-dynamics.md` |
| 106 | `wiki/topic/systematic-trading-transition.md` |
| 107 | `wiki/topic/systems-thinking-cognitive-development.md` |
| 108 | `wiki/topic/systems-thinking-leadership.md` |
| 109 | `wiki/topic/systems-thinking-tools.md` |
| 110 | `wiki/topic/systems-thinking-training.md` |
| 111 | `wiki/topic/systems-thinking-types.md` |
| 112 | `wiki/topic/tacit-knowledge.md` |
| 113 | `wiki/topic/tokenization-llm.md` |
| 114 | `wiki/topic/trading-education.md` |
| 115 | `wiki/topic/trading-heater-rule.md` |
| 116 | `wiki/topic/trading-methodology.md` |
| 117 | `wiki/topic/trading-policy-implementation.md` |
| 118 | `wiki/topic/trading-process.md` |
| 119 | `wiki/topic/trading-psychology.md` |
| 120 | `wiki/topic/trading-risk-management.md` |
| 121 | `wiki/topic/trading-state-policy.md` |
| 122 | `wiki/topic/trading-timing.md` |
| 123 | `wiki/topic/tribute-system-world-order.md` |
| 124 | `wiki/topic/uae-opec-exit-geopolitics.md` |
| 125 | `wiki/topic/us-saudi-relations.md` |
| 126 | `wiki/topic/vietnam-unemployment-insurance.md` |

---

## Individual ERRORs (non-systemic)

---

### Issue 1: Source slug exceeds 50 characters

**File:** `wiki/sources/src_give-me-14-minutes-and-ill-destroy-your-procrastination-forever.md`
**Severity:** ERROR
**Category:** Naming
**Issue:** Source slug exceeds 50-character limit (63 chars after `src_` prefix)
**Current:** `give-me-14-minutes-and-ill-destroy-your-procrastination-forever` (63 chars)
**Expected:** Slug ≤ 50 chars (after `src_` prefix)
**Suggested fix:** Shorten to `give-me-14-minutes-destroy-procrastination` (42 chars) or similar. Update filename and all backlinks.

---

## WARNING summary

**315 WARNINGs — breakdown:**

| Category | Count | Description |
|---|---|---|
| Broken wikilinks | 290 | Forward-references to uncompiled concepts (expected in growing KB) |
| Original wikilink not found | 4 | `original` field points to raw file that doesn't exist |
| Field order mismatch | ~20 | Frontmatter field order doesn't match spec |
| Other | ~1 | Miscellaneous |

### Top broken wikilink targets (most-referenced, uncompiled concepts)

These 194 unique targets account for 290 occurrences. Top targets:

| Count | Target |
|---|---|
| 10x | `game-theory` |
| 8x | `confirmation-bias` |
| 6x | `pareto-principle` |
| 5x | `ai-coding-agents` |
| 5x | `career-design` |
| 5x | `decision-making` |
| 4x | `deep-work` |
| 3x | `ai-hype-vs-reality`, `economic-inequality`, `critical-thinking`, `naval-ravikant`, `risk-parity`, `second-law-of-thermodynamics`, `saying-no`, `power-imbalance`, `first-order-thinking` |

These are forward-references to concepts not yet compiled. No action needed now — they will resolve as the KB grows.

---

## Escalation

### [SYSTEMATIC VIOLATION] Index Agent not generating frontmatter for topic files

```
[SYSTEMATIC VIOLATION]
Pattern: 126/126 topic files under wiki/topic/ have no YAML frontmatter
Likely cause: Index Agent generates topic files without frontmatter block
Required: type, scope, auto_generated, last_updated fields per format-spec.md
Recommendation: Update openclaw/skills/index-agent/SKILL.md to include
  YAML frontmatter block in topic file template
```

---

## Post-validation summary

- **Files checked:** 623 (354 concepts + 110 sources + 33 indexes + 126 topics)
- **126/127 ERRORs are systemic** (topic files missing frontmatter → single root cause)
- **1 ERROR is a single-file fix** (slug too long → rename file + update backlinks)
- **315 WARNINGs are forward-references** (broken wikilinks → expected in growing KB, no action needed)
- **Actionable for Julius:** Decide whether to fix Index Agent SKILL.md for topic file frontmatter, and approve the single source file rename
