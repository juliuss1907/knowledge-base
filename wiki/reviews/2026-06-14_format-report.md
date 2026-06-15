# Format Validation — 2026-06-14

**Status:** approved
**Approved by:** Julius
**Issues found:** 293 (shown: 20)
**Created:** 2026-06-14 23:20:23
**Validator:** format-validator

- **ERROR:** 4
- **WARNING:** 289
- **INFO:** 0
- **Files checked:** 394

> **Note:** Only first 20 issues shown (ERROR prioritized). Full scan found 293 total issues.

---

## Issue 1: Markdown link used for internal content: [X Developers]

**File:** wiki/sources/src_hermes-xurl-skill-guide.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Markdown link used for internal content: [X Developers]
**Current:** [X Developers](...)
**Expected:** [[slug]]

---

## Issue 2: Invalid source slug: the-power-of-incentives-hidden-forces-shape-behavior

**File:** wiki/sources/src_the-power-of-incentives-hidden-forces-shape-behavior.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Invalid source slug: the-power-of-incentives-hidden-forces-shape-behavior
**Current:** the-power-of-incentives-hidden-forces-shape-behavior
**Expected:** lowercase-hyphen, max 50

---

## Issue 3: Invalid source slug: todays-most-crucial-leadership-skill-is-systems-thinking

**File:** wiki/sources/src_todays-most-crucial-leadership-skill-is-systems-thinking.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Invalid source slug: todays-most-crucial-leadership-skill-is-systems-thinking
**Current:** todays-most-crucial-leadership-skill-is-systems-thinking
**Expected:** lowercase-hyphen, max 50

---

## Issue 4: Frontmatter parse error: missing frontmatter

**File:** wiki/tag/tag.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** Frontmatter parse error: missing frontmatter
**Current:** missing or invalid frontmatter
**Expected:** Valid YAML frontmatter with type field

---

## Issue 5: Broken wikilink to concept: momentum

**File:** wiki/concepts/activation-energy.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: momentum
**Current:** momentum
**Expected:** File momentum.md exists

---

## Issue 6: Broken wikilink to concept: inertia

**File:** wiki/concepts/activation-energy.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: inertia
**Current:** inertia
**Expected:** File inertia.md exists

---

## Issue 7: Broken wikilink to concept: breaking-point

**File:** wiki/concepts/activation-energy.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: breaking-point
**Current:** breaking-point
**Expected:** File breaking-point.md exists

---

## Issue 8: Broken wikilink to concept: agent-initiated-code-artifacts

**File:** wiki/concepts/agent-harness.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: agent-initiated-code-artifacts
**Current:** agent-initiated-code-artifacts
**Expected:** File agent-initiated-code-artifacts.md exists

---

## Issue 9: Broken wikilink to concept: multi-agent-systems

**File:** wiki/concepts/agent-harness.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: multi-agent-systems
**Current:** multi-agent-systems
**Expected:** File multi-agent-systems.md exists

---

## Issue 10: Broken wikilink to concept: autonomous-agents

**File:** wiki/concepts/agentic-commerce.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: autonomous-agents
**Current:** autonomous-agents
**Expected:** File autonomous-agents.md exists

---

## Issue 11: Broken wikilink to concept: ai-hype-vs-reality

**File:** wiki/concepts/ai-impression-of-work.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: ai-hype-vs-reality
**Current:** ai-hype-vs-reality
**Expected:** File ai-hype-vs-reality.md exists

---

## Issue 12: Broken wikilink to concept: dao-legal-structure

**File:** wiki/concepts/ai-legal-personhood.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: dao-legal-structure
**Current:** dao-legal-structure
**Expected:** File dao-legal-structure.md exists

---

## Issue 13: Broken wikilink to concept: automated-security-testing

**File:** wiki/concepts/ai-vulnerability-discovery.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: automated-security-testing
**Current:** automated-security-testing
**Expected:** File automated-security-testing.md exists

---

## Issue 14: Broken wikilink to concept: economic-inequality

**File:** wiki/concepts/ai-white-collar-automation.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: economic-inequality
**Current:** economic-inequality
**Expected:** File economic-inequality.md exists

---

## Issue 15: Broken wikilink to concept: ubi-universal-basic-income

**File:** wiki/concepts/ai-white-collar-automation.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: ubi-universal-basic-income
**Current:** ubi-universal-basic-income
**Expected:** File ubi-universal-basic-income.md exists

---

## Issue 16: Broken wikilink to concept: hierarchical-organization-mental-model

**File:** wiki/concepts/alloying-mental-model.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: hierarchical-organization-mental-model
**Current:** hierarchical-organization-mental-model
**Expected:** File hierarchical-organization-mental-model.md exists

---

## Issue 17: Broken wikilink to concept: theory-of-constraints

**File:** wiki/concepts/bottlenecks-mental-model.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: theory-of-constraints
**Current:** theory-of-constraints
**Expected:** File theory-of-constraints.md exists

---

## Issue 18: Broken wikilink to concept: scale-mental-model

**File:** wiki/concepts/bottlenecks-mental-model.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: scale-mental-model
**Current:** scale-mental-model
**Expected:** File scale-mental-model.md exists

---

## Issue 19: Broken wikilink to concept: executive-ai-psychosis

**File:** wiki/concepts/business-idiot-archetype.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: executive-ai-psychosis
**Current:** executive-ai-psychosis
**Expected:** File executive-ai-psychosis.md exists

---

## Issue 20: Broken wikilink to concept: emergence-mental-model

**File:** wiki/concepts/catalysts-mental-model.md
**Severity:** WARNING
**Category:** Markdown
**Issue:** Broken wikilink to concept: emergence-mental-model
**Current:** emergence-mental-model
**Expected:** File emergence-mental-model.md exists
