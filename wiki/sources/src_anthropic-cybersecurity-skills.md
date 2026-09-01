---
type: source
original: "[[2026-08-30_mukul975_anthropic-cybersecurity-skills]]"
main_tag: ai
sub_tags: [tools, hack, research]
topic: ai-cybersecurity-skills-library
date_compiled: 2026-08-31
url: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
author: mukul975
---

# Anthropic Cybersecurity Skills

## Metadata

- **Author:** mukul975
- **Published:** [unknown]
- **Source:** github.com
- **URL:** https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- **Type:** repo

## Summary

Anthropic Cybersecurity Skills là thư viện skills lớn nhất cho AI agents về cybersecurity với 818 skills production-grade, trải dài 34 security domains, mapping 6 industry frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF, MITRE F3). Đây không phải bộ sưu tập scripts hay checklists — nó là AI-native knowledge base theo agentskills.io standard, với YAML frontmatter cho discovery dưới giây, Markdown structured cho step-by-step execution, và reference files cho deep technical context. Mỗi skill encoded practitioner workflows thật, không generated summaries. Agent scan 818 skills trong một pass (~30 tokens mỗi skill) và load sâu 500–2000 tokens khi cần thực thi. Giải quyết khoảng trống 4.8 triệu unfilled roles trong cybersecurity workforce (ISC2 2024).

## Key points

- **818 skills, 34 domains:** Cloud Security, SOC, Threat Hunting, Digital Forensics, Malware Analysis, Red Teaming, AI Security, và nhiều hơn
- **6 framework mapping:** MITRE ATT&CK v19.1 (805 skills), NIST CSF 2.0 (804), D3FEND (139), NIST AI RMF (97), MITRE F3 (94), MITRE ATLAS (93)
- **MITRE F3 mới (2026-04-09):** Fight Fraud Framework — 2 fraud-specific tactics (Positioning, Monetization), 94 fraud-relevant skills
- **Progressive disclosure architecture:** ~30 tokens scan frontmatter, 500–2000 tokens load full workflow — scan 818 skills trong 1 pass
- **Skill anatomy:** SKILL.md (frontmatter + YAML) + references/ (standards, workflows) + scripts/ + assets/
- **AI-native knowledge base:** Không phải scripts hay checklists, mà là workflows thực tế của practitioner
- **Zero revoked IDs:** 290 distinct ATT&CK techniques (146 base + 144 sub), validated với mitreattack-python library
- **Compatible đa nền tảng:** Claude Code, GitHub Copilot, Cursor, Codex CLI, Gemini CLI, LangChain, CrewAI, AutoGen, MCP-compatible agents
- **Community project:** Không affiliated với Anthropic PBC, Apache-2.0 license
- **Giải quyết workforce gap:** 4.8M unfilled roles — AI agents cần structured domain knowledge để trở thành security analyst capable

## Concepts referenced

- [[cybersecurity-skills-library]]
- [[ai-security-tools]]
- [[agent-skill-management]]
- [[progressive-disclosure]]

## Original excerpts

> "Existing security tool repos give you wordlists, payloads, or exploit code. None of them give an AI agent the structured decision-making workflow a senior analyst follows."

> "Without these skills, the agent guesses at tool commands and misses critical steps. With them, it follows the same playbook a senior DFIR analyst would use."