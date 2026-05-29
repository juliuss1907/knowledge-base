# Hygiene Report — 2026-05-29

> Hygiene Inspector run: 2026-05-29 11:12 AM
> Ground truth: `wiki/meta/folder-structure.md` v1.2 (2026-05-17)
> KB path: `/home/julius/knowledge-base/`
> **Status:** PENDING REVIEW

---

## 1. Summary

| Check | Result |
|---|---|
| Folder structure | ✅ PASS |
| Files in correct folders | ✅ PASS |
| `wiki/meta/` structure | ✅ PASS |
| `wiki/sources/` naming | ✅ PASS |
| `wiki/concepts/` naming | ✅ PASS |
| `wiki/tag/` structure | ✅ PASS |
| `wiki/topic/` structure | ✅ PASS |
| `wiki/drafts/` structure | ✅ PASS |
| `wiki/reviews/` structure | ✅ PASS |
| Forbidden patterns (.bak, .tmp, .DS_Store) | ✅ CLEAN |
| **Wikilink validation** | ⚠️ **32 broken concept links** |
| **Orphan concepts** | ⚠️ **32 missing concept files** |

---

## 2. Folder Structure — ✅ PASS

### 2.1 Root level

All allowed folders present: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`

### 2.2 Wiki structure

```
wiki/
├── meta/           ✅ (3 files: format-spec.md, folder-structure.md, index-spec.md)
├── sources/        ✅ (36 source files, all with src_ prefix)
├── concepts/      ✅ (163 concept files, lowercase-hyphen naming)
├── tag/           ✅ (19 files: tag.md + 18 tag index files)
├── topic/         ✅ (39 topic index files)
├── drafts/        ✅ (.gitkeep present)
├── reviews/       ✅ (_action-required.md + dated reports + archive/)
```

### 2.3 Reviews structure

- `_action-required.md` ✅ present
- Dated reports (2026-05-14 through 2026-05-28) ✅ present
- `archive/` subfolder ✅ present

---

## 3. Wikilink Validation — ⚠️ ISSUES FOUND

### 3.1 Sources → Concepts links

All 36 source files correctly reference concept slugs in their `## Concepts referenced` sections. No broken links found in source files.

### 3.2 Concept → Concept links

Scanned all 163 concept files for internal wikilinks. **32 concept links point to non-existent concept files:**

| Missing Concept | Referenced By (sample) |
|---|---|
| `agent-initiated-code-artifacts` | src_code-as-agent-harness-arxiv |
| `ai-hype-vs-reality` | src_the-revenge-of-the-business-idiot |
| `ai-safety` | src_project-glasswing-update |
| `automated-security-testing` | src_project-glasswing-update |
| `autonomous-agents` | src_agentic-commerce |
| `bittensor` | src_hermes-polymarket-btc-trading-agent |
| `code-for-action` | src_code-as-agent-harness-arxiv |
| `code-for-environment-modeling` | src_code-as-agent-harness-arxiv |
| `code-for-reasoning` | src_code-as-agent-harness-arxiv |
| `crypto-trading-bots` | src_hermes-polymarket-btc-trading-agent |
| `dao-legal-structure` | src_aaron-wright-ai-agents-legal-body |
| `dead-drop-communication` | src_11-minutes-hack-github |
| `dns-tunneling` | src_11-minutes-hack-github |
| `economic-inequality` | src_ai-will-destroy-world-economy |
| `embedding-search` | src_retrieval-augmented-generation |
| `executive-ai-psychosis` | src_the-revenge-of-the-business-idiot |
| `financial-crisis-2008-comparison` | src_ai-will-destroy-world-economy |
| `github-security` | src_11-minutes-hack-github |
| `harness-control` | src_plan-execute-verify-loop |
| `market-inefficiency` | src_reflexivity-soros |
| `mcp-model-context-protocol` | src_hermes-agent |
| `multi-agent-systems` | src_code-as-agent-harness-arxiv |
| `nous-research` | src_hermes-xurl-skill-guide |
| `orphan-commit-attack` | src_11-minutes-hack-github |
| `pareto-principle` | src_why-we-complicate-life-productive-peter |
| `prediction-markets` | src_hermes-polymarket-btc-trading-agent |
| `program-of-thoughts` | src_code-as-agent-harness-arxiv |
| `self-learning-agents` | src_hermes-polymarket-btc-trading-agent |
| `smart-contracts` | src_zero-member-llc |
| `supergrok-subscription` | src_hermes-xurl-skill-guide |
| `transposed-organization` | src_how-ai-productivity-fails |
| `ubi-universal-basic-income` | src_ai-will-destroy-world-economy |
| `vector-database` | src_retrieval-augmented-generation |

**Total broken concept links: 32**

### 3.3 Raw file references

All wikilinks referencing raw files (in source file `original:` fields) are correctly formatted and reference existing raw files. ✅

---

## 4. Issues Summary

| # | Severity | Type | Count | Description |
|---|---|---|---|---|
| 1 | WARNING | Missing concept files | 32 | Wikilinks point to concept files that don't exist |
| 2 | INFO | Stale "Concepts referenced" sections | 36 | Source files list concepts not yet compiled (by design — source files are compiled first, concepts second) |

---

## 5. Recommendations

### For OpenClaw Compile Agent

These 32 missing concepts should be created from the source material that references them:

**High priority (referenced multiple times):**
- `prediction-markets` — referenced by src_hermes-polymarket-btc-trading-agent
- `crypto-trading-bots` — same source
- `self-learning-agents` — same source
- `multi-agent-systems` — referenced by src_code-as-agent-harness-arxiv and src_multi-agent-taxonomy
- `ubi-universal-basic-income` — referenced by src_ai-will-destroy-world-economy

**Medium priority (referenced once):**
- `agent-initiated-code-artifacts`, `code-for-action`, `code-for-environment-modeling`, `code-for-reasoning`
- `dao-legal-structure`, `smart-contracts`
- `mcp-model-context-protocol`
- `market-inefficiency`, `financial-crisis-2008-comparison`

**Low priority (general knowledge):**
- `dead-drop-communication`, `dns-tunneling`, `github-security`
- `embedding-search`, `vector-database`
- `economic-inequality`, `ai-safety`, `automated-security-testing`

### Note on "Stale" links

The 36 "stale" references in source files' "Concepts referenced" sections are expected — source files are compiled before concepts exist. This is by design in the pipeline (NGUỐN → INGEST → COMPILE → INDEX → VALIDATION).

---

## 6. Resolution

| # | Action | Owner |
|---|---|---|
| 1 | Create 32 missing concept files from source material | OpenClaw (compile-agent) |
| 2 | Verify wikilinks resolve correctly after concepts are created | Hermes (hygiene-inspector) |

---

*Report generated by Hygiene Inspector — Hermes subagent*
*Next scheduled run: 2026-05-30 (or on demand)*