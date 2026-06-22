# Format Validator Report — 2026-06-22

**Validator:** Connor (Hermes-RK800)
**Status:** approved
**Approved by:** Julius
**Created:** 2026-06-22 08:20
**Scope:** 563 files (324 concepts + 99 sources + 31 indexes + 109 topics)

---

## Issues Found: 450 (132 ERROR, 318 WARNING, 0 INFO)

---

### 🔴 ERROR — Topic Files Missing Frontmatter (109 files)

**Severity:** ERROR
**Category:** Frontmatter
**Pattern:** All 109 files under `wiki/topic/*.md` have no YAML frontmatter at all.

**[SYSTEMATIC VIOLATION]** Index Agent generates topic files without frontmatter. This was flagged in 06-19 and remains unfixed.

**Files affected:** 109
```
wiki/topic/activation-energy-mental-model.md
wiki/topic/active-thinking.md
wiki/topic/active-thinking-methodology.md
wiki/topic/agent-memory-systems.md
wiki/topic/ai-architecture.md
wiki/topic/ai-business-criticism.md
wiki/topic/ai-coding-context-handoff.md
wiki/topic/ai-economic-disruption-white-collar.md
wiki/topic/ai-engineering.md
wiki/topic/ai-first-business.md
wiki/topic/ai-funding-dynamics.md
wiki/topic/ai-lab-valuation-dynamics.md
wiki/topic/ai-landing-page-discovery.md
wiki/topic/ai-legal-personhood.md
wiki/topic/ai-overviews.md
wiki/topic/ai-productivity.md
wiki/topic/ai-reflexivity-2026.md
wiki/topic/ai-security-vulnerability-research.md
wiki/topic/ai-systems-thinking-augmentation.md
wiki/topic/ai-trading-agent-claude-code.md
wiki/topic/ai-vulnerability-discovery.md
wiki/topic/ai-workflow-methodology.md
wiki/topic/brain-health.md
wiki/topic/brain-health-habits.md
wiki/topic/career-advice-ai-age.md
wiki/topic/code-as-agent-harness.md
wiki/topic/compounding-growth.md
wiki/topic/coordinated-vulnerability-disclosure.md
wiki/topic/counterinsurgency-warfare.md
wiki/topic/dan-koe-mind-game.md
wiki/topic/deepseek-v4-architecture.md
wiki/topic/discipline-and-spontaneity.md
wiki/topic/embodied-knowledge.md
wiki/topic/evolutionary-mismatch-modern-life.md
wiki/topic/factory-missions-architecture.md
wiki/topic/financial-statement-analysis.md
wiki/topic/generative-ai-search-optimization.md
wiki/topic/generative-ai-seo.md
wiki/topic/generative-search-results.md
wiki/topic/geo-strategy.md
wiki/topic/github-supply-chain-attack-vs-code.md
wiki/topic/google-ai-mode.md
wiki/topic/google-ai-search-optimization.md
wiki/topic/hermes-operator-builder-pattern.md
wiki/topic/hermes-personal-analyst-setup.md
wiki/topic/hermes-polymarket-trading-agent.md
wiki/topic/hermes-top-skills-analysis.md
wiki/topic/hermes-workflow-optimization.md
wiki/topic/hermes-xai-grok-integration.md
wiki/topic/hermes-xurl-x-api-integration.md
wiki/topic/hypergamy-relationships.md
wiki/topic/ikigai-unbundling.md
wiki/topic/incentives-psychology.md
wiki/topic/job-evaluation-framework.md
wiki/topic/job-worth-doing.md
wiki/topic/leader-leader-leadership.md
wiki/topic/leverage-mental-model.md
wiki/topic/llm-capabilities.md
wiki/topic/llm-memory-consolidation.md
wiki/topic/loop-native-factory.md
wiki/topic/market-cycles.md
wiki/topic/market-dynamics.md
wiki/topic/market-psychology.md
wiki/topic/market-structure.md
wiki/topic/market-structure-analysis.md
wiki/topic/meaning-life-purpose.md
wiki/topic/mental-models.md
wiki/topic/mental-models-art.md
wiki/topic/mental-models-biology.md
wiki/topic/mental-models-economics.md
wiki/topic/mental-models-feedback.md
wiki/topic/mental-models-latticework.md
wiki/topic/mental-models-systems.md
wiki/topic/multi-agent-architecture.md
wiki/topic/nuclear-deterrence.md
wiki/topic/personal-finance.md
wiki/topic/personal-finance-saving-rate.md
wiki/topic/personal-systems.md
wiki/topic/petrodollar-collapse.md
wiki/topic/post-systems-thinking.md
wiki/topic/responsible-ai-security-research.md
wiki/topic/retrieval-augmented-generation.md
wiki/topic/saudi-defense-diversification.md
wiki/topic/seed-vs-machine-architecture.md
wiki/topic/simplicity-psychology.md
wiki/topic/sleep-hygiene.md
wiki/topic/speed-vs-velocity-productivity.md
wiki/topic/sso-security-risks.md
wiki/topic/structural-competition.md
wiki/topic/system-dynamics.md
wiki/topic/systematic-trading-transition.md
wiki/topic/systems-thinking-cognitive-development.md
wiki/topic/systems-thinking-leadership.md
wiki/topic/systems-thinking-tools.md
wiki/topic/systems-thinking-training.md
wiki/topic/systems-thinking-types.md
wiki/topic/tacit-knowledge.md
wiki/topic/tokenization-llm.md
wiki/topic/trading-education.md
wiki/topic/trading-heater-rule.md
wiki/topic/trading-methodology.md
wiki/topic/trading-policy-implementation.md
wiki/topic/trading-process.md
wiki/topic/trading-psychology.md
wiki/topic/trading-risk-management.md
wiki/topic/trading-state-policy.md
wiki/topic/uae-opec-exit-geopolitics.md
wiki/topic/us-saudi-relations.md
wiki/topic/vietnam-unemployment-insurance.md
```

**Suggested fix:** Update Index Agent to add YAML frontmatter to topic files (type: index, scope: topic, topic: <slug>, auto_generated: true, last_updated: <date>).

---

### 🔴 ERROR — main_tag `psychology` (Pool B only, 11 files)

**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `psychology` is in Pool B (sub-tag only per TAGS.md), used as main_tag.

**Concepts (9 files):**
- wiki/concepts/collaborative-thinking.md
- wiki/concepts/meaning-through-work.md
- wiki/concepts/nash-equilibrium.md
- wiki/concepts/occams-broom.md
- wiki/concepts/occams-razor.md
- wiki/concepts/prisoners-dilemma.md
- wiki/concepts/repeated-games.md
- wiki/concepts/ultimatum-game.md
- wiki/concepts/zero-sum-game.md

**Sources (2 files):**
- wiki/sources/src_critical-thinking-dennett.md
- wiki/sources/src_game-theory-will-change-your-life.md

**Suggested fix:** Change main_tag to `productivity` (behavioral/mental-model content) or propose `psychology` → Pool A to Julius.

---

### 🔴 ERROR — Code Blocks Missing Language Tags (8 files)

**Severity:** ERROR
**Category:** Markdown

**Files:**
- wiki/concepts/ai-coach-prompting.md
- wiki/concepts/content-generation-workflow.md
- wiki/concepts/dollar-as-rent-payment.md
- wiki/concepts/existential-vacuum.md
- wiki/concepts/expert-knowledge-extraction.md
- wiki/concepts/trading-addiction-cycle.md
- wiki/concepts/x-search-tool.md
- wiki/sources/src_petrodollar-system-analysis.md

---

### 🔴 ERROR — wiki/tag/tag.md Missing Fields (4 issues)

**Severity:** ERROR
**Category:** Frontmatter / Sections

1. Missing required field: `parent`
2. Missing required field: `items_managed_by`
3. `items_managed_by` should be `ingest-agent` or `index-agent`
4. Missing required section: `## Parent`

---

### 🟡 WARNING — Broken Wikilinks (272 instances)

**Severity:** WARNING
**Category:** Markdown
**Pattern:** Forward-references to concepts not yet compiled — expected in a growing KB.

Top affected concepts: `probabilistic-thinking` (5), `collaborative-thinking` (5), `vibe-coding` (4), `occams-razor` (4), `systematic-trading` (4).

**Note:** Not individual errors. Systemic forward-referencing behavior. Flagged as single aggregate warning.

---

### 🟡 WARNING — Unquoted Wikilinks in Tag Files (21 files)

**[SPEC CONFLICT]** Tag index files have `parent: [[tag]]` (unquoted) which YAML parses as nested list. format-spec.md §9 requires quoted `"[[tag]]"`.

**Files:** wiki/tag/{ai,automation,coding,crypto,defi,economic,hack,health,investment,law,layer1,layer2,news,opinion,perpdex,politic,productivity,psychology,research,system,tech,tools,tutorial,vibecode}.md

---

### 🟡 WARNING — Other (2 files)

- wiki/sources/src_dan-koe-workflow-analysis-markus.md — Field order mismatch
- wiki/sources/src_map-is-not-territory.md — `original` wikilink `[[2026-06-03_map-is-not-territory]]` points to non-existent raw file

---

### ✅ Passing

- 324 concepts: all required frontmatter fields present, YAML syntax valid
- 99 sources: all required frontmatter fields present
- 31 index files: compliant with index-spec.md
- No duplicate YAML sub_tags detected
- No `.md` extension in source `original` fields
- No `stub` status values
- Field order consistent across concepts

---

## Verdict

**REVISE** — 132 ERROR, 318 WARNING.

Key systemic issues:
1. **109 topic files without frontmatter** — Index Agent config needs update (carry-over from 06-19)
2. **11 files with main_tag `psychology`** — new batch of game-theory/psychology concepts with wrong Pool assignment
3. **21 unquoted wikilinks** — same SPEC CONFLICT since 06-17

Actionable individual fixes: 8 code block lang tags, 4 wiki/tag/tag.md fields.
