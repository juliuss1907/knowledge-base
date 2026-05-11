# Compile Agent — Tagging Rules

Detailed logic for assigning tags from `TAGS.md` during compilation.

---

## Overview

Every wiki file (source notes and concept notes) must have:
- **1 main-tag** from Pool A (required)
- **1-3 sub-tags** from Pool B (required)
- **1 topic** (free-form slug, not a tag)

This document defines how Compile Agent picks the right tags for each piece of content.

---

## Pool A — Main-tag Selection

Pool A tags are **broad domain categories**. Pick exactly ONE per file.

### Decision tree

```
Is content primarily about AI/ML/LLM/agents?
├── YES → #ai
└── NO → next question

Is content primarily about blockchain/crypto/DeFi?
├── YES → #crypto
└── NO → next question

Is content primarily about software/dev/infra?
├── YES → #tech
└── NO → next question

Is content primarily about workflows/methodologies/PKM?
├── YES → #productivity
└── NO → next question

Is content primarily about system design/architecture?
├── YES → #system
└── NO → next question

Is content primarily about markets/finance/macroeconomics?
├── YES → #economic
└── NO → next question

Is content primarily about policy/regulation/geopolitics?
├── YES → #politic
└── NO → ESCALATE (no Pool A tag fits)
```

### When in doubt — the 60% rule

If content spans multiple domains, ask: **"What is 60%+ of the content about?"**

Examples:

| Content | Primary domain | Main-tag |
|---|---|---|
| AI tool for crypto trading | 60% AI implementation, 40% crypto use case | `#ai` |
| DeFi protocol with AI risk model | 60% DeFi mechanics, 40% AI feature | `#crypto` |
| Productivity system using AI | 60% workflow methodology, 40% AI tool | `#productivity` |
| Architecture for LLM apps | 60% system design, 40% AI specifics | `#system` |

### Tag definitions (detailed)

#### `#ai`
**Use when content is about:**
- Large language models (LLM, GPT, Claude, Gemini)
- AI agents and agentic systems
- Machine learning and deep learning
- AI safety, alignment, interpretability
- Prompt engineering, RAG, fine-tuning
- Multimodal models (vision, audio, video)
- AI training, inference, deployment

**Examples:**
- "How Claude Code works" → `#ai`
- "Building RAG pipelines" → `#ai`
- "LLM evaluation benchmarks" → `#ai`

**Don't use for:**
- AI tools used in crypto context (use `#crypto` if crypto is primary)
- Generic mentions of "AI" without depth

---

#### `#crypto`
**Use when content is about:**
- Blockchain protocols and consensus mechanisms
- Smart contracts and dApps
- Tokens, NFTs, DeFi protocols
- Crypto exchanges (CEX, DEX, perpdex)
- On-chain analysis, MEV, staking
- Crypto regulation specifically
- Web3 infrastructure

**Examples:**
- "Curve Finance exploit analysis" → `#crypto`
- "Layer 2 scaling solutions" → `#crypto`
- "Hyperliquid perpdex review" → `#crypto`

**Don't use for:**
- Traditional finance (use `#economic`)
- Government crypto policy (use `#politic` if regulation is primary)

---

#### `#tech`
**Use when content is about:**
- Software engineering practices
- Programming languages, frameworks, libraries
- Development tools (IDE, CLI, version control)
- Web/mobile/desktop development
- DevOps, CI/CD, cloud infrastructure
- APIs, databases, system integration

**Examples:**
- "TypeScript best practices" → `#tech`
- "Docker compose patterns" → `#tech`
- "GitHub Actions workflows" → `#tech`

**Don't use for:**
- AI-specific tooling (use `#ai`)
- System architecture concepts (use `#system`)

---

#### `#productivity`
**Use when content is about:**
- Personal knowledge management (PKM)
- Note-taking systems (Obsidian, Notion, Roam)
- Workflow methodologies (GTD, PARA, Zettelkasten)
- Time management, focus techniques
- Learning strategies, deliberate practice
- Personal automation for daily tasks

**Examples:**
- "Building a second brain" → `#productivity`
- "Obsidian graph view tips" → `#productivity`
- "Pomodoro technique deep dive" → `#productivity`

**Don't use for:**
- Team productivity tools (use `#tech` if dev-focused)
- AI productivity tools (use `#ai` if AI is primary)

---

#### `#system`
**Use when content is about:**
- System architecture and design patterns
- Distributed systems, microservices
- Pipeline design (data, ML, automation)
- Multi-agent systems, orchestration
- Infrastructure as code, observability
- Capacity planning, scaling strategies

**Examples:**
- "Knowledge base architecture" → `#system`
- "Agent orchestration patterns" → `#system`
- "Event-driven systems" → `#system`

**Don't use for:**
- Specific tools or frameworks (use `#tech`)
- AI agent implementations (use `#ai` if model-focused)

---

#### `#economic`
**Use when content is about:**
- Macroeconomics, monetary policy
- Stock markets, commodities, forex
- Trading strategies, market analysis
- Economic indicators, recession analysis
- Banking, traditional finance
- Business strategy, valuation

**Examples:**
- "Fed rate decision impact" → `#economic`
- "Equity market analysis Q2 2026" → `#economic`
- "Recession indicators 2026" → `#economic`

**Don't use for:**
- Crypto markets (use `#crypto`)
- Government regulation (use `#politic`)

---

#### `#politic`
**Use when content is about:**
- Government policy and regulation
- Geopolitics, international relations
- Election analysis, political movements
- Legal/regulatory frameworks
- Sanctions, trade wars
- Policy impact on industries

**Examples:**
- "EU AI Act analysis" → `#politic`
- "US-China tech war" → `#politic`
- "SEC crypto regulation 2026" → `#politic`

**Don't use for:**
- Pure economic analysis (use `#economic`)
- Tech industry news without policy angle (use `#tech` or `#ai`)

---

## Pool B — Sub-tag Selection

Pool B tags are **cross-cutting attributes**. Pick 1-3 per file.

### Selection algorithm

For each candidate sub-tag, ask:
1. **Does this attribute clearly apply?** (not a stretch)
2. **Would Julius search for this content using this tag?**
3. **Is this in the top 3 most defining attributes?**

If yes to all → include. If no to any → exclude.

### Tag definitions (detailed)

#### `#hack`
**Use when content covers:**
- Security exploits, vulnerabilities
- Attack vectors, post-mortems
- Penetration testing, red teaming
- Smart contract hacks
- Prompt injection, jailbreaks

**Examples:**
- DeFi exploit analysis → `#hack`
- LLM jailbreak techniques → `#hack`
- CVE writeups → `#hack`

---

#### `#tools`
**Use when content covers:**
- Specific software products
- Libraries, frameworks, services
- Developer tools (CLI, IDE, plugins)
- SaaS platforms

**Examples:**
- Cursor editor review → `#tools`
- Claude Code features → `#tools`
- Anthropic SDK guide → `#tools`

**Note:** Use this tag liberally — most actionable content involves specific tools.

---

#### `#automation`
**Use when content covers:**
- Bots, scripts, scheduled jobs
- Automated pipelines (CI/CD, data, ML)
- Workflow automation tools (n8n, Zapier)
- Agent-based automation

**Examples:**
- GitHub Actions tutorial → `#automation`
- Telegram bot for trading → `#automation`
- Scheduled data pipelines → `#automation`

---

#### `#vibecode`
**Use when content covers:**
- AI-assisted development style
- Coding with Cursor, Copilot, Claude Code
- Agent-driven coding workflows
- Pair programming with AI

**Examples:**
- Vibe coding manifesto → `#vibecode`
- Cursor productivity tips → `#vibecode`
- Claude Code daily workflow → `#vibecode`

---

#### `#research`
**Use when content covers:**
- Academic papers (arXiv, journals)
- Deep technical analysis
- Empirical studies, benchmarks
- Original research findings

**Examples:**
- "Attention Is All You Need" paper → `#research`
- LLM scaling laws analysis → `#research`
- Empirical studies on prompt techniques → `#research`

---

#### `#tutorial`
**Use when content covers:**
- Step-by-step how-to guides
- Walkthroughs with examples
- Beginner-friendly explanations
- Configuration guides

**Examples:**
- "How to build a RAG system" → `#tutorial`
- Docker setup walkthrough → `#tutorial`
- Setting up Obsidian with plugins → `#tutorial`

---

#### `#opinion`
**Use when content covers:**
- Personal takes, editorials
- Predictions, hot takes
- Industry commentary
- Subjective analysis

**Examples:**
- "Why I quit Twitter" → `#opinion`
- "AI will/won't replace devs" → `#opinion`
- Crypto market predictions → `#opinion`

---

#### `#news`
**Use when content covers:**
- Recent announcements (within 30 days)
- Breaking events
- Product launches
- Time-sensitive updates

**Examples:**
- "Anthropic releases Opus 5" → `#news`
- "Major DeFi exploit today" → `#news`
- "GitHub announces new feature" → `#news`

**Note:** `#news` is time-sensitive. After 6 months, content may not warrant this tag anymore (but don't remove from existing files).

---

#### `#defi`
**Use when content covers:**
- Decentralized exchanges (DEX)
- Lending/borrowing protocols
- Yield farming, liquidity pools
- AMM mechanics
- Stablecoin protocols

**Examples:**
- Uniswap V4 analysis → `#defi`
- Aave lending mechanics → `#defi`
- Curve pool exploit → `#defi`

**Pairs with:** Almost always with `#crypto` as main-tag.

---

#### `#perpdex`
**Use when content covers:**
- Perpetual futures DEXs
- Derivatives trading on-chain
- Funding rate mechanics
- Specific perpdex protocols (dYdX, GMX, Hyperliquid)

**Examples:**
- Hyperliquid review → `#perpdex`
- GMX vs dYdX comparison → `#perpdex`
- Funding rate strategies → `#perpdex`

**Pairs with:** Almost always with `#crypto` as main-tag.

---

#### `#layer1`
**Use when content covers:**
- Base-layer blockchains (Ethereum, Solana, Bitcoin)
- L1 consensus mechanisms
- L1 vs L1 comparisons
- Native token economics

**Examples:**
- Solana TPS analysis → `#layer1`
- Ethereum roadmap → `#layer1`
- Move-based chains review → `#layer1`

---

#### `#layer2`
**Use when content covers:**
- Rollups (optimistic, ZK)
- Sidechains, validiums
- Bridge protocols
- L2 scaling solutions

**Examples:**
- Arbitrum vs Optimism → `#layer2`
- ZK rollup deep dive → `#layer2`
- L2 bridge security → `#layer2`

---

## Topic Generation

Topic is a **free-form lowercase-hyphen slug** that describes the specific subject.

### Rules

1. **Lowercase only** — no uppercase letters
2. **Hyphens for spaces** — not underscores, not camelCase
3. **Max 50 characters** — concise but descriptive
4. **Specific** — should distinguish this content from others
5. **Stable** — same topic for related content (enables grouping)

### Generation logic

```
Step 1: Identify the most specific subject
Step 2: Convert to lowercase
Step 3: Replace spaces with hyphens
Step 4: Remove non-alphanumeric (except hyphens)
Step 5: Truncate to 50 chars
```

### Examples

| Content title | Topic slug |
|---|---|
| "How to write Claude Code skills" | `claude-code-skills` |
| "Curve Finance Pool Exploit Analysis" | `curve-pool-exploit` |
| "Progressive Disclosure for Agent Skills" | `progressive-disclosure` |
| "Building RAG Pipeline with LangChain" | `rag-pipeline-langchain` |
| "Hyperliquid Perpdex Review Q2 2026" | `hyperliquid-review-2026-q2` |
| "L2 Narrative Analysis 2026" | `l2-narrative-2026` |

### Topic vs Tag — when in doubt

**Use a tag** when the attribute is **cross-cutting** (applies to many topics):
- `#hack`, `#tutorial`, `#research` are tags
- They appear across many subjects

**Use a topic** when the subject is **specific** (only this content + closely related):
- `claude-code-skills`, `curve-pool-exploit` are topics
- They are unique subjects with their own grouping

### Stability across files

Same topic should be used for related content:

**Good:**
- File 1: `topic: claude-code-skills`
- File 2: `topic: claude-code-skills` (same topic, both about Claude Code skills)
- File 3: `topic: claude-code-skills`

**Bad:**
- File 1: `topic: claude-code-skills-guide`
- File 2: `topic: claude-skills-tutorial` (slight variation, breaks grouping)
- File 3: `topic: skills-claude-code`

→ Index Agent generates `wiki/topic/<topic>.md` per unique topic. Inconsistent topics fragment the index.

---

## Example Tag Assignments

### Example 1: AI tool tutorial

**Content:** "How to use Claude Code for daily development"

**Analysis:**
- Domain: AI (Claude is an AI assistant)
- Attributes: tools (Claude Code), tutorial (how-to), vibecode (AI-assisted dev)
- Subject: Claude Code workflow

**Tags:**
```yaml
main_tag: ai
sub_tags: [tools, tutorial, vibecode]
topic: claude-code-workflow
```

---

### Example 2: DeFi exploit analysis

**Content:** "Curve Finance pool exploit: $40M lost in reentrancy attack"

**Analysis:**
- Domain: Crypto (DeFi protocol)
- Attributes: hack (exploit), defi (DeFi protocol), news (recent event)
- Subject: Curve pool exploit

**Tags:**
```yaml
main_tag: crypto
sub_tags: [hack, defi, news]
topic: curve-pool-exploit
```

---

### Example 3: Academic paper

**Content:** "Attention Is All You Need (Vaswani et al., 2017)"

**Analysis:**
- Domain: AI (Transformer architecture)
- Attributes: research (academic paper)
- Subject: Transformer architecture

**Tags:**
```yaml
main_tag: ai
sub_tags: [research]
topic: transformer-architecture
```

**Note:** Only 1 sub-tag is acceptable (minimum is 1).

---

### Example 4: Productivity opinion piece

**Content:** "Why I switched from Notion to Obsidian"

**Analysis:**
- Domain: Productivity (PKM)
- Attributes: tools (Obsidian, Notion), opinion (personal take)
- Subject: Note-taking app comparison

**Tags:**
```yaml
main_tag: productivity
sub_tags: [tools, opinion]
topic: notion-to-obsidian
```

---

### Example 5: System architecture

**Content:** "Building a multi-agent knowledge base with OpenClaw and Hermes"

**Analysis:**
- Domain: System (architecture)
- Attributes: tools (OpenClaw, Hermes), automation (agent pipeline)
- Subject: KB architecture with agents

**Tags:**
```yaml
main_tag: system
sub_tags: [tools, automation]
topic: kb-multi-agent-architecture
```

---

### Example 6: L2 protocol news

**Content:** "Arbitrum announces Stylus mainnet launch"

**Analysis:**
- Domain: Crypto (L2 protocol)
- Attributes: layer2 (Arbitrum is L2), news (announcement), tools (Stylus)
- Subject: Arbitrum Stylus launch

**Tags:**
```yaml
main_tag: crypto
sub_tags: [layer2, news, tools]
topic: arbitrum-stylus-launch
```

---

## Tag Proposal Workflow

When existing tags don't fit, propose a new one. **Never auto-add.**

### When to propose

Only if:
1. Content clearly needs a new attribute or category
2. No existing tag captures it (even loosely)
3. The new tag would apply to multiple future files (not one-off)

### When NOT to propose

If:
- An existing tag fits "good enough" → use that
- The need is one-off (only this single file) → use closest existing
- The content is too narrow for a tag → use as topic instead

### Proposal format

```
[TAG PROPOSAL]
Pool: A (main-tag) | B (sub-tag)
Proposed: #<new-tag>
Reason: <1-2 sentences explaining why existing tags don't fit>
File context: raw/<type>/<filename>
Closest existing tag: <fallback if rejected>
Estimated future usage: <how many other files might need this tag>
```

### Examples

#### Good proposal (likely approved)

```
[TAG PROPOSAL]
Pool: B (sub-tag)
Proposed: #mcp
Reason: Multiple files cover Model Context Protocol implementation, which is distinct from generic #tools or #automation. MCP is a specific protocol with growing ecosystem.
File context: raw/articles/2026-05-05_mcp-server-guide.md
Closest existing tag: #tools
Estimated future usage: ~10-15 files in next 6 months (MCP is trending)
```

#### Bad proposal (likely rejected)

```
[TAG PROPOSAL]
Pool: B (sub-tag)
Proposed: #cool-stuff
Reason: This article is really cool
File context: raw/articles/2026-05-05_random.md
Closest existing tag: #tools
Estimated future usage: unclear
```

→ Too vague, not a real attribute.

---

## Anti-patterns (avoid these)

### ❌ Tag stuffing

```yaml
# Wrong: too many sub-tags
sub_tags: [tools, automation, tutorial, vibecode, news]
```

```yaml
# Right: max 3, most relevant
sub_tags: [tools, automation, tutorial]
```

### ❌ Vague main-tag

```yaml
# Wrong: forcing #tech for AI content
main_tag: tech  # Should be #ai
sub_tags: [tools]
```

### ❌ Topic as tag

```yaml
# Wrong: topic value used as a tag
sub_tags: [tools, claude-code-workflow]  # claude-code-workflow is a topic, not a tag
```

```yaml
# Right
sub_tags: [tools]
topic: claude-code-workflow
```

### ❌ Inconsistent topics

```yaml
# Wrong: same subject, different topic slugs
File 1: topic: rag-pipeline
File 2: topic: rag-system
File 3: topic: rag-architecture
```

```yaml
# Right: stable topic across related files
File 1: topic: rag-pipeline
File 2: topic: rag-pipeline
File 3: topic: rag-pipeline
```

### ❌ Inventing tags without proposal

```yaml
# Wrong: agent invented #devops without asking
sub_tags: [tools, devops]
```

→ If `#devops` isn't in TAGS.md, must propose first.

---

## Quick Reference Checklist

Before finalizing tags for a file, verify:

- [ ] Exactly **1 main-tag** from Pool A
- [ ] **1-3 sub-tags** from Pool B
- [ ] **1 topic** (lowercase-hyphen, max 50 chars)
- [ ] All tags exist in current `TAGS.md`
- [ ] Tags are most relevant (not stretching)
- [ ] Topic is consistent with related files
- [ ] If new tag needed → proposal sent, not auto-added

---

## Related Documentation

- [SKILL.md](SKILL.md) — Compile Agent overview
- [workflow.md](workflow.md) — Step-by-step compilation
- `TAGS.md` (root) — Current tag taxonomy (source of truth)
- `wiki/meta/format-spec.md` — Frontmatter schema

