# TAGS.md — Knowledge Base Tag Taxonomy

> Two independent pools: main-tags (categories) + sub-tags (attributes).
> Tags are flat, not nested. Connections emerge via co-occurrence in files.
> **Append-only.** Index Agent proposes new tags → Julius approves → entry added here.

**Version:** 1.4
**Last updated:** 2026-08-06

---

## 1. Tagging rules

Every file in `wiki/concepts/` and `wiki/sources/` must declare:

- **1 main-tag** (required) — chosen from Pool A
- **1–3 sub-tags** (1 minimum, 3 maximum) — chosen from Pool B
- **1 topic** (required, free-form `lowercase-hyphen` slug) — not a tag, used for the topic index

Frontmatter format:

```yaml
main_tag: <one-from-pool-a>
sub_tags: [<one-to-three-from-pool-b>]
topic: <free-form-slug>
```

Obsidian renders these as separate flat tags: `#main_tag`, `#sub_tag_1`, `#sub_tag_2`, etc. Graph view shows connections between tags via files that contain them.

---

## 2. Pool A — Main-tags (broad categories)

| Tag | Description |
|---|---|
| `#ai` | AI / ML / LLM, agents, models, training, inference |
| `#crypto` | Blockchain, DeFi, tokens, exchanges, on-chain activity |
| `#tech` | Software engineering, infrastructure, web, mobile, dev tooling |
| `#productivity` | Workflows, methodologies, knowledge management, personal systems |
| `#system` | System design, architecture, automation pipelines |
| `#economic` | Macroeconomics, finance, markets, trading |
| `#politic` | Policy, regulation, geopolitics |
| `#health` | Physical health, sleep, exercise, nutrition, biohacking |
| `#investment` | Investment principles, portfolio management, asset allocation, risk management |

**Total:** 9 main-tags.

---

## 3. Pool B — Sub-tags (cross-cutting attributes)

Sub-tags are independent of main-tags. Any sub-tag may co-occur with any main-tag.

| Tag | Description |
|---|---|
| `#hack` | Exploits, vulnerabilities, attacks, post-mortems |
| `#tools` | Concrete software, products, services, libraries |
| `#automation` | Bots, scripts, scheduled jobs, automated workflows |
| `#vibecode` | Vibe coding, AI-assisted development style |
| `#research` | Academic papers, deep analysis, primary sources |
| `#tutorial` | How-to guides, walkthroughs, step-by-step instructions |
| `#opinion` | Personal takes, editorials, commentary |
| `#news` | Recent events, announcements, time-sensitive updates |
| `#defi` | Decentralized finance protocols, AMMs, lending, yield |
| `#perpdex` | Perpetual exchanges, derivatives DEXs |
| `#layer1` | Base-layer blockchains |
| `#layer2` | Scaling solutions, rollups, sidechains |
| `#law` | Legal frameworks, contracts, regulations, compliance |
| `#coding` | Programming, software development, code generation, dev practices |
| `#psychology` | Cognitive science, behavioral psychology, mental models, biases |
| `#health` | Physical health, sleep, exercise, nutrition, biohacking |
| `#ai` | AI / ML / LLM, agents, models, training, inference (as attribute) |
| `#system` | System design, architecture, automation pipelines (as attribute) |
| `#geopolitics` | Geopolitical analysis, international relations, empire cycles, tribute systems, great power competition |
| `#strategy` | Strategic thinking, decision frameworks, competitive positioning, game theory |

**Total:** 20 sub-tags.

---

## 4. Example combinations

A file about "AI security tools":
```yaml
main_tag: ai
sub_tags: [tools, hack]
topic: ai-red-teaming
```
→ Obsidian tags: `#ai`, `#tools`, `#hack`

A file about "DeFi exploits":
```yaml
main_tag: crypto
sub_tags: [defi, hack, news]
topic: curve-pool-exploit-2026
```
→ Obsidian tags: `#crypto`, `#defi`, `#hack`, `#news`

A file about "Vibe coding workflows":
```yaml
main_tag: tech
sub_tags: [vibecode, automation]
topic: claude-code-workflow
```
→ Obsidian tags: `#tech`, `#vibecode`, `#automation`

A file about "Macro analysis of L2 narratives":
```yaml
main_tag: crypto
sub_tags: [layer2, opinion]
topic: l2-narrative-2026-q2
```
→ Obsidian tags: `#crypto`, `#layer2`, `#opinion`

---

## 5. Index files generated from tags

The OpenClaw Index Agent maintains:

- `wiki/tag/<tag>.md` — one file per tag (both main and sub), listing all concepts and sources tagged with it, plus a co-occurring tags section
- `wiki/topic/<topic>.md` — one file per topic, grouping concepts and sources sharing the same `topic` slug

These files are auto-regenerated. Do not edit manually — edits will be overwritten on the next index run.

---

## 6. Adding new tags (proposal workflow)

When the Compile or Index Agent encounters content that doesn't fit any existing tag:

1. **Stop.** Do not write a new tag into any file frontmatter.
2. **Propose** to Julius via the agreed channel using this format:

   ```
   [TAG PROPOSAL]
   Pool: A (main-tag) | B (sub-tag)
   Proposed: #<new-tag>
   Reason: <1–2 sentences>
   File context: <slug of the file requiring this tag>
   Closest existing tag: <fallback if rejected>
   ```

3. **Wait** for Julius's reply. Block on this file until decision.
4. **If approved:**
   - Append the new tag entry to the correct pool table in this file (TAGS.md)
   - Bump the `Last updated` date and the pool's count
   - Create `wiki/tag/<new-tag>.md` index stub
   - Apply the tag to the originating file
5. **If rejected:**
   - Use the closest existing tag (specified in the proposal)
   - Log the rejection in the agent's MEMORY.md

---

## 7. Forbidden actions (hard rules)

- ❌ Never delete an existing tag entry from this file
- ❌ Never modify a tag's name or description without explicit Julius approval
- ❌ Never use a tag not present in this file (proposal flow is mandatory)
- ❌ Never use nested tag syntax like `#ai/tools` — flat tags only
- ❌ Never apply more than 3 sub-tags or fewer than 1 sub-tag to a file
- ❌ Never apply more than 1 main-tag to a file

---

## 8. Change log

| Date | Change | Author |
|---|---|---|
| 2026-05-04 | Initial taxonomy: 7 main-tags + 12 sub-tags | Julius |
| 2026-06-17 | Approved: #health → Pool A, #ai/#system → Pool B (Julius) | Kara |
| 2026-06-19 | Approved: #investment → Pool A (Julius) | Kara |
| 2026-06-19 | Approved: #geopolitics → Pool B (Julius) — includes empire cycles, tribute systems, great power competition | Kara |
| 2026-08-06 | Approved: #strategy → Pool B (Julius) — strategic thinking, decision frameworks, competitive positioning, game theory | Connor |
