# Format Validation Report — 2026-05-28

> Format-Validator scan against format-spec.md v2.2 (updated 2026-05-26)
> Wikilinks in frontmatter fields `original:` and `sources:` must use quoted format `"[[...]]"`

**Scan date:** 2026-05-28 09:47
**Files checked:** 80 (30 sources + 50 concepts)
**Issues found:** 80 (all ERROR)

---

## Summary

| Severity | Count | Description |
|----------|-------|-------------|
| **ERROR** | 80 | Wikilink in frontmatter not quoted |
| WARNING | 0 | — |
| INFO | 0 | — |

---

## Issue Details

### Source files — `original:` field

29 source files have `original:` wikilinks that are **not quoted**.

**Expected:** `original: "[[...]]"`
**Found:** `original: [[...]]`

| # | File | Current value |
|---|------|---------------|
| 1 | `sources/src_google-generative-ai-search-guide.md` | `original: [[2026-05-23_google-publishes-generative-ai-search-guide-semrush]]` |
| 2 | `sources/src_will-ai-replace-systems-thinking.md` | `original: [[2026-05-25_will-ai-replace-systems-thinking]]` |
| 3 | `sources/src_dont-sign-in-with-google.md` | `original: [[2026-05-19_dont-sign-in-with-google]]` |
| 4 | `sources/src_project-glasswing-update.md` | `original: [[2026-05-23_project-glasswing-anthropic-initial-update]]` |
| 5 | `sources/src_code-as-agent-harness-arxiv-2605-18747.md` | `original: [[2026-05-22_code-as-agent-harness-arxiv-2605-18747.md]]` |
| 6 | `sources/src_11-minutes-hack-github.md` | `original: [[2026-05-20_the-smart-ape-11-minutes-hack-github]]` |
| 7 | `sources/src_hermes-analyst-workflow-essentials.md` | `original: [[2026-05-18_hermes-analyst-workflow-essentials]]` |
| 8 | `sources/src_how-ai-productivity-fails.md` | `original: [[2026-05-14_how-ai-productivity-fails]]` |
| 9 | `sources/src_google-guide-optimizing-generative-ai-search.md` | `original: [[2026-05-18_google-guide-optimizing-generative-ai-search]]` |
| 10 | `sources/src_aaron-wright-ai-agents-legal-body.md` | `original: [[2026-05-17_aaron-wright-ai-agents-legal-body]]` |
| 11 | `sources/src_build-ai-trading-agent-claude-code-alpaca.md` | `original: [[2026-05-27_build-ai-trading-agent-claude-code-alpaca]]` |
| 12 | `sources/src_hermes-200-30-skills-3-worth-it.md` | `original: [[2026-05-18_hermes-200-30-skills-3-worth-it]]` |
| 13 | `sources/src_llm-need-sleep-consolidation.md` | `original: [[2026-05-27_llm-need-sleep-consolidation]]` |
| 14 | `sources/src_1-month-with-hermes-ive-been-using-wrong.md` | `original: [[2026-05-18_1-month-with-hermes-ive-been-using-wrong]]` |
| 15 | `sources/src_luke-alvoeiro-multi-agent-architecture-factory.md` | `original: [[2026-05-22_luke-alvoeiro-multi-agent-architecture-factory.md]]` |
| 16 | `sources/src_3-things-learnt-3-weeks-hermes-analyst.md` | `original: [[2026-05-18_3-things-learnt-3-weeks-hermes-analyst]]` |
| 17 | `sources/src_why-we-complicate-life-productive-peter.md` | `original: [[2026-05-26_why-we-complicate-life-productive-peter]]` |
| 18 | `sources/src_agent-memory-anatomy.md` | `original: [[2026-05-27_agent-memory-anatomy]]` |
| 19 | `sources/src_how-some-people-become-unrecognizable.md` | `original: [[2026-05-14_how-some-people-become-unrecognizable]]` |
| 20 | `sources/src_hermes-as-a-real-time-analyst.md` | `original: [[2026-05-18_hermes-as-a-real-time-analyst]]` |
| 21 | `sources/src_uae-opec-exit-end-of-era.md` | `original: [[2026-05-27_uae-opec-exit-end-of-era]]` |
| 22 | `sources/src_generative-ai-search-optimization.md` | `original: [[2026-05-23_optimize-content-generative-ai-search-sagepath]]` |
| 23 | `sources/src_were-not-supposed-to-live-like-this.md` | `original: [[2026-05-20_juliachristina-were-not-supposed-to-live-like-this]]` |
| 24 | `sources/src_the-revenge-of-the-business-idiot.md` | `original: [[2026-05-27_the-revenge-of-the-business-idiot]]` |
| 25 | `sources/src_ai-trillion-dollar-blind-spot.md` | `original: [[2026-05-25_suyash-karn-ai-trillion-dollar-blind-spot-static-website]]` |
| 26 | `sources/src_ai-will-destroy-world-economy.md` | `original: [[2026-05-20_the-smart-ape-ai-destroy-world-economy]]` |
| 27 | `sources/src_active-vs-lazy-thinking.md` | `original: [[2026-05-12_active-vs-lazy-thinking]]` |
| 28 | `sources/src_hermes-polymarket-btc-trading-agent.md` | `original: [[2026-05-20_0xmovez-hermes-polymarket-btc-trading-agent]]` |
| 29 | `sources/src_what-comes-after-systems-thinking.md` | `original: [[2026-04-02_what-comes-after-systems-thinking]]` |

**Compliant file (1):** `sources/src_hermes-xurl-skill-guide.md` — already uses quoted format

---

### Concept files — `sources:` field

All 50 concept files have `sources:` array wikilinks that are **not quoted**.

**Expected:** `sources:\n  - "[[src_slug]]"`
**Found:** `sources:\n  - [[src_slug]]`

| # | File | Current value |
|---|------|---------------|
| 1 | `concepts/agent-memory-taxonomy.md` | `  - [[src_agent-memory-anatomy]]` |
| 2 | `concepts/user-md-configuration.md` | `  - [[src_hermes-analyst-workflow-essentials]]` |
| 3 | `concepts/user-md-configuration.md` | `  - [[src_3-things-learnt-3-weeks-hermes-analyst]]` |
| 4 | `concepts/memory-extraction-timing.md` | `  - [[src_agent-memory-anatomy]]` |
| 5 | `concepts/productivity-wage-gap.md` | `  - [[src_ai-will-destroy-world-economy]]` |
| 6 | `concepts/skill-atrophy.md` | `  - [[src_how-ai-productivity-fails]]` |
| 7 | `concepts/hermes-agent.md` | `  - [[src_hermes-polymarket-btc-trading-agent]]` |
| 8 | `concepts/hunter-gatherer-lifestyle.md` | `  - [[src_were-not-supposed-to-live-like-this]]` |
| 9 | `concepts/systems-thinking-limitations.md` | `  - [[src_what-comes-after-systems-thinking]]` |
| 10 | `concepts/negative-compounding.md` | `  - [[src_how-some-people-become-unrecognizable]]` |
| 11 | `concepts/orchestrator-worker-validator.md` | `  - [[src_luke-alvoeiro-multi-agent-architecture-factory]]` |
| 12 | `concepts/information-compression.md` | `  - [[src_active-vs-lazy-thinking]]` |
| 13 | `concepts/last30days-skill.md` | `  - [[src_3-things-learnt-3-weeks-hermes-analyst]]` |
| 14 | `concepts/fast-weights.md` | `  - [[src_llm-need-sleep-consolidation]]` |
| 15 | `concepts/sso-single-point-of-failure.md` | `  - [[src_dont-sign-in-with-google]]` |
| 16 | `concepts/ai-research-workflow.md` | `  - [[src_hermes-as-a-real-time-analyst]]` |
| 17 | `concepts/ai-research-workflow.md` | `  - [[src_1-month-with-hermes-ive-been-using-wrong]]` |
| 18 | `concepts/hindsight-skill.md` | `  - [[src_3-things-learnt-3-weeks-hermes-analyst]]` |
| 19 | `concepts/ai-vulnerability-discovery.md` | `  - [[src_project-glasswing-update]]` |
| 20 | `concepts/ai-powered-discovery.md` | `  - [[src_ai-trillion-dollar-blind-spot]]` |
| 21 | `concepts/hedonic-treadmill.md` | `  - [[src_why-we-complicate-life-productive-peter]]` |
| 22 | `concepts/default-mode-network.md` | `  - [[src_were-not-supposed-to-live-like-this]]` |
| 23 | `concepts/human-judgment-ai.md` | `  - [[src_will-ai-replace-systems-thinking]]` |
| 24 | `concepts/supply-chain-attack.md` | `  - [[src_11-minutes-hack-github]]` |
| 25 | `concepts/ai-legal-personhood.md` | `  - [[src_aaron-wright-ai-agents-legal-body]]` |
| 26 | `concepts/google-ai-mode.md` | `  - [[src_google-generative-ai-search-guide]]` |
| 27 | `concepts/strait-of-hormuz-geopolitics.md` | `  - [[src_uae-opec-exit-end-of-era]]` |
| 28 | `concepts/autobiographical-memory-systems.md` | `  - [[src_agent-memory-anatomy]]` |
| 29 | `concepts/ai-agent-setup-mistakes.md` | `  - [[src_3-things-learnt-3-weeks-hermes-analyst]]` |
| 30 | `concepts/organizational-incrementalism.md` | `  - [[src_active-vs-lazy-thinking]]` |
| 31 | `concepts/google-ai-overviews.md` | `  - [[src_google-guide-optimizing-generative-ai-search]]` |
| 32 | `concepts/taste-holders.md` | `  - [[src_how-ai-productivity-fails]]` |
| 33 | `concepts/american-security-guarantee.md` | `  - [[src_uae-opec-exit-end-of-era]]` |
| 34 | `concepts/agency-law.md` | `  - [[src_aaron-wright-ai-agents-legal-body]]` |
| 35 | `concepts/cynefin-framework.md` | `  - [[src_what-comes-after-systems-thinking]]` |
| 36 | `concepts/evolutionary-mismatch.md` | `  - [[src_were-not-supposed-to-live-like-this]]` |
| 37 | `concepts/domain-takeover-vulnerability.md` | `  - [[src_dont-sign-in-with-google]]` |
| 38 | `concepts/token-theft-attack.md` | `  - [[src_dont-sign-in-with-google]]` |
| 39 | `concepts/conversational-website.md` | `  - [[src_ai-trillion-dollar-blind-spot]]` |
| 40 | `concepts/generative-ai-search-optimization.md` | `  - [[src_google-guide-optimizing-generative-ai-search]]` |
| 41 | `concepts/discipline-system.md` | `  - [[src_how-some-people-become-unrecognizable]]` |
| 42 | `concepts/complicated-vs-complex.md` | `  - [[src_what-comes-after-systems-thinking]]` |
| 43 | `concepts/reflect-skill-hindsight.md` | `  - [[src_hermes-200-30-skills-3-worth-it]]` |
| 44 | `concepts/reflect-skill-hindsight.md` | `  - [[src_3-things-learnt-3-weeks-hermes-analyst]]` |
| 45 | `concepts/hermes-persistent-memory.md` | `  - [[src_3-things-learnt-3-weeks-hermes-analyst]]` |
| 46 | `concepts/ai-white-collar-automation.md` | `  - [[src_ai-will-destroy-world-economy]]` |
| 47 | `concepts/patience-vs-passivity.md` | `  - [[src_how-some-people-become-unrecognizable]]` |
| 48 | `concepts/non-commodity-content.md` | `  - [[src_google-guide-optimizing-generative-ai-search]]` |
| 49 | `concepts/hippocampal-replay.md` | `  - [[src_llm-need-sleep-consolidation]]` |
| 50 | `concepts/agent-handoff.md` | `  - [[src_luke-alvoeiro-multi-agent-architecture-factory]]` |

---

## Fix Pattern

**For sources files (`original:` field):**
```
# Before
original: [[2026-05-25_will-ai-replace-systems-thinking]]

# After
original: "[[2026-05-25_will-ai-replace-systems-thinking]]"
```

**For concept files (`sources:` array):**
```
# Before
sources:
  - [[src_will-ai-replace-systems-thinking]]

# After
sources:
  - "[[src_will-ai-replace-systems-thinking]]"
```

---

## Reference

Format spec v2.2 (2026-05-26):
> **Note:** Wikilinks in frontmatter fields (`original`, `sources`) use quoted format `"[[...]]"` for Obsidian compatibility. Wikilinks in body content use bare format `[[...]]`.